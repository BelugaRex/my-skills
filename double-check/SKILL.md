---
name: double-check
description: Enforce two consecutive validations after file changes such as code edits, refactors, deletions, documentation updates, or configuration changes. Use when the task modifies files and the agent should verify correctness before finishing.
---

# 双重验证 / Double Check

## 这个技能做什么 / What this skill does

- 对所有文件修改任务执行**两次连续验证**。  
  Applies **two consecutive validation runs** to file modification tasks.
- 降低“改完看起来没问题，其实一跑就炸”的概率。  
  Reduces the chance of changes that look fine but break at build, test, or run time.
- 适用于代码、文档、配置、脚本和功能删除。  
  Works for code, documentation, configuration, scripts, and feature removal.

## 什么时候使用 / When to use this skill

在以下情况应自动使用：  
Use this skill automatically when:

- 用户要求新增、修改、删除、重构任何文件。  
  The user asks to add, modify, delete, or refactor files.
- 任务需要“改完后确认没问题”。  
  The task requires confidence that the change still works.
- 项目存在测试、构建、运行、类型检查、lint 或文档校验流程。  
  The project has tests, builds, runtime checks, type checks, linting, or documentation validation.

## 核心规则 / Core rules

1. 改动前先进行一次 commit，再开始新的文件改动。  
  Make one commit before editing, then start new file changes.
2. 修改文件后，必须验证。  
  After changing files, always validate.
3. 必须使用**同一类验证方式连续成功两次**。  
   The **same validation method must succeed twice in a row**.
4. 如果第一次或第二次失败，都要修正后重新从第一次开始。  
   If either run fails, fix the issue and restart from the first validation.
5. 两次验证之间不能再插入新的文件修改。  
   Do not make new edits between the two validation runs.
6. 验证通过后必须立即提交 commit，避免累计大量未提交改动。  
  Commit immediately after validation passes; avoid accumulating large uncommitted changes.
7. 提交信息遵循规范：前缀（feat/fix/chore/perf/refactor 等）+ 中英双语描述。  
  Commit messages must follow the format: prefix (feat/fix/chore/perf/refactor, etc.) + bilingual (CN/EN) description.
8. 如果没有标准验证命令，要和用户确认替代方案，并说明局限性。  
   If no standard validation command exists, agree on an alternative with the user and explain the limitations.

## 工作流程 / Workflow

### 0. 改动前先提交 / Pre-change commit first
- 在开始新改动前先提交一次当前改动，不要带着大量未提交变更继续开发。  
  Before starting new edits, make one commit of current changes; do not continue with large uncommitted diffs.
- 提交信息遵循“前缀 + 英文描述 / 中文描述”规范。  
  Commit message must follow: "prefix + English description / Chinese description".

### 1. 识别改动范围 / Identify the change scope
- 明确这次改了哪些文件、改动属于哪一类。  
  Identify which files changed and what kind of change it is.

### 2. 选择验证方式 / Choose the validation method
- 优先选标准命令，例如测试、构建、lint、类型检查、文档构建。  
  Prefer standard commands such as tests, builds, lint, type checks, or doc builds.
- 若有多个选项，优先选最能覆盖改动风险的那一个。  
  If multiple options exist, choose the one that best covers the risk of the change.

### 3. 第一次验证 / First validation
- 运行命令并记录结果。  
  Run the command and record the result.
- 失败则修复并回到第一次验证。  
  If it fails, fix the issue and return to the first validation.

### 4. 第二次验证 / Second validation
- 立即用**相同命令、相同参数、相同环境**再次运行。  
  Immediately run the **same command, same parameters, same environment** again.
- 只有第二次也成功，任务才算真正完成。  
  The task is complete only if the second run also succeeds.

### 5. 立即提交 / Commit immediately
- 两次验证都通过后，立刻提交本次改动。  
  After both validations pass, commit the current change immediately.
- 提交信息使用“前缀 + 英文描述 / 中文描述”格式。  
  Use the format "prefix + English description / Chinese description".
- 推荐示例：`fix: resolve image loading issue / 修复图片加载问题`。  
  Recommended example: `fix: resolve image loading issue / 修复图片加载问题`.

## 验证方式选择建议 / Validation method guide

- **有测试时**：优先跑测试。  
  **If tests exist**: prefer running tests.
- **无测试但可构建**：跑构建或类型检查。  
  **If no tests but the project builds**: run the build or type check.
- **无测试无构建但可运行**：运行主程序或最接近真实使用路径的命令。  
  **If no tests or build but the app can run**: run the main program or the closest real usage path.
- **文档或配置改动**：优先跑文档构建、配置校验、格式校验。  
  **For docs or config changes**: prefer doc build, config validation, or formatting checks.

## 向用户汇报时应包含 / Report to the user with

- 改动前 commit 情况（是否已提交、提交信息）。  
  Pre-change commit status (whether committed and the commit message).
- 改了什么。  
  What changed.
- 用什么命令验证。  
  Which command was used for validation.
- 第一次结果。  
  The first validation result.
- 第二次结果。  
  The second validation result.
- commit 是否已完成，以及提交信息。  
  Whether commit is completed, and the commit message used.
- 如果验证方式有限，要明确风险边界。  
  If the validation is limited, clearly state the risk boundary.

## 常见边界情况 / Common edge cases

- **删除功能**：别忘了清理调用、导入、配置和文档引用。  
  **Feature removal**: also clean up calls, imports, configuration, and docs references.
- **没有标准命令**：先说明限制，再征得用户同意。  
  **No standard command**: explain the limitation first and get user agreement.
- **命令依赖缓存**：尽量避免使用可能造成假阳性的缓存结果。  
  **Cached commands**: avoid cache-dependent passes when possible.
- **命令超时或环境缺失**：说明阻塞原因并给出替代验证建议。  
  **Timeouts or missing environment**: explain the blocker and propose an alternative validation path.

## 简短示例 / Short example

**任务 / Task**：修复一个前端表单校验 bug。  
**推荐流程 / Recommended flow**：

1. 先提交一次当前改动。  
  Make one commit of current changes first.
2. 修改相关文件。  
   Edit the relevant files.
3. 运行测试或构建。  
   Run tests or the build.
4. 通过后，立刻再跑一次同样的命令。  
   If it passes, immediately run the same command again.
5. 两次都通过后立即提交，提交信息遵循双语前缀规范。  
  Commit immediately after both passes, following the bilingual prefix convention.

---

> **记住：一次通过是好消息，两次通过才是交付信号。**  
> **Remember: one pass is encouraging; two passes are a delivery signal.**
