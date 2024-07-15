courses = {
    "js": "JavaScript 101",
    "Python": ["Python 101", "Python 201"],
    "html": "Html 101"
}

# print(courses.get("css", "CSS 101"))
if courses.get("css", None):
    print("You are enrolled in css 101")