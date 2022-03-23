#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 08:01:38 2022

@author: baye
"""
import mysql.connector
from menu import * 
from SQL_SELECT import *

mydb = mysql.connector.connect(
    user='baye',
    password="eBaye1er",
    host='localhost',
    database='base_exo',
    use_pure=False)
mycursor = mydb.cursor()


def mySelectFonction():
    """ We are gonna choose each corresponding portion and make a 
    display thanks to a MySQL Query in the database 'base_exo' 
    
    For each yet executed query, it will be removed from the menu and stocked into a python
    container that I called here queryStillExecuting.
    We will need show our queries already executed thanks to the queryStillExecuting list.
     """
    
    queryStillExecuting = list()
    query = ""
    while query != "Q":
        print("\n ********* MENU ******** \n")
        menuFunc()
        query = input("Choose a number or a letter here to execute a query:")
        query = query.upper()

        if query == "1":
            mycursor.execute(sql1)
            res1 = mycursor.fetchall()
            for res in res1:
                print(res)
            queryStillExecuting.append(list_sql[0])
            myMenuNumber.pop("1")
            
          
        elif query == "2":
            mycursor.execute(sql2)
            res2 = mycursor.fetchall()
            for res in res2:
                print(res)
            queryStillExecuting.append(list_sql[1])
            myMenuNumber.pop("2")
            
            
        elif query == "3":
            mycursor.execute(sql3)
            res3 = mycursor.fetchall()
            for res in res3:
                print(res)
            queryStillExecuting.append(list_sql[2])
            myMenuNumber.pop("3")
            
        elif query == "4":
            mycursor.execute(sql4)
            res4 = mycursor.fetchall()
            for res in res4:
                print(res)
            queryStillExecuting.append(list_sql[3])
            myMenuNumber.pop("4")
                
        elif query == "5":
            mycursor.execute(sql5)
            res5 = mycursor.fetchall()
            for res in res5:
                print(res)
            queryStillExecuting.append(list_sql[4])
            myMenuNumber.pop("5")
                
        elif query == "6":
            mycursor.execute(sql6)
            res6 = mycursor.fetchall()
            for res in res6:
                print(res)
            queryStillExecuting.append(list_sql[5])
            myMenuNumber.pop("6")
            
        elif query == "7":
            mycursor.execute(sql7)
            res7 = mycursor.fetchall()
            for res in res7:
                print(res)
            queryStillExecuting.append(list_sql[6])
            myMenuNumber.pop("7")
            
        elif query == "8":
            mycursor.execute(sql8)
            res8 = mycursor.fetchall()
            for res in res8:
                print(res)
            queryStillExecuting.append(list_sql[7])
            myMenuNumber.pop("8")
            
        elif query == "9":
            mycursor.execute(sql9)
            res9 = mycursor.fetchall()
            for res in res9:
                print(res)
            queryStillExecuting.append(list_sql[8])
            myMenuNumber.pop("9")
                
        elif query == "10":
            mycursor.execute(sql10)
            res10 = mycursor.fetchall()
            for res in res10:
                print(res)
            queryStillExecuting.append(list_sql[9])
            myMenuNumber.pop("10")
            
        elif query == "11":
            mycursor.execute(sql11)
            res11 = mycursor.fetchall()
            for res in res11:
                print(res)
            queryStillExecuting.append(list_sql[10])
            myMenuNumber.pop("11")
           
        elif query == "12":
            mycursor.execute(sql12)
            res12 = mycursor.fetchall()
            for res in res12:
                print(res)
            queryStillExecuting.append(list_sql[11])
            myMenuNumber.pop("12")
           
        elif query == "13":
            mycursor.execute(sql13)
            res13 = mycursor.fetchall()
            for res in res13:
                print(res)
            queryStillExecuting.append(list_sql[12])
            myMenuNumber.pop("13")
           
        elif query == "14":
            mycursor.execute(sql14)
            res14 = mycursor.fetchall()
            for res in res14:
                print(res)
            queryStillExecuting.append(list_sql[13])
            myMenuNumber.pop("14")
              
        elif query == "15":
            mycursor.execute(sql15)
            res15 = mycursor.fetchall()
            for res in res15:
                print(res)
            queryStillExecuting.append(list_sql[14])
            myMenuNumber.pop("15")
                
        elif query == "16":
            mycursor.execute(sq16)
            res16 = mycursor.fetchall()
            for res in res16:
                print(res)
            queryStillExecuting.append(list_sql[15])
            myMenuNumber.pop("16")
            
        elif query == "17":
            mycursor.execute(sql17)
            res17 = mycursor.fetchall()
            for res in res17:
                print(res)
            queryStillExecuting.append(list_sql[16])
            myMenuNumber.pop("17")
           
        elif query == "18":
            mycursor.execute(sql18)
            res18 = mycursor.fetchall()
            for res in res18:
                print(res)
            queryStillExecuting.append(list_sql[17])
            myMenuNumber.pop("18")
            
        elif query == "19":
            mycursor.execute(sql19)
            res19 = mycursor.fetchall()
            for res in res19:
                print(res)
            queryStillExecuting.pop(list_sql[18])
            myMenuNumber.pop("19")
           
        elif query == "20":
            mycursor.execute(sql20)
            res20 = mycursor.fetchall()
            for res in res20:
                print(res)
            queryStillExecuting.append(list_sql[19])
            myMenuNumber.pop("20")
            
        elif query == "21":
            mycursor.execute(sql21)
            res21 = mycursor.fetchall()
            for res in res21:
                print(res)
            queryStillExecuting.append(list_sql[20])
            myMenuNumber.pop("21")
               
        elif query == "22":
            mycursor.execute(sql22)
            res22 = mycursor.fetchall()
            for res in res22:
                print(res)
            queryStillExecuting.append(list_sql[21])
            myMenuNumber.pop("22")
               
        elif query == "23":
            mycursor.execute(sql23)
            res23 = mycursor.fetchall()
            for res in res23:
                print(res)
            queryStillExecuting.append(list_sql[22])
            myMenuNumber.pop("23")
               
        elif query == "24":
            mycursor.execute(sql24)
            res24 = mycursor.fetchall()
            for res in res24:
                print(res)
            queryStillExecuting.append(list_sql[23])
            myMenuNumber.pop("24")
            
        elif query == "25":
            mycursor.execute(sql25)
            res24 = mycursor.fetchall()
            for res in res25:
                print(res)
            queryStillExecuting.append(list_sql[24])
            myMenuNumber.pop("25")
            
        # Displaying Queries yet executing    
        elif query == "E":
            for rq in queryStillExecuting:
                mycursor.execute(rq)
                display = mycursor.fetchall()
                for display1 in display:
                    print(display1)
            
        # Displaying the whole Menu
        elif query == "R":
            for allmenu in myallMenu.values():
                print(allmenu)
           
    print("Thanks, Bye!")  

mySelectFonction()          