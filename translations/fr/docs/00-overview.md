# Vue d'ensemble

La Méthode d'ingénierie produit autonome transforme une intention exprimée en langage courant en travail d'ingénierie logicielle structuré, révisable et assisté par agents.

Elle existe parce que les utilisateurs ambitieux décrivent souvent leur vision avec des mots imprécis, tandis que les agents IA exécutent trop littéralement. Le résultat peut être une démo superficielle alors qu'un produit sérieux était attendu, ou un système surconstruit alors qu'il fallait un workflow ciblé.

La méthode ajoute une couche disciplinée de traduction entre intention humaine, mémoire produit durable, contrats d'ingénierie versionnés et exécution autonome.

## Ce que fait la méthode

Elle aide un agent ou une équipe à :

1. comprendre l'intention réelle ;
2. détecter écarts d'ambition et ambiguïtés ;
3. challenger l'idée avant de construire ;
4. séparer faits, décisions, hypothèses, propositions et inconnues ;
5. découper le produit en couches cohérentes ;
6. séparer expérience utilisateur et opérations de pilotage ;
7. modéliser domaines, capacités, objets, états, événements, artefacts, coûts, risques et permissions ;
8. stabiliser des fondations versionnées ;
9. conserver une mémoire produit riche sans obliger chaque session de développement à tout relire ;
10. compiler la définition active en dépôt Prêt à développer ;
11. créer des missions de workers bornées ;
12. intégrer et vérifier indépendamment les résultats ;
13. préparer livraison et exploitation supervisées ;
14. intégrer le feedback sans réécrire silencieusement toute la vision.

## Ce que la méthode ne fait pas

Elle ne garantit pas :

- l'adéquation produit-marché ;
- la sécurité automatique de l'autonomie ;
- le remplacement de l'expertise métier ;
- la suppression du besoin de tests ;
- la transformation automatique de toute idée vague en plateforme complète ;
- la preuve qu'un produit est premium sans preuve utilisateur ;
- qu'un export documentaire brut est un contrat d'ingénierie ;
- qu'un agent possède une autorité seulement parce qu'il accède à un dépôt.

## Pour qui

La méthode est utile pour :

- fondateurs décrivant des outils ambitieux ;
- architectes produit transformant une vision en couches ;
- coding agents préparant des plans de build ;
- architectes documentaires créant une mémoire réutilisable ;
- équipes compilant des définitions produit en dépôts d'ingénierie ;
- opérateurs supervisant des workers autonomes ;
- équipes cherchant la vitesse agentique sans chaos caché.

## Contrat central

L'utilisateur peut parler naturellement.

Le système doit répondre avec une vérité produit structurée.

L'agent doit :

- reformuler ce qu'il a compris ;
- marquer les hypothèses comme hypothèses ;
- poser seulement les questions qui changent la trajectoire ;
- challenger les risques cachés ;
- définir le bon niveau de scope ;
- éviter les faux succès ;
- rapporter ce qui est fait, fragile, simulé ou bloqué ;
- préserver la provenance lors du passage de la mémoire à l'exécution ;
- distinguer acceptation produit et réussite technique.

## Deux artefacts complémentaires

### Mémoire produit

Elle maximise la compréhension : recherches, alternatives, sources, historique, références sensibles, décisions, hypothèses et contexte long terme.

### Dépôt d'ingénierie

Il maximise l'exécution explicite, versionnée et partagée : constitution active, provenance, autorités, gates, état d'ingénierie, code, tests et preuves.

Le dépôt n'est pas un dump de la mémoire. C'est une compilation sémantique de la définition active.

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
  -> Baseline de mémoire produit
  -> Prêt à compiler
  -> Compilation du dépôt d'ingénierie
  -> Prêt à développer
  -> Workers isolés
  -> Intégration et acceptation indépendantes
  -> Release supervisée
  -> Apprentissage opérationnel
```

## Bascules d'autorité

1. Avant compilation, la version approuvée de la mémoire fait autorité pour la définition à compiler.
2. Après la baseline Prêt à développer, le dépôt fait autorité pour le contrat produit actif.
3. Pendant l'exploitation, code, tests, données, services et preuves runtime déterminent ce qui fonctionne réellement.
4. L'intention ne doit pas être réécrite silencieusement pour arranger l'implémentation.
5. Une modification de mémoire n'est active qu'après compilation et merge.

## Première utilisation

Commencer avec [product-brief-template.md](../templates/product-brief-template.md), puis utiliser [deductive-product-profiler.md](../prompts/system-prompts/deductive-product-profiler.md). Pour un produit ambitieux, poursuivre avec la [Méthode autonome Vision-to-Product](20-autonomous-vision-to-product.md) et son [Control Pack](../templates/vision-to-product-control-pack-template.md).

Lorsque la mémoire active est cohérente, utiliser [De la mémoire produit au dépôt d'ingénierie](21-product-memory-to-engineering-repository.md), le [template de constitution du dépôt](../templates/engineering-repository-constitution-template.md) et le [prompt de compilation](../prompts/starter-prompts/compile-product-memory-to-repository.md).

Ne pas commencer à coder tant que la gate de challenge et la gate Prêt à développer n'ont pas passé, sauf verticale de falsification explicitement bornée et approuvée.
