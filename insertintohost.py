import os
from dotenv import load_dotenv
import psycopg

# 載入環境變數
load_dotenv()

# 建立連線
conn = psycopg.connect(os.getenv("DATABASE_URL"))

with conn.cursor() as cur:
    cur.execute("""
        INSERT INTO host (name, site,account)
        VALUES (%s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "wordpress/miabubu20xx",
        "https://wordpress.com/",
        "miabubu20xx@gmail.com",
    ))
    conn.commit()

conn.close()
