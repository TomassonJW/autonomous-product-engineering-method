# Modèle de sécurité et de risque

La méthode utilise un modèle de sécurité à trois zones.

Le but est de maximiser l'autonomie utile tout en évitant les dommages irréversibles, erreurs publiques, coûts cachés, expositions de secrets et dégâts en production.

## Actions vertes

Les actions vertes sont locales, réversibles, testables, à faible risque et sans effet externe.

Exemples :

- créer ou modifier une documentation locale ;
- ajouter un test local ;
- lancer un formatter local ;
- rédiger un rapport ;
- générer un template local ;
- préparer une commande dry-run ;
- inspecter des fichiers publics et sûrs.

Les actions vertes peuvent être autonomes si la mission les autorise.

## Actions orange

Les actions orange sont structurantes, coûteuses, ambiguës ou potentiellement impactantes.

Exemples :

- changer l'architecture ;
- introduire une nouvelle dépendance ;
- changer une API publique ;
- élargir les permissions d'un worker ;
- lancer des évaluations coûteuses ;
- préparer une publication ;
- changer roadmap ou scope produit.

Les actions orange exigent une proposition avant exécution.

## Actions rouges

Les actions rouges sont irréversibles, destructives, publiques, financières, liées aux secrets, liées à la production ou envoyant un message externe.

Exemples :

- supprimer des données ;
- publier à l'extérieur ;
- envoyer des emails ou messages ;
- dépenser de l'argent ;
- modifier la production ;
- exposer des services ;
- lire, imprimer, commiter ou faire tourner des secrets ;
- force push ;
- modifier des credentials ;
- exécuter des migrations irréversibles.

Les actions rouges exigent une approbation humaine explicite et des garde-fous observables.

## Gestion des secrets

Les agents ne doivent jamais demander aux utilisateurs de coller des secrets dans le chat.

Utiliser des flux d'authentification sûrs, variables d'environnement, stores de secrets locaux ou mécanismes d'authentification fournisseurs. Les exemples de documentation doivent utiliser seulement des placeholders.

## Rapport de risque

Pour les travaux orange et rouges, produire :

- description de l'action ;
- classe de risque ;
- dommage possible ;
- plan de rollback ou récupération ;
- approbation requise ;
- preuve de vérification ;
- conditions d'arrêt.
