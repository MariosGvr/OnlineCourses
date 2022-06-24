# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 00:12:24 2020

@author: mario
"""


def championships(tennis, stadium):
    list_open = open(tennis, "r")
    
    for line in list_open:
        line = line.strip("\n")
        line_list = line.split(",")
        if stadium in line_list:
            athletes= (line_list[2], line_list[3])
            dic_winners[line_list[0]] = athletes
    return(dic_winners)


def champion_athlete(first_list):
    #print(first_list.values())
    champions_list= []
    
    for year in first_list:
        champion = first_list[year][0]
        if champion not in dic_champions:
            dic_champions[champion] = [year]
        else:
            years = dic_champions.get(champion)
            years.append(year)
            dic_champions[champion] = years
    return(dic_champions)
    
def losers(first_list):
    first_place = []
    second_place= []
    for year in first_list:
        first_place.append(first_list[year][0])
    for year in first_list:
        second = first_list[year][1]
        if second not in first_place:
            if second not in second_place:
                second_place.append(second)

                
def tournaments(athlete, champions):
    years = champions.get(athlete)
    num_of_champions = len(years)

    
def most_wins(how_many,champions):
    dic_num_champs = {}
    count = 0
    
    for key in champions:
        num_of_champ = len(champions.get(key))
        dic_num_champs[key]= num_of_champ
    sorted_dic_num_champs = sorted(dic_num_champs, key=dic_num_champs.get, reverse=True)

    for i in sorted_dic_num_champs:
        count +=1
        if count == how_many:
            break
        
def menu():
    print ("hi")
    file_name = input("Συμπληρώστε το όνομα του αρχείου: ")
    while True:
        tournament_name = input ("Συμπληρώστε το όνομα του σταδείου: ")
        if tournament_name in tournament_list:
            break
        else:
            print("Λάθος όνομα!")
    print("Δημιουργία  λεξικού  το οποίο έχει ως κλειδί το έτος και τιμή μια πλειάδα με το ζευγάρι των τελικών του τουρνουά")
    championships(file_name, tournament_name)
    print_dictionary = input("Θέλετε να τυπώσετε το λεξικό; (Ναι/Όχι) ")
    while True:
        if print_dictionary == "Ναι":
            print(dic_winners)
            break
        elif print_dictionary == "Όχι":
            break
        else:
            print_dictionary = input("Λάθος επιλογή. Θέλετε να τυπώσετε το λεξικό; (Ναι/Όχι) ")
    
    ex_order2 = input("Δημιουργία λεξικού με κλειδί το όνομα του αθλητή και τιμή μια λίστα με τα έτη που κέρδισε το τουρνουά. (Ναι/Όχι) ")
    while True:
        if ex_order2 == "Ναι":
            champion_athlete (dic_winners)
            order2 = True
            break
        elif ex_order2 == "Όχι":
            print("Το λεξικό αυτό είναι απαραίτητο για την εκτέλεση της εντολής #4 και #5. Αν εκτελεστεί η εντολή #4 ή #5 θα δημιουργηθεί αυτόματα και το λεξικό αυτό.")
            order2 = False
            break
        else:
            ex_order2 = input("Λάθος επιλογή. Δημιουργία λεξικού με κλειδί το όνομα του αθλητή και τιμή μια λίστα με τα έτη που κέρδισε το τουρνουά. (Ναι/Όχι)  ")
    
    ex_order3 = input("Δημιουργεία λίστας με τους αθλητές που συμμετείχαν αλλά δεν κέρδισαν ποτέ κάποιο τελικό του τουρνουά. (Ναι/Όχι) ")
    while True:
        if ex_order3 == "Ναι":
            losers(dic_winners)
            break
        elif ex_order3 == "Όχι":
            print("H λίστα αυτή δε θα δημιουργηθεί.")
            break
        else:
            ex_order3 = input("Λάθος επιλογή. Δημιουργεία λίστας με τους αθλητές που συμμετείχαν αλλά δεν κέρδισαν ποτέ κάποιο τελικό του τουρνουά. (Ναι/Όχι) ")
    
    ex_order4 = input("Θέλετε να βρείτε το πλήθος των τουρνουά που έχει κερδίσει ένας αθλητής στο τουρνουά του " + tournament_name + ". (Ναι/Όχι) ")
    while True:
        if ex_order4 == "Ναι":
            if order2 == False:
                print("Εκτέλεση Εντολής #2")
                order2 == True
                champion_athlete (dic_winners)
            name_of_athlete = input("Ποιο είναι το όνομα του αθλητή;")
            if name_of_athlete not in dic_champions.keys():
                print("Λάθος όνομα.")
                continue
            else:
                tournaments(name_of_athlete, dic_champions)
        elif ex_order4 == "Όχι":
            break
        else:
            ex_order4 = input("Λάθος εισαγωγή. Θέλετε να βρείτε το πλήθος των τουρνουά που έχει κερδίσει ένας αθλητής στο τουρνουά του " + tournament_name +". (Ναι/Όχι) ")

    ex_order5 = input("Θέλετε να βρείτε τους καλύτερους αθλητές; (Ναι/Όχι)")
    while True:
        if ex_order5 == "Ναι":
            if order2 == False:
                print("Εκτέλεση Εντολής #2")
                order2 == True
                champion_athlete (dic_winners)
            num_of_athletes = int(input("Τους πόσους καλύτερους αθλητές θέλετε; (Δώστε νούμερο)"))
            most_wins(num_of_athletes, dic_champions)
        elif ex_order5 == "Όχι":
            break
        else:
            ex_order5 = input("Λάθος εισαγωγή. Θέλετε να βρείτε τους καλύτερους αθλητές; (Ναι/Όχι)")

            
dic_winners = {}
dic_champions = {}
tournament_list = ["Australian Open", "U.S. Open", "Wimbledon", "French Open"]
            
menu()