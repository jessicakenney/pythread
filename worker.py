import random
import logging
import threading
import time

#reference https://www.pythoncentral.io/how-to-create-a-thread-in-python/
# https://www.tutorialspoint.com/python/python_multithreading.htm 

class MyThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name, daemon=daemon)
        self.args = args
        self.kwargs = kwargs
        self.maria
        self.mongo

    def run(self):
        logging.debug('running with {0} and {1} '.format(self.args, self.kwargs))

class MyThreadStoreRaw(MyThread):
    def __init__(self, bstream):
        self.bstream = bstream

    def run(self):
        self.maria.insert_rows_into_stream(self.bstream)



    # def worker(num):
    #     """thread worker function"""
    #     pause = random.randint(1, 5) / 10
    #     logging.debug('sleeping %0.2f', pause)
    #     time.sleep(pause)
    #     logging.debug('ending')


# def worker(num):
#     """thread worker function"""
#     logging.debug('Starting')
#     time.sleep(0.2)
#     logging.debug('Exiting')
#
# def my_service(num):
#     """thread worker function"""
#     logging.debug('Starting')
#     time.sleep(0.4)
#     logging.debug('Exiting')


def main():
    logging.basicConfig(level=logging.DEBUG,
                        format='[%(levelname)s] (%(threadName)-10s) %(message)s',)

    for i in range(3):
        t = MyThread(args=(i,), kwargs={'a': 'A', 'b': 'B'})
        t.start()

    # enumerate will return list of active Thread instances
    # for t in threading.enumerate():
    #     if t is main_thread:
    #         continue
    #     logging.debug('joining %s', t.getName())
    #     t.join()


if __name__ == "__main__": main()
