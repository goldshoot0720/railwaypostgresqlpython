import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from datetime import datetime

# 載入環境變數
load_dotenv()

# 連接 MongoDB
client = MongoClient(os.getenv("MONGODB_URI"))
db = client["railway"]
collection = db["article"]

# 建立 title 唯一索引（只需一次，之後會自動忽略重複）
collection.create_index("title", unique=True)

# 要插入的兩筆資料
articles = [
    {
        "title": "7月6日公務人員高考三級考試延期舉行",
        "content": """引用來源:
https://wwwc.moex.gov.tw/main/news/wfrmNews.aspx?kind=3&menu_id=42&news_id=7518
引用內容:
114/07/05
114年公務人員高考三級考試設臺北、桃園、新竹、苗栗、臺中、彰化、雲林、嘉義、臺南、高雄、宜蘭、花蓮、臺東、澎湖、金門、馬祖16考區，原定7月6日至8日舉行，因受丹娜絲颱風影響，臺南市政府、高雄市政府等已宣布7月6日停止上班上課...""",
        "newDate": datetime.strptime("2025-07-23 07:23:26", "%Y-%m-%d %H:%M:%S"),
        "url1": "https://fra.cloud.appwrite.io/v1/storage/buckets/6867c5280021205ba9c0/files/687fe17d00145748fcfc/view?project=680c76af0037a7d23e44&mode=admin",
        "url2": None,
        "url3": None
    },
    {
        "title": "受丹娜絲颱風持續影響 114年公務人員高考三級考試再度順延至7月8日至10日舉行",
        "content": """引用來源:
https://wwwc.moex.gov.tw/main/news/wfrmNews.aspx?kind=3&menu_id=42&news_id=7520
引用內容:
114/07/06
考選部表示，依據中央氣象署最新颱風預報資料顯示，丹娜絲颱風暴風圈進入臺灣南部陸地，對臺灣各地及澎湖構成威脅...""",
        "newDate": datetime.strptime("2025-07-24 07:24:26", "%Y-%m-%d %H:%M:%S"),
        "url1": "https://fra.cloud.appwrite.io/v1/storage/buckets/6867c5280021205ba9c0/files/686a5ee800352c80f246/view?project=680c76af0037a7d23e44&mode=admin",
        "url2": None,
        "url3": None
    }
]

# 插入資料，處理重複錯誤
for article in articles:
    try:
        collection.insert_one(article)
        print(f"✅ 成功插入：{article['title']}")
    except DuplicateKeyError:
        print(f"⚠️ 已存在，略過：{article['title']}")

# 關閉連線（非必要，程式結束會自動關閉）
client.close()
