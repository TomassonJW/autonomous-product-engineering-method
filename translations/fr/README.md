# Autonomous Product Engineering Method

Méthode ouverte pour transformer des visions produit exprimées en langage courant en workflows d'ingénierie logicielle assistés par IA, sûrs, premium et autonomes.

Cette traduction française est maintenue officiellement. L'anglais reste la source canonique : en cas d'écart, se référer aux fichiers anglais et mettre cette traduction à jour.

Ce dépôt est la fondation publique de la **Méthode d'ingénierie produit autonome**. Elle aide une personne à exprimer une idée ambitieuse en langage courant, construire une mémoire produit durable, challenger et stabiliser le produit, compiler la définition active en dépôt d'ingénierie versionné, puis remettre ce dépôt à des coding agents, workers autonomes ou équipes humaines.

La méthode est indépendante d'un outil unique. Elle peut être adaptée à Codex, Hermes, des agents CLI, des chatbots, des systèmes multi-agents personnalisés ou des équipes humaines utilisant l'IA comme partenaire d'ingénierie produit.

## Ce que c'est

Ce dépôt contient documentation, templates et prompts. Il fournit :

- une méthode de transformation produit-vers-ingénierie ;
- des règles de mémoire produit et de handoff vers un dépôt ;
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

> « Je veux un outil qui construit des apps pour moi. »

ou :

> « L'UI fait pauvre. Je veux quelque chose de premium mais toujours puissant. »

La méthode force le système à traduire ce langage en :

- intention produit ;
- niveau d'ambition ;
- types d'utilisateurs ;
- non-objectifs ;
- risques ;
- couches produit ;
- implications UX ;
- contrats métier et données ;
- cartes de capacités ;
- gates d'acceptation ;
- autorités du dépôt ;
- missions de workers ;
- tests ;
- limites de coût ;
- plans d'exécution sûrs.

## Mémoire produit et dépôt d'ingénierie

Les produits complexes bénéficient de deux artefacts distincts :

- **La mémoire produit** maximise la compréhension. Elle peut contenir recherches, alternatives, sources, historique de raisonnement, références sensibles, décisions, hypothèses et contexte long terme.
- **Le dépôt d'ingénierie** maximise l'exécution explicite, versionnée et partagée. Il contient la constitution active, la provenance, les autorités, les gates, l'état d'ingénierie, le code, les tests et les preuves.

Pont canonique :

```text
Exploration en langage courant
  -> mémoire produit riche
  -> Prêt à compiler
  -> compilation sémantique
  -> dépôt d'ingénierie versionné
  -> Prêt à développer
  -> reprise par l'agent
  -> Git opérationnel, implémentation, livraison et apprentissage
```

Lire [De la mémoire produit au dépôt d'ingénierie](docs/21-product-memory-to-engineering-repository.md) pour le contrat complet.

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

- clarté, cohérence, fluidité et qualité UX à la Apple ;
- profondeur, configurabilité, contrôle et ouverture à la Windows.

Éviter les deux extrêmes : beau mais fermé et limité, ou puissant mais lourd et confus.

## Flux de méthode

```text
Langage courant
  -> Profilage produit
  -> Clarification et challenge
  -> Inférences projet traçables
  -> Exploration fonctionnelle
  -> Cartes produit et contrats
  -> Curation et verticales de falsification
  -> Foundation Freeze versionnée
  -> Baseline de mémoire produit
  -> Compilation du dépôt d'ingénierie
  -> Gate Prêt à développer
  -> Agents de développement isolés
  -> Intégration et gates indépendantes
  -> Livraison et exploitation supervisées
  -> Apprentissage et révision de la fondation
```

Le protocole produit complet est défini dans la [Méthode autonome Vision-to-Product](docs/20-autonomous-vision-to-product.md). La transition mémoire-vers-dépôt est définie dans [De la mémoire produit au dépôt d'ingénierie](docs/21-product-memory-to-engineering-repository.md).

## Commencer ici

1. Lire [Vue d'ensemble](docs/00-overview.md).
2. Lire [Principes fondamentaux](docs/02-core-principles.md).
3. Utiliser le [template de brief produit](templates/product-brief-template.md).
4. Lancer le [prompt d'architecte produit autonome](prompts/system-prompts/autonomous-product-architect.md).
5. Appliquer la [gate de challenge](docs/06-challenge-gate.md) avant de construire.
6. Pour un produit ambitieux, utiliser le [Vision-to-Product Control Pack](templates/vision-to-product-control-pack-template.md) et le [Vision-to-Product Orchestrator](prompts/system-prompts/vision-to-product-orchestrator.md).
7. Lorsque la mémoire est stable, utiliser le [template de constitution du dépôt](templates/engineering-repository-constitution-template.md) et le [prompt de compilation](prompts/starter-prompts/compile-product-memory-to-repository.md).
8. Utiliser les [gates qualité](docs/14-quality-gates.md) avant de déclarer quoi que ce soit terminé.

## Carte du dépôt

- [docs/](docs/00-overview.md) : méthode, principes, protocole Vision-to-Product, pont mémoire-produit, gates, runtime, risques et limites.
- [templates/](templates/product-brief-template.md) : artefacts produit, dépôt, manifeste et workers.
- [prompts/](prompts/README.md) : prompts pour découverte, compilation, agents et revues.
- [runbooks/](runbooks/setup-codex.md) : guides opérationnels.
- [adapters/](adapters/codex.md) : adaptations par outil, dont [Hermes](adapters/hermes.md).
- [examples/](examples/README.md) : exemples publics et sûrs.
- [case-studies/](case-studies/hermes-agency-os/README.md) : leçons sanitisées de Hermes Agency OS.
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

Les dépôts produit internes sont privés par défaut. Une publication publique exige approbation explicite et revue de redaction.

## Statut actuel

Ce dépôt est en **v0.3**, fondation publique enrichie. Il ajoute le contrat De la mémoire produit au dépôt d'ingénierie, une constitution de dépôt documentaire, un manifeste de compilation, un prompt opérationnel et un modèle de reprise Hermes actualisé.

La méthode doit encore être validée sur des produits, équipes, mémoires et environnements agentiques variés. Ce n'est pas un standard final, une certification, un framework ni une garantie d'autonomie sûre.

## Licence

MIT. Voir [LICENSE](../../LICENSE).

MIT a été choisi parce que ce dépôt contient des templates, prompts et extraits opérationnels réutilisables que les personnes doivent pouvoir copier, adapter et intégrer dans leurs workflows.
