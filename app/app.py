import time
import pandas as pd
from flask import Flask, render_template, Response




app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=["GET", "POST"]) 
def welcome():
    """ 
    Our about us page.
    """
    spread = pd.read_csv('spread.csv')
    return render_template('base.html', tables=[spread.to_html(classes='data', header="true", index=False)])


if __name__ == '__main__':
  app.run()