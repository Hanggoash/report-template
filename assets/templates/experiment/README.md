# 实验报告模板

主文件：`main.tex`。完整使用方法见 `使用手册.pdf`。

## 开始使用

1. 复制整个“实验报告模板”文件夹，为每份报告保留独立副本。
2. 在 `main.tex` 的“个人配置”中修改课程、题目、姓名、学号、教师、日期和学院。
3. 替换正文示例，增删章节；将实验截图放入 `images/`。
4. 使用 **XeLaTeX** 编译两次，更新目录、公式编号和文献引用。

Overleaf：上传 `main.tex` 与 `images/`，主文件设为 `main.tex`，编译器选择 XeLaTeX。也可上传完整文件夹的 ZIP。无需单独上传字体。

本地已有 TeX Live 或 MacTeX 时，在模板文件夹中运行：

```sh
xelatex -interaction=nonstopmode -halt-on-error main.tex
xelatex -interaction=nonstopmode -halt-on-error main.tex
```

若已安装 latexmk，也可用 `latexmk -xelatex main.tex` 自动完成多轮编译。

## 文件结构

```text
实验报告模板/
  main.tex                        配置、样式、组件和正文
  images/
    logo.png                      从原报告保留的校徽
  使用手册.pdf          简明操作手册
  README.md                       快速开始与模板说明
```

`verification.png` 没有附带，是有意保留的图片占位路径。上传自己的同名截图即可显示；也可以修改调用中的路径。

## 从三个原报告保留与统一的内容

- 保留 `ctexart`、A4、12pt、四边 2.5cm、1.35 倍行距、居中封面信息栏，以及带边框和行号的代码块。
- 保留原校徽与学院名称；姓名、学号、教师、项目题目、实验结果均替换为占位内容。
- 将课程报告、实训报告、研究型实验统一为“目的与任务、环境、设计与原理、实验过程、结果分析、问题解决、总结”骨架；按课程实际要求调整节名。
- 统一使用三线表。截图默认 `[H]` 放在源码当前位置；实际图片等比缩放，缺图显示占位框。
- 参考 beamer 模板的集中配置和单文件文献用法；无需 `.bib` 文件、BibTeX 或 Biber。

## 常改设置

| 设置 | 用法 |
| --- | --- |
| 报告名称、题目等 | 修改 `ReportTitle`、`ReportTopic` 等已有定义 |
| 无独立实验题目 | `\ShowTopicfalse` |
| 显示封面摘要 / 自评 | `\ShowSummarytrue`，再修改 `SummaryLabel` 与 `ReportSummary` |
| 不显示校徽 | `\ShowLogofalse` |
| 不显示目录 | `\ShowContentsfalse` |
| 仓库地址 | 修改 `RepositoryURL`，空内容自动隐藏 |
| 图片高度 | `\ReportFigure[5cm]{images/xxx.png}{图注}{fig:xxx}` |

学校名称很长、题目超过两行、封面摘要超过 150 字时，检查封面是否溢出。必要时缩短文本或减少封面宏中的 `\vspace`。

## 字体与预览

中文显式使用 TeX Live 自带的 Fandol 字体，保持宋体正文、黑体标题的报告风格，避免依赖本机字体。不要把 beamer 模板的 `fonts/` 或字体初始化代码复制过来。

源码已通过 Codex 内置编译器检查。内置编译器只检查单个 `.tex` 文件：封面校徽用学院文字替代，正文外部图片用占位框替代。校徽与实际截图的最终效果请在完整 Overleaf 或本地项目中检查。

## 交稿前

删除写作提示、示例代码、占位文献和“待填写”；换成真实实验内容。确认目录完整、图表不越界、引用没有问号、封面只有一页。不要将占位框视作实际实验截图。
