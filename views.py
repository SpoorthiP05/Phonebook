from hashlib import new
from asyncore import write
import re
import sys
import csv
import telnetlib
from typing import ValuesView

def add(i):
    with open('data.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(i)

def view():
    data = []
    with open('data.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    print(data)
    return data

# view()

def remove(i):
    def save(j):
        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(j)

    new_list = []
    telephone = i

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)

            for element in row:
                if element == telephone:
                    new_list.remove(row)
    save(new_list)

#remove('645441')
#view()

def update(i):
    
    def update_newlist(j):
        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(j)

    new_list = []
    telephone = i[0]
    # ['123', 'demo', 'M', '123', 'demo@gmail.com']

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)
            for element in row:
                if element == telephone:
                    name = i[1]
                    gender = i[2]
                    telephone = i[3]
                    email = i[4]

                    data = [name, gender, telephone, email]
                    index = new_list.index(row)
                    new_list[index] = data

    update_newlist(new_list)

# sample = ['123','girlCoder','F','123','girl123@gmail.com']
# update(sample)

def search(i):
    data = []
    telephone = i

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for element in row:
                if element == telephone:
                    data.append(row)
    print(data)
    return data
search('123')