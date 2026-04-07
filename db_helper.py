import pymysql

conn = pymysql.connect(
    host="ec2-107-22-5-206.compute-1.amazonaws.com",
    user="student",
    password="student123",
    database="cloud_db"
)

def run_sql_query(query, is_select=True):
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(query)

    if is_select:
        return cursor.fetchall()


    

    