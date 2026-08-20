# 🐍 Python 练习场（阶段 1）

第 2-3 周用：每天写小练习，先打好 Python 基础。

## 📂 建议结构

```
sandbox/
├── README.md            ← 本文件
├── week2-basics/        ← 语法、列表、字典、函数
├── week3-advanced/      ← 类、异步、类型、pydantic
└── tiny-projects/       ← 小项目练手
```

## 🎯 阶段 1 必会清单

### Week 2 · 基础
- [ ] 变量、数据类型、字符串格式化（f-string）
- [ ] 列表 / 字典 / 集合 / 元组 的增删改查
- [ ] 条件、循环、`for...else`
- [ ] 函数、`*args` / `**kwargs`、lambda
- [ ] 异常处理 `try / except / finally`
- [ ] 文件读写、JSON 处理
- [ ] `requests` 调 API

### Week 3 · 进阶
- [ ] 类与对象、`__init__`、`self`
- [ ] 继承、装饰器
- [ ] 生成器、`yield`
- [ ] `async / await` 基本语法
- [ ] 类型提示（type hints）
- [ ] `pydantic` BaseModel
- [ ] `python-dotenv` 读 .env

## 🎁 练手小项目

完成后能调 LLM API：

```python
# tiny-projects/01-weather-cli/weather.py
import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_weather(city: str) -> dict:
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()

if __name__ == "__main__":
    data = get_weather("Beijing")
    print(f"{data['name']}: {data['main']['temp']}°K")
```

## 🔧 环境安装

```bash
# 用 uv（推荐，超级快）
curl -LsSf https://astral.sh/uv/install.sh | sh
uv python install 3.11
uv venv
source .venv/bin/activate

# 或者用传统方式
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 📚 推荐资源

- 官方教程：https://docs.python.org/zh-cn/3/tutorial/
- Real Python：https://realpython.com/
- 《Python编程：从入门到实践》前半本

完成 Week 2-3 后，**回到 [README.md 主计划](../README.md)** 进入阶段 2 First 7 Days Sprint。