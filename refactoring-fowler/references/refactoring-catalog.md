# 重构手法名录 / Refactoring Catalog（《重构》第 2 版 第 5–12 章）

> 页码为英文第 2 版页码（中译本一致）。每条手法的完整"动机 / 做法 / 范例"见书中对应章节。
> Page numbers refer to the 2nd English edition. Full motivation/mechanics/examples live in the book.

## 名录条目的标准格式 / Catalog entry format（第 5 章）

撰写或规划一个重构时，按书的体例组织，便于评审与执行：

1. **名称（Name）**：中英对照，标注反向重构。
2. **速写（Sketch）**：before/after 极简代码对照。
3. **动机（Motivation）**：为什么值得做、什么时候不做。
4. **做法（Mechanics）**：编号的小步清单，每步可独立验证。
5. **范例（Examples）**：最小可运行示例。

## 第 6 章 第一组重构 / A First Set of Refactorings（最常用 ★）

| 手法 / Refactoring | 页码 | 用途 / When | 反向 / Inverse |
| --- | --- | --- | --- |
| 提炼函数 Extract Function | 106 | 一段代码意图需要注释才能看懂时，按"做什么"命名提炼 | 内联函数（115） |
| 内联函数 Inline Function | 115 | 函数体与名字一样直白；间接层失去价值 | — |
| 提炼变量 Extract Variable | 119 | 复杂表达式拆出有名字的局部量 | 内联变量（123） |
| 内联变量 Inline Variable | 123 | 变量名没比表达式本身传达更多信息 | — |
| 改变函数声明 Change Function Declaration | 124 | 改名、增删参数、统一签名（别名：Rename Function / Add / Remove Parameter） | — |
| 封装变量 Encapsulate Variable | 132 | 变量需要收窄访问面、为搬移/演化铺路 | — |
| 变量改名 Rename Variable | 137 | 名字不达意 | — |
| 引入参数对象 Introduce Parameter Object | 140 | 一组数据总是结伴作为参数出现 | — |
| 函数组合成类 Combine Functions into Class | 144 | 几个函数总是围绕同一批数据操作 | — |
| 函数组合成变换 Combine Functions into Transform | 148 | 派生数据的计算逻辑分散、重复 | — |
| 拆分阶段 Split Phase | 154 | 一段代码先后处理两件不同的事（如：解析 → 处理） | — |

## 第 7 章 封装 / Encapsulation

| 手法 | 页码 | 用途 | 反向 |
| --- | --- | --- | --- |
| 封装记录 Encapsulate Record | 162 | 用类隐藏裸记录/嵌套 map 的结构细节 | — |
| 封装集合 Encapsulate Collection | 170 | 不让调用方直接读写集合内部 | — |
| 以对象取代基本类型 Replace Primitive with Object | 174 | 领域概念值得一个带行为的类 | — |
| 以查询取代临时变量 Replace Temp with Query | 178 | 临时变量可提炼为可复用的查询 | — |
| 提炼类 Extract Class | 182 | 类承担了本应分开的职责 | 内联类（186） |
| 内联类 Inline Class | 186 | 类已无足轻重 | 提炼类（182） |
| 隐藏委托关系 Hide Delegate | 189 | 屏蔽客户端与委托对象的导航耦合 | 移除中间人（192） |
| 移除中间人 Remove Middle Man | 192 | 转发已无价值 | 隐藏委托关系（189） |
| 替换算法 Substitute Algorithm | 195 | 有更清晰的实现可整体替换 | — |

## 第 8 章 搬移特性 / Moving Features

| 手法 | 页码 | 用途 | 反向 |
| --- | --- | --- | --- |
| 搬移函数 Move Function | 198 | 函数对别的上下文更亲密（依恋情结） | — |
| 搬移字段 Move Field | 207 | 字段被另一个类更需要 | — |
| 搬移语句到函数 Move Statements into Function | 213 | 调用方代码其实是函数内部事务 | — |
| 搬移语句到调用者 Move Statements to Callers | 217 | 边界处理其实由调用方差异决定 | — |
| 以函数调用取代内联代码 Replace Inline Code with Function Call | 222 | 现成的库函数/已有函数可替代手写实现 | — |
| 移动语句 Slide Statements | 223 | 调整语句顺序使相关代码聚拢 | — |
| 拆分循环 Split Loop | 227 | 一个循环做了多件事 | — |
| 以管道取代循环 Replace Loop with Pipeline | 231 | filter/map/reduce 表达更清晰 | — |
| 移除死代码 Remove Dead Code | 237 | 永远不会执行的分支与定义 | — |

## 第 9 章 重新组织数据 / Organizing Data

| 手法 | 页码 | 用途 | 反向 |
| --- | --- | --- | --- |
| 拆分变量 Split Variable | 240 | 变量被多次赋值、身兼多职 | — |
| 变量改名 Rename Variable | 137 | 名字不达意 | — |
| 以查询取代派生变量 Replace Derived Variable with Query | 248 | 可计算的派生值直接算出来，别存中间副本 | — |
| 将引用对象改为值对象 Change Reference to Value | 252 | 对象小且不可变时值语义更简单 | 将值对象改为引用对象（256） |
| 将值对象改为引用对象 Change Value to Reference | 256 | 多处需要共享同一实体（如订单 → 客户） | 将引用对象改为值对象（252） |

## 第 10 章 简化条件逻辑 / Simplifying Conditional Logic

| 手法 | 页码 | 用途 | 反向 |
| --- | --- | --- | --- |
| 分解条件表达式 Decompose Conditional | 260 | 条件与分支各提炼成函数 | — |
| 合并条件表达式 Consolidate Conditional Expression | 263 | 多个检查其实在做同一件事 | — |
| 以卫语句取代嵌套条件表达式 Replace Nested Conditional with Guard Clauses | 266 | 先处理特例提前返回，主路径保持平坦 | — |
| 以多态取代条件表达式 Replace Conditional with Polymorphism | 272 | switch/if-else 链可映射到类型行为 | — |
| 引入特例 Introduce Special Case | 289 | 多处对同一特殊值（如 null）做相同检查；即 Null Object | — |
| 引入断言 Introduce Assertion | 302 | 显式声明并检查不变量 | — |

## 第 11 章 重构 API / Refactoring APIs

| 手法 | 页码 | 用途 | 反向 |
| --- | --- | --- | --- |
| 将查询函数和修改函数分离 Separate Query from Modifier | 306 | 有返回值就不该有可见副作用（CQS） | — |
| 函数参数化 Parameterize Function | 310 | 几个函数逻辑相同只有字面值不同 | — |
| 移除标记参数 Remove Flag Argument | 314 | 布尔参数导致截然不同的行为，拆成两个函数 | — |
| 保持对象完整 Preserve Whole Object | 319 | 从一个对象拆出的几个参数改为整体传入 | — |
| 以查询取代参数 Replace Parameter with Query | 324 | 参数可由函数内部推导 | 以参数取代查询（327） |
| 以参数取代查询 Replace Query with Parameter | 327 | 内部查询造成隐藏依赖/不可变性 | 以查询取代参数（324） |
| 移除设值函数 Remove Setting Method | 331 | 字段创建后不该再改，收紧可变性 | — |
| 以工厂函数取代构造函数 Replace Constructor with Factory Function | 334 | 构造过程需要更多灵活性（如返回子类/缓存实例） | — |
| 以命令取代函数 Replace Function with Command | 337 | 大函数需要拆解、排序、撤销等对象化能力 | 以函数取代命令（344） |
| 以函数取代命令 Replace Command with Function | 344 | 命令对象只剩一个执行入口时简化回去 | 以命令取代函数（337） |

## 第 12 章 处理继承关系 / Dealing with Inheritance

| 手法 | 页码 | 用途 | 反向 |
| --- | --- | --- | --- |
| 函数上移 Pull Up Method | 350 | 子类重复的函数体提升到超类 | 函数下移（359） |
| 字段上移 Pull Up Field | 353 | 子类重复的字段提升到超类 | 字段下移（361） |
| 构造函数本体上移 Pull Up Constructor Body | 355 | 子类构造中的公共初始化上移 | — |
| 函数下移 Push Down Method | 359 | 只有部分子类需要的函数下沉 | 函数上移（350） |
| 字段下移 Push Down Field | 361 | 只有部分子类需要的字段下沉 | 字段上移（353） |
| 以子类取代类型码 Replace Type Code with Subclasses | 362 | 类型码只影响行为差异且外部不可变 | — |
| 移除子类 Remove Subclass | 369 | 子类已无差异（常因以委托取代后） | 以子类取代类型码（362） |
| 提炼超类 Extract Superclass | 375 | 两个类有共同的函数/字段 | — |
| 折叠继承体系 Collapse Hierarchy | 380 | 超类与子类已无实质差别 | — |
| 以委托取代子类 Replace Subclass with Delegate | 381 | 继承导致类爆炸或类型码需要动态变化 | 以子类取代类型码（362） |
| 以委托取代超类 Replace Superclass with Delegate | 399 | 子类并不真正"是一种"超类（被拒绝的遗赠） | — |

## 高频组合 / High-frequency pairings

- **过长函数** → Extract Function（106）为主轴，循环配 Split Loop（227）/管道（231），条件配卫语句（266）。
- **条件分支大量重复** → Replace Type Code with Subclasses（362）+ Replace Conditional with Polymorphism（272）。
- **加新功能前的预备重构** → Split Phase（154）、Extract Class（182）、Move Function（198）最常让改动"变容易"。
- **数据传参混乱** → Introduce Parameter Object（140）+ Preserve Whole Object（131）+ Remove Flag Argument（314）。

## 书外资源 / External resources

- 在线名录（含每条手法的速写代码）：https://refactoring.com/catalog/
- 中文在线阅读：https://cactus-proj.github.io/Refactoring-2ed-zh/
- 实施任何手法前，先确认测试安全网；每完成一小步即运行测试。
