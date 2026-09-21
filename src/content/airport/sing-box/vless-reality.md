---
title: "如何在 sing-box 中配置 Vless Reality"
description: "剖析目前最强抗封锁协议 Vless Reality 在 sing-box 中的参数填写要点。"
order: 6
---

## 一、 Reality 协议简介

Reality 取代了传统的 TLS 证书机制，它不需要您拥有真实的域名，而是直接“偷取”大厂（如微软、苹果）的数字证书来伪装自己。这使得 GFW 根本无从下手。

## 二、 配置关键参数

在 sing-box 的 outbound 中配置 Reality，您必须填对三个核心参数：
1. `server_name` (SNI)：您要伪装的目标域名（如 `www.microsoft.com`）。
2. `public_key`：服务端生成的公钥。
3. `short_id`：短 ID，用于验证连接身份。

只要填对这三个参数，您的节点将坚如磐石。
