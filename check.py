import os.path
import json
import itertools
import sys
from datetime import datetime

filename = "checktest.status"
file = "suggest.status"
if not (os.path.exists(filename)) :
    with open(filename, 'w') as outfile:
        print("Status File Created")
        
def searchbook(book,data):
    x = 0
    for each_dict in data:
        if each_dict.get('Name', '') == book:
            return x;
            break;
        x = x + 1
    return -1;
def suggestlist(sug , suglist):
    if sug in suglist:
        print(suglist[sug])
        

def print_note(filename):
    
    if os.path.exists(filename):
            with open(filename, 'r') as fp:
                data = json.load(fp)
            for each_dict in data:
                return_date = each_dict.get('Return date',0)
                
                if return_date:
                    cur_date = datetime.now()
                    date = [int(each) for each in return_date.split('-')]
                    r_d = datetime(date[2], date[1], date[0], 12, 0 ,0)
                    diff = (r_d - cur_date)
                
                    if diff.days <= 5 and diff.days > 0:
                        book_name = each_dict.get('Name','')
                        print("You have",diff.days,"days left to return your book ",book_name)
                    
            
with open(filename,'r') as loadfile:
    print_note(filename)
    ex = 'n'
    while (ex == 'n'):
        menu = input("Menu , Type 1 : For Enter New Record  , Type 2 : For Show Status , Type 3 : Search , Type 4 : Delete \n")
    
        menu = int(menu)

        if menu == 1:
            return_date = ''
            book = input("Please Enter Book's Name \n")
            genre = input("Enter the book's genre (Classics, Fantasy, Adventure, Horror, Educational, Drama). This will help us suggest more books of the same kind. ")
            page = int(input("Which Page are you in? \n"))
            library = input('Is the book from a library?(y/n)')
            if library == 'y':
                return_date = input("Enter the return date(dd/mm/yy)")
        
        
            if os.path.exists(filename) :
                try:
                    data = json.load(loadfile)
                except:
                    print("Cannot Access File , Please Backup and Delete Status File or using our system to automatically do for you\n")
                    print(" Just Press 1 , Let System fix it , If it was your first time using this software \n")
                    choice = int(input("Press 1 : Continue let our system fix it , Press 2 Just Exit \n"))
                    if(choice == 1):
                        data = []
                    else:
                        sys.exit()
            else :
                data = []

            number = searchbook(book,data)
            if(number > -1):
                del data[number]
            with open(filename, 'w') as outfile:
                if return_date:
                    
                    data.append({'Name':book,'Page':page,'Genre':genre, 'Return date':return_date})
                else:
                    data.append({'Name':book,'Page':page,'Genre':genre})
                json.dump(data, outfile)
            
        elif menu == 2:
            with open(filename, 'r') as fp:
                data = json.load(fp)
            for each_dict in data:
                book_name = each_dict.get('Name', '')
                page = each_dict.get('Page', 0)
                return_date = each_dict.get('Return date',0)
                print("Status:")
                print(book_name, "at Page", page)
                print("The book has to be returned on ", return_date)
        
        elif menu == 3 :
            with open(filename, 'r') as a:
            
                data = json.load(a)
                
                book = input("Which book you want to search \n")
                number = searchbook(book,data)
                if( number > -1 ) :
                    print("You read " + data[number]['Name'] + " at page "+ str(data[number]['Page'])+ "\n")
                    sug = data[number]['Genre']
                else :
                    print (" No Records Found ")
            with open(file, 'r') as b:
                    
                suglist = json.load(b)
                suggestbook(sug, suglist)    
                                 
                
            
            sys.exit();
 
        elif menu == 4:
            book = input(" Which book you want to delete , Type *all* to delete all \n")
            data = json.loads(loadfile.read())

            with open(filename, 'w') as outfile:
                if(book=="*all*"):
                    data = []
                    json.dump(data, outfile)
                else:
                    number = searchbook(book,data)
                    if(number > -1):
                        del (data[number])
                        json.dump(data, outfile)
                        print(book + " records has been deleted")
                    else:
                        print("No Records Found")



   
            sys.exit()
