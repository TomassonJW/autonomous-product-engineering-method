# Bootstrap d'un projet existant

## But

Appliquer la méthode à un projet qui possède déjà du code, des docs ou une architecture partielle.

## Quand l'utiliser

Avant de restructurer ou étendre un dépôt existant.

## Sortie attendue

Carte de l'état actuel, écarts, risques, alignement avec la méthode et prochaines étapes bornées.

## Prompt

```text
Je veux appliquer la Méthode d'ingénierie produit autonome à un projet existant.

Commence par inspecter les fichiers publics et sûrs disponibles. Ne lis pas les secrets, credentials, logs privés, profils locaux, fichiers .env, fichiers auth ou vaults.

Produis :
1. Interprétation produit actuelle.
2. Carte de documentation existante.
3. Carte de capacités existante si elle peut être inférée.
4. Statut du modèle de double UI.
5. Risques sécurité et coût.
6. Artefacts manquants.
7. Écarts de gates qualité.
8. Première amélioration bornée recommandée.

Contraintes :
- Ne réécris pas encore le projet.
- Ne change pas l'architecture sans proposer une ADR.
- Ne suppose pas que des scaffolds générés valent de vrais parcours produit.

Limites de sécurité :
- N'imprime jamais de secrets.
- Traite publication, suppression, changements production et messages externes comme actions rouges.

Étape suivante :
Recommande le plus petit artefact documentaire ou de planification nécessaire avant l'implémentation.
```
