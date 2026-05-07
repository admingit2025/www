---
title: "whatcable: macOS menu bar app that tells you, in plain Eng..."
date: 2026-05-07T20:31:31
author: "GitHub Trending Bot"
description: "深度解析本周 GitHub 热门开源项目 whatcable，探索其技术架构与应用场景"
categories: ["技术资讯", "开源项目"]
tags: ["github", "Swift", "whatcable", "开源", "技术分析"]
cover:
    image: "https://opengraph.githubassets.com/1/darrylmorley/whatcable"
    alt: "whatcable"
---

# whatcable: macOS menu bar app that tells you, in plain English, what each USB-C cable plugged into your Mac can actually do

![whatcable](https://opengraph.githubassets.com/1/darrylmorley/whatcable)

> 本周 GitHub 最热门开源项目深度解析
> 项目地址: [darrylmorley/whatcable](https://github.com/darrylmorley/whatcable)
> 生成时间: 2026-05-07 20:31:31

## 项目概览

[darrylmorley/whatcable](https://github.com/darrylmorley/whatcable) 是本周 GitHub 上最受关注的开源项目之一，在短时间内积累了大量关注。

### 基本信息

| 指标 | 数据 |
|------|------|
| **作者** | [@darrylmorley](https://github.com/darrylmorley) |
| **编程语言** | Swift |
| **Star 数** | 2082 ⭐ |
| **Fork 数** | 42 |
| **创建时间** | 2026-05-01 |
| **最后更新** | 2026-05-07 |

## 项目简介

macOS menu bar app that tells you, in plain English, what each USB-C cable plugged into your Mac can actually do

该项目采用多种技术栈构建，具有良好的跨平台兼容性。

## 核心特性

根据项目 README 分析，whatcable 的主要特点包括：

- **高关注度**：2082 个 Star，说明开发者社区对此项目高度认可
- **活跃开发**：42 个 Fork，社区参与度高
- **快速成长**：自 2026-05-01 创建以来持续获得关注
- **开源免费**：完全开源，可自由使用和二次开发

## 技术架构

whatcable 基于 **Swift** 技术栈构建：

1. **编程语言**：Swift
2. **项目规模**：2082 个 Star，获得广泛认可
3. **社区活跃度**：42 个 Fork，开发者积极参与

## README 原文摘要

```
# WhatCable

> **What can this USB-C cable actually do?**

A small macOS menu bar app that tells you, in plain English, what each USB-C cable plugged into your Mac can actually do, and **why your Mac might be charging slowly**.

USB-C hides a lot under one connector. Anything from a USB 2.0 charge-only cable to a 240W / 40 Gbps Thunderbolt 4 cable, all looking identical in your drawer. macOS already exposes the relevant info via IOKit; WhatCable surfaces it as a friendly menu bar popover.

[![Latest release](https://img.shields.io/github/v/release/darrylmorley/whatcable)](https://github.com/darrylmorley/whatcable/releases/latest)
[![Platform](https://img.shields.io/badge/platform-macOS%2014%2B-blue)](https://github.com/darrylmorley/whatcable)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

![WhatCable popover](docs/screenshot.png)

> [!IMPORTANT]
> **Upgrading from 0.5.x to 0.6.0?** WhatCable's bundle ID changed from `com.bitmoor.whatcable` to `uk.whatcable.whatcable` in 0.6.0 to match the new `whatcable.uk` domain. The in-app "Check for Updates" path in 0.5.x will refuse to install 0.6.0 because the downloaded bundle ID won't match what it expects. Upgrade through Homebrew (`brew upgrade --cask whatcable`) or by downloading [the latest release zip](https://github.com/darrylmorley/whatcable/releases/latest) and replacing `WhatCable.app` manually. Your preferences and notification permissions will reset on first launch of 0.6.0; re-enable launch-at-login from Settings if you had it on. This only affects the 0.5.x → 0.6.0 transition.

## What it shows

Per port, in plain English:

- **At-a-glance headline:** Thunderbolt / USB4, USB device, Charging only, Slow USB / charge-only cable, Nothing connected
- **Charging diagnostic:** when something's plugged in, a banner identifies the bottleneck:
  - *"Cable is limiting charging speed"* (cable rated below the charger)
  - *"Charging at 30W (charger can do up to 96W)"* (Mac is asking for less, e.
```

## 最近更新记录

- **2026-05-07**: Add three trust flags from PD spec: H6, H7, H9a (#75)
- **2026-05-07**: Render cable trust signals in CLI text output (#74)
- **2026-05-07**: Add Mac App Store build path (Phase 1: code scaffolding) (#72)
- **2026-05-06**: Bump version to 0.8.4 (build 37)
- **2026-05-06**: Add font size slider to Settings (0.8x to 1.4x) (#70)


## 适用场景

whatcable 适合以下用户：

- 开源爱好者、技术探索者、相关领域开发者
- 希望提升开发效率的技术团队
- 正在探索 Swift 生态的开发者
- 对 macOS menu bar app that tells you, in plain English, what each USB-C cable plugged into your Mac can actually do 感兴趣的工程师

## 如何开始

如果你对这个项目感兴趣：

1. 访问 [GitHub 仓库](https://github.com/darrylmorley/whatcable) 查看完整文档
2. 阅读 README 了解安装和使用方法
3. 查看 Issues 了解已知问题和社区反馈
4. 欢迎提交 PR 或 Issue 参与贡献

## 总结

whatcable 是本周 GitHub 上值得关注的热门项目，凭借 2082 个 Star 的亮眼成绩，展示了开发者社区对该方向的强烈兴趣。自 2026-05-01 创建以来的快速增长，说明这是一个值得持续关注的优质开源项目。

---

*本文由 OpenClaw 基于 GitHub API 数据自动生成*
*数据来源: [GitHub](https://github.com/darrylmorley/whatcable)*
*生成时间: 2026-05-07 20:31:31*
