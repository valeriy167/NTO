from flask import Flask, jsonify
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  #eto nado inache ne furichit

# Пример эндпоинта для получения данных
@app.route('/api/data')
def get_data():
    # Эмуляция данных с датчиков
    return jsonify({
        "pressure": round(random.uniform(3.0, 5.0), 2),
        "flow_rate": round(random.uniform(10, 20), 2),
        "leak_status": random.choice([True, False]),
        "pressure_history": [round(random.uniform(3.0, 5.0), 2) for _ in range(6)]  # История давления
    })

if __name__ == '__main__':
    app.run(debug=True)