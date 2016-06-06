import sqlite3

conn = sqlite3.connect('first_db.sql')
cursor = conn.cursor();

# inserts = '''
# INSERT INTO Ages (name, age) VALUES ('Rana', 27);
# INSERT INTO Ages (name, age) VALUES ('Jiao', 21);
# INSERT INTO Ages (name, age) VALUES ('Ruqayah', 31);
# INSERT INTO Ages (name, age) VALUES ('Carlynn', 30);
# '''
# 
# for insert in inserts.split(';'):
#     cursor.execute(insert + ';')

sql = 'select hex(name || age) as x from Ages order by x'
[print(row) for row in cursor.execute(sql)] 