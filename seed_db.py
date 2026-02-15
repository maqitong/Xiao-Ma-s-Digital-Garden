from app import models, database, crud
from sqlalchemy.orm import Session

db = database.SessionLocal()

def seed():
    print("Seeding database...")
    
    # Profile
    if not db.query(models.Profile).first():
        print("Creating Profile...")
        profile = models.Profile(
            name="小马",
            role="全栈开发工程师 / 摄影爱好者",
            bio="热爱技术，追求卓越。专注于构建高性能、用户友好的 Web 应用。在工作之余，我也喜欢通过镜头记录生活的美好。",
            email="mqtfire@qq.com",
            resume_url="/static/resumes/resume.pdf"
        )
        db.add(profile)
    
    # Experience
    if db.query(models.Experience).count() == 0:
        print("Creating Experience...")
        exps = [
            models.Experience(
                title="高级前端工程师", 
                company="某科技公司", 
                duration="2021 - 至今", 
                description="负责公司核心产品的前端架构设计与开发\n带领团队完成多个大型项目的交付\n优化性能，提升用户体验"
            ),
            models.Experience(
                title="前端工程师", 
                company="某互联网公司", 
                duration="2019 - 2021", 
                description="参与多个Web应用的开发与维护\n与设计师和后端工程师紧密协作\n学习并应用最新的前端技术"
            ),
            models.Experience(
                title="前端实习生", 
                company="某创业公司", 
                duration="2018 - 2019", 
                description="协助开发公司官网和管理系统\n学习前端开发的基础知识和最佳实践"
            )
        ]
        db.add_all(exps)

    # Education
    if db.query(models.Education).count() == 0:
        print("Creating Education...")
        edus = [
            models.Education(degree="计算机科学学士", school="某大学", duration="2015 - 2019")
        ]
        db.add_all(edus)

    # Skills
    if db.query(models.Skill).count() == 0:
        print("Creating Skills...")
        skills = [
            models.Skill(name="React / Next.js", category="Frontend"),
            models.Skill(name="TypeScript", category="Frontend"),
            models.Skill(name="Tailwind CSS", category="Frontend"),
            models.Skill(name="Vue.js", category="Frontend"),
            models.Skill(name="Node.js", category="Backend"),
            models.Skill(name="Python / FastAPI", category="Backend"),
            models.Skill(name="PostgreSQL / SQLite", category="Backend"),
            models.Skill(name="Git / Docker", category="Tools"),
        ]
        db.add_all(skills)

    # Projects
    if db.query(models.Project).count() == 0:
        print("Creating Projects...")
        projects = [
            models.Project(
                title="个人数字花园",
                description="基于 FastAPI 和 Tailwind CSS 构建的现代化个人网站，集成博客、作品集和管理后台。",
                image_url="/static/gallery_files/1.png",
                link="#",
                category="Web Development",
                tags="FastAPI, Tailwind, Jinja2"
            ),
            models.Project(
                title="电商平台前端重构",
                description="使用 Next.js 对原有电商系统进行性能优化和 SEO 重构，提升首屏加载速度 40%。",
                image_url="/static/projects_files/search-image.jpg",
                link="#",
                category="Web Development",
                tags="Next.js, TypeScript"
            ),
        ]
        db.add_all(projects)

    # Gallery
    if db.query(models.GalleryItem).count() == 0:
        print("Creating Gallery Items...")
        items = [
            models.GalleryItem(title="摄影作品 1", description="昙华林游记", image_url="/static/gallery_files/1.png", category="Photography"),
            models.GalleryItem(title="生活记录 2", description="城市角落", image_url="/static/gallery_files/2.jpg", category="Life"),
            models.GalleryItem(title="生活记录 3", description="光影瞬间", image_url="/static/gallery_files/3.jpg", category="Life"),
            models.GalleryItem(title="生活记录 4", description="静谧时刻", image_url="/static/gallery_files/4.jpg", category="Life"),
            models.GalleryItem(title="生活记录 5", description="街头色彩", image_url="/static/gallery_files/5.jpg", category="Life"),
            models.GalleryItem(title="生活记录 6", description="午后时光", image_url="/static/gallery_files/6.jpg", category="Life"),
            models.GalleryItem(title="生活记录 7", description="夜色朦胧", image_url="/static/gallery_files/7.jpg", category="Life"),
        ]
        db.add_all(items)

    # Videos
    if db.query(models.VideoItem).count() == 0:
        print("Creating Video Items...")
        items = [
            models.VideoItem(title="技术分享视频", description="关于 FastAPI 的实战教程。", video_url="#", thumbnail_url="/static/videos_files/search-image.jpg", platform="Bilibili"),
        ]
        db.add_all(items)

    # Blog
    if db.query(models.BlogPost).count() == 0:
        print("Creating Blog Posts...")
        posts = [
            models.BlogPost(
                title="我的网站上线啦", 
                excerpt="记录一下数字花园从构思到部署的全过程。",
                content="<p>这是我的第一篇博客内容...</p>",
                cover_image="/static/blog_files/search-image.jpg",
                author="小马",
                date="2024-01-15",
                tags="Announcement"
            ),
        ]
        db.add_all(posts)

    db.commit()
    print("Seeding complete.")

if __name__ == "__main__":
    seed()
