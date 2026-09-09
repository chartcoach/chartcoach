import babelConfig from "./babel.config.json" with { type: "json" };

export default {
  plugins: {
    "@stylexjs/postcss-plugin": {
      include: ["app/**/*.{ts,tsx}", "components/**/*.{ts,tsx}"],
      babelConfig: {
        babelrc: false,
        configFile: false,
        parserOpts: { plugins: ["typescript", "jsx"] },
        plugins: babelConfig.plugins,
      },
      useCSSLayers: true,
    },
    // Autoprefixer treats selector() feature queries as declarations.
    autoprefixer: { supports: false },
  },
};
