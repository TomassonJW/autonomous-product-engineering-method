# Gouvernance des coûts et ressources

Le coût est une contrainte produit. Les systèmes autonomes échouent quand ils dépensent appels de modèles coûteux, runtime et attention humaine sans valeur visible.

Premium ne signifie pas maximal. Premium signifie utiliser la bonne profondeur pour la bonne tâche.

## Dimensions de coût

Chaque capacité et worker doit considérer :

- coût token ;
- coût modèle ;
- coût API ;
- runtime ;
- stockage ;
- appels réseau ;
- potentiel de cache ;
- risque de boucle répétée ;
- coût de revue humaine ;
- coût de maintenance ;
- coût d'opportunité ;
- valeur produite.

## Routage modèle

Utiliser l'option la moins chère qui reste fiable pour la tâche :

- scripts déterministes pour les vérifications mécaniques ;
- parsing local pour données structurées ;
- modèles plus petits pour brouillons et classification ;
- modèles plus forts pour raisonnement produit ambigu ;
- modèles plus forts pour revue finale de sécurité, architecture ou challenge ;
- approbation humaine pour actions rouges.

## Politique de budget

Une mission worker doit définir :

- cycles maximum ;
- runtime maximum ;
- appels externes maximum ;
- taille de contexte maximum ;
- classe de modèle autorisée ;
- politique de cache ;
- conditions d'arrêt ;
- conditions d'escalade.

## Cost Gate

Le Cost Gate échoue quand :

- une action coûteuse n'a pas de justification de valeur ;
- des retries continuent sans nouvelle preuve ;
- le contexte est chargé largement sans besoin ;
- un modèle fort est utilisé pour une tâche déterministe ;
- un worker ne peut pas expliquer le budget consommé ;
- un run cache les opérations liées au coût au Control Plane.

## Règle pratique

Si l'utilisateur serait surpris par le coût, la latence ou l'exécution répétée, le système doit le rendre visible avant de continuer.
