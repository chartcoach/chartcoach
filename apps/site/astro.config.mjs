// @ts-check
import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";
import { fileURLToPath } from "node:url";

// https://astro.build/config
export default defineConfig({
  vite: {
    resolve: {
      alias: {
        "@chartcoach/site": fileURLToPath(new URL("./src", import.meta.url)),
      },
    },
  },
  integrations: [
    starlight({
      title: "Chart Coach",
      customCss: ["./src/styles/custom.css"],
      social: [{ icon: "github", label: "GitHub", href: "http://github.com/peter-gy/chartcoach" }],
      components: {
        TableOfContents: "./src/components/starlight/TableOfContents.astro",
        MobileTableOfContents: "./src/components/starlight/MobileTableOfContents.astro",
      },
      sidebar: [
        {
          label: "Start",
          items: [
            { label: "Overview", link: "/" },
            { label: "Catalog structure", link: "/catalog/" },
            { label: "Labels & filters", link: "/labels/" },
            { label: "About", link: "/about/" },
          ],
        },
        {
          label: "Catalog",
          items: [{ label: "Guidelines", link: "/guidelines/" }],
        },
      ],
    }),
  ],
});
