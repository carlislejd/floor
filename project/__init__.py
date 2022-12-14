import pandas as pd
from flask import Flask, render_template

from .config import prices_collection


def create_app():
    app = Flask(__name__, static_url_path='/static')

    prices_db = prices_collection()


    @app.route('/', methods=["GET", "POST"]) 
    def welcome():
        """ 
        Our about us page.
        """
        spread = pd.DataFrame(list(prices_db.find())).drop('_id', axis=1)
        return render_template('base.html', tables=[spread.to_html(classes='data', header="true", index=False)])

    return app