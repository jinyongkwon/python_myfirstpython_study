from random import choice


class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])  # 1이면 오른쪽 , -1이면 왼쪽으로 움직임

            x_distance = choice([0, 1, 2, 3, 4])  # 정해진 방향으로 얼마나 움직일지 결정
            x_step = x_direction * x_distance  # 각 방향으로 얼마나 움직일지 결정

            y_direction = choice([1, -1])

            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance  # x는 좌우, y는 상하

            if x_step == 0 and y_step == 0:  # 모두 0이면 움직임 x 무시후 진행
                continue

            x = self.x_values[-1] + x_step  # x,y의 다음값을 구함.
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

        # print(self.x_values)
        # print(self.y_values)