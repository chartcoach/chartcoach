export const brandAssetBasePath = "/brand" as const;

export const brandLogoPath = `${brandAssetBasePath}/chartcoach-horizontal.svg` as const;
export const brandLogoWhitePath =
  `${brandAssetBasePath}/chartcoach-horizontal-white.svg` as const;
export const brandSquareLightPath =
  `${brandAssetBasePath}/chartcoach-square-light.svg` as const;
export const brandSquareMutedPath =
  `${brandAssetBasePath}/chartcoach-square-muted.svg` as const;
export const brandSquareDarkPath =
  `${brandAssetBasePath}/chartcoach-square-dark.svg` as const;
export const brandSquareAccentPath =
  `${brandAssetBasePath}/chartcoach-square-accent.svg` as const;
export const iconPath = `${brandAssetBasePath}/icon.svg` as const;
export const iconWhitePath = `${brandAssetBasePath}/icon-white.svg` as const;
export const faviconPath = `${brandAssetBasePath}/favicon.svg` as const;
export const faviconPngPath = `${brandAssetBasePath}/favicon.png` as const;
export const appIconLightPath = `${brandAssetBasePath}/app-icon-light.svg` as const;
export const appIconDarkPath = `${brandAssetBasePath}/app-icon-dark.svg` as const;
export const appIconLightPngPath = `${brandAssetBasePath}/app-icon-light.png` as const;
export const appIconDarkPngPath = `${brandAssetBasePath}/app-icon-dark.png` as const;
export const appleTouchIconPath = appIconLightPngPath;

export const brandAssets = {
  logo: brandLogoPath,
  logoWhite: brandLogoWhitePath,
  squareLight: brandSquareLightPath,
  squareMuted: brandSquareMutedPath,
  squareDark: brandSquareDarkPath,
  squareAccent: brandSquareAccentPath,
  icon: iconPath,
  iconWhite: iconWhitePath,
  favicon: faviconPath,
  faviconPng: faviconPngPath,
  appIconLight: appIconLightPath,
  appIconDark: appIconDarkPath,
  appIconLightPng: appIconLightPngPath,
  appIconDarkPng: appIconDarkPngPath,
  appleTouchIcon: appleTouchIconPath,
} as const;

export type BrandAssetName = keyof typeof brandAssets;
