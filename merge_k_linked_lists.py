
import random
import matplotlib.pyplot as plt

class Node:
    # Constructor for the Node class, taking a value as a parameter.
    def __init__(self, value):
        self.value = value  # Initialize the node's value attribute.
        self.next = None  # Initialize the 'next' reference to None.

# Define a LinkedList class for creating and manipulating linked lists.
class LinkedList:
    # Constructor for the LinkedList class.
    def __init__(self):
        self.head = None  # Initialize the 'head' of the linked list to None.
        self.tail = None  # Initialize the 'tail' attribute to track the last node.

    # Method for inserting a value into the linked list in sorted order.
    def insert(self, value):
        new_node = Node(value)  # Create a new Node with the given value.

        if not self.head or value < self.head.value:
            # If the list is empty or the new value is smaller than the current head's value:
            new_node.next = self.head  # Set the new node's 'next' to the current head.
            self.head = new_node  # Update the head to the new node.
        else:
            current = self.head  # Start with the head as the current node.
            while current.next and current.next.value < value:
                # Traverse the list until you find the appropriate position to insert the new node.
                current = current.next
            new_node.next = current.next  # Set the new node's 'next' to the current node's 'next'.
            current.next = new_node  # Update the current node's 'next' to the new node.

            # Update the 'tail' if the new node is inserted at the end.
            if new_node.next is None:
                self.tail = new_node  # If the new node is now the last one, update the 'tail'.

    # Method to print the elements of the linked list.
    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")  # Print the value of the current node, separated by "->".
            current = current.next
        print("None")  # Print "None" to indicate the end of the list.

    # Method to make the linked list iterable using a for loop.
    def __iter__(self):
        current = self.head
        while current:
            yield current.value  # Yield the value of the current node.
            current = current.next

def generate_random_sorted_linked_lists(k, n):
    lists = []
    elements_per_list = [n // k] * k  # Distribute elements equally among lists
    remaining_elements = n % k

    for i in range(remaining_elements):
        elements_per_list[i] += 1

    for i in range(k):
        elements_in_current_list = elements_per_list[i]

        # Generate a sorted linked list with random values
        linked_list = LinkedList()  # Create a new linked list
        for _ in range(elements_in_current_list):
            linked_list.insert(random.randint(0, n))  # Insert random values

        lists.append(linked_list)

    return lists

class HeapNode:
    def __init__(self, linked_list_index, key):
        self.linked_list_index = linked_list_index
        self.key = key

def heapify_min(heap, length_heap, current):
    comparisons = 0  # Initialize the comparison count
    assignments = 0  # Initialize the assignment count
    smallest = current
    left = 2 * current + 1
    right = 2 * current + 2

    if left < length_heap:
        comparisons += 1  # Increment comparison count
        if heap[left].key < heap[smallest].key:
            smallest = left

    if right < length_heap:
        comparisons += 1  # Increment comparison count
        if heap[right].key < heap[smallest].key:
            smallest = right

    if smallest != current:
        heap[current], heap[smallest] = heap[smallest], heap[current]
        assignments += 3  # Increment assignment count for swap
        comp, assign = heapify_min(heap, length_heap, smallest)
        comparisons += comp
        assignments += assign

    return comparisons, assignments

def build_heap_bottom_up_min(heap):
    length_heap = len(heap)
    comparisons = 0  # Initialize the comparison count
    assignments = 0  # Initialize the assignment count

    for i in range(length_heap // 2 - 1, -1, -1):
        comp, assign = heapify_min(heap, length_heap, i)
        comparisons += comp
        assignments += assign

    return comparisons, assignments

def insert_top_down_min(heap, new_node):
    comparisons = 0  # Initialize the comparison count
    assignments = 0  # Initialize the assignment count
    heap.append(new_node)
    n = len(heap)
    i = n - 1

    while i > 0:
        comparisons += 1  # Increment comparison count
        parent = (i - 1) // 2
        if heap[i].key < heap[parent].key:
            heap[i], heap[parent] = heap[parent], heap[i]
            assignments += 3
            i = parent
        else:
            break

    return comparisons, assignments

def merge_sorted_lists(lists):
    result = LinkedList()  # Initialize the result linked list
    min_heap = []  # Initialize the min-heap

    # Initialize the min-heap with the first element from each list
    for i, linked_list in enumerate(lists):
        if linked_list.head:
            heap_node = HeapNode(i, linked_list.head.value)
            insert_top_down_min(min_heap, heap_node)

    comparisons, assignments = 0, 0

    while min_heap:
        # Get the minimum element from the min-heap
        min_heap_node = min_heap[0]
        list_index = min_heap_node.linked_list_index
        key = min_heap_node.key

        # Append the minimum element to the result linked list
        result.insert(key)

        # Move to the next node in the linked list
        lists[list_index].head = lists[list_index].head.next

        # Check if the linked list is not empty, then insert the new head into the min-heap
        if lists[list_index].head:
            new_key = lists[list_index].head.value
            insert_top_down_min(min_heap, HeapNode(list_index, new_key))

        # Remove the root of the min-heap
        min_heap[0] = min_heap[-1]
        min_heap.pop()
        comp, assigns = heapify_min(min_heap, len(min_heap), 0)
        comparisons += comp
        assignments += assigns

    return result, comparisons, assignments


def task_1():
    k_values = [5, 10, 100]  # Values of k for the first part of the experiment
    n_range = list(range(100, 10001, 400))  
    # Varying n from 100 to 10000 with an increment of 100

    # Lists to store the results for each k value
    total_operations_results = []

    for k in k_values:
        total_operations_k = []

        for n in n_range:
            lists = generate_random_sorted_linked_lists(k, n)
            result, comparisons, assignments = merge_sorted_lists(lists)

            total_operations = assignments + comparisons
            total_operations_k.append(total_operations)

        total_operations_results.append(total_operations_k)

    # Generate the chart for total operations (assignments + comparisons)
    for i, k in enumerate(k_values):
        plt.plot(n_range, total_operations_results[i], label=f'k = {k}')

    plt.xlabel('Total Elements (n)')
    plt.ylabel('Total Operations (Assignments + Comparisons)')
    plt.legend()
    plt.title('Total Operations vs. Total Elements for Different Values of k')
    plt.show()

def task_2():
 
    # Second part of the experiment (n = 10,000, varying k from 10 to 500 with an increment of 10)
    k_values = list(range(10, 501, 10))
    n = 10000

    total_operations_k = []

    for k in k_values:
        lists = generate_random_sorted_linked_lists(k, n)
        result, comparisons, assignments = merge_sorted_lists(lists)

        total_operations = assignments + comparisons
        total_operations_k.append(total_operations)

    # Generate the chart for total operations in the second part
    plt.plot(k_values, total_operations_k, label='n = 10,000')

    plt.xlabel('Number of Lists (k)')
    plt.ylabel('Total Operations (Assignments + Comparisons)')
    plt.legend()
    plt.title('Total Operations vs. Number of Lists for n = 10,000')
    plt.show()

task_1()
task_2()

