from flask import Flask, render_template
from db import get_connection

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conn = get_connection()
        conn.close()
        return "Database Connected ✅"

    except Exception as e:
        return f"Connection Failed ❌ <br><br> {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)