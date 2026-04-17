---
name: always-ask-next
description: Ask the user what to do next before ending a completed task, and offer 3 context-aware follow-up suggestions plus a freeform option. Use when the workflow could naturally continue and you want the agent to avoid stopping too early.
license: MIT
compatibility: Designed for Agent Skills-compatible clients such as GitHub Copilot in VS Code and skills.sh installations. No external tools are required.
metadata:
  author: BelugaRex
  languages: zh-CN,en
  category: workflow
---

# 始终追问下一步 / Always Ask Next

## 这个技能做什么 / What this skill does

- 在任务已经完成、代理准备收尾时，提醒代理**先问用户下一步**。  
  When the current task is complete, this skill reminds the agent to **ask for the next step before closing**.
- 用 3 个基于当前上下文的建议，把后续动作说具体。  
  It turns follow-up possibilities into 3 concrete, context-aware suggestions.
- 避免代理过早宣布“完成”然后中断协作。  
  It helps prevent the agent from declaring “done” too early and breaking collaboration flow.

## 什么时候使用 / When to use this skill

在以下场景优先使用：  
Prefer this skill when:

- 当前请求已经完成，但存在明显的后续动作。  
  The current request is complete but obvious next actions remain.
- 你希望代理不要擅自决定“到这里就结束”。  
  You do not want the agent to decide unilaterally that the work is over.
- 当前任务属于连续协作型流程，例如改代码、写文档、验证结果、规划下一轮。  
  The task is part of an iterative workflow such as coding, documenting, validating, or planning the next round.

## 核心规则 / Core rules

1. 当前任务完成后，结束前必须发起一次“下一步”提问。  
   After the current task is complete, ask one next-step question before ending.
2. 问题应等效于：`What would you like to do next?`  
   The question should be equivalent to: `What would you like to do next?`
3. 提供 3 个与当前上下文强相关的后续建议。  
   Provide 3 follow-up suggestions that are strongly tied to the current context.
4. 第 4 个选项固定保留为：`Other (please specify)`  
   Keep the 4th option fixed as: `Other (please specify)`
5. 提问后等待用户回应，而不是自己继续假设。  
   Wait for the user’s response instead of making further assumptions automatically.

## 工作流程 / Workflow

### 1. 确认当前任务已完成 / Confirm the current task is complete
- 只有在当前任务真正完成时才触发。  
  Trigger only when the current task is genuinely complete.

### 2. 提炼后续动作 / Extract follow-up actions
- 从刚完成的工作中找出最自然的 3 个下一步。  
  Derive the 3 most natural next steps from the work that was just completed.

### 3. 组织成可选项 / Turn them into options
- 每个选项都应具体、可执行、与上下文直接相关。  
  Each option should be concrete, actionable, and directly tied to the context.

### 4. 提问并停下 / Ask and pause
- 提出问题后，等待用户选择或补充。  
  After asking, wait for the user to choose or add their own direction.

## 选项生成规则 / Option generation rules

优先从这三类动作里选：  
Prefer options from these categories:

1. **延续当前成果**：继续当前工作流。  
   **Continue the current work**: extend what was just done.
2. **验证当前成果**：测试、检查、确认边界。  
   **Verify the result**: test, inspect, or confirm edge cases.
3. **扩展当前成果**：文档、配套功能、下一轮优化。  
   **Extend the result**: docs, adjacent features, or another improvement pass.

避免以下低质量选项：  
Avoid these low-quality options:

- 太空泛：`继续处理项目`  
  Too vague: `continue working on the project`
- 与上下文无关：`帮你写首诗`  
  Irrelevant to the task: `write a poem`
- 只是同一句话换三种说法。  
  Three options that are really the same action with different wording.

## 推荐输出样式 / Recommended output shape

```text
➡️ Next Action
What would you like to do next?

1. <上下文相关建议 1>
2. <上下文相关建议 2>
3. <上下文相关建议 3>
4. Other (please specify)
```

## 边界情况 / Edge cases

- 如果任务还没完成，不要提前追问下一步。  
  Do not ask for next steps before the current task is finished.
- 如果用户明确说“先到这里”或“不用继续问”，就不要强行追问。  
  If the user explicitly says “stop here” or “don’t ask me what’s next,” do not force it.
- 如果没有明显的后续动作，也至少提供与当前结果最接近的合理选项。  
  If follow-up actions are not obvious, provide the most reasonable next steps adjacent to the current result.

## 简短示例 / Short example

如果代理刚完成一个 bug 修复，合适的下一步可能是：  
If the agent just fixed a bug, reasonable next actions might be:

```text
➡️ Next Action
What would you like to do next?

1. 继续帮我补上相关测试
2. 再检查一下这个修复是否影响其他模块
3. 帮我整理这次修改的说明
4. Other (please specify)
```

---

> **记住：不要替用户决定终点；把下一步摆出来，让用户选择方向。**  
> **Remember: do not decide the finish line for the user; surface the next moves and let the user choose.**
