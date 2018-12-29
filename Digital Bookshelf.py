#global variables
search_history = []

import re
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#removes a book from the bookshelf
def remove_book():
    book_title = input("Enter the title of the book you want to remove: ")
    results = sheet.findall(book_title)#change to row 1 only
    if bool(results):
            search_shelf(book_title,2)
            selection = int(input('To confirm removal, enter the number of the result you wish to delete: '))
            row = results[selection - 1].row
            author = sheet.cell(row, 2).value 
            sheet.delete_row(int(row))
            print('Removed %s by %s from bookshelf.' %(book_title,author))
    else:
        print('No books with the entered title were found!')

#add a book to the bookshelf
def add_book():#could change to insert_row(rowtext, rownum) so never will overwrite?
    max_rows = len(sheet.get_all_values()) #may be better to fill empty as missing row would be a wipe of the next cells
    #max_cols = len(sheet.get_all_values()[0])# has no functionality atm 

    print("You will be asked to enter the book's title and author.")
    book_title = input("Enter the book's title: ")
    sheet.update_cell(max_rows + 1, 1, book_title)

    book_author = input("Enter the book's author: ")
    sheet.update_cell(max_rows + 1, 2, book_author)

    print('Book has been added to the bookshelf!')

#search books by title or author
def search():#make it accept 'close' queries in both title and auth
    print('1:search_by_title 2:search_by_author 3:return')
    choice = input('Enter your choice: ')
    if choice == '1':
        book_info = input("Enter the book's title: ")
        column = 2
        search_shelf(book_info, column)
    elif choice == '2':#change to row 2 only 
        book_info = input("Enter the book's author: ")
        column = 1
        search_shelf(book_info, column)
    elif choice == '3':
        pass
    else:
        print('Must choose 1-3. Please choose again.')

#search spreadsheet for entered value matches
def search_shelf(book_info, column):
    search_history.append(book_info) 
    results = sheet.findall(book_info)#change to row 1 only
    if bool(results):
        result_count = 0
        for item in results:
            result_count += 1
            row = item.row
            paired_info = sheet.cell(row, column).value
            if column == 2:
                print('Result %s: Found %s by %s.' %(result_count,book_info,paired_info))
            else:
                print('Result %s: Found %s by %s.' %(result_count,paired_info,book_info))
    else:
        print('No books with the entered title were found!')

#view the search history
def view_search_history():
    for item in search_history:
        print(item)

#terminal interface once user chooses a sheet to operate within
def terminal_interface():
    quit = False
    while not quit:
        print('1:display_books 2:search 3:add_book 4:remove_book 5:view_search_history 6:change_sheet/exit')
        choice = input('Enter your choice: ')
        if choice == '1':
            pass
        elif choice == '2':
            search()
        elif choice == '3':
            add_book()
        elif choice == '4':
            remove_book()
        elif choice == '5':
            view_search_history()
        elif choice == '6':
            quit = True
        else:
            print('Must choose 1-5. Please choose again.')

#main
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secrets.json', scope)
client = gspread.authorize(creds)

owned = client.open("Ben's Digital Bookshelf").worksheet('Owned')
wanted = client.open("Ben's Digital Bookshelf").worksheet('Wanted')

quit = False
while not quit:
    print('1:owned_books 2:wanted_books 3:exit')
    sheet_choice = input('Enter your choice: ')
    if sheet_choice == '1':
        sheet = owned
        terminal_interface()
    elif sheet_choice == '2':
        sheet = wanted
        terminal_interface()
    elif sheet_choice == '3':
        quit = True
    else:
        print('Must choose 1-3. Please choose again.')

    