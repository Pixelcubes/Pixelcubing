import random
import time

def slot_machine_sort(arr):
    n = len(arr)
    target = sorted(arr)
    lower, upper = min(arr), max(arr)

    while True:
        trial = []
        for _ in range(n):
            trial.append(random.randint(lower, upper))
            print("Current Slots: " + str(trial))
        if trial == target:
            arr[:] = trial  # mutate in place so caller sees the result
            return

def generate_random_list(n, lower=0, upper=9):
    # lower & upper inclusive
    return [random.randint(lower, upper) for _ in range(n)]

# Example usage:
if __name__ == "__main__":
    inputList = generate_random_list(5) # argument = magnitude of n
    originalList = inputList.copy()
    # inputList = [] # manual input
    
    start_time = time.time()
    slot_machine_sort(inputList)
    end_time = time.time()
    elapsed = end_time - start_time

    print("Original arr: " + str(originalList))
    print("Slot Machine Sort: " + str(inputList))
    print(f"Time Elapsed: {elapsed:.6f}s")
