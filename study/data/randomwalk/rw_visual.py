import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()

    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    print(point_numbers)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, s=1)
    ax.get_xaxis().set_visible(False) # x,y의 축을 제거
    ax.get_yaxis().set_visible(False)
    ax.scatter(0, 0, c='green', cmap=plt.cm.Reds, s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)

    plt.show()

    keep_running = input("랜덤워크를 더 진행하시겠습니까 ? (y/n)")
    if keep_running == 'n':
        break
