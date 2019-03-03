# Enigma Machine
# SHSHacks2019
import random
from random import randint
import tkinter as tk
from tkinter import *
import math
from PIL import ImageTk, Image
import os

message = input("Enter your message: ")
message.lower()
print(message)

de = "decrypt"
en = "encrypt"
choice_1 = input("Would you like to encrypt or decrypt? :")

encrypt = []
Reverse1 = []
#letter value
arrange = []
def num_text(text, bluhas):
    dictt = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8',
    'i':'9','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17',
    'r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'
    }

    newtext = text.lower()
    for i in list(newtext):
        for k, j in dictt.items():
            if k == i:
                bluhas.append(int(j))
    return bluhas

while (choice_1[:1] != de[:1] and choice_1[:1] != en[:1]):
    print("Invalid entry")
    choice_1 = input("Would you like to encrypt or decrypt?: ")
if (choice_1[:1] == en[:1]):
    print(num_text(message, arrange))
  



if choice_1[:1] == en[:1]:
#initializing message
    rotor1user = int(input("How many rotations do you want?"))
    newMessage = []

    def rotor1():
        diction2 = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10,
                   11:11, 12:12, 13:13, 14:14, 15:15, 16:16, 17:17, 18:18, 19:19,
                   20:20, 21:21, 22:22, 23:23, 24:24, 25:25, 26:26
                   }
        for i in arrange:
            for k, j in diction2.items():
                if k == i:
                    j += rotor1user
                    if j > 26:
                        j %= 26
                    newMessage.append(int(j))
        return (newMessage)
    rotor1()

    secRot = []
    def rotor2():
        diction = {1:10, 2:3, 3:20, 4:13, 5:22, 6:24, 7:14, 8:26, 9:23, 10:7,
                   11:9, 12:6, 13:2, 14:15, 15:8, 16:21, 17:5, 18:19, 19:11,
                   20:1, 21:18, 22:17, 23:4, 24:16, 25:25, 26:12
                   }
        for i in newMessage:
            for k, j in diction.items():
                if k == i:
                    secRot.append(int(j))
        return secRot
    #print(rotor2())
    rotor2()

    thirdRot = []

    def rotor3():
        dictt3 = {1:1, 2:8, 3:26, 4:11, 5:23, 6:16, 7:19, 8:20, 9:13, 10:14, 11:24, 12:15, 13:17,
        14:9, 15:21, 16:4, 17:7, 18:25, 19:3, 20:22, 21:6, 22:5, 23:12, 24:2, 25:10, 26:18
        }
        for i in secRot:
            for k, j in dictt3.items():
                if k == i:
                    thirdRot.append(int(j))
        return (thirdRot)
    #print(rotor3())
    rotor3()

    
    def num2let():
        dictt = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',
        9:'i',10:'j', 11:'k', 12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',
        18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'
        }
        
        for i in list(thirdRot):
            for k, j in dictt.items():
                if k == i:
                    encrypt.append((j))
        return (encrypt)
    num2let()
    
    for x in encrypt:
        print(x, end='')    

if choice_1[:1] == de[:1]:
    newDeMess = []
    num_text(message, Reverse1)  
   
    def Decrypt1():
        dictt3 = {1:1, 8:2, 26:3, 11:4, 23:5, 16:6, 19:7, 20:8, 13:9, 14:10, 24:11, 15:12, 17:13,
        9:14, 21:15, 4:16, 7:17, 25:18, 3:19, 22:20, 6:21, 5:22, 12:23, 2:24, 10:25, 18:26  
        }
        for i in Reverse1:
            for k, j in dictt3.items():
                if k == i:
                    newDeMess.append(int(j))
        return (newDeMess)
    Decrypt1()
    
    Reverse2 = []
    def Decrypt2():
        dictt2 = {10:1, 3:2, 20:3, 13:4, 22:5, 24:6, 14:7, 26:8, 23:9, 7:10,
               9:11, 6:12, 2:13, 15:14, 8:15, 21:16, 5:17, 19:18, 11:19,
               1:20, 18:21, 17:22, 4:23, 16:23, 25:25, 12:26

        }
        for i in (newDeMess):
            for k, j in dictt2.items():
                if k == i:
                    Reverse2.append(int(j))
        return(Reverse2)
    Decrypt2()
    
    Reverse3 = []
    rotor1user2 = int(input("How many rotations did you input: "))
    def Decrypt3():
        diction3 = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10,
                   11:11, 12:12, 13:13, 14:14, 15:15, 16:16, 17:17, 18:18, 19:19,
                   20:20, 21:21, 22:22, 23:23, 24:24, 25:25, 26:26
                   }
        for i in Reverse2:
            for k, j in diction3.items():
                if k == i:
                    j -= rotor1user2
                    if j < 1:
                        j %= 26
                    Reverse3.append(int(j))
        return (Reverse3)
    Decrypt3()        
    
    finalDecrypt = []
    def num2let2():
        dictt = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',
        9:'i',10:'j', 11:'k', 12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',
        18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'
        }
        
        for i in list(Reverse3):
            for k, j in dictt.items():
                if k == i:
                    finalDecrypt.append((j))
        return (finalDecrypt)

    
    num2let2()
    



# GUI 
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.master.title("Enigma Machine")

    
    def create_widgets(self):

        # Your Message
        self.yourMessage = tk.Button(self)
        self.yourMessage["text"] = "Your Message\n(Click me)"
        self.yourMessage["fg"] = "#228B22"
        self.yourMessage["bg"] = "#FFD700"
        self.yourMessage["command"] = self.enigmaUI
        self.yourMessage.pack(side="top")

        
        # Quit 
        self.quit = tk.Button(self, text="QUIT", fg="#030303",
                    bg = "#FF3030", command=root.destroy)
        self.quit.pack(side="bottom")
        
        #  Encrypted Message
        self.encryptedMessage = tk.Button(self)
        self.encryptedMessage["text"] = "Encrypted Message"
        self.encryptedMessage["fg"] = "#228B22"
        self.encryptedMessage["bg"] = "#FFD700"
        self.encryptedMessage["command"] = self.encryptMes
        self.encryptedMessage.pack(side="bottom")

        # Decrypt Message
        self.decryptTool = tk.Button(self)
        self.decryptTool["text"] = "Decrypted Message"
        self.decryptTool["fg"] = "#228B22"
        self.decryptTool["bg"] = "#FFD700"
        self.decryptTool["command"] = self.decryptor
        self.decryptTool.pack(side="bottom")

    def enigmaUI(self):
        print(message)

    def encryptMes(self):
        if choice_1[:1] == de[:1]:
            print("Encryption Error")
        else:    
            for x in thirdRot:
                print(x, end='')
            print()

    def decryptor(self):
        if choice_1[:1] == en[:1]:
            print("Decryption Error")
        else:    
          for x in finalDecrypt:
            print(x,end='')
          print()    

root = tk.Tk()
root.configure(background="#006400")
root.geometry("400x300")
app = Application(master=root)
app.mainloop()





    
    

    
    
    

     

    
    

    
