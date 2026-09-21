---
title: "如何在 sing-box 中配置 Vless Reality"
description: "剖析目前最强抗封锁协议 Vless Reality 在 sing-box 中的参数填写要点。"
order: 6
---

## 一、 Reality 协议简介

Reality 取代了传统的 TLS 证书配置，不需要自己的域名，它通过模拟握手（Target 机制），向审查系统展示大厂（如微软或苹果）真实的公钥证书，从而隐藏代理的真实意图。

## 二、 配置关键参数

在 sing-box 的 outbound 中配置 Reality，您必须填对三个核心参数：
1. `server_name` (SNI)：您要伪装的目标域名（如 `www.microsoft.com`）。
2. `public_key`：服务端生成的公钥。
3. `short_id`：短 ID，用于验证连接身份。

只要填对这三个参数，您的节点将坚如磐石。
