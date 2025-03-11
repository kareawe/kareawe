import matplotlib.pyplot as plt

# 기술 스택 & 실력 (0~100%)
skills = {
    "Python": 85,
    "SQL": 80,
    "React": 75,
    "TypeScript": 70,
    "Tailwind CSS": 65,
    "Pandas": 85,
}

plt.figure(figsize=(10, 5))
plt.bar(skills.keys(), skills.values(), color=['blue', 'orange', 'green', 'red', 'purple', 'cyan'])

plt.xlabel("Tech Stack")
plt.ylabel("Skill Level (%)")
plt.title("📈 My Technical Skills (Stock Chart Style)")
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 이미지 저장
plt.savefig("tech_skills_chart.png")
plt.show()
