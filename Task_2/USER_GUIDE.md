# 📖 Task 2: Priority Waitlist & Sorting System - User Guide

Welcome to the user guide for **Task 2**. This module demonstrates the implementation of advanced data structures (**Max-Heap** and **Heap Sort**) built entirely from scratch without using Python's built-in `heapq` or `sort()` functions.

This guide explains how to run the automated demonstration script to see the algorithms in action.

---

## 1. Prerequisites
- **Python Version:** Python 3.6 or higher.
- **Environment:** Any standard terminal, command prompt, or IDE (e.g., VS Code, PyCharm, Colab).
- **Dependencies:** None. This task relies purely on Python's standard built-in features to demonstrate algorithmic understanding.

---

## 2. How to Run the Demonstration

We have provided an automated script, `demo_run.py`, which simulates real-world library scenarios to test our data structures. 

To execute the demo, open your terminal, navigate to the Task 2 directory, and run:

```bash
python demo_run.py
```

---

## 3. Understanding the Output

Once you run the script, it will execute two distinct demonstrations sequentially:

### 🟢 Demo 1: Max-Heap (Priority Queue)
This section tests the **Priority Waitlist**. It simulates three members requesting the same popular book (ID: B001) in the following arrival order:
1. **Alice** (Student)
2. **Dr. Smith** (Faculty)
3. **Bob** (Student)

**What you will see:**
The system will print the internal array state of the Heap. When the book becomes available, the system will extract members one by one. 
*   **Expected Behavior:** The system will notify **Dr. Smith** first (highest priority score due to Faculty status), followed by **Alice** (earlier timestamp than Bob), and finally **Bob**.

### 🔵 Demo 2: Heap Sort (Book Popularity)
This section tests the **Heap Sort** algorithm. It creates an unsorted list of books, each with a different "Borrow Count".

**What you will see:**
*   **Before Sorting:** The console will display the books in their original, unordered state.
*   **After Sorting:** The console will display the books seamlessly sorted in **ascending order** based on their borrow counts.
*   **Expected Behavior:** The algorithm sorts the catalog in-place with a guaranteed time complexity of $O(n \log n)$ and space complexity of $O(1)$.

---

## 4. Integration (For Developers)

If you wish to integrate this waitlist system into the main Task 1 Library System, you can easily import the core classes from `waitlist_system.py`:

```python
from waitlist_system import PriorityWaitlist, WaitlistNode, heap_sort_books

# Initialize the waitlist
book_waitlist = PriorityWaitlist()

# Add a user to the waitlist
# node = WaitlistNode(member_object, book_id)
# book_waitlist.insert(node)
```
