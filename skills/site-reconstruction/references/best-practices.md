# 最佳实践

## 一手来源优先

优先使用：

- Chrome DevTools 官方文档
- MDN
- Playwright 官方文档
- React / Tailwind / Router 等框架官方文档

## 运行时真源优先

高保真复刻时，运行时页面优先于：

- 保存页 HTML
- 低保真截图
- 主观记忆
- 本地近似实现

很多站点经过：

- SSR
- hydration
- 主题分支渲染
- source map
- 动画初始化
- 媒体查询分支

所以只看静态 HTML 往往不够。

## 反编译时优先直取源码

如果能从这些位置直接恢复内容，就不要重写：

- source map
- bundle
- network response
- 运行时 DOM
- SVG path
- 资源 URL
- CSS token
- 动画参数

原则不是“写得像”，而是“尽量把真实实现抽出来再组件化落地”。

## 用 computed style 核对状态

核对 hover / active / focus / open 时，不只看 class，要看最终样式值：

- `color`
- `background-color`
- `border-color`
- `box-shadow`
- `opacity`
- `filter`
- `transform`

## 截图回归必须分层

同时保留：

- 首屏图
- 整页图
- section 图
- 交互态图
- 移动端图

不要只看整页。

## 官方来源

- Chrome DevTools Inspect mode：`https://developer.chrome.com/docs/devtools/inspect-mode`
- Chrome DevTools CSS reference：`https://developer.chrome.com/docs/devtools/css/reference`
- Chrome DevTools source maps：`https://developer.chrome.com/docs/devtools/javascript/source-maps`
- Chrome DevTools overrides：`https://developer.chrome.com/docs/devtools/overrides`
- MDN `getComputedStyle()`：`https://developer.mozilla.org/en-US/docs/Web/API/Window/getComputedStyle`
- Playwright screenshots：`https://playwright.dev/docs/screenshots`
- Playwright visual comparisons：`https://playwright.dev/docs/test-snapshots`
- React 状态结构：`https://react.dev/learn/choosing-the-state-structure`
- Tailwind dark mode：`https://tailwindcss.com/docs/dark-mode`
