# W3 D5 周五 · 4h — 综合项目 weather-llm

- **阶段**：1 Python 突击 | **周次**：W3 | **状态**：⬜
- **主题**：把所有本周学的串成一个项目

---

## 🎯 今日目标（1 项）

- [ ] **完成 `sandbox/tiny-projects/02-weather-llm/` 综合项目**

---

## ✅ 任务清单（4h）

### 💻 综合项目（4h）

- [ ] **[240min]** 创建 `sandbox/tiny-projects/02-weather-llm/`：

  **目录结构：**
  ```
  02-weather-llm/
  ├── .env                # DEEPSEEK_API_KEY
  ├── .env.example        # 模板
  ├── settings.py         # 配置管理
  ├── weather_api.py      # 调真实天气 API
  ├── agent.py            # LLM 决策 + 返回建议
  ├── main.py             # 入口
  └── requirements.txt    # pydantic, python-dotenv, requests, openai
  ```

  **1. `settings.py`**（30min）

  ```python
  """配置"""
  import os
  from dotenv import load_dotenv
  from pydantic import BaseModel
  
  load_dotenv()
  
  class Settings(BaseModel):
      deepseek_api_key: str
      deepseek_base_url: str = "https://api.deepseek.com/v1"
      model_name: str = "deepseek-chat"
      openweather_api_key: str = ""
  
  settings = Settings(
      deepseek_api_key=os.getenv("DEEPSEEK_API_KEY", ""),
      openweather_api_key=os.getenv("OPENWEATHER_API_KEY", ""),
  )
  ```

  **2. `weather_api.py`**（45min）

  ```python
  """调 OpenWeather API"""
  import requests
  from settings import settings
  
  def get_weather(city: str) -> dict:
      """获取城市当前天气
      
      Returns:
          {"ok": True, "temp": 25, "description": "clear sky", "humidity": 60}
          或 {"ok": False, "error": "city_not_found"}
      """
      if not settings.openweather_api_key:
          return {"ok": False, "error": "no_api_key", "hint": "注册 https://openweathermap.org/"}
      
      url = "https://api.openweathermap.org/data/2.5/weather"
      params = {
          "q": city,
          "appid": settings.openweather_api_key,
          "units": "metric",
          "lang": "zh_cn",
      }
      
      try:
          resp = requests.get(url, params=params, timeout=10)
          data = resp.json()
          
          if resp.status_code == 404:
              return {"ok": False, "error": "city_not_found"}
          if resp.status_code != 200:
              return {"ok": False, "error": "api_error", "message": data.get("message", "")}
          
          return {
              "ok": True,
              "city": data["name"],
              "temp": data["main"]["temp"],
              "feels_like": data["main"]["feels_like"],
              "humidity": data["main"]["humidity"],
              "description": data["weather"][0]["description"],
              "wind_speed": data["wind"]["speed"],
          }
      except requests.Timeout:
          return {"ok": False, "error": "timeout"}
      except Exception as e:
          return {"ok": False, "error": "exception", "message": str(e)}
  ```

  **3. `agent.py`**（60min）

  ```python
  """LLM 决策：要不要调天气 API"""
  import os
  from openai import OpenAI
  from settings import settings as cfg
  from weather_api import get_weather
  
  client = OpenAI(api_key=cfg.deepseek_api_key, base_url=cfg.deepseek_base_url)
  
  SYSTEM_PROMPT = """你是一个穿衣助手。根据天气数据，给出穿衣建议。
  
  ## 输出格式（Markdown）
  ## 当前天气
  - 城市：
  - 温度：
  - 天气：
  - 湿度：
  
  ## 穿衣建议
  - ...
  """
  
  def get_clothing_advice(city: str) -> str:
      """获取城市的穿衣建议"""
      # 1. 调天气 API
      weather = get_weather(city)
      if not weather["ok"]:
          return f"❌ 获取天气失败：{weather.get('error')} - {weather.get('hint', weather.get('message', ''))}"
      
      # 2. 让 LLM 生成建议
      weather_text = f"""
      城市: {weather['city']}
      温度: {weather['temp']}°C（体感 {weather['feels_like']}°C）
      天气: {weather['description']}
      湿度: {weather['humidity']}%
      风速: {weather['wind_speed']} m/s
      """
      
      response = client.chat.completions.create(
          model=cfg.model_name,
          messages=[
              {"role": "system", "content": SYSTEM_PROMPT},
              {"role": "user", "content": f"请根据以下天气给出穿衣建议：\n{weather_text}"},
          ],
      )
      return response.choices[0].message.content
  ```

  **4. `main.py`**（30min）

  ```python
  """入口"""
  from agent import get_clothing_advice
  
  if __name__ == "__main__":
      city = input("输入城市名（如 Beijing）：").strip()
      if not city:
          print("城市名不能为空")
          exit(1)
      
      advice = get_clothing_advice(city)
      print("\n" + "=" * 40)
      print(advice)
      print("=" * 40)
  ```

  **5. `.env.example`**（5min）
  ```bash
  DEEPSEEK_API_KEY=sk-xxx
  OPENWEATHER_API_KEY=
  ```

  **6. `requirements.txt`**（5min）
  ```text
  pydantic>=2.0
  python-dotenv>=1.0
  requests>=2.31
  openai>=1.0
  ```

### 🧪 测试（30min）

- [ ] **[30min]** 跑测试：
  1. 没 OpenWeather Key → 优雅报错
  2. 输入不存在的城市 → 优雅报错
  3. 输入真实城市 → 输出穿衣建议
  - 截图存到 `notes/week3/weather-llm-demo.png`

---

## 📚 项目验收清单

- [ ] 项目结构清晰（settings / api / agent / main 分离）
- [ ] 用 pydantic 做配置管理
- [ ] 用 dotenv 读 .env
- [ ] 所有错误都用结构化 dict 返回
- [ ] 代码 ≤ 100 行（main + agent + weather_api 总和）
- [ ] README 写好（用 `02-weather-llm/README.md`）

---

## ✅ 当日验收

- [ ] `python main.py` 跑通
- [ ] 输入 "Beijing" 能拿到穿衣建议
- [ ] 代码提交到 Git

---

## 💡 关键测试

**LangChain 源码测试**：
打开 [LangChain 源码](https://github.com/langchain-ai/langchain) 任意文件，尝试读懂：
- 函数签名（应该看得懂）
- 类型提示（应该看得懂）
- pydantic 模型（应该看得懂）
- async/await（应该不陌生）

读懂率 ≥ 60% → 阶段 1 毕业 ✓
读懂率 < 60% → W3 周末多花时间补

---

**完成后**：周日打开 [`W3-review.md`](W3-review.md)