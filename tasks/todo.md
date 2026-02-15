# 任务计划

## 待办事项清单

### 1. 实现博客详情页 (Blog Detail Page)
- [x] **后端 (Backend)**:
    - [x] 在 `app/crud.py` 中添加 `get_blog_post(db, post_id)` 函数，用于按 ID 获取单篇文章。
    - [x] 在 `app/main.py` 中添加路由 `@app.get("/blog/{post_id}")`。
- [x] **前端 (Frontend)**:
    - [x] 创建 `templates/post.html` 模板，用于展示文章详情（标题、元数据、内容）。
    - [x] 修改 `templates/blog.html`，将列表项的链接指向新的详情页路由。

### 2. 实现文章编辑功能 (Edit Blog Post)
- [x] **后端 (Backend)**:
    - [x] 在 `app/crud.py` 中添加 `update_blog_post(db, post_id, title, content, ...)` 函数。
    - [x] 在 `app/admin.py` 中添加 `GET /admin/blog/edit/{post_id}` 路由，渲染带有预填充数据的编辑表单。
    - [x] 在 `app/admin.py` 中添加 `POST /admin/blog/edit/{post_id}` 路由，处理更新逻辑。
- [x] **前端 (Frontend)**:
    - [x] 创建 `templates/admin/edit_blog.html` 模板（或复用现有表单逻辑），确保表单中包含现有文章数据。
    - [x] 在 `templates/admin/blog.html` 的文章列表中添加 "Edit" 按钮。

## 复盘 (Review)
### 2024-05-23
- 成功实现了 **博客详情页**：
    - 访客现在可以点击博客列表中的标题或 "Read More" 链接，跳转到 `/blog/{id}` 页面阅读完整文章。
    - 详情页展示了标题、作者、日期、标签、封面图以及 HTML 格式的内容。
- 成功实现了 **后台文章编辑功能**：
    - 在 `/admin/blog` 列表页为每篇文章添加了 "Edit" 按钮。
    - 点击编辑会进入 `/admin/blog/edit/{id}` 页面，表单会自动填充当前文章的数据。
    - 提交表单后，文章内容会被更新，并跳转回列表页。
- 此次改动保持了代码的简洁性，复用了现有的数据库会话逻辑和模板风格。
