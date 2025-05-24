from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)  # Allow requests from GitHub pages

# MySQL connection config
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="ebook_store"
)
cursor = conn.cursor(dictionary=True)

@app.route("/upload", methods=["POST"])
def upload():
    data = request.get_json()
    title = data.get("title")
    author = data.get("author")
    url = data.get("url")

    sql = "INSERT INTO books (title, author, url) VALUES (%s, %s, %s)"
    cursor.execute(sql, (title, author, url))
    conn.commit()

    return jsonify({"message": "Book uploaded successfully"}), 201

@app.route("/books", methods=["GET"])
def books():
    cursor.execute("SELECT * FROM books ORDER BY uploaded_at DESC")
    rows = cursor.fetchall()
    return jsonify(rows)

if __name__ == "__main__":
    app.run(debug=True)
