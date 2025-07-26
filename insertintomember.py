import os
from dotenv import load_dotenv
import psycopg

# 載入環境變數
load_dotenv()

# 建立連線
conn = psycopg.connect(os.getenv("DATABASE_URL"))

with conn.cursor() as cur:
    cur.execute("""
        INSERT INTO member (name, title,relation, gov, site,img)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "塗○傑",
        "董事",
        "國中同班同學",
        "臺北農產運銷股份有限公司",
        "https://www.tapmc.com.tw",
        None
    ))
    conn.commit()

conn.close()
