# main.py
from app import app
from waitress import serve

if __name__ == "__main__":
    # Railway erwartet 0.0.0.0:8080
    serve(app.server, host="0.0.0.0", port=8080)