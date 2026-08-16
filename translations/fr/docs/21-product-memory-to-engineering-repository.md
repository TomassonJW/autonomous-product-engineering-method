# De la mémoire produit au dépôt d'ingénierie

Statut : extension canonique de la méthode  
Version : 0.3.0  
Public : product owners, architectes produit, architectes documentaires, coding agents, concepteurs de systèmes autonomes, reviewers et opérateurs d'ingénierie

Cette extension définit comment une mémoire produit riche devient un dépôt d'ingénierie versionné qu'un agent de développement autonome peut reprendre proprement.

Elle vise les produits durables, complexes ou répartis sur plusieurs sessions. Elle n'impose pas Notion : **espace de mémoire produit** désigne tout système durable utilisé pour les recherches, explorations, sources, décisions et définitions produit. GitHub sert ici d'exemple canonique de dépôt partagé et versionné.

## 1. Les quatre surfaces

| Surface | Responsabilité principale | Ne doit pas devenir |
| --- | --- | --- |
| Product owner | Intention, goût produit, arbitrages matériels, acceptation visible | Chef de projet technique quotidien |
| Architecte produit ou agent conversationnel | Découverte, challenge, mémoire structurée, compilation sémantique | Propriétaire permanent de l'implémentation |
| Espace de mémoire produit | Contexte riche, recherches, alternatives, sources, décisions, mémoire produit durable | Backlog d'ingénierie vivant ou contrat runtime implicite |
| Dépôt d'ingénierie | Constitution produit active, provenance, diffs, état d'ingénierie, code, tests et preuves | Miroir brut de la mémoire |
| Agent ou équipe de développement | Clone, Git opérationnel, architecture, planification, implémentation, tests, livraison et handoff | Auteur silencieux du produit |

Règle centrale :

> La mémoire peut être large et exploratoire. Le dépôt d'ingénierie doit être explicite, versionné, prêt à développer et lisible sans rouvrir toute la mémoire.

## 2. Flux canonique

```text
Exploration en langage courant
  -> mémoire produit riche
  -> gate Prêt à compiler
  -> compilation sémantique
  -> dépôt d'ingénierie versionné
  -> gate Prêt à développer
  -> reprise par l'agent de développement
  -> Git opérationnel, code, tests, livraison et apprentissage
```

Ce flux crée deux transitions volontaires au lieu d'un handoff vague.

### Transition A : Prêt à compiler

La définition active est assez cohérente pour être compilée sans inventer le produit.

### Transition B : Prêt à développer

Le dépôt contient un contrat produit, une provenance, des autorités et des gates suffisants pour qu'un agent commence sans accès aux conversations ou à la mémoire d'origine.

## 3. Mémoire produit

L'espace de mémoire peut contenir :

- langage brut de l'utilisateur ;
- recherches et documents sources ;
- interprétations produit concurrentes ou rejetées ;
- historique de raisonnement ;
- profilage produit ;
- vocabulaire métier ;
- workflows et parcours ;
- exploration UI/UX ;
- inventaires de données et d'intégrations ;
- contraintes juridiques, de sécurité, d'exploitation et économiques ;
- décisions, hypothèses, inconnues et contre-arguments ;
- sources sensibles qui ne doivent pas entrer dans un dépôt.

Il distingue au minimum :

- `[FACT]`
- `[DECISION]`
- `[HYPOTHESIS]`
- `[PROPOSAL]`
- `[UNKNOWN]`
- `[CONSTRAINT]`
- `[SOURCE]`

La mémoire peut être verbeuse. Sa fonction est la compréhension durable, pas l'exécution au minimum de tokens.

## 4. Gate Prêt à compiler

La gate ne passe que si la définition active rend sans ambiguïté :

- la finalité et la valeur ;
- le niveau d'ambition ;
- les utilisateurs, rôles et contextes critiques ;
- le vocabulaire, les objets, états et règles métier ;
- les parcours, outils, vues, actions et permissions ;
- l'UI/UX et les comportements d'acceptation lorsqu'une interface existe ;
- les sources de données, intégrations, propriétaires et sensibilités ;
- le périmètre, les non-objectifs, les phases et conditions de changement d'échelle ;
- les contraintes, coûts, risques et la réversibilité ;
- les décisions acceptées et alternatives rejetées ;
- les questions ouvertes classées bloquantes ou non bloquantes ;
- les gates produit, UX, techniques, de sécurité et d'acceptation humaine ;
- la visibilité du dépôt et la politique de redaction ;
- les versions de méthode et canons locaux à épingler.

La gate échoue si la compilation obligerait à :

- inventer une architecture produit ;
- masquer une contradiction matérielle ;
- transformer une hypothèse en décision ;
- réduire silencieusement l'ambition ;
- exporter des données privées ou secrètes inutiles ;
- choisir un dépôt public sans approbation explicite.

## 5. Compilation sémantique

La compilation sémantique n'est ni un export, ni un résumé libre, ni un copier-coller.

Le compilateur peut réorganiser et condenser, mais il préserve :

- l'intention ;
- les priorités ;
- les frontières de scope ;
- les alternatives rejetées qui contraignent encore le produit ;
- la propriété des décisions ;
- l'incertitude ;
- les preuves d'acceptation ;
- la traçabilité des sources.

Il exclut par défaut :

- transcriptions complètes des conversations ;
- notes dupliquées ;
- branches obsolètes sans valeur d'anti-référence ;
- secrets et credentials ;
- données personnelles inutiles ;
- sources sensibles non nécessaires à l'ingénierie ;
- gros snapshots bruts lorsqu'une source map vérifiable suffit.

Toute omission susceptible de changer l'interprétation est enregistrée dans la provenance.

## 6. Constitution par défaut du dépôt

Un dépôt peut commencer sans code applicatif. Le même dépôt reçoit ensuite le pilotage d'ingénierie, le code, les tests et les preuves de livraison.

```text
AGENTS.md
README.md
product/
  00-index.md
  vision-and-value.md
  users-and-journeys.md
  domain-and-rules.md
  product-experience.md
  data-and-integrations.md
  scope-and-risks.md
  decisions-and-unknowns.md
  acceptance-gates.md
  ui-contract.md              # seulement si une UI existe
provenance/
  COMPILATION-MANIFEST.yml
  SOURCE-MAP.md
  PRODUCT-CHANGELOG.md
```

Les noms sont des valeurs par défaut, pas une contrainte cosmétique. Les fonctions suivantes sont obligatoires :

1. contrat d'autorité et d'exploitation agentique ;
2. constitution produit active ;
3. décisions et inconnues ;
4. gates d'acceptation ;
5. provenance et mapping des sources ;
6. versions épinglées de la méthode et des canons locaux ;
7. commande explicite de démarrage pour l'agent de développement.

Après reprise, l'agent ajoute ou adapte :

- roadmap ;
- backlog ou board ;
- état courant ;
- décisions d'architecture ;
- handoff ;
- exploitation et rollback ;
- code, tests, migrations et assets de déploiement.

## 7. Manifeste de compilation

`COMPILATION-MANIFEST.yml` enregistre au minimum :

- projet et identifiant de contexte ;
- version de la mémoire produit ;
- date de compilation ;
- identité ou rôle du compilateur ;
- dépôt et branche cibles ;
- pages ou documents réellement lus ;
- fichiers compilés et leur fonction ;
- mapping source-vers-sortie ;
- éléments omis, redacted ou différés et leurs raisons ;
- faits, décisions, hypothèses et inconnues encore actifs ;
- versions épinglées de la méthode, de l'UI, de la sécurité et des canons locaux ;
- visibilité du dépôt ;
- résultat Prêt à compiler ;
- résultat Prêt à développer ;
- commit de baseline et tag éventuel.

Un snapshot brut de la mémoire est facultatif. Lorsqu'il existe pour audit ou recompilation, il reste en lecture seule et secondaire par rapport à la constitution sémantique.

## 8. Gate Prêt à développer

Le dépôt est prêt seulement si :

- il peut être compris sans l'espace de mémoire ;
- `AGENTS.md` définit autorités, responsabilité Git, gates, arrêts et reporting ;
- la constitution active est cohérente ;
- le manifeste et la source map sont complets ;
- les contradictions matérielles sont résolues ou explicitement bloquantes ;
- le contenu sensible est absent ;
- les versions de méthode et canons locaux sont épinglées ;
- un commit de baseline est identifiable ;
- la commande de démarrage existe ;
- la première preuve bornée est définie ;
- si une UI existe, le contrat UI local et la première gate visible sont explicites.

Le volume documentaire ne prouve pas la préparation. Un petit paquet cohérent peut passer. Un gros export brut peut échouer.

## 9. Reprise par l'agent de développement

L'agent doit :

1. cloner ou mettre à jour le dépôt sans détruire de travail local ;
2. vérifier branche, baseline et manifeste ;
3. lire `AGENTS.md`, le manifeste et toute la constitution ;
4. produire une carte de couverture avant l'implémentation ;
5. remonter seulement les contradictions matérielles ou autorités manquantes ;
6. créer ou mettre à jour planification, état, décisions et handoff ;
7. posséder le Git opérationnel et l'exécution d'ingénierie ;
8. préserver la constitution active ;
9. proposer explicitement les changements de fondation produit au lieu de la réécrire pour arranger l'implémentation ;
10. exécuter le préflight et la première preuve autorisée.

Les sessions ordinaires reprennent depuis Git, l'état et le handoff. Elles ne rouvrent pas la mémoire produit.

## 10. Responsabilité Git

### Architecte produit ou agent conversationnel

Peut :

- créer le dépôt documentaire initial ;
- compiler une baseline produit ;
- préparer des branches d'amendement ;
- ouvrir des pull requests avec des diffs produit ;
- revoir la réalisation par rapport à la constitution.

Ne devient pas le committer quotidien du code sans mission explicite.

### Agent de développement

Possède par défaut :

- clone local ;
- branches et worktrees ;
- commits d'implémentation ;
- intégration ;
- tags techniques ;
- tests et corrections CI ;
- rollback ;
- état et handoff.

### Product owner

Approuve les décisions matérielles de produit, sécurité, coût, données, publication et irréversibilité. Il n'a pas à manipuler Git.

## 11. Amendements

Un changement stratégique suit :

```text
Discussion produit
  -> mise à jour de la mémoire
  -> amendement versionné
  -> branche ou pull request
  -> diff produit lisible
  -> revue et décision
  -> merge
  -> analyse d'impact par l'agent de développement
```

Les découvertes d'ingénierie ordinaires restent dans le dépôt. Il n'existe pas de synchronisation bidirectionnelle continue générale entre mémoire et Git.

Une modification de mémoire n'est active qu'après compilation et merge.

## 12. Confidentialité et visibilité

- Les dépôts produit internes sont privés par défaut.
- Une publication publique exige approbation explicite et revue de redaction.
- Un dépôt de méthode ne peut être public que si exemples et sources sont sanitisés.
- Ne jamais copier secrets, credentials, données personnelles inutiles, transcriptions privées ou sources confidentielles dans un dépôt.
- Conserver une référence vers une source restreinte sans embarquer son contenu lorsque l'ingénierie n'a besoin que de la provenance.

## 13. Exception légère

Un flux prompt-vers-agent direct peut convenir à un spike jetable si tout est explicite :

- durée courte ;
- aucun effet production ou externe ;
- aucune donnée durable ;
- aucune propriété multi-session ;
- aucune attente de réutilisation ;
- destruction ou absorption prévue.

Dès que le travail devient durable, partagé, exploité, réglementé ou stratégique, il doit être compilé dans un dépôt d'ingénierie.

## 14. Anti-patterns

Rejeter :

- export brut présenté comme constitution ;
- dépôt de spécification jetable suivi d'un dépôt de code sans continuité ;
- synchronisation implicite continue entre mémoire et Git ;
- agent relisant toutes les notes historiques à chaque session ;
- architecte produit committant quotidiennement l'implémentation par défaut ;
- agent de développement modifiant silencieusement l'intention ;
- dépôt public choisi par commodité ;
- omissions non documentées ;
- préparation déduite du nombre de fichiers ;
- baseline sans version de méthode épinglée.

## 15. Checklists minimales

### Prêt à compiler

- interprétation active explicite ;
- scope, utilisateurs, domaine, parcours, données, risques et gates cohérents ;
- inconnues bloquantes résolues ou déclarées ;
- confidentialité décidée ;
- règles de redaction connues ;
- compilation possible sans invention.

### Prêt à développer

- constitution autonome ;
- provenance et source map présentes ;
- méthode et canons locaux épinglés ;
- autorités et propriété Git explicites ;
- commit de baseline existant ;
- première preuve bornée et arrêts définis ;
- reprise possible sans rouvrir la mémoire.

## 16. Relation avec le reste de la méthode

Cette extension se place entre stabilisation produit et exécution d'ingénierie.

Elle complète :

- [Couches produit-vers-ingénierie](07-product-to-engineering-layers.md) ;
- [Méthode autonome Vision-to-Product](20-autonomous-vision-to-product.md) ;
- [Gates qualité](14-quality-gates.md) ;
- [Adapter Hermes](../adapters/hermes.md) ;
- [Template de constitution du dépôt](../templates/engineering-repository-constitution-template.md) ;
- [Template de manifeste](../../../templates/source-compilation-manifest-template.yml) ;
- [Prompt de compilation](../prompts/starter-prompts/compile-product-memory-to-repository.md).

Distinction centrale :

> La mémoire produit maximise la compréhension. Le dépôt d'ingénierie maximise l'exécution explicite, versionnée et partagée.
