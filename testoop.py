class Person():
    def __init__(self, name, age, height, weight, address):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.address = address
        #self.cardid = cardid

    def eatting(self, food):
        self.food = food
        print(f'{self.name}正在吃{self.food}.')

    def sport(self, sport_name):
        #self.sport_name = sport_name
        print(f'{self.name}正在玩{sport_name}.')


person_1 = Person('lijian', 31, 180, 140, '南波大厦')
person_1.eatting('午饭')
person_1.sport('足球')


class Person_add(Person):
    def __init__(self, name, age, heiget, weight, address, cardid):
        super().__init__(name, age, heiget, weight, address)
        self.cardid = cardid
        print(f'{self.name}的id号码是{cardid}')


person_2 = Person_add('lijian', 31, 180, 140, '南波大厦', 123)
person_2.sport('足球')
