import requests
import json

# FRED APIキー
api_key = '3a9b149188c85dfdf21e468641cd8a0a'

# FREDからT10Y2Yデータを取得
url = f"https://api.stlouisfed.org/fred/series/observations?series_id=T10Y2Y&api_key={api_key}&file_type=json"
response = requests.get(url)
data = response.json()

# データをJSONファイルとして保存
with open('t10y2y_data.json', 'w') as f:
    json.dump(data, f, indent=4)

