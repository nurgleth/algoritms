def time_value(func):
    import time
    def wrapper(*args,**kwargs):
        start = time.time()
        return_value = func(*args,**kwargs)
        end = time.time()
        print(f"время выполнения функции в секундах", end-start)
        return return_value
    return wrapper