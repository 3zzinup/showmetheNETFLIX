from flask import Flask, render_template, redirect, request, url_for
import randomforest as rf

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index_inyup.html')

@app.route('/resultpage', methods=['POST'])
def post():
    value = request.form
    rf.randomforest(value)
    return render_template('index_wooin.html')

if __name__ == '__main__':
    app.run(debug=True)