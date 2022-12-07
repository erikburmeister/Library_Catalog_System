#!/usr/bin/env python
# coding: utf-8

# # Library Catalog System

# In[1]:


import csv
import pandas as panda
import string
from random import choice 


# In[2]:


# RRN setup


# In[3]:


RRN_TRACKER = 0


# In[4]:


def current_rrn(): # debug funcion
    print(RRN_TRACKER)


# In[5]:


def update_rrn_tracker():
    global RRN_TRACKER
    RRN_TRACKER += 52


# In[6]:


def get_rrn():
    global RRN_TRACKER
    try: 
        csv_file = panda.read_csv("Library_Index_File.csv")
        
        RRN_TRACKER = max(csv_file.reference_field)
        update_rrn_tracker()
        
        return RRN_TRACKER
    
    except ValueError:
        RRN_TRACKER = 0
        return RRN_TRACKER


# In[7]:


# create/read files needed for the code


# In[8]:


def create_index_file():
    with open("Library_Index_File.csv", mode="w") as csv_file:
        field_names = ["ISBN", "reference_field"]
        index_writer = csv.DictWriter(csv_file, fieldnames=field_names)
        index_writer.writeheader()


# In[9]:


def index_directory():
    csv_file =panda.read_csv(
        "Library_Index_File.csv",
        header=0,
        names=["ISBN", "Reference Number"],
        usecols=["ISBN", "Reference Number"],
    )
    print(csv_file)


# In[10]:


def read_index_file():
    try: 
        csv_file =panda.read_csv("Library_Index_File.csv")

    except FileNotFoundError:
        create_index_file()


# In[11]:


def sort_index_file():
    csv_file = panda.read_csv("Library_Index_File.csv")
    csv_file.sort_values(["ISBN"], inplace=True)
    csv_file.to_csv("Library_Index_File.csv", encoding='utf-8', index=False)


# In[12]:


def create_data_file():
    with open("Library_Data_File.txt", "w") as file:
        pass


# In[13]:


def read_data_file(): # debug funcion
    try:
        with open("Library_Data_File.txt") as file:
            
            content = file.read()
            
#             print(content) # Debug
#             print("\nContent Length: ", len(content)) # Debug
    
    except FileNotFoundError:
        create_data_file()


# In[14]:


def create_secondary_index_file():
    with open("Library_Secondary_Index_File.csv", mode="w") as csv_file:
        field_names = ["secondary_key", "primary_key"]
        index_writer = csv.DictWriter(csv_file, fieldnames=field_names)
        index_writer.writeheader()


# In[15]:


def secondary_directory():
    csv_file =panda.read_csv(
        "Library_Secondary_Index_File.csv",
        header=0,
        names=["Book Title", "ISBN"],
        usecols=["Book Title", "ISBN"],
    )
    print(csv_file)


# In[16]:


def read_secondary_index_file():
    try: 
        csv_file =panda.read_csv("Library_Secondary_Index_File.csv")

    except FileNotFoundError:
        create_secondary_index_file()


# In[17]:


def sort_secondary_index_file():
    csv_file = panda.read_csv("Library_Secondary_Index_File.csv")
    csv_file.sort_values(["secondary_key"], inplace=True)
    csv_file.to_csv("Library_Secondary_Index_File.csv", encoding='utf-8', index=False)


# In[18]:


def create_available_list_file():
    with open("Library_Available_List_File.csv", mode="w+", newline="") as csv_file:
        field_names = ["available_space"]
        index_writer = csv.DictWriter(csv_file, fieldnames=field_names)
        index_writer.writeheader()


# In[19]:


def read_available_list_file():
    try: 
        csv_file =panda.read_csv("Library_Available_List_File.csv")
#         print(csv_file) # Debug

    except FileNotFoundError:
        create_available_list_file()


# In[20]:


# backend functions


# In[21]:


def backend_setup():
    read_index_file()
    read_data_file()
    read_secondary_index_file()
    read_available_list_file()
    get_rrn()


# In[22]:


def reset_files(): # debug funcion
    create_index_file()
    create_data_file()
    create_secondary_index_file()
    create_available_list_file()


# In[23]:


def add_to_index(record: list):
    with open("Library_Index_File.csv", mode="a+", newline="") as csv_file:
        index_writer = csv.writer(csv_file)
        index_writer.writerow(record)


# In[24]:


def add_to_data(record: str):
    with open("Library_Data_File.txt", mode="a+") as file:
        file.write(record)


# In[25]:


def append_to_data(record: str, reference: int):
    with open("Library_Data_File.txt", mode="r+") as file_in:
        content = file_in.read()
        
        part_1 = content[0:reference]
        cut_part = content[reference:reference+52]
        part_2 = content[reference+52:]
        
        new_content = part_1 + record + part_2

        with open("Library_Data_File.txt", mode="w+") as file_out:
            file_out.write(new_content)


# In[26]:


def add_to_secondary_index(record: list):
    with open("Library_Secondary_Index_File.csv", mode="a+", newline="") as csv_file:
        index_writer = csv.writer(csv_file)
        index_writer.writerow(record)


# In[27]:


def add_to_available_list(record: list):
    with open("Library_Available_List_File.csv", mode="a+", newline="") as csv_file:
        index_writer = csv.writer(csv_file)
        index_writer.writerow(record)


# In[28]:


def check_isbn(new_isbn):
    csv_file =panda.read_csv("Library_Index_File.csv")
    isbn_list = list(csv_file.ISBN)

    if new_isbn not in isbn_list:
        return True
    else:
        return False


# In[29]:


def check_available_list():
    try: 
        csv_file = panda.read_csv("Library_Available_List_File.csv")
        
        open_space = min(csv_file.available_space)
        return open_space

    except ValueError:
        return None


# In[30]:


def add_to_available_list(reference_number: list):
    with open("Library_Available_List_File.csv", mode="a+", newline="") as csv_file:
        index_writer = csv.writer(csv_file)
        index_writer.writerow(reference_number)


# In[31]:


def read_available_list(used_space: int):
    
    updated_list = []
    exist_counter = 0
    
    with open("Library_Available_List_File.csv", mode="r") as csv_file_in:
        
        for row in csv.reader(csv_file_in):
            if str(used_space) != row[0]:
                updated_list.append(row)

    return updated_list


# In[32]:


def update_available_list_file(updated_list: list):
    with open("Library_Available_List_File.csv", mode="w", newline="") as csv_file_out:
        writer = csv.writer(csv_file_out)
        writer.writerows(updated_list)


# In[33]:


# program functions


# In[34]:


def make_book():
    
    alphabet = list(string.ascii_uppercase)
    random_letter = choice(alphabet)
    
    unique_status = False
    while not unique_status:
        
        isbn = input("Enter isbn: ").upper()
        isbn = isbn.zfill(6)
        isbn = isbn[:6]
        
        unique_status = check_isbn(isbn)
        
        if unique_status == False:
            print("ISBN already exists. Create a new one.\n")
    
    isbn = list(isbn)
    isbn[0] = random_letter
    isbn = "".join(isbn)

    book_name = input("Enter book name: ").title()
    book_name = book_name.ljust(22)[:22]

    author_name = input("Enter author's name: ").title()
    author_name = author_name.ljust(22)[:22]

    record = f"{isbn}|{book_name}|{author_name}"
    
    return record


# In[35]:


def add():
    index_rrn = []
    title_index = []
    record = ""
    rrn = get_rrn()
    available_space = check_available_list()
    
    print("\nINSTRUCTIONS")
    print("Type in book information. Each record can only store 50 characters.")
    print("ISBNs can hold up to 6 characters (randomly assigned letter + 5 characters)")
    print("Book Name can hold up to 22 characters.")
    print("Author Name can hold up to 22 characters.")
    print("Any part of the record past the limit of characters will be cut off.\n")
    
    record = make_book()
    
    isbn = record[0:6]
    book_name = record[7:29]
    author_name = record[30:]
    
    if available_space:
        rrn = available_space
        update_available_list_file(read_available_list(rrn))
    
    index_rrn.append(isbn)
    index_rrn.append(rrn)
    
    title_index.append(book_name)
    title_index.append(isbn)
    
    if not available_space:
        update_rrn_tracker()
    
    add_to_index(index_rrn)
    sort_index_file()
    
    add_to_secondary_index(title_index)
    sort_secondary_index_file()

    if available_space:
        append_to_data(record, rrn)
    else:
        add_to_data(record)
    
    print("\nBook Added")
    print("ISBN: " + isbn)
    print("Book Title: " + book_name)
    print("Author: " + author_name)


# In[36]:


def search_by_isbn(): 
    
    search_by_isbn = input("Search by ISBN: ").upper()
    results = []
    reference_number = 0
    end_of_record = 0
    record = ""
    
    with open("Library_Index_File.csv", mode="r", newline="") as csv_file:
        index_reader = csv.reader(csv_file)
        rows = index_reader

        for row in rows:
            if search_by_isbn == row[0]:
                results.append(row)
    
    if len(results) == 0:
        print("\nNo results found!")
        
    else:
        reference_number = int(results[0][1])
        end_of_record = (reference_number + 52)

        with open("Library_Data_File.txt") as file:
                content = file.read()
                record = content[reference_number:end_of_record]

        print("\nSearch Results:")
        print(record)
        return record


# In[37]:


def search_by_title(): 
    
    search_by_book_title = input("Search by book title: ").title()
    title_results = []
    index_results = []
    reference_number = 0
    end_of_record = 0
    record = ""
    
    with open("Library_Secondary_Index_File.csv", mode="r", newline="") as csv_file:
        index_reader = csv.reader(csv_file)
        rows = index_reader

        for row in rows:
            if search_by_book_title == row[0].strip():
                title_results.append(row)
    
    if len(title_results) == 0:
        print("\nNo results found!")
        
    else:
        with open("Library_Index_File.csv", mode="r", newline="") as csv_file:
            index_reader = csv.reader(csv_file)
            rows = index_reader

            for row in rows:
                if title_results[0][1] == row[0]:
                    index_results.append(row)
        
        reference_number = int(index_results[0][1])
        end_of_record = (reference_number + 52)

        with open("Library_Data_File.txt") as file:
                content = file.read()
                record = content[reference_number:end_of_record]

        print("\nSearch Results:")
        print(record)


# In[38]:


def update_file(updated_list_1: list, updated_list_2: list):
    
    with open("Library_Index_File.csv", mode="w", newline="") as csv_file_out:
        writer = csv.writer(csv_file_out)
        writer.writerows(updated_list_1)
        
    with open("Library_Secondary_Index_File.csv", mode="w", newline="") as csv_file_out:
        writer = csv.writer(csv_file_out)
        writer.writerows(updated_list_2)


# In[39]:


def delete():
    
    delete_isbn = input("Delete by ISBN: ").upper()
    deleted_book = ""
    updated_list_1 = []
    updated_list_2 = []
    available_list = []
    exist_counter = 0
    
    unexistent_record = check_isbn(delete_isbn)
    
    if unexistent_record:
        print("\nA book with that ISBN does not exist.")
        return
    
    with open("Library_Index_File.csv", mode="r") as csv_file_in:
        
        for row in csv.reader(csv_file_in):
            
            if delete_isbn != row[0]:
                updated_list_1.append(row)
            else:
                available_list.append(row[1])
                exist_counter += 1
                
    with open("Library_Secondary_Index_File.csv", mode="r") as csv_file_in:
        
        for row in csv.reader(csv_file_in):
            
            if delete_isbn == row[1]:
                deleted_book = row[0].strip()
                
            if delete_isbn != row[1]:
                updated_list_2.append(row)
            else:
                exist_counter += 1
            
    if exist_counter:
        print(f"\nBook with the ISBN '{delete_isbn}' has been deleted.")
        print(f"The title of the book that was deleted is '{deleted_book}'.")

    add_to_available_list(available_list)
    update_file(updated_list_1, updated_list_2)


# In[40]:


def index_directory_list():
    csv_file =panda.read_csv("Library_Index_File.csv")
    isbn_list = list(csv_file.ISBN)
    reference_list = list(csv_file.reference_field)
    
    complete_list = zip(isbn_list, reference_list)
    
    return list(complete_list)


# In[41]:


def new_index_and_secondary_list(isbn: str):
    
    deleted_book = ""
    updated_list_1 = []
    updated_list_2 = []
    exist_counter = 0
    
    with open("Library_Index_File.csv", mode="r") as csv_file_in:
        
        for row in csv.reader(csv_file_in):
            
            if isbn != row[0]:
                updated_list_1.append(row)
            else:
                exist_counter += 1
                
    with open("Library_Secondary_Index_File.csv", mode="r") as csv_file_in:
        
        for row in csv.reader(csv_file_in):
            
            if isbn == row[1]:
                deleted_book = row[0].strip()
                
            if isbn != row[1]:
                updated_list_2.append(row)
            else:
                exist_counter += 1
    
    update_file(updated_list_1, updated_list_2)


# In[42]:


def update_record():
    
    search = search_by_isbn()
    
    if search is None:
        return
    
    isbn = search[0:6]
    title = search[7:29]
    reference = 0
    
    print("\nModify Book Information")
    updated_book = make_book()
    
    new_isbn = updated_book[0:6]
    new_title = updated_book[7:29]
    new_author = updated_book[30:]
    
    print("\nNew Book Information")
    print("Updated ISBN: " + new_isbn)
    print("Updated Book Title: " + new_title)
    print("Updated Author's Name: " + new_author)
    
    directory = index_directory_list()
    
    for item in directory:
        if item[0] == isbn:
            reference = item[1]

    isbn_rrn = [new_isbn, reference]
    title_isbn = [new_title, new_isbn]
    
    new_index_and_secondary_list(isbn)
    
    add_to_index(isbn_rrn)
    sort_index_file()
    
    add_to_secondary_index(title_isbn)
    sort_secondary_index_file()
    
    append_to_data(updated_book, reference)


# In[43]:


# Full program


# In[44]:


def library_catalog_system():
    
    user_message = "\n'Add', 'Search', 'Directory', 'Edit', or 'Remove' a book from the catalog: "
    search_message = "\nSEARCH: Would you prefer to search by 'ISBN' or 'book title'? "
    directory_message = "\nDIRECTORY: Would you prefer to see the 'ISBN' or 'book title' directory? "
    
    backend_setup()
    
    print("Welcome to the Library of Students Catalog System!")
    print("What would you like to do?")
    user_response = ""
    search_response = ""
    directory_response = ""
    
    while user_response != "exit":
        
        print("\nReminder: type 'exit' when ready to quit.")
        user_response = input(user_message).lower()
        
        if user_response == "exit":
            break
        
        if user_response == "add":
            add()
        elif user_response == "search":
            
            while search_response != "back":
                
                print("\nReminder: type 'back' when ready to go back to the main menu.")
                search_response = input(search_message).lower()
                
                if search_response == "back":
                    search_response = ""
                    break
                
                if search_response == "isbn":
                    search_by_isbn()
                elif search_response == "book title" or search_response == "title":
                    search_by_title()
                else:
                    print("Invalid response, try again.\n")
                
        elif user_response == "directory":
            
            while directory_response != "back":
                
                print("\nReminder: type 'back' when ready to go back to the main menu.")
                directory_response = input(directory_message).lower()
                
                if directory_response == "back":
                    directory_response = ""
                    break
                
                if directory_response == "isbn":
                    index_directory()
                elif directory_response == "book title" or directory_response == "title":
                    secondary_directory()
                else:
                    print("Invalid response, try again.\n")
        
        elif user_response == "edit":
            print("\nTo edit a record first find it using an ISBN.")
            update_record()
            
        elif user_response == "remove":
            delete()
            
        else:
            print("Invalid response, try again.\n")
    
    print("\nThank you for using Library of Students Catalog System!")


# In[45]:


if __name__ == "__main__":
    library_catalog_system()

