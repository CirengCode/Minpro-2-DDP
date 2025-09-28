# Minpro-2-DDP
Regina Jelita Ningsih
<br>(2509116061)
# Update Book Reading Tracker
Project ini ada versi update dari project sebelumnya (Minpro-1-DDP). Pada project ini saya menambahkan fitur login untuk 2 role, yaitu sebagai creator atau reader. Program pada project ini masih menggunakan CRUD dengan tambahan library PrettyTable untuk mempercantik tabel list buku, library Maskpass untuk menyembunyikan inputan password pada saat login, dictionary, looping, functions, dan error handling. Selanjutnya akan saya jelaskan mengenai fitur dan programnya lebih lanjut ^^
# Tampilan awal pada program
> Gambar dibawah ini merupakan tampilan awal saat program dijalankan. Pada project ini saya menambahkan opsi login sebagai creator atau sebagai reader. Kedua role tersebut memilik fitur-fitur nya tersendiri. 
<img width="1476" height="253" alt="image" src="https://github.com/user-attachments/assets/eb4d8105-3763-4ef3-a924-4fffe5433bcb" />

<br> **Header**
```
print("-" * 159)
print(" " * 159)
print(f"{"✮ ⋆ ˚｡𖦹 ⋆｡°✩ 𝐵𝑜𝑜𝑘 𝑅𝑒𝑎𝑑𝑖𝑛𝑔 𝑇𝑟𝑎𝑐𝑘𝑒𝑟 ✮ ⋆ ˚｡𖦹 ⋆｡°✩":>97}")
print(f"{"✮ by Regina Jelita Ningsih ✮":>88}")
print(" " * 159)
print("-" * 159)
```

<br> **Opsi Login**
```
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
```

<br> **Functions**
```
import maskpass

creator = {
    "username" : "atmin",
    "password" : "123"
}

reader = {
    "username" : "gina123",
    "password" : "2626"
}
```

# Role "Creator"
> Jika pengguna log in sebagai creator, pengguna dapat mengakses seluruh fitur yang ada pada program ini. Seperti, menambahkan buku, melakukan update tracker, dan menghapus buku. Untuk log in, pengguna harus memasukkan username dan password khusus untuk role "Creator". Jika pengguna berhasil log in, akan muncul pesan "Login successful!". Menu pilihan utama dan tabel yang berisi list buku akan ditampilkan. Namun jika username dan password yang di input tidak sesuai maka akan muncul pesan "Login failed!" lalu pengguna juga akan diminta untuk memasukan kembali username dan password yang sesuai.
<img width="1472" height="755" alt="image" src="https://github.com/user-attachments/assets/5baa2ad6-a633-4328-9e8a-712ecbe015e1" />

<br> **Functions**
```
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
```

> **Output jika username dan password yang di input tidak sesuai**
<img width="1473" height="501" alt="image" src="https://github.com/user-attachments/assets/5cc2b19e-a7f5-4340-84bc-ac3f8edd0c22" />

<br> **Library PrettyTable**
> Untuk mempercantik tabel yang berisi list buku saya menggunakan library PrettyTable.
```
from prettytable import PrettyTable

book_data = [
        ("All the Lovers in the Night", "Mieko Kawakami", "Slice of Life", "Unfinished", "Page 01"),
        ("Days at the Morisaki Bookshop", "Satoshi Yagisawa", "Slice of Life", "Unfinished", "Page 10"),
        ("Heaven", "Mieko Kawakami", "Slice of Life", "Unfinished", "Page 06")
        ]
```

> _Functions_
```
def book_list():
    table = PrettyTable()
    table.field_names = ["No.", "Book Title", "Author", "Genre", "Status", "Last page"]

    no = 1
    for book in book_data:  # book_data langsung dipakai
        table.add_row((no,) + book)
        no += 1

    print(table)
```

<br> **Library Maskpass**
> Untuk menyembunyikan inputan password, saya menggunakan library Maskpass.
```
import maskpass

creator = {
    "username" : "atmin",
    "password" : "123"
}

reader = {
    "username" : "gina123",
    "password" : "2626"
}
```

> _Functions_
```
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
```

<br> **1. Menu "New Book"**
> Pengguna dapat menambahkan buku baru dengan menginput judul buku, penulis, genre buku, status buku (unfinished/finished) dan halaman terakhir dari buku yang dibaca. Jika pengguna telah menginput data-data terebut, program akan langsung looping ke menu utama dengan menampilkan tabel list buku yang terbaru.
<img width="1518" height="913" alt="image" src="https://github.com/user-attachments/assets/afb92fb9-dbe0-4ec2-86e2-1e268d133ac1" />

> **Functions**
```
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
```

<br> **2. Menu "Update Tracker"**
> Pengguna dapat melakukan update status buku dan halaman buku yang terakhir di baca. Pengguna dapat menginput nomor dari buku yang ingin di update status buku dan halaman buku yang terakhir di baca. Jika nomor buku yang diinput valid, pengguna dapat form update dengan data-data (status buku dan halaman buku yang terakhir di baca) terbaru lalu, setelah selesai di update program akan langsung looping ke menu utama dengan menampilkan tabel list buku yang terbaru. Namun, jika nomor buku yang diinput tidak valid program akan menampilkan pesan "Book number not found T___T" dan akan meminta pengguna untuk kembali menginputkan nomor yang benar.
<img width="1481" height="890" alt="image" src="https://github.com/user-attachments/assets/3611a991-3a20-435a-a76b-62abc26c4339" />

> **Output jika nomor buku yang di input tidak valid**
<img width="1480" height="472" alt="image" src="https://github.com/user-attachments/assets/40913572-b4dd-4efd-af13-7dbc6d9fe584" />

> **Functions**
```
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
```

<br> **3. Menu "Delete Book"**
> Pada menu ini, pengguna dapat menghapus data buku berdasarkan nomor kolom buku yang dinput. Data buku akan berhasil dihapus jika nomor kolom buku yang diinput valid, program akan looping ke menu utama dengan menampilkan tabel list buku yang terbaru. Namun, jika nomor kolom buku yang diinput tidak valid, maka program akan menampikan pesan error "Column not found T___T" dan meminta pengguna untuk menginputkan nomor kolom buku yang benar.
<img width="1467" height="779" alt="image" src="https://github.com/user-attachments/assets/78852010-386b-4bf1-a166-5569df9203dd" />

> **Output jika nomor kolom buku yang di input tidak valid**
<img width="1483" height="472" alt="image" src="https://github.com/user-attachments/assets/a8c51e34-f5d1-4af9-9bf5-d0b7fb9a9a23" />

> **Functions**
```
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
```

<br> **4. Menu "Exit"**
> Jika pengguna ingin menghentikan program, pengguna dapat memilih opsi menu "exit". Program akan menghentikan loop utama lalu keluar dari loop dan program akan dihentikan. Jika program dihentikan, akan muncul pesan "Goodbye!"
<img width="1482" height="424" alt="image" src="https://github.com/user-attachments/assets/a4db76e4-2ed6-4bbc-8612-d3f9089afbda" />

```
                        elif menu == 0:
                            print("Goodbye!")
                            print("-" * 159)
                            run = False
                            break
```

# Role "Reader"
> Jika pengguna log in sebagai reader, fitur-fitur yang dapat di akses dan digunakan juga terbatas. Pengguna hanya dapat melihat tabel list buku dan melakukan update pada tracker. Untuk log in, pengguna harus memasukkan username dan password khusus untuk role "Reader". Jika pengguna berhasil log in, akan muncul pesan "Login successful!" dan menu pilihan utama akan ditampilkan. Namun jika username dan password yang di input tidak sesuai maka akan muncul pesan "Login failed!" lalu pengguna juga akan diminta untuk memasukan kembali username dan password yang sesuai.
<img width="1478" height="586" alt="image" src="https://github.com/user-attachments/assets/40c3fc37-7541-42eb-8dc8-dd69e4f94c35" />

> **Functions**
```
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
```

> **Output jika username dan password yang di input tidak sesuai**
<img width="1477" height="486" alt="image" src="https://github.com/user-attachments/assets/d371b1cd-a5c1-4471-b491-9611fc8fd403" />

<br> **1. Menu "Book List"**
> Pada menu ini pengguna dapat melihat tabel list buku yang ada. Setelah tabel list buku muncul, program juga akan langsung looping ke menu pilihan utama.
<img width="1478" height="480" alt="image" src="https://github.com/user-attachments/assets/826f158c-8f0a-4799-a992-6ebca59553c4" />

> **Functions**
```
def book_list():
    table = PrettyTable()
    table.field_names = ["No.", "Book Title", "Author", "Genre", "Status", "Last page"]

    no = 1
    for book in book_data:  # book_data langsung dipakai
        table.add_row((no,) + book)
        no += 1

    print(table)
```

<br> **2. Menu "Update Tracker"**
> Seperti yang telah dijelaskan sebelumnya, pengguna dapat melakukan update status buku dan halaman buku yang terakhir di baca. Pengguna dapat menginput nomor dari buku yang ingin di update status buku dan halaman buku yang terakhir di baca. Jika nomor buku yang diinput valid, pengguna dapat form update dengan data-data (status buku dan halaman buku yang terakhir di baca) terbaru lalu, setelah selesai di update program akan langsung looping ke menu utama dengan menampilkan tabel list buku yang terbaru. Namun, jika nomor buku yang diinput tidak valid program akan menampilkan pesan "Book number not found T___T" dan akan meminta pengguna untuk kembali menginputkan nomor yang benar.
<img width="1468" height="680" alt="image" src="https://github.com/user-attachments/assets/2945a8a8-01e9-4185-b9cd-53cc0dd55666" />

> **Output jika nomor buku yang di input tidak valid**
<img width="1493" height="438" alt="image" src="https://github.com/user-attachments/assets/334218a3-9a8a-448f-b988-beb93cf90f1d" />

> **Functions**
```
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
```

<br> **3. Menu "Exit"**
> Menu ini memiliki fungsi yang sama dengan menu exit yang ada pada role creator. Pengguna dapat memilih menu ini untuk menghentikan program. Program akan menghentikan loop utama lalu keluar dari loop dan program akan dihentikan. Jika program dihentikan, akan muncul pesan "Goodbye!"
<img width="1490" height="405" alt="image" src="https://github.com/user-attachments/assets/5c4f6d4c-0b39-40a9-b48c-e220040e763b" />
```
                        elif menu == 0:
                            print("Goodbye!")
                            print("-" * 159)
                            run = False
                            break
```

# Error Handling
> Setiap inputan yang ada pada program memiliki error handling yang dapat memudahkan pengguna dan pengembang untuk bisa mengetahui dan memperbaiki error yang ada karena error handling bisa menampilkan pesan khusus yang menjelaskan errornya.

<br> **1. Error Handling "ValueError"**
> Digunakan untuk inputan dengan tipe data integer. Jadi, saat pengguna menginputkan tipe data lain, pesan error berupa "Please enter the number only" akan muncul.
```
                    except ValueError:
                        print("-" * 159)
                        print("Please enter the number only")
                        print("-" * 159)
```

> **Output**
<img width="1487" height="320" alt="image" src="https://github.com/user-attachments/assets/9ae95047-2b46-4a4a-b8be-ad8345854545" />

<br> **2. Error Handling "KeyboardInterrupt"**
> Error Handling ini saya gunakan untuk semua jenis inputan. Jika pengguna melakukan kombinasi tombol CTRL+C, pesan error berupa "Please don't use Ctrl+C, okay?!" akan muncul.
```
                    except KeyboardInterrupt:
                        print("Please don't use Ctrl+C, okay?!")
                        print("-" * 159)
```

> **Output**
<img width="1487" height="390" alt="image" src="https://github.com/user-attachments/assets/0ee58160-b037-44f8-ba69-988309af19df" />

<br> **3. Error Handling "EOFError"**
> Error Handling ini juga saya gunakan untuk semua jenis inputan. Jika pengguna melakukan kombinasi tombol CTRL+Z, pesan error berupa "Please don't use Ctrl+Z, okay?!" akan muncul.
```
                    except EOFError:
                        print("-" * 159)
                        print("Please don't use Ctrl+Z, okay?!")
                        print("-" * 159)
```

> **Output**
<img width="1485" height="426" alt="image" src="https://github.com/user-attachments/assets/ff654f10-6f5e-4413-98b2-a2f8dd8038f4" />

# FLOWCHART
![MINPRO-2-REGINA drawio (1)](https://github.com/user-attachments/assets/1f4ff233-9b5e-4a0b-ac11-3604d94ee3e4)
