import time, os
from threading import Thread, current_thread
from multiprocessing import Process, current_process


COUNT = 200_000_000
SLEEP = 10


def io_bound(sec):
    pid = os.getpid()
    thread_name = current_thread().name
    process_name = current_process().name

    print(f"{pid} * {process_name} * {thread_name} ---> Start sleeping...")
    time.sleep(sec)
    print(f"{pid} * {process_name} * {thread_name} ---> Finished sleeping...")


def cpu_bound(n):
    pid = os.getpid()
    thread_name = current_thread().name
    process_name = current_process().name

    print(f"{pid} * {process_name} * {thread_name} ---> Start counting...")

    while n > 0:
        n -= 1

    print(f"{pid} * {process_name} * {thread_name} ---> Finished counting...")


if __name__ == "__main__":
    start = time.time()

    # # part 1 (Time taken in seconds - 20.014339208602905)
    # io_bound(SLEEP)
    # io_bound(SLEEP)

    # # part 2 (Time taken in seconds - 10.011425971984863)
    # t1 = Thread(target=io_bound, args=(SLEEP,))
    # t2 = Thread(target=io_bound, args=(SLEEP,))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()

    # # part 3 (Time taken in seconds - 10.01815152168274)
    # p1 = Process(target=io_bound, args=(SLEEP,))
    # p2 = Process(target=io_bound, args=(SLEEP,))
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()

    # # part 4 (Time taken in seconds - 34.47121238708496)
    # cpu_bound(COUNT)
    # cpu_bound(COUNT)

    # # part 5 (Time taken in seconds - 57.05397295951843)
    # t1 = Thread(target=cpu_bound, args=(COUNT,))
    # t2 = Thread(target=cpu_bound, args=(COUNT,))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()

    # # part 6 (Time taken in seconds - 16.14995288848877)
    # p1 = Process(target=cpu_bound, args=(COUNT,))
    # p2 = Process(target=cpu_bound, args=(COUNT,))
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()

    end = time.time()
    print('Time taken in seconds -', end - start)
