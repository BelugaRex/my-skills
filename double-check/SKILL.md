---
name: double-check
description: 在修改任何文件后（包括删除功能），自动进行两次独立验证（测试/编译/运行检查/文档或配置检查），确保无误才结束。本技能应默认应用于所有文件修改任务。 / After any file changes (including feature removal), automatically perform two independent verifications (tests/compilation/runtime checks/docs or config checks) to ensure correctness. This skill should be applied by default to any file modification task.
author: BelugaRex
tags: [coding, testing, verification, quality-assurance, bilingual]
---

# 双重验证技能 / Double-Check Skill

## 📌 关于本技能 / About This Skill

本技能适用于**任何文件修改场景**，包括代码、文档、配置、资源文件的添加、修改、删除、重构与更新等。
This skill applies to **any file modification scenario**, including adding, editing, deleting, refactoring, or updating code, documentation, configuration, and resource files.

**核心要求**：只要用户请求修改任何文件，AI 应**自动应用本技能**，并在每次修改后执行以下双重验证流程。
**Core requirement**: Whenever the user asks to modify any file, the AI should **automatically apply this skill** and perform the following double-check workflow after each change.

**激活标识**：每次启用本技能的回复以 ✅✅ 开头，便于你确认本技能已被调用。
**Activation marker**: Every reply using this skill should begin with ✅✅ so you can tell it has been activated.

- **连续两次验证**：修改后立即进行两次验证，**两次均无错误**才能结束。
  **Two consecutive validations**: Run validation twice immediately after the change, and finish only if **both runs succeed without errors**.
- **同样严谨**：两次验证使用相同的方式（如相同的测试命令或运行命令），确保结果可靠。
  **Same level of rigor**: Use the same validation method both times (for example, the same test or run command) to ensure reliable results.
- **自动触发**：无需用户额外提示，AI 应主动遵循本流程。
  **Automatic trigger**: The AI should follow this process proactively without waiting for extra user instructions.
- **验证目标**：确保修改后的文件变更能够**顺利通过对应检查**（无编译/运行/构建/文档校验错误，且原有功能或内容不受影响）。
  **Validation goal**: Ensure that the modified files **pass the relevant checks** successfully (no compile/runtime/build/documentation-validation errors, and no unintended breakage to existing behavior or content).

## 📌 适用场景 / Applicable Scenarios

本技能应默认应用于所有涉及文件修改的请求，包括但不限于：
This skill should be applied by default to all requests that involve file modifications, including but not limited to:

- **修复 Bug** 后运行测试用例或运行程序检查。  
  Run tests or execute the program after **fixing a bug**.
- **添加新功能**后确保原有功能正常。  
  Make sure existing behavior still works after **adding a new feature**.
- **删除功能**后验证剩余代码是否能顺利运行，无残留错误。  
  Verify that the remaining code still runs correctly after **removing a feature**, with no leftover errors.
- **重构代码**后检查编译/类型错误或运行程序。  
  Check for compile/type errors or run the program after **refactoring code**.
- **调整代码风格**后验证 lint 规则。  
  Validate lint rules after **style cleanup**.
- **更新依赖**后检查构建是否正常。  
  Confirm the build still works after **updating dependencies**.
- **更新文档**后验证文档构建或校验规则。  
  Validate documentation builds or checks after **updating docs**.
- **修改配置**后验证构建/运行流程是否正常。  
  Validate build/run flows after **changing configuration**.
- 任何其他文件变更后需要保证正确性的任务。  
  Any other task where correctness must be preserved after a file change.

## 🧠 核心原则 / Core Principles

1. **自动应用**：AI 应识别出“修改文件”的意图，并自动激活本技能。  
   **Automatic application**: The AI should recognize the intent to modify files and activate this skill automatically.
2. **修改 → 验证 → 修正 → 再验证**：任何文件修改都必须经过验证环节。  
   **Change → validate → fix → validate again**: Every file modification must go through validation.
3. **两次连续成功**：必须连续两次验证均无错误，才能视为最终成功。  
   **Two consecutive successes**: Only treat the task as complete after two successful validation runs in a row.
4. **同样严谨**：两次验证采用**完全相同的方式**（例如都运行 `npm test` 或 `python main.py`），确保一致性。  
   **Same rigor**: Use the **exact same method** for both validations (for example, `npm test` twice or `python main.py` twice) to ensure consistency.
5. **独立验证**：尽管命令相同，但两次运行在逻辑上是独立的（例如不使用缓存结果，或使用 `--no-cache` 等选项），避免偶然因素。  
   **Independent validation**: Even if the command is the same, the two runs should be logically independent (for example, avoid cached results or use options such as `--no-cache`) to reduce accidental passes.
6. **清晰报告**：每次验证后向用户报告结果（成功/失败，错误详情）。  
   **Clear reporting**: Report the result of each validation to the user (success/failure and relevant error details).

## 📋 执行步骤 / Execution Steps

### 1. 理解任务 / Understand the Task
- 明确用户希望修改的文件（增、删、改、重构等）。  
  Identify which files the user wants to modify (add, delete, update, refactor, and so on).
- 确认项目类型和可用的验证方式（测试命令、构建命令、运行命令、文档/配置检查等）。  
  Determine the project type and available validation methods (test commands, build commands, run commands, documentation/config checks, and so on).

### 2. 执行修改 / Make the Change
- 按照用户要求修改文件（包括删除功能时，需一并移除相关调用、引用等）。  
  Modify the files according to the user’s request (including removing related calls, imports, and references when deleting a feature).
- 记录修改内容（便于回溯）。  
  Keep track of what was changed for traceability.

### 3. 确定验证方式 / Choose the Validation Method
根据项目情况选择合适的验证方式：
Choose an appropriate validation method based on the project:

- **如果有标准测试/构建/文档校验命令**（如 `npm test`、`pytest`、`cargo check`、`make test`、`mkdocs build`、`markdownlint` 等），优先使用这些命令进行验证。  
  **If standard test/build/doc validation commands exist** (such as `npm test`, `pytest`, `cargo check`, `make test`, `mkdocs build`, or `markdownlint`), prefer using them.
- **如果没有标准验证命令**，则与用户协商一个可执行的检查方式（如运行主程序、执行构建脚本、或使用已存在的校验脚本），通过退出码（0 表示成功）和错误输出来判断是否正常。**注意**：这种方式只能发现运行时/构建层面的错误，不能保证逻辑或内容正确性，需告知用户。  
  **If no standard validation command exists**, discuss a workable check with the user (such as running the main program, invoking a build script, or using an existing validation script), and use the exit code (`0` means success) plus error output to judge the result. **Note**: This can only catch runtime/build-level problems and does not guarantee logical or content correctness, so the limitation should be explained to the user.

### 4. 第一次验证 / First Validation
- 运行确定的验证命令。  
  Run the chosen validation command.
- 捕获输出，判断是否通过（测试通过/编译成功/运行无报错且退出码为 0）。  
  Capture the output and determine whether it passed (tests passed / compilation succeeded / program ran without errors and exited with code 0).

### 5. 结果处理 / Handle the Result
- **如果验证失败**：  
  **If validation fails**:
  - 向用户报告错误详情（错误信息、行号等）。  
    Report the error details to the user (messages, line numbers, and so on).
  - 根据错误修正相关文件变更。  
    Fix the relevant file changes based on the error.
  - 返回步骤 4（第一次验证）重新开始，**计数重置**。  
    Return to step 4 (first validation) and restart the process, **resetting the count**.
- **如果验证成功**：  
  **If validation succeeds**:
  - 记录“第一次成功”。  
    Record the first success.
  - 进入步骤 6。  
    Continue to step 6.

### 6. 第二次验证（同样严谨） / Second Validation (Same Rigor)
- **立即再次运行相同的验证命令**（使用相同的方式，例如同样包含 `--no-cache` 等选项）。  
  **Immediately run the same validation command again** using the same method, including the same options such as `--no-cache` when applicable.
- 捕获输出，判断是否通过。  
  Capture the output and determine whether it passed.

### 7. 最终判断 / Final Decision
- **如果第二次验证也成功**：  
  **If the second validation also succeeds**:
  - 向用户报告：✅ **双重验证通过！修改已完成且连续两次验证无错误。**  
    Report to the user: ✅ **Double-check passed! The change is complete and both validation runs succeeded without errors.**
  - 结束任务。  
    Finish the task.
- **如果第二次验证失败**：  
  **If the second validation fails**:
  - 向用户报告失败详情（可能是偶发性问题或修改引入的新错误）。  
    Report the failure details to the user (it could be a flaky issue or a new problem introduced by the change).
  - 根据错误修正相关文件变更。  
    Fix the relevant file changes based on the error.
  - 返回步骤 4（第一次验证），**计数重置**，重新开始双重验证流程。  
    Return to step 4 (first validation), **reset the count**, and restart the double-check workflow.

## 🔧 验证方式示例 / Validation Examples

| 项目类型 / Project Type | 推荐验证命令 / Recommended Command | 说明 / Notes |
|----------|--------------|------|
| Node.js（有测试 / with tests） | `npm test` | 运行测试 / Run tests |
| Node.js（无测试 / without tests） | `node index.js` | 运行主程序，检查是否报错 / Run the main program and check for errors |
| Python（有测试 / with tests） | `pytest` 或 `python -m unittest` | 运行测试 / Run tests |
| Python（无测试 / without tests） | `python main.py` | 运行主程序，检查是否报错 / Run the main program and check for errors |
| Rust | `cargo test` 或 `cargo check` | 运行测试或编译检查 / Run tests or compile checks |
| Go | `go test ./...` | 运行测试 / Run tests |
| Go（无测试 / without tests） | `go run main.go` | 运行主程序，检查是否报错 / Run the main program and check for errors |
| Java（Maven） | `mvn test` | 运行测试 / Run tests |
| Java（无测试 / without tests） | `java -jar target/app.jar` | 运行打包后的程序，检查是否报错 / Run the packaged app and check for errors |
| 通用（有 Makefile / with Makefile） | `make test` 或 `make check` | 自定义测试 / Custom test command |
| 通用（无测试 / without tests） | 与用户协商运行命令 / Agree on a run command with the user | 例如运行脚本、启动服务等 / For example, run a script or start a service |

## 💬 用户交互示例 / User Interaction Examples

### 示例 1：删除功能（有测试） / Example 1: Remove a Feature (With Tests)
**用户 / User**：请删除用户登录功能，用不到它了。  
**AI**：
1. 定位并删除登录功能的相关代码（文件、函数、调用等）。  
   Find and remove the code related to the login feature (files, functions, calls, and so on).
2. 运行 `npm test`（第一次验证）→ 测试通过（原有测试不受影响）。  
   Run `npm test` (first validation) → tests pass, and existing behavior is unaffected.
3. 再次运行 `npm test`（第二次验证）→ 测试通过。  
   Run `npm test` again (second validation) → tests pass.
4. 报告：✅ **双重验证通过！登录功能已删除，剩余代码运行正常，所有测试通过。**  
   Report: ✅ **Double-check passed! The login feature has been removed, the remaining code works correctly, and all tests pass.**

### 示例 2：删除功能（无测试，运行检查） / Example 2: Remove a Feature (No Tests, Run Check)
**用户 / User**：删掉设置页面的主题切换功能，没用了。  
**AI**：
1. 删除主题切换的相关代码。  
   Remove the code related to theme switching.
2. **由于没有找到测试命令，与用户协商**：“我没有找到标准的测试命令。我可以运行 `python main.py` 来检查是否有运行时错误，这种方式只能发现程序崩溃，无法验证逻辑正确性。你同意吗？或者你有其他验证方式？”  
   **Since no standard test command was found, discuss it with the user**: “I couldn’t find a standard test command. I can run `python main.py` to check for runtime errors, but that only catches crashes and cannot verify logical correctness. Does that work for you, or do you have another preferred validation method?”
3. 用户回复：“可以，就运行看看。”  
   The user replies: “That works. Go ahead.”
4. 运行 `python main.py`（第一次验证）→ 程序正常运行，退出码 0。  
   Run `python main.py` (first validation) → the program runs normally and exits with code 0.
5. 再次运行 `python main.py`（第二次验证）→ 程序正常运行，退出码 0。  
   Run `python main.py` again (second validation) → the program runs normally and exits with code 0.
6. 报告：✅ **双重验证通过！主题切换功能已删除，程序运行无报错。请注意，这仅验证了运行时错误，未检查其他功能是否受影响。**  
   Report: ✅ **Double-check passed! The theme-switching feature has been removed and the program runs without errors. Please note that this only validates runtime stability, not broader logical correctness.**

### 示例 3：验证失败并修正（添加功能） / Example 3: Validation Fails, Then Fix and Retry
**用户 / User**：添加一个计算器函数。  
**AI**：
1. 添加函数及相关代码。  
   Add the function and related code.
2. 运行 `pytest`（第一次验证）→ 失败（新函数测试未通过）。  
   Run `pytest` (first validation) → it fails because the new function’s tests do not pass.
3. 报告错误详情，修正代码。  
   Report the error details and fix the code.
4. 再次运行 `pytest`（第一次验证重置）→ 通过。  
   Run `pytest` again (first validation after reset) → it passes.
5. 再次运行 `pytest`（第二次验证）→ 通过。  
   Run `pytest` again (second validation) → it passes.
6. 报告：✅ **双重验证通过！计算器函数添加成功，所有测试通过。**  
   Report: ✅ **Double-check passed! The calculator function was added successfully, and all tests pass.**

## ⚠️ 注意事项 / Important Notes

- **自动应用**：本技能旨在**默认应用于所有文件修改任务**。AI 应主动识别文件修改意图并遵循本流程。  
  **Automatic application**: This skill is meant to be **the default behavior for all file modification tasks**. The AI should recognize such tasks proactively and follow this process.
- **删除功能的特殊考虑**：删除功能时，需确保移除了所有相关引用（如调用、导入、配置），避免残留代码导致错误。  
  **Special care when deleting features**: Remove all related references (calls, imports, configuration, and so on) to avoid leftover errors.
- **验证方式协商**：如果项目没有标准的验证命令，AI **必须**与用户协商确定验证方式（如简单的运行命令或构建脚本），并告知用户该方式的局限性（只能发现运行时/构建错误，不能保证逻辑或内容正确）。  
  **Agree on the validation method**: If the project lacks a standard validation command, the AI **must** discuss the validation method with the user and explain its limitations (it may catch runtime/build issues only, not logical or content correctness).
- **验证命令可用性**：确保验证命令在环境中可用。如果无法执行（例如没有运行环境），应与用户协商替代方案（如人工审查）。  
  **Command availability**: Make sure the validation command is available in the environment. If it cannot be executed (for example, due to a missing runtime), discuss an alternative with the user such as manual review.
- **连续两次**：强调“连续”意味着两次验证之间**没有新的文件修改**，只有验证执行。  
  **Consecutive means consecutive**: There should be **no new file edits between the two validation runs**, only validation.
- **同样严谨**：两次验证应使用**完全相同的方式**（包括命令、参数、环境等），以确保结果一致且可靠。  
  **Same rigor**: The two validation runs should use **exactly the same method** (including command, parameters, and environment) to ensure consistency and reliability.
- **验证独立性**：如果工具存在缓存机制可能影响结果，建议使用清除缓存的相关选项（如 `npm test -- --no-cache`、`pytest --cache-clear` 等）确保两次验证真实独立。  
  **Validation independence**: If caching could affect the result, prefer cache-clearing options such as `npm test -- --no-cache` or `pytest --cache-clear` so the two runs are genuinely independent.
- **超时处理**：如果验证命令运行时间过长（例如超过 5 分钟），可提示用户并建议手动检查，或允许用户中断。  
  **Timeout handling**: If the validation command runs too long (for example, more than 5 minutes), notify the user, suggest a manual check, or allow interruption.
- **与版本控制结合**：建议在修改前创建提交点或暂存更改，以便回滚。  
  **Use with version control**: It is recommended to create a commit point or stash changes before editing so you can roll back if needed.

## 🚀 与现有技能结合 / Works Well with Other Skills

如果你已在用 `answer-framework` 技能，本技能可与它自然衔接。例如，`answer-framework` 负责分析问题、组织回答，而 `double-check` 负责确保修改后的文件质量。AI 在收到文件修改请求时，应同时融合两个技能的指导。
If you are already using the `answer-framework` skill, this skill fits naturally alongside it. For example, `answer-framework` helps analyze the question and structure the response, while `double-check` ensures the quality of the modified files. When the AI receives a file-editing request, it should combine the guidance of both skills.

---

> **记住：文件质量不是偶然，而是双重验证的结果。本技能应默认应用于每次文件修改。**  
> **Remember: File quality is not an accident; it is the result of double-checking. This skill should be applied by default to every file modification.**
