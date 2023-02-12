from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #dekorator wprowadzający funkcje na daną stronę
def hello_world():
    return render_template('hello.html')

@app.route('/another')
def another():
    return 'Hello on another '

if __name__ == '__main__':
    app.run(debug = True)