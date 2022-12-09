def get_left_child(i):
    return 2 * i + 1


def get_right_child(i):
    return 2 * i + 2

#Min Heapify

def min_heapify(arr, i):
    left = get_left_child(i)
    right = get_right_child(i)
    smallest = i

    if left < len(arr) and arr[i] > arr[left]:
        smallest = left
    if right < len(arr) and arr[smallest] > arr[right]:
        smallest = right
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, smallest)
		
def build_min_heap(arr):
    for i in reversed(range(len(arr)//2)):
        min_heapify(arr, i)
		
#Max Heapify

def max_heapify(arr, i):
    left = get_left_child(i)
    right = get_right_child(i)
    largest = i

    if left < len(arr) and arr[left] > arr[largest]:
        largest = left
    if right < len(arr) and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, largest)
		
def build_max_heap(arr):
    for i in reversed(range(len(arr)//2)):
        max_heapify(arr, i)