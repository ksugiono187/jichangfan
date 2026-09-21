---
title: "sing-box 路由规则 (Route) 编写指南"
description: "掌握 sing-box 的 rule_set 机制，实现精准的国内外流量分流。"
order: 4
---

## 一、 Rule 的基本写法

在 `route.rules` 数组中，每一项都是一个匹配条件。例如 `{"domain_suffix": [".cn"], "outbound": "direct"}`，意为所有国内域名直接发送到直连出站。

## 二、 Rule Set (规则集)

为了避免把上万个域名写在配置文件里，sing-box 引入了 Rule Set (SRS 格式文件)。这是经过二进制预编译的规则数据库，加载速度极快，内存占用极低，是 sing-box 性能强悍的秘诀之一。

## 三、 默认路由

如果所有规则都没有命中，流量将走向您配置的 `auto_detect_interface` 或排在出站列表第一位的 outbound。
