%%writefile /content/hkmulib/library.py
from models import Book, Member, StudentMember, FacultyMember
from typing import Dict

class Library:
    def __init__(self):
        self._books: Dict[str, Book] = {}
        self._members: Dict[str, Member] = {}
        self.load_data()

    def load_data(self):
        self._books = {
            "B001": Book("B001", "Street Survival Rules", "Eric Chiu", "978-123456"),
            "B002": Book("B002", "Four Kittens", "Cognac Chan", "978-654321"),
            "B003": Book("B003", "Food Guide 2026", "Jack Lau", "978-135790"),
            "B004": Book("B004", "Between Two Doors", "Joker Lau", "978-246851"),
        }
        self._members = {
            "S001": StudentMember("S001", "Alice Chan"),
            "S002": StudentMember("S002", "Klay Lee"),
            "F001": FacultyMember("F001", "Dr. Tony Wong"),
            "F002": FacultyMember("F002", "Dr. Jay Ma"),
        }

    def borrow_book(self, member_id: str, item_id: str) -> str:
        member = self._members.get(member_id)
        book = self._books.get(item_id)
        if not member or not book:
            return "❌ 會員或書籍不存在"
        if book.borrow(member_id, member.get_max_borrow_days()):
            member.borrow_item(item_id)
            return f"✅ {member._name} 成功借閱 {book._title}"
        return "❌ 書籍已被借出"

    def return_book(self, member_id: str, item_id: str) -> str:
        member = self._members.get(member_id)
        book = self._books.get(item_id)
        if not member or not book:
            return "❌ 資料錯誤"
        if book.return_item():
            member.return_item(item_id)
            return f"✅ {book._title} 已成功歸還"
        return "❌ 書籍未被借出"

    def list_books(self) -> str:
        return "\n".join([book.get_details() for book in self._books.values()]) or "目前無書籍"
