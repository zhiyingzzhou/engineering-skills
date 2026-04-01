---
name: frontend-accessibility
description: 当你需要为前端界面实现、修复或审查可访问性时使用这个 skill。它聚焦语义化 HTML、键盘导航、focus 管理、名称与状态表达、ARIA 使用边界和复杂交互模式，不负责通用表单流程、性能优化或设计系统治理。
---

# Frontend Accessibility Skill

## 适用场景

这个 skill 用来处理前端可访问性相关工作，覆盖：

- 可访问性缺陷修复
- 语义化 HTML 整改
- 键盘导航与 focus 问题排查
- 对话框、菜单、标签页等复杂交互模式审查
- PR 或页面的无障碍 review

## 先读什么

按下面顺序读取：

1. `references/semantic-html.md`
2. `references/focus-and-keyboard.md`
3. `references/aria-and-patterns.md`
4. `references/audit-checklist.md`

这些 references 以 MDN 和 WAI-ARIA Authoring Practices Guide 为基线。

## 开始前确认

- 当前任务涉及哪些页面、组件或交互模式
- 现有实现里哪些元素承担了交互职责
- 当前仓库真实可用的 lint、test、e2e 或手工验证命令
- 是否已有设计系统或基础组件可复用

## 统一工作流

### 1. 建立当前语义与交互基线

- 先确认真实 DOM 结构、标题层级、landmark、交互元素类型
- 再走一遍键盘路径：Tab、Shift+Tab、Enter、Space、Escape、方向键
- 如果是复杂组件，确认是否已有可复用模式，而不是临时发明新交互

### 2. 再按风险高低整改

- 先修真正阻塞使用的问题：无法聚焦、无法触发、状态不明、读屏无名
- 原生语义能解决的不要改成 ARIA 组件
- 所有 `aria-*` 状态都必须与真实行为同步

### 3. 最后做回归验证

- 验证键盘可达、焦点顺序、可见 focus 和状态变化
- 验证名称、角色、状态是否对读屏软件有意义
- 如果只能做静态审查，要明确未做的真实交互验证

## 专题检查点

- 语义元素优先于 `div`/`span` 拼交互
- 可见文本、可访问名称和控件职责要一致
- 焦点进入、移动、关闭和返回路径必须可预期
- 复杂 widget 只在原生语义不够时才使用 APG 模式
- 异步反馈、展开折叠、选中状态必须能被感知

## 验证与交付要求

- 说明本轮影响了哪些语义、角色、状态或键盘行为
- 至少运行与改动范围匹配的真实验证命令，或完成一次键盘路径核对
- 如果未验证读屏、放大或高对比场景，要明确写出缺口
