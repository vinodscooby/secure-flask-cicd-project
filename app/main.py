from flask import Flask, jsonify
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['DEBUG'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'change-this-in-production-12345')

@app.route('/')
def home():
    return jsonify({"message": "Secure Flask App - Project 1 Completed ✅", "owner": "vinodscooby"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "project": "IBM CI/CD Project 1"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)