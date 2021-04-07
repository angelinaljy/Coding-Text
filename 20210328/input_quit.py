# 从控制台输入一系列的字符或数字，把这些逐个写入到文件中，直到连续输入了quit后则停止程序；

def input_quit():
    answers = []
    while True:
        answer = input("Please write down anything: (Quit the question by 'quit')")
        answers.append(answer)
        if answer == "quit":
            print(answers)
            break


if __name__ == "__main__":
    input_quit()



# 需要依次输入 quit 可以形成退出
