from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

die = Die()

results = []
for roll_num in range(1000):
    result = die.roll()  # 주사위 1000번 굴리기
    results.append(result)

frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)  # 1~6까지 나온 값을 세서 넣어준다.
    frequencies.append(frequency)

x_values = list(range(1, die.num_sides + 1))
data = [Bar(x=x_values, y=frequencies)]  # x,y의 값을 Bar(막대그래프)형태의 데이터세트로 변환

x_axis_config = {'title': 'Result'}  # x축 눈금 title
y_axis_config = {'title': 'Frequency of Result'}  # y축 눈금 title
my_layout = Layout(title='정육면체 주사위를 1000번 던진 결과', xaxis=x_axis_config, yaxis=y_axis_config)  # layout 설정
offline.plot({'down_data': data, 'layout': my_layout}, filename='d6.html')  # 결과 html로 확인.

