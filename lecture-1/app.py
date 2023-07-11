from flask import Flask, redirect,url_for

app=Flask(__name__)

@app.route('/')
def home():
    return 'Hello, i am saran'
@app.route('/target')
def courses():
    return 'To learn flask framework'
@app.route('/<name>')
def name(name):
    return f'Hello {name}'

@app.route('/admin')
def admin():
    return redirect(url_for("courses"))

if __name__=='__main__':
    app.run(debug=True)