from random import randint
from time import sleep

def game():
    try:
        while True:
            num_player = int(input('how many player want to play :) = '))
            coun = int(input('how much you want to play :) = '))
            #     ===============   1 player =======================
            if num_player == 1:
                name1 = input('player number 1 name : ')
                name2 = 'robot'
                num1 = 0
                num2 = 0
                for i in range(1,coun+1):
                    if (i%2==0):
                        print(f'\n==========>>>  {name2}  <<<<==========  round {i} ')
                        y = 1
                        z = randint(1,6)
                        v = randint(1,6)
                        x = randint(1,6)
                        if (z == x or v== x):
                            for j in range(12):
                                y = y + j
                                print(y * '*')
                                sleep(.15)
                            print('\ntrue number was \t        ==> {} <== \n'.format(x))
                            num2 =  num2 + 1
                            if i % 2 == 0:
                                z = randint(1,6)
                                v = randint(1,6)
                                x = randint(1,6)
                                if (z == x or v== x):
                                    num2 = num2 + 1
                                    for j in range(12):
                                        y = y + j
                                        print(y * '*')
                                        sleep(.15)
                                    print('\ntrue number was \t        ==> {} <== \n'.format(x))
                        else:
                            print('\nfalse number was {} \n'.format(x))
                    else:
                        print(f'\n==========>>>  {name1}  <<<<==========  round {i} ')
                        y = 1
                        z = int(input('please enter a number : '))
                        v = int(input('please enter a number : ')) 
                        x = randint(1,6)
                        if (z == x or v== x):
                            for j in range(12):
                                y = y + j
                                print(y * '*')
                                sleep(.15)
                            print('\ntrue number was \t        ==> {} <== \n'.format(x))
                            if i % 2 != 0:
                                num1 =  num1 + 1
                                z = int(input('please enter a number : '))
                                v = int(input('please enter a number : '))
                                x = randint(1,6)
                                if (z == x or v== x):
                                    num1 = num1 + 1
                                    for j in range(12):
                                        y = y + j
                                        print(y * '*')
                                        sleep(.15)
                                    print('\ntrue number was \t        ==> {} <== \n'.format(x))
                            
                        else:
                            print('\nfalse number was {} \n'.format(x))
                    print('{} have {} score\n'.format(name1, num1))
                    print('{} have {} score\n'.format(name2, num2))
                if(num1 > num2):
                    for k in range(7):
                        if( k == 3):
                            print('*******    *******')
                        if( k == 4):
                            print(f'***    {name1}   ***')
                        if( k == 5):
                            print('*******    *******')
                        else:
                            print(18*'*',end=(''))
                        print()
                elif(num2 > num1):
                    for k in range(7):
                        if( k == 3):
                            print('*******    *******')
                        if( k == 4):
                            print(f'***    {name2}   ***')
                        if( k == 5):
                            print('*******    *******')
                        else:
                            print(18*'*',end=(''))
                        print()
                else:
                    print(':(')
            
            
            
            
            #     ===============   2 player =======================
            if num_player == 2:
                name1 = input('player number 1 name : ')
                name2 = input('player number 2 name : ')
                num1 = 0
                num2 = 0
                for i in range(1,coun+1):
                    if (i%2==0):
                        print(f'\n==========>>>  {name2}  <<<<==========  round {i} ')
                    else:
                        print(f'\n==========>>>  {name1}  <<<<==========  round {i} ')
                    y = 1
                    z = int(input('please enter a number : '))
                    v = int(input('please enter a number : ')) 
                    x = randint(1,6)
                    if (z == x or v== x):
                        for j in range(12):
                            y = y + j
                            print(y * '*')
                            sleep(.15)
                        print('\ntrue number was \t        ==> {} <== \n'.format(x))
                        if i % 2 == 0:
                            num2 =  num2 + 1
                            z = int(input('please enter a number : '))
                            v = int(input('please enter a number : '))
                            x = randint(1,6)
                            if (z == x or v== x):
                                num2 = num2 + 1
                                for j in range(12):
                                    y = y + j
                                    print(y * '*')
                                    sleep(.15)
                                print('\ntrue number was \t        ==> {} <== \n'.format(x))
                            
                            
                        else:
                            num1 = num1 + 1
                            z = int(input('please enter a number : '))
                            v = int(input('please enter a number : '))
                            x = randint(1,6)
                            if (z == x or v== x):
                                num1 = num1 + 1
                                for j in range(12):
                                    y = y + j  
                                    print(y * '*')
                                    sleep(.15)
                                print('\ntrue number was \t        ==> {} <== \n'.format(x))
                        
                    else:
                        print('\nfalse number was {} \n'.format(x))
                    print('{} have {} score\n'.format(name1, num1))
                    print('{} have {} score\n'.format(name2, num2))
                if(num1 > num2):
                    for k in range(7):
                        if( k == 3):
                            print('*******    *******')
                        if( k == 4):
                            print(f'***    {name1}   ***')
                        if( k == 5):
                            print('*******    *******')
                        else:
                            print(18*'*',end=(''))
                        print()
                elif(num2 > num1):
                    for k in range(7):
                        if( k == 3):
                            print('*******    *******')
                        if( k == 4):
                            print(f'***    {name2}   ***')
                        if( k == 5):
                            print('*******    *******')
                        else:
                            print(18*'*',end=(''))
                        print()
                else:
                    print(':(')
                    
            #     ===============   3 player =======================
            
            
            if num_player == 3:
                name1 = input('player number 1 name : ')
                name2 = input('player number 2 name : ')
                name3 = input('player number 3 name : ')
                num1 = 0
                num2 = 0
                num3 = 0
                num4 = 0
                names =  (coun // 3) * [name1 , name2 , name3]
            
                for i in names:
                    num4 += 1
                    if (i == name2):
                        print(f'\n==========>>>  {name2}  <<<<==========  round {num4} ')
                        y = 1
                        z = int(input('please enter a number : '))
                        v = int(input('please enter a number : ')) 
                        x = randint(1,6)
                        if (z == x or v== x):
                            for j in range(12):
                                y = y + j
                                print(y * '*')
                                sleep(.15)
                            print('\ntrue number was \t        ==> {} <== \n'.format(x))
                            num2 =  num2 + 1
                            if i == name2:
                                z = int(input('please enter a number : '))
                                v = int(input('please enter a number : ')) 
                                x = randint(1,6)
                                if (z == x or v== x):
                                    num2 = num2 + 1
                                    for j in range(12):
                                        y = y + j
                                        print(y * '*')
                                        sleep(.15)
                                    print('\ntrue number was \t        ==> {} <== \n'.format(x))
                        else:
                            print('\nfalse number was {} \n'.format(x))
                    if(i == name1):
                        print(f'\n==========>>>  {name1}  <<<<==========  round {num4} ')
                        y = 1
                        z = int(input('please enter a number : '))
                        v = int(input('please enter a number : ')) 
                        x = randint(1,6)
                        if (z == x or v== x):
                            for j in range(12):
                                y = y + j
                                print(y * '*')
                                sleep(.15)
                            print('\ntrue number was \t        ==> {} <== \n'.format(x))
                            if i == name1:
                                num1 =  num1 + 1
                                z = int(input('please enter a number : '))
                                v = int(input('please enter a number : '))
                                x = randint(1,6)
                                if (z == x or v== x):
                                    num1 = num1 + 1
                                    for j in range(12):
                                        y = y + j
                                        print(y * '*')
                                        sleep(.15)
                                    print('\ntrue number was \t        ==> {} <== \n'.format(x))
                                
                        else:
                            print('\nfalse number was {} \n'.format(x))
                    
                    if(i == name3):
                        print(f'\n==========>>>  {name3}  <<<<==========  round {num4} ')
                        y = 1
                        z = int(input('please enter a number : '))
                        v = int(input('please enter a number : ')) 
                        x = randint(1,6)
                        if (z == x or v== x):
                            for j in range(12):
                                y = y + j
                                print(y * '*')
                                sleep(.15)
                            print('\ntrue number was \t        ==> {} <== \n'.format(x))
                            if i == name3:
                                num3 =  num3 + 1
                                z = int(input('please enter a number : '))
                                v = int(input('please enter a number : '))
                                x = randint(1,6)
                                if (z == x or v== x):
                                    num3 = num3 + 1
                                    for j in range(12):
                                        y = y + j
                                        print(y * '*')
                                        sleep(.15)
                                    print('\ntrue number was \t        ==> {} <== \n'.format(x))
                            

                        else:
                            print('\nfalse number was {} \n'.format(x))
                    print('{} have {} score\n'.format(name1, num1))
                    print('{} have {} score\n'.format(name2, num2))
                    print('{} have {} score\n'.format(name3, num3))
                if(num1 > max(num3, num2)):
                    for k in range(7):
                        if( k == 3):
                            print('*******    *******')
                        if( k == 4):
                            print(f'***    {name1}   ***')
                        if( k == 5):
                            print('*******    *******')
                        else:
                            print(18*'*',end=(''))
                        print()
                if(num2 > max(num1, num3)):
                    for k in range(7):
                        if( k == 3):
                            print('*******    *******')
                        if( k == 4):
                            print(f'***    {name2}   ***')
                        if( k == 5):
                            print('*******    *******')
                        else:
                            print(18*'*',end=(''))
                        print()
                if(num3 > max(num1, num2)):
                    for k in range(7):
                        if( k == 3):
                            print('*******    *******')
                        if( k == 4):
                            print(f'***    {name3}   ***')
                        if( k == 5):
                            print('*******    *******')
                        else:
                            print(18*'*',end=(''))
                        print()
                else:
                    print(':(')
            
            #     ===============   4 player =======================
            
            
            if num_player == 4:
                name1 = input('player number 1 name : ')
                name2 = input('player number 2 name : ')
                name3 = input('player number 3 name : ')
                name4 = input('player number 4 name : ')
                num1 = 0
                num2 = 0
                num3 = 0
                num5 = 0
                num4 = 0
                names =  (coun // 4) * [name1 , name2 , name3 , name4]
            
                for i in names:
                    num4 += 1
                    if (i == name2):
                        print(f'\n==========>>>  {name2}  <<<<==========  round {num4} ')
                        y = 1
                        z = int(input('please enter a number : '))
                        v = int(input('please enter a number : ')) 
                        x = randint(1,6)
                        if (z == x or v== x):
                            for j in range(12):
                                y = y + j
                                print(y * '*')
                                sleep(.15)
                            print('\ntrue number was \t        ==> {} <== \n'.format(x))
                            num2 =  num2 + 1
                            if i == name2:
                                z = int(input('please enter a number : '))
                                v = int(input('please enter a number : ')) 
                                x = randint(1,6)
                                if (z == x or v== x):
                                    num2 = num2 + 1
                                    for j in range(12):
                                        y = y + j
                                        print(y * '*')
                                        sleep(.15)
                                    print('\ntrue number was \t        ==> {} <== \n'.format(x))
                        else:
                            print('\nfalse number was {} \n'.format(x))
                    if(i == name1):
                        print(f'\n==========>>>  {name1}  <<<<==========  round {num4} ')
                        y = 1
                        z = int(input('please enter a number : '))
                        v = int(input('please enter a number : ')) 
                        x = randint(1,6)
                        if (z == x or v== x):
                            for j in range(12):
                                y = y + j
                                print(y * '*')
                                sleep(.15)
                            print('\ntrue number was \t        ==> {} <== \n'.format(x))
                            if i == name1:
                                num1 =  num1 + 1
                                z = int(input('please enter a number : '))
                                v = int(input('please enter a number : '))
                                x = randint(1,6)
                                if (z == x or v== x):
                                    num1 = num1 + 1
                                    for j in range(12):
                                        y = y + j
                                        print(y * '*')
                                        sleep(.15)
                                    print('\ntrue number was \t        ==> {} <== \n'.format(x))
                                
                        else:
                            print('\nfalse number was {} \n'.format(x))
                    if(i == name4):
                        print(f'\n==========>>>  {name4}  <<<<==========  round {num4} ')
                        y = 1
                        z = int(input('please enter a number : '))
                        v = int(input('please enter a number : ')) 
                        x = randint(1,6)
                        if (z == x or v== x):
                            for j in range(12):
                                y = y + j
                                print(y * '*')
                                sleep(.15)
                            print('\ntrue number was \t        ==> {} <== \n'.format(x))
                            if i == name4:
                                num5 =  num5 + 1
                                z = int(input('please enter a number : '))
                                v = int(input('please enter a number : '))
                                x = randint(1,6)
                                if (z == x or v== x):
                                    num5 = num5 + 1
                                    for j in range(12):
                                        y = y + j
                                        print(y * '*')
                                        sleep(.15)
                                    print('\ntrue number was \t        ==> {} <== \n'.format(x))

                        else:
                            print('\nfalse number was {} \n'.format(x))
                            
                            
                    
                    if(i == name3):
                        print(f'\n==========>>>  {name3}  <<<<==========  round {num4} ')
                        y = 1
                        z = int(input('please enter a number : '))
                        v = int(input('please enter a number : ')) 
                        x = randint(1,6)
                        if (z == x or v== x):
                            for j in range(12):
                                y = y + j
                                print(y * '*')
                                sleep(.15)
                            print('\ntrue number was \t        ==> {} <== \n'.format(x))
                            if i == name3:
                                num3 =  num3 + 1
                                z = int(input('please enter a number : '))
                                v = int(input('please enter a number : '))
                                x = randint(1,6)
                                if (z == x or v== x):
                                    num3 = num3 + 1
                                    for j in range(12):
                                        y = y + j
                                        print(y * '*')
                                        sleep(.15)
                                    print('\ntrue number was \t        ==> {} <== \n'.format(x))
                            
            

                        else:
                            print('\nfalse number was {} \n'.format(x))
                    print('{} have {} score\n'.format(name1, num1))
                    print('{} have {} score\n'.format(name2, num2))
                    print('{} have {} score\n'.format(name3, num3))
                    print('{} have {} score\n'.format(name4, num5))
                    
                if(num1 > max(num3, num2 , num5)):
                    for k in range(7):
                        if( k == 3):
                            print('*******    *******')
                        if( k == 4):
                            print(f'***    {name1}   ***')
                        if( k == 5):
                            print('*******    *******')
                        else:
                            print(18*'*',end=(''))
                        print()
                if(num2 > max(num1, num3 , num5)):
                    for k in range(7):
                        if( k == 3):
                            print('*******    *******')
                        if( k == 4):
                            print(f'***    {name2}   ***')
                        if( k == 5):
                            print('*******    *******')
                        else:
                            print(18*'*',end=(''))
                        print()
                if(num3 > max(num1, num2 , num5)):
                    for k in range(7):
                        if( k == 3):
                            print('*******    *******')
                        if( k == 4):
                            print(f'***    {name3}   ***')
                        if( k == 5):
                            print('*******    *******')
                        else:
                            print(18*'*',end=(''))
                        print()
                if(num5 > max(num1, num2 , num3)):
                    for k in range(7):
                        if( k == 3):
                            print('*******    *******')
                        if( k == 4):
                            print(f'***    {name3}   ***')
                        if( k == 5):
                            print('*******    *******')
                        else:
                            print(18*'*',end=(''))
                        print()
                        
                else:
                    print(':(')
    finally:
        game()

game()
