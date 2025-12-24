from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

total_requests = 0

@app.route("/metrics", methods=["GET"])
def metrics():
    global total_requests
    total_requests += 1

    request_processing_latency = round(random.uniform(0.1, 1.5), 3)
    model_prediction_success_rate = round(random.uniform(80.0, 100.0), 2)

    prometheus_metrics = (
        f"# HELP request_processing_latency_seconds The latency of processing requests in seconds.\n"
        f"# TYPE request_processing_latency_seconds gauge\n"
        f"request_processing_latency_seconds {request_processing_latency}\n"
        f"# HELP model_prediction_success_rate_percentage The success rate of model predictions in percentage.\n"
        f"# TYPE model_prediction_success_rate_percentage gauge\n"
        f"model_prediction_success_rate_percentage {model_prediction_success_rate}\n"
        f"# HELP total_requests_total The total number of requests received.\n"
        f"# TYPE total_requests_total counter\n"
        f"total_requests_total {total_requests}\n"
    )

    return prometheus_metrics, 200, {"Content-Type": "text/plain; charset=utf-8"}

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to the Metrics API. Access /metrics for Prometheus metrics."})

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)

