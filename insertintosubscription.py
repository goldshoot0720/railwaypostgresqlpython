import os
from dotenv import load_dotenv
import psycopg

# 載入環境變數
load_dotenv()

# 建立連線
conn = psycopg.connect(os.getenv("DATABASE_URL"))

with conn.cursor() as cur:
    cur.execute("""
        INSERT INTO subscription (name, site, price, nextdate, note, account)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "linode",
        "https://cloud.linode.com/linodes",
        "213",
        None,
        """
Nanode 1 GB $5美元
Virtual Private Server 
""",
        "goldshoot0720@gmail.com"
    ))
    conn.commit()

conn.close()
