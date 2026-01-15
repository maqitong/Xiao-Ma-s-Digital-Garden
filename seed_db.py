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
            email="contact@xiaoma.dev"
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

    # Projects (If empty)
    if db.query(models.Project).count() == 0:
        print("Creating Projects...")
        # Add some dummy projects if none exist
        pass

    db.commit()
    print("Seeding complete.")

if __name__ == "__main__":
    seed()
