# Intake 与工具检测

## Intake 顺序

开始前按这个顺序确认：

1. 目标站点是否为公司内部站点，以及测试用途是什么
2. 目标网站 URL
3. 目标技术栈
4. 是否要求纯组件化
5. 是否允许模板注入
6. 是否要求 1:1 还原全部页面与全部交互

## 站点属性与测试目标

默认按公司内部站点、内部模板资产、staging 环境、生产镜像处理，不把授权确认设为默认阻塞项。

开始前至少确认：

- 目标是否属于公司内部或其它可控资产
- 主要测试目标是白盒测试、黑盒测试、视觉回归、交互验证、DOM/CSS 结构分析还是源码还原

只有当目标明显是外部第三方站点时，才补充确认权限边界。

## 技术栈未指定时

必须先问，不要直接开始。

推荐选项：

- `React + Vite + Tailwind`
- `Vue + Vite + Tailwind`
- `Svelte / SvelteKit`
- `Astro`
- `HTML / CSS / JS`

## Chrome DevTools MCP 检测

判断标准：

- 当前环境是否暴露 DevTools MCP 能力
- 能否打开目标站
- 能否列页签
- 能否抓 snapshot
- 能否截图

如果以上都能做，视为可用。

## Playwright 检测

判断标准：

- 本地存在 `playwright` 或 `playwright-core`
- `playwright --version` 或 `npx playwright --version` 可执行

## 组合策略

### DevTools MCP + Playwright

最佳组合：

- DevTools 做反编译与运行时真源采集
- Playwright 做截图矩阵和回归

### 只有 DevTools MCP

可完成高保真复刻。  
截图回归可手动或后续补脚本。

### 只有 Playwright

可做：

- 批量截图
- 基础 DOM 采集
- 网络资源记录

但 CSS 交互态调试深度通常不如 DevTools。

### 两者都没有

降级到：

- HTML 快照
- bundle
- source map
- 静态资源
- 手工截图

必须明确告诉用户置信度更低。
