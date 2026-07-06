# Graphe de capacités

Le graphe de capacités décrit comment les capacités produit se relient sans transformer le système en réseau emmêlé de dépendances directes.

## Ce qu'une capacité déclare

Chaque capacité doit déclarer :

- nom ;
- but ;
- utilisateurs ;
- entrées ;
- sorties ;
- artefacts ;
- événements émis ;
- événements consommés ;
- profil de coût ;
- profil de risque ;
- zone de sécurité ;
- contexte réutilisable ;
- domaines liés ;
- suggestions possibles ;
- triggers autorisés ;
- triggers interdits ;
- exposition dans l'Experience Plane ;
- exposition dans le Control Plane ;
- gates qualité.

## Exemple

```text
Capacité : Créer un brief produit

But :
Transformer une intention en langage courant en brief produit structuré.

Entrées :
- déclaration brute de l'utilisateur
- contexte produit existant optionnel
- niveau d'ambition souhaité si connu

Sorties :
- brief produit
- hypothèses
- questions décisives
- niveau de challenge recommandé

Artefacts :
- product-brief.md
- profiling-notes.md

Événements :
- product.intent.received
- product.profile.created

Profil de coût :
- coût token faible à moyen
- cacheable si l'intention source ne change pas

Risques :
- sur-inférence
- manquer une interprétation très ambitieuse

Ne doit pas déclencher :
- implémentation
- publication externe
- changements irréversibles

Experience Plane :
- montre l'intention reformulée et les questions

Control Plane :
- montre hypothèses, confiance, références source et trace de profilage
```

## Utilisation du graphe

Utiliser le graphe pour répondre :

- Que peut réutiliser cette capacité ?
- Que peut-elle déclencher ?
- Que ne doit-elle jamais déclencher ?
- Quel plan d'UI doit l'exposer ?
- Quel événement informe le reste du système qu'un changement a eu lieu ?
- Quels gates doivent réussir avant l'étape suivante ?

## Anti-pattern

Une capacité n'est pas complète si elle nomme seulement une fonctionnalité. Elle doit décrire comportement, limites, preuves, coût et relation au reste du produit.
