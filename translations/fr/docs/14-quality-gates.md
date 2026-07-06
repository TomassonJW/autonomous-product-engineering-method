# Gates qualité

Les gates qualité sont des contrats de revue. Ils empêchent les agents de déclarer un travail terminé avant qu'une preuve existe.

## Truth Gate

Échoue si :

- des données simulées sont présentées comme réelles ;
- une information inférée n'est pas marquée ;
- l'incertitude est cachée ;
- un badge de statut compresse des vérités incompatibles ;
- le système affirme la complétion sans preuve.

## Challenge Gate

Échoue si :

- un travail ambitieux ou ambigu démarre sans challenge ;
- les alternatives ne sont pas considérées ;
- coût et sécurité sont ignorés ;
- le système obéit à une instruction risquée sans limite.

## Dual UI Gate

Échoue si :

- les utilisateurs finaux doivent comprendre logs, workers ou pipelines ;
- les opérateurs ne peuvent pas inspecter vérité, coût ou échecs ;
- un écran mélange contrôles admin et workflows utilisateur finaux.

## User Simplicity Gate

Échoue si :

- l'action primaire n'est pas claire ;
- les réglages par défaut submergent l'utilisateur ;
- le wording utilise du jargon interne ;
- les options avancées sont visibles trop tôt.

## Journey Gate

Échoue si :

- la fonctionnalité est seulement un modèle de données, une route ou un écran ;
- aucun chemin de bout en bout n'existe ;
- le succès ne peut pas être observé par un utilisateur ou opérateur.

## Transversality Gate

Échoue si :

- la capacité est un silo ;
- les relations sont implicites ;
- événements et artefacts manquent ;
- le couplage direct remplace les contrats.

## Cost Gate

Échoue si :

- les actions coûteuses ne sont pas bornées ;
- les boucles répétées n'ont pas de condition d'arrêt ;
- le choix du modèle n'est pas justifié ;
- le coût est caché aux opérateurs.

## Safety Gate

Échoue si :

- des actions rouges peuvent se lancer sans approbation humaine explicite ;
- des secrets peuvent être lus, imprimés, commités ou exposés ;
- des systèmes externes sont modifiés sans autorisation ;
- aucun rollback n'existe pour les changements risqués.

## Product Honesty Gate

Échoue si :

- "premium" est affirmé sans preuve ;
- "done" signifie seulement généré ;
- "autonome" cache des besoins manuels ;
- les limites ne sont pas documentées.
