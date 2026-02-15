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

### 3. Markdown 支持 (Markdown Support)
- [x] **后端**: 集成 `markdown` 库，在 `app/main.py` 中实现渲染逻辑。
- [x] **前端**: 引入 `Prism.js` 实现代码高亮，优化文章样式。

### 4. 全站搜索 (Global Search)
- [x] **后端**: 在 `app/crud.py` 中实现对 Blog 和 Project 的联合搜索。
- [x] **前端**: 添加搜索框（桌面端/移动端），创建 `templates/search.html` 结果页。
- [x] **优化**: 重新设计搜索框交互（展开式），移除旧样式。

## 复盘 (Review)
### 2024-05-23
- **博客详情页**: 实现了文章独立阅读页面，包含完整的元数据和导航。
- **后台编辑**: 实现了文章内容的在线修改功能，解决了之前只能删不能改的痛点。
- **Markdown & 代码高亮**: 现在可以直接发布技术文章，代码块有漂亮的语法高亮。
- **全站搜索**: 添加了高效的搜索功能，支持文章和项目的关键词检索。
- **样式优化**: 优化了搜索框交互和文章排版，提升了用户体验。
- **文档**: 添加了 Solo 开发指南，并自动导入到了博客中。
