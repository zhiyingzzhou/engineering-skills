# 执行检查清单

## 开始前

- 已确认目标站点属性与测试目标
- 如目标为外部第三方站点，已确认权限边界
- 已确认目标技术栈
- 已检测 DevTools MCP 是否可用
- 已检测 Playwright 是否可用
- 已锁定真实路由
- 已锁定主题与视口矩阵

## 采集阶段

- 抓标题、文案、按钮、链接
- 抓首屏图、整页图、section 图
- 抓关键交互态图
- 抓 computed style
- 抓资源路径
- 抓 bundle / source map / 静态资源

## 实现阶段

- 页面级内容源
- route-specific sections
- 低层 primitives
- 无模板注入
- 无兼容桥接层
- 交互状态单一拥有者

## 回归阶段

- `lint`
- `build`
- 同视口、同主题截图对比
- hover / active / focus / open 校对
- 动画节奏校对
- 不存在于远端的内容全部移除
