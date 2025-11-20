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
    pageTitle: "ColivingLiguria",
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
        header: "Schibsted Grotesk",
        body: "Source Sans Pro",
        code: "IBM Plex Mono",
      },
      colors: {
        // Colori chiari (Sfondo bianco, Testo scuro)
        lightMode: {
          light: "#faf8f8",     // Sfondo principale (Bianco sporco)
          lightgray: "#e5e5e5", // Sfondo per sidebar/blocchi
          gray: "#b8b8b8",       // Bordo/Linee
          darkgray: "#4e4e4e",   // Testo
          dark: "#2b2b2b",       // Testo principale
          // [MODIFICA]: Link e accenti (Verde Muschio)
          secondary: "#4a7c59",
          // [MODIFICA]: Accenti secondari (Marrone Beige/Terra)
          tertiary: "#c4a381",
          highlight: "rgba(143, 159, 169, 0.15)",
          textHighlight: "#fff23688",
        },
        // Colori scuri (Sfondo scuro, Testo chiaro)
        darkMode: {
          light: "#161618",     // Sfondo principale scuro
          lightgray: "#393639", // Sfondo sidebar/blocchi
          gray: "#646464",       // Bordo/Linee
          darkgray: "#d4d4d4",   // Testo
          dark: "#ebebec",       // Testo principale
          // [MODIFICA]: Link e accenti (Verde Oliva Chiaro)
          secondary: "#a4b490",
          // [MODIFICA]: Accenti secondari (Marrone Terra Chiaro)
          tertiary: "#c4a381",
          highlight: "rgba(143, 159, 169, 0.15)",
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