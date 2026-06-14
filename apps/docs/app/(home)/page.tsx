import Link from "next/link";

export default function HomePage() {
  return (
    <main className="mx-auto flex min-h-[70vh] w-full max-w-3xl flex-1 flex-col justify-center px-6 py-20">
      <p className="mb-4 text-sm font-medium text-fd-muted-foreground">
        ChartCoach documentation
      </p>
      <h1 className="text-balance text-4xl font-semibold tracking-normal md:text-5xl">
        Inspect the Guideline Catalog and the packages that load it.
      </h1>
      <p className="mt-6 max-w-2xl text-pretty text-base leading-7 text-fd-muted-foreground">
        The docs describe the catalog shape, the loader packages, and the commands
        that validate ChartCoach data.
      </p>
      <div className="mt-8 flex flex-wrap gap-3">
        <Link
          href="/docs"
          className="inline-flex min-h-10 items-center rounded-md bg-fd-primary px-4 text-sm font-medium text-fd-primary-foreground"
        >
          Open docs
        </Link>
        <Link
          href="/docs/catalog"
          className="inline-flex min-h-10 items-center rounded-md border px-4 text-sm font-medium"
        >
          Catalog contract
        </Link>
      </div>
    </main>
  );
}
