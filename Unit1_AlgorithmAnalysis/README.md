# Recursion Tree for Merge Sort

## Description

This project visualizes the recursion tree of the Merge Sort algorithm
for an array containing 8 elements.

The visualization shows how Merge Sort recursively divides the array
into smaller subarrays and then merges them back to obtain the final
sorted array.

## Problem Statement

Draw a recursion tree for Merge Sort dividing an array of 8 elements.

## Algorithm

### Merge Sort

1. If the array contains one or zero elements, return.
2. Find the middle position of the array.
3. Divide the array into two halves.
4. Recursively apply Merge Sort to the left half.
5. Recursively apply Merge Sort to the right half.
6. Merge the two sorted halves.
7. Continue until the complete array is sorted.

## Pseudocode

MERGE_SORT(A, low, high)

1. If low >= high
       return

2. mid = (low + high) / 2

3. MERGE_SORT(A, low, mid)

4. MERGE_SORT(A, mid + 1, high)

5. MERGE(A, low, mid, high)

6. Return

## Prompt Used

"Draw a recursion tree for Merge Sort dividing an array of 8 elements."

## Output

The generated visualization shows the recursive division of an
8-element array into smaller subarrays until individual elements
are obtained.

It then shows the merging process, where the sorted subarrays are
combined step by step to produce the final sorted array.

The final sorted array is:

[1, 2, 3, 4, 5, 6, 7, 8]

## Learning Outcome

- Understood the recursive nature of Merge Sort.
- Learned how a recursion tree represents recursive division.
- Understood the divide and merge phases of Merge Sort.
- Learned to visualize an algorithm using an AI-generated diagram.
- Practiced documenting a DAA project for GitHub.