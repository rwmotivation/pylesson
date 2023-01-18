"""
Asymptotic complexity in terms of size of `arr` `n`:
* Time: O(n * log(n)).
* Auxiliary space: O(n).
* Total space: O(n).
"""
"""
Just unlikely merge Sort, QuickSort is a divide and conquer algorithm. It picks an element as a pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways. 

    Always pick the first element as a pivot
    Always pick the last element as a pivot
    Pick a random element as a pivot
    Pick median as a pivot

Here we will be picking the last element as a pivot. The key process in quickSort is partition(). Target of partitions is, given an array and an element ‘x’ of array as a pivot, put x at its correct position in a sorted array and put all smaller elements (smaller than x) before x, and put all greater elements (greater than x) after x. All this should be done in linear time. 

Pseudo Code: Recursive QuickSort function 
Pseudo Code: Recursive QuickSort function 

// low  --> Starting index,
// high  --> Ending index
quickSort(arr[], low, high) {

  // Till starting index is lesser than ending index
  if (low < high) {

    // pi is partitioning index,
    // arr[p] is now at right place
    pi = partition(arr, low, high);

    // Before pi
    quickSort(arr, low, pi - 1);
    // After pi
    quickSort(arr, pi + 1, high);
  }
}



"""
def qsort(arr, start, end):
    if start >= end:
        return
    # Pick a random element as pivot.
    randindex = random.randint(start, end)
    arr[randindex], arr[start] = arr[start], arr[randindex]
    pivot = arr[start]
    smaller = start
    bigger = start
    for bigger in range(start + 1, end + 1):
        if arr[bigger] <= pivot:
            smaller += 1
            arr[smaller], arr[bigger] = arr[bigger], arr[smaller]
    # Place pivot in the right spot
    arr[start], arr[smaller] = arr[smaller], arr[start]
    qsort(arr, start, smaller - 1)
    qsort(arr, smaller + 1, end)

def quick_sort(arr):
    qsort(arr, 0, len(arr) - 1)
    return arr
