# Controls And Labels

本页规则以 web.dev Forms 和 MDN 原生表单语义为基线。

## 控件选择

- 优先使用 `input`、`select`、`textarea`、`button`
- 根据数据类型选择正确的 `type`、`inputmode` 和 `autocomplete`
- 同组单选或复选使用 `fieldset` 和 `legend`
- 提交动作保持真实 `submit` 语义

## 标签与说明

- 每个字段都应有可见标签
- 辅助说明与错误信息应通过程序化关系关联到字段
- 必填、可选、格式要求应在输入前可见
- 占位符不是标签

## 常见修正方向

- 把纯样式容器外层补上真实 `label`
- 把“请输入”类占位符改成说明文本
- 把字段组的标题从普通文本升级为 `legend`
- 让按钮文案直接描述动作，而不是只写“确定”
