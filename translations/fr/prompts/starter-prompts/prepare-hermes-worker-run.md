# Préparer un run worker Hermes

## But

Préparer un run durable de style Hermes avec wrapper, checkpoints, conscience des quotas et reporting vrai.

## Quand l'utiliser

Avant de lancer ou superviser un workflow autonome Hermes.

## Sortie attendue

Mission worker, exigences wrapper, fichiers de statut, checkpoints, politique de quota et contrat de rapport.

## Prompt

```text
Prépare un run worker Hermes avec la Méthode d'ingénierie produit autonome.

Mission :
<coller la mission>

Contexte :
<coller le contexte projet sanitizé>

Produis :
1. Objectif du worker.
2. Golden path.
3. Responsabilités du wrapper.
4. Politique de queue.
5. Checkpoints.
6. Contrat de fichier de statut.
7. Contrat de logs et de rapport.
8. Politique de quota et pause.
9. Conditions d'arrêt.
10. Détection de faux succès.
11. Stratégie Telegram ou notification si disponible.
12. Points d'approbation humaine.

Contraintes :
- Ne laisse pas le worker être l'autorité finale sur la complétion.
- Ne cache pas les cycles échoués.
- Ne lance pas de boucles coûteuses sans politique de budget.

Limites de sécurité :
- Pas de credentials dans les prompts ou rapports.
- Les actions rouges exigent une approbation explicite.
- Le reporting public doit être sanitizé.

Étape suivante :
Retourne une charte de mission prête pour run et liste les décisions humaines requises.
```
