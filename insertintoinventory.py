import os
from dotenv import load_dotenv
import psycopg

# 載入環境變數
load_dotenv()

# 建立連線
conn = psycopg.connect(os.getenv("DATABASE_URL"))

with conn.cursor() as cur:
    cur.execute("""
        INSERT INTO inventory (name, price, amount, img, shop)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "芋泥蒙布朗布丁",
        "55",
        "1",
        "https://fra.cloud.appwrite.io/v1/storage/buckets/6867c5280021205ba9c0/files/68847b530005e70ef90d/view?project=680c76af0037a7d23e44&mode=admin",
        "全家",
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO inventory (name, price, amount, img, shop)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "香蕉巧克力夾心酥",
        "49",
        "1",
        "https://fra.cloud.appwrite.io/v1/storage/buckets/6867c5280021205ba9c0/files/68847bce003af8788807/view?project=680c76af0037a7d23e44&mode=admin",
        "全家",
    ))
    conn.commit()

conn.close()