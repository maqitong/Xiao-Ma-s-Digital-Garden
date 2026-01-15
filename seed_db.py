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
            role="全栈开发工程师",
            bio="热爱技术，追求卓越。专注于构建高性能、用户友好的 Web 应用。",
            email="contact@xiaoma.dev",
            resume_url="/static/resumes/resume.pdf"
        )
        db.add(profile)
    
    # Experience
    if db.query(models.Experience).count() == 0:
        print("Creating Experience...")
        exps = [
            models.Experience(title="高级前端工程师", company="Tech Corp", duration="2021 - 至今", description="负责核心产品的前端架构设计与开发，带领团队完成多个大型项目重构。"),
            models.Experience(title="前端工程师", company="StartUp Inc", duration="2019 - 2021", description="参与早期产品研发，独立负责后台管理系统开发。")
        ]
        db.add_all(exps)

    # Education
    if db.query(models.Education).count() == 0:
        print("Creating Education...")
        edus = [
            models.Education(degree="计算机科学学士", school="某某大学", duration="2015 - 2019")
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
            models.Skill(name="Python", category="Backend"),
            models.Skill(name="PostgreSQL", category="Backend"),
            models.Skill(name="Figma", category="Tools"),
        ]
        db.add_all(skills)

    # Projects
    if db.query(models.Project).count() == 0:
        print("Creating Projects...")
        projects = [
            models.Project(
                title="E-Commerce Platform",
                description="A full-featured online store built with Next.js and Stripe integration. Includes product management, cart functionality, and secure checkout.",
                image_url="/static/projects_files/search-image.jpg",
                link="#",
                category="Web Development",
                tags="Next.js, Stripe, Tailwind"
            ),
            models.Project(
                title="Task Management App",
                description="A productivity tool for teams to organize tasks and track progress. Features real-time updates and collaborative boards.",
                image_url="/static/projects_files/search-image(1).jpg",
                link="#",
                category="Productivity",
                tags="React, Firebase, Redux"
            ),
            models.Project(
                title="Social Media Dashboard",
                description="Analytics dashboard for tracking social media performance. Visualizes data with interactive charts and graphs.",
                image_url="/static/projects_files/search-image(2).jpg",
                link="#",
                category="UI/UX Design",
                tags="Vue.js, Chart.js, Figma"
            ),
            models.Project(
                title="Travel Booking System",
                description="A comprehensive booking platform for flights and hotels. Integrates with multiple APIs for real-time pricing.",
                image_url="/static/projects_files/search-image(3).jpg",
                link="#",
                category="Web Development",
                tags="Python, Django, PostgreSQL"
            ),
            models.Project(
                title="Fitness Tracker App",
                description="Mobile-first application to track workouts and nutrition. Syncs with wearable devices.",
                image_url="/static/projects_files/search-image(4).jpg",
                link="#",
                category="Mobile App",
                tags="React Native, Node.js"
            ),
            models.Project(
                title="Portfolio Website",
                description="A modern, responsive portfolio website template for designers and developers.",
                image_url="/static/projects_files/search-image(5).jpg",
                link="#",
                category="Web Design",
                tags="HTML, CSS, JavaScript"
            ),
        ]
        db.add_all(projects)

    # Gallery
    if db.query(models.GalleryItem).count() == 0:
        print("Creating Gallery Items...")
        items = [
            models.GalleryItem(title="Mountain Sunrise", description="云南·梅里雪山", image_url="/static/gallery_files/search-image.jpg", category="Photography"),
            models.GalleryItem(title="City Lights", description="上海·外滩", image_url="/static/gallery_files/search-image(1).jpg", category="Photography"),
            models.GalleryItem(title="Street Portrait", description="北京·798艺术区", image_url="/static/gallery_files/search-image(2).jpg", category="Photography"),
            models.GalleryItem(title="Ocean Waves", description="海南·三亚", image_url="/static/gallery_files/search-image(3).jpg", category="Photography"),
            models.GalleryItem(title="Modern Architecture", description="深圳·平安金融中心", image_url="/static/gallery_files/search-image(4).jpg", category="Photography"),
            models.GalleryItem(title="Forest Path", description="四川·九寨沟", image_url="/static/gallery_files/search-image(5).jpg", category="Photography"),
            models.GalleryItem(title="Golden Hour", description="杭州·西湖", image_url="/static/gallery_files/search-image(6).jpg", category="Photography"),
            models.GalleryItem(title="Cherry Blossoms", description="武汉·东湖", image_url="/static/gallery_files/search-image(7).jpg", category="Photography"),
            models.GalleryItem(title="Night Market", description="台北·士林夜市", image_url="/static/gallery_files/search-image(8).jpg", category="Photography"),
        ]
        db.add_all(items)

    # Videos
    if db.query(models.VideoItem).count() == 0:
        print("Creating Video Items...")
        items = [
            models.VideoItem(title="Web Development Tutorial", description="Building a React app from scratch.", video_url="#", thumbnail_url="/static/videos_files/search-image.jpg", platform="YouTube"),
            models.VideoItem(title="UI Design Process", description="Designing a mobile app interface.", video_url="#", thumbnail_url="/static/videos_files/search-image(1).jpg", platform="Bilibili"),
        ]
        db.add_all(items)

    # Blog
    if db.query(models.BlogPost).count() == 0:
        print("Creating Blog Posts...")
        posts = [
            models.BlogPost(
                title="React 19 新特性深度解析", 
                excerpt="探索 React 19 带来的新特性，包括 Server Components, Actions 等。",
                content="<p>React 19 带来了革命性的变化...</p>",
                cover_image="/static/blog_files/search-image.jpg",
                author="Xiao Ma",
                date="2024-03-15",
                tags="React, Frontend"
            ),
            models.BlogPost(
                title="构建高性能的 Web 应用", 
                excerpt="分享一些提升 Web 应用性能的实用技巧和最佳实践。",
                content="<p>性能优化是 Web 开发中不可忽视的一环...</p>",
                cover_image="/static/blog_files/search-image(1).jpg",
                author="Xiao Ma",
                date="2024-03-10",
                tags="Performance, Web"
            ),
        ]
        db.add_all(posts)

    db.commit()
    print("Seeding complete.")

if __name__ == "__main__":
    seed()
