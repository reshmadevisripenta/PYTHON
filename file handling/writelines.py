courses = [
"Python\n",
"Java\n",
"Data Science\n",
"Digital Marketing\n"
]
with open("courses.txt", "w") as file:
file.writelines(courses = ["Python", "Java", "Data Science"])

courses = ["Python", "Java", "Data Science"]
with open("courses2.txt", "w") as file:
    file.writelines(courses)