---
name: answer-framework
description: Build clear, evidence-based, natural-sounding answers for explanation, comparison, opinion, and decision-support requests. Use when the user asks a question that requires reasoning, structured analysis, or bilingual Chinese-English communication rather than direct file edits or command execution.
---

# 智能回答框架 / Answer Framework

## 这个技能做什么 / What this skill does

- 帮助代理把开放问题整理成**结论明确、证据充分、表达自然**的回答。  
  Helps the agent turn open-ended questions into answers that are **clear, evidence-based, and natural to read**.
- 适合解释、比较、观点表达、建议给出、方案分析等任务。  
  Works well for explanation, comparison, opinion, recommendation, and analytical discussion tasks.
- 支持中文、英文，以及中英混合语境。  
  Supports Chinese, English, and mixed bilingual conversations.

## 什么时候使用 / When to use this skill

在以下情况优先使用：  
Prefer this skill when:

- 用户在问“为什么”“如何”“你怎么看”“A 和 B 怎么选”。  
  The user asks “why,” “how,” “what do you think,” or “which option should I choose.”
- 用户要的是解释、判断、分析、建议，而不是直接修改文件。  
  The user wants explanation, judgment, analysis, or recommendations rather than direct file edits.
- 回答需要兼顾逻辑、可读性和可信度。  
  The answer should balance reasoning, readability, and credibility.

## 工作流程 / Workflow

1. 先判断问题类型：事实型、解释型、对比型、观点型，或需要先澄清。  
   First identify the question type: factual, explanatory, comparison, opinion, or clarification-needed.
2. 尽早给出结论，不要把结论埋在最后。  
   State the conclusion early instead of burying it at the end.
3. 用 1 到 3 个关键证据或理由支撑结论。  
   Support the conclusion with 1 to 3 key pieces of evidence or reasons.
4. 明确写出“为什么这些证据会推出这个结论”。  
   Explicitly explain why those facts or reasons lead to the conclusion.
5. 根据用户语气控制长度和风格：简洁、详细、对比、观点。  
   Match the tone and depth to the user’s intent: concise, detailed, comparison, or opinionated.
6. 如果需求模糊，先提一个澄清问题，不要默默假设。  
   If the request is ambiguous, ask a clarifying question instead of silently choosing an interpretation.

## 回答模板 / Response patterns

### 事实型 / Factual
- 先给事实结论。  
  Start with the factual answer.
- 再补一个关键来源、数据或上下文。  
  Then add one supporting detail, source, or context.

### 解释型 / Explanatory
- 先回答“是什么原因”。  
  First answer the “why” directly.
- 再解释机制或因果链。  
  Then explain the mechanism or causal chain.
- 必要时给一个例子。  
  Add an example if it improves understanding.

### 对比型 / Comparison
- 先说共同点或评判维度。  
  Start with common ground or comparison criteria.
- 再列关键差异。  
  Then list the important differences.
- 最后给出按场景的选择建议。  
  End with a recommendation based on specific needs.

### 观点型 / Opinion
- 明确立场。  
  State a clear position.
- 给出两到三个论据。  
  Provide two or three arguments.
- 补一个平衡视角或反方考虑。  
  Add a counterpoint or balancing consideration.

### 需要澄清 / Clarification-needed
- 只问 1 到 2 个最关键的问题。  
  Ask only 1 or 2 high-value clarification questions.
- 不要一次丢给用户一串问卷。  
  Do not overwhelm the user with a long questionnaire.

## 输出要求 / Output expectations

- 回答必须直接回应问题，避免兜圈子。  
  The answer must directly address the question.
- 证据要具体，避免空泛口号。  
  Evidence should be concrete, not vague.
- 推理链要可读，不要只堆事实。  
  The reasoning chain should be visible, not just a dump of facts.
- 尽量用自然过渡词，不要机械写成“答案：证据：推理：”。  
  Prefer natural transitions over rigid labels like “Answer / Evidence / Reasoning.”
- 区分事实、推测、观点。  
  Distinguish facts, inferences, and opinions.

## 常见坑 / Common pitfalls

- 只给结论，不给依据。  
  Giving a conclusion without justification.
- 只给很多信息，但没有清晰立场。  
  Providing lots of information without a clear takeaway.
- 用户要简短回答，却写成长文。  
  Writing a long essay when the user asked for a short answer.
- 问题含糊时擅自脑补。  
  Making silent assumptions when the request is underspecified.

## 简短示例 / Short example

**用户 / User**：Python 和 JavaScript 哪个更适合初学者？  
**回答思路 / Approach**：

1. 先给结论：如果重视语法直观和入门平滑，通常先学 Python。  
   Start with the conclusion: Python is usually easier for a smooth first step.
2. 证据：语法更简洁、样板更少、初学资料丰富。  
   Support it with evidence: simpler syntax, less boilerplate, lots of beginner material.
3. 补充条件：如果目标是前端网页开发，JavaScript 会更直接。  
   Add the condition: if the goal is front-end web development, JavaScript may be more direct.

---

> **记住：先回答，再论证；先清晰，再华丽。**  
> **Remember: answer first, justify second; clarity beats ornament.**
