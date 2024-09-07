import sqlite3
import random
from datetime import datetime, timedelta
import os

def create_bundle_db():
    # Подключение к базе данных
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
#frontrun hash 
    # Создание таблицы bundlesIncluded
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS bundlesIncluded (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        userid BIGINT UNSIGNED,
        username VARCHAR(32),
        token CHAR(42),
        frontrunValue DECIMAL(12,6),
        backrunValue DECIMAL(12,6),
        pnl DECIMAL(12,6) DEFAULT 0,
        includedBlock BIGINT UNSIGNED,
        frontrunHash CHAR(66), 
        victimHash CHAR(66),
        backrunHash CHAR(66),
        minVictimBuy DECIMAL(9,2),
        minLiquidity DECIMAL(9,2),
        maxLiquidity DECIMAL(12,2),
        minTokenHolders BIGINT UNSIGNED,
        maxTaxBuy DECIMAL(5,2),
        maxTaxSell DECIMAL(5,2),
        minSlippage INT UNSIGNED,
        minPriceImpact INT UNSIGNED,
        bribe DECIMAL(4,2),
        minBuy DECIMAL(9,2),
        maxBuy DECIMAL(9,2),
        victimValue DECIMAL(12,6),
        victimSlippage INT UNSIGNED,
        victimPriceImpact INT UNSIGNED,
        tokenTaxBuy DECIMAL(5,2),
        tokenTaxSell DECIMAL(5,2),
        tokenHolders BIGINT UNSIGNED,
        tokenLP DECIMAL(16,1),
        minimizedValue DECIMAL(12,6),
        maximizedValue DECIMAL(12,6),
        status VARCHAR(100),
        date DATETIME
    )
    ''')

    # Создание таблицы bundlesNotIncluded
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS bundlesNotIncluded (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        userid BIGINT UNSIGNED,
        username VARCHAR(32),
        token CHAR(42),
        frontrunValue DECIMAL(12,6),
        targetBlock BIGINT UNSIGNED,
        victimHash CHAR(66),
        minVictimBuy DECIMAL(9,2),
        minLiquidity DECIMAL(9,2),
        maxLiquidity DECIMAL(12,2),
        minTokenHolders BIGINT UNSIGNED,
        maxTaxBuy DECIMAL(5,2),
        maxTaxSell DECIMAL(5,2),
        minSlippage INT UNSIGNED,
        minPriceImpact INT UNSIGNED,
        bribe DECIMAL(4,2),
        minBuy DECIMAL(9,2),
        maxBuy DECIMAL(9,2),
        victimValue DECIMAL(12,6),
        victimSlippage INT UNSIGNED,
        victimPriceImpact INT UNSIGNED,
        tokenTaxBuy DECIMAL(5,2),
        tokenTaxSell DECIMAL(5,2),
        tokenHolders BIGINT UNSIGNED,
        tokenLP DECIMAL(16,1),
        minimizedValue DECIMAL(12,6),
        maximizedValue DECIMAL(12,6),
        otherMevRevenue DECIMAL(12,6),
        otherMevPnl DECIMAL(12,6),
        otherMevBuilderReward DECIMAL(12,6),
        otherMevBribe DECIMAL(4,2),
        status VARCHAR(100),
        date DATETIME
    )
    ''')

    # Сохранение изменений и закрытие соединения
    conn.commit()


    print("Таблицы успешно созданы.")

    # Функция для генерации случайной даты
    def random_date(start, end):
        return start + timedelta(
            seconds=random.randint(0, int((end - start).total_seconds())),
        )

    # Генерация случайных данных для таблицы bundlesIncluded
    for _ in range(50):
        userid = random.randint(1000000000, 9999999999)
        username = f'user{random.randint(1, 1000)}'
        token = f'0x{random.randint(10**41, 10**42-1):x}'
        frontrunValue = round(random.uniform(0.1, 1000.0), 6)
        backrunValue = round(random.uniform(0.1, 1000.0), 6)
        status = random.choice(['success', 'failed', 'pending'])
        date = random_date(datetime(2023, 1, 1), datetime(2024, 9, 1))

        cursor.execute('''
        INSERT INTO bundlesIncluded (userid, username, token, frontrunValue, backrunValue, status, date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (userid, username, token, frontrunValue, backrunValue, status, date))

    # Генерация случайных данных для таблицы bundlesNotIncluded
    for _ in range(50):
        userid = random.randint(1000000000, 9999999999)
        username = f'user{random.randint(1, 1000)}'
        token = f'0x{random.randint(10**41, 10**42-1):x}'
        frontrunValue = round(random.uniform(0.1, 1000.0), 6)
        status = random.choice(['success', 'failed', 'pending'])
        date = random_date(datetime(2023, 1, 1), datetime(2024, 9, 1))

        cursor.execute('''
        INSERT INTO bundlesNotIncluded (userid, username, token, frontrunValue, status, date)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (userid, username, token, frontrunValue, status, date))

    # Сохранение изменений и закрытие соединения
    conn.commit()
    conn.close()

    print("Таблицы успешно заполнены случайными данными.")

def create_user_settings_db():
    # Подключение к базе данных (если файла базы данных нет, он будет создан)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Создание таблицы user_settings
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_settings (
        telegram_id TEXT PRIMARY KEY,
        min_purchase REAL,
        min_liquidity REAL,
        max_liquidity REAL,
        min_token_holders INTEGER,
        max_buy_tax REAL,
        max_sell_tax REAL,
        min_slippage REAL,
        min_price_impact REAL,
        bribe REAL,
        max_purchase REAL
    )
    ''')

    # Сохранение изменений и закрытие соединения
    conn.commit()


    print("База данных и таблица успешно созданы.")

    # Пример данных для вставки
    user_settings = [
        ('123456789', 10.0, 1000.0, 5000.0, 100, 5.0, 5.0, 0.5, 1.0, 50.0, 1000.0),
        ('987654321', 20.0, 2000.0, 6000.0, 200, 4.0, 4.0, 0.4, 0.8, 40.0, 2000.0)
    ]

    # Подключение к базе данных
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Вставка данных
    cursor.executemany('''
    INSERT INTO user_settings (telegram_id, min_purchase, min_liquidity, max_liquidity, min_token_holders, 
                            max_buy_tax, max_sell_tax, min_slippage, min_price_impact, bribe, max_purchase)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', user_settings)

    # Сохранение изменений и закрытие соединения
    conn.commit()
    conn.close()

    print("Данные успешно добавлены.")


def update_user_settings(telegram_id, settings):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    UPDATE user_settings
    SET min_purchase = ?, min_liquidity = ?, max_liquidity = ?, min_token_holders = ?, max_buy_tax = ?, 
        max_sell_tax = ?, min_slippage = ?, min_price_impact = ?, bribe = ?, max_purchase = ?
    WHERE telegram_id = ?
    ''', (
        settings['min_purchase'], settings['min_liquidity'], settings['max_liquidity'], 
        settings['min_token_holders'], settings['max_buy_tax'], settings['max_sell_tax'], 
        settings['min_slippage'], settings['min_price_impact'], settings['bribe'], 
        settings['max_purchase'], telegram_id
    ))
    
    conn.commit()
    conn.close()


def get_transactions():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    query = '''
    SELECT token, frontrunValue, backrunValue, status, date
    FROM (
        SELECT token, frontrunValue, backrunValue, status, date
        FROM bundlesIncluded
        UNION ALL
        SELECT token, frontrunValue, NULL as backrunValue, status, date
        FROM bundlesNotIncluded
    )
    ORDER BY date DESC
    LIMIT 20
    '''
    
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    
    transactions = []
    for row in rows:
        transactions.append({
            "token": row[0],
            "frontrunValue": row[1],
            "backrunValue": row[2],
            "status": row[3],
            "date": row[4]
        })
    
    return transactions

def get_user_settings(telegram_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT min_purchase, min_liquidity, max_liquidity, min_token_holders, max_buy_tax, 
               max_sell_tax, min_slippage, min_price_impact, bribe, max_purchase
        FROM user_settings
        WHERE telegram_id = ?
    """, (telegram_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            "min_purchase": row[0],
            "min_liquidity": row[1],
            "max_liquidity": row[2],
            "min_token_holders": row[3],
            "max_buy_tax": row[4],
            "max_sell_tax": row[5],
            "min_slippage": row[6],
            "min_price_impact": row[7],
            "bribe": row[8],
            "max_purchase": row[9]
        }
    else:
        return None


if __name__ == '__main__':
    os.remove("database.db")
    create_user_settings_db()
    create_bundle_db()