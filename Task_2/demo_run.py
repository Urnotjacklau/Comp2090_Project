# demo_run.py
from waitlist_system import WaitlistNode, PriorityWaitlist, heap_sort_books

print("==================================================")
print("📚 Task 2 Demo: Library Priority Waitlist System")
print("==================================================\n")

# ---------------------------------------------------------
# 1. Create Mock Classes for Testing
# (Simulating the models.py from Task 1)
# ---------------------------------------------------------
class MockMember:
    def __init__(self, name, is_faculty=False):
        # Deliberately use '_name' to match the attribute in models.py
        self._name = name
        # Dynamically assign class name for priority evaluation
        self.__class__.__name__ = "FacultyMember" if is_faculty else "StudentMember"

class MockBook:
    def __init__(self, title, borrow_count):
        self.title = title
        # Simulating a protected attribute for book popularity
        self._borrow_count = borrow_count
        
    def __repr__(self):
        return f"'{self.title}' (Borrow Count: {self._borrow_count})"

# ---------------------------------------------------------
# 2. Test Phase 1: Max-Heap (Priority Queue)
# ---------------------------------------------------------
print("--- [Demo 1] Max-Heap: Priority Queue ---")
waitlist = PriorityWaitlist()

# Simulate 3 members requesting the same book (ID: B001)
# Arrival order: Alice (Student) -> Dr. Smith (Faculty) -> Bob (Student)
print("📥 Members joining the reservation waitlist...")
waitlist.insert(WaitlistNode(MockMember("Alice (Student)"), "B001"))
waitlist.insert(WaitlistNode(MockMember("Dr. Smith (Faculty)", is_faculty=True), "B001"))
waitlist.insert(WaitlistNode(MockMember("Bob (Student)"), "B001"))

# Print the internal array state of the Heap
waitlist.print_waitlist() 

print("\n📤 Book returned. System notifies the highest priority member:")
while not waitlist.is_empty():
    served_person = waitlist.extract_max()
    print(f"✅ Notification sent to: {served_person}")

# Expected extraction order: 
# 1. Dr. Smith (Highest role score)
# 2. Alice (Same score as Bob, but earlier timestamp)
# 3. Bob (Latest timestamp)

print("\n")

# ---------------------------------------------------------
# 3. Test Phase 2: Heap Sort (Book Popularity)
# ---------------------------------------------------------
print("--- [Demo 2] Heap Sort: Sort Books by Popularity ---")

# Create an unsorted list of books
books = [
    MockBook("Python Data Structures", 5),
    MockBook("Advanced OOP in Python", 100),
    MockBook("Introduction to Algorithms", 20),
    MockBook("Learn C++ in 21 Days", 2)
]

print("📊 Before Sorting (Unordered):")
for b in books: 
    print(f"  - {b}")

# Execute the O(n log n) in-place sorting algorithm
sorted_books = heap_sort_books(books)

print("\n📈 After Sorting (Ascending by Borrow Count):")
for b in sorted_books: 
    print(f"  - {b}")

print("\n==================================================")
print("🎉 Task 2 Demonstration Completed!")
print("==================================================")

