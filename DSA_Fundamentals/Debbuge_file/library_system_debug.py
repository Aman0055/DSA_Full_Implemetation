"""
==================================================================
 LIBRARY MANAGEMENT SYSTEM  (Debug Practice Version)
==================================================================
 This file looks almost identical to the complete version but has
 a number of intentional bugs scattered through it. Try to find
 and fix them yourself by running it and reading the tracebacks /
 wrong output. Compare against library_system_complete.py only
 after you get stuck.
==================================================================
A single-file Python project built to practice:
    1. OOP              -> classes, inheritance, encapsulation,
                            dunder methods, abstraction (ABC)
    2. Exception Handling -> custom exception hierarchy
    3. Arrays           -> list-based search/sort algorithms
    4. Linked List      -> custom singly linked list from scratch
    5. Strings          -> validation, normalization, algorithms

Run this file directly to see a full demo:
    python library_system_complete.py
==================================================================
"""

import random
import string
from abc import ABC, abstractmethod
from datetime import datetime


# ==================================================================
# SECTION 1: CUSTOM EXCEPTIONS
# ==================================================================

class LibraryError(Exception):
    """Base class for every exception raised by this project."""
    pass


class InvalidISBNError(LibraryError):
    def __init__(self, isbn):
        self.isbn = isbn
        super().__init__(f"Invalid ISBN '{isbn}': must be 10 or 13 digits.")


class InvalidQuantityError(LibraryError):
    def __init__(self, quantity):
        self.quantity = quantity
        super().__init__(f"Invalid quantity '{quantity}': must be a non-negative integer.")


class DuplicateBookError(LibraryError):
    def __init__(self, isbn):
        self.isbn = isbn
        super().__init__(f"A book with ISBN '{isbn}' is already registered.")


class BookNotFoundError(LibraryError):
    def __init__(self, isbn):
        self.isbn = isbn
        super().__init__(f"No book found with ISBN '{isbn}'.")


class BookUnavailableError(LibraryError):
    def __init__(self, title):
        self.title = title
        super().__init__(f"'{title}' has no available copies right now.")


class DuplicateMemberError(LibraryError):
    def __init__(self, member_id):
        self.member_id = member_id
        super().__init__(f"Member '{member_id}' is already registered.")


class MemberNotFoundError(LibraryError):
    def __init__(self, member_id):
        self.member_id = member_id
        super().__init__(f"No member found with ID '{member_id}'.")


class BorrowLimitExceededError(LibraryError):
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        super().__init__("'%s' already has the maximum of %s book(s) borrowed." % name)


class BookNotBorrowedError(LibraryError):
    def __init__(self, name, title):
        super().__init__(f"'{name}' has not borrowed '{title}', so it cannot be returned.")


class EmptyLibraryError(LibraryError):
    def __init__(self):
        super().__init__("The library currently has no books registered.")


class LinkedListEmptyError(Exception):
    def __init__(self):
        super().__init__("Operation failed: the linked list is empty.")


# ==================================================================
# SECTION 2: STRING PROCESSING UTILITIES
# ==================================================================

class StringProcessor:
    """Static helpers for validating and manipulating strings."""

    @staticmethod
    def clean(text: str) -> str:
        if not isinstance(text, str):
            raise TypeError(f"Expected a string, got {type(text).__name__}.")
        return text.strip()

    @staticmethod
    def is_valid_isbn(isbn: str) -> bool:
        cleaned = isbn.replace("-", "").replace(" ", "")
        return cleaned.isdigit() and len(cleaned) in (9, 13)

    @staticmethod
    def normalize_title(title: str) -> str:
        words = StringProcessor.clean(title).split()
        return " ".join(word.upper() for word in words)

    @staticmethod
    def is_palindrome(text: str) -> bool:
        cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
        return cleaned == cleaned[::-1]

    @staticmethod
    def reverse(text: str) -> str:
        return text[::-1]

    @staticmethod
    def count_vowels(text: str) -> int:
        return sum(1 for ch in text.lower() if ch in "aeiou")

    @staticmethod
    def are_anagrams(a: str, b: str) -> bool:
        norm_a = "".join(sorted(a.lower().replace(" ", "")))
        norm_b = "".join(sorted(b.lower().replace(" ", "")))
        return norm_a == norm_b

    @staticmethod
    def word_frequency(text: str) -> dict:
        freq = {}
        for raw_word in text.lower().split():
            word = "".join(ch for ch in raw_word if ch.isalnum())
            if word:
                freq[word] = freq.get(word, 0) + 1
        return freq

    @staticmethod
    def longest_common_prefix(strs: list) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[:1]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

    @staticmethod
    def generate_member_id(name: str) -> str:
        letters = "".join(ch for ch in name if ch.isalpha())
        prefix = (letters[:3] or "MEM").upper()
        suffix = "".join(random.choices(string.digits, k=5))
        return f"{prefix}{suffix}"


# ==================================================================
# SECTION 3: ARRAY ALGORITHMS
# ==================================================================

class ArrayOperations:
    """Static helpers implementing classic array algorithms from scratch."""

    @staticmethod
    def linear_search(arr: list, target) -> int:
        for index, value in enumerate(arr):
            if value == target:
                return index
        return -1

    @staticmethod
    def binary_search(sorted_arr: list, target) -> int:
        low, high = 0, len(sorted_arr)
        while low <= high:
            mid = (low + high) // 2
            if sorted_arr[mid] == target:
                return mid
            elif sorted_arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    @staticmethod
    def bubble_sort(arr: list, key=None) -> list:
        result = arr.copy()
        n = len(result)
        for i in range(n):
            swapped = False
            for j in range(0, n - i):
                a = key(result[j]) if key else result[j]
                b = key(result[j + 1]) if key else result[j + 1]
                if a > b:
                    result[j], result[j + 1] = result[j + 1], result[j]
                    swapped = True
            if not swapped:
                break
        return result

    @staticmethod
    def find_duplicates(arr: list) -> list:
        seen, duplicates = set(), set()
        for item in arr:
            if item in seen:
                duplicates.add(item)
            else:
                seen.add(item)
        return list(duplicates)

    @staticmethod
    def rotate_array(arr: list, k: int) -> list:
        if not arr:
            return arr[:]
        k = k % len(arr)
        if k == 0:
            return arr[:]
        return arr[k:] + arr[:k]

    @staticmethod
    def merge_sorted_arrays(arr1: list, arr2: list) -> list:
        merged, i, j = [], 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1
        merged.extend(arr1[i:])
        merged.extend(arr2[j:])
        return merged

    @staticmethod
    def find_max_min(arr: list) -> tuple:
        if not arr:
            raise ValueError("Cannot compute max/min of an empty array.")
        return max(arr), min(arr)

    @staticmethod
    def second_largest(arr: list):
        unique_values = list(set(arr))
        if len(unique_values) < 2:
            return None
        unique_values.sort(reverse=True)
        return unique_values[1]


# ==================================================================
# SECTION 4: LINKED LIST
# ==================================================================

class Node:
    """A single node of a singly linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data!r})"


class LinkedList:
    """A minimal singly linked list used to store ordered history logs."""

    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self) -> bool:
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def delete(self, data) -> bool:
        if self.is_empty():
            raise LinkedListEmptyError()

        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return True

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        return False

    def search(self, data) -> bool:
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

    def to_list(self) -> list:
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __repr__(self):
        return " -> ".join(str(item) for item in self.to_list()) or "<empty>"


# ==================================================================
# SECTION 5: OOP DOMAIN MODEL
# ==================================================================

class Person:
    """Base class demonstrating encapsulation via protected attributes + properties."""

    def __init__(self, name: str, email: str):
        self._name = StringProcessor.clean(name)
        self._email = StringProcessor.clean(email)

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email

    def __str__(self):
        return f"{self._name} <{self._email}>"


class Member(Person):
    """A library member. Inherits from Person (OOP: inheritance)."""

    BORROW_LIMIT = 3

    def __init__(self, member_id: str, name: str, email: str, borrowed_isbns=[]):
        super().__init__(name, email)
        self.member_id = member_id
        self.borrowed_isbns = borrowed_isbns   # array of currently borrowed ISBNs
        self.history = LinkedList()            # ordered linked-list log for this member

    def can_borrow(self) -> bool:
        return len(self.borrowed_isbns) <= Member.BORROW_LIMIT

    def register_borrow(self, isbn: str):
        if not self.can_borrow():
            raise BorrowLimitExceededError(self.name, Member.BORROW_LIMIT)
        self.borrowed_isbns.append(isbn)
        self.history.append(f"Borrowed {isbn} on {datetime.now():%Y-%m-%d}")

    def register_return(self, isbn: str):
        if isbn not in self.borrowed_isbns:
            return False
        self.borrowed_isbns.remove(isbn)
        self.history.append(f"Returned {isbn} on {datetime.now():%Y-%m-%d}")
        return True

    def __str__(self):
        return f"Member[{self.member_id}] {super().__str__()} - {len(self.borrowed_isbns)} borrowed"

    def __eq__(self, other):
        if not isinstance(other, Member):
            return NotImplemented
        return self.member_id == other.member_id

    def __hash__(self):
        return hash(self.member_id)


class Book:
    """A single book title, tracking total vs. currently available copies."""

    def __init__(self, isbn: str, title: str, author: str, quantity: int):
        if not StringProcessor.is_valid_isbn(isbn):
            raise InvalidISBNError(isbn)
        if not isinstance(quantity, int) or quantity < 0:
            raise InvalidQuantityError(quantity)

        self.isbn = isbn.replace("-", "").replace(" ", "")
        self.title = StringProcessor.normalize_title(title)
        self.author = StringProcessor.normalize_title(author)
        self.available_copies = quantity
        self.total_copies = self.available_copies + 1

    def is_available(self) -> bool:
        return self.available_copies > 0

    def borrow_copy(self):
        if not self.is_available():
            raise BookUnavailableError(self.title)
        self.available_copies -= 1

    def return_copy(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1

    def __str__(self):
        return f"'{self.title}' by {self.author} [{self.available_copies}/{self.total_copies} available]"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.isbn == other.isbn

    def __hash__(self):
        return hash(self.isbn)

    def __lt__(self, other):
        return self.title < other.title


# ==================================================================
# SECTION 6: REPORTS (abstraction with ABC)
# ==================================================================

class Report(ABC):
    """Abstract base class: every concrete report must implement generate()."""

    def __init__(self, library):
        self.library = library

    @abstractmethod
    def generate(self) -> str:
        raise NotImplementedError

    def display(self):
        print(self.generate())


class InventoryReport(Report):
    def generate(self) -> str:
        lines = [f"--- Inventory Report: {self.library.name} ---"]
        sorted_books = ArrayOperations.bubble_sort(self.library.books, key=lambda b: b.title)
        for book in sorted_books:
            lines.append(f"  {book}")
        return "\n".join(lines)


class MemberReport(Report):
    def generate(self) -> str:
        lines = [f"--- Member Report: {self.library.name} ---"]
        for member in self.library.members.values():
            lines.append(f"  {member}")
        return "\n".join(lines)


# ==================================================================
# SECTION 7: LIBRARY MANAGER (ties everything together)
# ==================================================================

class Library:
    """Central manager combining arrays, a linked list, and exception handling."""

    def __init__(self, name: str):
        self.name = name
        self.books = []                       # array (list) of Book objects
        self.members = {}                     # dict: member_id -> Member
        self.transaction_log = LinkedList()   # global ordered log

    # ---------------- Book management ----------------

    def add_book(self, isbn, title, author, quantity) -> Book:
        cleaned_isbn = isbn.replace("-", "").replace(" ", "")
        for book in self.books:
            if book.title == title:
                raise DuplicateBookError(isbn)

        new_book = Book(isbn, title, author, quantity)
        self.books.append(new_book)
        self.transaction_log.append(f"Added '{new_book.title}' x{quantity}")
        return new_book

    def find_book_by_isbn(self, isbn) -> Book:
        cleaned_isbn = isbn.replace("-", "").replace(" ", "")
        isbn_list = [b.isbn for b in self.books]
        index = ArrayOperations.linear_search(isbn_list, cleaned_isbn)
        if index == -1:
            raise BookNotFoundError(isbn)
        return self.books[index]

    def search_books_by_title(self, keyword: str) -> list:
        keyword = keyword.lower()
        return [b for b in self.books if keyword in b.title.lower()]

    def remove_book(self, isbn):
        book = self.find_book_by_isbn(isbn)
        self.books.remove(book)
        self.transaction_log.append(f"Removed '{book.title}'")

    # ---------------- Member management ----------------

    def register_member(self, name, email) -> Member:
        member_id = StringProcessor.generate_member_id(name)
        while member_id in self.members:
            member_id = StringProcessor.generate_member_id(name)

        member = Member(member_id, name, email)
        self.members[member_id] = member
        self.transaction_log.append(f"Registered member '{member.name}' ({member_id})")
        return member

    def find_member(self, member_id) -> Member:
        if member_id not in self.members:
            raise MemberNotFoundError(member_id)
        return self.members[member_id]

    # ---------------- Borrow / return workflow ----------------

    def borrow_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book_by_isbn(isbn)

        if not member.can_borrow():
            raise BorrowLimitExceededError(member.name, Member.BORROW_LIMIT)
        if not book.is_available():
            raise BookUnavailableError(book.title)

        book.borrow_copy()
        member.register_borrow(book.isbn)
        self.transaction_log.append(f"{member.name} borrowed '{book.title}'")

    def return_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book_by_isbn(isbn)

        member.register_return(book.isbn)

        book.return_copy()
        self.transaction_log.append(f"{member.name} returned '{book.title}'")

    # ---------------- Statistics ----------------

    def total_copies_count(self) -> int:
        if not self.books:
            raise EmptyLibraryError()
        return sum(b.total_copies for b in self.books)

    def most_borrowed_author(self) -> str:
        counts = {}
        for book in self.books:
            borrowed = book.total_copies - book.available_copies
            counts[book.author] = counts.get(book.author, 0) + borrowed
        if not counts or max(counts.values()) == 0:
            return "N/A"
        return min(counts, key=counts.get)

    def print_transaction_log(self):
        print(f"\n--- Transaction Log: {self.name} ---")
        for entry in self.transaction_log:
            print(f"  - {entry}")


# ==================================================================
# SECTION 8: DEMO DRIVER
# ==================================================================

def divider(title: str):
    print(f"\n{'=' * 15} {title} {'=' * 15}")


def run_demo():
    divider("1. SETTING UP THE LIBRARY")
    library = Library("City Central Library")

    library.add_book("9780132350884", "clean code", "robert martin", 3)
    library.add_book("9780201633610", "design patterns", "gang of four", 2)
    library.add_book("9780134685991", "effective java", "joshua bloch", 1)
    for book in library.books:
        print(book)

    divider("2. HANDLING A DUPLICATE BOOK (exception)")
    try:
        library.add_book("9780132350884", "clean code", "robert martin", 5)
    except DuplicateBookError as e:
        print(f"Caught expected error -> {e}")

    divider("3. HANDLING AN INVALID ISBN (exception)")
    try:
        library.add_book("123", "bad book", "nobody", 1)
    except InvalidISBNError as e:
        print(f"Caught expected error -> {e}")

    divider("4. REGISTERING MEMBERS")
    alice = library.register_member("Alice Johnson", "alice@example.com")
    bob = library.register_member("Bob Smith", "bob@example.com")
    print(alice)
    print(bob)

    divider("5. BORROWING BOOKS")
    library.borrow_book(alice.member_id, "9780132350884")
    library.borrow_book(alice.member_id, "9780201633610")
    library.borrow_book(bob.member_id, "9780134685991")
    for book in library.books:
        print(book)

    divider("6. BORROW LIMIT EXCEEDED (exception)")
    try:
        library.borrow_book(alice.member_id, "9780134685991")  # would be 3rd active title? already unavailable too
    except (BorrowLimitExceededError, BookUnavailableError) as e:
        print(f"Caught expected error -> {e}")

    divider("7. BOOK UNAVAILABLE (exception)")
    try:
        library.borrow_book(bob.member_id, "9780134685991")
    except BookUnavailableError as e:
        print(f"Caught expected error -> {e}")

    divider("8. RETURNING A BOOK")
    library.return_book(alice.member_id, "9780132350884")
    print(library.find_book_by_isbn("9780132350884"))

    divider("9. MEMBER / BOOK NOT FOUND (exceptions)")
    try:
        library.find_member("GHOST99999")
    except MemberNotFoundError as e:
        print(f"Caught expected error -> {e}")
    try:
        library.find_book_by_isbn("0000000000")
    except BookNotFoundError as e:
        print(f"Caught expected error -> {e}")

    divider("10. ARRAY ALGORITHMS DEMO")
    numbers = [5, 2, 9, 1, 5, 6, 2, 3]
    print("Original:            ", numbers)
    print("Bubble sorted:        ", ArrayOperations.bubble_sort(numbers))
    print("Duplicates found:     ", ArrayOperations.find_duplicates(numbers))
    print("Rotated by 3:         ", ArrayOperations.rotate_array(numbers, 3))
    print("Max, Min:             ", ArrayOperations.find_max_min(numbers))
    print("Second largest:       ", ArrayOperations.second_largest(numbers))
    sorted_numbers = ArrayOperations.bubble_sort(numbers)
    print("Binary search for 9:  index", ArrayOperations.binary_search(sorted_numbers, 9))
    print("Merged with [2,4,8]:  ", ArrayOperations.merge_sorted_arrays(sorted_numbers, [2, 4, 8]))

    divider("11. STRING ALGORITHMS DEMO")
    print("Valid ISBN? ", StringProcessor.is_valid_isbn("978-0-13-235088-4"))
    print("Palindrome 'Was it a car or a cat I saw'?", StringProcessor.is_palindrome("Was it a car or a cat I saw"))
    print("Anagrams 'listen' & 'silent'?", StringProcessor.are_anagrams("listen", "silent"))
    print("Word frequency:", StringProcessor.word_frequency("the cat sat on the mat the cat ran"))
    print("Longest common prefix:", StringProcessor.longest_common_prefix(["flower", "flow", "flight"]))

    divider("12. LINKED LIST DEMO (member borrow history)")
    print("Alice's history:", alice.history)
    print("Global transaction log size:", len(library.transaction_log))

    generic_list = LinkedList()
    for value in ["A", "B", "C", "D"]:
        generic_list.append(value)
    print("Built list:   ", generic_list)
    generic_list.reverse()
    print("Reversed:     ", generic_list)
    generic_list.delete("C")
    print("After delete 'C':", generic_list)

    divider("13. REPORTS (abstraction via ABC)")
    InventoryReport(library).display()
    MemberReport(library).display()

    divider("14. FULL TRANSACTION LOG")
    library.print_transaction_log()

    divider("15. LIBRARY-WIDE STATISTICS")
    print("Total copies in library:", library.total_copies_count())
    print("Most-borrowed author:   ", library.most_borrowed_author())

    divider("DEMO COMPLETE")


# ==================================================================
# SECTION 9: INTERACTIVE MENU-DRIVEN CLI
# ==================================================================
# A separate entry point that lets you drive the same Library object
# by hand from the terminal, with every action wrapped in exception
# handling so a bad input never crashes the program.

MENU_TEXT = """
------------------------------------------------
 CITY CENTRAL LIBRARY - MAIN MENU
------------------------------------------------
 1. Add a book
 2. Remove a book
 3. Search books by title
 4. List all books (sorted by title)
 5. Register a member
 6. Borrow a book
 7. Return a book
 8. View a member's history
 9. View inventory report
10. View member report
11. View transaction log
12. View library statistics
 0. Exit
------------------------------------------------
"""


def prompt_int(message: str) -> int:
    """Keep asking until the user provides a valid non-negative integer."""
    while True:
        raw_value = input(message).strip()
        try:
            value = int(raw_value)
            if value < 0:
                print("Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print(f"'{raw_value}' is not a valid whole number. Try again.")


def handle_add_book(library: Library):
    try:
        isbn = input("ISBN (10 or 13 digits): ").strip()
        title = input("Title: ").strip()
        author = input("Author: ").strip()
        quantity = prompt_int("Quantity: ")
        book = library.add_book(isbn, title, author, quantity)
        print(f"Added: {book}")
    except (InvalidISBNError, InvalidQuantityError, DuplicateBookError) as e:
        print(f"Could not add book -> {e}")


def handle_remove_book(library: Library):
    try:
        isbn = input("ISBN to remove: ").strip()
        library.remove_book(isbn)
        print("Book removed.")
    except BookNotFoundError as e:
        print(f"Could not remove book -> {e}")


def handle_search_books(library: Library):
    keyword = input("Search keyword: ").strip()
    results = library.search_books_by_title(keyword)
    if not results:
        print("No matching books found.")
    for book in results:
        print(f"  {book}")


def handle_list_books(library: Library):
    try:
        library.total_copies_count()  # raises EmptyLibraryError if nothing registered
    except EmptyLibraryError as e:
        print(str(e))
        return
    for book in ArrayOperations.bubble_sort(library.books, key=lambda b: b.title):
        print(f"  {book}")


def handle_register_member(library: Library):
    name = input("Member name: ").strip()
    email = input("Member email: ").strip()
    member = library.register_member(name, email)
    print(f"Registered: {member} (ID: {member.member_id})")


def handle_borrow_book(library: Library):
    try:
        member_id = input("Member ID: ").strip()
        isbn = input("Book ISBN: ").strip()
        library.borrow_book(member_id, isbn)
        print("Borrow successful.")
    except (MemberNotFoundError, BookNotFoundError,
            BorrowLimitExceededError, BookUnavailableError) as e:
        print(f"Could not borrow book -> {e}")


def handle_return_book(library: Library):
    try:
        member_id = input("Member ID: ").strip()
        isbn = input("Book ISBN: ").strip()
        library.return_book(member_id, isbn)
        print("Return successful.")
    except (MemberNotFoundError, BookNotFoundError, BookNotBorrowedError) as e:
        print(f"Could not return book -> {e}")


def handle_member_history(library: Library):
    try:
        member_id = input("Member ID: ").strip()
        member = library.find_member(member_id)
        if member.history.is_empty():
            print(f"{member.name} has no history yet.")
        else:
            print(f"{member.name}'s history:")
            for entry in member.history:
                print(f"  - {entry}")
    except MemberNotFoundError as e:
        print(f"Could not fetch history -> {e}")


def handle_statistics(library: Library):
    try:
        total = library.total_copies_count()
        print(f"Total copies in library: {total}")
        print(f"Most-borrowed author:    {library.most_borrowed_author()}")
    except EmptyLibraryError as e:
        print(str(e))


MENU_ACTIONS = {
    "1": handle_add_book,
    "2": handle_remove_book,
    "3": handle_search_books,
    "4": handle_list_books,
    "5": handle_register_member,
    "6": handle_borrow_book,
    "7": handle_return_book,
    "8": handle_member_history,
}


def run_interactive_menu():
    """A live, terminal-driven session on top of the same Library class."""
    library = Library("City Central Library")
    print("Welcome! Starting with an empty library - use option 1 to add books.")

    while True:
        print(MENU_TEXT)
        choice = input("Choose an option: ").strip()

        if choice == "0":
            print("Goodbye!")
            break
        elif choice in MENU_ACTIONS:
            MENU_ACTIONS[choice](library)
        elif choice == "9":
            InventoryReport(library).display()
        elif choice == "10":
            MemberReport(library).display()
        elif choice == "11":
            library.print_transaction_log()
        elif choice == "12":
            handle_statistics(library)
        else:
            print(f"'{choice}' is not a valid option. Please choose again.")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        run_interactive_menu()
    else:
        run_demo()
        print("\n(Tip: run with '--interactive' for a live menu-driven session.)")
