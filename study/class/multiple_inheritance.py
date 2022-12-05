class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        print("차")

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"이 차는 {self.odometer_reading}km만큼 달렸습니다.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("주행거리계를 올릴수 없습니다.")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("연료를 채웁니다.")

    def test(self):
        print("차 테스트")


class Battery:
    # 전기자동차에서 배터리만  클래스로 분리
    def __init__(self, battery_size=75):
        print("배터리")
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"이 차의 배터리는 {self.battery_size}KWh입니다.")

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"현재 배터리로 {range}km만큼 이동할수 있습니다.")

    def test(self):
        print("배터리 테스트")


class ElectricCar(Car, Battery):
    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year)  # ElectricCar의 부모클래스 호출 = Car
        super(Car, self).__init__()  # Car의 부모클래스 호출 = Battery
        super(Battery, self).__init__()  # Battery의 부모클래스 호출 = object
        self.battery_size = 75  # ElectricCar에서만 사용하는 변수
        self.battery = Battery()  # 클래스의 일부분을 다른 클래스로 분리

        def fill_gas_tank(self):  # 오버라이드
            print("전기자동차에는 연료탱크가 없습니다.")


print(ElectricCar.mro())
my_tesla = ElectricCar('tesla', 'model s ', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.battery.describe_battery()  # .연산자를 통해 배터리 내부 메서드 호출.
my_tesla.battery.get_range()
my_cooper = Car('mini', 'cooper', 2021)
my_cooper.fill_gas_tank()
my_tesla.fill_gas_tank()
my_tesla.test()
