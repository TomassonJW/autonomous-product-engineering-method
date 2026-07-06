# Alternatives

Cette méthode n'est pas la seule façon de structurer l'ingénierie produit agentique.

## Prototype lean d'abord

Construire immédiatement un petit prototype, puis apprendre par l'usage.

À choisir quand :

- le risque est faible ;
- le produit est simple ;
- la découverte est peu coûteuse ;
- aucun effet externe n'existe.

Arbitrage :

- peut sous-traduire l'ambition et créer un succès trompeur.

## Product Requirements Document traditionnel

Écrire un PRD complet avant l'exécution.

À choisir quand :

- les équipes ont besoin d'approbation formelle ;
- le scope est stable ;
- les parties prenantes exigent de la documentation.

Arbitrage :

- peut devenir lent et déconnecté des preuves d'implémentation.

## Architecture humaine d'abord

Un architecte définit le système avant d'impliquer les agents.

À choisir quand :

- le risque métier est élevé ;
- la sécurité ou la conformité compte ;
- l'autonomie agent n'est pas encore fiable.

Arbitrage :

- réduit la vitesse agentique et peut manquer les boucles de feedback en langage courant.

## Workflow agent spécifique à un outil

Utiliser le workflow natif d'un seul outil, par exemple un processus Codex-only ou Hermes-only.

À choisir quand :

- l'équipe utilise un seul environnement ;
- la portabilité n'est pas importante.

Arbitrage :

- crée du lock-in et peut cacher les concepts de méthode dans le comportement de l'outil.

## Pourquoi cette méthode existe

La Méthode d'ingénierie produit autonome vise une voie médiane : assez structurée pour éviter l'autonomie superficielle ou dangereuse, mais assez pratique pour soutenir une vraie exécution entre outils.
