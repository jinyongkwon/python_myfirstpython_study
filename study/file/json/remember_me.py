import json

filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("이름이 뭐에요?")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"만나서 반가워요{username}")
else:
    print(f.read())
    print(f"환영합니다{username}")

