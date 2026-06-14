from flask import Flask, render_template
from db import get_connection

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users")

        users = cursor.fetchall()

        output = "<h1>Users from MySQL</h1>"

        for user in users:
            output += f"<p>{user[0]} - {user[1]}</p>"

        cursor.close()
        conn.close()
        return output
    except Exception as e:
        return f"Connection Failed ❌ <br><br> {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)