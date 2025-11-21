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
        header: "Tinos",
        body: "Tinos",
        code: "JetBrains Mono",
      },
      colors: {
        // Colori chiari (Sfondo bianco, Testo scuro)
        lightMode: {
          light: "#ffffff",     // Sfondo principale (Bianco Puro)
          lightgray: "#f0f0f0", // Sfondo per sidebar/blocchi (Grigio Chiarissimo)
          gray: "#d0d0d0",       // Bordo/Linee
          darkgray: "#606060",   // Testo secondario (Grigio Medio)
          dark: "#000000",       // Testo principale (Nero)
          // [MODIFICA]: Link e accenti (Nero)
          secondary: "#000000",
          // [MODIFICA]: Accenti secondari (Grigio Scuro)
          tertiary: "#606060",
          highlight: "rgba(0, 0, 0, 0.05)",
          textHighlight: "#fff23688",
        },
        // Colori scuri (Sfondo scuro, Testo chiaro)
        darkMode: {
          light: "#000000",     // Sfondo principale (Nero Puro)
          lightgray: "#202020", // Sfondo sidebar/blocchi
          gray: "#404040",       // Bordo/Linee
          darkgray: "#a0a0a0",   // Testo secondario
          dark: "#ffffff",       // Testo principale (Bianco)
          // [MODIFICA]: Link e accenti (Bianco)
          secondary: "#ffffff",
          // [MODIFICA]: Accenti secondari
          tertiary: "#a0a0a0",
          highlight: "rgba(255, 255, 255, 0.1)",
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