# CRISTIANO MARTINS BERALDO

def sum_of_even(LISTN):
    sumevenitens = 0
    for i in range(0, len(LISTN)):
        if LISTN[i] % 2 == 0:
            sumevenitens += LISTN[i]

    print('\nThe sum of even itens is: ',sumevenitens)

#-------------------------
def palindrome(searchstring):
    otherstring = searchstring[::-1]
    if searchstring.upper() == otherstring.upper():
        print('\n String is a palindrome!!')
    else:
        print('\n String is NOT a palindrome!!')

#-------------------------
def reversestring(searchstring):
    otherstring = searchstring[::-1]
    print('\n Reverse string is: ',otherstring)

#-------------------------
def Fibonacci_number2(n2,n_ind,n_max):
    n_max = int(n_max)

    if n_ind < n_max:
        LISTF.append(n2)
        if n_ind > 0:
            n3 = n2 + LISTF[n_ind-1]
        else:
            n3 = n2
        N_NOW = n_ind + 1

        return Fibonacci_number2(n3,N_NOW,n_max)

#-------------------------
def Fibonacci_number(n2,n_ind,n_max2):
    n_max2 = int(n_max2)
    if n2 <= n_max2:
        LISTF.append(n2)
        if n_ind > 0:
            n3 = n2 + LISTF[n_ind-1]
        else:
            n3 = n2
        N_NOW = n_ind + 1

        return Fibonacci_number(n3,N_NOW,n_max2)

#-------------------------
def unique_elements(LISTU):
    LISTN = []
    for i in range(0,len(LISTU)):
        if LISTU.count(LISTU[i]) == 1:
            LISTN.append(LISTU[i])
        else:
            if LISTN.count(LISTU[i]) == 0:
                LISTN.append(LISTU[i])
    print('\nOriginal List: ', LISTU)
    print('\nUnique elements List: ', LISTN)

#-------------------------
def count_string(string):
    dic_string = {}
    for i in range(0,len(string)):
        #print(i,string[i],len(string))
        dic_string[string[i]] = {string.count(string[i])}
    print(dic_string)

#-------------------------
def calculatepower(number,power,np,nresult):

    np += 1
    if np <= power:
        nresult = nresult * number
        return calculatepower(number,power,np,nresult)
    else:
        return nresult


#--------------------------------------------------------------------------------------

X = 99
i = 0
while int(X) != 0:
    try:
        print('Choose the operation:')
        print('1 - Find the sum of all even numbers in a list')
        print('2 - Determine if a given string is a palindrome')
        print('3 - Reverses a given string')
        print('4 - Generate the Fibonacci sequence up to a certain number of terms')
        print('5 - Generate the Fibonacci sequence up to a max number')
        print('6 - Send a list and receive a new list with unique elements')
        print('7 - Counts the occurrences of each word in a string')
        print('8 - Calculates the power of a number using recursion')
        print('0 - Leave')
        X = int(input('Operation: '))

        if 0 <= X <= 8:
            if X == 1:
                LIST = []
                N = input('\n Enter the number of elements in the list: ')

                while not N.isnumeric():
                    print('INVALID NUMBER!!')
                    N = input('\n Enter the number of elements in the list: ')

                N = int(N)
                for i in range(0,N):
                    T = int(input(f'\nEnter the number {i+1} : '))
                    LIST.append(T)

                sum_of_even(LIST)

                Y = input('\nPress enter to continue!!')

            elif X == 2:
                S = ''

                S = input('\n Enter the string: ')
                while S.strip() is None or S == '':
                    print('\nInvalid String!')
                    S = input('\n Enter the string: ')

                palindrome(S)

                Y = input('\nPress enter to continue!!')

            elif X == 3:
                S = ''

                S = input('\n Enter the string: ')
                while S.strip() is None or S == '':
                    print('\nInvalid String!')
                    S = input('\n Enter the string: ')

                reversestring(S)

                Y = input('\nPress enter to continue!!')

            elif X == 4:
                LISTF=[]
                N2 = 1
                N_NOW = 0
                number = input("\nNumber of Fibonacci's numbers: ")

                if number.strip() is None or number == '':
                    print("\nNUMBER NOT BE NULL!!")
                elif number.isnumeric() == False:
                    print('\nNOT A NUMBER!!!')
                elif int(number) < 1:
                    print("\nINVALID NUMBER!!")
                elif int(number) > 997:
                    print('\nMax number is 996!!')
                else:
                    number = int(number)
                    result = Fibonacci_number2(N2, N_NOW, number)
                    print("\nFibonacci Result: ", LISTF)

                Y = input('\nPress enter to continue!!')

            elif X == 5:
                LISTF=[]
                N2 = 1
                N_NOW = 0
                number = input("\nMAX Fibonacci's number: ")

                if number.strip() is None or number == '':
                    print("\nNUMBER NOT BE NULL!!")
                elif number.isnumeric() == False:
                    print('\nNOT A NUMBER!!!')
                elif int(number) < 1:
                    print("\nINVALID NUMBER!!")
                else:
                    number = int(number)
                    result = Fibonacci_number(N2, N_NOW, number)
                    print("\nResult: ", LISTF)

                Y = input('\nPress enter to continue!!')

            elif X == 6:
                LIST = []
                N = int(input('\n Enter the number of elements in the list: '))

                for i in range(0,N):
                    T = input(f'\nEnter the item {i+1} : ')
                    LIST.append(T)

                unique_elements(LIST)

                Y = input('\nPress enter to continue!!')

            elif X == 7:
                S = ''

                S = input('\n Enter the string: ')
                while S.strip() is None or S == '':
                    print('\nInvalid String!')
                    S = input('\n Enter the string: ')

                count_string(S)

                Y = input('\nPress enter to continue!!')

            elif X == 8:
                npower = 0
                nresult = 0
                numero = 'x'
                while numero == 'x':
                    numero = input('\nNumber: ')
                    if numero.isnumeric() == False:
                        print('\nNumber invalid. Try again!')
                        numero = 'x'
                    else:
                        potencia = 'x'
                        while potencia == 'x':
                            potencia = input('\nPower: ')
                            if potencia.isnumeric() == False:
                                print('\nPower number invalid. Try again!')
                                potencia = 'x'
                            else:
                                nresult = int(numero)
                                print("\nResult: ", calculatepower(int(numero),int(potencia),npower,nresult))

                Y = input('\nPress enter to continue!!')

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

