# Adapter Codex

Codex est adapté au travail d'ingénierie local dans un dépôt : lire des fichiers, modifier code ou docs, lancer des tests, inspecter les diffs et produire des rapports finaux.

## Forces

- Conscience du dépôt local.
- Éditions par patch.
- Exécution de tests.
- Revue de statut Git et diff.
- Bon fit pour documentation, code et refactors structurés.

## Risques

- Lire trop largement.
- Coder avant de comprendre les patterns locaux.
- Écraser des changements utilisateur.
- Traiter du code généré comme vérifié.
- Lancer des commandes avec effets externes cachés.

## Adaptation de la méthode

Utiliser cette séquence :

1. Inspecter tâche et statut du dépôt.
2. Lire les docs et fichiers pertinents.
3. Identifier la zone de sécurité.
4. Planifier le travail non trivial.
5. Implémenter de petits changements.
6. Ajouter tests ou checks.
7. Lancer la vérification.
8. Relire le diff.
9. Rapporter fichiers, décisions, tests, limites, risques et prochaine action.

## Limites requises

- Pas de secrets.
- Pas de force push.
- Pas d'actions destructives sans approbation explicite.
- Pas de changement d'architecture sans ADR ou décision acceptée.
- Pas de "done" final sans preuve.

## Prompt utile

Utiliser [prepare-codex-build-plan.md](../prompts/starter-prompts/prepare-codex-build-plan.md).
