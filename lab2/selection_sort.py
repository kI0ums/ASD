import random
import time


# Sort by selection with number of comparisons, moves and time
def selection_sort(array):
    n = len(array)
    comparisons = 0
    moves = 0
    start_time = time.time()

    for i in range(n - 1):
        min_index = i
        for j in range(i+1, n):
            comparisons += 1
            if array[j] < array[min_index]:
                min_index = j

        moves += 1
        array[i], array[min_index] = array[min_index], array[i]

    end_time = time.time()
    time_taken = round((end_time - start_time) * 1000, 3)

    return comparisons, moves, time_taken


# Generation of arrays with 100, 1000 and 10000 random elements
def generate_random_array():
    return ([random.randint(1, 100) for _ in range(100)],
            [random.randint(1, 100) for _ in range(1000)],
            [random.randint(1, 100) for _ in range(10000)])


# Array output
def display_array(array):
    elements_per_line = len(array) / 5
    for i, element in enumerate(array):
        print(element, end=", ")
        if (i + 1) % elements_per_line == 0:
            print()
    print()


# The main function of outputting all data
def main():
    arrays = generate_random_array()
    for i in range(3):
        print(f"Array {10**(i+2)}", "\n")
        print("Unsorted array:")
        display_array(arrays[i])

        comparisons, moves, time_taken = selection_sort(arrays[i])
        print("Sorted array:")
        display_array(arrays[i])

        print(f"Comparisons: {comparisons}")
        print(f"Moves: {moves}")
        print(f"Time taken: {time_taken}ms", "\n")
        print("-"*200)


# Calculation of average values of comparisons, moves and time for sorting
def average_stats(n):
    total_comparisons, total_moves, total_time_taken = 0, 0, 0
    num_iterations = 10
    print("Iterations:", num_iterations, "\n")
    for i in range(num_iterations):
        array = [random.randint(1, 100) for _ in range(n)]
        comparisons, moves, time_taken = selection_sort(array)
        total_comparisons += comparisons
        total_moves += moves
        total_time_taken += time_taken
    return total_comparisons/num_iterations, total_moves/num_iterations, total_time_taken/num_iterations


# Output of average values of comparisons, moves and time for arrays
def display_average_stats():
    for i in range(3):
        print(f"Array {10**(i+2)}", "\n")
        average_comparisons, average_moves, average_time_taken = average_stats(10**(i+2))
        print(f"Average comparisons: {average_comparisons}")
        print(f"Average moves: {average_moves}")
        print(f"Average time taken: {average_time_taken}ms", "\n")
        print("-"*200)

main()
display_average_stats()
