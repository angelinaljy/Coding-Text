from numpy import *

# 用字典存储一个班的学生信息（学号，姓名，性别，年龄，总分等），统计本班学生年龄最小的/最大的、分数最高的/最低的学生的信息，并输出到控制台；请求出男生的平均年龄、平均分；女生的平均年龄平均分；请求出本班的平均年龄、平均分。

student_01 = {"student_id": 202101, "name": "Angelina", "Gender": "Female", "Age":18, "Scores": 120}
student_02 = {"student_id": 202102, "name": "Bobby",    "Gender": "Male",   "Age":25, "Scores": 98 }
student_03 = {"student_id": 202103, "name": "Cindy",    "Gender": "Female", "Age":28, "Scores": 110}
student_04 = {"student_id": 202104, "name": "Douge",    "Gender": "Male",   "Age":15, "Scores": 79 }
student_05 = {"student_id": 202105, "name": "Ellen",    "Gender": "Male",   "Age":30, "Scores": 150}
student_06 = {"student_id": 202106, "name": "Flora",    "Gender": "Female", "Age":30, "Scores": 66 }

class_01 = {"student_01": student_01, "student_02": student_02, "student_03":student_03, "student_04": student_04, "student_05": student_05,
            "student_06": student_06}
print(f"The whole class info: {class_01}")



# 统计本班年纪最小/最大的年纪的学生信息：
age = []
for std_info in class_01.values():
    for key in std_info.keys():
        if key == "Age":
            age.append(std_info[key])
# print(age)
# print(max(age))
# print(min(age))

max_age_stds = {}
min_age_stds = {}
for std_number, std_details in class_01.items():
    for key in std_details.keys():
        if std_details[key] == max(age):
            max_age_stds[std_number] = std_details
        elif std_details[key] == min(age):
            min_age_stds[std_number] = std_details

print(f"The oldest student's info as below: {max_age_stds}")
print(f"The youngest student's info as below: {min_age_stds}")

# 全班平均年龄
class_age_avg = mean(age)
print(f"The average age of the class is: {class_age_avg:.4}")

# 统计分数最高/最低的学生信息：
scores = []
for std_info in class_01.values():
    for key in std_info.keys():
        if key == "Scores":
            scores.append(std_info[key])
# print(scores)
# print(max(scores))
# print(min(scores))

max_score_stds = {}
min_score_stds = {}

for std_number, std_details in class_01.items():
    for key in std_details.keys():
        if std_details[key] == max(scores):
            max_score_stds[std_number] = std_details
        elif std_details[key] == min(scores):
            min_score_stds[std_number] = std_details

print(f"The info of student who got the highest score as below: {max_score_stds}")
print(f"The info of student who got the lowest score as below: {min_score_stds}")

# 全班平均分
class_scores_avg = mean(scores)
print(f"The average score of the class: {class_scores_avg:.5}")

# 男生平均年龄
male_age = []
for std_info in class_01.values():
    if std_info['Gender'] == 'Male':
        male_age.append(std_info["Age"])

# print(male_age)
# print(max(male_age))
# print(min(male_age))
print(f"The average age of the boys: {mean(male_age):.4}")


# 男生平均分
male_scores = []
for std_info in class_01.values():
    if std_info['Gender'] == 'Male':
        male_scores.append(std_info["Scores"])
# print(male_scores)
print(f"The average scores of the boys: {mean(male_scores):.5}")

# 女生平均年龄
female_age = []
for std_info in class_01.values():
    if std_info['Gender'] == 'Female':
        female_age.append(std_info["Age"])

# print(female_age)
# print(max(female_age))
# print(min(female_age))
print(f"The average age of the girls: {mean(female_age):.4}")

# 女生平均分
female_scores = []
for std_info in class_01.values():
    if std_info['Gender'] == 'Female':
        female_scores.append(std_info["Scores"])
# print(female_scores)
print(f"The average score of the girls: {mean(female_scores):.5}")
