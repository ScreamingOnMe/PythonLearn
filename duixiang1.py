class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}.')

    def play(self):
        print(f'{self.name}正在玩游戏.')


stu1 = Student('jack', 40)
stu2 = Student('juice', 15)
stu1.study('Python程序设计')
stu2.play()
