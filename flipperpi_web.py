# Flask web UI
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home(): return 'FlipperPi Web'
