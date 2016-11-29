import threading
import time

class Worker(threading.Thread):
    def __init__(self, worker_id):
        self.worker_id = worker_id
        self._stop = threading.Event()
        super(Worker, self).__init__()

    def stop(self):
        self._stop.set()

    def run(self):
        i = 0
        while not self._stop.isSet():
            print "ID: "+str(self.worker_id)+ " Number: "+str(i)
            time.sleep(2)
            i = i + 1
