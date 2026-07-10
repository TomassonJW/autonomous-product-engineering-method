# Registre de risques

| Risque | Sévérité | Probabilité | Mitigation |
| --- | --- | --- | --- |
| L'agent sous-construit une demande ambitieuse | Haute | Haute | Profilage déductif et échelle d'ambition |
| L'agent surconstruit une demande simple | Moyenne | Moyenne | Première tranche utile et gate de challenge |
| Fausse UX premium | Haute | Moyenne | Dual UI, Truth Gate et Journey Gate |
| Exposition de secrets | Critique | Moyenne | `.gitignore`, scan secret, règles no-secret |
| Publication publique avec contenu privé | Critique | Faible | Workflow GitHub sûr et scan public-safe |
| Explosion des coûts | Haute | Moyenne | Cost Gate, politique de budget, exécution consciente des quotas |
| Faux succès de worker | Haute | Haute | Pattern superviseur et rapport final basé sur preuves |
| Documentation trop abstraite | Moyenne | Moyenne | Exemples, templates et checks opérationnels |
| Prompt donnant une autorité dangereuse | Haute | Moyenne | Limites de sécurité dans chaque prompt |
| Maillage de capacités sur-ingéniéré | Moyenne | Moyenne | Exiger un but opérationnel pour chaque relation |
| Gate de challenge bureaucratique | Moyenne | Moyenne | Adapter le niveau de challenge au risque de la tâche |
| Approbations humaines floues | Haute | Moyenne | Modèle d'actions verte/orange/rouge |
| Le profilage projet devient un profilage personnel clandestin | Critique | Faible | Limitation des finalités, consentement, correction, minimisation et frontière de profiling |
| L'exploration fonctionnelle ne sature jamais | Haute | Moyenne | Dispositions de curation, test de saturation et valeur de l'information |
| La fondation partagée dérive entre agents parallèles | Critique | Moyenne | Foundation Freeze versionnée, ownership isolé et propositions de changement |
| Une intégration avec fixture est présentée comme réelle | Haute | Haute | Vocabulaire des preuves et Integration Gate indépendante |
| Un pourcentage masque des dimensions faibles | Haute | Haute | Rapport pondéré par dimensions avec preuves, confiance et acceptation humaine |
| Un produit public est lancé sans obligations d'exploitation | Critique | Moyenne | Revue privé/interne/public, gates de release, rollback, monitoring et incidents |

## Risque ouvert

La méthode doit encore être validée sur plusieurs dépôts réels et outils agentiques. D'ici là, certains conseils peuvent être incomplets ou trop idéalisés.
