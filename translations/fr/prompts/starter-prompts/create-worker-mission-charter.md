# Créer une charte de mission worker

## But

Transformer une demande de travail en mission de worker autonome bornée.

## Quand l'utiliser

Avant de lancer un run Codex, un worker Hermes, un agent CLI ou une automation longue.

## Sortie attendue

Charte de mission avec scope, budget, checkpoints, gates, conditions d'arrêt et exigences de rapport final.

## Prompt

```text
Crée une charte de mission worker pour cette demande.

Demande :
<coller la demande de travail>

Contexte :
<coller brief produit, issue ou notes de dépôt pertinentes>

Produis :
1. Objectif de mission.
2. Scope autorisé.
3. Hors scope.
4. Zone de sécurité.
5. Approbations requises.
6. Limites de budget.
7. Paquet de contexte.
8. Queue de travail.
9. Checkpoints.
10. Gates qualité.
11. Conditions d'arrêt.
12. Notes de rollback ou récupération.
13. Structure de rapport final.

Contraintes :
- N'autorise pas d'autonomie non bornée.
- Ne laisse pas le worker auto-certifier son succès final sans preuve.
- Ne permets pas d'action rouge sans approbation.

Limites de sécurité :
- Aucun secret dans la mission.
- Aucune action production, publique, financière, destructive ou de message externe sans approbation explicite.

Étape suivante :
Demande acceptation si la mission inclut des actions orange ou rouges. Sinon, fournis la charte prête à exécuter.
```
