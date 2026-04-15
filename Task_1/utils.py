%%writefile /content/hkmulib/utils.py
from datetime import datetime
def is_overdue(due_date: datetime) -> bool:
    return datetime.now() > due_date
