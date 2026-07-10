# Couches produit-vers-ingénierie

La méthode convertit l'intention utilisateur en logiciel par couches. Cela évite à l'agent de passer directement d'un désir vague au code.

## Chaîne de couches

```text
Intention brute
  -> Profil produit
  -> North Star
  -> Vision produit
  -> Principes et non-objectifs
  -> Carte des domaines
  -> Carte des capacités
  -> Modèle de double UI
  -> Parcours utilisateur
  -> Parcours de pilotage
  -> Direction UX/UI
  -> Architecture système
  -> Modèle de données
  -> Graphe de capacités
  -> Modèle d'événements
  -> Modèle d'artefacts
  -> Verticales de falsification
  -> Foundation Freeze
  -> Roadmap
  -> Portefeuille de missions de build
  -> DAG d'exécution
  -> Missions de workers
  -> Code
  -> Tests
  -> Intégration et acceptation indépendantes
  -> Release et exploitation supervisées
  -> Rapports de run et d'apprentissage
  -> Feedback humain
  -> Mises à jour ciblées des couches
```

## Pourquoi les couches comptent

Sans couches, les agents ont tendance à :

- coder trop tôt ;
- surinterpréter la première phrase ;
- manquer les implications UX ;
- construire des modules isolés ;
- oublier coûts et sécurité ;
- déclarer la complétion sans preuve produit.

Les couches rendent le raisonnement révisable.

## Routage du feedback

Le feedback doit mettre à jour la bonne couche.

Exemples :

- "C'est confus" peut affecter le wording UX, la navigation ou la séparation des deux UI.
- "Je veux que ce soit un vrai agency OS" peut affecter la North Star, les domaines et la roadmap.
- "Ne touche pas l'architecture" contraint la couche d'implémentation.
- "Rends-le moins cher" affecte le routage modèle, la politique de cache et les budgets workers.

## Discipline de couches

Ne pas réécrire la vision haute pour chaque petit commentaire.

Ne pas implémenter du code pour chaque ambition large.

Mapper le feedback, identifier les couches affectées et produire la plus petite mise à jour cohérente.

Les règles complètes de transition, incluant curation, Foundation Freeze, isolation des workers parallèles, états d'intégration et apprentissage post-livraison, sont définies dans la [Méthode autonome Vision-to-Product](20-autonomous-vision-to-product.md).
