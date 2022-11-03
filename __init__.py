from sys import flags
from flask import Flask, render_template

DEV_MODE = flags.dev_mode

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def root():
  return render_template('index.html')

@app.route('/dexter')
def dexter():
  return 'Hello Dexter'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3000, debug=DEV_MODE)
