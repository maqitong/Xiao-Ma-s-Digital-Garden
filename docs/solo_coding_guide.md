# Solo 开发模式下的 AI 结对编程指南：以 Claude Code 为例

在单人开发（Solo Development）场景下，AI 不仅仅是一个代码生成器，更应该被视为你的**结对编程伙伴（Pair Programmer）**、**技术导师**和**项目经理**。

本指南旨在帮助你最大化利用像 Claude Code 这样的先进 AI 编程助手，通过结构化的提示词（Prompting）和工作流，提升代码质量、开发效率和项目可维护性。

## 🌟 核心理念：从“命令者”转变为“协作者”

不要只把 AI 当作搜索引擎或自动补全工具。要想获得高质量的输出，你需要提供高质量的上下文。

*   **Context is King（上下文为王）**：AI 越了解你的项目结构、技术栈和业务目标，它的建议就越精准。
*   **Iterative Refinement（迭代优化）**：不要期望一次提示就能完美解决复杂问题。将大任务拆解为小步骤。
*   **Verification Loop（验证闭环）**：始终要求 AI 提供验证方案（测试用例或检查脚本），确保代码不仅仅是“看起来是对的”。

---

## 🛠️ 最佳实践与提示词策略

### 1. 项目启动与上下文注入 (Context Injection)

在开始任何复杂任务之前，确保 AI “脑子”里有你的项目全貌。

**技巧**：使用 `CLAUDE.md` 或类似的规则文件（Rules）来持久化项目规范。

**提示词模板 (System Prompt / Rules)**：
> "你是一个资深的全栈工程师，正在协助我开发一个基于 FastAPI 和 Vue.3 的个人数字花园项目。
> 
> **项目原则**：
> 1. **简洁至上**：优先使用现有的库和模式，避免过度设计。
> 2. **类型安全**：Python 代码必须包含类型注解（Type Hints）。
> 3. **安全性**：所有公开接口必须有权限验证，输入必须经过清洗。
> 4. **文档化**：关键函数必须有 Docstring。
> 
> **技术栈**：
> - Backend: FastAPI, SQLAlchemy, SQLite
> - Frontend: Jinja2 Templates, TailwindCSS, Vanilla JS (无构建工具)
> 
> 在回答之前，请先检查 `app/models.py` 和 `app/crud.py` 以理解数据结构。"

### 2. 复杂任务拆解 (Chain of Thought & Planning)

对于跨文件修改或复杂逻辑，**强制要求 AI 先思考，再编码**。这能有效减少逻辑错误和“幻觉”。

**提示词模板**：
> "我需要实现[用户评论功能]。
> 
> 请不要直接写代码。先执行以下步骤：
> 1. **分析**：列出需要修改的文件（Model, API, UI）。
> 2. **设计**：描述数据模型的变化和 API 接口定义。
> 3. **计划**：给出一个分步实施计划（Step-by-step plan）。
> 4. **风险**：指出潜在的安全隐患或性能瓶颈。
> 
> 等我确认计划后，我们再开始第一步。"

### 3. 编写代码与重构 (Coding & Refactoring)

要求 AI 生成的代码具有生产级质量，而不仅仅是“能跑就行”。

**提示词模板 (Refactoring)**：
> "请重构 `app/crud.py` 中的 `get_items` 函数。
> 
> **目标**：
> - 提高查询效率，增加分页功能。
> - 优化错误处理，当 ID 不存在时抛出明确的 HTTP 404。
> - 保持函数签名尽量兼容，或者说明破坏性变更。
> 
> 请先解释你的重构思路，然后提供修改后的完整代码块。"

### 4. 调试与排错 (Debugging)

当遇到报错时，不要只贴错误信息，要提供上下文。

**提示词模板**：
> "我在运行 `seed_db.py` 时遇到了 `ModuleNotFoundError`。
> 
> **错误日志**：
> ```
> [粘贴具体的 traceback]
> ```
> 
> **环境信息**：
> - 操作系统：Windows
> - 虚拟环境：已激活 (venv)
> - 当前目录结构：[粘贴 `ls -R` 的部分输出]
> 
> 请分析原因，并提供修复命令或代码修改建议。如果是路径问题，请优先检查导入语句。"

### 5. 编写测试与验证 (Testing & Verification)

Solo 开发者最容易忽略测试。让 AI 帮你写测试，是提升代码信心的捷径。

**提示词模板**：
> "我刚刚完成了 `create_blog_post` 的 API 接口。
> 
> 请为这个接口编写一个 `pytest` 测试用例：
> 1. 测试正常创建流程（Happy Path）。
> 2. 测试字段缺失时的错误处理（Edge Case）。
> 3. 测试未授权访问（Security Check）。
> 
> 请确保测试代码可以直接运行，不需要额外的配置。"

---

## 🚀 进阶：Solo 开发者的 AI 工作流 (Workflow)

结合 `Claude Code` 或类似工具，推荐以下工作流：

1.  **Discovery (探索)**：
    *   `@Search` "查找所有处理用户认证的代码逻辑"
    *   `@Search` "解释 `app/main.py` 的启动流程"
2.  **Plan (计划)**：
    *   "在 `tasks/todo.md` 中创建一个新任务列表，关于集成 Giscus 评论系统。"
3.  **Act (执行)**：
    *   按计划逐个文件修改。每次修改后，要求 AI 解释改动点。
4.  **Verify (验证)**：
    *   "生成一个 `curl` 命令来测试新的 API。"
    *   "运行现有的测试套件，确保没有破坏旧功能。"
5.  **Document (文档)**：
    *   "更新 `README.md`，说明新添加的环境变量配置。"
    *   "在 `tasks/todo.md` 中记录本次开发的复盘总结。"

## 📚 常用指令速查 (Prompt Cheatsheet)

| 场景 | 关键指令词 (Keywords) | 示例 |
| :--- | :--- | :--- |
| **解释代码** | `Explain`, `Trace` | "Trace the data flow from the login form to the database." |
| **生成代码** | `Scaffold`, `Implement` | "Scaffold a new CRUD module for 'Tags'." |
| **优化代码** | `Optimize`, `Refactor` | "Refactor this function to be more 'Pythonic' and readable." |
| **查找问题** | `Debug`, `Analyze` | "Analyze why this SQL query is slow." |
| **生成文档** | `Document`, `Summarize` | "Generate a Docstring for this class in Google style." |

---

> **给 Solo 开发者的一句话**：
> AI 是你的副驾驶，但**方向盘始终在你手中**。保持批判性思维，审查每一行生成的代码，你将不仅能跑得更快，还能走得更远。
