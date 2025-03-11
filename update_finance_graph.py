import requests
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Alpha Vantage API 키
API_KEY = "YOUR_API_KEY"
CURRENCY_PAIR = ("USD", "KRW")
URL = f"https://www.alphavantage.co/query?function=FX_DAILY&from_symbol={CURRENCY_PAIR[0]}&to_symbol={CURRENCY_PAIR[1]}&apikey={API_KEY}"

# 데이터 요청
response = requests.get(URL)
data = response.json().get("Time Series FX (Daily)", {})

# 데이터 가공
df = pd.DataFrame.from_dict(data, orient="index").astype(float)
df.index = pd.to_datetime(df.index)
df = df.sort_index().tail(30)  # 최근 30일 데이터

# 그래프 생성
plt.figure(figsize=(8, 3))
plt.plot(df.index, df["4. close"], marker="o", linestyle="-", color="blue", label=f"{CURRENCY_PAIR[0]}/{CURRENCY_PAIR[1]}")
plt.fill_between(df.index, df["4. close"], color="blue", alpha=0.1)
plt.xlabel("날짜")
plt.ylabel("환율")
plt.title("최근 30일 환율 변동")
plt.xticks(rotation=45)
plt.legend()
plt.grid()

# SVG 저장
plt.savefig("finance_graph.svg", format="svg", bbox_inches="tight")
