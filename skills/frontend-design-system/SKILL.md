---
name: frontend-design-system
description: 当你需要搭建、扩展或审查前端设计系统时使用这个 skill。它聚焦 design token、组件契约、状态矩阵、文档化和治理规则，不负责单页性能优化、具体业务表单流程或端到端测试编排。
---

# Frontend Design System Skill

## 适用场景

这个 skill 用来处理前端设计系统相关工作，覆盖：

- design token 建模与分层
- 基础组件 API 与状态矩阵设计
- Storybook 或等价文档体系
- 组件库规范审查
- 设计系统变更治理

## 先读什么

按下面顺序读取：

1. `references/token-modeling.md`
2. `references/component-contracts.md`
3. `references/storybook-docs.md`
4. `references/governance.md`

这些 references 以 Design Tokens Format Module 和 Storybook 官方文档为基线。

## 开始前确认

- 当前仓库的 token 来源、主题机制和组件分层
- 哪些组件属于基础层，哪些已经被业务耦合污染
- 当前仓库真实可用的 Storybook、文档、测试和构建命令
- 当前变更是否会破坏现有组件契约

## 统一工作流

### 1. 先画清层级

- 区分基础 token、语义 token、组件 token
- 区分基础组件、组合组件和业务组件
- 明确每个组件的职责边界和消费者

### 2. 再收敛契约

- 组件 API 围绕意图和状态，不围绕临时样式参数
- 把必要状态、变体、槽位和可访问性要求显式建模
- 不要让同类组件长期分叉生长

### 3. 最后落文档与治理

- 为关键状态和变体补齐 stories 或等价文档
- 记录设计决策、禁用用法和迁移方向
- 如果决定破坏式调整，就在同一轮里统一迁移，不长期保留旧接口

## 专题检查点

- token 是否按语义分层，而不是直接暴露裸值
- 组件输入输出是否稳定、简洁、可解释
- 状态矩阵是否覆盖默认、禁用、错误、加载等真实场景
- 文档是否能让调用方知道何时用、何时不用
- 治理规则是否能阻止一次性分叉和样式漂移

## 验证与交付要求

- 说明本轮影响了哪些 token、组件契约或文档入口
- 至少运行与改动范围匹配的真实文档、测试或构建命令
- 如果存在未迁移完的调用方或未覆盖状态，要明确写出
