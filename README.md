# my-skills

面向 **Agent Skills / skills.sh / GitHub Copilot in VS Code** 的个人技能库。  
A personal skill library designed for **Agent Skills / skills.sh / GitHub Copilot in VS Code**.

## 🚀 推荐分享与安装路径 / Recommended sharing and installation flow

如果你像我一样，是通过 `skills.sh` 把 skill 分享给朋友，并让他们在 VS Code Copilot 中使用，推荐路径如下：

1. 把 skill 发布到 GitHub 仓库
2. 让 `skills.sh` 收录并公开展示
3. 朋友在 VS Code 安装扩展：`AutomataLabs.copilot-mcp`
4. 朋友在扩展的 **Skills** 视图中搜索并安装 skill
5. 朋友在 GitHub Copilot Chat 中直接调用，或让 Copilot 按描述自动加载

If you are sharing skills through `skills.sh` and want friends to use them in VS Code Copilot, this is the recommended path:

1. Publish the skill in a GitHub repository
2. Let it be indexed and distributed through `skills.sh`
3. Have users install the `AutomataLabs.copilot-mcp` extension in VS Code
4. Let them search and install the skill from the extension’s **Skills** view
5. Use the skill in GitHub Copilot Chat directly or let Copilot load it automatically

## 🧭 这个仓库的写法原则 / Authoring principles in this repository

这些 skill 目前统一按以下原则编写：

- 优先遵循 **Agent Skills 标准**，便于 `skills.sh` 分发
- 同时兼顾 **VS Code Copilot** 的推荐写法：`name` 与目录名一致，`description` 明确说明“做什么 + 什么时候用”
- 保持**中英双语**，方便中文用户理解，也有助于英文生态检索
- 尽量使用可移植 frontmatter，避免过度依赖单一客户端的私有字段

These skills are intentionally written to:

- follow the **Agent Skills standard** first, so they distribute cleanly through `skills.sh`
- align with **VS Code Copilot** recommendations, especially clear `name` and `description` discovery metadata
- remain **bilingual** for both Chinese-speaking and English-speaking users
- stay portable across Agent Skills-compatible clients instead of depending too heavily on one client’s private metadata

## 📚 技能列表 / Skills

### 1. 🧠 `answer-framework`
- **中文**：用于解释、比较、观点表达与建议型问题，让回答更清晰、有证据、自然流畅。
- **English**: For explanation, comparison, opinion, and recommendation tasks that need clear, evidence-based, natural responses.

### 2. ✅✅ `double-check`
- **中文**：用于任何文件修改任务，在结束前强制进行两次连续验证。
- **English**: For any file modification task that should be verified twice before completion.

### 3. ➡️ `always-ask-next`
- **中文**：用于连续协作型任务，在结束前先询问用户下一步想做什么。
- **English**: For collaborative workflows where the agent should ask for the next step before ending.

## 📦 关于技能格式 / About the skill format

每个 skill 目录至少包含一个 `SKILL.md`，并满足以下要求：

- 目录名与 frontmatter 里的 `name` 一致
- `description` 明确说明能力和触发场景
- 正文尽量保持简洁、结构化、适合按需加载
- 仓库层保留一个公共 `README.md`，不要求每个 skill 单独提供 `README.md`

Each skill directory contains at least a `SKILL.md` file, with:

- a directory name that matches the frontmatter `name`
- a `description` that explains both the capability and when to use it
- a concise, structured body that is suitable for on-demand loading by Copilot
- one shared repository-level `README.md` as the main documentation entry point, instead of requiring a per-skill `README.md`

## 🗂️ 推荐目录结构 / Recommended directory layout

```text
my-skills/
├── README.md
├── LICENSE
├── answer-framework/
│   └── SKILL.md
├── double-check/
│   └── SKILL.md
└── always-ask-next/
	└── SKILL.md
```

这种结构的好处是：

- 更简洁，减少重复文档
- 更适合维护统一的分享说明
- 更适合通过 `skills.sh` 对外发布时保持仓库整洁

This structure keeps the repository simpler, avoids repeated documentation, and makes the public sharing story cleaner for `skills.sh`.

## 📄 许可证 / License

本仓库使用 MIT License。详见 `LICENSE`。  
This repository is licensed under MIT. See `LICENSE` for details.
