import sqlite3


def create_database():
    connection = sqlite3.connect("customers.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            phone TEXT
        )
    """)

    customers = [
        (1, "John Smith", "john@example.com", "5551001"),
        (2, "Sarah Jones", "sarah@example.com", "5551002"),
        (3, "David Brown", "david@example.com", "5551003"),
        (4, "Emma Wilson", "emma@example.com", "5551004"),
        (5, "Michael Taylor", "michael@example.com", "5551005")
    ]

    cursor.executemany(
        "INSERT OR IGNORE INTO customers VALUES (?, ?, ?, ?)",
        customers
    )

    connection.commit()
    connection.close()


def search_customer(email):
    connection = sqlite3.connect("customers.db")

    cursor = connection.cursor()

    # Intentionally inefficient query for the demo
    query = f"""
        SELECT *
        FROM customers
        WHERE email = '{email}'
    """

    cursor.execute(query)

    result = cursor.fetchall()

    connection.close()

    return result
