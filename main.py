import threading
from worker import Worker
from flask import Flask, request, jsonify, abort
app = Flask(__name__)

workers_array = []

def cantor_function(k1, k2):
    cantor_key = 0.5*(k1 + k2)*(k1 + k2 + k1) + k2
    return int(cantor_key)

def find_worker(worker_id):
    for worker in workers_array:
        if worker.worker_id == worker_id:
            return worker
    return None

def remove_worker(worker_id):
    worker = find_worker(worker_id)
    if worker is None:
        return None
    else:
        worker.signal = False
        workers_array.remove(worker);
        return worker

def start_worker(worker_id):
    thread = Worker(worker_id)
    thread.start()
    workers_array.append(thread)

@app.route("/create", methods=['POST'])
def create():
    content = request.json
    json_id = content["id"]
    type_id = content["type_id"]
    worker_id = cantor_function(json_id, type_id)
    if find_worker(worker_id) is None:
        start_worker(worker_id)
        return jsonify(worker_id), 201
    else:
        return jsonify("Duplicated Worker"), 409

@app.route("/remove", methods=['POST'])
def remove():
    content = request.json
    worker_id = content["worker_id"]
    worker = remove_worker(worker_id)
    if worker is None:
        return jsonify("Worker ID not found"), 422
    else:
        return jsonify(worker_id)

@app.route("/info")
def info():
    workers_ids = list(map(lambda worker: worker.worker_id, workers_array))
    return jsonify(workers_ids)

if __name__ == "__main__":
    app.run()
