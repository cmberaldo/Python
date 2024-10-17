# CRISTIANO MARTINS BERALDO


import random
import math

#-------------------------
def even_and_odd(NUM):

    lstsource = []
    lstodd = []
    lsteven = []
    # Generate the source random list of numbers automatically
    for i in range(0,NUM):
        lstsource.append(random.randint(0,100))
    #With sourcelist Test and create two other lists
    for i in range(0,len(lstsource)):
        if lstsource[i] % 2 == 0:
            lsteven.append(lstsource[i])
        else:
            lstodd.append(lstsource[i])

    print('\n Source List: ', lstsource)
    print('\n Even List: ', lsteven)
    print('\n Odd List: ', lstodd)

#-------------------------

def pos_and_neg(NUM):
    # Generate the source random list with random numbers automatically
    lstsource = []
    lstneg = []
    lstposodd = []
    lstposeven = []
    for i in range(0,NUM):
        lstsource.append(random.randint(-100,100))

    for i in range(0,len(lstsource)):
        if lstsource[i] < 0:
            lstneg.append(lstsource[i])
        elif lstsource[i] >= 0 and lstsource[i] % 2 == 0:
            lstposeven.append(lstsource[i])
        else:
            lstposodd.append(lstsource[i])


    print('\n Source List: ', lstsource)
    print('\n Negative List: ', lstneg)
    print('\n Sum of Negative List: ', sum(lstneg))
    print('\n Positive Even List: ', lstposeven)
    print('\n Sum of Positive Even List: ', sum(lstposeven))
    print('\n Positive Odd List: ', lstposodd)
    print('\n Sum of Positive Odd List: ', sum(lstposodd))

#-------------------------
def number_occur(LIST,NUM):
    count_n = 0
    for i in range(0,len(lstsource)):
        if lstsource[i] == NUM:
            count_n += 1

    print('\n Number "' + str(NUM) + '" was found ' + str(count_n) + ' times!!')

#-------------------------

def even_and_odd_tuple(NUM):

    larg_odd = 0
    larg_even = 0

    # Generate the source random list of numbers automatically
#    for i in range(0,NUM):
#        tpsource = (random.randint(0,100),)

    tpsource = tuple(random.randint(0, 100) for i in range(NUM))

    #With source Tuple Test find largest Even and Odd
    for i in range(0,len(tpsource)):
        if tpsource[i] % 2 == 0:
            if larg_even < tpsource[i]:
                larg_even = tpsource[i]
        elif larg_odd < tpsource[i]:
            larg_odd = tpsource[i]

    print('\n Source Tuple: ', tpsource)
    print('\n Largest Even number: ', larg_even)
    print('\n Largest Odd number: ', larg_odd)


#-------------------------

def sort_list_of_tuples(NUM):
    # Generate the source random list of tuples with random numbers automatically
    lstsource = []
    tpsource = ()

    for i in range(0,NUM):
        T1 = random.randint(1,9)
        T2 = random.randint(1, 9)
        tpsource = (T1,T2)
        lstsource.append(tpsource)

    print('\n Source List: ', lstsource)
    lstsource.sort(key=lambda x: (x[1], x[0]))
    print('\n Sorted List: ', lstsource)


#-------------------------

def list_of_tuples(NUM):
    # Generate the source random list of tuples with random numbers automatically
    lstsource = []
    tpsource = ()

    for i in range(0, NUM):
        T1 = random.randint(0, 100)
        T2 = round(math.sqrt(T1),2)

        tpsource = (T1, T2)
        lstsource.append(tpsource)

    print('\n List of Tuples: ', lstsource)


#-------------------------

def reverse_list(NUM):

    lstsource = []
    lstreverse = []

    for i in range(0,NUM):
        lstsource.append(random.randint(-100,100))

    print('\n Source List: ', lstsource)
    lstsource.sort()
    print('\n Sorted source List: ', lstsource)
    lstreverse = lstsource[::-1]
    print('\n Reversed List: ', lstreverse)


#-------------------------

def sum_list(NUM):

    lstsource = []
    lstsum = []

    for i in range(0,NUM):
        lstsource.append(random.randint(0,100))

    print('\n Source List: ', lstsource)
    lstsource.sort()
    print('\n Sorted source List: ', lstsource)

    for i in range(0,len(lstsource)):
        if i == 0:
            SN = lstsource[i]
        else:
            SN += lstsource[i]
        lstsum.append(SN)

    print('\n List of Sums: ', lstsum)


#-------------------------
def intersect_list(NUM1,NUM2):

    lstsource1 = []
    lstsource2 = []
    lstintersect = []

    for i in range(0,NUM1):
        lstsource1.append(random.randint(0,100))

    for i in range(0,NUM2):
        lstsource2.append(random.randint(0,100))

    lstsource1.sort()
    print('\n FIRST source List: ', lstsource1)
    lstsource2.sort()
    print('\n SECOND source List: ', lstsource2)

    for i in range(0,len(lstsource1)):
        for y in range(0,len(lstsource2)):
            if lstsource1[i] == lstsource2[y]:
                lstintersect.append(lstsource2[y])

    print('\n Intersect List: ', lstintersect)


#--------------------------------------------------------------------------------------

X = 99
i = 0
while int(X) != 0:
    try:
        print('Choose the operation:')
        print('1 - Even and Odd numbers')
        print('2 - Sum of Negative, Even and Odd numbers')
        print('3 - Number Occurrence')
        print('4 - Largest Even and Odd numbers in a Tuple')
        print('5 - Sort a list of tuples')
        print('6 - List of tuples with a number and its square')
        print('7 - Reverse list')
        print('8 - Sum of list elements')
        print('9 - Intersection of lists')
        print('0 - Leave')
        X = int(input('Operation: '))

        if 0 <= X <= 9:
            if X == 1:
                S = ''
                N = 0
                while S.strip() is None or S == '' or S.isnumeric() == False:
                    try:
                        S = input('\n Enter the total numbers of the source list: ')
                        N = int(S)
                    except:
                        print('\nInvalid Number!')
                        continue

                even_and_odd(N)

                Y = input('\nPress enter to continue!!')

            elif X == 2:
                S = ''
                N = 0
                while S.strip() is None or S == '' or S.isnumeric() == False:
                    try:
                        S = input('\n Enter the total numbers of the source list: ')
                        N = int(S)
                    except:
                        print('\nInvalid Number!')
                        continue

                pos_and_neg(N)

                Y = input('\nPress enter to continue!!')

            elif X == 3:
                S = ''
                N = 0
                lstsource = []
                # Generate a Random Source list
                for i in range(0, 20):
                    lstsource.append(random.randint(0, 10))
                print('\n Source List: ', lstsource)

                while S.strip() is None or S == '' or S.isnumeric() == False:
                    try:
                        S = input('\n Enter the search number in the source list: ')
                        N = int(S)
                    except:
                        print('\nInvalid Number!')
                        continue

                number_occur(lstsource,N)

                Y = input('\nPress enter to continue!!')

            elif X == 4:
                S = ''
                N = 0
                while S.strip() is None or S == '' or S.isnumeric() == False:
                    try:
                        S = input('\n Enter the total numbers of the source Tuple: ')
                        N = int(S)
                    except:
                        print('\nInvalid Number!')
                        continue

                even_and_odd_tuple(N)

                Y = input('\nPress enter to continue!!')

            elif X == 5:
                S = ''
                N = 0
                while S.strip() is None or S == '' or S.isnumeric() == False:
                    try:
                        S = input('\n Enter the total tuples of the source list: ')
                        N = int(S)
                    except:
                        print('\nInvalid Number!')
                        continue

                sort_list_of_tuples(N)

                Y = input('\nPress enter to continue!!')

            elif X == 6:
                S = ''
                N = 0
                while S.strip() is None or S == '' or S.isnumeric() == False:
                    try:
                        S = input('\n Enter the total tuples of the source list: ')
                        N = int(S)
                    except:
                        print('\nInvalid Number!')
                        continue

                list_of_tuples(N)

                Y = input('\nPress enter to continue!!')

            elif X == 7:
                S = ''
                N = 0
                while S.strip() is None or S == '' or S.isnumeric() == False:
                    try:
                        S = input('\n Enter the total itens of the source list: ')
                        N = int(S)
                    except:
                        print('\nInvalid Number!')
                        continue

                reverse_list(N)

                Y = input('\nPress enter to continue!!')

            elif X == 8:
                S = ''
                N = 0
                while S.strip() is None or S == '' or S.isnumeric() == False:
                    try:
                        S = input('\n Enter the total numbers of the source list: ')
                        N = int(S)
                    except:
                        print('\nInvalid Number!')
                        continue

                sum_list(N)

                Y = input('\nPress enter to continue!!')

            elif X == 9:
                S1 = ''
                S2 = ''
                N1 = 0
                N2 = 0
                while S1.strip() is None or S1 == '' or S1.isnumeric() == False:
                    try:
                        S1 = input('\n Enter the total numbers of the FIRST source list: ')
                        N1 = int(S1)
                    except:
                        print('\nInvalid Number!')
                        continue

                while S2.strip() is None or S2 == '' or S2.isnumeric() == False:
                    try:
                        S2 = input('\n Enter the total numbers of the SECOND source list: ')
                        N2 = int(S2)
                    except:
                        print('\nInvalid Number!')
                        continue

                intersect_list(N1,N2)

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

