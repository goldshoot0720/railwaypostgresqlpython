import os
from dotenv import load_dotenv
import psycopg

# 載入環境變數
load_dotenv()

# 建立連線
conn = psycopg.connect(os.getenv("DATABASE_URL"))

with conn.cursor() as cur:
    cur.execute("""
        INSERT INTO cloud (name, site, account,space)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "dropbox/goldshoot0720",
        "https://www.dropbox.com/",
	"goldshoot0720@gmail.com",
        "5",
    ))
    conn.commit()

    cur.execute("""
        INSERT INTO cloud (name, site, account,space)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "InfiniCLOUD",
        "https://infini-cloud.net",
	"goldshoot0720@gmail.com",
        "48",
    ))
    conn.commit()

conn.close()
