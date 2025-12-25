import mysql.connector

def execute_query(sql):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Amma@3114",
        database="shipping_data"
    )
    cur = conn.cursor(dictionary=True)
    cur.execute(sql)
    result = cur.fetchall()
    conn.close()
    return result
