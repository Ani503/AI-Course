"""
Merge Sort Implementation with Examples
========================================

Merge Sort is a divide-and-conquer algorithm that divides the array into halves,
recursively sorts them, and then merges the sorted halves back together.

Time Complexity: O(n log n) in all cases (best, average, worst)
Space Complexity: O(n)
Stable: Yes (maintains relative order of equal elements)
"""


def merge_sort(arr):
    """
    Main merge sort function that divides the array and initiates sorting.
    
    Args:
        arr (list): The array to be sorted
    
    Returns:
        list: The sorted array
    """
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    Merge two sorted arrays into a single sorted array.
    
    Args:
        left (list): First sorted array
        right (list): Second sorted array
    
    Returns:
        list: Merged sorted array
    """
    result = []
    left_idx = 0
    right_idx = 0
    
    # Compare elements from left and right arrays
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    
    # Add remaining elements from left array
    result.extend(left[left_idx:])
    
    # Add remaining elements from right array
    result.extend(right[right_idx:])
    
    return result


def merge_sort_custom(arr, key=None, reverse=False):
    """
    Advanced merge sort with custom comparison key and reverse option.
    
    Args:
        arr (list): The array to be sorted
        key (function): Function to extract comparison key from each element
        reverse (bool): If True, sort in descending order
    
    Returns:
        list: The sorted array
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_sorted = merge_sort_custom(arr[:mid], key, reverse)
    right_sorted = merge_sort_custom(arr[mid:], key, reverse)
    
    return merge_custom(left_sorted, right_sorted, key, reverse)


def merge_custom(left, right, key=None, reverse=False):
    """
    Merge two sorted arrays with custom comparison logic.
    
    Args:
        left (list): First sorted array
        right (list): Second sorted array
        key (function): Function to extract comparison key
        reverse (bool): If True, sort in descending order
    
    Returns:
        list: Merged sorted array
    """
    result = []
    left_idx = 0
    right_idx = 0
    
    while left_idx < len(left) and right_idx < len(right):
        left_val = left[left_idx] if key is None else key(left[left_idx])
        right_val = right[right_idx] if key is None else key(right[right_idx])
        
        # Determine comparison based on reverse flag
        if reverse:
            condition = left_val >= right_val
        else:
            condition = left_val <= right_val
        
        if condition:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    
    return result


# ============================================================================
# EXAMPLES
# ============================================================================

def print_example(title, description, code_block):
    """Helper function to print formatted examples."""
    print("\n" + "="*70)
    print(f"Example: {title}")
    print("="*70)
    print(f"Description: {description}\n")
    print(code_block)


if __name__ == "__main__":
    
    # Example 1: Basic Merge Sort with Integers
    print("\n" + "█"*70)
    print("MERGE SORT IMPLEMENTATION WITH EXAMPLES")
    print("█"*70)
    
    example_code = """
arr = [64, 34, 25, 12, 22, 11, 90]
print(f"Original array: {arr}")
sorted_arr = merge_sort(arr)
print(f"Sorted array:   {sorted_arr}")
    """
    print_example(
        "Basic Merge Sort - Integers",
        "Sort an array of integers in ascending order",
        example_code
    )
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {arr}")
    sorted_arr = merge_sort(arr)
    print(f"Sorted array:   {sorted_arr}\n")
    
    
    # Example 2: Negative Numbers
    example_code = """
arr = [-5, 10, -3, 0, 25, -10, 8]
print(f"Original array: {arr}")
sorted_arr = merge_sort(arr)
print(f"Sorted array:   {sorted_arr}")
    """
    print_example(
        "Merge Sort with Negative Numbers",
        "Sort an array containing both positive and negative integers",
        example_code
    )
    arr = [-5, 10, -3, 0, 25, -10, 8]
    print(f"Original array: {arr}")
    sorted_arr = merge_sort(arr)
    print(f"Sorted array:   {sorted_arr}\n")
    
    
    # Example 3: Floating Point Numbers
    example_code = """
arr = [3.5, 1.2, 4.8, 2.1, 0.9]
print(f"Original array: {arr}")
sorted_arr = merge_sort(arr)
print(f"Sorted array:   {sorted_arr}")
    """
    print_example(
        "Merge Sort with Floating Point Numbers",
        "Sort decimal numbers using merge sort",
        example_code
    )
    arr = [3.5, 1.2, 4.8, 2.1, 0.9]
    print(f"Original array: {arr}")
    sorted_arr = merge_sort(arr)
    print(f"Sorted array:   {sorted_arr}\n")
    
    
    # Example 4: String Sorting
    example_code = """
arr = ["banana", "apple", "cherry", "date", "elderberry"]
print(f"Original array: {arr}")
sorted_arr = merge_sort(arr)
print(f"Sorted array:   {sorted_arr}")
    """
    print_example(
        "Merge Sort with Strings",
        "Sort strings in alphabetical order",
        example_code
    )
    arr = ["banana", "apple", "cherry", "date", "elderberry"]
    print(f"Original array: {arr}")
    sorted_arr = merge_sort(arr)
    print(f"Sorted array:   {sorted_arr}\n")
    
    
    # Example 5: Already Sorted Array (Best Case)
    example_code = """
arr = [1, 2, 3, 4, 5, 6, 7]
print(f"Original array (already sorted): {arr}")
sorted_arr = merge_sort(arr)
print(f"Sorted array:                    {sorted_arr}")
    """
    print_example(
        "Best Case - Already Sorted Array",
        "Sorting an already sorted array still takes O(n log n) time",
        example_code
    )
    arr = [1, 2, 3, 4, 5, 6, 7]
    print(f"Original array (already sorted): {arr}")
    sorted_arr = merge_sort(arr)
    print(f"Sorted array:                    {sorted_arr}\n")
    
    
    # Example 6: Reverse Sorted Array (Worst Case in some algorithms)
    example_code = """
arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(f"Original array (reverse sorted): {arr}")
sorted_arr = merge_sort(arr)
print(f"Sorted array:                    {sorted_arr}")
    """
    print_example(
        "Worst Case for Other Algorithms - Reverse Sorted Array",
        "Merge sort handles reverse sorted arrays efficiently",
        example_code
    )
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(f"Original array (reverse sorted): {arr}")
    sorted_arr = merge_sort(arr)
    print(f"Sorted array:                    {sorted_arr}\n")
    
    
    # Example 7: Array with Duplicates
    example_code = """
arr = [5, 2, 8, 2, 9, 1, 5, 5]
print(f"Original array: {arr}")
sorted_arr = merge_sort(arr)
print(f"Sorted array:   {sorted_arr}")
print("Note: Merge sort is STABLE - maintains relative order of duplicates")
    """
    print_example(
        "Array with Duplicate Elements",
        "Merge sort is stable and preserves the relative order of equal elements",
        example_code
    )
    arr = [5, 2, 8, 2, 9, 1, 5, 5]
    print(f"Original array: {arr}")
    sorted_arr = merge_sort(arr)
    print(f"Sorted array:   {sorted_arr}")
    print("Note: Merge sort is STABLE - maintains relative order of duplicates\n")
    
    
    # Example 8: Single Element
    example_code = """
arr = [42]
print(f"Original array: {arr}")
sorted_arr = merge_sort(arr)
print(f"Sorted array:   {sorted_arr}")
    """
    print_example(
        "Single Element Array",
        "Edge case: array with only one element",
        example_code
    )
    arr = [42]
    print(f"Original array: {arr}")
    sorted_arr = merge_sort(arr)
    print(f"Sorted array:   {sorted_arr}\n")
    
    
    # Example 9: Empty Array
    example_code = """
arr = []
print(f"Original array: {arr}")
sorted_arr = merge_sort(arr)
print(f"Sorted array:   {sorted_arr}")
    """
    print_example(
        "Empty Array",
        "Edge case: empty array",
        example_code
    )
    arr = []
    print(f"Original array: {arr}")
    sorted_arr = merge_sort(arr)
    print(f"Sorted array:   {sorted_arr}\n")
    
    
    # Example 10: Sorting Objects by Key (Advanced)
    example_code = """
students = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 78},
    {'name': 'Diana', 'score': 95}
]
print("Original list:")
for student in students:
    print(f"  {student['name']}: {student['score']}")

sorted_students = merge_sort_custom(students, key=lambda x: x['score'], reverse=True)
print("\\nSorted by score (descending):")
for student in sorted_students:
    print(f"  {student['name']}: {student['score']}")
    """
    print_example(
        "Sorting Objects by Custom Key",
        "Sort a list of dictionaries (students) by their scores in descending order",
        example_code
    )
    students = [
        {'name': 'Alice', 'score': 85},
        {'name': 'Bob', 'score': 92},
        {'name': 'Charlie', 'score': 78},
        {'name': 'Diana', 'score': 95}
    ]
    print("Original list:")
    for student in students:
        print(f"  {student['name']}: {student['score']}")
    
    sorted_students = merge_sort_custom(students, key=lambda x: x['score'], reverse=True)
    print("\nSorted by score (descending):")
    for student in sorted_students:
        print(f"  {student['name']}: {student['score']}\n")
    
    
    # Example 11: Sorting by String Length
    example_code = """
words = ["elephant", "cat", "butterfly", "dog", "hippopotamus", "a"]
print(f"Original words: {words}")
sorted_words = merge_sort_custom(words, key=len)
print(f"Sorted by length: {sorted_words}")
    """
    print_example(
        "Sorting by String Length",
        "Sort words by their character length",
        example_code
    )
    words = ["elephant", "cat", "butterfly", "dog", "hippopotamus", "a"]
    print(f"Original words: {words}")
    sorted_words = merge_sort_custom(words, key=len)
    print(f"Sorted by length: {sorted_words}\n")
    
    
    # Example 12: Large Array Performance
    example_code = """
import time
arr = list(range(1000, 0, -1))  # Array with 1000 elements in reverse order
start_time = time.time()
sorted_arr = merge_sort(arr)
end_time = time.time()
print(f"Sorted {len(arr)} elements in {(end_time - start_time)*1000:.4f} ms")
print(f"First 10 elements: {sorted_arr[:10]}")
print(f"Last 10 elements:  {sorted_arr[-10:]}")
    """
    print_example(
        "Performance with Large Array",
        "Demonstrate merge sort's efficiency with 1000 elements",
        example_code
    )
    import time
    arr = list(range(1000, 0, -1))
    start_time = time.time()
    sorted_arr = merge_sort(arr)
    end_time = time.time()
    print(f"Sorted {len(arr)} elements in {(end_time - start_time)*1000:.4f} ms")
    print(f"First 10 elements: {sorted_arr[:10]}")
    print(f"Last 10 elements:  {sorted_arr[-10:]}\n")
    
    
    # Summary
    print("\n" + "="*70)
    print("MERGE SORT - KEY CHARACTERISTICS")
    print("="*70)
    print("""
Time Complexity:
  - Best Case:     O(n log n)
  - Average Case:  O(n log n)
  - Worst Case:    O(n log n)

Space Complexity: O(n)

Advantages:
  ✓ Guaranteed O(n log n) time complexity
  ✓ Stable sort (maintains relative order of equal elements)
  ✓ Suitable for linked lists
  ✓ Works well with external sorting
  ✓ Parallelizable

Disadvantages:
  ✗ Requires O(n) extra space (not in-place)
  ✗ Slower than QuickSort on average for small arrays
  ✗ More comparisons than other algorithms for nearly sorted data

Use Cases:
  • When guaranteed O(n log n) time is critical
  • When stability is required
  • External sorting (large datasets)
  • Sorting linked lists
  • When space is not a constraint
""")
    print("="*70)
