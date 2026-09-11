# 代码的坏味道速查表 / Code Smells Catalog（第 3 章，共 24 种）

> 坏味道是**信号，不是判定标准**：没有任何量度规矩比得上见识广博者的直觉。每条发现项必须落到具体代码证据与实际维护代价上。
> Smells are signals, not verdicts. Every finding must cite concrete code and a real maintenance cost.

标注 ★ 的是日常最高频、最值得优先处理的坏味道。
Items marked ★ are the most common and highest-value smells to check first.

## 结构类 / Structural smells

### ★ 神秘命名（Mysterious Name）3.1
- **识别**：函数、变量、类名需要点开实现才能懂；命名晦涩或有误导。
- **建议**：Change Function Declaration（124）、Rename Variable（137）、Rename Field（244）。想不出好名字本身就是更深设计问题的信号。

### ★ 重复代码（Duplicated Code）3.2
- **识别**：相同代码结构出现于多处；或"大体相似、细节略异"的成对函数。
- **建议**：Extract Function（106）；兄弟子类间 → 先统一再 Pull Up Method（350）；不相关的类 → Extract Class（182）。

### ★ 过长函数（Long Function）3.3
- **识别**：函数很长；注释密集（注释常暗示可提炼的意图）；需要竖向滚动才能理解。
- **建议**：Extract Function（106）；提前退出 → Replace Nested Conditional with Guard Clauses（266）；大条件块 → Decompose Conditional（260）；循环 → Split Loop（227）、Replace Loop with Pipeline（231）。

### 过长参数列表（Long Parameter List）3.4
- **识别**：参数多且总是一起传；有布尔/标记参数控制分支。
- **建议**：Introduce Parameter Object（140）、Preserve Whole Object（319）、Replace Parameter with Query（324）、Remove Argument（127）、Remove Flag Argument（314）。

### 全局数据（Global Data）3.5
- **识别**：模块级可变全局/静态变量被散布的代码读写。
- **建议**：Encapsulate Variable（132），再收窄访问面、搬移逻辑。

### 可变数据（Mutable Data）3.6
- **识别**：一个变量被多处赋值、承担多个责任；共享可变状态引发并发隐患。
- **建议**：Encapsulate Variable（132）、Split Variable（240）、Replace Derived Variable with Query（248）、Separate Query from Modifier（306）、Remove Setting Method（331）；能用不可变就用不可变。

## 变化与耦合类 / Change & coupling smells

### 发散式变化（Divergent Change）3.7
- **识别**：一个类因**不同原因、不同方向**反复被修改（加一个功能改 3 处，加另一个功能改另外 5 处）。
- **建议**：Extract Class（182），按变化方向拆开。

### 霰弹式修改（Shotgun Surgery）3.8
- **识别**：一个小改动要在很多类/文件里做许多细碎修改。与发散式变化相反。
- **建议**：Move Function（198）、Move Field（207）把相关元素聚到一处；多余壳层 → Inline Class（186）。

### 依恋情结（Feature Envy）3.9
- **识别**：函数对别的对象的数据比对自身数据的兴趣更大（一堆 `other.getX()` 调用）。
- **建议**：Move Function（198），搬到数据所在处；只有部分依恋 → Extract Function（106）先切分。

### 内幕交易（Insider Trading）3.19
- **识别**：两个模块互相大量了解对方的私有细节，"耦合夜宴"。
- **建议**：Move Function（198）、Move Field（207）减少互相窥探；共享数据 → Extract Class（182）；双向依赖 → Hide Delegate（189）。

### 过大的类（Large Class）3.20
- **识别**：类做了太多事；字段过多、重复 switch 多；单测要 mock 一堆。
- **建议**：先看客户端如何使用，按用途 Extract Class（182）；有共享行为 → Extract Superclass（375）。

## 数据与类型类 / Data & type smells

### 数据泥团（Data Clumps）3.10
- **识别**：几个数据项总是成组出现（同样的 2-4 个参数在多个函数间结伴旅行）。
- **建议**：Introduce Parameter Object（140）、Preserve Whole Object（319）、Extract Class（182）。判断标准：删掉其中一个数据项，其他还站得住吗？

### 基本类型偏执（Primitive Obsession）3.11
- **识别**：用基本类型表示领域概念（电话号码是 string、金额是 number、范围是 start/end 两个 int）。
- **建议**：Replace Primitive with Object（174）；类型码触发行为 → Replace Type Code with Subclasses（362）+ Replace Conditional with Polymorphism（272）；数据与行为分离 → Extract Class（182）。

### 重复的 switch（Repeated Switches）3.12
- **识别**：同样的 switch/if-else 链在多个地方重复出现，加一种类型要改所有处。
- **建议**：Replace Conditional with Polymorphism（272），底层 Replace Type Code with Subclasses（362）。

### 纯数据类（Data Class）3.22
- **识别**：只有字段和 getter/setter，行为全在别的类里。
- **建议**：Encapsulate Record（162）、Encapsulate Collection（170），再把使用该数据的行为 Move Function（198）搬进来；删除无意义的 setter → Remove Setting Method（331）。

### 临时字段（Temporary Field）3.16
- **识别**：字段只在特定算法/分支里有意义，平时是空的或被 null 检查包围。
- **建议**：Extract Class（182）把相关代码和数据搬走；null 分支 → Introduce Special Case（289）。

## 冗余与继承类 / Redundancy & inheritance smells

### ★ 循环语句（Loops）3.13
- **识别**：手工 for/foreach 做过滤、映射、累加（现代语言时代的新味道）。
- **建议**：Replace Loop with Pipeline（231）；一循环多件事 → Split Loop（227）。

### 冗赘的元素（Lazy Element）3.14
- **识别**：类、函数、字段已不再承担足够责任（可能因重构后变闲）。
- **建议**：Inline Function（115）、Inline Class（186）、Collapse Hierarchy（380）、Remove Subclass（369）、Remove Dead Code（237）。

### 夸夸其谈通用性（Speculative Generality）3.15
- **识别**：为"将来可能需要"预留的抽象、参数、钩子；目前无人使用。
- **建议**：Remove Dead Code（237）、Remove Argument（127）、Inline Class（186）、Collapse Hierarchy（380）。YAGNI。

### 过长的消息链（Message Chains）3.17
- **识别**：`a.getB().getC().getD()` 连环调用，客户端与导航结构紧耦合。
- **建议**：Hide Delegate（189）；让中间对象提供一个"直达"的委托方法。

### 中间人（Middle Man）3.18
- **识别**：类的接口一半以上只是简单转发给另一个对象。
- **建议**：Remove Middle Man（192）让调用方直连；仅个别函数 → Inline Function（115）。

### 异曲同工的类（Alternative Classes with Different Interfaces）3.21
- **识别**：两个类做几乎一样的事，只是方法名不同。
- **建议**：Change Function Declaration（124）统一签名 → Move Function（198）、字段搬移去重；仍重 → Extract Superclass（375）。

### 被拒绝的遗赠（Refused Bequest）3.23
- **识别**：子类只继承了一部分，另一部分方法/字段被覆盖为空或直接报错。
- **建议**：真的不等价 → Push Down Method（359）、Push Down Field（361）；继承关系本身错误 → Replace Subclass with Delegate（381）、Replace Superclass with Delegate（399）。

### 注释（Comments）3.24
- **识别**：注释在解释"这段代码干什么"或为糟糕的设计道歉（先别误解：注释本身常是好东西）。
- **建议**：注释提示了意图 → Extract Function（106）用注释命名新函数；解释参数/返回 → Change Function Declaration（124）；解释不变量 → Introduce Assertion（302）。改完代码后让注释过时即删。

## 使用提示 / How to use this catalog

- **先高频后长尾**：从 ★ 项入手通常收益最高；"过长函数 + 神秘命名 + 重复代码"三件套几乎总在丑代码里同框出现。
- **成对看方向**：3.7 发散式变化与 3.8 霰弹式修改互为反面；3.17 消息链与 3.18 中间人也互为反面——修一边时留意别造出另一边。
- **坏味道 → 手法映射**见 `refactoring-catalog.md`；先确认安全网（测试）再动手。
