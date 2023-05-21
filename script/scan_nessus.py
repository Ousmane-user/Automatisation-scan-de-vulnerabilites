import nmap
import NessusRESTfulAPI

# Définir les adresses IP à scanner
target_ips = ["192.168.56.108", "192.168.56.107"]

# Configuration de Nessus
nessus_host = "https://localhost:8834"
nessus_user = "admin"
nessus_password = "password"
nessus_policy = "basic"

# Initialiser l'API Nessus
nessus_api = NessusRESTfulAPI.NessusAPI(nessus_host, nessus_user, nessus_password)

# Créer un scan Nessus avec la politique spécifiée
scan_id = nessus_api.create_scan(target_ips, nessus_policy)

# Lancer le scan Nmap
nmap_scanner = nmap.PortScanner()
for ip in target_ips:
    nmap_scanner.scan(ip)

# Analyser les résultats du scan Nmap et lancer une analyse de vulnérabilités pour chaque hôte
for ip in target_ips:
    host = nmap_scanner[ip]
    print("Analyzing vulnerabilities for " + ip)
    nessus_api.launch_scan(scan_id, host['addresses']['mac'], host['addresses']['ipv4'])

# Attendre que tous les scans Nessus soient terminés
nessus_api.wait_until_scan_finished(scan_id)

# Afficher les résultats des scans Nessus
for ip in target_ips:
    print("Results for " + ip + ":")
    report = nessus_api.get_scan_report(scan_id, ip)
    print(report)
