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


## Installation & Usage

1. **Install Python 3**.

    - Ensure [Python 3](https://www.python.org/downloads/) is installed on your system.

    
2. **Clone the Repository**

    - Open a terminal (Git bash, Terminal, etc.)
    - Clone the repository:

    ``` bash
    git clone https://github.com/stnn00/robust-contact-manager.git
    ```

    - Move into the repo directory:
    
    ``` bash
    cd robust-contact-manager
    ```

3. **Run the Main Program**

    1. Once you're inside the cloned repository directory:

        ```bash
        python contact_manager.py
        ```
    - Interactive command-line interface will appear:

    ```text
    --- Contact Manager ---
    1. Add Contact
    2. Find Contact
    3. Delete Contact
    4. Exit
    ```
    
    2. Enter a number (1-4) to choose an option.
    - When adding a contact:
        - If the name already exists, it raises a `DuplicateContactError` and prints:
            `An error occurred: Anna already exists.`
        - If the name is new, it will print:
            `[add_contact] Added Anna (612-111-1111) to contacts.`
        - If you enter an invalid input, it will catch the invalid input and prompt again.
    - Finding or deleting contacts non-existent contact prints:

        ```text
        [find_contact] Contact 'Anna' not found.
        [delete_contact] Contact 'Anna' not found.
        ```



## Running Unit Tests
    
**Run all tests in the repository folder:**

``` bash
python -m unittest test_contact_manager.py
```

**Or discover all tests in the directory:**
    
``` bash
python -m unittest discover
```

**Example of Expected Output**:
```text
[add_contact] Added Vanilla (612-890-1234) to contacts.
.[add_contact] Added Anna (612-123-4567) to contacts.
.[add_contact] Added Existing Contact (612-123-4567) to contacts.
[delete_contact] Successfully deleted Existing Contact.
.[delete_contact] Contact 'Non-existent Contact' not found.
.[add_contact] Added Anna (612-123-4567) to contacts.
[find_contact] Found 'Anna': 612-123-4567
.[find_contact] Contact 'Non-existent Contact' not found.
.
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```
- Eacch dot (`.`) represents a passed test.
- Test failures produce tracebacks indicating what went wrong.