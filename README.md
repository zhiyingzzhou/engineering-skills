# engineering-skills

这是我的个人技能库仓库，用来沉淀可被 AI agent 直接调用的 `skills`。

仓库里的每个 skill 都是一个独立能力单元，目标不是保存零散笔记，而是把一类任务的触发条件、工作流、检查点和参考资料整理成可复用的执行规范。当前这批内容主要聚焦前端通用工程能力。

## 这个仓库解决什么问题

- 把高频工程经验沉淀成结构化 skill，而不是散落在聊天记录里
- 让不同主题的能力按目录独立维护，避免一个“大而全入口”持续膨胀
- 把最佳实践和执行步骤拆开：`SKILL.md` 保持精简，细节沉到 `references/`
- 让后续新增 skill 时有统一骨架，不需要每次从零设计

## 目录结构

```text
.
├── README.md
└── skills/
    ├── <skill-name>/
    │   ├── SKILL.md
    │   ├── agents/
    │   │   └── openai.yaml
    │   └── references/
    │       └── *.md
```

约定如下：

- `SKILL.md`：定义 skill 的适用场景、工作流、检查点和交付要求
- `agents/openai.yaml`：定义 UI 展示信息和默认 prompt
- `references/`：保存专题最佳实践、检查清单和细分规则

## 当前已收录的前端 skills

- `frontend-accessibility`：可访问性、语义化 HTML、键盘导航、focus、ARIA 模式
- `frontend-forms`：表单控件、标签、校验、错误反馈、autofill
- `frontend-responsive-layout`：响应式布局、断点、尺寸约束、溢出、媒体适配
- `frontend-performance`：Core Web Vitals、关键渲染路径、预算、性能回归
- `frontend-testing`：测试分层、DOM 测试、E2E、稳定 locator、flaky 治理
- `frontend-design-system`：design token、组件契约、Storybook 文档、治理规则

## 设计原则

- 所有 skill 平级独立，不设总入口
- 采用彻底切换，不做向后兼容式重复维护
- 一个 skill 只负责一个清晰主题，边界冲突时直接拆开
- `SKILL.md` 只保留高层流程，详细知识放进 `references/`
- 最佳实践优先参考官方或准官方资料，再抽象成可执行规则

## 适合怎么继续扩展

后续新增 skill 时，优先补真正高频、边界清晰、可独立触发的主题，例如：

- CSS 架构
- 数据获取与缓存
- 组件架构
- 动画与动效
- 前端安全
- 国际化与本地化

每次新增时，优先保证：

- 名称能准确触发
- 描述能说清“该用时机”和“不负责什么”
- `references/` 的拆分是一层结构，不做多层嵌套
- 最终能直接被 agent 使用，而不只是人类阅读
