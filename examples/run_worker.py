from rq import Queue, Connection
from rq import GeventWorker as Worker

if __name__ == '__main__':
    # Tell rq what Redis connection to use
    with Connection():
        q = Queue()
        Worker(q, slaves=8).work()
