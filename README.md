# Automatisation scan de vulnerabilites avec Nmap + OSINT avec OWASP

J'ai installé Kali linux pour pouvoir effectuer un script qui va nous permettre d'analyser les vulnérabilités : 
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


Qu'est ce que l'outil OWASP ?

L'outil OWASP Nettacker est créé pour automatiser la collecte d'informations, l'analyse des vulnérabilités et éventuellement générer un rapport pour les réseaux, y compris les services, les bogues, les vulnérabilités, les erreurs de configuration et d'autres informations. Ce logiciel utilisera TCP SYN, ACK, ICMP et de nombreux autres protocoles afin de détecter et de contourner les périphériques Firewall/IDS/IPS. En tirant parti d'une méthode unique dans OWASP Nettacker pour découvrir des services et des appareils protégés tels que SCADA. Cela ferait un avantage concurrentiel par rapport aux autres scanners, ce qui en ferait l'un des meilleurs.
