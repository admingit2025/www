---
title: "QMAI: 青幕AI写作软件，解决长篇小说写作问题，解决小说角色性格不统一，防止人设崩坏。"
date: 2026-06-06T02:31:28
author: "GitHub Trending Bot"
description: "深度解析本周 GitHub 热门开源项目 QMAI，探索其技术架构与应用场景"
categories: ["技术资讯", "开源项目"]
tags: ["github", "TypeScript", "QMAI", "开源", "技术分析"]
cover:
    image: "https://opengraph.githubassets.com/1/Mochocyang/QMAI"
    alt: "QMAI"
---

# QMAI: 青幕AI写作软件，解决长篇小说写作问题，解决小说角色性格不统一，防止人设崩坏。

![QMAI](https://opengraph.githubassets.com/1/Mochocyang/QMAI)

> 本周 GitHub 最热门开源项目深度解析
> 项目地址: [Mochocyang/QMAI](https://github.com/Mochocyang/QMAI)
> 生成时间: 2026-06-06 02:31:28

## 项目概览

[Mochocyang/QMAI](https://github.com/Mochocyang/QMAI) 是本周 GitHub 上最受关注的开源项目之一，在短时间内积累了大量关注。

### 基本信息

| 指标 | 数据 |
|------|------|
| **作者** | [@Mochocyang](https://github.com/Mochocyang) |
| **编程语言** | TypeScript |
| **Star 数** | 350 ⭐ |
| **Fork 数** | 64 |
| **创建时间** | 2026-05-31 |
| **最后更新** | 2026-06-05 |

## 项目简介

青幕AI写作软件，解决长篇小说写作问题，解决小说角色性格不统一，防止人设崩坏。

TypeScript 是 JavaScript 的超集，提供强类型支持，适合大型项目开发。

## 核心特性

根据项目 README 分析，QMAI 的主要特点包括：

- **高关注度**：350 个 Star，说明开发者社区对此项目高度认可
- **活跃开发**：64 个 Fork，社区参与度高
- **快速成长**：自 2026-05-31 创建以来持续获得关注
- **开源免费**：完全开源，可自由使用和二次开发

## 技术架构

QMAI 基于 **TypeScript** 技术栈构建：

1. **编程语言**：TypeScript
2. **项目规模**：350 个 Star，获得广泛认可
3. **社区活跃度**：64 个 Fork，开发者积极参与

## README 原文摘要

```
<p align="center">
  <img src="QM-LOGO.png" width="120" alt="青幕AI写作 Logo" />
</p>

<h1 align="center">青幕AI写作（QMAI）</h1>

<p align="center">
  面向长篇小说的记忆型 AI 写作桌面系统
</p>

<p align="center">
  <a href="https://github.com/Mochocyang/QMAI/releases">
    <img src="https://img.shields.io/github/v/release/Mochocyang/QMAI?style=flat-square" alt="Release" />
  </a>
  <img src="https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-blue?style=flat-square" alt="Platform" />
  <img src="https://img.shields.io/badge/license-MIT-green?style=flat-square" alt="License" />
</p>

---
<img width="1232" height="836" alt="image" src="https://github.com/user-attachments/assets/66630916-85b8-4865-9477-f5e04706bee3" />

## 软件概述

青幕AI写作不是普通的 AI 聊天写作工具。它是一套**长篇小说记忆型写作系统**，专为 200 万～300 万字量级的连载小说创作设计。

核心理念：

> 写前自动提取上下文 → 写后自动沉淀章节记忆 → 图谱追踪关系变化 → 审查系统防止崩坏 → 人工确认最终定稿

普通 AI 写作工具的问题在于：写到后期 AI 会遗忘前文、人物性格不一致、时间线混乱、伏笔丢失。青幕AI写作通过结构化记忆系统和混合检索引擎，让 AI 在每次生成时都能"记住"之前的一切。

**适用场景：**
- 网文日更作者：保持长篇连载质量、防止人设崩坏
- 小说策划者：管理世界观、势力关系、多线剧情
- AI 辅助写作者：让大模型在长篇创作中持续可用

---
<img width="1239" height="883" alt="image" src="https://github.com/user-attachments/assets/076740be-85ef-4503-842d-565c367aebdc" />
<img width="1201" height="832" alt="image" src="https://github.com/user-attachments/assets/57936132-45b2-4fed-8c80-2c9282fedbf5" />

## 核心功能

### 📚 记忆系统

记忆系统是青幕AI写作的核心引擎。每章正式保存后，系统会自动执行**章节摄取**，将正文内容结构化为可检索、可追踪、可复用的记忆单元。

**章节摄取提取的内容：**
- 章节摘要与结尾钩子
- 出场人物、地点、组织、物品
- 关键事件与状态变化
- 人物关系变化与角色认知变化
- 伏笔新增 / 推进 / 回收
- 时间线事件
- 图谱节点与关系边

**上下文引擎（写作前自动触发）：**

每次调用 LLM 写作前，系统自动生成**上下文包**，按优先级组装：

````
用户明确指定 > 当前章节细纲 > 上一章结尾 > Canon 正史规则
> 当前人物状态 > 伏笔状态 > 最近章节摘要 > 图谱关系
> 向量搜索结果 > 关键词搜索结果
````

上下文包有 token 预算控制，自动在保证关键信息不遗漏的前提下裁剪内容。

**混合检索策略：**
- 最近章节窗口：直接获取最近 N 章的摘要
- 关键词搜索：BM25 风格的精确匹配
- 向量搜索：语义级别的相似内容检索
- 图谱搜索：沿关系边扩展相关节点
- Canon 规则：强制注入的不可违背设定

**数据存储方式：**

所有记忆数据以项目目录形式本地存储，章节正文保存为 Markdown，快照与状态保存为 JSON。支持导出、备份和索引重建。

---
<img width="1235" height="843" alt="image" src="https://github.com/user-attachments/ass
```

## 最近更新记录

- **2026-06-05**: chore: release qmai 2.2.0
- **2026-06-05**: chore: release qmai 2.1.10 fixes
- **2026-06-05**: fix windows updater manifest signing
- **2026-06-05**: fix release updater manifest upload
- **2026-06-05**: fix updater proxy handling


## 适用场景

QMAI 适合以下用户：

- 大型项目团队、注重代码质量的开发者、企业级应用开发
- 希望提升开发效率的技术团队
- 正在探索 TypeScript 生态的开发者
- 对 青幕AI写作软件，解决长篇小说写作问题，解决小说角色性格不统一，防止人设崩坏。 感兴趣的工程师

## 如何开始

如果你对这个项目感兴趣：

1. 访问 [GitHub 仓库](https://github.com/Mochocyang/QMAI) 查看完整文档
2. 阅读 README 了解安装和使用方法
3. 查看 Issues 了解已知问题和社区反馈
4. 欢迎提交 PR 或 Issue 参与贡献

## 总结

QMAI 是本周 GitHub 上值得关注的热门项目，凭借 350 个 Star 的亮眼成绩，展示了开发者社区对该方向的强烈兴趣。自 2026-05-31 创建以来的快速增长，说明这是一个值得持续关注的优质开源项目。

---

*本文由 OpenClaw 基于 GitHub API 数据自动生成*
*数据来源: [GitHub](https://github.com/Mochocyang/QMAI)*
*生成时间: 2026-06-06 02:31:28*
