# Autonomous Product Engineering Method

Méthode ouverte pour transformer des visions produit exprimées en langage courant en workflows d'ingénierie logicielle assistés par IA, sûrs, premium et autonomes.

Cette traduction française est maintenue officiellement. L'anglais reste la source canonique : en cas d'écart, se référer aux fichiers anglais et mettre cette traduction à jour.

Ce dépôt est la fondation publique initiale de la **Méthode d'ingénierie produit autonome**. Elle aide une personne à exprimer une idée produit ambitieuse en langage courant, puis guide des agents IA, coding agents ou workers autonomes à travers le profilage produit, le challenge, l'architecture, la modélisation UX/UI, la cartographie des capacités, les gates de sécurité, la gouvernance des coûts, l'exécution, les tests, le reporting et l'intégration du feedback.

La méthode est indépendante d'un outil unique. Elle peut être adaptée à Codex, Hermes, des agents CLI, des chatbots, des systèmes multi-agents personnalisés ou des équipes humaines utilisant l'IA comme partenaire d'ingénierie produit.

## Ce que c'est

Ce dépôt contient de la documentation et des prompts. Il fournit :

- une méthode de transformation produit-vers-ingénierie ;
- des templates réutilisables ;
- des prompts copy-pasteables ;
- des gates de sécurité et de qualité ;
- des runbooks pour workers autonomes ;
- des adapters pour environnements agentiques courants ;
- un cas d'étude sanitizé ;
- des auto-audits et risques connus.

Ce n'est **pas** une promesse d'automatisation magique. La méthode ne supprime pas le besoin de jugement, de tests, de goût produit, de revue sécurité ou d'approbation humaine pour les actions dangereuses.

## Idée centrale

Les utilisateurs ne devraient pas être obligés de parler comme des product managers, architectes logiciels, chercheurs UX ou ingénieurs DevOps.

Ils peuvent dire :

> "Je veux un outil qui construit des apps pour moi."

ou :

> "L'UI fait pauvre. Je veux quelque chose de premium mais toujours puissant."

La méthode force le système à traduire ce langage en :

- intention produit ;
- niveau d'ambition ;
- types d'utilisateurs ;
- non-objectifs ;
- risques ;
- couches produit ;
- implications UX ;
- implications d'architecture ;
- cartes de capacités ;
- missions de workers ;
- tests ;
- gates qualité ;
- limites de coût ;
- plans d'exécution sûrs.

## Premium signifie clarté, pas décoration

Dans cette méthode, **premium** ne signifie pas design ornemental, polish vague ou modèles coûteux partout.

Premium signifie :

- clarté immédiate ;
- faible charge cognitive ;
- comportement fiable ;
- statut honnête ;
- incertitude visible ;
- pas de coût caché ;
- bons réglages par défaut ;
- profondeur de configuration quand elle est utile ;
- automatisation puissante mais sûre ;
- parcours testables ;
- confiance utilisateur.

La cible est le meilleur de deux mondes :

- une clarté, une cohérence, une fluidité et une qualité UX à la Apple ;
- une profondeur, une configurabilité, un contrôle et une ouverture à la Windows.

Il faut éviter les deux extrêmes : beau mais fermé et limité, ou puissant mais lourd, confus et cognitivement coûteux.

## Flux de méthode

```text
Langage courant
  -> Profilage produit
  -> Calibration de l'ambition
  -> Gate de challenge
  -> North Star et couches produit
  -> Cartes de domaines et de capacités
  -> Modèle de double UI
  -> Architecture et modèle événements/artefacts
  -> Politiques de coût et de sécurité
  -> Chartes de mission des workers
  -> Plan d'implémentation
  -> Tests et gates qualité
  -> Rapports de run
  -> Intégration du feedback
```

## Commencer ici

1. Lire [Vue d'ensemble](docs/00-overview.md).
2. Lire [Principes fondamentaux](docs/02-core-principles.md).
3. Utiliser le [template de brief produit](templates/product-brief-template.md).
4. Lancer le [prompt d'architecte produit autonome](prompts/system-prompts/autonomous-product-architect.md).
5. Appliquer le [gate de challenge](docs/06-challenge-gate.md) avant de construire.
6. Utiliser les [gates qualité](docs/14-quality-gates.md) avant de déclarer quoi que ce soit terminé.

## Carte du dépôt

- [docs/](docs/00-overview.md) : méthode, principes, gates, runtime, risques et limites.
- [templates/](templates/product-brief-template.md) : artefacts structurés réutilisables.
- [prompts/](prompts/README.md) : prompts copy-pasteables pour agents et revues.
- [runbooks/](runbooks/setup-codex.md) : guides opérationnels pour environnements courants.
- [adapters/](adapters/codex.md) : notes d'adaptation par outil.
- [examples/](examples/README.md) : exemples publics et sûrs.
- [case-studies/](case-studies/hermes-agency-os/README.md) : leçons sanitizées de Hermes Agency OS.
- [audits/](audits/method-self-audit.md) : auto-critique, registre de risques, anti-patterns et alternatives.

## Traductions

- [Politique de traduction](../../TRANSLATION_POLICY.md)
- [Glossaire français](GLOSSARY.md)
- [Statut de traduction](TRANSLATION_STATUS.md)

## Position de sécurité

La méthode sépare les actions en trois zones :

- **Verte** : locale, réversible, testable, faible risque, sans effet externe.
- **Orange** : structurante, coûteuse, impactante ou ambiguë ; nécessite une proposition avant exécution.
- **Rouge** : irréversible, destructive, publique, financière, liée aux secrets, liée à la production ou envoyant un message externe ; nécessite une approbation humaine explicite.

Aucun agent ne devrait publier, supprimer, dépenser de l'argent, exposer des services, envoyer des messages, modifier la production ou manipuler des secrets sans autorisation explicite et garde-fous vérifiables.

## Statut actuel

Ce dépôt est en **v0.1**, fondation publique initiale. Il doit être utilisé, challengé et amélioré. Ce n'est pas un standard final, une certification, un framework ni une garantie d'autonomie sûre.

## Licence

MIT. Voir [LICENSE](../../LICENSE).

MIT a été choisi parce que ce dépôt contient des templates, prompts et extraits opérationnels réutilisables que les personnes doivent pouvoir copier, adapter et intégrer dans leurs propres workflows. Une licence Creative Commons pourra être étudiée plus tard si le projet devient principalement documentaire.
