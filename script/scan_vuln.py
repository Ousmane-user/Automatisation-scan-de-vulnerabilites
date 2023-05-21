import requests
import json

# Définition de la fonction pour générer le rapport
def generate_report(vulnerabilities):
    report = ""
    for vuln in vulnerabilities:
        report += "Vulnérabilité : {}\n".format(vuln['name'])
        report += "Description : {}\n".format(vuln['description'])
        report += "Gravité : {}\n".format(vuln['severity'])
        report += "Solution recommandée : {}\n".format(vuln['solution'])
        report += "\n"
    return report

# Liste de vulnérabilités (exemple)
vulnerabilities = [
    {
        'name': 'Injection SQL',
        'description': 'Permet à un attaquant d\'injecter du code SQL malveillant.',
        'severity': 'Élevée',
        'solution': 'Utiliser des requêtes paramétrées pour les interactions avec la base de données.'
    },
    {
        'name': 'Cross-Site Scripting (XSS)',
        'description': 'Permet à un attaquant d\'injecter du code JavaScript malveillant.',
        'severity': 'Moyenne',
        'solution': 'Valider et échapper correctement les entrées utilisateur.'
    },
    {
        'name': 'Authentification faible',
        'description': 'Utilisation de mots de passe faibles ou de mécanismes d\'authentification non sécurisés.',
        'severity': 'Haute',
        'solution': 'Utiliser des mots de passe forts et des mécanismes d\'authentification sécurisés.'
    }
]

# Génération du rapport
report = generate_report(vulnerabilities)

# Affichage du rapport
print(report)

# Enregistrement du rapport dans un fichier
with open('rapport_vulnerabilites.txt', 'w') as file:
    file.write(report)
