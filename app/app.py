import re
import pandas as pd
from flask import Flask, render_template, request, make_response, send_file, send_from_directory




app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=["GET", "POST"]) 
def welcome():
    """ 
    Our about us page.
    """
    
    return render_template('base.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)