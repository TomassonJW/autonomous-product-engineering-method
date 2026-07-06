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

## Risque ouvert

La méthode doit encore être validée sur plusieurs dépôts réels et outils agentiques. D'ici là, certains conseils peuvent être incomplets ou trop idéalisés.
