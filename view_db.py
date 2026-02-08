import sqlite3

conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

# Show tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables:")
for row in cursor.fetchall():
    print(row[0])

print("\nAttendance table contents:\n")

cursor.execute("SELECT * FROM module")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()