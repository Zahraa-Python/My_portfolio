from flask import Flask, render_template

app = Flask(__name__)

# Task 6: قائمة المشاريع بصيغة قواميس مطابقة تماماً للمصطلحات المطلوبة في الورقة
projects = [
    {
        "title": "Python Calculator",
        "description": "A calculator built using Python programming language.",
        "tech_stack": "Python",
        "image": "file_manager.png"
    },
    {
        "title": "Personal Portfolio",
        "description": "A personal website built using Flask, HTML and CSS.",
        "tech_stack": "Flask, HTML, CSS",
        "image": "portfolio.png"
    },
    {
        "title": "Python File Manager",
        "description": "A simple project for organizing files using Python.",
        "tech_stack": "Python",
        "image": "file_manager.png"
    }
]

@app.route("/")
def home():
    # Task 5: قائمة المهارات الحقيقية المكتسبة
    skills = ["Python", "Flask", "HTML", "CSS"]
    return render_template(
        "index.html",
        projects=projects,
        skills=skills
    )

if __name__ == "__main__":
    app.run(debug=True)