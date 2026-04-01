# Autofill

本页规则以 web.dev Autofill 建议为基线。

## 基础原则

- 为常见字段提供正确的 `autocomplete` token
- 认证字段要兼容密码管理器和一次性验证码
- 字段命名、顺序和分组尽量稳定
- 不要用脚本阻断浏览器自动填充

## 常见字段

- 身份信息：`name`、`given-name`、`family-name`
- 联系方式：`email`、`tel`
- 地址：`street-address`、`address-level1`、`postal-code`
- 认证：`username`、`current-password`、`new-password`、`one-time-code`

## 常见误区

- 多个字段复用同一个错误 `autocomplete`
- 为了样式把真实输入拆得过碎
- 登录页不区分用户名和新密码场景
- 提交前用脚本重写字段值导致密码管理器失效
