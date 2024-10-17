# CRISTIANO MARTINS BERALDO


#A good example of encountering a TypeError in Python is in a mathematical operation
# performing an invalid operation such as division by zero.
# In this case, the code must, using try-except, provide specific treatment for this error.
# As for others too, this way it does not show untreated errors and cause the system stop.
# Example below
def treat_error():
    try:
        N1 = 3
        N2 = 0
        NR = N1/N2
    except ZeroDivisionError:
        print('DIVISION BY ZERO ERROR!!')
        print('\n A good example of encountering a TypeError in Python is in a mathematical operation')
        print(' performing an invalid operation such as division by zero (3/0).')
        print(' In this case, the code must, using try-except, provide specific treatment for this error.')
        print(' As for others too, this way it does not show untreated errors and cause the system stop.')

#-------------------------

def exception_test():
    NR = 0
    while NR == 0:
        try:
            print('To force other error (generic), use the operator 999 in one of two operators!\n')
            N1 = int(input('First operator: '))
            N2 = int(input('Second operator: '))
            # Force other error
            if N1 == 999 or N2 == 999:
                Print('')

            NR = N1/N2
            print('The result is: ',NR)

        except ZeroDivisionError:
            print('\nDIVISION BY ZERO ERROR!!\n')
        except ValueError:
            print('\nINVALID OPERATOR!!\n')
        except:
            print('\nAN ERROR OCCUR. TRY AGAIN!!\n')
            NR = 0

#-------------------------

class BankAccount:

    def __init__(self, Account_Number, Name, Balance):
        self.Account_Number = Account_Number
        self.Name = Name
        self.Balance = Balance

    def Create_Account(self):
        try:
            with open(self.Account_Number+'.txt', 'r') as file:
                account = file.read()
                print('\nAccount already created previously!')

        except FileNotFoundError:
            account_info = f'{self.Account_Number}\n{self.Name}\n{self.Balance}'
            #account_info = self.Account_Number + '\n' + self.Name + '\n' + self.Balance
            with open(self.Account_Number+'.txt', 'w') as file:
                file.write(account_info)
                return '\nAccount created successfully\n'
        except:
            return '\nSorry. Error to create account!'

    def Show_Balance(self):
        try:
            with open(self.Account_Number+'.txt', 'r') as file:
                account = file.readlines()
                return account
        except FileNotFoundError:
            return '\nAccount not found!'

    def Deposit_value(self,add_balance):
        try:
            with open(self.Account_Number+'.txt', 'r') as file:
                account = file.readlines()
                temp_balance = account[2].strip()
            new_balance = float(temp_balance) + float(add_balance)
            with open(self.Account_Number + '.txt', 'w') as file:
                account[2] = str(new_balance)
                file.writelines(account)
            return '\nDeposit made successfully'
        except FileNotFoundError:
            return '\nAccount not found! Deposit NOT made!'

    def Withdraw_value(self,ret_balance):
        try:
            with open(self.Account_Number+'.txt', 'r') as file:
                account = file.readlines()
                temp_balance = account[2].strip()
            if float(ret_balance) > float(temp_balance):
                return '\nInsufficient balance! Withdraw NOT made!'
            new_balance = float(temp_balance) - float(ret_balance)
            with open(self.Account_Number + '.txt', 'w') as file:
                account[2] = str(new_balance)
                file.writelines(account)
            return '\nWithdraw made successfully'
        except FileNotFoundError:
            return '\nAccount not found! Withdraw not made!'


#-------------------------

class LibraryCatalog:

    def __init__(self, Id, Name, Author, BookType, Date):
        self.Id = Id
        self.Name = Name
        self.Author = Author
        self.BookType = BookType
        self.Date = Date

    def Create_List(self):
        try:
            with open('Books.txt', 'r') as file:
                book = file.read()

        except FileNotFoundError:
            with open('Books.txt', 'w') as file:
                file.write('')


    def Show_Books(self):
        try:
            with open('Books.txt', 'r') as file:
                book = file.readlines()
                return book
        except FileNotFoundError:
            return '\nBook File not found!\n'

    def Add_book(self):
        try:
            with open('Books.txt', 'r') as file:
                book = file.readlines()
                for line in book:
                    lines = line.strip().split(',')
                    if lines[0] == self.Id:
                        return '\nBook ID already exists. Book not Added! \n'

            book_info = f'{self.Id},{self.Name},{self.Author},{self.BookType},{self.Date}'
            with open('Books.txt', 'a') as file:
                file.write(book_info + '\n')
            return '\nBook Added successfully!\n'
        except FileNotFoundError:
            return '\nERROR. Book not Added!\n'

    def Remove_book(self,id):
        achou = 0
        with open('Books.txt', 'r') as file:
            book = file.readlines()
        with open('Books.txt', 'w') as file2:
            for line in book:
                lines = line.strip().split(',')
                if lines[0] != id:
                    file2.write(line.strip() + '\n')
                elif lines[0] == id:
                    achou = 1

        if achou == 1:
            return '\nBook removed successfully!\n'
        else:
            return '\nBook not found!\n'

    def Backup_bookList(self):
        try:
            with open('Books.txt', 'r') as file:
                bookbackup = file.readlines()
            with open('Books_backup.txt', 'w') as file:
                for line in bookbackup:
                    file.write(line.strip() + '\n')
        except FileNotFoundError:
            return '\nProblems with create backup!!'


#-------------------------

class ShoppingCart:

    def __init__(self, Id, Name, Quantity, Price):
        self.Id = Id
        self.Name = Name
        self.Quantity = Quantity
        self.Price = Price

    def Create_List(self):
        try:
            with open('ListItens.txt', 'r') as file:
                listitens = file.read()

        except FileNotFoundError:
            with open('ListItens.txt', 'w') as file:
                file.write('')


    def Show_Itens(self):
        try:
            with open('ListItens.txt', 'r') as file:
                listitens = file.readlines()
                return listitens
        except FileNotFoundError:
            return '\nShopping File not found!\n'

    def Add_Item(self):
        try:
            with open('ListItens.txt', 'r') as file:
                listitens = file.readlines()
                for line in listitens:
                    lines = line.strip().split(',')
                    if lines[0] == self.Id:
                        return '\nItem ID already exists. Item not Added! \n'

            listitens_info = f'{self.Id},{self.Name},{self.Quantity},{self.Price}'
            with open('ListItens.txt', 'a') as file:
                file.write(listitens_info + '\n')
            return '\nItem Added successfully!\n'
        except:
            return '\nERROR. Item not Added!\n'

    def Remove_Item(self,id):
        achou = 0
        with open('ListItens.txt', 'r') as file:
            listitens = file.readlines()
        with open('ListItens.txt', 'w') as file2:
            for line in listitens:
                lines = line.strip().split(',')
                if lines[0] != id:
                    file2.write(line.strip() + '\n')
                elif lines[0] == id:
                    achou = 1

        if achou == 1:
            return '\nItem removed successfully!\n'
        else:
            return '\nItem not found!\n'

    def Calculate_Total(self):
        try:
            total = 0
            with open('ListItens.txt', 'r') as file:
                listitens = file.readlines()
                for line in listitens:
                    lines = line.strip().split(',')
                    totalitem = float(lines[2]) * float(lines[3])
                    total = total + totalitem
            return str(total)
        except:
            return '\nProblems for Calculate Total!!'

#-------------------------

class EmailClient:

    def __init__(self, Id, Subject, Body):
        self.Id = Id
        self.Subject = Subject
        self.Body = Body

    def Create_List(self):
        try:
            with open('DraftList.txt', 'r') as file:
                draftlist = file.read()
        except FileNotFoundError:
            with open('DraftList.txt', 'w') as file:
                file.write('')
        try:
            with open('InboxList.txt', 'r') as file:
                inboxlist = file.read()
        except FileNotFoundError:
            with open('InboxList.txt', 'w') as file:
                file.write('')

    def ComposeEmail(self):
        maxid = 0
        with open('DraftList.txt', 'r') as file:
            draftlist = file.readlines()
            for line in draftlist:
                lines = line.strip().split(',')
                if int(lines[0]) > maxid:
                    maxid = int(lines[0])
        if maxid == 0:
            maxid = 1
        draftemail_info = f'{str(maxid)},{self.Subject},{self.Body}'
        with open('DraftList.txt', 'a') as file:
            file.write(draftemail_info + '\n')
        return '\nE-mail saved in draft list!!\n'

    def Show_DraftMessages(self):
        try:
            with open('DraftList.txt', 'r') as file:
                draftlist = file.readlines()
                return draftlist
        except FileNotFoundError:
            return '\nDraft list not found!\n'

    def Show_InboxMessages(self):
        try:
            with open('InboxList.txt', 'r') as file:
                inboxlist = file.readlines()
                return inboxlist
        except FileNotFoundError:
            return '\nDraft list not found!\n'

    # Messages sent go from the draft list to the inbox list
    def SendEmail(self,id):
        achou = 0
        with open('DraftList.txt', 'r') as file:
            draftlist = file.readlines()
        with open('DraftList.txt', 'w') as file2:
            for line in draftlist:
                lines = line.strip().split(',')
                if lines[0] != id:
                    file2.write(line.strip() + '\n')
                elif lines[0] == id:
                    with open('InboxList.txt', 'a') as file3:
                        file3.write(line.strip() + '\n')
                    achou = 1

        if achou == 1:
            return '\nE-mail sent successfully!\n'
        else:
            return '\nE-mail not found!\n'

    def RemoveEmail(self,id):
        achou = 0
        with open('DraftList.txt', 'r') as file:
            draftlist = file.readlines()
        with open('DraftList.txt', 'w') as file2:
            for line in draftlist:
                lines = line.strip().split(',')
                if lines[0] != id:
                    file2.write(line.strip() + '\n')
                elif lines[0] == id:
                    achou = 1
        if achou == 1:
            return '\nE-mail removed successfully!\n'
        else:
            achou = 0
            with open('InboxList.txt', 'r') as file:
                inboxlist = file.readlines()
            with open('InboxList.txt', 'w') as file2:
                for line in inboxlist:
                    lines = line.strip().split(',')
                    if lines[0] != id:
                        file2.write(line.strip() + '\n')
                    elif lines[0] == id:
                        achou = 1
            if achou == 1:
                return '\nE-mail removed successfully!\n'
            else:
                return '\nE-mail not found!\n'



#--------------------------------------------------------------------------------------

X = 99
i = 0
while int(X) != 0:
    try:
        print('Choose the operation:')
        print('1 - Example of TypeError in Python code')
        print('2 - Exception Handling Test')
        print('3 - BankAccount class')
        print('4 - LibraryCatalog class')
        print('5 - ShoppingCart class')
        print('6 - EmailClient class')
        print('0 - Leave')
        X = int(input('Operation: '))

        if 0 <= X <= 6:
            if X == 1:
                treat_error()
                Y = input('\nPress enter to continue!!')

            elif X == 2:
                exception_test()
                Y = input('\nPress enter to continue!!')

            elif X == 3:
                T = 999
                while T != 0:
                    try:
                        print('Choose the operation:')
                        print('1 - Create Account')
                        print('2 - Show Balance')
                        print('3 - Deposit value')
                        print('4 - Withdraw value')
                        print('0 - Previous Menu')
                        T = int(input('Operation: '))

                        if T == 1:
                            id = input('Enter ID: ')
                            name = input('Enter Name: ')
                            ini_balance = input('Enter Initial balance: ')
                            account_created = BankAccount(id,name,ini_balance)
                            return_account = account_created.Create_Account()
                            print(return_account)
                        elif T == 2:
                            id = input('Enter Account ID: ')
                            account_created = BankAccount(id, '', '')
                            return_account = account_created.Show_Balance()
                            print('\n Id:',return_account[0],'Name:', return_account[1],'Balance: $', return_account[2],'\n')
                        elif T == 3:
                            id = input('Enter Account ID: ')
                            add_balance = input('Enter deposit value: ')
                            account_created = BankAccount(id, '', '')
                            return_account = account_created.Deposit_value(add_balance)
                            print(return_account)
                        elif T == 4:
                            id = input('Enter Account ID: ')
                            ret_balance = input('Enter withdraw value: ')
                            account_created = BankAccount(id, '', '')
                            return_account = account_created.Withdraw_value(ret_balance)
                            print(return_account)
                    except:
                        print('TRANSACTION ERROR! TRY AGAIN!')

            elif X == 4:
                book_created = LibraryCatalog('', '', '', '', '')
                book_created.Create_List()
                T = 999
                while T != 0:
                    try:
                        print('Choose the operation:')
                        print('1 - Show Book list')
                        print('2 - Add Book')
                        print('3 - Remove Book')
                        print('0 - Previous Menu')
                        T = int(input('Operation: '))

                        if T == 1:
                            #book_created = LibraryCatalog('', '', '','','')
                            return_book = book_created.Show_Books()
                            print('Book List:\n')
                            for line in return_book:
                                print(line.strip())
                            print('\nEnd List:\n')
                        elif T == 2:
                            book_created.Backup_bookList()
                            id = input('Enter Book ID: ')
                            name = input('Enter Book Name: ')
                            author = input('Enter Book Author: ')
                            booktype = input('Enter Book Type: ')
                            date = input('Enter Book Date (yyyy-mm-dd): ')
                            book_created = LibraryCatalog(id,name,author,booktype,date)
                            return_book = book_created.Add_book()
                            print(return_book)
                        elif T == 3:
                            book_created.Backup_bookList()
                            id = input('Enter Book ID: ')
                            #book_created = LibraryCatalog('', '', '','','')
                            return_book = book_created.Remove_book(id)
                            print(return_book)
                    except:
                        print('TRANSACTION ERROR! TRY AGAIN!')

            elif X == 5:
                list_created = ShoppingCart('', '', '', '')
                list_created.Create_List()
                T = 999
                while T != 0:
                    try:
                        print('Choose the operation:')
                        print('1 - Show Cart Itens list')
                        print('2 - Add Item')
                        print('3 - Remove Item')
                        print('4 - Calculate Total')
                        print('0 - Previous Menu')
                        T = int(input('Operation: '))

                        if T == 1:
                            return_list = list_created.Show_Itens()
                            print('Itens List:\n')
                            for line in return_list:
                                print(line.strip())
                            print('\nEnd List:\n')
                        elif T == 2:
                            id = input('Enter Item ID: ')
                            name = input('Enter Item Name: ')
                            quantity = input('Enter Quantity: ')
                            price = input('Enter Unit Price: ')
                            list_created = ShoppingCart(id,name,quantity,price)
                            return_list = list_created.Add_Item()
                            print(return_list)
                        elif T == 3:
                            id = input('Enter Item ID: ')
                            return_list = list_created.Remove_Item(id)
                            print(return_list)
                        elif T == 4:
                            return_list = list_created.Calculate_Total()
                            print('\nTotal Value of the List is: $',return_list,'\n')
                    except:
                        print('TRANSACTION ERROR! TRY AGAIN!')

            elif X == 6:

                email_created = EmailClient('', '', '')
                email_created.Create_List()
                T = 999
                while T != 0:
                    try:
                        print('Choose the operation:')
                        print('1 - Compose New e-mail')
                        print('2 - Show draft messages')
                        print('3 - Show inbox messages')
                        print('4 - Send e-mail')
                        print('5 - Remove e-mail')
                        print('0 - Previous Menu')
                        T = int(input('Operation: '))

                        if T == 1:
                            subject = input('Enter E-mail Subject: ')
                            body = input('Enter E-mail Body: ')
                            id = 0
                            email_created = EmailClient(id,subject,body)
                            return_email = email_created.ComposeEmail()
                            print(return_email)
                        elif T == 2:
                            return_email = email_created.Show_DraftMessages()
                            print('Draft List:\n')
                            for line in return_email:
                                print(line.strip())
                            print('\nEnd List:\n')
                        elif T == 3:
                            return_email = email_created.Show_InboxMessages()
                            print('Inbox List:\n')
                            for line in return_email:
                                print(line.strip())
                            print('\nEnd List:\n')
                        elif T == 4:
                            return_email = email_created.Show_DraftMessages()
                            print('Inbox List:\n')
                            for line in return_email:
                                print(line.strip())
                            print('\nEnd List:\n')
                            id = input('Enter E-mail ID: ')
                            return_email = email_created.SendEmail(id)
                            print(return_email)
                        elif T == 5:
                            id = input('Enter E-mail ID: ')
                            return_email = email_created.RemoveEmail(id)
                            print(return_email)
                    except:
                        print('TRANSACTION ERROR! TRY AGAIN!')

        else:
            i += 1
            if i < 3:
                print('\n\nInvalid operation. Try again!\n\n')

            else:
                print('\n\nPLEASE, Try a valid number!!!\n\n')
    except:
        i += 1
        print('\n\nInvalid operation. Try again!')
        Y = input('\nPress enter to continue!!')

print('\n\nThank you!')
print('Merci beaucoup!')
