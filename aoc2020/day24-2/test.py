import threading, queue


result = queue.Queue()


def task_wrapper(*args):
    result.put(target(*args))


threads = [threading.Thread(target=task_wrapper, args=args) for args in args_list]

for t in threads:
    t.start()
    while True:
        if len(threading.enumerate()) < max_num:
            break
for t in threads:
    t.join()
return result
