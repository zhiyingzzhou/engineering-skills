# ARIA And Patterns

本页规则以 WAI-ARIA Authoring Practices Guide 为基线。

## 使用边界

- 原生语义够用时，不要追加多余 `role`
- `aria-label`、`aria-labelledby`、`aria-describedby` 只解决命名和说明问题
- `aria-expanded`、`aria-selected`、`aria-pressed` 等状态必须反映真实 UI 状态
- 不要让 `role` 与元素的真实行为互相矛盾

## 复杂模式

- `dialog`：需要清晰标题、焦点管理和关闭路径
- `tablist`：需要可感知的激活项和方向键移动
- `menu` / `listbox`：只在真正的应用式复合控件中使用
- `accordion`：触发按钮应暴露展开状态和关联区域

## 常见误用

- 用 `role="button"` 替代原生 `button`
- 给静态内容乱加 `aria-hidden="true"`
- 用 live region 持续广播所有状态变化
- 只改视觉选中样式，不同步可访问状态
