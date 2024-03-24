#----------------------------
# Celine Ma 100874382
# Assignment 2- Merge Sort Algorithm
#----------------------------
import winsound

# Merge Sort Algorithm
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        print_step("Dividing array", arr)
        print_step("Left half", left_half)
        print_step("Right half", right_half)
        print()

        merge_sort(left_half)
        merge_sort(right_half)
     
        merge(arr, left_half, right_half)

def merge(arr, left_half, right_half):
    i = j = k = 0

    # Merge the two sorted halves back into the original array
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
            # Play sound effect for swap
            winsound.Beep(1000, 100)
        k += 1

    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

    print_step("Merging", arr)

# Function to print the current step
def print_step(message, arr):
    print(message, end=": ")
    print_array(arr)

# Function to print the array
def print_array(arr):
    for element in arr:
        print(element, end=" ")
    print()

def main():
    # Input array
    arr = list(map(int, input("Enter the array elements, separated by space: ").split()))

    # Print unsorted array
    print("\nUnsorted array:")
    print_array(arr)
    print()

    # Sort the array using Merge Sort
    merge_sort(arr)

    # Print sorted array
    print("\nSorted array:")
    print_array(arr)

# Execute main function
if __name__ == "__main__":
    main()
