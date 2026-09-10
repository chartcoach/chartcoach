import type { EveDynamicToolPart } from "eve/react";
import {
  BookOpen,
  ChartNoAxesCombined,
  ChevronRight,
  Combine,
  Database,
  Search,
  MessagesSquare,
  TableProperties,
  TextSearch,
  Waypoints,
  Wrench,
} from "lucide-react";
import type { ReactNode } from "react";
import { z } from "zod";
import {
  parseTool,
  describeOutput,
  readOutput,
  searchOutput,
  sqlOutput,
} from "../../chat/tool-output";
import * as stylex from "@stylexjs/stylex";
import { disclosureScope } from "../ui/tokens.stylex";
import { styles } from "./tool-activity.styles";
import { ui } from "../ui/ui";
import { modes, workflowSchema } from "../../shared/workflow";

const skillLabels = {
  visfeedback: { label: "Reviewing chart", icon: ChartNoAxesCombined },
  visrec: { label: "Planning a chart", icon: ChartNoAxesCombined },
  discuss: { label: "Comparing choices", icon: MessagesSquare },
};
const skillInput = z.object({ skill: workflowSchema });

export function skillActivity(part: EveDynamicToolPart) {
  if (part.toolName !== "load_skill") return undefined;
  const workflow = skillInput.safeParse(part.input);
  if (!workflow.success)
    return {
      label: "Loading guidance",
      icon: BookOpen,
      title: "Guidance",
      description: "Preparing instructions for this request.",
    };
  const mode = modes[workflow.data.skill];
  return { ...skillLabels[workflow.data.skill], title: mode.label, description: mode.description };
}

const searchMethods = {
  vector: { label: "Vector search", icon: Waypoints },
  keyword: { label: "Keyword search", icon: TextSearch },
  hybrid: { label: "Hybrid search", icon: Combine },
};
const toolKinds = new Map([
  ["search_guidelines", { label: "Search guidelines", icon: Search }],
  ["read_guidelines", { label: "Read guidelines and sources", icon: BookOpen }],
  ["query_catalog", { label: "Query catalog", icon: Database }],
  ["describe_catalog", { label: "Explore catalog structure", icon: TableProperties }],
]);

function toolStatus(part: EveDynamicToolPart, stopped: boolean, failed: boolean) {
  if (part.state === "output-error" || part.state === "output-denied") return "Failed";
  if (part.state === "output-available" && !part.partial) return "complete";
  if (failed) return "Failed";
  return stopped ? "Stopped" : "Working";
}

function ToolInput({
  query,
  sql,
  ids,
  raw,
}: {
  query?: string;
  sql?: string;
  ids?: string[];
  raw: unknown;
}) {
  if (sql !== undefined)
    return (
      <>
        <h3 {...stylex.props(styles.heading)}>SQL query</h3>
        <pre {...stylex.props(ui.mono, styles.pre)}>
          <code>{sql}</code>
        </pre>
      </>
    );
  if (query !== undefined)
    return (
      <>
        <h3 {...stylex.props(styles.heading)}>Search query</h3>
        <p {...stylex.props(styles.paragraph, styles.foreground)}>{query}</p>
      </>
    );
  if (ids)
    return (
      <>
        <h3 {...stylex.props(styles.heading)}>Requested guidelines</h3>
        <ul {...stylex.props(ui.mono, styles.pre, styles.list)}>
          {Array.from(new Set(ids)).map((id) => (
            <li key={id}>{id}</li>
          ))}
        </ul>
      </>
    );
  return (
    <>
      <h3 {...stylex.props(styles.heading)}>Input</h3>
      <pre {...stylex.props(ui.mono, styles.pre)}>
        {JSON.stringify(raw, null, 2) ?? "Input is being prepared."}
      </pre>
    </>
  );
}

function SourceLink({
  url,
  doi,
  children,
}: {
  url?: string | null;
  doi?: string | null;
  children: ReactNode;
}) {
  const href =
    url && /^https?:\/\//i.test(url)
      ? url
      : doi
        ? `https://doi.org/${encodeURIComponent(doi)}`
        : undefined;
  return href ? (
    <a
      {...stylex.props(ui.focus, styles.link)}
      href={href}
      target="_blank"
      rel="noopener noreferrer"
    >
      {children}
    </a>
  ) : (
    <>{children}</>
  );
}

function SearchResults({ search }: { search: z.infer<typeof searchOutput> }) {
  const { label, icon: MethodIcon } = searchMethods[search.method];
  return (
    <>
      <div {...stylex.props(styles.method)}>
        <MethodIcon {...stylex.props(ui.icon, styles.methodIcon)} size={16} aria-hidden="true" />
        <span>{label}</span>
      </div>
      <dl {...stylex.props(styles.config)}>
        {search.ranking && search.ranking !== search.metric ? (
          <>
            <dt>Ranking</dt>
            <dd {...stylex.props(styles.configValue)}>{search.ranking}</dd>
          </>
        ) : null}
        {search.model ? (
          <>
            <dt>Embedding model</dt>
            <dd {...stylex.props(styles.configValue)}>{search.model}</dd>
          </>
        ) : null}
        {search.metric ? (
          <>
            <dt>Distance metric</dt>
            <dd {...stylex.props(styles.configValue)}>{search.metric}</dd>
          </>
        ) : null}
        {search.dimensions !== undefined ? (
          <>
            <dt>Dimensions</dt>
            <dd {...stylex.props(styles.configValue)}>{search.dimensions}</dd>
          </>
        ) : null}
        {search.profile ? (
          <>
            <dt>Index profile</dt>
            <dd {...stylex.props(styles.configValue)}>{search.profile}</dd>
          </>
        ) : null}
      </dl>
      <h3 {...stylex.props(styles.heading)}>{`Search matches (${search.matches.length})`}</h3>
      <ul {...stylex.props(styles.list, styles.results)}>
        {search.matches.map((match) => (
          <li key={match.id}>
            <p {...stylex.props(styles.paragraph, styles.resultTitle)}>{match.title}</p>
            <p {...stylex.props(styles.paragraph)}>{match.description}</p>
          </li>
        ))}
      </ul>
    </>
  );
}

function ToolResults({
  search,
  read,
  sqlResult,
  description,
  output,
}: {
  search?: z.infer<typeof searchOutput>;
  read?: z.infer<typeof readOutput>;
  sqlResult?: z.infer<typeof sqlOutput>;
  description?: z.infer<typeof describeOutput>;
  output: unknown;
}) {
  if (search) return <SearchResults search={search} />;
  if (description)
    return (
      <>
        <div {...stylex.props(styles.method)}>
          <Database {...stylex.props(ui.icon, styles.methodIcon)} size={16} aria-hidden="true" />
          <span>Catalog tables · DuckDB</span>
        </div>
        {description.tables.map((table) => (
          <section key={table.name} {...stylex.props(styles.schema)}>
            <h3 {...stylex.props(styles.heading, styles.schemaHeading)}>
              <code {...stylex.props(ui.mono)}>{table.name}</code>
              <span {...stylex.props(styles.schemaCount)}>
                {table.rows.toLocaleString("en")} rows
              </span>
            </h3>
            <dl {...stylex.props(styles.schemaList)}>
              {table.columns.map((column) => (
                <div key={column.name} {...stylex.props(styles.schemaRow)}>
                  <dt>
                    <code {...stylex.props(ui.mono)}>{column.name}</code>
                  </dt>
                  <dd {...stylex.props(styles.schemaValue)}>{column.type}</dd>
                </div>
              ))}
            </dl>
          </section>
        ))}
        <dl {...stylex.props(styles.config)}>
          <dt>Label families</dt>
          <dd {...stylex.props(styles.configValue)}>
            {description.label_families.map((family) => family.name).join(", ")}
          </dd>
          <dt>Section roles</dt>
          <dd {...stylex.props(styles.configValue)}>
            {description.section_roles.map((role) => role.name).join(", ")}
          </dd>
          <dt>Index profiles</dt>
          <dd {...stylex.props(styles.configValue)}>{description.profiles.join(", ")}</dd>
          <dt>Query limits</dt>
          <dd {...stylex.props(styles.configValue)}>
            {description.limits.default_rows} rows by default, up to {description.limits.max_rows}.{" "}
            {description.limits.timeout_ms / 1000} second timeout.
          </dd>
        </dl>
      </>
    );
  if (sqlResult)
    return (
      <>
        <div {...stylex.props(styles.method)}>
          <Database {...stylex.props(ui.icon, styles.methodIcon)} size={16} aria-hidden="true" />
          <span>SQL · DuckDB</span>
        </div>
        <h3 {...stylex.props(styles.heading)}>
          {sqlResult.truncated
            ? `First ${sqlResult.row_count} rows`
            : `${sqlResult.row_count} ${sqlResult.row_count === 1 ? "row" : "rows"}`}
        </h3>
        <div
          {...stylex.props(ui.focus, styles.tableScroll)}
          role="region"
          aria-label="SQL results"
          tabIndex={0}
        >
          <table {...stylex.props(styles.table)}>
            <thead>
              <tr>
                {sqlResult.columns.map((column, index) => (
                  <th
                    key={`${column.name}:${index}`}
                    {...stylex.props(styles.cell, styles.headerCell)}
                    scope="col"
                  >
                    {column.name}
                    <span {...stylex.props(styles.columnType)}>{column.type}</span>
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {sqlResult.rows.map((row, index) => (
                <tr key={index}>
                  {row.map((value, column) => (
                    <td key={column} {...stylex.props(styles.cell, styles.valueCell)}>
                      {value === null ? <span {...stylex.props(styles.muted)}>NULL</span> : value}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        {sqlResult.truncated ? (
          <p {...stylex.props(styles.paragraph)}>
            Results are limited to {sqlResult.limit} rows. Narrow the query to inspect more specific
            entries.
          </p>
        ) : null}
      </>
    );
  if (read)
    return (
      <>
        <h3 {...stylex.props(styles.heading)}>Guidelines read</h3>
        <ul {...stylex.props(styles.list, styles.results)}>
          {Array.from(new Map(read.guidelines.map((item) => [item.id, item])).values()).map(
            (item) => {
              const citation = read.citations.find((entry) => entry.id === item.id);
              return (
                <li key={item.id}>
                  <p {...stylex.props(styles.paragraph, styles.resultTitle)}>
                    <SourceLink url={citation?.url}>{item.title}</SourceLink>
                  </p>
                  <p {...stylex.props(styles.paragraph)}>{item.description}</p>
                  {citation?.sources.length ? (
                    <ul {...stylex.props(styles.list, styles.sources)}>
                      {citation.sources.map((source) => (
                        <li key={source.reference_id}>
                          <SourceLink url={source.url} doi={source.doi}>
                            {source.citation}
                          </SourceLink>
                        </li>
                      ))}
                    </ul>
                  ) : null}
                </li>
              );
            },
          )}
        </ul>
      </>
    );
  return (
    <>
      <h3 {...stylex.props(styles.heading)}>Result</h3>
      <pre {...stylex.props(ui.mono, styles.pre)}>{JSON.stringify(output, null, 2)}</pre>
    </>
  );
}

export function ToolActivity({
  part,
  stopped,
  failed,
}: {
  part: EveDynamicToolPart;
  stopped: boolean;
  failed: boolean;
}) {
  const status = toolStatus(part, stopped, failed);
  const complete = status === "complete";
  const toolFailed = status === "Failed";
  const skill = skillActivity(part);
  const {
    query,
    sql,
    ids,
    search,
    read,
    sqlResult,
    description,
    method: inputMethod,
  } = parseTool(part);
  const context =
    query ?? sql ?? read?.guidelines.map((item) => item.title).join(" · ") ?? ids?.join(" · ");
  const kind = toolKinds.get(part.toolName);
  const method = search?.method ?? inputMethod;
  const Icon =
    part.toolName === "search_guidelines" && method
      ? searchMethods[method].icon
      : (skill?.icon ?? kind?.icon ?? Wrench);
  const label = skill?.label ?? kind?.label ?? part.toolName;

  return (
    <details {...stylex.props(disclosureScope, styles.root)}>
      <summary {...stylex.props(ui.focus, styles.summary)}>
        <Icon {...stylex.props(ui.icon)} size={14} aria-hidden="true" />
        <span {...stylex.props(styles.label)}>
          <span>{label}</span>
          {context ? <span {...stylex.props(styles.context)}>{context}</span> : null}
        </span>
        {!complete ? <span {...stylex.props(styles.state)}>{status}</span> : null}
        <ChevronRight {...stylex.props(ui.chevron, styles.chevron)} size={14} aria-hidden="true" />
      </summary>
      <div {...stylex.props(styles.details)}>
        {skill ? (
          <>
            <h3 {...stylex.props(styles.heading)}>{skill.title}</h3>
            <p {...stylex.props(styles.paragraph)}>{skill.description}</p>
          </>
        ) : !read && part.toolName !== "describe_catalog" ? (
          <ToolInput query={query} sql={sql} ids={ids} raw={part.input} />
        ) : null}
        {complete && !skill ? (
          <ToolResults
            search={search}
            read={read}
            sqlResult={sqlResult}
            description={description}
            output={part.output}
          />
        ) : null}
        {part.state === "output-error" ? (
          <p {...stylex.props(ui.error, styles.paragraph)}>{part.errorText}</p>
        ) : null}
        {part.state === "output-denied" ? (
          <p {...stylex.props(styles.paragraph)}>The tool request was denied.</p>
        ) : null}
        {!complete && !toolFailed ? (
          <p {...stylex.props(styles.paragraph)}>
            {stopped ? "Stopped before results arrived." : "Waiting for results."}
          </p>
        ) : null}
      </div>
    </details>
  );
}
