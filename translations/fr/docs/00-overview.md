# Vue d'ensemble

La Méthode d'ingénierie produit autonome transforme une intention produit exprimée en langage courant en travail d'ingénierie logicielle structuré, révisable et assisté par agents.

Elle existe parce que les utilisateurs ambitieux décrivent souvent leurs visions produit avec des mots imprécis, tandis que les agents IA exécutent trop littéralement. Le résultat peut être une démo superficielle alors que l'utilisateur attendait un produit sérieux, ou un système surconstruit alors qu'il fallait seulement un workflow ciblé.

La méthode ajoute une couche disciplinée de traduction entre l'intention humaine et l'exécution autonome.

## Ce que fait la méthode

La méthode aide un agent ou une équipe à :

1. comprendre l'intention réelle de l'utilisateur ;
2. détecter les écarts d'ambition et les ambiguïtés ;
3. challenger l'idée avant de construire ;
4. découper le produit en couches cohérentes ;
5. séparer l'expérience utilisateur des opérations de pilotage ;
6. modéliser les capacités comme unités réutilisables et connectées ;
7. définir événements, artefacts, coûts, risques et permissions ;
8. créer des missions de workers bornées ;
9. stabiliser des fondations versionnées avant le build parallèle ;
10. intégrer et vérifier indépendamment les résultats des workers ;
11. préparer une livraison et une exploitation supervisées ;
12. intégrer le feedback sans réécrire toute la vision.

## Ce que la méthode ne fait pas

Elle ne garantit pas :

- l'adéquation produit-marché ;
- la sécurité automatique de l'autonomie ;
- le remplacement de l'expertise métier ;
- la suppression du besoin de tests ;
- la transformation automatique de toute idée vague en plateforme complète ;
- la preuve qu'un produit est premium sans preuve utilisateur.

## Pour qui

La méthode est utile pour :

- des fondateurs qui décrivent des outils ambitieux ;
- des architectes produit qui transforment une vision en couches ;
- des coding agents qui préparent des plans de build ;
- des documentalistes projet qui créent une mémoire réutilisable ;
- des opérateurs qui supervisent des workers autonomes ;
- des équipes qui veulent de la vitesse agentique sans chaos caché.

## Contrat central

L'utilisateur peut parler naturellement.

Le système doit répondre avec une vérité produit structurée.

Cela signifie que l'agent doit :

- reformuler ce qu'il a compris ;
- marquer les hypothèses comme hypothèses ;
- poser seulement les questions qui changent la trajectoire ;
- challenger les risques cachés ;
- définir le bon niveau de scope ;
- éviter les faux succès ;
- rapporter ce qui est fait, fragile, simulé ou bloqué.

## Flux de base

```text
Intention utilisateur
  -> Profil produit
  -> Challenge et interprétations concurrentes
  -> Inférences traçables
  -> Exploration fonctionnelle
  -> Cartes produit et contrats
  -> Fondation curée
  -> Verticales de falsification
  -> Foundation Freeze
  -> Portefeuille de missions de build
  -> Workers isolés
  -> Intégration et acceptation indépendantes
  -> Release supervisée
  -> Apprentissage opérationnel
```

## Première utilisation

Commencer avec [product-brief-template.md](../templates/product-brief-template.md), puis utiliser [deductive-product-profiler.md](../prompts/system-prompts/deductive-product-profiler.md). Pour un produit ambitieux, poursuivre avec la [Méthode autonome Vision-to-Product](20-autonomous-vision-to-product.md) et son [Control Pack](../templates/vision-to-product-control-pack-template.md). Ne pas commencer à coder tant que le gate de challenge n'a pas réussi ou produit une verticale de falsification bornée et acceptée.
