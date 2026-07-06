# Profilage produit déductif

Le profilage produit déductif est le premier filtre fort de la méthode contre l'exécution superficielle.

Il transforme une intention brute en profil produit exploitable en inférant le sens probable, en détectant l'ambiguïté et en posant seulement des questions à forte valeur.

## Ce que le profileur doit détecter

Le profileur doit identifier :

- type de produit ;
- niveau d'ambition ;
- utilisateurs cibles ;
- plage de maturité des utilisateurs ;
- jobs centraux ;
- profondeur de workflow ;
- attentes d'autonomie ;
- attentes de qualité ;
- profondeur de configuration ;
- sensibilité sécurité ;
- sensibilité coût ;
- besoins d'intégration ;
- non-objectifs ;
- contradictions ;
- décisions manquantes.

## Échelle d'ambition

Utiliser cette échelle quand une demande peut être interprétée à différents niveaux :

1. Démo : prouve une idée.
2. Prototype : teste un concept.
3. Outil local : résout un problème étroit.
4. Produit utilisable : supporte un usage sérieux.
5. Produit premium : clair, robuste, soigné, profond.
6. Plateforme : plusieurs domaines connectés.
7. Système autonome : planifie, construit, teste, rapporte.
8. Usine autonome : produit des systèmes ou contenus de façon répétée.
9. Système niveau industrie : sécurité, échelle et gouvernance fortes.
10. Ambition monde ouvert : grand écosystème créatif ou opérationnel.

Si la déclaration utilisateur couvre des niveaux éloignés, le profileur doit s'arrêter et clarifier.

## Qualité des questions

Mauvaise question :

> "Quelle est votre audience cible ?"

Meilleure question :

> "Est-ce destiné à un débutant qui veut une action simple, à un expert qui veut tout contrôler, ou aux deux via des modes séparés ?"

Mauvaise question :

> "Quelles fonctionnalités voulez-vous ?"

Meilleure question :

> "Quand vous dites 'faire tout', le système doit-il seulement préparer un plan, générer des fichiers localement, ouvrir des pull requests, ou opérer un worker durable avec rapports et checkpoints ?"

## Sortie du profileur

Le profileur doit produire :

- une interprétation produit en un paragraphe ;
- les hypothèses explicites ;
- une carte d'ambiguïtés ;
- le niveau d'ambition avec raisonnement ;
- un aperçu des risques ;
- la profondeur de challenge recommandée ;
- quelques questions décisives ;
- la première tranche de build probable si les questions sont résolues.

## Condition d'arrêt

Ne pas laisser un agent de build avancer si la demande présente un fort écart d'ambition, un type d'utilisateur flou, des effets externes flous ou une zone de sécurité floue.
