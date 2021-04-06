# 用字典存储一个班的学生信息（学号，姓名，性别，年龄，总分等），统计本班学生年龄最小的/最大的、分数最高的/最低的学生的信息，并输出到控制台；请求出男生的平均年龄、平均分；女生的平均年龄平均分；请求出本班的平均年龄、平均分。

# 班级学生信息的统计：
student_01 = {"student_id": 202101, "name": "Angelina", "Gender": "Female", "Age": 18, "Scores": 120}
student_02 = {"student_id": 202102, "name": "Bobby", "Gender": "Male", "Age": 25, "Scores": 98}
student_03 = {"student_id": 202103, "name": "Cindy", "Gender": "Female", "Age": 28, "Scores": 110}
student_04 = {"student_id": 202104, "name": "Douge", "Gender": "Male", "Age": 15, "Scores": 79}
student_05 = {"student_id": 202105, "name": "Ellen", "Gender": "Male", "Age": 30, "Scores": 150}
student_06 = {"student_id": 202106, "name": "Flora", "Gender": "Female", "Age": 30, "Scores": 66}

class_01 = {"student_01": student_01, "student_02": student_02, "student_03": student_03, "student_04": student_04,
            "student_05": student_05,
            "student_06": student_06}


# 生成年纪的统计列表
def get_age_list():
    age_list = []
    for std_info in class_01.values():
        # for key in std_info.keys():  get方法优于遍历，遍历太慢了 commented by shlian at 2021.04.06
        #    if key == "Age":
        #        age.append(std_info[key])
        age = std_info.get("Age")
        age_list.append(age)
    return age_list


# 生成分数统计列表
def get_scores_list():
    scores = []
    for std_info in class_01.values():
        for key in std_info.keys():
            if key == "Scores":
                scores.append(std_info[key])
    return scores


# 生成男年纪统计列表：
def get_male_stds_info():
    male_age = []
    for std_info in class_01.values():
        if std_info['Gender'] == 'Male':
            male_age.append(std_info["Age"])
    return male_age


# 生成男生分数统计列表：
def get_male_scores():
    male_scores = []
    for std_info in class_01.values():
        if std_info['Gender'] == 'Male':
            male_scores.append(std_info["Scores"])
    return male_scores


# 生成女生年龄统计列表：
def get_female_ages():
    female_age = []
    for std_info in class_01.values():
        if std_info['Gender'] == 'Female':
            female_age.append(std_info["Age"])
    return female_age


# 生成女生分数统计列表：
def get_female_scores():
    female_scores = []
    for std_info in class_01.values():
        if std_info['Gender'] == 'Female':
            female_scores.append(std_info["Scores"])
    return female_scores


# 统计本班年纪最大的年纪的学生信息：
def get_max_age_stds():
    max_age_stds = {}
    for std_number, std_details in class_01.items():
        for key in std_details.keys():
            if std_details[key] == max(get_age_list()):
                max_age_stds[std_number] = std_details
    print(f"The oldest student's info as below: {max_age_stds}")


# 统计本班年纪最小的年纪的学生信息：
def get_min_age_stds():
    min_age_stds = {}
    for std_number, std_details in class_01.items():
        for key in std_details.keys():
            if std_details[key] == min(get_age_list()):
                min_age_stds[std_number] = std_details
    print(f"The youngest student's info as below: {min_age_stds}")


# 全班平均年龄
def get_class_age_avg():
    class_age_avg = sum(get_age_list()) / len(get_age_list())
    print(f"The average age of the class is: {class_age_avg:.4}")


# 统计分数最低的学生信息：
def get_min_score_stds():
    min_score_stds = {}
    for std_number, std_details in class_01.items():
        for key in std_details.keys():
            if std_details[key] == min(get_scores_list()):
                min_score_stds[std_number] = std_details
    print(f"The info of student who got the lowest score as below: {min_score_stds}")


# 统计分数最高的学生信息：
def get_max_score_stds():
    max_score_stds = {}
    for std_number, std_details in class_01.items():
        for key in std_details.keys():
            if std_details[key] == max(get_scores_list()):
                max_score_stds[std_number] = std_details
    print(f"The info of student who got the highest score as below: {max_score_stds}")


# 全班平均分
def get_class_scores_avg():
    class_scores_avg = sum(get_scores_list()) / len(get_scores_list())
    print(f"The average score of the class: {class_scores_avg:.5}")


# 男生平均年龄
def get_male_ages_avg():
    print(f"The average age of the boys: {sum(get_male_stds_info()) / len(get_male_stds_info()):.4}")


# 男生平均分
def get_male_scores_avg():
    print(f"The average scores of the boys: {sum(get_male_scores()) / len(get_male_scores()):.5}")


# 女生平均年龄
def get_female_ages_avg():
    print(f"The average age of the girls: {sum(get_female_ages()) / len(get_female_ages()):.4}")


# 女生平均分
def get_female_scores_avg():
    print(f"The average score of the girls: {sum(get_female_scores()) / len(get_female_scores()):.5}")


if __name__ == "__main__":
    get_min_age_stds()
    get_max_age_stds()
    get_class_age_avg()
    get_min_score_stds()
    get_max_score_stds()
    get_class_scores_avg()
    get_male_ages_avg()
    get_male_scores_avg()
    get_female_ages_avg()
    get_female_scores_avg()
