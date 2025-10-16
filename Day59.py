# Decoraters.


def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("GoodBye!")
    return mfx
@greet
def name():
    print("Hello My Name is Huzaifa Waleed")

name()


import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Time taken: {end - start:.4f} seconds")
    return wrapper

@timer
def process_data():
    print("Processing data...")
    time.sleep(2)  # simulating a slow task

process_data()




import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b

my_function(10, 20)




# args and kwargs

def func(*args):
    print(args)
    return sum(args)

res = func(2,5,4,7)
print(res)

def myfunc(**kwargs):
    print(kwargs)

myfunc(name="Huzaifa", roll_no=125, marks=90)    