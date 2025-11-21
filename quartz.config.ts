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
          light: "#ffffff",     // Sfondo principale (Bianco Puro)
          lightgray: "#f5f5f5", // Sfondo per sidebar/blocchi (Grigio Chiarissimo)
          gray: "#e0e0e0",       // Bordo/Linee
          darkgray: "#4e4e4e",   // Testo secondario
          dark: "#222222",       // Testo principale
          // [MODIFICA]: Link e accenti (Blu Scuro Profondo)
          secondary: "#001f3f",
          // [MODIFICA]: Accenti secondari (Blu Notte)
          tertiary: "#003366",
          highlight: "rgba(0, 31, 63, 0.05)",
          textHighlight: "#fff23688",
        },
        // Colori scuri (Sfondo scuro, Testo chiaro)
        darkMode: {
          light: "#050505",     // Sfondo principale (Quasi Nero)
          lightgray: "#1f2833", // Sfondo sidebar/blocchi
          gray: "#3a3a3a",       // Bordo/Linee
          darkgray: "#a0a0a0",   // Testo secondario
          dark: "#e0e0e0",       // Testo principale
          // [MODIFICA]: Link e accenti (Blu Muted / Grigio Bluastro)
          secondary: "#64ffda", // Un tocco di colore minimale (Ciano Muted) per contrasto su scuro
          // [MODIFICA]: Accenti secondari
          tertiary: "#3a506b",
          highlight: "rgba(100, 255, 218, 0.1)",
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