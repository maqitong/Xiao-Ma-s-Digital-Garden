# Xiao Ma's Digital Garden

A full-stack personal digital garden built with FastAPI, SQLite, and TailwindCSS.

## 🚀 Version 3.0 Features

- **📝 Enhanced Blog Experience**:
    - **Markdown Support**: Write articles in Markdown with automatic HTML rendering.
    - **Code Highlighting**: Integrated Prism.js for beautiful code blocks.
    - **Detail View**: Dedicated page for reading full articles (`/blog/{id}`).

- **🔍 Global Search**:
    - Unified search bar in navigation.
    - Search across Blog Posts and Projects instantly.
    - Expandable search interaction design.

- **⚙️ Admin Capabilities**:
    - **Edit Mode**: Update existing blog posts directly from the admin dashboard.
    - Content management for Projects, Resume, Gallery, and Videos.

- **📚 Documentation**:
    - Added `docs/solo_coding_guide.md`: A guide for AI-assisted solo development.

## 🛠️ Tech Stack
- **Backend**: Python, FastAPI, SQLAlchemy
- **Database**: SQLite
- **Frontend**: Jinja2 Templates, TailwindCSS, JavaScript
- **Deployment**: Ready for standard Python environments.

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/maqitong/Xiao-Ma-s-Digital-Garden.git

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn app.main:app --reload
```
