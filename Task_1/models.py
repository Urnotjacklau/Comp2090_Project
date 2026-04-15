%%writefile /content/hkmulib/models.py
from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from typing import List, Optional

class AbstractItem(ABC):
    def __init__(self, item_id: str, title: str):
        self._item_id = item_id
        self._title = title
        self._is_available = True
        self._borrower_id: Optional[str] = None
        self._due_date: Optional[datetime] = None

    @abstractmethod
    def get_details(self) -> str:
        pass

    def borrow(self, member_id: str, days: int) -> bool:
        if self._is_available:
            self._is_available = False
            self._borrower_id = member_id
            self._due_date = datetime.now() + timedelta(days=days)
            return True
        return False

    def return_item(self) -> bool:
        if not self._is_available:
            self._is_available = True
            self._borrower_id = None
            self._due_date = None
            return True
        return False

class Book(AbstractItem):
    def __init__(self, item_id: str, title: str, author: str, isbn: str):
        super().__init__(item_id, title)
        self._author = author
        self._isbn = isbn

    def get_details(self) -> str:
        status = "可借" if self._is_available else f"已借出 (到期: {self._due_date.strftime('%Y-%m-%d')})"
        return f"📖 {self._title} | 作者: {self._author} | ISBN: {self._isbn} | {status}"

class Member(ABC):
    def __init__(self, member_id: str, name: str):
        self._member_id = member_id
        self._name = name
        self._borrowed_items: List[str] = []

    @abstractmethod
    def get_max_borrow_days(self) -> int:
        pass

    def borrow_item(self, item_id: str):
        self._borrowed_items.append(item_id)

    def return_item(self, item_id: str):
        if item_id in self._borrowed_items:
            self._borrowed_items.remove(item_id)

class StudentMember(Member):
    def get_max_borrow_days(self) -> int:
        return 14

class FacultyMember(Member):
    def get_max_borrow_days(self) -> int:
        return 30
