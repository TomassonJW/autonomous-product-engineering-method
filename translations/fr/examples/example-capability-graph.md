# Exemple de graphe de capacités

## Produit

Constructeur de produit assisté par IA.

## Capacité : créer un brief produit

Entrées :

- déclaration utilisateur brute ;
- contexte existant optionnel.

Sorties :

- brief produit ;
- hypothèses ;
- questions décisives.

Artefacts :

- `product-brief.md`

Événements :

- `product.intent.received`
- `product.brief.created`

Coût :

- coût token faible à moyen ;
- cacheable quand l'entrée ne change pas.

Risques :

- sur-inférence ;
- sous-estimer l'ambition.

Peut déclencher :

- suggestion de rapport de challenge ;
- suggestion de mapping des couches produit.

Ne doit pas déclencher :

- génération de code ;
- publication GitHub ;
- exécution externe de worker.

Experience Plane :

- montre l'intention reformulée et les questions.

Control Plane :

- montre hypothèses, confiance, références source et version de prompt.
