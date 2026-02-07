from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

DB_NAME = "students.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def stats_page():
    return render_template("index.html")

@app.route("/api/students")
def stats_api():
    conn = get_db_connection()
    stats = conn.execute("SELECT COUNT(STUDENTwordStart) FROM students WHERE students.STUDENTwordStart = lecture.wordStart").fetchone()
    conn.close()

    return jsonify({
        "total_users": stats["total_users"],
        "page_views": stats["page_views"],
        "engagement_rate": stats["engagement_rate"],
        "avg_rating": stats["avg_rating"]
    })

if __name__ == "__main__":
    app.run(debug=True)

