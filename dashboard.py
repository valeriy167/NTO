from flask import Flask, jsonify
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  #eto nado inache ne furichit

@app.route('/api/data')
def get_data():
    # Эмуляция данных с датчиков
    return jsonify({
        "pressure": random.uniform(3.0, 5.0),
        "flow_rate": random.uniform(10, 20),
        "leak_status": random.choice([True, False])
    })

if __name__ == '__main__':
    app.run(debug=True)  # [[5]]