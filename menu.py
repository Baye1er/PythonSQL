#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 10:21:22 2022

@author: baye
"""


myMenuNumber = {
            "1":"□ 1: Pour lister les tous les agences",
            "2":"□ 2: Pour lister tous les caissiers par ordre croissant de leur nom",
            "3":"□ 3: Pour lister tous chef d’agence ainsi que l'adresse de l’agence",
            "4":"□ 4: Pour lister les comptes de transaction de l’agence Plateau par ordre croissant du solde",
            "5":"□ 5: Pour lister la somme des montants déposés par un caissier dans un compte de transaction de l’agence dont le chef est moussa dop par ordre croissant du montant",
            "6":"□ 6: Pour lister les utilisateurs de l’agence Plateau",
            "7":"□ 7: Pour lister le nombre de compte par agence",
            "8":"□ 8: Pour lister les comptes affectés à l’utilisateur moussa diop durant le mois de Mai 2021",
            "9":"□ 9: Pour lister les utilisateurs à qui on a affecté le compte numéro 001 durant année 2021",
            "10":"□ 10: Pour lister le montant des transactions effectué par utilisateur et par date dans l’agence dont le numéro est 001",
            "11":"□ 11: Pour lister le nombre d’affectation par utilisateur et numéro de compte durant le premier trimestre de l’année 2021 par ordre croissant de ce nombre d’affectation dans l’agence dont le numéro est 001",
            "12":"□ 12: Pour lister les dépôts effectués et les retraits par jour dans l’agence dont le chef est moussa diop par ordre croissant du montant",
            "13":"□ 13: Pour lister les montants de transactions et les frais associés effectués par l’utilisateur Assane Faye dans l’agence dont le chef est moussa diop",
            "14":"□ 14: Pour lister la somme des parts de l’agence, de l'état et de l’état des transactions par date dans l’agence dont le numéro est 001",
            "15":"□ 15: Pour lister la somme des parts de l’agence et de l'état par agence durant deuxième de l’année 2021",
            "16":"□ 16: Pour lister l’agence qui a fait le plus de transfert durant le mois de Juin 2021",
            "17":"□ 17: Pour lister l’agence qui a fait le moins de transfert de dépôt le 10-08-2021",
            "18":"□ 18: Pour lister l’agence qui a fait le retrait le plus grand durant le mois de MAI 221",
            "19":"□ 19: Pour lister les agences qui n’ont pas fait de dépôt le 10-08-2021",
            "20":"□ 20: Pour lister les noms utilisés par l’agence numéro 001 durant le mois de MAI 221",
            "21":"□ 21: Pour lister le ou les clients qui ont effectué le dépôt le plus petit durant le mois de MAI 221",
            "22":"□ 22: Pour lister le ou les clients qui ont effectué le plus de dépôt durant le mois de MAI 221",
            "23":"□ 23: Pour lister les 5 agences qui ont effectué le plus de transactions durant l’année 2021",
            "24":"□ 24: Pour lister les 5 agences dont le montant gagné (somme des frais gagnés sur les transactions) sont les plus faibles en 2021.",
            "25":"□ 25: Pour lister l’utilisateur qui fait le plus de transfert dans l’agence dont le chef est moussa diop",
            "26":"□ Taper 'E' pour afficher les  resultats deja executes",
            "27":"□ Taper 'R' pour reafficher tout le Menu (execute ou non)",
            "28":"□ Taper 'Q' pour quitter",
    }


myallMenu = myMenuNumber.copy() # This will be used in order to dispaly the whole of the menu.




def menuFunc():
    """ Function that allows us to show
    an update menu"""    
    for row in myMenuNumber.values():
        print(row)