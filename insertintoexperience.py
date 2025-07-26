import os
from dotenv import load_dotenv
import psycopg

# 載入環境變數
load_dotenv()

# 建立連線
conn = psycopg.connect(os.getenv("DATABASE_URL"))

with conn.cursor() as cur:
    cur.execute("""
        INSERT INTO experience (title, year, gov, site)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (title) DO NOTHING
    """, (
        "高考三級資訊處理榜首",
        "2025",
        "行政院人事行政總處",
        "https://www.dgpa.gov.tw"
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO experience (title, year, gov, site)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (title) DO NOTHING
    """, (
        "台北市長(候選人)",
        "2038",
        "台北市政府",
        "https://www.gov.taipei/"
    ))
    conn.commit()

conn.close()
