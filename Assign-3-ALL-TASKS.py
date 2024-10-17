# CRISTIANO MARTINS BERALDO


import random


def sort_lower_upper(string):

    # Separate and order the lowers
    NEW_ST_L = ''.join(sorted(filter(lambda x: x.islower(),string)))
    # Separate and order the uppers
    NEW_ST_U = ''.join(sorted(filter(lambda x: x.isupper(),string)))
    # Other characters
    NEW_ST_O = ''.join(sorted(filter(lambda x: (not x.isupper() and not x.islower()),string)))
    #join the both strings
    NEW_ST = NEW_ST_L + NEW_ST_U + NEW_ST_O
    print('\n Original string is: ', string)
    print('\n New string is: ', NEW_ST)

#-------------------------
def count_type_character(string):
    count_u = 0
    count_l = 0
    count_s = 0
    count_n = 0
    count_v = 0

    # Count different types of characters including empty characters
    for i in range(0,len(string)):
        if not string[i].isalnum() and string[i] != ' ':
            count_s += 1
        elif string[i].isupper():
            count_u += 1
        elif string[i].islower():
            count_l += 1
        elif string[i].isnumeric():
            count_n += 1
        elif string[i] == ' ':
            count_v += 1

    print('\nString has '+ str(count_u) + ' Uppercase Characters,\n'+ str(count_l) + ' Lowercase Characters,')
    print(str(count_s) + ' Special symbol Characters \nand ' + str(count_n) + ' Number Characters!!')
    if count_v > 0:
        print('\n String also has '+ str(count_v) + ' Empty Characters!')

#-------------------------

def balance_strings(string1,string2):

    strd1 = {}
    strd2 = {}

    #input all characters of string1 in dict1 with number of occurences
    for c in string1:
        if c in strd1:
            strd1[c] +=1
        else:
            strd1[c] = 1

    #input all characters of string2 in dict2 with number of occurences
    for c in string2:
        if c in strd2:
            strd2[c] +=1
        else:
            strd2[c] = 1
    #validate if strd1 is in strd2
    if all(strd2.get(key, 0) >= value for key, value in strd1.items()):
        print(f'\n String "{string1}" and "{string2}" are balanced')
    else:
        print(f'\n String "{string1}" and "{string2}" are NOT balanced')

#-------------------------

def count_strings(string):

    strd = {}
    #input all characters of string1 in dict1 with number of occurences
    for c in string:
        if c in strd:
            strd[c] +=1
        else:
            strd[c] = 1

    print('\n Original string is: ', string)
    print('\n Result is: ', strd)

#-------------------------

def number_occur(LIST,NUM):
    numd = {}

    for i in range(0,len(LIST)):
        # input all numbers of LIST in dict with number of occurences
        if LIST[i] in numd:
            numd[LIST[i]] += 1
        else:
            numd[LIST[i]] = 1

    print('\n Result is: ', numd)

#-------------------------

def reversestring(searchstring):
    otherstring = searchstring[::-1]
    print('\n Reverse string is: ',otherstring)

#-------------------------

def draw_pattern(NUM):

    NUM_PAT = 0
    STR = ''
    for i in range(1,NUM *2):
        if i <= NUM:
            NUM_PAT = i
        else:
            NUM_PAT = (NUM*2) - i

        for i in range(NUM_PAT):
            STR = STR + '*'
        print(STR)
        STR = ''

#-------------------------


def calculate_sign(NUM1,NUM2):
    #Create a dictionary of the astrological signs
    dict_signs = {
        "Aries": ((21, 3), (19, 4)),
        "Taurus": ((20, 4), (20, 5)),
        "Gemini": ((21, 5), (20, 6)),
        "Cancer": ((21, 6), (22, 7)),
        "Leo": ((23, 7), (22, 8)),
        "Virgo": ((23, 8), (22, 9)),
        "Libra": ((23, 9), (22, 10)),
        "Scorpio": ((23, 10), (21, 11)),
        "Sagittarius": ((22, 11), (21, 12)),
        "Capricorn": ((22, 12), (19, 1)),
        "Aquarius": ((20, 1), (18, 2)),
        "Pisces": ((19, 2), (20, 3))
    }
    date_user = (NUM1,NUM2)
    for (sign,(date_ini,date_fin)) in dict_signs.items():
        #print(date_ini,date_fin,date_user,(date_ini[1] == date_user[1] and date_ini[0] <= date_user[0]), (date_fin[1] == date_user[1] and date_user[0] <= date_fin[0]) )
        if (date_ini[1] == date_user[1] and date_ini[0] <= date_user[0]) or (date_fin[1] == date_user[1] and date_user[0] <= date_fin[0]):
            print(f'\nYour date,{date_user[0]}/{date_user[1]}, correspond of Astrological sign: ',sign)
            break


#--------------------------------------------------------------------------------------

X = 99
i = 0
while int(X) != 0:
    try:
        print('Choose the operation:')
        print('1 - Task 1 - Arrange String with Lower and Upper')
        print('2 - Task 2 - Count Characters types of String')
        print('3 - Task 3 - String Balance')
        print('4 - Task 4 - Count Character Occurrence')
        print('5 - Task 5 - Count each Element of a List')
        print('6 - Task 6 - Reverses a Given String')
        print('7 - Task 7 - Construct Defined Pattern')
        print('8 - Task 8 - Give Astrological Sign')
        print('0 - Leave')
        X = int(input('Operation: '))

        if 0 <= X <= 9:
            if X == 1:
                S = ''

                S = input('\n Enter the string: ')
                while S.strip() is None or S == '':
                    print('\nInvalid String!')
                    S = input('\n Enter the string: ')

                sort_lower_upper(S)

                Y = input('\nPress enter to continue!!')

            elif X == 2:
                S = ''

                S = input('\n Enter the string: ')
                while S.strip() is None or S == '':
                    print('\nInvalid String!')
                    S = input('\n Enter the string: ')

                count_type_character(S)

                Y = input('\nPress enter to continue!!')

            elif X == 3:
                S1 = ''
                S2 = ''

                S1 = input('\n Enter the first string: ')
                while S1.strip() is None or S1 == '':
                    print('\nInvalid String!')
                    S1 = input('\n Enter the first string: ')

                S2 = input('\n Enter the second string: ')
                while S2.strip() is None or S2 == '':
                    print('\nInvalid String!')
                    S2 = input('\n Enter the second string: ')

                balance_strings(S1,S2)

                Y = input('\nPress enter to continue!!')

            elif X == 4:
                S = ''

                S = input('\n Enter the string: ')
                while S.strip() is None or S == '':
                    print('\nInvalid String!')
                    S = input('\n Enter the string: ')

                count_strings(S)

                Y = input('\nPress enter to continue!!')

            elif X == 5:
                S = ''
                N = 0
                lstsource = []

                while S.strip() is None or S == '' or S.isnumeric() == False:
                    try:
                        S = input('\n Enter the total numbers of the source list: ')
                        N = int(S)
                        # Generate a Random Source list with step 10
                        for i in range(0, N):
                            lstsource.append(random.randrange(0, 100, 10))
                        lstsource.sort()
                        print('\n Source List: ', lstsource)

                    except:
                        print('\nInvalid Number!')
                        continue

                number_occur(lstsource,N)

                Y = input('\nPress enter to continue!!')

            elif X == 6:
                S = ''

                S = input('\n Enter the string: ')
                while S.strip() is None or S == '':
                    print('\nInvalid String!')
                    S = input('\n Enter the string: ')

                reversestring(S)

                Y = input('\nPress enter to continue!!')

            elif X == 7:
                S = ''
                #Construct a pattern according to the user desire
                while S.strip() is None or S == '' or S.isnumeric() == False:
                    try:
                        S = input('\n Enter highest number of "*" in the same lign: ')
                        N = int(S)
                    except:
                        print('\nInvalid Number!')
                        continue

                draw_pattern(N)

                Y = input('\nPress enter to continue!!')

            elif X == 8:
                S1 = ''
                S2 = ''

                while S1.strip() is None or S1 == '' or S1.isnumeric() == False:
                    try:
                        S1 = input('\n Enter the Day of Birth (1-31): ')
                        N1 = int(S1)
                        if N1 < 1 or N1 > 31:
                            print('\nInvalid Number!')
                            S1 = ''
                            continue
                    except:
                        print('\nInvalid Number!')
                        continue

                while S2.strip() is None or S2 == '' or S2.isnumeric() == False:
                    try:
                        S2 = input('\n Enter the Month of Birth (1-12): ')
                        N2 = int(S2)
                        if N2 < 1 or N2 > 12:
                            print('\nInvalid Number!')
                            S2 = ''
                            continue
                    except:
                        print('\nInvalid Number!')
                        continue

                calculate_sign(N1,N2)

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

