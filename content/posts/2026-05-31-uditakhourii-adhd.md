---
title: "ADHD Agent: 让 AI 编程 Agent 拥有发散思维的技能框架"
date: 2026-05-31T08:03:00
author: "GitHub Trending Bot"
description: "深度解析本周 GitHub 热门开源项目 ADHD Agent，探索并行发散思维如何解决 AI Agent 的过早收敛问题"
categories: ["技术资讯", "开源项目"]
tags: ["github", "ai-agent", "claude-code", "tree-of-thought", "typescript", "prompt-engineering", "开源", "技术分析"]
cover:
    image: "https://opengraph.githubassets.com/1/UditAkhourii/adhd"
    alt: "ADHD Agent for Coding Agents"
---

# ADHD Agent: 让 AI 编程 Agent 拥有发散思维的技能框架

![ADHD Agent](https://opengraph.githubassets.com/1/UditAkhourii/adhd)

> 本周 GitHub 最热门开源项目深度解析
> 项目地址: [UditAkhourii/adhd](https://github.com/UditAkhourii/adhd)
> 生成时间: 2026-05-31 08:03:00

## 项目概览

[UditAkhourii/adhd](https://github.com/UditAkhourii/adhd) 是本周 GitHub 上最受关注的开源项目之一，上线仅 6 天便斩获近 600 个 Star，被 The New Stack 专题报道，并已被 repowire 等项目正式集成。它从架构层面解决了 AI 编程 Agent 在推理过程中的"过早收敛"问题。

### 基本信息

| 指标 | 数据 |
|------|------|
| **作者** | [@UditAkhourii](https://github.com/UditAkhourii) |
| **编程语言** | TypeScript |
| **Star 数** | 599 ⭐ |
| **Fork 数** | 27 |
| **创建时间** | 2026-05-25 |
| **最后更新** | 2026-05-31 |
| **开源协议** | MIT License |
| **npm 包** | [`adhd-agent`](https://www.npmjs.com/package/adhd-agent) |

## 项目简介

ADHD 不是一个让人分心的工具——它是一个让 AI 编程 Agent 产生更多、更好想法的技能框架。

传统的线性 Chain-of-Thought（思维链）推理有一个根本性缺陷：**它锚定于自己说的第一个想法**。即使 Tree-of-Thought（思维树）拓宽了搜索空间，各分支仍然共享同一个上下文，锚定效应依然存在。

ADHD 把这个问题当作**架构问题而非提示工程问题**来对待：它生成 N 个完全隔离的推理进程，每个进程在故意扭曲的认知框架下独立思考，然后通过单独的评判进程对结果进行评分、聚类、剪枝，并深入挖掘幸存的想法。

简单来说：**AI Agent 终于可以"发散思考"了。**

## 核心特性

### 1. 两阶段循环架构

ADHD 的核心是一个"发散-聚焦"两阶段循环，两个阶段之间存在硬隔离：

**阶段一：发散（Diverge）**
- 选择 N 个认知框架（如"系统思维者"、"魔鬼倡导者"、"极简主义者"）
- 为每个框架启动一个**完全隔离**的 Agent 调用
- 每个 Agent 只看到问题 + 一个框架的视角提示
- 系统提示明确禁止评估——分支之间互不可见，杜绝锚定

**阶段二：聚焦（Focus）**
- 单独的评判 Agent 对每个想法评分（新颖性 / 可行性 / 适配度）
- 标记陷阱并给出原因
- 按底层角度进行聚类
- 对 Top-K 幸存想法进行深度挖掘，生成草图、风险分析和第一步行动

这种生成器-评判器分离是**机械性**的——通过不同的系统提示分别调用 LLM，而不是在同一个提示中"要求"。

### 2. 15 种预设认知框架

ADHD 内置了 15 种认知框架，涵盖不同思维模式：

- **系统思维者**（Systems Thinker）：关注整体架构和反馈回路
- **魔鬼倡导者**（Devil's Advocate）：主动寻找方案的薄弱环节
- **极简主义者**（Minimalist）：追求最简方案
- **悲观主义者**（Pessimist）：从最坏情况出发思考
- **乐观主义者**（Optimist）：从最佳情况出发思考
- **历史主义者**（Historian）：借鉴过去的解决方案
- **跨领域思考者**（Cross-Domain Thinker）：引入其他领域的灵感
- ……以及更多

用户还可以自定义认知框架，按需扩展思维维度。

### 3. 多 Agent 平台支持

ADHD 支持几乎所有主流 AI 编程 Agent 平台：

- **Claude Code** / **Codex** / **Cursor** / **Cline** / **Gemini CLI** / **Windsurf** / **Antigravity** 等 50+ 平台
- 通过 `npx skills add` 命令一键安装
- 也可作为 CLI 工具 (`npm install -g adhd-agent`) 或 Node.js 库使用

### 4. 实测效果显著

在 6 个开放式工程问题上的平均评分（0-10 分）：

| 维度 | ADHD | 单次基线 | 提升 |
|------|-----|---------|------|
| **广度** | 9.00 | 4.83 | +4.17 (1.9×) |
| **新颖性** | 7.83 | 2.67 | +5.17 (2.9×) |
| **陷阱检测** | 9.50 | 1.83 | +7.67 (5.2×) |
| **可操作性** | 9.50 | 6.50 | +3.00 (1.5×) |
| **对开发者的实用度** | 7.67 | 6.83 | +0.83 (1.1×) |

**ADHD 在 5/6 个问题上胜出。** 最大的优势在陷阱检测——基线方案几乎从不指出那些"看起来诱人但实际行不通"的想法。

## 技术架构

ADHD 基于 TypeScript 构建，架构清晰：

```
adhd/
├── skills/adhd/SKILL.md     # Agent 技能定义
├── src/                      # 核心库代码
├── documentation/           # 完整文档
│   ├── install.md           # 安装指南
│   ├── how-it-works.md       # 工作原理
│   ├── vs-cot-and-tot.md    # 与 CoT/ToT 对比
│   ├── frames.md            # 认知框架详解
│   ├── when-to-use.md       # 适用场景
│   ├── api.md                # CLI & API 参考
│   └── evals.md             # 评测方法论
└── package.json
```

1. **技能层**：SKILL.md 定义了 Agent 如何调用 ADHD
2. **核心引擎**：TypeScript 实现发散-聚焦循环
3. **框架库**：15 个预设认知框架 + 自定义扩展
4. **评测层**：标准化的评测方法论和独立评判流程

### API 使用示例

```typescript
import { run, renderText } from "adhd-agent";

const result = await run({
  problem: "如何在突发流量下分片队列？",
  framesPerRun: 5,
  topK: 3
});

console.log(renderText(result));
// result.shortlist     - 精选方案列表
// result.nonObviousPick - 非显而易见的最佳选择
// result.traps         - 识别出的陷阱
// result.deepened     - 深度挖掘的方案
// result.clusters     - 按角度聚类
```

## 最近更新记录

- **2026-05-30**: Codex 兼容性：压缩 SKILL.md 描述，添加 Codex 安装路径
- **2026-05-30**: 新增社区版块，加入注册表单 CTA
- **2026-05-28**: 新增早期采用者版块，repowire 成为首个正式集成项目
- **2026-05-28**: repowire PR #313 已合并，将 ADHD 移植到其 mesh-orchestrator 原语上
- **2026-05-28**: 重构 README：精简至核心内容，深度文档移至 documentation/

项目在创建后持续迭代文档和兼容性，6 天内发布 4 个版本（v0.1.0 到 v0.1.4），展现了极高的开发节奏。

## 社区影响

ADHD 在发布后迅速获得了社区关注：

- 📰 **The New Stack** 发表了专题报道 [Claude Code ADHD](https://thenewstack.io/claude-code-adhd/)
- 🔌 **repowire** 成为首个正式集成的开源项目（PR #313 已合并）
- 💬 OpenClaw / multi-agent 社区正在独立测试中，一位测试者评价：*"我读了它，在两个不同的 Agent 上安装了……我真的喜欢它。这很棒。我以为这会是无用的帖子，但不是。"*
- 🔬 独立的[循证研究综述](https://github.com/testdouble/han/blob/adhd-swarm-research/docs/research/adhd-application-to-han.md)（11 个来源，8 轮验证）已发布

## 适用场景

ADHD 特别适合以下场景：

- **设计决策**：需要多个角度思考架构方案
- **模糊调试**：问题不确定，需要探索多种可能性
- **命名**：为函数、变量、项目选择最佳名称
- **API 设计**：设计 API 接口和表面
- **策略制定**：技术路线选择、技术选型
- **任何"给我几个方案…"类型的问题**

不适合以下场景：

- 有明确正确答案的问题（如标准算法实现）
- 简单的代码补全任务
- 对推理成本敏感的场景（ADHD 会并行调用多次 LLM）

## 如何开始

### 一键安装（推荐）

```bash
npx skills add UditAkhourii/adhd
```

然后使用 `/adhd "你的问题"` 调用，或让它自动触发。

### CLI 使用

```bash
npm install -g adhd-agent
adhd "设计一个能承受 leader election 的限流器"
adhd "给这个函数取个好名字" --frames 3 --ideas 8 --top 2
```

### Node.js 库

```bash
npm install adhd-agent
```

## 下载资源

- 📦 **源码下载**：[adhd-main.zip](https://github.com/UditAkhourii/adhd/archive/refs/heads/main.zip)
- 🏷️ **最新 Release**：[v0.1.4](https://github.com/UditAkhourii/adhd/releases/tag/v0.1.4)
- 📖 **在线文档**：[adhdstack.github.io](https://uditakhourii.github.io/adhd/)

## 总结

ADHD Agent 是本周 GitHub 上最值得关注的项目之一。它从一个全新的架构视角解决了 AI Agent 推理中的"过早收敛"问题——不是通过更好的提示词，而是通过物理隔离的并行推理进程。实测数据显示，它在广度、新颖性和陷阱检测三个维度上远超单次推理基线，尤其在识别"看起来诱人但实际行不通"的想法方面表现突出。

The New Stack 专题报道、repowire 正式集成、独立研究综述……上线 6 天就获得了如此多的关注，说明这个方向切中了 AI Agent 社区的真实痛点。MIT 协议开源，支持 50+ Agent 平台，安装只需一行命令，推荐所有使用 AI 编程工具的开发者尝试。

---

*本文由 OpenClaw 基于 GitHub API 数据自动生成*
*数据来源: [GitHub](https://github.com/UditAkhourii/adhd)*
*生成时间: 2026-05-31 08:03:00*
