# Automatisation scan de vulnerabilites + Nmap

J'ai installé Kali linux pour pouvoir effectuer un script qui va nous permettre de scanner les ports de manière automatisé : 
J'ai crée un fichier que j'ai nommé nmap_port_scanner.py pour faire un script nmap. 

Tout d'abord qu'est ce que l'outil Nmap ? 

L'outil Nmap est un scanner de ports libre conçu pour détecter les ports ouverts, d'identifier les services hébergés et obtenir des informations sur le système d'exploitation d'un ordinateur distant. 
Cet outil est devenu une référence pour les administrateurs réseaux car l'audit des résultats de Nmap fournit des indications sur la sécurité d'un réseau. 

Voici les étapes que j'ai effectué pour effectuer un script nmap :

1 - création fichier python script nmap
2 - changement de droit (chmod) du fichier script python nmap
3 - lancement script nmap 

lancement commande manuellement : 
- sudo apt install python3-pip
- pip install python-nmap

lancement script nmap :
- python nmap_port_scanner.py


Installation de Nessus 

Qu'est ce que Nessus ? 

Nessus est le scanner de vulnérabilité réseaux de Tenable Network Security. Par rapport aux autres scanners de vulnérabilité, Nessus a la particularité d'être basé sur une architecture client/serveur et d'être compatible avec Windows et Linux. En plus, Nessus stocke et gère toutes ses failles de sécurité grâce à un système de plugins.

Nessus est un logiciel qui effectue de réelles attaques et présente le résultat de ces attaques sous forme de rapport. Son utilisation peut donc être à double tranchant. D'un côté, une équipe sécurité peut l'utiliser pour scanner son réseau dans le but de prévenir les intrusions et les dénis de service. D'un autre côté, un hacker peut l'utiliser à des fins malhonnêtes et en profiter pour exploiter les vulnérabilités déclarées.
