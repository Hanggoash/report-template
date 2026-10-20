# 实验报告

模板：`../assets/templates/experiment/main.tex`，复制整个 `experiment/`。详细组件见模板内 `README.md` 与 `使用手册.pdf`。

- `main.tex` 的个人配置区集中设置 `ReportTitle`、`ReportTopic`、`StudentName`、`StudentID`、`Supervisor`、`ReportDate`、`Institution` 等。修改已有定义，不重复定义同名命令。原日期为示例，应按实际填写。
- 封面默认显示校徽占位符；用户提供校徽后放到 `images/logo.png`，或修改 `LogoFile`。不需要校徽区域时关闭 `ShowLogo`。学校和学院名称向用户确认。
- 默认 A4、12pt、边距 2.5 cm、1.35 倍行距；使用 TeX 环境自带 Fandol，不需要复制其他模板的字体设置。
- 按任务调整“目的与任务、环境、设计与原理、实验过程、结果分析、问题解决、总结”。老师有指定结构时使用指定结构。
- 截图放 `images/`；用 `\ReportFigure[最大高度]{路径}{图注}{唯一标签}` 等比放置。缺图会出现占位框，因此编译通过不证明证据齐全。
- 结果分析要对应运行结果、参数、测试用例和截图。实验尚未执行时可先写方法、计划和报告骨架，结果留待补。
