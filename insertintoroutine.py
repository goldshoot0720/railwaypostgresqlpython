import os
from dotenv import load_dotenv
import psycopg

# 載入環境變數
load_dotenv()

# 建立連線
conn = psycopg.connect(os.getenv("DATABASE_URL"))

with conn.cursor() as cur:
    cur.execute("""
        INSERT INTO routine (name, date1,date2, date3, note,site)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "天晟/身心科/譚詠康",
        "2025-07-31",
        None,
        None,
        "買潤餅",
        "https://www.tcmg.com.tw/index.php/main/schedule_time?id=14"
    ))
    conn.commit()

conn.close()
