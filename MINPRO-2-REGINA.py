print("-" * 159)
print(" " * 159)
print(f"{"✮ ⋆ ˚｡𖦹 ⋆｡°✩ 𝐵𝑜𝑜𝑘 𝑅𝑒𝑎𝑑𝑖𝑛𝑔 𝑇𝑟𝑎𝑐𝑘𝑒𝑟 ✮ ⋆ ˚｡𖦹 ⋆｡°✩":>97}")
print(f"{"✮ by Regina Jelita Ningsih ✮":>88}")
print(" " * 159)
print("-" * 159)

from prettytable import PrettyTable

book_data = [
        ("All the Lovers in the Night", "Mieko Kawakami", "Slice of Life", "Unfinished", "Page 01"),
        ("Days at the Morisaki Bookshop", "Satoshi Yagisawa", "Slice of Life", "Unfinished", "Page 10"),
        ("Heaven", "Mieko Kawakami", "Slice of Life", "Unfinished", "Page 06")
        ]

import maskpass

creator = {
    "username" : "atmin",
    "password" : "123"
}

reader = {
    "username" : "gina123",
    "password" : "2626"
}

def book_list():
    table = PrettyTable()
    table.field_names = ["No.", "Book Title", "Author", "Genre", "Status", "Last page"]

    no = 1
    for book in book_data:
        table.add_row((no,) + book)
        no += 1

    print(table)



def new():
    while True:
        try:
            title = input("Book Title: ")
            author = input("Author: ")
            genre = input("Genre: ")
            status = input("Status (Unfinished/Finished): ")
            progress = input("Last page: ")
            print("-" * 159)
            book_data.append((title, author, genre, status, progress))
        
            print(" " * 159)
            print("The Book been successfully added ^^")
            print(" " * 159)
            print("-" * 159)
            return

        except KeyboardInterrupt:
            print("Please don't use Ctrl+C, okay?!")
            print("-" * 159)
        except EOFError:
            print("-" * 159)
            print("Please don't use Ctrl+Z, okay?!")
            print("-" * 159)

def update():
    while True:
        try:
            search_number = int(input("Book Number: "))
            print("-" * 159)
            book_index = search_number - 1

            if 0 <= book_index < len(book_data):
                print(f"{book_data[book_index][0]}")
                while True:
                    try:
                        update_status = input("Update 'Status': ")
                        update_page = input("Update 'Last page': ")

                        book_data[book_index] = (
                            book_data[book_index][0],
                            book_data[book_index][1],
                            book_data[book_index][2],
                            update_status,
                            update_page
                        )

                        print("-" * 159)
                        print(" " * 159)
                        print("The tracker has been successfully updated ^^")
                        print(" " * 159)
                        print("-" * 159)
                        return  

                    except KeyboardInterrupt:
                        print("Please don't use Ctrl+C, okay?!")
                        print("-" * 159)
                    except EOFError:
                        print("-" * 159)
                        print("Please don't use Ctrl+Z, okay?!")
                        print("-" * 159)
            else:
                print("Book number not found T___T")
                print("-" * 159)

        except ValueError:
            print("-" * 159)
            print("Please enter the number only")
            print("-" * 159)
        except KeyboardInterrupt:
            print("Please don't use Ctrl+C, okay?!")
            print("-" * 159)
        except EOFError:
            print("-" * 159)
            print("Please don't use Ctrl+Z, okay?!")
            print("-" * 159)

def delete():
    while True:
        try: 
            column = int(input("Book Column: "))
            del_book = column - 1
        
            if 0 <= del_book < len(book_data):
                book_data.pop(del_book)
                print("-" * 159)
                print(" " * 159)
                print("The book has been deleted ^^")
                print(" " * 159)
                print("-" * 159)
                return
            
            else:
                print("-" * 159)
                print("Column not found T___T")
                print("-" * 159)
    
        except ValueError:
            print("Please enter the number only")
        except KeyboardInterrupt:
            print("Please don't use Ctrl+C, okay?!")
            print("-" * 159)
        except EOFError:
            print("-" * 159)
            print("Please don't use Ctrl+Z, okay?!")
            print("-" * 159)

def login_creator():
    run = True
    while run:
        try:
            print("Please log in first ^^")
            username = input("Username: ")
            password = maskpass.askpass(prompt="Password: ", mask="*")
            
            if username == creator["username"] and creator["password"] == password:
                print("-" * 159)
                print(" " * 159)
                print("Login successful!")
                print(" " * 159)
                print("-" * 159)
            
                while True:
                    try:
                        book_list()
                        print("Main menu")
                        print("[1] New Book")
                        print("[2] Update Tracker")
                        print("[3] Delete Book")
                        print("[0] Exit")
                        print("-" * 159)
                        menu = int(input("Select the menu: "))
                        print("-" * 159)

                        if menu == 1:
                            new()

                        elif menu == 2:
                            update()

                        elif menu == 3:
                            delete()
                        
                        elif menu == 0:
                            print("Goodbye!")
                            print("-" * 159)
                            run = False
                            break

                        else:
                            print("Option not found!")
                            print("-" * 159)
                    
                    except ValueError:
                        print("-" * 159)
                        print("Please enter the number only")
                        print("-" * 159)
                    except KeyboardInterrupt:
                        print("Please don't use Ctrl+C, okay?!")
                        print("-" * 159)
                    except EOFError:
                        print("-" * 159)
                        print("Please don't use Ctrl+Z, okay?!")
                        print("-" * 159)

            else:
                print("-" * 159)
                print(" " * 159)
                print("Login failed!")
                print(" " * 159)
                print("-" * 159)

        except KeyboardInterrupt:
            print("Please don't use Ctrl+C, okay?")
            print("-" * 159)
        except EOFError:
            print("-" * 159)
            print("Please don't use Ctrl+Z, okay?!")
            print("-" * 159)

def login_reader():
    run = True
    while run:
        try:
            print("Please log in first ^^")
            username = input("Username: ")
            password = maskpass.askpass(prompt="Password: ", mask="*")
            
            if username == reader["username"] and reader["password"] == password:
                print("-" * 159)
                print(" " * 159)
                print("Login successful!")
                print(" " * 159)
                print("-" * 159)
                
                while True:
                    try:
                        print("Main menu")
                        print("[1] Book List")
                        print("[2] Update Tracker")
                        print("[0] Exit")
                        print("-" * 159)
                        menu = int(input("Select the menu: "))
                        print("-" * 159)

                        if menu == 1:
                            book_list()

                        elif menu == 2:
                            update()
                        
                        elif menu == 0:
                            print("Goodbye!")
                            print("-" * 159)
                            run = False
                            break

                        else :
                            print("Option not found!")
                            print("-" * 159)

                    except ValueError:
                        print("-" * 159)
                        print("Please enter the number only")
                        print("-" * 159)
                    except KeyboardInterrupt:
                        print("Please don't use Ctrl+C, okay?!")
                        print("-" * 159)
                    except EOFError:
                        print("-" * 159)
                        print("Please don't use Ctrl+Z, okay?!")
                        print("-" * 159)
                    

            else:
                print("-" * 159)
                print(" " * 159)
                print("Login failed!")
                print(" " * 159)
                print("-" * 159)

        except KeyboardInterrupt:
            print("Please don't use Ctrl+C, okay?!")
            print("-" * 159)
        except EOFError:
            print("-" * 159)
            print("Please don't use Ctrl+Z, okay?!")
            print("-" * 159)

while True:
    try:
        print("Log in as?")
        print("[1] Creator")
        print("[2] Reader")
        print("-" * 159)
        role = int(input(">> "))
        print("-" * 159)
        if role == 1:
            login_creator()
            break

        elif role == 2:
            login_reader()
            break

        else:
            print("Option not found!")
            print("-" * 159)
    
    except ValueError:
            print("-" * 159)
            print("Please enter the number only")
            print("-" * 159)
    except KeyboardInterrupt:
            print("Please don't use Ctrl+C, okay?!")
            print("-" * 159)
    except EOFError:
            print("-" * 159)
            print("Please don't use Ctrl+Z, okay?!")
            print("-" * 159)
