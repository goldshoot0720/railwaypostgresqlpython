import os
from dotenv import load_dotenv
import psycopg

# 載入環境變數
load_dotenv()

# 建立連線
conn = psycopg.connect(os.getenv("DATABASE_URL"))

with conn.cursor() as cur:

    # 建立 article 資料表
    cur.execute("""
        CREATE TABLE IF NOT EXISTS article (
            id serial PRIMARY KEY,
            title text UNIQUE,
            content text,
            newDate timestamp,
            url1 text,
            url2 text,
            url3 text
        );
    """)
    conn.commit()

    # 建立 mail 資料表
    cur.execute("""
        CREATE TABLE IF NOT EXISTS mail (
            id serial PRIMARY KEY,
            name text UNIQUE,
            host text,
            address text,
            account text,
            site text
        );
    """)
    conn.commit()

    # 建立 inventory 資料表
    cur.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            id serial PRIMARY KEY,
            name text UNIQUE,
            price integer,
            amount integer,
            img text,
            shop text
        );
    """)
    conn.commit()

    # 建立 experience 資料表
    cur.execute("""
        CREATE TABLE IF NOT EXISTS experience (
            id serial PRIMARY KEY,
            title text UNIQUE,
            year integer,
            gov text,
            site text
        );
    """)
    conn.commit()

    # 建立 member 資料表（已補上逗號）
    cur.execute("""
        CREATE TABLE IF NOT EXISTS member (
            id serial PRIMARY KEY,
            name text UNIQUE,
            title text,
            relation text,
            gov text,
            site text,
            img text
        );
    """)
    conn.commit()

    # 建立 bank 資料表
    cur.execute("""
        CREATE TABLE IF NOT EXISTS bank (
            id serial PRIMARY KEY,
            name text UNIQUE,
            deposit integer,
            site text,
            address text,
            withdrawals integer,
            transfer integer,
            activity text,
            card text,
            account text
        );
    """)
    conn.commit()

    # 建立 cloud 資料表
    cur.execute("""
        CREATE TABLE IF NOT EXISTS cloud (
            id serial PRIMARY KEY,
            name text UNIQUE,
            site text,
            account text,
            space integer
        );
    """)
    conn.commit()

    # 建立 routine 資料表（修正表名與語法）
    cur.execute("""
        CREATE TABLE IF NOT EXISTS routine (
            id serial PRIMARY KEY,
            name text UNIQUE,
            date1 date,
            date2 date,
            date3 date,
            note text,
            site text
        );
    """)
    conn.commit()

    # 建立 host 資料表
    cur.execute("""
        CREATE TABLE IF NOT EXISTS host (
            id serial PRIMARY KEY,
            name text UNIQUE,
            site text,
            account text
        );
    """)
    conn.commit()

    # 建立 subscription 資料表
    cur.execute("""
        CREATE TABLE IF NOT EXISTS subscription (
            id serial PRIMARY KEY,
            name text UNIQUE,
            site text,
            price integer,
            nextdate date,
            note text,
            account text
        );
    """)
    conn.commit()

    # 建立 video 資料表
    cur.execute("""
        CREATE TABLE IF NOT EXISTS video (
            id serial PRIMARY KEY,
            name text UNIQUE,
            url text,
            img text,
            type text,
            date text,
            song text,
            site text,
            watch text,
            youtube text,
            year integer,
            season text
        );
    """)
    conn.commit()

    # 建立 food 資料表（修正表名與型別、刪除尾逗號）
    cur.execute("""
        CREATE TABLE IF NOT EXISTS food (
            id serial PRIMARY KEY,
            name text UNIQUE,
            amount integer,
            price integer,
            shop text,
            todate text,
            photo text,
            photoHash text
        );
    """)
    conn.commit()

conn.close()
