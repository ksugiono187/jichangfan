---
title: "sing-box TUN 模式开启与排错"
description: "解决无法创建虚拟网卡、DNS 泄露等 sing-box 桌面端常见问题。"
order: 8
---

## 一、 权限问题

在 Windows 上开启 sing-box 的 TUN 模式，必须以管理员权限运行程序，否则无法加载 WinTun 虚拟网卡驱动，导致核心启动失败崩溃。

## 二、 DNS 劫持

TUN 模式下最常见的问题是 DNS 无法正确解析。在 `inbounds` 中配置 TUN 时，务必确保 `auto_route` 和 `strict_route` 参数开启，并将系统的 DNS 请求强行劫持到 sing-box 的 DNS 引擎中进行处理，防止产生 DNS 污染泄露。
