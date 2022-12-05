import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]  # 그래프로 그릴 데이터 세트
input_values = [1, 2, 3, 4, 5]  # 그래프로 그릴 데이터 세트
c = [0, 0, 1, 0, 1]
fig, ax = plt.subplots()  # fig와 ax객체 생성
ax.scatter(input_values, squares, c=c, cmap='spring', linewidth=3)  # 데이터를 그래프로 표현

ax.set_title("Square Numbers", fontsize=24)  # 타이틀 지정
ax.set_xlabel("Value", fontsize=14)  # x축 label 지정
ax.set_ylabel("Square of Value", fontsize=14)  # y축 label지정
ax.tick_params(axis='both', labelsize=14)  # 눈금 지정.

plt.show()  # viewer에 그래프를 표시
