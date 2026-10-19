#!/usr/bin/env python3
"""Copy a bundled template into a new, non-overwriting coursework project."""

import argparse
from datetime import datetime
import json
import os
from pathlib import Path
import re
import shutil
import sys

SKILL_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = SKILL_ROOT / "assets" / "templates"
TEMPLATES = {"experiment": "main.tex", "humanities": "report.tex", "beamer": "main.tex"}
MODES = ("undecided", "automatic", "guided", "hybrid")


def directory_name(value):
    if (not value or value in (".", "..") or len(value) > 120
            or value != value.strip() or any(c in value for c in '/\\\x00')
            or any(ord(c) < 32 for c in value)):
        raise ValueError("目录名必须是 1–120 个字符的单层名称，不能包含路径分隔符或控制字符。")
    return value


def create_project(template, title, output_root, mode="undecided", name=None):
    if template not in TEMPLATES:
        raise ValueError("未知模板类型。")
    if mode not in MODES:
        raise ValueError("未知执行模式。")
    title = title.strip()
    if not title or any(ord(c) < 32 for c in title):
        raise ValueError("任务题目不能为空或包含控制字符。")
    source = TEMPLATE_ROOT / template
    if not (source / TEMPLATES[template]).is_file():
        raise ValueError("模板缺少主文档，请检查技能资源。")
    now = datetime.now().astimezone()
    slug = re.sub(r"[^\w\-]+", "-", title, flags=re.UNICODE).strip("-_")[:90] or "report"
    name = directory_name(name if name is not None else now.strftime("%Y-%m-%d-") + slug)
    root = Path(output_root).expanduser().resolve()
    if root == SKILL_ROOT or SKILL_ROOT in root.parents:
        raise ValueError("作业目录应位于技能仓库之外，以保留模板原件。")
    root.mkdir(parents=True, exist_ok=True)
    project = root / name
    # mkdir is exclusive, including when another process creates this name first.
    project.mkdir(exist_ok=False)
    shutil.copytree(source, project / "report", ignore=shutil.ignore_patterns(
        ".DS_Store", "._*", "*.aux", "*.log", "*.out", "*.toc", "*.nav",
        "*.snm", "*.fls", "*.fdb_latexmk", "*.synctex.gz"))
    for folder in ("materials", "evidence", "work", "deliverables"):
        (project / folder).mkdir()
    task = {
        "schema_version": 1,
        "title": title,
        "template": template,
        "mode": mode,
        "stage": "intake",
        "created_at": now.isoformat(timespec="seconds"),
        "main_file": "report/" + TEMPLATES[template],
    }
    (project / "task.json").write_text(json.dumps(task, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    workflow = f"""# {title}

## 当前状态

- 阶段：接收要求
- 执行模式：{mode}
- 主文件：report/{TEMPLATES[template]}
- 当前阻碍：尚未整理任务要求

## 要求与来源

记录每项要求、原始材料的页码或截图名称、对应成果和验证方式。

| 要求 | 来源 | 对应成果 | 状态 |
| --- | --- | --- | --- |

## 已确定的方案与分工

记录用户已决定的方案、Agent 与用户各自负责的步骤及后续调整。

## 进度与实际结果

记录已完成的操作、参数、验证结果以及未解决的问题。

## 证据索引

| 文件 | 对应要求 | 操作或参数 | 支持的结论 |
| --- | --- | --- | --- |

## 下一步与待补材料

- 读取老师的要求和用户提供的资料，整理方案与待核实项。

## 交付与验证

尚未编译或交付。本目录中的报告仍是模板副本，示例内容与占位符不代表实际成果。
"""
    (project / "workflow.md").write_text(workflow, encoding="utf-8")
    return project


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--template", required=True, choices=TEMPLATES)
    parser.add_argument("--title", required=True)
    parser.add_argument("--mode", default="undecided", choices=MODES)
    parser.add_argument("--output-root", default=os.environ.get(
        "REPORT_TEMPLATE_OUTPUT_ROOT", str(Path.home() / "Desktop" / "College" / "课程作业")))
    parser.add_argument("--directory-name")
    args = parser.parse_args()
    try:
        project = create_project(args.template, args.title, args.output_root, args.mode, args.directory_name)
    except FileExistsError:
        parser.exit(2, "错误：目标已存在，未覆盖；请继续已有任务或指定其他目录名。\n")
    except (ValueError, OSError) as exc:
        parser.exit(2, f"错误：{exc}；若创建中途失败，请检查目标中的部分文件。\n")
    print(json.dumps({"project": str(project), "main_file": str(project / "report" / TEMPLATES[args.template])}, ensure_ascii=False))


if __name__ == "__main__":
    sys.exit(main())
