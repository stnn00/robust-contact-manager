# robust-contact-manager

A robust command-line tool for managing a contact list.

Originating from the starter script `buggy_contacts.py`, intentionally designed with flaws and incomplete logic, this project demonstrates the process of refactoring, debugging, and testing to build a robust and maintainable program.

This application allows users to:
- Add new contacts while preventing duplicate entries.
- Search for existing contacts.
- Delete contacts without triggering errors.
- Navigate through a clean, user-friendly command-line interface.
- Run automated unit tests to verify functionality.

The project now features a cleaner and more resilient design, incorporating **custom exception handling**, thorough **input validation**, and a **modular structure**, all supported by an extensive **test suite** built with the `unittest` framework.


## Demonstration

Video on YouTube (--:--) for demonstration purposes of `contact_manager.py` and `test_contact_manager.py`:

- *[LINK_HERE](LINK_HERE)*


## Original Issues in `buggy_contacts.py`
The initial starter script was intentionally designed with several flaws and missing features:

| Problem | Description |
|----------|-------------|
| **Crash on invalid menu input** | Entering non-numeric values as input triggered a `ValueError`. |
| **Crash when searching for non-existent contacts** | The `find_contact` function raised a `KeyError` when no matching contact was found. |
| **Crash when deleting non-existent contacts** | The `delete_contact` function also produced a `KeyError`. |
| **No duplicate contact prevention** | Adding the same contact twice silently overwrote the previous entry. |
| **No testing or documentation** | The original starter code lacked unit tests, comments, and docstrings for maintainability. |



## Improvements Implemented
The refactored version introduces several key enhancements:

| Feature | Description |
|----------|-------------|
| **Input validation** | Implemented `try/except` blocks to gracefully handle invalid (non-numeric) menu input. |
| **Safe KeyError handling** | Wrapped `find_contact` and `delete_contact` in `try/except` blocks to prevent crashes. |
| **Duplicate contact prevention** | Created a custom `DuplicateContactError` exception to detect and block duplicate entries. |
| **Improved modularity** | Extracted menu display logic into a new function `display_menu()` for cleaner structure. |
| **.strip() input cleanup** | Applied `.strip()` to remove leading and trailing whitespace from user input. |
| **Comprehensive documentation** | Added descriptive module-level and function-level docstrings for clarity. |
| **Unit testing** | Built a `unittest` suite in `test_contact_manager.py` to verify all core features. |
