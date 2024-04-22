import os
from flask import Flask, render_template
import pyterrier as pt

java_home = os.environ.get('JAVA_HOME')

if java_home is None:
    raise EnvironmentError("JAVA_HOME environment variable is not set")

if not pt.started():
    pt.init()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('homePage.html')

if __name__ == '__main__':
    app.run()
