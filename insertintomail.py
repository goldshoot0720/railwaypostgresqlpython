import os
from dotenv import load_dotenv
import psycopg

# 載入環境變數
load_dotenv()

# 建立連線
conn = psycopg.connect(os.getenv("DATABASE_URL"))

with conn.cursor() as cur:
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "goldshoot0720/hotmail",
        "outlook",
        "goldshoot0720@hotmail.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "abuhg17myyahoo",
        "gmail",
        "abuhg17myyahoo@gmail.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "goldshoot0720/outlook",
        "outlook",
        "goldshoot0720@outlook.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "miabubu20xx",
        "gmail",
        "miabubu20xx@gmail.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "abuhg2016",
        "gmail",
        "abuhg2016@gmail.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "goldshoot0721",
        "gmail",
        "goldshoot0721@gmail.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "soilshoot0720",
        "gmail",
        "soilshoot0720@gmail.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "fireshoot0720",
        "gmail",
        "fireshoot0720@gmail.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "watershoot0720",
        "gmail",
        "watershoot0720@gmail.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "woodshoot0720",
        "gmail",
        "woodshoot0720@gmail.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "ironshoot0720",
        "gmail",
        "ironshoot0720@gmail.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "coppershoot0720",
        "gmail",
        "coppershoot0720@gmail.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "silvershoot0720",
        "gmail",
        "silvershoot0720@gmail.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "tsaopaofenghsiungistaipeimayor",
        "gmail",
        "tsaopaofenghsiungistaipeimayor@gmail.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "tsaopaofenghsiung202507050418",
        "gmail",
        "tsaopaofenghsiung202507050418@gmail.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "tsaopaofenghsiung2025",
        "gmail",
        "tsaopaofenghsiung2025@gmail.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "chbondg2",
        "gmail",
        "chbondg2@gmail.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "feng33feng35feng3",
        "gmail",
        "feng33feng35feng3@gmail.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "chbondg2025",
        "gmail",
        "chbondg2025@gmail.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "goldshoot2025",
        "gmail",
        "goldshoot2025@gmail.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "tsaopaofenghsiung",
        "gmail",
        "tsaopaofenghsiung@gmail.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "peoper31206",
        "gmail",
        "peoper31206@gmail.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "peoper11206",
        "gmail",
        "peoper11206@gmail.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "fengwithlai1103",
        "gmail",
        "fengwithlai1103@gmail.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "fengwithtu1127",
        "gmail",
        "fengwithtu1127@gmail.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "fengwithting0831",
        "gmail",
        "fengwithting0831@gmail.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "tu0403withyu0723",
        "gmail",
        "tu0403withyu0723@gmail.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "fengwithfeng1127",
        "gmail",
        "fengwithfeng1127@gmail.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "abuhg17",
        "gmail",
        "abuhg17@gmail.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "goldshoot0720/gmail",
        "gmail",
        "goldshoot0720@gmail.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "goldshoot0720/aol",
        "aol",
        "goldshoot0720@aol.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "goldshoot0720/zohomail",
        "zohomail",
        "goldshoot0720@zohomail.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "goldshoot0720/yandex",
        "yandex",
        "goldshoot0720@yandex.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "goldshoot0720/vk",
        "vk",
        "goldshoot0720@vk.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "goldshoot0720/naver",
        "naver",
        "goldshoot0720@naver.com",
        None,
        None,
    ))
    conn.commit()
    cur.execute("""
        INSERT INTO mail (name, host, address, account, site)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (name) DO NOTHING
    """, (
        "goldshoot0720/daum",
        "daum",
        "goldshoot0720@daum.net",
        None,
        None,
    ))
    conn.commit()

conn.close()