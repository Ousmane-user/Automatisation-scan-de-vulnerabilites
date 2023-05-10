#!/usr/bin/env python3
#Utilisez ces commandes dans Kali pour installer le logiciel requis
#  sudo apt install python3-pip
#  pip install python-nmap
# Importer nmap afin que nous puissions l'utiliser pour l'analyse
import nmap
# Nous devons créer des expressions régulières pour nous assurer que l'entrée est correctement formatée
import re
# Modèle d'expression régulière pour reconnaître les adresses IPv4.
ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
# Modèle d'expression régulière pour extraire le nombre de ports que vous souhaitez analyser.
# Spécification <lowest_port_number>-<highest_port_number> (ex 10-100)
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
# Initialiser les numéros de port, utilisera les variables plus tard.
port_min = 0
port_max = 65535
# Ce scanner de port utilise le module Python nmap.
# Vous devrez installer les éléments suivants pour le faire fonctionner sous Linux :
# Étape 1 : sudo apt install python3-pip
# Étape 2 : pip install python-nmap
# En-tête de l'interface utilisateur de base
print(r"VOUS SOUHAITEZ EFFECTUER UN SCAN COMPLETE DES PORTS ? ")
print("\n****************************************************************")
open_ports = []
# Demandez à l'utilisateur de saisir l'adresse IP qu'il souhaite analyser.
while True:
    ip_add_entered = input("\nVeuillez entrer l'adresse IP que vous souhaitez analyser : ")
    if ip_add_pattern.search(ip_add_entered):
        print(f"{ip_add_entered} est une adresse IP valide")
        break
while True:
    # Vous pouvez scanner 0-65535 ports. Ce scanner est basique et n'utilise pas le multithreading, donc la numérisation 
    # tous les ports ne sont pas conseillés.
    print("Veuillez saisir la plage de ports que vous souhaitez analyser au format : <int>-<int> (ex would be 60-120)")
    port_range = input("Saisissez la plage de ports :")
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break
nm = nmap.PortScanner()
# Nous parcourons tous les ports de la plage spécifiée.
for port in range(port_min, port_max + 1):
    try:
         
        # Il contient ce qui a été envoyé à la ligne de commande en plus du statut du port que nous recherchons. 
        # Pour nmap pour le port (num port) et l'ip 192.X.X.X, vous exécuterez : nmap -oX - -p (num port) -sV 192.X.X.X
        result = nm.scan(ip_add_entered, str(port))
        # Décommentez la ligne suivante et regardez le dictionnaire
        # print(result)
        # Nous extrayons le statut du port de l'objet retourné
        port_status = (result['scan'][ip_add_entered]['tcp'][port]['state'])
        print(f"Port {port} is {port_status}")
    except:
        # Nous ne pouvons pas analyser certains ports et cela garantit que le programme ne plante pas lorsque nous essayons de les analyser.
        print(f"Cannot scan port {port}.")
