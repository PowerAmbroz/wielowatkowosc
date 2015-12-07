# -*- coding: utf-8 -*-

#Przykład	
#!/usr/bin/python

import thread 
import time

# Define a function for the thread
def print_time( threadName, delay): #deklaracja wątków wypisania czasu
    count = 0 #licznik ilości wywołania wątku
    while count < 5: #jeśli licznik jest mniejszy niż zadana wartość
      time.sleep(delay) #ustaw uśpienie na delay
      count += 1 #zwiększ licznik o 1
      print"%s: %s" %( threadName, time.ctime(time.time())) #Wypisz w postaci stringów

def print_text( threadName, delay): #deklaracja wątków wypisania tekstu
    count = 0
    while count < 5:
      time.sleep(delay)
      count += 1
      print"%s: %s" %( threadName, "bolek")

      
# Create two threads as follows
try:
    thread.start_new_thread( print_time,("Thread-1",2,)) #rozpoczęcie nowego wątku o pobranej wcześniej nazwie oraz podanym delay
    thread.start_new_thread( print_time,("Thread-2",4,))
    thread.start_new_thread( print_text,("Thread-3",6,))
    
except:
    print"Error: unable to start thread" #wyświetla, jesli watek się nie uruchomi
while 1:
    pass
