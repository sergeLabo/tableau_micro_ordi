#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import csv



def improve_case(case):
    # Lien http, remplacé par Lien
    if "http://" in case or "https://" in case:
        # Si ' ' à la fin du lien
        if case[-1] == ' ':
            case = case[:-1]
        # Si " à la fin du lien
        if case[-1] == '"':
            case = case[:-1]

        case = "[" + case + " Lien]"

        ### Si " à la fin du lien
        ##if case[0] == '" ':
            ##case = case[2:]

    else:
        case = case.replace("-", " ", 3)
        case = case.replace("_", " ", 3)

    return case



csv_dir = os.getcwd()
csv_file = csv_dir + "/comparatif_carte_micro_processeur modif francois_V2.csv"

with open(csv_file, 'r') as f:
    csv_lines = f.read().splitlines()
f.close()

first = """=Tableau auto en python=
Ce tableau a été crée avec les infos de:
* [http://linuxgizmos.com/ringing-in-2016-with-64-open-spec-hacker-friendly-sbcs/ '''linuxgizmos.com''']


{|class="wikitable sortable" style="text-align:center; font-size: 50%;"
|+ Micro-Ordinateurs
"""

rows = csv.reader(csv_lines)

# ! Nom || Fabriquant || Site || Page produit || Processeur
# | A10-OlinuXino-Lime || Olimex, OlinuXino, Mouser  || https://www.

row_number = 0
corps =  """"""

for columns in rows:
    # Uniquement pour la 1ère ligne des titres
    row_number += 1
    if row_number == 1:
        new_line = "! "
        for i in range(len(columns)):
            new_line += columns[i] + "||"

    # Toutes les autres lignes
    else:
        corps += "|"
        new_line = ""
        for i in range(len(columns)):
            case = columns[i]
            # Amélioration de la case
            case = improve_case(case)
            # Ajout
            new_line += case + "||"

    # Dans tous les cas, suppression des ||| à la fin de la ligne
    # je boucle 12 fois, c'est bourrin, ça marche, TODO
    for test in range(12):
        if new_line[len(new_line) - 1] == "|":
            new_line = new_line[:-1]

    # Ajout d'une bonne nouvelle ligne
    corps += new_line + "\n" + "|-" + "\n"

# Pas de |- à dernière ligne
corps = corps[:-3]

tableau_end = "\n" + "|}"

all_lines = first + corps + tableau_end

print(all_lines)

sortie_file = csv_dir + "/sortie.txt"

with open(sortie_file, 'w') as f:
    f.write(all_lines)

f.close()
