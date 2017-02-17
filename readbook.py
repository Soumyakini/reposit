import os.path
import json
import itertools
import sys
filename = "readbook.status"
def searchbook(book,data):
    x = 0
    for sublist in data:
        if sublist[0] == book:
            return x;
            break;
        x = x + 1
    return -1;

with open(filename,'r') as loadfile:
    menu = input("Menu , Type 1 : For Enter New Record  , Type 2 : For Show Status , Type 3 : Search , Type 4 : Progress , Type 5 : Delete \n")
    menu = int(menu)

    if menu == 1:
        book = raw_input("Please Enter Books Name \n")
        page = int(input("Which Page you already read \n"))
        if os.path.exists(filename) :
            try:
                data = json.loads(loadfile.read())
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
            data.append([book,page])
            json.dump(data, outfile)
        sys.exit()
    elif menu == 3 :
        if os.path.exists(filename) :
            book = raw_input("Which book you want to search \n")
            data = json.loads(loadfile.read())
            number = searchbook(book,data)
            if( number > -1 ) :
                print("You read " + data[number][0] + " at page "+ str(data[number][1])+ "\n")
            else :
                print (" No Records Found ")
        else:
            print(" No Records Found ")
        sys.exit();
    elif menu == 4:
        if os.path.exists(filename) :
            x= 0 ;
            data = json.loads(loadfile.read())
            for sublist in data:
                x = sublist[1] + x
            print("You read " + str(x) + " page so far , Well done!")
        else:
            print(" No Records Found")
    elif menu == 5:
        book = raw_input(" Which book you want to delete , Type *all* to delete all \n")
        data = json.loads(loadfile.read())

        with open(filename, 'w') as outfile:

            if(book=="*all*"):
                data = []
                json.dump(data, outfile)
            else:
                number = searchbook(book,data)
                if(number > -1):
                    del(data[number])
                    json.dump(data, outfile)
                    print(book + " records has been deleted")
                else:
                    print("No Records Found")



    else:
        if os.path.exists(filename) :
            print("Here is some status")
            data = json.loads(loadfile.read())
            for val in data:
                print("You read " + val[0] + " at page " + str(val[1]) + "\n")
        else:
            print(" No Record Found ")
        sys.exit()
