import threading

# def bar():
#     for _ in range(5):
#         print("hello")

# my_thread = threading.Thread(target=bar, daemon=False)

# my_thread.start()

# my_thread.join()

my_lock = threading.Lock()

def bar():
    for count in range(1, 6):
        with my_lock:
            print(f"bar: {count}")

def foo():
    for count in range(1, 6):
        with my_lock:
            print(f"foo: {count}")

thread_1 = threading.Thread(target=bar)
thread_2 = threading.Thread(target=foo)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()




print("finish")