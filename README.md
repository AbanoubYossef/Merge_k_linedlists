# Merge Sorted Lists Experiment

This Python code includes two tasks related to merging sorted linked lists. The tasks are designed to analyze the performance of the merge operation in terms of the number of assignments and comparisons, and how it behaves with varying values of `k` (the number of linked lists) and `n` (the total number of elements).

## Task 1: Varying `n` for Different `k` Values

In this task, we vary the number of total elements `n` while keeping the number of linked lists `k` constant. We then measure the total operations (assignments + comparisons) required to merge the sorted linked lists.

### Code Explanation:
- The code defines a `LinkedList` class, which is used to create and manipulate sorted linked lists.
- It also defines functions for generating random sorted linked lists (`generate_random_sorted_linked_lists`) and merging these lists (`merge_sorted_lists`).
- The main part of the code (`task_1`) performs the following:
  - Varies the values of `k` (number of linked lists) and `n` (total elements) and stores the total operations for each combination.
  - Plots a chart to visualize the relationship between the total operations and the total elements for different values of `k`.

## Task 2: Varying `k` for a Fixed `n` Value

In this task, we keep the total number of elements `n` fixed at 10,000 and vary the number of linked lists `k`. The goal is to understand how the performance of the merge operation changes with an increasing number of linked lists.

### Code Explanation:
- The code extends the `task_2` function, which analyzes the performance with varying values of `k`.
- Similar to Task 1, it measures the total operations (assignments + comparisons) and plots a chart to visualize the relationship between the total operations and the number of lists for a fixed `n` value.

## Running the Code:

To run the code and execute the two tasks, you need to ensure that you have the required libraries installed, especially `matplotlib` for plotting. You can install it using the following command:

```python
pip install matplotlib
```

Once you have the necessary libraries installed, you can run the code to perform the experiments and generate the charts for Task 1 and Task 2.

**Note:** You can customize the values of `k` and `n` in the code to perform your own experiments and analyze the performance of the merge operation for different scenarios.

Have fun experimenting and analyzing the results!
