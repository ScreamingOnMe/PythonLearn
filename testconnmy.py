import pymysql.cursors
"""
Python测试连接到云主机zabbix mysql脚本
"""
connect = pymysql.Connect(
    host='47.95.235.127',
    port=3306,
    user='zabbix',
    passwd='password',
    db='zabbix',
    charset='utf8'
)

cursor = connect.cursor()

cursor.execute("SELECT * FROM hosts")
data = cursor.fetchall()

print(data)
