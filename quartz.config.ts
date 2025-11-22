import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 Configuration
 *
 * See https://quartz.jzhao.xyz/configuration for more information.
 */
const config: QuartzConfig = {
  configuration: {
    // [MODIFICA] Titolo del sito aggiornato
    pageTitle: "Simone Testino",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: {
      provider: "plausible",
    },
    locale: "en-US",
    baseUrl: "https://simonetestino.pages.dev",
    // [CORREZIONE] Path del contenuto (non toccare se non hai cambiato la configurazione)
    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Tinos",
        body: "Tinos",
        code: "JetBrains Mono",
      },
      colors: {
        // Desaturated Monochrome - Near-black/white with subtle blue
        lightMode: {
          light: "#FAFAFA",     // Sfondo principale (Near-white)
          lightgray: "#F0F0F0", // Sfondo per sidebar/blocchi
          gray: "#D8D8D8",       // Bordo/Linee (very light gray)
          darkgray: "#5A5A5A",   // Testo secondario (medium gray)
          dark: "#0A0A0A",       // Testo principale (Near-black)
          // [MODIFICA]: Link e accenti (Very desaturated dark blue-gray)
          secondary: "#3B4A5A",
          // [MODIFICA]: Accenti secondari (Lighter desaturated blue-gray)
          tertiary: "#6B7A8A",
          highlight: "rgba(59, 74, 90, 0.08)",
          textHighlight: "#fff23688",
        },
        // Colori scuri (Sfondo scuro, Testo chiaro)
        darkMode: {
          light: "#0A0A0A",     // Sfondo principale (Near-black)
          lightgray: "#1A1A1A", // Sfondo sidebar/blocchi
          gray: "#2A2A2A",       // Bordo/Linee
          darkgray: "#A0A0A0",   // Testo secondario
          dark: "#F0F0F0",       // Testo principale (Near-white)
          // [MODIFICA]: Link e accenti (Light desaturated blue-gray)
          secondary: "#A5B5C5",
          // [MODIFICA]: Accenti secondari (Slightly darker)
          tertiary: "#8595A5",
          highlight: "rgba(165, 181, 197, 0.12)",
          textHighlight: "#b3aa0288",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [
      Plugin.RemoveDrafts(),
    ],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      // Comment out CustomOgImages to speed up build time
      Plugin.CustomOgImages(),
    ],
  },
}

export default config