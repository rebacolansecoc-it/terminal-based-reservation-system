from prettytable import PrettyTable
import os

books = [
    {"number": 1, "name": "Harry Potter", "is_reserved": False, "student_id": None},
    {"number": 2, "name": "Juvenille Law", "is_reserved": False, "student_id": None},
    {"number": 3, "name": "Earth Life", "is_reserved": False, "student_id": None},
    {"number": 4, "name": "Biology", "is_reserved": False, "student_id": None}
]

def find_by_number(number):
    for book in books:
        if book["number"] == number:
            return book
    return None

def find_by_name(name):
    name = name.lower()
    return [book for book in books if name in book["name"].lower()]

def search_book_by_name():
    name = input("Enter book name (or part of it): ").strip()
    matches = find_by_name(name)

    if not matches:
        print("No books match your query.")
    else:
        table = PrettyTable(["Number", "Book Name", "Status"])
        for book in matches:
            status = "Reserved" if book["is_reserved"] else "Available"
            table.add_row([book["number"], book["name"], status])
        print("Matching books:")
        print(table)
        
    input("\nPress Enter to go back to menu...")

def reserve_book():
    try:
        number = int(input("Enter book number to reserve: ").strip())
        
        book = find_by_number(number)
        if not book:
        	print(f"No book with number {number} exists.")
        elif book["is_reserved"]:
        	print(f"Book '{book['name']}' is already reserved by Student {book['student_id']}.")
        else:
	        student_id = input("Enter your Student ID: ").strip()
	        book["is_reserved"] = True
	        book["student_id"] = student_id
	        print(f"Successfully reserved '{book['name']}' for Student {student_id}.")
    except ValueError:
        print("Invalid number.")
    input("\nPress Enter to go back to menu...")
        
def cancel_reservation():
    name = input("Enter book name (or part of it) you want to cancel: ").strip()
    student_id = input("Enter your Student ID: ").strip()
    matches = find_by_name(name)
    canceled = False

    table = PrettyTable(["Number", "Book Name", "Status"])
    for book in matches:
        if book["is_reserved"] and book["student_id"] == student_id:
            book["is_reserved"] = False
            book["student_id"] = None
            print(f"Canceled reservation for '{book['name']}' (Student {student_id}).")
            canceled = True
            status = "Cancelled"
        else:
            status = "Reserved" if book["is_reserved"] else "Available"
        table.add_row([book["number"], book["name"], status])

    print("Result:")
    print(table)

    if not canceled:
        print("No matching reservation found for that student ID.")
    input("\nPress Enter to go back to menu...")

def view_reservations():
    reserved = [book for book in books if book["is_reserved"]]
    if not reserved:
        print("No reservations yet.")
    else:
        table = PrettyTable(["Number", "Book Name", "Student ID"])
        for book in reserved:
            table.add_row([book["number"], book["name"], book["student_id"]])
        print("Current reservations:")
        print(table)
    input("\nPress Enter to go back to menu...")

def main():
    options = {
        "1": search_book_by_name,
        "2": reserve_book,
        "3": cancel_reservation,
        "4": view_reservations,
        "5": exit
    }

    while True:
        os.system('clear')
        print("\n--- BOOK RESERVATION SYSTEM ---")
        print("1. Search book by name")
        print("2. Reserve a book")
        print("3. Cancel reservation")
        print("4. View all reservations")
        print("5. Exit")
        choice = input("\nChoose an option: ").strip()

        action = options.get(choice)
        if action:
            action()
        else:
            print("Invalid option, try again.")
            input("\nPress Enter to go back to menu...")

if __name__ == "__main__":
    main()
