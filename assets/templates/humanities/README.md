# 文科报告模板

从本项目的 `report.tex`、`pack/neumain.tex` 和正式 Word 模板中提炼的通用课程实践、社会调研与人文社科报告模板。

## 开始使用

1. 复制整个文件夹作为新报告项目。
2. 打开 `report.tex`，修改顶部“1. 填写区”和“3. 封面与成员”。
3. 替换正文所有 `【填写】` 提示、示例图表、示例文献；按研究需要增删章节。
4. 选用 **XeLaTeX**，至少编译两次。正文页码、章节号、图表号和引用会自动更新。
5. 详细步骤及代码示例见同目录的 `使用手册.pdf`。

## 文件与版式

- `report.tex`：单文件主文档，包含格式、封面、写作框架和图表、引用示例。
- `fig/`：放报告图片。缺图时显示占位框；正式提交前替换或删去。
- `fonts/`：附原项目中的宋体、黑体及华文中宋；完整复制文件夹即可使用。
- `使用手册.pdf`：三页使用说明。

格式依据你提供的思政实践要求截图：

- A4；上下左右页边距均为 2.5 cm。
- 报告题目：华文中宋，小二号（18 pt），加粗。
- 正文：宋体，小四号（12 pt），1.5 倍行距。
- 章、节一级标题：黑体，小四号（12 pt）。
- 字符间距：标准，不增加字距或拉伸字符。
- 本次思政实践报告：不少于 5000 字。

模板另保留首行缩进两个字符、封面不计正文页码、正文从第 1 页开始等设置。

`fonts/simsun.ttc`、`fonts/simhei.ttf` 与 `fonts/STZHONGS.TTF` 已全部从原项目复制，完整文件夹编译时自动使用指定字体。缺少字体时，默认草稿模式会使用备用字体，不能视为满足指定字体要求。正式提交前，把 `report.tex` 中的 `\strictfontsfalse` 改为 `\strictfontstrue`；缺少指定字体时编译会报错，防止误用备用字体提交。文件名及大小写须一致。


## 编译

Overleaf：上传 `report.tex` 和图片，主文件设为 `report.tex`，编译器选择 XeLaTeX。

本地：已安装含中文支持的 TeX Live 或 MacTeX 时，在本文件夹运行：

```sh
xelatex -interaction=nonstopmode -halt-on-error report.tex
xelatex -interaction=nonstopmode -halt-on-error report.tex
```

不需要 BibTeX 或 Biber。`\cite{source1}` 与 `\bibitem{source1}` 配对。

备用字体与指定字体有差异；LaTeX 和 Word 的 1.5 倍行距算法也不同。正式提交请按实际课程要求核对字体、封面、页数与文献格式。
