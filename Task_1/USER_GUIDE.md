User Guide: HKMU Library Management System
Project Title: HKMU Library Management System
Course: COMP2090SEF


How to Run:
Create a new folder named hkmulib
Place the above all the .py files into it
Execute the following command in the terminal:
Bashcd hkmulib
python main.py
You can then use the text menu to navigate.


1. Prerequisites
Python 3.8 or higher
No additional packages required (uses only standard libraries: abc, datetime, typing)
Recommended IDE: VS Code, PyCharm, or Google Colab


3. Project Structure
hkmulib/
├── models.py          # All OOP class definitions
├── library.py         # Core library logic
├── utils.py           # Helper utility functions
├── main.py            # Program entry point (text-based interface)
└── USER_GUIDE.md


4. How to Run on Local Computer
Method A: Using Terminal / Command Prompt
Download the entire hkmulib folder.
Open a terminal and navigate to the project folder:
cd path/to/hkmulib
Run the program:
python main.py
(On Windows you may use py main.py; on macOS/Linux use python3 main.py)

Method B: Using VS Code
Open the hkmulib folder in VS Code.
Right-click main.py → “Run Python File in Terminal”.


5. How to Use the System
After launching, you will see the main menu:

🌟 Welcome to HKMU Library Management System 🌟

=== Main Menu ===
1. List All Books
2. Borrow Book
3. Return Book
4. Exit

Please enter your choice (1-4):
Example Operations:
List books → Enter 1
Borrow a book → Enter 2 → Enter Member ID (S001 or F001 or S002 or F002) → Enter Book ID (B001 or B002 or B003or B004)
Return a book → Enter 3 → Enter Member ID → Enter Book ID

Default Test Accounts:
Student: S001 – Alice Chan (maximum borrow period: 14 days)
Student: S002 – Klay Lee (maximum borrow period: 14 days)
Faculty: F001 – Dr. Tony Wong (maximum borrow period: 30 days)
Faculty: F002 – Dr. Jay Ma (maximum borrow period: 30 days)
Books: B001, B002 , B003 , B004


6. Sample Test Cases
Test Case	Steps	Expected Result
TC1	Choose 1	Displays details of all the books
TC2	Choose 2 → S001 → B001	“Alice Chan successfully borrowed Street Survival Rules”
TC3	Choose 1	B001 shows “Borrowed” status
TC4	Choose 3 → S001 → B001	“Street Survival Rules has been successfully returned”
TC5	Choose 2 → F001 → B002	Dr. Tony Wong successfully borrows the book
