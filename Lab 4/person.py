class Person:
    moods = ("happy", "tired", "lazy")
    def __init__(self, name: str, money: int):
        self.name = name
        self.money = money
        self.mood = None
        self.healthRate = None
    def money(self):
        return self.money
    def money(self, money: int):
        if isinstance(money, int):
            if money >= 0:
                self.money = money
            else:
                print("The value of money can't be negative")

        else:
            print("Money must be integer")
    def healthRate(self):
        return self.healthRate
    def healthRate(self, healthRate: int):
        if isinstance(healthRate, int):
            if 0 <= healthRate <= 100:
                self.healthRate = healthRate
            else:
                print("Health rate must be between 0 and 100")
        else:
            print("Health rate must be integer")
    def Sleep(self, cls, hours: int):
        if isinstance(hours, int):
            if hours == 7:
                self.mood = cls.moods[0]

            elif hours > 7:
                self.mood = cls.moods[1]

            else:
                self.mood = cls.moods[2]
        else:
            print("Hours must be integer")
    def Eat(self, meals: int):
        if isinstance(meals, int):
            if meals == 3:
                self.healthRate = 100
            elif meals == 2:
                self.healthRate = 75
            elif meals == 1:
                self.healthRate = 0
            else:
                print("Number of meals must be 1, 2 or 3")
        else:
            print("Meals must be integer")
    def Buy(self, items: int):
        self.money -= items * 10