from queue import Queue

my_queue = Queue()

for val in range(20, 31):
    my_queue.put(val)

while not my_queue.empty():
    print(my_queue.get())