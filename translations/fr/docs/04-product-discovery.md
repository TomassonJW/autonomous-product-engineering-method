# Découverte produit

Dans cette méthode, la découverte produit part du langage courant, pas d'un formulaire d'intake corporate.

Le but est de comprendre ce que l'utilisateur demande vraiment, ce qu'il n'a pas encore dit, et ce qui rendrait le produit utile plutôt que simplement généré.

## Sorties de découverte

Une bonne passe de découverte produit produit :

- une intention produit reformulée ;
- les utilisateurs cibles et leurs niveaux de maturité ;
- les jobs principaux à accomplir ;
- le niveau d'ambition attendu ;
- les contraintes connues ;
- les non-objectifs ;
- les hypothèses cachées ;
- les risques probables ;
- les décisions manquantes ;
- la première tranche produit testable.

## Entrées en langage courant

Les utilisateurs peuvent dire :

- "Je veux un outil qui construit des apps pour moi."
- "Ça doit faire premium."
- "L'UI est mauvaise."
- "Je veux des réglages profonds, mais l'action principale doit rester simple."
- "Je veux qu'il fasse tout, pas une version jouet."

Le système ne doit pas punir l'imprécision. Il doit la traduire.

## Règles de découverte

1. Reformuler avant de structurer.
2. Séparer ce qui est explicite de ce qui est inféré.
3. Ne pas poser de questions qui ne changent pas le chemin de build.
4. Détecter tôt les écarts d'ambition.
5. Identifier la première tranche utile sans réduire la vision long terme.
6. Nommer les risques en langage clair.

## Exemple de traduction

Déclaration utilisateur :

> "Je veux un logiciel qui génère des jeux 3D."

Interprétations possibles :

- générateur de prototype à partir d'un prompt ;
- éditeur de niveaux ;
- plugin de moteur de jeu ;
- pipeline d'assets ;
- workflow de studio de jeu autonome ;
- operating system complet de production de jeux.

La découverte doit rendre cette ambiguïté visible avant qu'un worker construise une petite démo et l'appelle succès.

## Artefact de découverte

Utiliser [product-brief-template.md](../templates/product-brief-template.md) et [product-profiling-template.md](../templates/product-profiling-template.md) pour capturer le résultat.

L'artefact doit être assez court pour être lu vite, mais assez concret pour qu'un autre agent ou développeur puisse continuer sans contexte oral.
