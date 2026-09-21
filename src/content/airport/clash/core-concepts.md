---
title: "Clash 核心概念解析：Proxy、Rule 与 Provider"
description: "深入理解 Clash 的底层逻辑，搞懂代理组、规则和配置提供者的区别。"
order: 4
---

## 一、 代理 (Proxy) 与策略组 (Proxy Group)

在 Clash 中，每一个具体的服务器节点就是一个 Proxy。为了方便管理，Clash 引入了“策略组”的概念。
您可以将多个节点放入一个策略组中，并为其指定选择逻辑（如自动测速选择、手动选择、负载均衡等）。

## 二、 规则 (Rule)

Clash 强大的核心在于其分流规则。规则决定了您的网络请求是直接连接（DIRECT）、走代理（PROXY）还是被拦截（REJECT）。常见的规则类型包括域名匹配 (DOMAIN-SUFFIX)、IP 匹配 (IP-CIDR) 和地理位置匹配 (GEOIP)。

## 三、 Provider 机制

Provider 允许将节点列表或规则列表从主配置文件中分离出来，通过远程链接动态更新。这就是为什么您可以一键更新机场订阅，而不会覆盖您自己写的本地分流规则的原因。
