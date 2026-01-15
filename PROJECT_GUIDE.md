# Xiao Ma's Digital Garden 项目指南

这份文档旨在帮助你了解本站的技术架构、如何进行日常维护以及如何将其部署到生产服务器。

---

## 1. 技术栈说明 (Technology Stack)

本站采用了现代化的前后端分离思想，但通过集成模板引擎实现了高效的渲染和 SEO 友好性。

- **后端框架**: [FastAPI](https://fastapi.tiangolo.com/) - 一个高性能、异步的 Python Web 框架。
- **数据库**: [SQLite](https://www.sqlite.org/) - 轻量级文件型数据库，无需安装额外的数据库服务。
- **ORM (对象关系映射)**: [SQLAlchemy](https://www.sqlalchemy.org/) - 用于在 Python 代码中操作数据库，无需直接编写 SQL。
- **模板引擎**: [Jinja2](https://jinja.palletsprojects.com/) - 用于将动态数据注入到 HTML 页面中。
- **前端样式**: [Tailwind CSS](https://tailwindcss.com/) - 原子化 CSS 框架，负责全站的响应式设计和动画。
- **图标库**: [Remix Icon](https://remixicon.com/) - 提供了全站使用的矢量图标。

---

## 2. 项目目录结构

- `/app`: 核心后端代码
    - `models.py`: 数据库表结构定义（如工作经历、项目、博客等）。
    - `crud.py`: 数据库的增删改查逻辑。
    - `admin.py`: 管理后台的路由逻辑。
    - `main.py`: 项目入口，定义了前台页面的路由。
- `/static`: 静态资源文件（CSS, JS, 图片, PDF 简历）。
- `/templates`: HTML 模板文件。
    - `/admin`: 管理后台专用模板。
- `sql_app.db`: 数据库文件（部署时需保留）。

---

## 3. 网站修改与维护操作说明

### A. 如何更新工作经历/项目/相册
1.  启动项目后，访问 `http://localhost:8000/admin`。
2.  在对应的导航栏（如 Resume, Projects, Gallery）中进行添加或修改。
3.  **注意**：简历页面的“工作经历”现在是动态加载的，你在后台修改后，前台会自动同步更新。

### B. 如何上传图片并在网页显示
1.  **准备图片**：将图片文件放入 `static/gallery_files/` 文件夹。
2.  **获取路径**：图片的 Web 路径将是 `/static/gallery_files/文件名.后缀`。
3.  **填入后台**：在管理后台添加新项目或照片时，在 `Image URL` 输入框填入上述路径即可。

### C. 修改联系信息
- 全站的邮箱地址已统一。如需再次修改，请前往 `app/models.py` 修改 `Profile` 模型的默认值，或者直接在管理后台的 Profile 页面进行修改。

---

## 4. 部署到腾讯云 (Windows Server) 指南

### 1. 服务器环境准备
- **安装 Python**: 下载并安装 Python 3.10+，安装时勾选 "Add Python to PATH"。
- **安装 Git**: 用于同步 GitHub 上的代码。

### 2. 拉取代码与安装依赖
打开服务器终端（PowerShell）：
```powershell
git clone <你的仓库地址>
cd "Xiao Ma's Digital Garden 2"
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### 3. 配置防火墙（腾讯云控制台）
- 登录腾讯云，进入“轻量应用服务器”详情页。
- 点击“防火墙” -> “添加规则”。
- 开放 **TCP:80** 端口（用于通过 IP 直接访问）或 **TCP:8000**。

### 4. 启动项目
在服务器终端中运行：
```powershell
# 使用 80 端口启动（需要管理员权限）
python -m uvicorn app.main:app --host 0.0.0.0 --port 80
```

### 5. 保持后台运行
建议在 Windows 上使用 **NSSM** 工具将该启动命令注册为“Windows 服务”，这样即使你退出远程桌面或服务器重启，网站依然可以正常运行。

---

## 5. 常用命令备忘

- **本地启动服务**: `python -m uvicorn app.main:app --reload`
- **重置数据库**: `python reset_db.py` (警告：这会清空所有数据)
- **提交更改到 Git**:
  ```bash
  git add .
  git commit -m "你的修改说明"
  git push origin main
  ```
