# Exemple de modèle de double UI

## Produit

Constructeur d'apps assisté par IA.

## Experience Plane

Utilisateur principal :

- fondateur, product owner ou créateur qui veut décrire une app.

Action principale :

> Décrivez le produit que vous voulez construire.

Vue par défaut :

- zone d'intention ;
- compréhension reformulée ;
- trois questions décisives ;
- bouton de démarrage du profilage ;
- réglages avancés repliés.

Caché par défaut :

- logs de workers ;
- compteurs de tokens ;
- état de queue ;
- traces brutes ;
- routage modèle ;
- internes Git.

## Control Plane

Utilisateur principal :

- développeur, opérateur, QA ou builder avancé.

Affiche :

- runs actifs ;
- artefacts ;
- résultats de gates ;
- checks échoués ;
- estimations de coût ;
- routage modèle ;
- demandes d'approbation ;
- notes de rollback.

## Test de gate

Un utilisateur non technique peut créer un brief produit sans comprendre les workers. Un opérateur peut auditer le run sans demander à l'utilisateur final des détails cachés.
