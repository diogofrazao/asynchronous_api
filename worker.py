import threading
import time

class Worker(threading.Thread):
    def __init__(self, worker_id):
        self.worker_id = worker_id
        self.signal = True
        super(Worker, self).__init__()

    def run(self):
        i = 0
        while self.signal:
            print "ID: "+str(self.worker_id)+ " Number: "+str(i)
            time.sleep(2)
            i = i + 1
