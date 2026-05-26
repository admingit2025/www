---
title: "bumblebee: Read-only developer endpoint scanner for on-dis..."
date: 2026-05-26T20:31:51
author: "GitHub Trending Bot"
description: "深度解析本周 GitHub 热门开源项目 bumblebee，探索其技术架构与应用场景"
categories: ["技术资讯", "开源项目"]
tags: ["github", "Go", "bumblebee", "开源", "技术分析"]
cover:
    image: "https://opengraph.githubassets.com/1/perplexityai/bumblebee"
    alt: "bumblebee"
---

# bumblebee: Read-only developer endpoint scanner for on-disk package, extension, and developer-tool metadata, built to check exposure to known software supply-chain compromises.

![bumblebee](https://opengraph.githubassets.com/1/perplexityai/bumblebee)

> 本周 GitHub 最热门开源项目深度解析
> 项目地址: [perplexityai/bumblebee](https://github.com/perplexityai/bumblebee)
> 生成时间: 2026-05-26 20:31:51

## 项目概览

[perplexityai/bumblebee](https://github.com/perplexityai/bumblebee) 是本周 GitHub 上最受关注的开源项目之一，在短时间内积累了大量关注。

### 基本信息

| 指标 | 数据 |
|------|------|
| **作者** | [@perplexityai](https://github.com/perplexityai) |
| **编程语言** | Go |
| **Star 数** | 2817 ⭐ |
| **Fork 数** | 218 |
| **创建时间** | 2026-05-20 |
| **最后更新** | 2026-05-26 |

## 项目简介

Read-only developer endpoint scanner for on-disk package, extension, and developer-tool metadata, built to check exposure to known software supply-chain compromises.

Go 语言以高性能、高并发著称，是云原生和后端服务开发的热门选择。

## 核心特性

根据项目 README 分析，bumblebee 的主要特点包括：

- **高关注度**：2817 个 Star，说明开发者社区对此项目高度认可
- **活跃开发**：218 个 Fork，社区参与度高
- **快速成长**：自 2026-05-20 创建以来持续获得关注
- **开源免费**：完全开源，可自由使用和二次开发

## 技术架构

bumblebee 基于 **Go** 技术栈构建：

1. **编程语言**：Go
2. **项目规模**：2817 个 Star，获得广泛认可
3. **社区活跃度**：218 个 Fork，开发者积极参与

## README 原文摘要

```
# bumblebee

Bumblebee is a read-only inventory collector for package, extension,
and developer-tool metadata on macOS and Linux developer endpoints.

It answers a narrow supply-chain response question: when an advisory
names a package, extension, or version, which developer machines show
a match in their on-disk metadata right now?

SBOMs help answer what shipped, and EDR helps answer what ran or
touched the network, but supply-chain response often needs a different
view: messy local state across lockfiles, package-manager metadata,
extension manifests, and supported developer-tool configs.

Bumblebee turns that scattered on-disk state into structured NDJSON
component records and, when given an exposure catalog, flags exact
matches for fast, read-only exposure checks when responders already
know what they are looking for.

## Scope

- Single static binary, Go 1.25+, zero non-stdlib dependencies.
- Three scan profiles (`baseline`, `project`, `deep`) for different
  populations and cadences.
- Reads only the lockfiles, package-manager install metadata,
  extension manifests, and supported MCP JSON configs listed in
  [docs/inventory-sources.md](docs/inventory-sources.md). No package
  manager execution (`npm ls`, `pip show`, `go list`, ...) and no
  source-file reads. MCP host configs can carry environment values
  and credentials in their `env` blocks; Bumblebee parses these
  configs for the server inventory it needs but does not emit those
  values in its records.

## Coverage

| Family | Emitted `ecosystem` | Sources |
|---|---|---|
| npm | `npm` | `package-lock.json`, `npm-shrinkwrap.json`, `node_modules/.package-lock.json`, `node_modules/<pkg>/package.json` |
| pnpm | `npm` | `pnpm-lock.yaml`, `.pnpm/.../package.json` |
| Yarn | `npm` | `yarn.lock` (Classic + Berry) |
| Bun | `npm` | `bun.lock`; `bun.lockb` presence as diagnostic |
| PyPI | `pypi` | `*.dist-info/METADATA`, `INSTALLER`, `direct_url.json`, `*.egg-info/PKG-INFO` |
| Go modules | `go` | `go.sum`, `
```

## 最近更新记录

- **2026-05-24**: feat(threat_intel): add TrapDoor Crypto Stealer exposure catalog (#17)
- **2026-05-23**: Merge pull request #9 from perplexityai/psi/exposure/laravel-lang-2026-05-23
- **2026-05-23**: clean up: trim catalog metadata, complete version coverage to 700 tags
- **2026-05-23**: Add Laravel Lang exposure catalog
- **2026-05-22**: initial public release (v0.1.1)


## 适用场景

bumblebee 适合以下用户：

- 云原生开发者、微服务架构师、高并发系统开发者
- 希望提升开发效率的技术团队
- 正在探索 Go 生态的开发者
- 对 Read-only developer endpoint scanner for on-disk package, extension, and developer-tool metadata, built to check exposure to known software supply-chain compromises. 感兴趣的工程师

## 如何开始

如果你对这个项目感兴趣：

1. 访问 [GitHub 仓库](https://github.com/perplexityai/bumblebee) 查看完整文档
2. 阅读 README 了解安装和使用方法
3. 查看 Issues 了解已知问题和社区反馈
4. 欢迎提交 PR 或 Issue 参与贡献

## 总结

bumblebee 是本周 GitHub 上值得关注的热门项目，凭借 2817 个 Star 的亮眼成绩，展示了开发者社区对该方向的强烈兴趣。自 2026-05-20 创建以来的快速增长，说明这是一个值得持续关注的优质开源项目。

---

*本文由 OpenClaw 基于 GitHub API 数据自动生成*
*数据来源: [GitHub](https://github.com/perplexityai/bumblebee)*
*生成时间: 2026-05-26 20:31:51*
