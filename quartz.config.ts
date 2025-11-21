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
        header: "Libre Baskerville",
        body: "Lora",
        code: "JetBrains Mono",
      },
      colors: {
        // Colori chiari (Sfondo bianco, Testo scuro)
        lightMode: {
          light: "#faf9f6",     // Sfondo principale (Bianco Sporco / Eggshell)
          lightgray: "#e2e8f0", // Sfondo per sidebar/blocchi (Grigio Soft)
          gray: "#a0aec0",       // Bordo/Linee
          darkgray: "#4a5568",   // Testo secondario (Blu-Grigio Scuro)
          dark: "#2d3748",       // Testo principale (Blu-Nero Soft)
          // [MODIFICA]: Link e accenti (Blu-Grigio Desaturato)
          secondary: "#4a5568",
          // [MODIFICA]: Accenti secondari (Blu-Grigio Chiaro)
          tertiary: "#718096",
          highlight: "rgba(74, 85, 104, 0.05)",
          textHighlight: "#fff23688",
        },
        // Colori scuri (Sfondo scuro, Testo chiaro)
        darkMode: {
          light: "#1a202c",     // Sfondo principale (Blu Notte Scuro Soft)
          lightgray: "#2d3748", // Sfondo sidebar/blocchi
          gray: "#4a5568",       // Bordo/Linee
          darkgray: "#cbd5e0",   // Testo secondario
          dark: "#edf2f7",       // Testo principale
          // [MODIFICA]: Link e accenti (Grigio-Blu Muted)
          secondary: "#a0aec0",
          // [MODIFICA]: Accenti secondari
          tertiary: "#718096",
          highlight: "rgba(160, 174, 192, 0.1)",
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