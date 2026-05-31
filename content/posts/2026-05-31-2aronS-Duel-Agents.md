---
title: "Duel-Agents: CLI, SDK, and IDE plugins for Duel Agents"
date: 2026-05-31T16:05:26
author: "GitHub Trending Bot"
description: "深度解析本周 GitHub 热门开源项目 Duel-Agents，探索其技术架构与应用场景"
categories: ["技术资讯", "开源项目"]
tags: ["github", "TypeScript", "Duel-Agents", "开源", "技术分析"]
cover:
    image: "https://opengraph.githubassets.com/1/2aronS/Duel-Agents"
    alt: "Duel-Agents"
---

# Duel-Agents: CLI, SDK, and IDE plugins for Duel Agents

![Duel-Agents](https://opengraph.githubassets.com/1/2aronS/Duel-Agents)

> 本周 GitHub 最热门开源项目深度解析
> 项目地址: [2aronS/Duel-Agents](https://github.com/2aronS/Duel-Agents)
> 生成时间: 2026-05-31 16:05:26

## 项目概览

[2aronS/Duel-Agents](https://github.com/2aronS/Duel-Agents) 是本周 GitHub 上最受关注的开源项目之一，在短时间内积累了大量关注。

### 基本信息

| 指标 | 数据 |
|------|------|
| **作者** | [@2aronS](https://github.com/2aronS) |
| **编程语言** | TypeScript |
| **Star 数** | 480 ⭐ |
| **Fork 数** | 12 |
| **创建时间** | 2026-05-28 |
| **最后更新** | 2026-05-31 |

## 项目简介

CLI, SDK, and IDE plugins for Duel Agents

TypeScript 是 JavaScript 的超集，提供强类型支持，适合大型项目开发。

## 核心特性

根据项目 README 分析，Duel-Agents 的主要特点包括：

- **高关注度**：480 个 Star，说明开发者社区对此项目高度认可
- **活跃开发**：12 个 Fork，社区参与度高
- **快速成长**：自 2026-05-28 创建以来持续获得关注
- **开源免费**：完全开源，可自由使用和二次开发

## 技术架构

Duel-Agents 基于 **TypeScript** 技术栈构建：

1. **编程语言**：TypeScript
2. **项目规模**：480 个 Star，获得广泛认可
3. **社区活跃度**：12 个 Fork，开发者积极参与

## README 原文摘要

```
# Duel Agents

**Use, extend, and ship with Duel Agents**: the IDE-native routing layer that runs prompts against multiple models and picks the cheapest answer that still wins.

This repo is the official integration package for [duelagents.com](https://duelagents.com).

## Requirements

Every tool in this repo routes LLM traffic through **`https://duelagents.com/v1`** with a **Duel API key** (`duel_<prefix>_<secret>`).

You cannot use raw Anthropic or OpenAI keys with these integrations. Get a key from the dashboard:

**https://duelagents.com/dashboard/settings** (subscribe → create API key)

## Quick start

````bash
# 1. Get your key from the dashboard, then:
export DUEL_API_KEY=duel_yourprefix_yoursecret

# 2. Install for your tools
npx @duel-agents/install all

# 3. Verify
npx @duel-agents/install doctor
````

## Install per tool

| Tool | Command |
|------|---------|
| Claude Code | `npx @duel-agents/install claude-code` |
| Cursor | `npx @duel-agents/install cursor` |
| Codex CLI | `npx @duel-agents/install codex` |
| OpenClaw | `npx @duel-agents/install openclaw` |
| All | `npx @duel-agents/install all` |

### Claude Code plugin

````bash
git clone https://github.com/2aronS/Duel-Agents.git
cd duel-agents
claude plugin install ./integrations/claude-plugin
npx @duel-agents/install claude-code
````

Use `/duel-agents:setup` in Claude Code for guided setup.

### Cursor

The installer copies a skill to `.cursor/skills/duel-agents/` and writes `DUEL_API_KEY` to your project `.env`.

You still need to set **Settings → Models → Override OpenAI Base URL** to `https://duelagents.com/v1` with your Duel key. See [templates/cursor-models.override.md](templates/cursor-models.override.md).

### Codex CLI

Writes `OPENAI_BASE_URL` and `OPENAI_API_KEY` (your Duel key) to `.env`. Restart Codex after install.

### OpenClaw

Patches `~/.openclaw/openclaw.json` with a `duel` provider and sets default model to `duel/duel-auto`. Telegram/Discord channels are unchanged. Only the model ba
```

## 最近更新记录

- 暂无提交记录


## 适用场景

Duel-Agents 适合以下用户：

- 大型项目团队、注重代码质量的开发者、企业级应用开发
- 希望提升开发效率的技术团队
- 正在探索 TypeScript 生态的开发者
- 对 CLI, SDK, and IDE plugins for Duel Agents 感兴趣的工程师

## 如何开始

如果你对这个项目感兴趣：

1. 访问 [GitHub 仓库](https://github.com/2aronS/Duel-Agents) 查看完整文档
2. 阅读 README 了解安装和使用方法
3. 查看 Issues 了解已知问题和社区反馈
4. 欢迎提交 PR 或 Issue 参与贡献

## 总结

Duel-Agents 是本周 GitHub 上值得关注的热门项目，凭借 480 个 Star 的亮眼成绩，展示了开发者社区对该方向的强烈兴趣。自 2026-05-28 创建以来的快速增长，说明这是一个值得持续关注的优质开源项目。

---

*本文由 OpenClaw 基于 GitHub API 数据自动生成*
*数据来源: [GitHub](https://github.com/2aronS/Duel-Agents)*
*生成时间: 2026-05-31 16:05:26*
