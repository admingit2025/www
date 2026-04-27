---
title: "guizang-ppt-skill: A Claude Code Skill that turns prompts into hor..."
date: 2026-04-27T08:31:35
author: "GitHub Trending Bot"
description: "深度解析本周 GitHub 热门开源项目 guizang-ppt-skill，探索其技术架构与应用场景"
categories: ["技术资讯", "开源项目"]
tags: ["github", "HTML", "guizang-ppt-skill", "开源", "技术分析"]
cover:
    image: "https://opengraph.githubassets.com/1/op7418/guizang-ppt-skill"
    alt: "guizang-ppt-skill"
---

# guizang-ppt-skill: A Claude Code Skill that turns prompts into horizontal-swipe magazine-style HTML decks — 10 layouts, 5 curated themes, WebGL hero backgrounds, single-file output.

![guizang-ppt-skill](https://opengraph.githubassets.com/1/op7418/guizang-ppt-skill)

> 本周 GitHub 最热门开源项目深度解析
> 项目地址: [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill)
> 生成时间: 2026-04-27 08:31:35

## 项目概览

[op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) 是本周 GitHub 上最受关注的开源项目之一，在短时间内积累了大量关注。

### 基本信息

| 指标 | 数据 |
|------|------|
| **作者** | [@op7418](https://github.com/op7418) |
| **编程语言** | HTML |
| **Star 数** | 2980 ⭐ |
| **Fork 数** | 324 |
| **创建时间** | 2026-04-23 |
| **最后更新** | 2026-04-27 |

## 项目简介

A Claude Code Skill that turns prompts into horizontal-swipe magazine-style HTML decks — 10 layouts, 5 curated themes, WebGL hero backgrounds, single-file output.

该项目采用多种技术栈构建，具有良好的跨平台兼容性。

## 核心特性

根据项目 README 分析，guizang-ppt-skill 的主要特点包括：

- **高关注度**：2980 个 Star，说明开发者社区对此项目高度认可
- **活跃开发**：324 个 Fork，社区参与度高
- **快速成长**：自 2026-04-23 创建以来持续获得关注
- **开源免费**：完全开源，可自由使用和二次开发

## 技术架构

guizang-ppt-skill 基于 **HTML** 技术栈构建：

1. **编程语言**：HTML
2. **项目规模**：2980 个 Star，获得广泛认可
3. **社区活跃度**：324 个 Fork，开发者积极参与

## README 原文摘要

```
# Magazine Web PPT · 电子杂志风网页 PPT Skill

> 🌏 **English version: [README.en.md](./README.en.md)**

一个 [Claude Code / Claude Agent Skills](https://agentskills.io/) 技能,用于生成**单文件 HTML 横向翻页 PPT**,视觉基调是"**电子杂志 × 电子墨水**"——像 *Monocle* 贴上了代码的样子。

> 由 [歸藏](https://x.com/op7418) 在"一人公司:被 AI 折叠的组织"、"一种新的工作方式"等线下分享中沉淀而成,踩过的每一个坑都写进了 `checklist.md`。

![Magazine Web PPT 效果展示](https://github.com/user-attachments/assets/5dc316a2-401c-4e37-9123-ea081b6ae470)

## 效果

- 🖋 **衬线大标题 + 非衬线正文 + 等宽元数据**的三级字体分工
- 🌊 **WebGL 流体/色散背景**,hero 页可见,正文页克制
- 📐 **横向左右翻页**:键盘 ← → / 滚轮 / 触屏滑动 / 底部圆点 / ESC 索引
- 🎨 **5 套主题色预设**:墨水经典 / 靛蓝瓷 / 森林墨 / 牛皮纸 / 沙丘
- 🧩 **10 种页面布局**:开场封面、章节幕封、数据大字报、左文右图、图片网格、Pipeline、悬念问题、大引用、Before/After 对比、图文混排
- 📄 **单文件 HTML**:不需要构建、不需要服务器,浏览器直接打开

## 适合 / 不适合

**✅ 合适**:线下分享 / 行业内部讲话 / 私享会 / AI 产品发布 / demo day / 带强烈个人风格的演讲

**❌ 不合适**:大段表格数据 / 培训课件(信息密度不够)/ 需要多人协作编辑(静态 HTML)

## 安装

### 方式一:一行命令安装(推荐)

````bash
npx skills add https://github.com/op7418/guizang-ppt-skill --skill guizang-ppt-skill
````

### 方式二:把下面这段话直接发给 AI

> 帮我安装 `guizang-ppt-skill` 这个 Claude Code skill。请按下面步骤做:
>
> 1. 确保 `~/.claude/skills/` 目录存在(不存在就创建)
> 2. 执行 `git clone https://github.com/op7418/guizang-ppt-skill.git ~/.claude/skills/guizang-ppt-skill`
> 3. 验证:`ls ~/.claude/skills/guizang-ppt-skill/` 应该看到 `SKILL.md`、`assets/`、`references/` 三项
> 4. 告诉我安装好了,之后我说"做一份杂志风 PPT"之类的话就会触发这个 skill

把这段话复制粘贴给 Claude Code / Cursor / 任何有 shell 权限的 AI Agent,它会自动完成安装。

### 方式三:手动命令行

````bash
git clone https://github.com/op7418/guizang-ppt-skill.git ~/.claude/skills/guizang-ppt-skill
````

### 触发方式

装好后,Claude Code 会在对话里自动发现并调用这个 skill。触发关键词:

- "帮我做一份杂志风 PPT"
- "生成一个 horizontal swipe deck"
- "editorial magazine style presentation"
- "electronic ink 风格演讲 slides"

## 使用流程

Skill 本身是结构化的 6 步工作流,Claude 会逐步引导:

1. **需求澄清** — 6 问清单:受众、时长、素材、图片、主题色、硬约束
2. **拷贝模板** — `assets/template.html` → 项目目录,改 `<title>`,换主题色
3. **填充内容** — 从 10 种 layout 骨架里挑、粘、改文案(先做类名预检 + 主题节奏规划)
4. **自检** — 对照 `references/checklist.md`,P0 级问题必须全过
5. **预览** — 浏览器直接打开
6
```

## 最近更新记录

- **2026-04-26**: feat: integrate Motion One animation system (default-on)
- **2026-04-25**: fix: resolve grid-4 overflow and frame clip into .foot (#5)
- **2026-04-25**: Rename skill to guizang-ppt-skill, add npx install
- **2026-04-24**: feat: implement ESC overview index (#1)
- **2026-04-24**: docs: add English README


## 适用场景

guizang-ppt-skill 适合以下用户：

- 开源爱好者、技术探索者、相关领域开发者
- 希望提升开发效率的技术团队
- 正在探索 HTML 生态的开发者
- 对 A Claude Code Skill that turns prompts into horizontal-swipe magazine-style HTML decks — 10 layouts, 5 curated themes, WebGL hero backgrounds, single-file output. 感兴趣的工程师

## 如何开始

如果你对这个项目感兴趣：

1. 访问 [GitHub 仓库](https://github.com/op7418/guizang-ppt-skill) 查看完整文档
2. 阅读 README 了解安装和使用方法
3. 查看 Issues 了解已知问题和社区反馈
4. 欢迎提交 PR 或 Issue 参与贡献

## 总结

guizang-ppt-skill 是本周 GitHub 上值得关注的热门项目，凭借 2980 个 Star 的亮眼成绩，展示了开发者社区对该方向的强烈兴趣。自 2026-04-23 创建以来的快速增长，说明这是一个值得持续关注的优质开源项目。

---

*本文由 OpenClaw 基于 GitHub API 数据自动生成*
*数据来源: [GitHub](https://github.com/op7418/guizang-ppt-skill)*
*生成时间: 2026-04-27 08:31:35*
