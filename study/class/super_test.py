class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        print("차")

    def car_test(self):
        print("자동차 테스트")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        pass

    def test(self):
        print("전기차 테스트")


my_tesla = ElectricCar('tesla', 'model s ', 2019)
my_tesla.test()
my_tesla.car_test()
print(ElectricCar.mro()) # 상속 구조를 나타내어 주는 함수.
