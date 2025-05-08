# 📚 Library Management System

A simple Python-based library manager that allows you to register and manage books easily through a text-based interactive menu.

## ✨ Main Features

With this manager, you can:

- ✅ **Add books** to the system  
- 🔍 **Search for books** by title  
- 📕 **Register book loans**  
- 📗 **Register book returns**  
- ❌ **Delete books** (if no copies are on loan)  
- 📂 **List books by genre**  
- 📊 **View inventory summary** (total books and available copies)  

## ⚙️ Code Structure

- The program is fully written using **functions**.
- A **dictionary in memory** is used to store book information.
- Input validation prevents common errors like:
  - Invalid genres  
  - Non-numeric or invalid number of copies  
  - Duplicate titles  
  - Returning books that weren’t loaned  

## 📋 Supported Genres

- Fiction  
- Nonfiction  
- Science  
- Biography  
- Children  

> The system automatically converts genre input to lowercase to avoid input mismatches.

## 🧪 How to Run

Run the Python script in a terminal or command-line environment where user input is supported:

```bash
python library_manager.py

## 🖥️ Example Usage

```text
Library management  
1. Add book  
2. Search book  
3. Register loan  
4. Register return  
5. Delete book  
6. List by genre  
7. Show summary  
8. Exit  
Choose an option: 1  

Add one book  
Add title of book: The Alchemist  
Author of book: Paulo Coelho  
Genre (Fiction, Nonfiction, Science, Biography, Children): fiction  
Copies of book: 3  
Book 'The Alchemist' added correctly  

Library management  
Choose an option: 1  

Add one book  
Add title of book: A Brief History of Time  
Author of book: Stephen Hawking  
Genre (Fiction, Nonfiction, Science, Biography, Children): science  
Copies of book: 2  
Book 'A Brief History of Time' added correctly  

Library management  
Choose an option: 2  

Name of the title: The Alchemist  
Title: The Alchemist  
Author: Paulo Coelho  
Genre: fiction  
Copies: 3  
Copies available: 3  

Library management  
Choose an option: 3  

Name of the title: The Alchemist  
Loan registered successfully  

Library management  
Choose an option: 4  

Name of the title: The Alchemist  
Copy returned correctly  

Library management  
Choose an option: 6  

Genre (Fiction, Nonfiction, Science, Biography, Children): fiction  
Books found:  
- The Alchemist  

Library management  
Choose an option: 7  

Total books: 2  
Total available copies: 5  

Library management  
Choose an option: 5  

Name of the title to delete: A Brief History of Time  
Book deleted from system  

Library management  
Choose an option: 8  

Exiting the system...
