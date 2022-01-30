#!/usr/bin/python3

# threads are parts of a program that can run simultaneously
# Bits of threads exist within a process
# Sharing resources

import threading
from threading import Thread
import time

# display time
def meter(name, delay, repetitions):
    print(name, " has been launched")
    for i in range(repetitions):
        time.sleep(delay)
        print(name, " ", str(time.ctime(time.time())))
    print(name, " has ceased operations")


list = []
for i in range(3):
    list.append(
        Thread(target=meter, args=("Meter " + str(i + 1), i + 1, (i + 1) ** 2))
    )

for x in list:
    x.start()


class my_threads(threading.Thread):
    def __init__(self, name="Threads", delay=1, repetitions=3):
        threading.Thread.__init__(self)

        self.name = name
        self.delay = delay
        self.repetitions = repetitions

    def run(self):
        print(self.name, " starts operation")
        for i in range(self.repetitions):
            print(self.name, " goes to sleep on ", self.delay, " s")
            time.sleep(self.repetitions)
        print(self.name, " terminates")


print("Creating two threads")
threads1 = my_threads("Threads 1", 1, 8)
threads2 = my_threads("Threads 2", 2, 3)
threads1.start()
threads2.start()
threads1.join()
threads2.join()
print("DONE!")