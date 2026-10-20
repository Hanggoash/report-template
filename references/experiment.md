# 实验报告

模板：`../assets/templates/experiment/main.tex`，复制整个 `experiment/`。详细组件见模板内 `README.md` 与 `使用手册.pdf`。

- `main.tex` 的个人配置区集中设置 `ReportTitle`、`ReportTopic`、`StudentName`、`StudentID`、`Supervisor`、`ReportDate`、`Institution` 等。修改已有定义，不重复定义同名命令。原日期为示例，应按实际填写。
- `images/logo.png` 是原模板保留的校徽；学校不同时更换或关闭 `ShowLogo`。学院和学校不能从校徽自行推断。
- 默认 A4、12pt、边距 2.5 cm、1.35 倍行距；使用 TeX 环境自带 Fandol，不需要复制其他模板的字体设置。
- 按任务调整“目的与任务、环境、设计与原理、实验过程、结果分析、问题解决、总结”。老师有指定结构时使用指定结构。
- 截图放 `images/`；用 `\ReportFigure[最大高度]{路径}{图注}{唯一标签}` 等比放置。缺图会出现占位框，因此编译通过不证明证据齐全。
- 结果分析要对应运行结果、参数、测试用例和截图。实验尚未执行时可先写方法、计划和报告骨架，结果留待补。
