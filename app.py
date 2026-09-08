from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return {"student_id": "245506L", "name": "Sulashee Ayodhya", "message": "hello from inside the container"}

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
