
from library import Library

def main():
    lib = Library()
    print("🌟 歡迎使用 HKMU 圖書館管理系統 🌟\n")

    while True:
        print("\n=== 主選單 ===")
        print("1. 列出所有書籍")
        print("2. 借書")
        print("3. 還書")
        print("4. 退出")
        choice = input("請輸入選項 (1-4): ")

        if choice == "1":
            print("\n" + lib.list_books())
        elif choice == "2":
            member_id = input("輸入會員 ID (S001 /S002/ F001/ F002): ")
            item_id = input("輸入書籍 ID (B001 / B002 /B003 /B004): ")
            print(lib.borrow_book(member_id, item_id))
        elif choice == "3":
            member_id = input("輸入會員 ID: ")
            item_id = input("輸入書籍 ID: ")
            print(lib.return_book(member_id, item_id))
        elif choice == "4":
            print("👋 感謝使用，再見！")
            break
        else:
            print("❌ 無效輸入，請重試")

if __name__ == "__main__":
    main()
