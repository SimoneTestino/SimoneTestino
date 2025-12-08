---
date: 2025-12-08
draft: false
tags: [Documentation, Markdown]
---

# Markdown Style Guide

Standards for creating content in this Quartz site.

---

## Frontmatter

Every file must start with YAML frontmatter:

```yaml
---
date: 2025-12-08
draft: false
tags: [Category, Topic]
---
```

**Required fields:**
- `date`: Creation or update date (YYYY-MM-DD)
- `draft`: `false` for published, `true` for WIP

**Optional:**
- `tags`: Categories (English only)
- `title`: Override filename as title

---

## Headers

- **H1 (`#`)**: Page title (usually from filename)
- **H2 (`##`)**: Main sections
- **H3 (`###`)**: Subsections

**Rules:**
- No numbered headers (use `## Introduction` not `## 1. Introduction`)
- Title Case for English headers

---

## Links

### Internal Links (Wikilinks)

```markdown
[[Page Name]]
[[Folder/Page Name|Display Text]]
```

### External Links

```markdown
[Display Text](https://example.com)
```

---

## Callouts

Use Obsidian-style callouts for emphasis:

```markdown
> [!NOTE]
> General information

> [!TIP]
> Helpful advice

> [!WARNING]
> Important caution

> [!IMPORTANT]
> Critical information
```

---

## Writing Style

Balance between:

1. **Discursive**: Full sentences for context and explanation
2. **Schematic**: Lists and tables for specifications

**Example:**

> *Discursive*: "This project combines aerospace engineering with advanced LED technology."
> 
> *Schematic*:
> - **Output**: 100,000 lumens
> - **Weight**: < 2 kg
> - **Cost**: €750

---

## File Organization

| Folder | Content Type |
|:-------|:-------------|
| `Academia/` | Academic work, papers, notes |
| `Luna/` | Luna project documentation |
| `System/` | Website utilities, documentation |
| `Personal Finance/` | Financial documentation |
