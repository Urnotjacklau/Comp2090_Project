from datetime import datetime

class WaitlistNode:
    """
    [Task 2: Self-Study Data Structure - Priority Queue / Max-Heap Node]
    This class represents a single request in the library waitlist.
    Each node encapsulates the member requesting the book, the book ID, 
    the exact request time, and a calculated priority score.
    """
    
    def __init__(self, member, book_id: str):
        """
        Initializes a new waitlist request node.
        
        Args:
            member: The member object requesting the book (e.g., StudentMember or FacultyMember).
            book_id (str): The ID of the requested book.
        """
        self.member = member
        self.book_id = book_id
        
        # Automatically record the exact timestamp when the request is created.
        self.request_time = datetime.now()
        
        # Calculate the priority score used to determine the position in the Max-Heap.
        self.priority_score = self._calculate_priority()

    def _calculate_priority(self) -> int:
        """
        [Encapsulation] Internal method to calculate the priority score of the request.
        
        Rules:
        - Faculty members have a higher base priority score (100).
        - Student members have a lower base priority score (50).
        
        Returns:
            int: The calculated priority score (100 or 50).
        """
        # Determine the class name of the member object dynamically.
        class_name = self.member.__class__.__name__
        
        # Assign a higher score if the member is a FacultyMember.
        if "Faculty" in class_name:
            return 100
        else:
            return 50

    def __lt__(self, other) -> bool:
        """
        Priority Rules for comparison:
        1. Higher priority_score means higher priority.
        2. If priority_scores are equal, earlier request_time means higher priority.
        
        Args:
            other (WaitlistNode): The other node to compare against.
            
        Returns:
            bool: True if 'self' has a lower priority than 'other', False otherwise.
        """
        # Rule 1: If priority scores are identical (e.g., both are students).
        if self.priority_score == other.priority_score:
            # A later request time (larger value) means lower priority.
            # Returning True indicates 'self' arrived later and thus is "less" prioritized than 'other'.
            return self.request_time > other.request_time
        
        # Rule 2: If priority scores are different.
        # Direct comparison: If 'self' has a lower score, it is "less" prioritized.
        return self.priority_score < other.priority_score

    def __str__(self) -> str:
        """
        [Magic Method] Returns a formatted string representation of the WaitlistNode 
        for debugging and display purposes.
        """
        # Determine role label based on the priority score for display.
        role = "Faculty" if self.priority_score == 100 else "Student"
        
        # Format the datetime object to a readable string (HH:MM:SS).
        time_str = self.request_time.strftime("%H:%M:%S")
        
        # Access the protected _name attribute of the member object (assuming it exists).
        return f"[{role} ({self.priority_score} pts)] {self.member._name} (Requested at: {time_str})"

class PriorityWaitlist:
    """
    [Task 2: Self-Study Data Structure - Max-Heap / Priority Queue]
    This class implements a Max-Heap using a dynamic array (list) to manage 
    library book waitlists. It ensures that the member with the highest priority 
    (e.g., Faculty before Student, earlier request before later request) 
    is always served first.
    """
    
    def __init__(self):
       
        self._heap = []

    # -------------------------------------------------------------------------
    # Helper Methods: Tree Navigation using Array Indices
    # In a 0-indexed array, for any node at index 'i':
    # Parent index: (i - 1) // 2
    # Left child index: 2 * i + 1
    # Right child index: 2 * i + 2
    # -------------------------------------------------------------------------
    def _parent(self, index: int) -> int:
        return (index - 1) // 2

    def _left_child(self, index: int) -> int:
        return 2 * index + 1

    def _right_child(self, index: int) -> int:
        return 2 * index + 2

    # -------------------------------------------------------------------------
    # Core Operation 1: Insert (Time Complexity: O(log n))
    # -------------------------------------------------------------------------
    def insert(self, node: WaitlistNode):
        """
        Inserts a new WaitlistNode into the Max-Heap.
        
        Algorithm:
        1. Append the new node to the end of the array (bottom level of the tree).
        2. Perform 'Heapify-Up' to restore the Max-Heap property.
        
        Args:
            node (WaitlistNode): The request node to be added to the waitlist.
        """
        self._heap.append(node)
        # Restore heap property starting from the last inserted element
        self._heapify_up(len(self._heap) - 1)

    def _heapify_up(self, index: int):
       
        # Continue swapping as long as the current node is not the root (index > 0)
        # and its priority is STRICTLY GREATER than its parent's priority.
        # Note: The comparison logic is handled by the WaitlistNode's __lt__ magic method.
        # If the parent is "less than" the child, we must swap them.
        while index > 0:
            parent_idx = self._parent(index)
            
            # If the parent is less prioritized than the current node
            if self._heap[parent_idx] < self._heap[index]:
                # Swap the parent and the current node
                self._heap[parent_idx], self._heap[index] = self._heap[index], self._heap[parent_idx]
                # Move the index pointer up to the parent's position
                index = parent_idx
            else:
                # If the parent is greater or equal, the heap property is restored.
                break

    # -------------------------------------------------------------------------
    # Core Operation 2: Extract Max (Time Complexity: O(log n))
    # -------------------------------------------------------------------------
    def extract_max(self) -> WaitlistNode:
        """
        Removes and returns the WaitlistNode with the highest priority from the heap.
        
        Algorithm:
        1. If the heap is empty, return None.
        2. If the heap has only one element, pop and return it.
        3. Save the root element (maximum priority) to return later.
        4. Move the last element of the array to the root position.
        5. Perform 'Heapify-Down' from the root to restore the Max-Heap property.
        
        Returns:
            WaitlistNode: The node with the highest priority, or None if empty.
        """
        if not self._heap:
            return None
            
        if len(self._heap) == 1:
            return self._heap.pop()

        # Step 3: Save the highest priority node (the root)
        max_node = self._heap[0]
        
        # Step 4: Replace the root with the last element in the array
        self._heap[0] = self._heap.pop()
        
        # Step 5: Restore the heap property starting from the root
        self._heapify_down(0)
        
        return max_node

    def _heapify_down(self, index: int):
        """
        [Algorithm: Heapify-Down]
        Moves a node down the tree if its priority is less than any of its children's,
        ensuring the Max-Heap property is maintained.
        """
        n = len(self._heap)
        
        while True:
            left_idx = self._left_child(index)
            right_idx = self._right_child(index)
            
            # Assume the current node is the largest
            largest_idx = index

            # Check if the left child exists and is greater than the current largest node
            if left_idx < n and self._heap[largest_idx] < self._heap[left_idx]:
                largest_idx = left_idx

            # Check if the right child exists and is greater than the current largest node
            if right_idx < n and self._heap[largest_idx] < self._heap[right_idx]:
                largest_idx = right_idx

            # If the largest node is no longer the current node, a swap is needed
            if largest_idx != index:
                # Swap the current node with the largest child
                self._heap[index], self._heap[largest_idx] = self._heap[largest_idx], self._heap[index]
                # Move the index pointer down to the child's position and repeat
                index = largest_idx
            else:
                # If the current node is larger than both children, the heap property is restored.
                break

    # -------------------------------------------------------------------------
    # Helper Method for debugging
    # -------------------------------------------------------------------------
    def is_empty(self) -> bool:
        """Returns True if the waitlist is empty, False otherwise."""
        return len(self._heap) == 0

    def print_waitlist(self):
        """
        Prints the current waitlist in array order.
        Note: The array order is not strictly sorted, but the root (index 0) 
        is guaranteed to be the maximum element.
        """
        print("=== Current Priority Waitlist ===")
        for i, node in enumerate(self._heap):
            print(f"Index {i}: {node}")
        print("=================================")

def heap_sort_books(books_list: list):
    """
    Algorithm steps:
    1. Build a Max-Heap from the unsorted array.
    2. Repeatedly swap the maximum element (root) with the last element of the heap.
    3. Reduce the heap size by 1 and heapify the new root to restore the Max-Heap property.
    
    Args:
        books_list (list): A list of Book objects to be sorted.
        
    Returns:
        list: The sorted list of books (sorted in-place).
    """
    n = len(books_list)

    # -------------------------------------------------------------------------
    # Phase 1: Build Max-Heap from the unsorted array
    # We start from the last non-leaf node (n // 2 - 1) and heapify downwards
    # all the way to the root (index 0).
    # -------------------------------------------------------------------------
    for i in range(n // 2 - 1, -1, -1):
        _heapify_for_sort(books_list, n, i)

    # -------------------------------------------------------------------------
    # Phase 2: Extract elements one by one from the heap
    # -------------------------------------------------------------------------
    for i in range(n - 1, 0, -1):
        # Swap the current root (the maximum element) with the element at the end of the heap
        books_list[i], books_list[0] = books_list[0], books_list[i]
        
        # Call heapify on the reduced heap (size 'i') to restore the Max-Heap property
        # at the root (index 0). The swapped maximum element is now safely placed at the end.
        _heapify_for_sort(books_list, i, 0)
        
    return books_list

def _heapify_for_sort(arr: list, n: int, i: int):
    """
    [Algorithm: Heapify-Down for Sorting]
    A specialized heapify-down function for the Heap Sort algorithm.
    It ensures the subtree rooted at index 'i' satisfies the Max-Heap property.
    
    Args:
        arr (list): The array representation of the heap.
        n (int): The current size of the heap (excluding already sorted elements at the end).
        i (int): The index of the root of the subtree to heapify.
    """
    largest = i             # Initialize largest as root
    left = 2 * i + 1        # left child index
    right = 2 * i + 2       # right child index

    # For demonstration, let's assume we are sorting by a hypothetical attribute '_borrow_count'.
    # In a real scenario, you can change this to sort by title, ID, or any other attribute.
    # We use getattr() defensively in case the attribute doesn't exist.
    
    # Check if the left child exists and is strictly greater than the root
    if left < n:
        left_val = getattr(arr[left], '_borrow_count', 0)
        largest_val = getattr(arr[largest], '_borrow_count', 0)
        if left_val > largest_val:
            largest = left
            
    # Check if the right child exists and is strictly greater than the current largest
    if right < n:
        right_val = getattr(arr[right], '_borrow_count', 0)
        largest_val = getattr(arr[largest], '_borrow_count', 0)
        if right_val > largest_val:
            largest = right

    # If the largest is not the root, a swap is needed to restore the heap property
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        
        # Recursively heapify the affected sub-tree
        # (This is the recursive version of heapify-down, compared to the iterative one in Step 2)
        _heapify_for_sort(arr, n, largest)
