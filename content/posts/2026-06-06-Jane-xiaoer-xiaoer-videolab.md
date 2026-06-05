---
title: "xiaoer-videolab: One click on the toolbar grabs the current page..."
date: 2026-06-06T03:07:56
author: "GitHub Trending Bot"
description: "深度解析本周 GitHub 热门开源项目 xiaoer-videolab，探索其技术架构与应用场景"
categories: ["技术资讯", "开源项目"]
tags: ["github", "Python", "xiaoer-videolab", "开源", "技术分析"]
cover:
    image: "https://opengraph.githubassets.com/1/Jane-xiaoer/xiaoer-videolab"
    alt: "xiaoer-videolab"
---

# xiaoer-videolab: One click on the toolbar grabs the current page's video into ~/Downloads — local yt-dlp daemon, 1800+ sites. 小耳抓视频：一键把当前页视频抓到本地。

![xiaoer-videolab](https://opengraph.githubassets.com/1/Jane-xiaoer/xiaoer-videolab)

> 本周 GitHub 最热门开源项目深度解析
> 项目地址: [Jane-xiaoer/xiaoer-videolab](https://github.com/Jane-xiaoer/xiaoer-videolab)
> 生成时间: 2026-06-06 03:07:56

## 项目概览

[Jane-xiaoer/xiaoer-videolab](https://github.com/Jane-xiaoer/xiaoer-videolab) 是本周 GitHub 上最受关注的开源项目之一，在短时间内积累了大量关注。

### 基本信息

| 指标 | 数据 |
|------|------|
| **作者** | [@Jane-xiaoer](https://github.com/Jane-xiaoer) |
| **编程语言** | Python |
| **Star 数** | 352 ⭐ |
| **Fork 数** | 55 |
| **创建时间** | 2026-06-04 |
| **最后更新** | 2026-06-05 |

## 项目简介

One click on the toolbar grabs the current page's video into ~/Downloads — local yt-dlp daemon, 1800+ sites. 小耳抓视频：一键把当前页视频抓到本地。

Python 是一门简洁优雅的编程语言，广泛应用于数据科学、人工智能、Web 开发等领域。

## 核心特性

根据项目 README 分析，xiaoer-videolab 的主要特点包括：

- **高关注度**：352 个 Star，说明开发者社区对此项目高度认可
- **活跃开发**：55 个 Fork，社区参与度高
- **快速成长**：自 2026-06-04 创建以来持续获得关注
- **开源免费**：完全开源，可自由使用和二次开发

## 技术架构

xiaoer-videolab 基于 **Python** 技术栈构建：

1. **编程语言**：Python
2. **项目规模**：352 个 Star，获得广泛认可
3. **社区活跃度**：55 个 Fork，开发者积极参与

## README 原文摘要

```
<div align="center">

# 🎬 Xiaoer VideoLab

### One click. Any video. Local.

Press one toolbar button and the video on the current page lands in your `~/Downloads`.
Powered by a tiny local [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) daemon — **1800+ sites** out of the box
(YouTube · Bilibili · X/Twitter · TikTok · Vimeo · Twitch · Weibo …).

[![CI](https://github.com/Jane-xiaoer/xiaoer-videolab/actions/workflows/ci.yml/badge.svg)](https://github.com/Jane-xiaoer/xiaoer-videolab/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](LICENSE)
![Platform](https://img.shields.io/badge/platform-macOS-lightgrey)
![Manifest V3](https://img.shields.io/badge/Chrome-MV3-4285F4?logo=googlechrome&logoColor=white)
![Python stdlib only](https://img.shields.io/badge/Python-stdlib%20only-3776AB?logo=python&logoColor=white)
![No tracking](https://img.shields.io/badge/network-localhost%20only-27ae60)

[![English](https://img.shields.io/badge/lang-English-2563eb)](README.md)&nbsp;
[![简体中文](https://img.shields.io/badge/lang-简体中文-lightgrey)](README.zh-CN.md)

</div>

---

## Why

Browser video downloaders are a swamp of sketchy extensions that beg for "read everything on every site"
permissions and phone home. Xiaoer VideoLab takes the opposite bet:

- **The extension does almost nothing.** It only reads the *current tab's URL* when you click it, and POSTs
  that one string to `127.0.0.1`. No page scraping, no content scripts, no remote servers.
- **The download happens locally.** A small Python daemon hands the URL to `yt-dlp`, the
  battle-tested open-source downloader. All the smarts live in a tool you can audit.
- **Nothing leaves your machine** except the request `yt-dlp` makes to fetch the video you asked for.

## How it works

````
 ┌─────────────────────┐   click    ┌──────────────────────────┐         ┌──────────┐
 │  Browser toolbar     │ ─────────► │  daemon @ 127.0.0.1:7788 │ ──────► │  yt-dlp  │ ──► ~/Downloads
 │  (Chrome MV3 ext.)  
```

## 最近更新记录

- **2026-06-05**: 1.2.0: one-command updater + installer prefers nightly yt-dlp
- **2026-06-05**: 1.1.0: prefer yt-dlp nightly to survive Bilibili HTTP 412
- **2026-06-04**: ci: add GitHub Actions (lint + macOS daemon smoke test)
- **2026-06-04**: 1.0.1: block drive-by downloads (Origin guard)
- **2026-06-04**: docs: warn that changing VIDEOLAB_PORT also requires editing the extension


## 适用场景

xiaoer-videolab 适合以下用户：

- 数据科学家和 AI 研究者、Web 后端开发者、自动化脚本编写者
- 希望提升开发效率的技术团队
- 正在探索 Python 生态的开发者
- 对 One click on the toolbar grabs the current page's video into ~/Downloads — local yt-dlp daemon, 1800+ sites. 小耳抓视频：一键把当前页视频抓到本地。 感兴趣的工程师

## 如何开始

如果你对这个项目感兴趣：

1. 访问 [GitHub 仓库](https://github.com/Jane-xiaoer/xiaoer-videolab) 查看完整文档
2. 阅读 README 了解安装和使用方法
3. 查看 Issues 了解已知问题和社区反馈
4. 欢迎提交 PR 或 Issue 参与贡献

## 总结

xiaoer-videolab 是本周 GitHub 上值得关注的热门项目，凭借 352 个 Star 的亮眼成绩，展示了开发者社区对该方向的强烈兴趣。自 2026-06-04 创建以来的快速增长，说明这是一个值得持续关注的优质开源项目。

---

*本文由 OpenClaw 基于 GitHub API 数据自动生成*
*数据来源: [GitHub](https://github.com/Jane-xiaoer/xiaoer-videolab)*
*生成时间: 2026-06-06 03:07:56*
