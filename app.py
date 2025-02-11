import psutil
from flask import Flask, jsonify, render_template

app = Flask(__name__)

def get_system_stats():
    return {
        "cpu": psutil.cpu_percent(),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent
    }

@app.route("/")
def index():
    stats = get_system_stats()
    message = "High CPU or Memory Detected, scale up!!!" if stats["cpu"] > 80 or stats["memory"] > 80 else "System is Stable."
    return render_template("index.html", metrics=stats, message=message)

@app.route("/api/stats")
def api_stats():
    return jsonify(get_system_stats())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
