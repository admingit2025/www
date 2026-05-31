---
title: "gemini-web2api: Convert Google Gemini web into OpenAI-compatibl..."
date: 2026-05-31T12:08:09
author: "GitHub Trending Bot"
description: "深度解析本周 GitHub 热门开源项目 gemini-web2api，探索其技术架构与应用场景"
categories: ["技术资讯", "开源项目"]
tags: ["github", "Python", "gemini-web2api", "开源", "技术分析"]
cover:
    image: "https://opengraph.githubassets.com/1/Sophomoresty/gemini-web2api"
    alt: "gemini-web2api"
---

# gemini-web2api: Convert Google Gemini web into OpenAI-compatible API. Zero auth, cross-platform, single file.

![gemini-web2api](https://opengraph.githubassets.com/1/Sophomoresty/gemini-web2api)

> 本周 GitHub 最热门开源项目深度解析
> 项目地址: [Sophomoresty/gemini-web2api](https://github.com/Sophomoresty/gemini-web2api)
> 生成时间: 2026-05-31 12:08:09

## 项目概览

[Sophomoresty/gemini-web2api](https://github.com/Sophomoresty/gemini-web2api) 是本周 GitHub 上最受关注的开源项目之一，在短时间内积累了大量关注。

### 基本信息

| 指标 | 数据 |
|------|------|
| **作者** | [@Sophomoresty](https://github.com/Sophomoresty) |
| **编程语言** | Python |
| **Star 数** | 577 ⭐ |
| **Fork 数** | 191 |
| **创建时间** | 2026-05-28 |
| **最后更新** | 2026-05-31 |

## 项目简介

Convert Google Gemini web into OpenAI-compatible API. Zero auth, cross-platform, single file.

Python 是一门简洁优雅的编程语言，广泛应用于数据科学、人工智能、Web 开发等领域。

## 核心特性

根据项目 README 分析，gemini-web2api 的主要特点包括：

- **高关注度**：577 个 Star，说明开发者社区对此项目高度认可
- **活跃开发**：191 个 Fork，社区参与度高
- **快速成长**：自 2026-05-28 创建以来持续获得关注
- **开源免费**：完全开源，可自由使用和二次开发

## 技术架构

gemini-web2api 基于 **Python** 技术栈构建：

1. **编程语言**：Python
2. **项目规模**：577 个 Star，获得广泛认可
3. **社区活跃度**：191 个 Fork，开发者积极参与

## README 原文摘要

```
# gemini-web2api

<p align="center">
  <img src="logo.png" width="200" alt="gemini-web2api logo">
</p>

[中文文档](README_CN.md)

Convert Google Gemini's web interface into an OpenAI-compatible API. Zero authentication, zero cost, cross-platform.

## Features

- **Optional API Keys**: no auth when `api_keys` is empty, OpenAI-style Bearer auth when configured
- **OpenAI Compatible**: Drop-in replacement for `/v1/chat/completions` and `/v1/models`
- **Tool Calling**: Full function calling support (OpenAI format)
- **Multiple Models**: Flash, Flash Thinking (20k+ char output), Pro, Auto, Lite
- **Thinking Depth**: Adjustable via `@think=N` suffix (0=deepest, 4=shallowest)
- **Web Search**: Built-in internet access (Gemini's native search)
- **Cross-Platform**: Pure Python, no dependencies beyond stdlib
- **Streaming**: SSE streaming support
- **Codex CLI**: Responses API (`/v1/responses`) for OpenAI Codex integration
- **Gemini CLI**: Google native API (`/v1beta/models`) for Gemini CLI compatibility

## Quick Start

````bash
python gemini_web2api.py
````

Server starts at `http://localhost:8081/v1`.

## Client Configuration

### Cherry Studio / ChatBox / any OpenAI client

| Field | Value |
|-------|-------|
| Base URL | `http://localhost:8081/v1` |
| API Key | any `api_keys` value from `config.json`; anything if not configured |
| Model | `gemini-3.5-flash-thinking` |

### curl

````bash
curl http://localhost:8081/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-your-key" \
  -d '{"model":"gemini-3.5-flash","messages":[{"role":"user","content":"Hello!"}]}'
````

### OpenAI Python SDK

````python
from openai import OpenAI
client = OpenAI(base_url="http://localhost:8081/v1", api_key="sk-your-key")
resp = client.chat.completions.create(
    model="gemini-3.5-flash-thinking",
    messages=[{"role": "user", "content": "Explain quantum computing"}]
)
print(resp.choices[0].message.content)
````

### Gemini CLI

````bash
export GEMINI_API_KEY=
```

## 最近更新记录

- 暂无提交记录


## 适用场景

gemini-web2api 适合以下用户：

- 数据科学家和 AI 研究者、Web 后端开发者、自动化脚本编写者
- 希望提升开发效率的技术团队
- 正在探索 Python 生态的开发者
- 对 Convert Google Gemini web into OpenAI-compatible API. Zero auth, cross-platform, single file. 感兴趣的工程师

## 如何开始

如果你对这个项目感兴趣：

1. 访问 [GitHub 仓库](https://github.com/Sophomoresty/gemini-web2api) 查看完整文档
2. 阅读 README 了解安装和使用方法
3. 查看 Issues 了解已知问题和社区反馈
4. 欢迎提交 PR 或 Issue 参与贡献

## 总结

gemini-web2api 是本周 GitHub 上值得关注的热门项目，凭借 577 个 Star 的亮眼成绩，展示了开发者社区对该方向的强烈兴趣。自 2026-05-28 创建以来的快速增长，说明这是一个值得持续关注的优质开源项目。

---

*本文由 OpenClaw 基于 GitHub API 数据自动生成*
*数据来源: [GitHub](https://github.com/Sophomoresty/gemini-web2api)*
*生成时间: 2026-05-31 12:08:09*
