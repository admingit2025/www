---
title: "9drive: 9Drive is a storage gateway web app for connect..."
date: 2026-06-07T20:31:33
author: "GitHub Trending Bot"
description: "深度解析本周 GitHub 热门开源项目 9drive，探索其技术架构与应用场景"
categories: ["技术资讯", "开源项目"]
tags: ["github", "TypeScript", "9drive", "开源", "技术分析"]
cover:
    image: "https://opengraph.githubassets.com/1/zenhosta/9drive"
    alt: "9drive"
---

# 9drive: 9Drive is a storage gateway web app for connecting multiple Google Drive accounts into one virtual storage dashboard. Users can connect Google Drive accounts, track quota, upload files, organize files with virtual folders, preview files, and let the backend route uploads to the Drive account with enough free space.

![9drive](https://opengraph.githubassets.com/1/zenhosta/9drive)

> 本周 GitHub 最热门开源项目深度解析
> 项目地址: [zenhosta/9drive](https://github.com/zenhosta/9drive)
> 生成时间: 2026-06-07 20:31:33

## 项目概览

[zenhosta/9drive](https://github.com/zenhosta/9drive) 是本周 GitHub 上最受关注的开源项目之一，在短时间内积累了大量关注。

### 基本信息

| 指标 | 数据 |
|------|------|
| **作者** | [@zenhosta](https://github.com/zenhosta) |
| **编程语言** | TypeScript |
| **Star 数** | 354 ⭐ |
| **Fork 数** | 130 |
| **创建时间** | 2026-06-04 |
| **最后更新** | 2026-06-07 |

## 项目简介

9Drive is a storage gateway web app for connecting multiple Google Drive accounts into one virtual storage dashboard. Users can connect Google Drive accounts, track quota, upload files, organize files with virtual folders, preview files, and let the backend route uploads to the Drive account with enough free space.

TypeScript 是 JavaScript 的超集，提供强类型支持，适合大型项目开发。

## 核心特性

根据项目 README 分析，9drive 的主要特点包括：

- **高关注度**：354 个 Star，说明开发者社区对此项目高度认可
- **活跃开发**：130 个 Fork，社区参与度高
- **快速成长**：自 2026-06-04 创建以来持续获得关注
- **开源免费**：完全开源，可自由使用和二次开发

## 技术架构

9drive 基于 **TypeScript** 技术栈构建：

1. **编程语言**：TypeScript
2. **项目规模**：354 个 Star，获得广泛认可
3. **社区活跃度**：130 个 Fork，开发者积极参与

## README 原文摘要

```
![9Drive cover](https://i.ibb.co.com/35BySv1C/image.png)

# 9Drive

9Drive is a storage gateway web app for connecting multiple Google Drive accounts into one virtual storage dashboard. Users can register with email/password or Google, automatically connect their first Google Drive account during Google sign-in, track quota, upload files into a dedicated `9drive` Drive folder, organize files with virtual folders, preview files, sync MySQL from Google Drive, and let the backend route uploads to the Drive account with enough free space.

## Features

- React + Vite frontend.
- Express + TypeScript backend.
- MySQL database with Prisma migrations.
- Bearer token authentication.
- Email/password auth plus Google sign-in/register with automatic first Drive connection.
- Global Google OAuth config stored encrypted in DB.
- Optional reCAPTCHA on email/password registration.
- Direct upload stream to Google Drive. Files are not stored on the server.
- Google Drive uploads are stored under a root `9drive` folder.
- Manual sync from the Google Drive `9drive` folder back into MySQL.
- Multi-account storage quota summary.
- Quota tracker page.
- Virtual folders.
- File preview, download, rename, move, and delete actions.
- Bottom-right upload progress panel.

## Preview

Live preview: https://9drive.zenhosta.com

![9Drive dashboard preview](https://i.ibb.co.com/HLjG3JRf/image.png)

![9Drive shared file preview](https://i.ibb.co.com/QLpYGmx/image.png)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=zenhosta/9drive&type=Date)](https://www.star-history.com/#zenhosta/9drive&Date)

## Project Structure

````txt
backend/   Express API, Prisma schema, Google Drive integration
frontend/  Vite React app
````

## Requirements

- Node.js 20+
- npm
- MySQL running locally
- Google Cloud project
- Google OAuth Client ID and Client Secret

Default database used by this project:

````txt
host: localhost
port: 3306
database: 9drive
user: root
password: empty
````

#
```

## 最近更新记录



## 适用场景

9drive 适合以下用户：

- 大型项目团队、注重代码质量的开发者、企业级应用开发
- 希望提升开发效率的技术团队
- 正在探索 TypeScript 生态的开发者
- 对 9Drive is a storage gateway web app for connecting multiple Google Drive accounts into one virtual storage dashboard. Users can connect Google Drive accounts, track quota, upload files, organize files with virtual folders, preview files, and let the backend route uploads to the Drive account with enough free space. 感兴趣的工程师

## 如何开始

如果你对这个项目感兴趣：

1. 访问 [GitHub 仓库](https://github.com/zenhosta/9drive) 查看完整文档
2. 阅读 README 了解安装和使用方法
3. 查看 Issues 了解已知问题和社区反馈
4. 欢迎提交 PR 或 Issue 参与贡献

## 总结

9drive 是本周 GitHub 上值得关注的热门项目，凭借 354 个 Star 的亮眼成绩，展示了开发者社区对该方向的强烈兴趣。自 2026-06-04 创建以来的快速增长，说明这是一个值得持续关注的优质开源项目。

---

*本文由 OpenClaw 基于 GitHub API 数据自动生成*
*数据来源: [GitHub](https://github.com/zenhosta/9drive)*
*生成时间: 2026-06-07 20:31:33*
