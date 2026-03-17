---
title: "gstack: Y Combinator CEO's AI Programming Team OS Hits 18K Stars in One Week"
date: 2026-03-17
author: "Tech Observer Team"
description: "Deep dive into gstack — the open-source Claude Code skill set by Y Combinator CEO Garry Tan that transforms a single AI assistant into a team of specialized experts."
categories: ["Artificial Intelligence", "Developer Tools", "Open Source"]
tags: ["AI Coding", "Claude Code", "Open Source", "Y Combinator", "gstack", "Developer Productivity"]
cover:
    image: "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=1200"
    alt: "AI Programming Tools"
---

# gstack: Y Combinator CEO's AI Programming Team OS

![AI Programming Tools](https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=1200)

This week's most talked-about open source project on GitHub isn't a new framework or a new model — it's a skill set that lets your AI coding assistant **switch cognitive modes on demand**.

[gstack](https://github.com/garrytan/gstack), open-sourced by Y Combinator President & CEO **Garry Tan**, accumulated over **18,000 stars** in just one week, making it one of the fastest-growing projects on GitHub this week.

## The Problem It Solves

![Developer Workflow](https://images.unsplash.com/photo-1461749280684-dccba630e2f6?w=1200)

Anyone who has used Claude Code or similar AI coding tools knows the frustration: **the AI is too "one-size-fits-all"**.

Ask it to do product planning and it starts writing code. Ask it for a code review and it starts brainstorming new features. Planning, reviewing, shipping, testing — these require completely different mindsets, but AI always responds in the same mushy generic mode.

Garry Tan's solution: **give the AI different "brains" and switch between them on demand.**

## 12 Expert Roles, Full Development Lifecycle

![Software Development](https://images.unsplash.com/photo-1504639725590-34d0984388bd?w=1200)

gstack provides 12 carefully designed slash commands, each corresponding to a specialist role:

| Command | Role | Core Capability |
|---------|------|----------------|
| `/plan-ceo-review` | Founder / CEO | Look beyond the literal request, find the real product |
| `/plan-eng-review` | Eng Manager | Lock in architecture, data flow, edge cases, test matrix |
| `/plan-design-review` | Senior Designer | 80-item design audit, AI Slop detection |
| `/review` | Paranoid Staff Engineer | Find bugs that pass CI but blow up in production |
| `/ship` | Release Engineer | Sync main, run tests, push, open PR — all in one go |
| `/browse` | QA Engineer | Give AI eyes to click through and test your app |
| `/qa` | QA Lead | Read git diff, auto-identify affected pages and test them |
| `/retro` | Engineering Manager | Analyze commit history, generate team retrospectives |
| `/document-release` | Technical Writer | Auto-update README and architecture docs post-release |

## The Killer Feature: Giving AI Eyes

![Browser Automation](https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200)

The most groundbreaking feature in gstack is `/browse` and `/qa`.

The biggest blind spot of traditional AI coding assistants: **they can't see what your app looks like**. They have to guess about UI state, auth flows, and page layouts.

gstack solves this with a built-in persistent Chromium instance powered by Playwright:

```
You:   /qa

Claude: Analyzing branch diff against main...
        12 files changed: 3 controllers, 2 views, 4 services
        Affected routes: /listings/new, /listings/:id, /api/listings
        Detected app running on localhost:3000

        [Tests each affected page — navigates, fills forms, clicks buttons,
        screenshots, checks console errors]

        QA Report: 3 routes tested, all working.
        No console errors. No regressions on adjacent pages.
```

**18 tool calls, ~60 seconds, a complete QA pass.**

## AI Slop Detection: Does Your Site Look AI-Generated?

![Website Design Review](https://images.unsplash.com/photo-1467232004584-a241de8bcf5d?w=1200)

`/plan-design-review` includes a feature that hits close to home for many developers: **AI Slop Detection**.

It identifies 10 telltale signs of AI-generated websites:
- Blue-to-purple gradient heroes
- 3-column icon grids
- Uniform bubbly border-radius on everything
- Centered text on every section
- Decorative floating blobs in the background

```
Claude: Design Score: C  |  AI Slop Score: D

        "The site communicates generic SaaS energy."
        "The hero uses a blue-to-purple gradient with a 3-column
         feature grid — the single most recognizable AI-generated layout."
        "If I had to describe this in one word: template."
```

## One Person, Ten Parallel AI Agents

![Parallel Development](https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1200)

Garry Tan describes his own workflow in the README:

> "This is the setup I use. One person, ten parallel agents, each with the right cognitive mode for its task. That is not incremental improvement. That is a different way of building software."

Combined with [Conductor](https://conductor.build), you can run multiple Claude Code sessions simultaneously:
- One session running `/qa` on staging
- Another doing `/review` on a PR
- A third implementing a feature
- Seven more working on other branches

Each workspace gets its own isolated browser instance — no port collisions, no shared state.

## Installation

Just paste one command into Claude Code:

```
Install gstack: run `git clone https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup`
```

Claude handles the rest automatically.

**Requirements:** Claude Code, Git, Bun v1.0+

## Why This Project Matters

gstack's viral success isn't just about its features — it represents a new AI programming paradigm:

1. **Specialization over generalization** — different tasks need different mindsets
2. **AI needs perception** — an AI that can "see" your app is a complete AI
3. **Workflow is the product** — great AI tools integrate into your flow, not interrupt it
4. **Solo teams become viable** — with AI expert roles, individual developers can have full team capabilities

As Garry Tan puts it: **"This is not a prompt pack for beginners. It is an operating system for people who ship."**

## References

- [gstack GitHub Repository](https://github.com/garrytan/gstack)
- [Garry Tan on X](https://x.com/garrytan)
- [Y Combinator](https://www.ycombinator.com/)
- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)

---