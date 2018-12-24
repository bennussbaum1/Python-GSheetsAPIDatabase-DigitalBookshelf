#global variables
search_history = []

import re
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#what from here goes into a function that is called in main and what is a global var? and global var only ones that codde updates????
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secrets.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Ben's Digital Bookshelf").sheet1
#sheet2 = client.open("Ben's Digital Bookshelf").sheet2

max_rows = len(sheet.get_all_values()) # may be better to fill empty as missing row would be a wipe of the next cells
max_cols = len(sheet.get_all_values()[0])

#removes a book from the bookshelf
def remove_book():
    book_title = input("Enter the title of the book you want to remove: ")
    results = sheet.findall(book_title)#chnage to row 1 only
    if bool(results):
        if len(results) > 1:
            selection = int(input('Enter the number of the book you wish to delete: '))#add a printed numbering so this makes sense
            row = results[selection -1].row
            author = sheet.cell(row, 2).value
            sheet.delete_row(int(row))
            print('Deleted %s by %s.' %(book_title,author))
        else:
            row = results[0].row
            author = sheet.cell(row, 2).value
            sheet.delete_row(int(row))
            print('Removed %s by %s from bookshelf.' %(book_title,author))
    else:
        print('No books with the entered title were found!')

#add a book to the bookshelf
def add_book():#could change to insert_row(rowtext, rownum) so never will overwrite?
    print("You will be asked to enter the book's title and author.")
    book_title = input("Enter the book's title: ")
    sheet.update_cell(max_rows + 1, 1, book_title)

    book_author = input("Enter the book's author: ")
    sheet.update_cell(max_rows + 1, 2, book_author)

    print('Book has been added to the bookshelf!')

#search books by title or author
def search():
    print('1:search_by_title 2:search_by_author 3:return')
    choice = input('Enter your choice: ')
    if choice == '1':
        book_search()
    elif choice == '2':
        author_search()
    elif choice == '3':
        pass
    else:
        print('Must choose 1-3. Please choose again.')

#title search
def book_search():
    book_title = input("Enter the book's title: ")
    search_history.append(book_title) #add a view history option in menu taht appears once you've done searches
    results = sheet.findall(book_title)#change to row 1 only
    if bool(results):
        for item in results:
            row = item.row
            author = sheet.cell(row, 2).value
            print('Found %s by %s.' %(book_title,author))
    else:
        print('No books with the entered title were found!')

#author search
def author_search():#change to row 2 only #make it accept 'close' queries in both title and auth
    book_author = input("Enter the book's author: ")
    search_history.append(book_author)
    results = sheet.findall(book_author)
    if bool(results):
        for item in results:
            row = item.row
            book = sheet.cell(row, 1).value
            print('Found %s by %s.' %(book, book_author))
    else:
        print('No books with the entered title were found!')
    

#main
quit = False
while not quit:
    print('1:display_books 2:search 3:add_book 4:remove_book 5:exit')
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
        quit = True
    else:
        print('Must choose 1-5. Please choose again.')
