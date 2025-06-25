from flask import Flask, render_template, request
import os
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    print(f"Name: {name}, Email: {email}, Message: {message}")
    return f"<h2>Thank you, {name}! Your message has been received.</h2>"
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)