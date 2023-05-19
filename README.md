# Automatisation-scan-de-vulnerabilites avec Nmap et Nessus

J'ai installé 3 VM (Ubuntu et Windows Server 2019) dont un Kali linux pour pouvoir effectuer un script qui va nous permettre d'analyser les vulnérabilités : 
Après avoir crée ces vm, dans kali linux j'ai crée un fichier que j'ai nommé nmap_port_scanner.py pour faire un script nmap. 

Tout d'abord qu'est ce que l'outil Nmap ? 
L'outil Nmap est un scanner de ports libre conçu pour détecter les ports ouverts, d'identifier les services hébergés et obtenir des informations sur le système d'exploitation d'un ordinateur distant. 
Cet outil est devenu une référence pour les administrateurs réseaux car l'audit des résultats de Nmap fournit des indications sur la sécurtié d'un réseau. 

Voici les étapes que j'ai effectué pour effectuer un script nmap :

1 - création fichier python script nmap
2 - changement de droit (chmod) du fichier script python nmap
3 - lancement script nmap 

lancement commande manuellement : 
- sudo apt install python3-pip
- pip install python-nmap

lancement script nmap :
- python nmap_port_scanner.py
