import random
import time

def preserves_elements(slots, original):
    if len(slots) != len(original):
        return False
    
    bag = list(original)

    for x in slots:
        if x in bag:
            bag.remove(x)
        else:
            return False
    return True

def slot_machine_sort(arr):
    n = len(arr)
    lower, upper = min(arr), max(arr)

    while True:
        slots = []
        for _ in range(n):
            slots.append(random.randint(lower, upper))
            print("Current Slots: " + str(slots))
        for i in range(n-1):
            if slots[i] > slots[i+1] or preserves_elements(slots,arr) is False:
                is_sorted = False
                break
            else:
                is_sorted = True
        if is_sorted:
            arr[:] = slots  # mutate input in place with slots list
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

    print("\nOriginal arr: " + str(originalList))
    print("Slot Machine Sort: " + str(inputList))
    print(f"Time Elapsed: {elapsed:.6f}s")
    print(f"Success probability per spin: {100 / ((max(originalList)-min(originalList)+1) ** len(originalList)):.10f}%") # math might be wrong

