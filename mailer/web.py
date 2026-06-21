from pathlib import Path

from flask import Flask, render_template, request, redirect, url_for
from mailer.subscribers import SubscriberManager

ROOT_DIR = Path(__file__).resolve().parents[1]
TEMPLATES_DIR = ROOT_DIR / 'templates'

manager = SubscriberManager()
app = Flask(__name__, template_folder=str(TEMPLATES_DIR))

@app.route('/')
def index():
    return render_template('welcome.html', name='Gość')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email', '')
    success = manager.add(email)
    if success:
        return redirect(url_for('index'))
    return "Nieprawidłowy lub duplikat adresu", 400

if __name__ == '__main__':
    app.run(debug=True)
