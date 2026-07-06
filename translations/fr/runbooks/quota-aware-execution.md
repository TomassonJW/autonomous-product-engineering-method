# Exécution consciente des quotas

Les runs autonomes doivent tenir compte des quotas, limites de débit, budgets et risques de boucles répétées.

## Politique de quota

Définir avant exécution :

- cycles maximum ;
- runtime maximum ;
- appels modèle maximum ;
- appels API externes maximum ;
- limites de retry ;
- règles de pause ;
- déclencheurs d'escalade.

## Détection de boucle répétée

Arrêter ou mettre en pause quand :

- la même erreur se répète ;
- aucune nouvelle preuve n'est produite ;
- les retries consomment du budget sans progrès ;
- le contexte grossit sans meilleures décisions ;
- le worker change de stratégie sans vérification.

## Routage conscient du coût

Préférer :

- checks locaux déterministes pour validation mécanique ;
- artefacts en cache quand les entrées n'ont pas changé ;
- modèles plus petits pour classification et brouillon ;
- revue plus forte seulement pour raisonnement à haut risque.

## Rapporter le coût

Un rapport de run doit inclure :

- appels modèle/API approximatifs ;
- checks coûteux ignorés ;
- utilisation du cache ;
- pauses quota ;
- dépassements ou alertes budget.

## Règle premium

Premium signifie bonne profondeur, pas dépense maximale.
