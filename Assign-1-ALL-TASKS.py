# CRISTIANO MARTINS BERALDO



def replacecharacter(ST,FC,RC):
    NEW_ST = ST.replace(FC,RC)
    print('\n Original string is: ', ST)
    print('\n New string is: ', NEW_ST)

#-------------------------

def reversestring(searchstring):
    otherstring = searchstring[::-1]
    print('\n Reverse string is: ',otherstring)

#-------------------------

def count_string(string,character):

    count_c = string.count(character)
    print('\n Character "' + character + '" was found '+ str(count_c) + ' times!!')

#-------------------------

def count_type_character(string):
    count_u = 0
    count_l = 0

    for i in range(0,len(string)):
        if string[i] == string[i].upper():
            count_u += 1
        elif string[i] == string[i].lower():
            count_l += 1

    print('\n String has '+ str(count_u) + ' Uppercase Characters and '+ str(count_l) + ' Lowercase Characters!!')

#-------------------------

def count_common_strings(string1,string2):
    lst_str = []
    for i in range(0,len(string1)):
        for n in range(0, len(string2)):
            if string1[i] == string2[n]:
                if lst_str.count(string2[n]) == False:
                    lst_str.append(string2[n])
                    break

    if len(lst_str) == 0:
        print('\n Common characters are: None')
    else:
        print('\n Common characters are: ', lst_str)

#-------------------------

def count_dif_strings(string1,string2):
    lst_str = []
    for i in range(0,len(string1)):
        found = 0
        for n in range(0, len(string2)):
            if string1[i] == string2[n]:
                found = 1
                break
        if found == 0 and lst_str.count(string1[i]) == False:
            lst_str.append(string1[i])

    if len(lst_str) == 0:
        print('\n Different characters are: None')
    else:
        print('\n Different characters are: ', lst_str)

#-------------------------

def sort_string(string):
    lst_str = []
    i = 0
    n = 0
    while i >= 0 and n != -1:
        n = string.find('-',i)
        if n != -1:
            lst_str.append(string[i:n])
        else:
            lst_str.append(string[i:])
        #print(i,n,string[i:])
        i = n + 1
    if len(lst_str) == 1:
        new_string = string
    else:
        lst_str.sort()
        new_string = '-'.join(lst_str)

    print('\n Old string is: ', string)
    print('\n New string is: ', new_string)

#-------------------------

def palindrome(searchstring):
    otherstring = searchstring[::-1]
    if searchstring.upper() == otherstring.upper():
        print('\n String is a palindrome!!')
    else:
        print('\n String is NOT a palindrome!!')

#-------------------------

def anagram(string1,string2):
    string1_sort = sorted(string1.upper())
    string2_sort = sorted(string2.upper())
    #print(string1_sort,string2_sort)
    if string1_sort == string2_sort:
        print('\n Strings "'+ string1 +'" and "'+ string2 + '" are anagrams!!')
    else:
        print('\n Strings "'+ string1 +'" and "'+ string2 + '" are NOT anagrams!!')


#--------------------------------------------------------------------------------------

X = 99
i = 0
while int(X) != 0:
    try:
        print('Choose the operation:')
        print('1 - Change Character')
        print('2 - Reverses a Given String')
        print('3 - Character Occurrence')
        print('4 - Count Number of Lowercase and Uppercase Characters')
        print('5 - Check Common Letters')
        print('6 - Check Different Letters')
        print('7 - Hyphen Separate Sequence')
        print('8 - Determine if a given string is a palindrome')
        print('9 - Detect Anagrams')
        print('0 - Leave')
        X = int(input('Operation: '))

        if 0 <= X <= 9:
            if X == 1:
                S = ''

                S = input('\n Enter the string: ')
                while S.strip() is None or S == '':
                    print('\nInvalid String!')
                    S = input('\n Enter the string: ')

                F = input('\n Enter the search character: ')
                while F.strip() is None or F == '':
                    print('\nInvalid Character!')
                    F = input('\n Enter the search character: ')

                R = input('\n Enter the replace character: ')
                while R.strip() is None or R == '':
                    print('\nInvalid Character!')
                    R = input('\n Enter the replace character: ')

                replacecharacter(S,F,R)

                Y = input('\nPress enter to continue!!')

            elif X == 2:
                S = ''

                S = input('\n Enter the string: ')
                while S.strip() is None or S == '':
                    print('\nInvalid String!')
                    S = input('\n Enter the string: ')

                reversestring(S)

                Y = input('\nPress enter to continue!!')

            elif X == 3:
                S = ''

                S = input('\n Enter the string: ')
                while S.strip() is None or S == '':
                    print('\nInvalid String!')
                    S = input('\n Enter the string: ')

                C = input('\n Enter the character to find: ')
                while C.strip() is None or C == '':
                    print('\nInvalid String!')
                    C = input('\n Enter the character to find: ')

                count_string(S,C)

                Y = input('\nPress enter to continue!!')

            elif X == 4:
                S = ''

                S = input('\n Enter the string: ')
                while S.strip() is None or S == '':
                    print('\nInvalid String!')
                    S = input('\n Enter the string: ')

                count_type_character(S)

                Y = input('\nPress enter to continue!!')

            elif X == 5:
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

                count_common_strings(S1,S2)

                Y = input('\nPress enter to continue!!')

            elif X == 6:
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

                count_dif_strings(S1,S2)

                Y = input('\nPress enter to continue!!')

            elif X == 7:
                S = ''

                S = input('\n Enter the string: ')
                while S.strip() is None or S == '':
                    print('\nInvalid String!')
                    S = input('\n Enter the string: ')

                sort_string(S)

                Y = input('\nPress enter to continue!!')

            elif X == 8:
                S = ''

                S = input('\n Enter the string: ')
                while S.strip() is None or S == '':
                    print('\nInvalid String!')
                    S = input('\n Enter the string: ')

                palindrome(S)

                Y = input('\nPress enter to continue!!')

            elif X == 9:
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

                anagram(S1,S2)

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

