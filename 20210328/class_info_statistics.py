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


# 打印学生信息
def print_class(class_number):
    for k, v in class_number.items():
        print(f"{k}:{v}")


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
    scores_list = []
    for std_info in class_01.values():
        score = std_info.get("Scores")
        scores_list.append(score)
    return scores_list


# 生成男年纪统计列表：
def get_male_stds_info():
    male_ages = []
    for std_info in class_01.values():
        if std_info['Gender'] == 'Male':
            male_age = std_info.get("Age")
            male_ages.append(male_age)
    return male_ages


# 生成男生分数统计列表：
def get_male_scores():
    male_scores = []
    for std_info in class_01.values():
        if std_info['Gender'] == 'Male':
            male_score = std_info.get("Scores")
            male_scores.append(male_score)
    return male_scores


# 生成女生年龄统计列表：
def get_female_ages():
    female_ages = []
    for std_info in class_01.values():
        if std_info['Gender'] == 'Female':
            female_age = std_info.get("Age")
            female_ages.append(female_age)
    return female_ages


# 生成女生分数统计列表：
def get_female_scores():
    female_scores = []
    for std_info in class_01.values():
        if std_info['Gender'] == 'Female':
            female_score = std_info.get("Scores")
            female_scores.append(female_score)
    return female_scores


# 统计本班年纪最大的年纪的学生信息：
def get_max_age_stds():
    print(f"\nThe oldest student's info as below:")
    for std_number, std_details in class_01.items():
        if std_details.get("Age") == max(get_age_list()):
            print(std_number)
            for k, v in std_details.items():
                print(f"\t{k}:{v}")


# 统计本班年纪最小的年纪的学生信息：
def get_min_age_stds():
    print(f"\nThe youngest student's info as below:")
    for std_number, std_details in class_01.items():
        if std_details.get("Age") == min(get_age_list()):
            print(std_number)
            for k, v in std_details.items():
                print(f"\t{k}:{v}")


# 全班平均年龄
def get_class_age_avg():
    class_age_avg = sum(get_age_list()) / len(get_age_list())
    print(f"\nThe average age of the class is: {class_age_avg:.4}")


# 统计分数最低的学生信息：
def get_min_score_stds():
    print(f"\nThe info of student who got the lowest score as below:")
    for std_number, std_details in class_01.items():
        if std_details.get("Scores") == min(get_scores_list()):
            print(std_number)
            for k, v in std_details.items():
                print(f"\t{k}:{v}")



# 统计分数最高的学生信息：
def get_max_score_stds():
    print(f"\nThe info of student who got the highest score as below:")
    for std_number, std_details in class_01.items():
        if std_details.get("Scores") == max(get_scores_list()):
            print(std_number)
            for k, v in std_details.items():
                print(f"\t{k}:{v}")


# 全班平均分
def get_class_scores_avg():
    class_scores_avg = sum(get_scores_list()) / len(get_scores_list())
    print(f"\nThe average score of the class: {class_scores_avg:.5}")


# 男生平均年龄
def get_male_ages_avg():
    print(f"\nThe average age of the boys: {sum(get_male_stds_info()) / len(get_male_stds_info()):.4}")


# 男生平均分
def get_male_scores_avg():
    print(f"\nThe average scores of the boys: {sum(get_male_scores()) / len(get_male_scores()):.5}")


# 女生平均年龄
def get_female_ages_avg():
    print(f"\nThe average age of the girls: {sum(get_female_ages()) / len(get_female_ages()):.4}")


# 女生平均分
def get_female_scores_avg():
    print(f"\nThe average score of the girls: {sum(get_female_scores()) / len(get_female_scores()):.5}")


if __name__ == "__main__":
    print_class(class_01)
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
