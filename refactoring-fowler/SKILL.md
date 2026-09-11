---
name: refactoring-fowler
description: Restructure existing code safely using Martin Fowler's Refactoring (2nd Ed.) methodology — identify code smells, pick the right refactoring from the catalog, and apply it in small behavior-preserving steps. Use when improving code design, reviewing for code smells, preparing code for a new feature, or when the user mentions refactoring, code smells, or the Refactoring book.
---

# 重构方法论 / Refactoring (Fowler, 2nd Edition)

## 这个技能做什么 / What this skill does

- 把《重构：改善既有代码的设计（第 2 版）》的方法论应用到实际编码中：**识别坏味道 → 选对手法 → 小步修改 → 每步验证**。
  Applies the methodology of *Refactoring: Improving the Design of Existing Code (2nd Ed.)*: **identify the smell → pick the refactoring → change in small steps → verify each step**.
- 核心定义（务必遵守）：重构是**在不改变软件可观察行为的前提下，调整其内部结构**。
  Core definition (must follow): refactoring changes the internal structure **without changing the observable behavior** of the software.

## 什么时候使用 / When to use this skill

- 用户要求改进代码设计、消除坏味道、降低复杂度，或提到 "refactor"、“重构”、"code smell"。
  The user asks to improve design, remove smells, reduce complexity, or mentions refactoring.
- **预备性重构**：加新功能之前，先把代码整理成“让这个改动容易做”的形状。
  **Preparatory refactoring**: before adding a feature, reshape the code so the change becomes easy.
- **代码评审**：需要指出设计问题并给出书中手法名称作为改进建议时。
  Code review: pointing out design problems with named, book-backed remedies.

## 铁律 / Iron rules（来自第 2 章 / from Chapter 2）

1. **两顶帽子**：加功能与重构**绝不混在一次修改里**。戴重构帽时，只做结构移动，不加新行为；写测试验证后立即摘帽。
   **Two hats**: never mix feature work and refactoring in one change. When wearing the refactoring hat, only move structure; when green, switch back.
2. **小步前进**：每次只做**一个**名录手法（或其中一小步），小到出错能立刻看出原因。
   **Small steps**: apply **one** catalog refactoring (or one part of it) at a time — small enough that a failure's cause is obvious.
3. **每步测试**：每一步之后跑测试；**测试红着的时候不重构，也不提交**。
   **Test after every step**: run tests between steps; **never refactor or commit on a red suite**.
4. **没有安全网就先织网**：目标代码没有测试覆盖时，先补特征测试（characterization tests）再动手（第 4 章）。
   **Build the safety net first**: if the target code lacks coverage, add characterization tests before touching it (Ch. 4).
5. **机会主义，不立项**：重构是日常编程的一部分，按“事不过三”法则（第三次重复时才容忍自己重构）择机进行；坏味道是信号，不是必修清单。
   **Opportunistic, not scheduled**: refactor as part of daily work (rule of three); smells are signals, not a mandatory checklist.
6. **知道何时停手**：接近重写的代码量级时建议重写而不是重构；不要为了“更漂亮”而重构无主代码或从未再改过的代码（YAGNI）。
   **Know when to stop**: suggest a rewrite when the module is near rewrite scale; don't refactor code that will never change again (YAGNI).

## 工作流程 / Workflow

1. **界定范围**：从请求和上下文确定重构范围；范围大时先摸清依赖热点，不做全量确认式停留，但要声明抽样未查的区域。
   **Resolve scope**: map the target code and hotspots; disclose sampled or uninspected areas.
2. **确认安全网**：检查测试覆盖；没有就先补测试（见铁律 4）。
   **Confirm the safety net**: check test coverage; add tests first if missing.
3. **闻坏味道**：通读目标代码，对照 [references/code-smells.md](references/code-smells.md) 逐一辨认坏味道，**引用具体代码证据**，按“影响 × 风险 × 工作量”排序。不要为了凑齐目录里的每个类别而制造发现项。
   **Smell out the code**: read the target code against [references/code-smells.md](references/code-smells.md), citing concrete evidence; rank by impact × risk × effort. Do not manufacture findings to cover every category.
4. **选手法并执行**：对每个确认的坏味道，从 [references/refactoring-catalog.md](references/refactoring-catalog.md) 选对应手法（坏味道条目里已给出建议手法），严格按名录的“做法”小步执行，每步后运行测试。
   **Pick and apply**: for each confirmed smell, choose the mapped refactoring from [references/refactoring-catalog.md](references/refactoring-catalog.md), follow its mechanics in small steps, testing between steps.
5. **收尾**：全部测试通过后立即 commit（`refactor:` 前缀），重构与功能改动分开提交；最后向用户报告：改了什么坏味道、用了什么手法、行为如何保证不变。
   **Wrap up**: commit immediately when green (`refactor:` prefix), keep refactoring commits separate from feature commits; report which smells were addressed, which refactorings applied, and how behavior preservation was verified.

## 参考资料按需加载 / Load references on demand

| 文件 / File | 内容 / Contents |
| --- | --- |
| `references/code-smells.md` | 24 种坏味道：识别特征 + 建议手法（第 3 章） |
| `references/refactoring-catalog.md` | 全部重构手法名录：动机、要点、反向手法（第 5–12 章） |

按需读取对应小节即可，不要一次性全文加载。
Read only the relevant sections on demand; do not load everything at once.

## 输出要求 / Reporting style

- 每条发现项格式：**坏味道名称（中英）+ 代码位置 + 为什么有害 + 建议手法（中英 + 页码）**。
  Each finding: **smell name + location + why it hurts + suggested refactoring (name + page)**.
- 不确定时直说，不要把教科书类目硬套在没有实际后果的代码上——没有实际维护代价的发现项不算发现项。
  Be honest about uncertainty; a textbook category without a practical maintenance cost is not a finding.
