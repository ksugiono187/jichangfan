---
title: "Clash 机场客户端全景指南"
description: "深入了解 Clash 这款 Windows 和 macOS 平台最强大的代理工具的生态、衍生版及核心优势。"
order: 1
---

## 一、 什么是 Clash？

在所有的科学上网客户端中，**Clash 绝对是目前的统治者**。

Clash 最初是一款基于 Go 语言开发的命令行网络代理内核。由于其极其强大的**基于规则的智能分流 (Rule-based Routing)** 能力，它迅速风靡全球。
通过 Clash，您可以精细地控制每一条网络请求的走向：
*   微信、淘宝、国内银行 APP -> **直连 (DIRECT)**
*   YouTube、Google、Twitter -> **走代理 (PROXY)**
*   Netflix、Disney+ -> **指定走专门的香港解锁节点**
*   广告域名、数据跟踪域名 -> **直接拦截 (REJECT)**

这一切都是在后台瞬间自动完成的，您只需要保持 Clash 开启，就能获得与身处海外毫无二致的无缝上网体验。

## 二、 Clash 的繁荣生态与衍生版本

由于原始的 Clash 只是一个没有界面的底层内核，全球的开源开发者为其开发了各种各样的图形化外壳（GUI），形成了庞大的生态族群。

目前主流的 Clash 版本包括：

### 1. Clash for Windows (CFW)
*   **曾经的王者**：这是过去几年 Windows 平台上装机量最大的翻墙软件，图标是一只可爱的小猫咪。
*   **现状**：由于不可抗力，该项目已于 2023 年底停止维护。虽然依然可用，但不再推荐新用户安装。

### 2. Clash Verge / Clash Verge Rev (强烈推荐 ⭐)
*   **新一代主力**：这是目前 PC 端 (Windows / macOS / Linux) **最推荐**的 Clash 客户端。
*   **优势**：采用 Tauri 或 Electron 重构，界面极具现代感且极其流畅。更重要的是，它内置了最新的 **Clash Meta (mihomo)** 开源内核，完美支持 Vless Reality、Hysteria2 等最新高级协议。

### 3. ClashX / ClashX Pro
*   **Mac 用户首选**：专为 macOS 开发的轻量级状态栏工具，深度融入苹果系统生态。目前也有接入 Meta 内核的分支版本（如 ClashX Meta）在持续更新。

### 4. Clash for Android (CFA)
*   安卓平台上最著名的 Clash 客户端，同样由于开发者退网已停止更新。目前安卓端更推荐使用 Clash Meta for Android 或者 Surfboard。

## 三、 为什么机场首推 Clash？

几乎世界上 100% 的正规机场都会在后台提供“一键导入 Clash 订阅”的按钮。这是因为：
1. **标准化**：Clash 的 YAML 配置文件已经成为了行业的绝对标准。
2. **托管便利**：机场可以在云端帮您配置好所有的分流规则和节点分组（如自动测速组、地区分组），您下载下来就能直接用，真正的“开箱即用傻瓜式体验”。

在接下来的教程中，我们将以目前最流行的 **Clash Verge Rev** 为例，教您如何导入订阅并进行高级测速。
