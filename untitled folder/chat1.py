user = ''
from time import sleep
from threading import Thread
import os

def signIn():
    import hashlib
    # password = input()
    # h = hashlib.md5(password.encode())
    # print(h.hexdigest())

    signInPromt= input('sign in or create an account (s/c):')
    if signInPromt== 'c':
        upfiles = open('usernames.txt', 'a')
        # x = open('num.txt','r+')
        unhashedUN = input('create username: ')
        h = hashlib.md5(unhashedUN.encode())
        out = str(h.hexdigest())
        print(out)
        upfiles.write(out)
        upfiles.write("\n")
        # upfiles.write('('+str(x)+')')
        upfiles.close()

        upfiles = open('passwords.txt', 'a')
        unhashedUN = input('create password: ')
        upfiles = hashlib.md5(unhashedUN.encode())
        out = str(h.hexdigest())
        print(out)
        upfiles.write(out)
        upfiles.write("\n")
        upfiles.close()
        # print(x)
        # x.write(str(int(x)+1))
        # x.close()
    elif signInPromt== 's':
        unhashedUN = open('usernames.txt', 'r')
        unhashedPW = open('passwords.txt', 'r')
        hashedUN = input('username: ')
        global user
        user = hashedUN

        hashedUN = hashlib.md5(hashedUN.encode())
        hashedUN = hashedUN.hexdigest()
        hashedUN = str(hashedUN)
        # print(hashedUN)
        hashedPW = input('password: ')
        hashedPW = hashlib.md5(hashedPW.encode())
        hashedPW = hashedPW.hexdigest()
        hashedPW = str(hashedPW)
        x = unhashedUN.read()
        y = unhashedPW.read()

        # hmm = open('hmm.txt','r')
        # hm = hmm.read()
        # if hashedUN in hm and hashedPW in hm:
        #  altchat()
        # hmm.close()

        if hashedUN in x and hashedPW in y:
            print('welcome', user + '!')
            chat()
        elif hashedUN in unhashedUN and hashedPW not in unhashedPW:
            print('incorrect password')
        else:
            print('username does not exist')
        return user


def chat():
    def text():
        l = True
        shortcuts = {'/1' : 'Cool','/2':'Thanks','/3':'OK','/4':'see you later'}
        while l == True:
            readfile = open('chat.txt', 'r')
            display = readfile.read()
            print()
            sleep(0.5)
            openfile = open('chat.txt', 'a')
            #print(display, end='\r')
            ty = input('')
            if ty in shortcuts:
                #input('it worked')
                ty = shortcuts[ty]
                #print(shortcuts[ty])
            text = user + ': ' + ty
            openfile.write(text)
            openfile.write("\n")
            openfile.flush()
            if ty == 'exit':
                l = False
            openfile.close()
            readfile.close()
    def check():
        os.system('cls')
        openfile = open('chat.txt','r')
        checkOF = openfile.read()
        print(checkOF)
        openfile.close()
        while True:
            openfile = open('chat.txt','r')
            checkOF = openfile.read()
            checkOF = len(checkOF)
            #print(c)
            while True:
                openfile2 = open('chat.txt','r')
                z = openfile2.read()
                checkOF2 = len(z)
                #print(checkOF2)
                sleep(1)
                if checkOF != checkOF2:
                    os.system('cls')
                    print(z)
                    break
                openfile2.close()
            openfile.close()

    t1 = Thread(target=text)
    t2 = Thread(target=check)

    t1.start()
    t2.start()


# def altchat():
# r = open('altchat.txt','r')
#    l = True
#   display = r.read()
#  print()
# print(display)
#     while l == True:
#      o = open('altchat.txt','a')
#     ty = input('')
#    text = user+': '+ty
#   openfile.write(text)
#  openfile.write("\n")
# if text == exit:
#  l = False
#  openfile.close()
#  r.close()

signIn()
# ç(˙∆˙)∫



