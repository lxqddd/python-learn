import requests

resp = requests.get("https://jsonplaceholder.typicode.com/users/1", timeout=5)

data = resp.json()

print(f"用户名：{data['name']}\n邮箱：{data['email']} \n公司名：{data['company']['name']}")


todoResp = requests.get("https://jsonplaceholder.typicode.com/todos?userId=1", timeout=5)

todoData = todoResp.json()

print(f"The user {data['name']} has {len((todoData))} todos to need be resolve")

