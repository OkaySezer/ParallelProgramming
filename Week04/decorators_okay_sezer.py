import time 
import tracemalloc

def performance(func):
    
    def wrapper(*args, **kwargs):
        wrapper.counter += 1

        start_time = time.perf_counter()
        tracemalloc.start()

        result = func(*args, **kwargs)

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        end_time = time.perf_counter()

        wrapper.total_time += (end_time - start_time)

        print(f"Call #{wrapper.counter}: {func.__name__} took {end_time - start_time:.6f}s, "
            f"Current memory: {current / 10**6:.6f}MB, Peak memory: {peak / 10**6:.6f}MB")
        return result
