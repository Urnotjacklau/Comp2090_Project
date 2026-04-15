# 🧠 Task 2: Self-Study Data Structure & Algorithm

**Author:** [LauMingWah] [13506964]
**Topic:** Priority Queue (Max-Heap) and Heap Sort Algorithm

---

## 📌 Introduction

As part of the **COMP2090SEF Course Project (Task 2)**, this module introduces a data structure and an algorithm that are **NOT covered in the standard course curriculum**. 

To solve the real-world problem of managing book reservations and popularity rankings in our OOP-based Library Management System, I independently studied and implemented a **Max-Heap (Priority Queue)** and the **Heap Sort** algorithm from scratch in Python.

---

## 🏗️ 1. New Data Structure: Max-Heap (Priority Queue)

### The Problem
In a standard library waitlist (Queue), readers are served on a strict "First-Come, First-Served" (FIFO) basis. However, in reality, **Faculty Members** often require higher priority than **Student Members** when requesting the same popular book.

### The Solution: `PriorityWaitlist`
I implemented a **Max-Heap** to act as a Priority Queue. Instead of a linked list, I used a dynamic array (`list`) to represent a complete binary tree, calculating parent-child relationships mathematically (`2*i + 1`, `2*i + 2`).

*   **Abstract Data Type (ADT) Operations:**
    *   **`insert(node)`**: Adds a new reader to the waitlist. It appends the node to the end of the array and performs **Heapify-Up** to restore the max-heap property.
        *   *Time Complexity:* $O(\log n)$
    *   **`extract_max()`**: Removes and returns the reader with the highest priority (the root of the heap). It replaces the root with the last element and performs **Heapify-Down**.
        *   *Time Complexity:* $O(\log n)$

### Priority Rules (`WaitlistNode`)
I designed a custom `__lt__` magic method to determine priority:
1.  **Role Score:** Faculty = 100 pts, Student = 50 pts. (Higher score = Higher priority)
2.  **Time Factor:** If scores are equal, the earlier `request_time` gets priority.

---

## 🚀 2. New Algorithm: Heap Sort

### The Problem
At the end of the year, the library needs to generate a report ranking all books by their popularity (borrow count). Using basic algorithms like Bubble Sort ($O(n^2)$) is too slow for a catalog of thousands of books.

### The Solution: `heap_sort_books()`
I implemented the **Heap Sort** algorithm, which leverages the Max-Heap structure to sort items efficiently in-place.

*   **How it works:**
    1.  **Build-Heap Phase:** Convert the unsorted array of books into a valid Max-Heap in $O(n)$ time.
    2.  **Sort Phase:** Repeatedly swap the maximum element (root) with the last element of the heap, reducing the heap size by 1 each time, and call **Heapify-Down** to restore the tree.
*   **Time Complexity:** Guaranteed $O(n \log n)$ for Best, Average, and Worst cases.
*   **Space Complexity:** $O(1)$ auxiliary space (In-place sorting), making it more memory-efficient than Merge Sort.

---
