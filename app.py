from flask import Flask, request, jsonify
import pickle
import numpy as np
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from google.cloud import bigquery
import pandas as pd

prediction_requests = Counter('prediction_requests_total', 'Total number of prediction requests')

app = Flask(__name__)
model = pickle.load(open("nba_model.pkl", "rb"))
bq_client = bigquery.Client()

@app.route('/predict', methods=['POST'])
def predict():
    prediction_requests.inc()  # Increment counter on each call
    data = request.get_json()
    features = np.array([
        data['minutes_played'],
        data['FGA'],
        data['TRB'],
        data['AST'],
        data['PF'],
        data['PTS']
    ]).reshape(1, -1)
    prediction = model.predict(features)[0]
    return jsonify({"isInjuredNextGame": int(prediction)})

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.route('/players')
def show_table():
    query = """
        SELECT Player, MP, FGA, TRB, AST, PF, PTS, isInjuredNextGame 
        FROM `msds434-module4-458020.module4bucketcp.nba_players_season_metrics_labeled`
        LIMIT 20
    """
    df = client.query(query).to_dataframe()
    return render_template("table.html", table=df.to_html(classes='table table-striped', index=False))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
