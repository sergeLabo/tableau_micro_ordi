#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import csv


csv_dir = os.getcwd()
csv_file = csv_dir + "/comparatif_carte_micro_processeur.csv"

with open(csv_file, 'r') as f:
    csv_lines = f.read().splitlines()
f.close()

first = """Ce tableau a été crée avec les infos de: [http://linuxgizmos.com/ringing-in-2016-with-64-open-spec-hacker-friendly-sbcs/ linuxgizmos.com]


{|class="wikitable sortable" style="text-align:center;"
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
            # Lien http, remplacé par Lien
            if "http://" in case or "https://" in case:
                case = "[" + case + " Lien]"
            # Ajout
            new_line += case + "||"

    # Dans tous les cas, suppression des ||| à la fin de la ligne
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
