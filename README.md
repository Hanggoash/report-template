# report-template

个人课程任务工作流技能：接收老师的要求文档或截图，讨论方案和执行分工，完成任务、收集证据，再用内置 TeX 模板撰写、修缮和编译报告。

包含实验报告、文科实践或调研报告、学术汇报 Beamer 三套模板，连同字体、图片和原使用手册一起保存。支持 Agent 自动执行、用户手动操作并提供截图、以及混合协作。

## 安装与触发

本仓库根目录就是一个完整的技能目录。将它安装到 agent 的技能目录，或在本机建立符号链接。例如，本仓库位于桌面 `develop` 中时：

```sh
mkdir -p ~/.codex/skills
ln -s ~/Desktop/develop/report-template ~/.codex/skills/report-template
```

如果目标位置已存在，先检查现有技能，不要覆盖。不同客户端的技能目录和重新加载方式以实际环境为准；如新技能暂未出现，可在重新加载技能或新会话后检查。

触发示例：

```text
$report-template 这是数据库实验三的要求，先和我讨论方案。
$report-template 使用文科模板；我已有调研照片，先整理提纲。
$report-template 根据这份报告做一个 8 分钟的 Beamer 汇报。
$report-template 继续“数据库实验三”，下面是我刚完成的截图。
```

技能内容见 [SKILL.md](SKILL.md)。它不包含模型服务，也不改变会话的文件权限；需要由支持技能与文件操作的 agent 执行。

## 三种执行模式怎么选

三种模式的区别是实验、代码实现、数据处理、调研等核心任务由谁执行。无论选择哪种模式，Agent 都可以根据真实材料帮你写报告、排版、修缮和编译。

| 模式 | 你负责什么 | Agent 负责什么 | 适用场景 |
| --- | --- | --- | --- |
| `automatic` 自动执行 | 提供要求和必要材料，讨论方案、审阅成果 | 在环境和授权允许的范围内完成核心任务、运行验证、保存证据并制作报告 | 希望将可自动完成的任务交给 Agent，当前环境能够支持执行 |
| `guided` 手动引导 | 亲自完成核心操作，反馈结果并按要求截图 | 分步讲解、给出预期结果和截图提示、核对与排错，最后整理报告 | 希望学会操作，或课程要求自己完成实验 |
| `hybrid` 混合协作 | 完成分配给自己的核心任务，例如在专用环境运行程序、操作设备或采集数据 | 完成分配给它的核心任务，例如实现代码、处理数据或分析结果，再汇总报告 | 希望双方分工，或部分操作只能由你在学校环境中完成 |

以数据库实验为例：

- **自动执行**：Agent 编写 SQL，在可用的数据库环境执行，验证结果并整理报告。
- **手动引导**：Agent 解释并分步指导，你编写 SQL、执行、根据提示截图；Agent 核对结果并整理报告。
- **混合协作**：Agent 编写 SQL，你在学校数据库环境执行和截图，Agent 根据运行结果修改代码、分析并整理报告。

Agent 提供讲解、示例和排错建议，仍可以是手动引导；如果它接手整块可交付代码，而你主要负责运行和截图，就更接近混合协作。仅仅提供已有材料、审阅成果，或让 Agent 帮忙写报告，不会自动把任务变成混合模式。

你可以直接用自然语言选择，不必记英文名称：

```text
$report-template 先讨论方案，确定后由你自动执行并验证。
$report-template 我想自己完成实验，请分步指导，并告诉我在哪里截图。
$report-template 你负责实现代码，我在学校环境运行和截图，我们分工完成。
```

也可以先讨论再决定。目录工具默认的 `undecided` 表示尚未确定分工，不是第四种执行模式。中途可以改为其他模式，例如“第一部分我已经学会了，后面的代码交给你”；Agent 会更新分工和进度记录。自动执行遇到环境或设备限制时，Agent 会说明缺口并与你调整分工。

## 新作业目录

Agent 可以调用辅助工具复制完整模板并建立进度记录；用户也可直接运行：

```sh
python3 scripts/create_project.py --template experiment --title '数据库实验三'
python3 scripts/create_project.py --template humanities --title '社会实践报告' --mode guided
python3 scripts/create_project.py --template beamer --title '课程汇报' --output-root '/你指定的目录'
```

默认根目录是 `~/Desktop/College/课程作业`，也可设置 `REPORT_TEMPLATE_OUTPUT_ROOT`。目录名默认为“日期-任务名称”，重名会报错，不覆盖已有任务；用 `--directory-name` 指定其他单层名称。

```text
日期-任务名称/
├── task.json        任务、模板、执行模式与阶段
├── workflow.md      要求、方案、进度、证据索引与下一步
├── materials/       老师要求和原始资料
├── evidence/        截图、原始数据和运行证据
├── work/            代码与其他工作文件
├── report/          完整模板副本、字体和正文图片
└── deliverables/    最终 PDF 和提交包
```

## 模板与编译

| 模板选项 | 用途 | 主文件 | 字体 |
| --- | --- | --- | --- |
| `experiment` | 实验、编程、课程设计 | `main.tex` | TeX 环境自带 Fandol |
| `humanities` | 文科实践、调研 | `report.tex` | 随附宋体、黑体、华文中宋 |
| `beamer` | 16:9 学术或课堂汇报 | `main.tex` | 随附思源黑体 CN |

需要支持中文的 XeLaTeX 环境，例如 TeX Live / MacTeX，或支持完整项目的在线/应用内编译器。模板和字体并不包含完整 TeX 发行版。通常在任务的 `report/` 中用 `latexmk -xelatex main.tex`；文科报告改用 `report.tex`。

老师当前要求优先于模板历史说明；模板中的“5000 字”等示例不自动适用于新任务。缺少实验、调研证据时保留待补状态，不生成虚构结果。

## 维护与验证

修改 `assets/templates/` 会影响之后新建的作业；已经建立的作业副本不会随之改变。

```sh
python3 scripts/check_assets.py
python3 -m unittest discover -s tests -v
```

字体、校徽与原手册按来源保留。本仓库没有为所有资源统一授予再分发许可；思源黑体的许可位于其 `fonts/LICENSE.txt`。其他字体未附许可文本，使用与分享时沿用各自原有授权。本项目初始以私有仓库保存。
