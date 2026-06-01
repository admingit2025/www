---
title: "weather-prediction-bot: polymarket trading bot polymarket trading bot p..."
date: 2026-06-01T15:05:20
author: "GitHub Trending Bot"
description: "深度解析本周 GitHub 热门开源项目 weather-prediction-bot，探索其技术架构与应用场景"
categories: ["技术资讯", "开源项目"]
tags: ["github", "TypeScript", "weather-prediction-bot", "开源", "技术分析"]
cover:
    image: "https://opengraph.githubassets.com/1/Signal-Trade-Core/weather-prediction-bot"
    alt: "weather-prediction-bot"
---

# weather-prediction-bot: polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot

![weather-prediction-bot](https://opengraph.githubassets.com/1/Signal-Trade-Core/weather-prediction-bot)

> 本周 GitHub 最热门开源项目深度解析
> 项目地址: [Signal-Trade-Core/weather-prediction-bot](https://github.com/Signal-Trade-Core/weather-prediction-bot)
> 生成时间: 2026-06-01 15:05:20

## 项目概览

[Signal-Trade-Core/weather-prediction-bot](https://github.com/Signal-Trade-Core/weather-prediction-bot) 是本周 GitHub 上最受关注的开源项目之一，在短时间内积累了大量关注。

### 基本信息

| 指标 | 数据 |
|------|------|
| **作者** | [@Signal-Trade-Core](https://github.com/Signal-Trade-Core) |
| **编程语言** | TypeScript |
| **Star 数** | 366 ⭐ |
| **Fork 数** | 5235 |
| **创建时间** | 2026-05-28 |
| **最后更新** | 2026-06-01 |

## 项目简介

polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot

TypeScript 是 JavaScript 的超集，提供强类型支持，适合大型项目开发。

## 核心特性

根据项目 README 分析，weather-prediction-bot 的主要特点包括：

- **高关注度**：366 个 Star，说明开发者社区对此项目高度认可
- **活跃开发**：5235 个 Fork，社区参与度高
- **快速成长**：自 2026-05-28 创建以来持续获得关注
- **开源免费**：完全开源，可自由使用和二次开发

## 技术架构

weather-prediction-bot 基于 **TypeScript** 技术栈构建：

1. **编程语言**：TypeScript
2. **项目规模**：366 个 Star，获得广泛认可
3. **社区活跃度**：5235 个 Fork，开发者积极参与

## README 原文摘要

```
# Polymarket Weather Trading Bot

Node.js / TypeScript trading automation for Polymarket daily temperature markets. The bot fuses multi-region weather forecasts (NWS for US cities, Open-Meteo for international cities) with Polymarket CLOB pricing: it maps each city's forecast max temperature to the matching market bucket, then either prints read-only signals, paper-trades against a local JSON ledger, or posts real CLOB limit orders.

## Overview

For each configured city, the bot:

1. Pulls a daily-max forecast for the next few days from the right weather provider.
2. Looks up the matching Polymarket "Highest temperature in {city} on {date}" event.
3. Finds the temperature bucket (Yes/No market) whose range contains the forecast.
4. Compares the YES price to `ENTRY_THRESHOLD` and `EXIT_THRESHOLD` and acts according to the selected mode.

Everything is driven by `.env` at runtime; there is no `config.json` in the primary flows.

---

## Key features

- **Multi-region weather data**: NWS observations + hourly forecasts for US cities (°F), Open-Meteo `temperature_2m_max` (with `timezone=auto`) for international cities (°C). The provider, coordinates, and temperature unit are declared per city in `src/nws.ts` (`LOCATIONS`).
- **Unit-safe bucket matching**: each city declares `tempUnit` (`F` or `C`); the parser tags every Polymarket bucket question with its own unit, and the strategy only matches buckets whose unit equals the city's. °F and °C markets are never cross-matched.
- **Three execution modes**:
  - `signal` (dry-run) — no orders, no state changes.
  - `paper` (`--live`) — simulated PnL written to `simulation.json`.
  - `execute` (`--execute`) — real CLOB limit orders on Polygon.
- **Proxy wallet support**: MetaMask signer with Polymarket proxy/Safe funder via `USE_PROXY_WALLET=true` and `SIGNATURE_TYPE=2`. Signature types 0 (EOA), 1 (Polymarket proxy/Magic), 2 (Gnosis Safe) all supported.
- **Live wallet check**: before any `execute` run the bot reads pUSD coll
```

## 最近更新记录

- 暂无提交记录


## 适用场景

weather-prediction-bot 适合以下用户：

- 大型项目团队、注重代码质量的开发者、企业级应用开发
- 希望提升开发效率的技术团队
- 正在探索 TypeScript 生态的开发者
- 对 polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot polymarket trading bot 感兴趣的工程师

## 如何开始

如果你对这个项目感兴趣：

1. 访问 [GitHub 仓库](https://github.com/Signal-Trade-Core/weather-prediction-bot) 查看完整文档
2. 阅读 README 了解安装和使用方法
3. 查看 Issues 了解已知问题和社区反馈
4. 欢迎提交 PR 或 Issue 参与贡献

## 总结

weather-prediction-bot 是本周 GitHub 上值得关注的热门项目，凭借 366 个 Star 的亮眼成绩，展示了开发者社区对该方向的强烈兴趣。自 2026-05-28 创建以来的快速增长，说明这是一个值得持续关注的优质开源项目。

---

*本文由 OpenClaw 基于 GitHub API 数据自动生成*
*数据来源: [GitHub](https://github.com/Signal-Trade-Core/weather-prediction-bot)*
*生成时间: 2026-06-01 15:05:20*
