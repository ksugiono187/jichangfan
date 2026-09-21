---
title: "如何在 Clash 中自定义分流规则"
description: "教您手写 Clash 规则，让特定网站或软件强行直连或走指定节点。"
order: 6
---

## 一、 YAML 语法基础

Clash 的配置文件使用 YAML 格式。在 `rules:` 字段下，规则的匹配优先级是从上到下的。一旦匹配命中，后续规则将不再执行。

## 二、 常用分流规则示例

*   `DOMAIN-SUFFIX,openai.com,美国节点`：让所有 ChatGPT 的请求强制走“美国节点”策略组。
*   `DOMAIN-KEYWORD,baidu,DIRECT`：只要域名包含 baidu，就直连。
*   `IP-CIDR,192.168.0.0/16,DIRECT`：局域网 IP 直连，保证您能正常访问家里的路由器后台。

## 三、 规则集的引用

为了避免配置文件过于臃肿，推荐使用 `rule-providers` 引用各大开源社区维护的规则集（如 Loyalsoldier 规则集）。
