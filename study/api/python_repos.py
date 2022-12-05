import requests
from plotly.graph_objs import Bar
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:python&amp;sort=starts'
headers = {'Accept': 'application/vnd.github.v3+json'}  # base64로 인코딩된 json을 반환.
r = requests.get(url, headers=headers)
print(f"응답 코드 : {r.status_code}")

response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, starts, labels = [], [], []

for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>" #html을 사용하여 하이퍼링크 사용
    repo_links.append(repo_link)
    starts.append(repo_dict['stargazers_count'])
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

data = [{
    'type': 'bar',
    'x': repo_links,
    'y': starts,
    'hovertext': labels
}]
my_layout = {
    'title': 'Most-Starred Python Projects on Github',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Starts'}
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
