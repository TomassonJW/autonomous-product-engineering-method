# Leçons apprises

## Les scaffolds UI ne sont pas des produits

Un écran, une route ou un flow mock peut créer un sentiment de progrès sans livrer un vrai parcours. Le Journey Gate doit exiger une preuve de bout en bout.

## Le statut truth-safe compte

Le statut doit distinguer :

- généré ;
- testé ;
- échoué ;
- bloqué ;
- simulé ;
- approuvé ;
- publié.

Compresser ces états en "done" crée une fausse confiance.

## Les workers ont besoin de wrappers

Un worker peut exécuter un cycle, mais un wrapper ou superviseur doit faire respecter :

- quota ;
- conditions d'arrêt ;
- checkpoints ;
- format de rapport ;
- autorité finale.

## Le reporting est une fonctionnalité produit

Pour les runs longs, le reporting n'est pas un bonus. C'est ainsi que l'utilisateur sait si l'autonomie est utile, bloquée, coûteuse ou risquée.

## Le quota change l'autonomie

Un agent qui peut travailler dix minutes et un agent qui peut travailler des heures ont besoin de gouvernances différentes. L'exécution consciente des quotas évite la dégradation silencieuse.
