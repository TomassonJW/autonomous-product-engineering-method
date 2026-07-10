# Méthode autonome Vision-to-Product

Statut : extension canonique de la méthode
Version : 0.2.0
Public : responsables produit, architectes produit, responsables ingénierie, concepteurs de systèmes agentiques, reviewers et opérateurs

La méthode autonome Vision-to-Product définit comment une équipe assistée par des agents peut transformer une vision initiale en un produit explicite, contestable, versionné, constructible par incréments, vérifié indépendamment et préparé pour une exploitation supervisée.

Elle relie les pratiques existantes du dépôt sur le profilage, le challenge, la modélisation produit, les workers, la sécurité, les coûts, les tests et le feedback dans un protocole opératoire de bout en bout. Elle ne remplace pas ces pratiques. Elle définit quand les utiliser, ce qu'elles doivent produire et quelles gates empêchent une progression prématurée.

## Sommaire

1. [Définition, finalité et frontières](#1-définition-finalité-et-frontières)
2. [Les cinq mouvements](#2-les-cinq-mouvements)
3. [Maturité de la vision](#3-maturité-de-la-vision)
4. [Amorçage humain](#4-amorçage-humain)
5. [Passage à une autonomie bornée](#5-passage-à-une-autonomie-bornée)
6. [Boucle d'inférence projet](#6-boucle-dinférence-projet)
7. [Exploration fonctionnelle](#7-exploration-fonctionnelle)
8. [Cartographie du produit](#8-cartographie-du-produit)
9. [Curation et saturation](#9-curation-et-saturation)
10. [Foundation Freeze](#10-foundation-freeze)
11. [Roadmap et portefeuille de missions de build](#11-roadmap-et-portefeuille-de-missions-de-build)
12. [Agents de développement parallèles](#12-agents-de-développement-parallèles)
13. [Cycle d'ingénierie de bout en bout](#13-cycle-dingénierie-de-bout-en-bout)
14. [Intégration et vérification](#14-intégration-et-vérification)
15. [Gates humaines et niveaux d'autonomie](#15-gates-humaines-et-niveaux-dautonomie)
16. [Sécurité et Privacy by Design](#16-sécurité-et-privacy-by-design)
17. [Produits privés, internes et publics](#17-produits-privés-internes-et-publics)
18. [Workers autonomes durables](#18-workers-autonomes-durables)
19. [Gouvernance des modèles](#19-gouvernance-des-modèles)
20. [Complétude sans théâtre de la complétude](#20-complétude-sans-théâtre-de-la-complétude)
21. [Sources de vérité et adaptation des artefacts](#21-sources-de-vérité-et-adaptation-des-artefacts)
22. [Acceptation indépendante](#22-acceptation-indépendante)
23. [Boucle d'apprentissage post-livraison](#23-boucle-dapprentissage-post-livraison)
24. [Catalogue des anti-patterns](#24-catalogue-des-anti-patterns)
25. [Exemple canonique et checklists finales](#25-exemple-canonique-et-checklists-finales)

## 1. Définition, finalité et frontières

### 1.1 Définition

Vision-to-Product est un processus de transformation gouverné :

```text
Vision initiale
  -> profilage du projet
  -> clarification et challenge
  -> inférences traçables
  -> exploration fonctionnelle
  -> cartes produit et contrats
  -> fondation curée
  -> verticales de falsification
  -> Foundation Freeze versionnée
  -> portefeuille de missions de build
  -> agents de développement isolés
  -> intégration et gates indépendantes
  -> livraison supervisée
  -> exploitation, apprentissage et révision
```

La règle centrale est :

> L'agent autonome ne code pas la première formulation d'une demande. Il transforme d'abord la vision en un modèle produit explicite, falsifiable et versionné. Il teste ensuite ce modèle au moyen de verticales fonctionnelles, stabilise une fondation et coordonne le développement sans perdre l'intention initiale.

### 1.2 Finalité

La méthode vise à répondre à cinq questions difficiles :

- Que veut réellement l'utilisateur, y compris ce qui reste incertain ?
- Quelles interprétations du produit faut-il explorer avant d'en sélectionner une ?
- Quels concepts sont assez stables pour devenir des contrats ?
- Comment plusieurs workers peuvent-ils construire sans fragmenter le produit ?
- Quelles preuves justifient le passage d'un modèle à un produit réel et exploité ?

### 1.3 Frontières

Cette méthode :

- soutient la compréhension du produit et du projet, pas le profilage comportemental clandestin ;
- structure les décisions, sans remplacer le goût produit ni l'expertise métier ;
- soutient le travail de conformité, sans certifier la conformité juridique ;
- soutient l'ingénierie de sécurité, sans certifier qu'un système est sûr ;
- permet une autonomie bornée, sans supprimer la responsabilité humaine ;
- considère le déploiement comme une action rouge, sauf politique d'exploitation explicite contraire ;
- n'accorde aucune autorité à un agent simplement parce qu'il a déduit qu'une action serait utile.

### 1.4 Frontières du profilage

Le profilage projet peut inclure trois vues explicitement séparées :

1. **Profil du commanditaire** : objectifs, contraintes, autorité de décision, préférences déclarées et critères de réussite de la personne ou du groupe à l'origine du travail.
2. **Profil du public** : tâches, contextes, besoins d'accessibilité, niveaux de maîtrise, risques et résultats attendus des personnes servies par le produit.
3. **Profil situationnel** : marché, organisation, workflow, technologie, réglementation, calendrier, ressources et environnement d'exploitation.

Ces vues ne doivent pas être fusionnées dans un dossier personnel caché. Ne collecter que les informations nécessaires à la finalité produit déclarée. Expliquer pourquoi elles sont nécessaires, obtenir le consentement quand il s'applique, permettre la correction et définir la rétention. Un comportement temporaire n'est pas une identité. Une inférence projet n'est pas un fait psychologique.

## 2. Les cinq mouvements

La méthode repose sur quatre mouvements successifs et un mouvement permanent.

| Mouvement | Question principale | Sortie typique | Condition de sortie |
| --- | --- | --- | --- |
| Comprendre | Que cherche-t-on, pour qui et sous quelles contraintes ? | Profil projet, carte des ambiguïtés, questions décisives | L'intention est assez cohérente pour être explorée |
| Diverger | Quels produits, domaines, workflows et risques valides peuvent en découler ? | Interprétations concurrentes, domaines et capacités candidates | L'exploration nouvelle produit peu de valeur nette |
| Stabiliser | Que peut-on accepter comme fondation versionnée ? | Cartes curées, contrats, résultats de falsification, Foundation Freeze Candidate | Une gate humaine accepte une fondation bornée |
| Construire | Comment implémenter, intégrer et vérifier le produit ? | Verticales, missions de workers, release candidate testée | Des preuves d'acceptation indépendantes existent |
| Observer, apprendre, réviser | Qu'est-ce que l'usage réel a invalidé ou révélé ? | Signaux, rapport d'apprentissage, propositions de changement | Boucle permanente, sans sortie finale |

Le mouvement n'est pas déterminé par le temps passé, mais par les preuves. Une équipe peut revenir de Construire à Diverger lorsqu'une intégration réelle invalide le modèle produit.

## 3. Maturité de la vision

Le profiler adapte son comportement à la maturité de la vision initiale.

| État initial | Comportement de l'agent | Risque principal | Preuve de sortie |
| --- | --- | --- | --- |
| Très floue | Faire émerger frustrations concrètes, changements désirés, exemples, contournements, acteurs et contexte. Proposer plusieurs interprétations plausibles. | Imposer le produit préféré de l'agent | L'utilisateur reconnaît le problème et rejette ou classe les interprétations |
| Fragmentaire | Reconstruire le système visé à partir de fonctionnalités, documents, workflows et contraintes partiels. Rechercher liens manquants et contradictions. | Traiter une liste de fonctionnalités comme un modèle produit | Les fragments majeurs sont reliés aux domaines, parcours et décisions ouvertes |
| Déjà précise | Auditer preuves, non-objectifs, hypothèses d'architecture, valeur utilisateur, faisabilité et obligations d'exploitation cachées. | Formaliser docilement une spécification erronée | Les hypothèses et alternatives ont été challengées puis acceptées ou révisées |
| Produit partiellement construit | Inspecter comportement réel, tests, architecture, parcours, incidents et documentation. Séparer état actuel, cible et migration. | Croire la documentation plutôt que les preuves runtime | Une carte des écarts vérifiée et un plan de transition borné existent |

Une demande détaillée n'est pas dispensée de challenge. Elle peut encore contenir de fausses prémisses, des contraintes incompatibles ou une architecture non testée.

## 4. Amorçage humain

### 4.1 Cadrage initial

Le premier passage enregistre :

- la vision brute dans les mots de l'utilisateur ;
- l'état futur désiré ;
- le problème actuel et le contournement existant ;
- le commanditaire, les publics, les parties affectées et les responsables de décision ;
- le contexte d'usage ;
- les preuves connues et la qualité de leurs sources ;
- les contraintes, non-objectifs, échéances et dépendances ;
- l'autonomie attendue et les effets externes ;
- la sensibilité des données et l'exposition réglementaire probable ;
- l'amplitude d'ambition, de l'outil local à la plateforme exploitée.

Utiliser le [Product Brief Template](../templates/product-brief-template.md), le [Product Profiling Template](../templates/product-profiling-template.md) et la [Challenge Gate](06-challenge-gate.md) comme artefacts de départ.

### 4.2 Langage de statut

Utiliser ces marqueurs lorsqu'ils clarifient réellement la vérité :

- `[FAIT]` : directement observé ou explicitement confirmé.
- `[INDICE]` : preuve pertinente compatible avec plusieurs interprétations.
- `[HYPOTHÈSE]` : explication ou besoin plausible mais non vérifié.
- `[DÉDUCTION FORTE]` : preuves convergentes sans contradiction matérielle trouvée, mais encore révisable.
- `[INCONNU]` : information manquante pouvant affecter la trajectoire.
- `[DÉCISION]` : choix accepté avec responsable et date.
- `[CONTRAINTE]` : frontière que le plan doit respecter.
- `[GATE HUMAINE]` : décision non délégable selon la politique active.

Ne pas étiqueter chaque phrase. Ces marqueurs empêchent une inférence de devenir silencieusement un fait.

### 4.3 Questions adaptatives

Une question n'est justifiée que si sa réponse peut modifier au moins un élément parmi :

- l'interprétation produit ;
- le public cible ;
- le premier parcours utile ;
- l'architecture ou le modèle de données ;
- la posture de sécurité, de confidentialité ou de conformité ;
- la politique de coûts et de ressources ;
- le niveau d'autonomie ;
- le périmètre de Foundation Freeze ;
- l'ordre de build ou les preuves d'acceptation.

Utiliser un budget de questions. Commencer par le plus petit ensemble de questions à forte valeur d'information, généralement trois à sept. Après chaque réponse, mettre le modèle à jour avant de poursuivre.

Arrêter l'entretien lorsque :

- une interprétation active et ses alternatives rejetées sont explicites ;
- le public principal, le problème et le résultat attendu sont exploitables ;
- les contradictions majeures sont résolues ou inscrites comme décisions nécessaires ;
- les risques liés aux données et aux actions externes ont une classe préliminaire ;
- l'étape d'exploration suivante est sûre et réversible ;
- une question supplémentaire a peu de chances de modifier la prochaine décision.

Le critère n'est pas une compréhension parfaite, mais une compréhension suffisante pour le prochain mouvement borné.

### 4.4 Challenge et confrontation

Le profiler teste activement la vision :

- Quelles preuves soutiennent le problème ?
- Quelle hypothèse rendrait le produit inutile si elle était fausse ?
- Quel public pourrait être lésé, exclu ou mal compris ?
- La fonctionnalité proposée traite-t-elle la cause ou un symptôme visible ?
- Quel workflow plus simple concurrence le système proposé ?
- Quelles charges d'exploitation, de support, de sécurité, de modération ou juridiques apparaissent après le lancement ?
- Qu'est-ce qui rendrait le produit techniquement complet mais inutilisable ?
- Quelle partie de la vision relève de l'aspiration plutôt que du besoin actuel ?

Le challenge n'est complet que si les alternatives et contre-hypothèses importantes sont visibles. Une simple recommandation de l'option préférée de l'agent ne suffit pas.

## 5. Passage à une autonomie bornée

L'autonomie ne commence qu'après la constitution d'un paquet d'amorçage contenant :

- l'interprétation produit active ;
- les incertitudes et le registre d'inférences ;
- les sources autorisées et interdites ;
- la classification des données ;
- la zone de sécurité et la politique d'approbation ;
- le mouvement actuel et la sortie attendue ;
- les budgets de temps, coût, modèle et outils ;
- les conditions d'arrêt et d'escalade ;
- les checkpoints requis ;
- les emplacements des sources de vérité ;
- les attentes de rollback ou de récupération.

La gate de transition échoue si l'agent doit inventer une autorité, inspecter des données personnelles sans rapport, utiliser un service externe non défini ou décider une action rouge au nom de l'utilisateur.

L'autonomie porte sur un résultat et une politique. Elle n'est jamais une propriété globale de l'agent.

## 6. Boucle d'inférence projet

### 6.1 Boucle

```text
Observer la source
  -> enregistrer l'indice
  -> générer des hypothèses concurrentes
  -> chercher preuves favorables et défavorables
  -> attribuer statut et base de confiance
  -> déduire la conséquence produit
  -> exposer l'incertitude
  -> obtenir correction ou décision de gate
  -> conserver, réviser, remplacer ou rejeter
```

### 6.2 Enregistrement d'inférence

Chaque inférence conséquente enregistre :

| Champ | Signification |
| --- | --- |
| `id` | Identifiant stable |
| `statement` | Affirmation évaluée |
| `status` | Indice, hypothèse, déduction forte, acceptée, rejetée, remplacée ou inconnue |
| `sources` | Références durables, pas dumps de contexte |
| `support` | Preuves favorables |
| `counter_evidence` | Preuves ou raisonnement défavorables |
| `alternatives` | Explications concurrentes |
| `product_consequence` | Ce qui change si l'affirmation est vraie |
| `risk_if_wrong` | Dommage ou gaspillage si elle est fausse |
| `confidence_basis` | Base qualitative de confiance, sans fausse précision numérique |
| `owner` | Personne ou rôle responsable de l'acceptation |
| `review_after` | Événement ou date déclenchant la revue |
| `supersedes` | Enregistrement précédent éventuel |

La correction explicite de l'utilisateur prime sur une inférence non vérifiée concernant ses objectifs. La correction n'efface pas l'historique : remplacer l'enregistrement et conserver la raison du changement.

### 6.3 Règle anti-effet Barnum

Une inférence échoue au test anti-Barnum lorsqu'elle est flatteuse, générique, difficile à falsifier ou applicable à presque tout projet.

Remplacer « les utilisateurs apprécient la simplicité » par une formulation testable :

> `[HYPOTHÈSE]` Les opérateurs débutants doivent terminer la revue de publication sans voir les termes de queue ou de worker. Valider par cinq sessions orientées tâche avec un seuil de réussite défini.

### 6.4 Red team des inférences

Avant qu'une déduction forte alimente la fondation, un reviewer demande :

- Quelle observation la réfuterait ?
- La source est-elle indépendante ou répète-t-elle la même origine ?
- Le système a-t-il déduit un besoin stable d'un état temporaire ?
- L'absence d'objection est-elle prise pour un consentement ?
- Une autre interprétation explique-t-elle mieux les preuves ?
- La confiance vient-elle de la répétition plutôt que de la qualité des sources ?

## 7. Exploration fonctionnelle

L'exploration doit être assez large pour découvrir le vrai produit, mais assez structurée pour s'arrêter.

### 7.1 Angles d'exploration

Explorer chaque interprétation plausible selon :

1. Acteurs et tâches à accomplir.
2. Parcours de bout en bout, incluant première utilisation, usage normal, récupération et sortie.
3. Étapes du cycle de vie avant, pendant et après l'action principale.
4. Objets, états, transitions et invariants.
5. Exceptions, échecs, abuse cases et actions refusées.
6. Décisions humaines et automatisation possible.
7. Surfaces Experience Plane et Control Plane.
8. Création, accès, rétention, suppression et export des données.
9. Intégrations et effets externes.
10. Exploitation, support, monitoring, réponse aux incidents et rollback.
11. Accessibilité, localisation et niveaux d'expertise.
12. Coût, performance, échelle et maintenance.

### 7.2 Passages divergents

Pour un produit ambitieux, exécuter au moins trois passages :

- **Produit attendu** : interprétation la plus directe de la demande.
- **Concurrent plus simple** : plus petit workflow susceptible de résoudre le vrai problème.
- **Système plus large** : plateforme ou modèle opératoire impliqué par l'ambition long terme.

Le but n'est pas de choisir l'interprétation la plus grande, mais de comprendre le choix.

### 7.3 Qualité d'un candidat

Une capacité candidate n'est utile que si elle possède :

- un acteur ou consommateur précis ;
- un résultat reconnaissable ;
- des entrées et sorties définies ;
- un domaine propriétaire ;
- une place dans au moins un parcours ;
- une preuve ou une hypothèse explicite ;
- des implications de sécurité et de coût connues ;
- une raison de ne pas être fusionnée avec une capacité existante.

Des noms génériques comme « gestion IA », « analytics intelligentes » ou « fonctionnalités de contenu » ne sont pas des définitions acceptables.

## 8. Cartographie du produit

Les cartes forment un système. Elles ne doivent pas devenir des inventaires déconnectés.

### 8.1 Domain Atlas

Un domaine est une frontière cohérente de responsabilité avec son propre langage, ses règles, objets et owner. Enregistrer :

- finalité et utilisateurs ;
- responsabilités et exclusions ;
- objets et politiques clés ;
- contrats entrants et sortants ;
- concepts partagés ;
- cycle de vie et échecs ;
- classe de données et exposition réglementaire ;
- owner opérationnel.

### 8.2 Capability Atlas

Une capacité est un comportement produit réutilisable, pas un écran ni un module de code. Enregistrer le contrat défini dans le [Capability Graph](10-capability-graph.md), ainsi que les preuves, la maturité et la disposition actuelle.

### 8.3 Module Map

Les modules et sous-modules sont des frontières de propriété d'implémentation réalisant des capacités. Ils peuvent changer sans redéfinir la valeur utilisateur. Enregistrer :

- capacités réalisées ;
- dépendances et dépendances interdites ;
- contrats publics ;
- propriété des données ;
- frontière de test ;
- risque de migration ou d'extraction.

Ne pas confondre domaine, capacité et module :

- un domaine organise la responsabilité produit ;
- une capacité exprime un comportement et une valeur réutilisables ;
- un module organise l'implémentation et la propriété.

### 8.4 Object And State Catalog

Pour chaque objet important, définir :

- nom canonique et sens ;
- domaine propriétaire ;
- identité et cycle de vie ;
- états et transitions valides ;
- acteur et permission de transition ;
- invariants ;
- rétention et suppression ;
- événements émis ;
- exigences d'audit.

Un workflow est incomplet s'il nomme des actions sans définir les états qui les rendent valides.

### 8.5 Cross-Domain Composition Map

Les compositions décrivent un comportement de bout en bout traversant plusieurs capacités ou domaines. Chaque composition précise :

- déclencheur et acteur initiateur ;
- capacités participantes ;
- contrats et artefacts échangés ;
- étapes synchrones et asynchrones ;
- comportement en cas d'échec partiel ;
- compensation ou rollback ;
- vérité finale visible par l'utilisateur ;
- preuve d'intégration.

### 8.6 UI Surface Map

Relier les surfaces aux acteurs, parcours, objets, décisions et exigences de vérité :

| Surface | Plan | Acteur principal | Tâche | Vérité exposée | Parcours avancé |
| --- | --- | --- | --- | --- | --- |
| Workspace produit | Experience | Utilisateur final | Obtenir le résultat métier | Statut et incertitude utiles à l'utilisateur | Réglages contextuels |
| Console d'exploitation | Control | Opérateur | Inspecter et contrôler les runs | Logs, gates, coûts, échecs, permissions | Diagnostic complet |

Appliquer le [Dual UI Model](08-dual-ui-model.md). Des valeurs par défaut simples ne doivent pas supprimer l'inspectabilité, et les contrôles experts ne doivent pas dominer la première utilisation.

### 8.7 Carte des permissions et de l'autonomie

Pour chaque capacité et transition, enregistrer :

- qui peut la demander ;
- qui peut l'approuver ;
- qui ou quoi peut l'exécuter ;
- le niveau d'autonomie applicable ;
- les classes de données touchées ;
- les effets externes ;
- les preuves requises ;
- le rollback ou la compensation ;
- la trace d'audit.

## 9. Curation et saturation

L'exploration produit des candidats. La curation produit un modèle exploitable.

### 9.1 Opérations de curation

Pour chaque candidat, choisir une disposition :

- `active` : appartient au modèle accepté ;
- `foundation-candidate` : peut devenir un contrat stable ;
- `incubator` : utile mais insuffisamment étayé ;
- `deferred` : valide mais hors horizon actuel ;
- `merged` : doublon absorbé dans un autre concept ;
- `split` : concept trop large divisé en plusieurs entrées ;
- `rejected` : évalué et refusé avec une raison ;
- `superseded` : remplacé par une décision ultérieure.

Curer noms, définitions, frontières, synonymes, propriétaires, contrats et traçabilité. Conserver les décisions rejetées afin de ne pas redécouvrir la même idée sans preuve nouvelle.

### 9.2 Test de saturation

L'exploration est saturée pour la décision actuelle lorsque deux passages consécutifs, selon des angles différents, ne produisent :

- aucun nouveau domaine P0 ;
- aucun nouvel objet partagé ni invariant d'état ;
- aucune nouvelle action rouge ni menace matérielle ;
- aucun nouveau public modifiant l'Experience Plane ;
- aucune nouvelle composition inter-domaines requise pour la première release ;
- aucune contradiction non résolue bloquant la fondation ;
- principalement des synonymes, raffinements ou candidats d'horizons ultérieurs.

La saturation est locale et versionnée. Elle ne signifie pas que le produit n'a plus d'inconnues futures.

### 9.3 Règle de valeur de l'information

Continuer l'exploration seulement si la valeur attendue de la nouvelle information dépasse son coût et son délai. Si une verticale fonctionnelle réversible permet de résoudre l'incertitude à moindre coût, construire cette verticale plutôt que prolonger l'entretien ou la carte.

## 10. Foundation Freeze

### 10.1 Définition

Une Foundation Freeze est une baseline versionnée et acceptée humainement des contrats produit et techniques sur lesquels le travail parallèle peut s'appuyer. Ce n'est ni un verrou architectural permanent, ni une déclaration de complétude du produit.

Elle protège la cohérence du build tout en laissant les concepts incertains dans un incubateur.

### 10.2 Contenu requis

Une Foundation Freeze Candidate comprend :

- North Star et vision produit active ;
- frontières des publics et de la situation ;
- domaines acceptés et langage partagé ;
- capacités et compositions principales ;
- objets canoniques, états et invariants ;
- principes Experience Plane et Control Plane ;
- modèle de permissions et d'autonomie ;
- classification des données et contraintes de confidentialité ;
- décisions d'architecture et contrats ;
- verticales P0 et preuves d'acceptation ;
- concepts exclus, différés et incubés ;
- risques connus et questions ouvertes ;
- version, owner, date et politique de remplacement.

### 10.3 Verticales de falsification

Avant de geler la fondation, construire ou exercer les plus petites verticales capables de réfuter ses hypothèses les plus risquées. Une verticale de falsification traverse les vraies frontières importantes, par exemple :

```text
Intention utilisateur
  -> objet métier persisté
  -> décision de politique
  -> exécution de capacité
  -> résultat visible dans l'Experience Plane
  -> preuve dans le Control Plane
```

Un parcours basé uniquement sur des fixtures peut valider la forme d'un contrat. Il ne prouve pas une intégration réelle.

### 10.4 Freeze Gate

La Foundation Freeze Gate exige :

- cartes de domaines et capacités curées ;
- objets et états partagés avec owners ;
- contrats versionnés ;
- verticales P0 de falsification testées ;
- alternatives et décisions rejetées explicites ;
- revue des menaces et de la confidentialité ;
- stratégie de rollback ou migration des changements de fondation ;
- acceptation humaine par les responsables produit et ingénierie.

### 10.5 Changement contrôlé

Après le gel, un changement de fondation exige une proposition contenant :

- déclencheur et preuves ;
- contrats, domaines, parcours et workers affectés ;
- alternatives ;
- impact de compatibilité et migration ;
- nouveaux tests et rollback ;
- responsable de décision ;
- version cible de la fondation.

L'exploration peut continuer dans l'incubateur sans modifier la fondation active. Cela sépare l'apprentissage de la dérive non gouvernée.

## 11. Roadmap et portefeuille de missions de build

### 11.1 Horizons

Maintenir quatre horizons explicites :

1. **Fondation P0** : contrats et verticales nécessaires pour tester le modèle produit.
2. **Première release utilisable** : parcours cohérents pour le public principal.
3. **Release opérationnelle** : fiabilité, support, sécurité, monitoring et gouvernance nécessaires à l'usage réel.
4. **Incubateur et horizons ultérieurs** : extensions plausibles qui ne doivent pas élargir silencieusement le périmètre actuel.

### 11.2 Tranches verticales

Une tranche de build traverse assez de couches pour produire une valeur et une preuve observables. Éviter les roadmaps composées seulement de couches horizontales comme « construire la base », « construire l'API » et « construire l'UI ».

Une verticale définit :

- acteur cible et résultat ;
- parcours déclencheur ;
- domaines et capacités touchés ;
- contrats et données ;
- surfaces UI ;
- zone de sécurité ;
- tests et acceptation observable ;
- rollback ;
- objectif d'apprentissage.

### 11.3 Priorisation

Prioriser explicitement selon :

- valeur utilisateur ;
- réduction des risques ;
- information obtenue ;
- dépendances débloquées ;
- réversibilité ;
- coût d'implémentation et d'exploitation ;
- urgence sécurité et conformité ;
- cohérence stratégique.

Une verticale à forte valeur dépendant d'une fondation non testée peut passer après une verticale de falsification plus petite.

### 11.4 Portefeuille de missions

Le Build Mission Portfolio traduit les verticales acceptées en missions bornées. Il enregistre :

- ID et objectif de mission ;
- verticale et contrats propriétaires ;
- prérequis ;
- workspace isolé et propriété des fichiers ;
- entrées et artefacts attendus ;
- politique de modèles et outils ;
- zone de sécurité, budget, timeout et mécanisme STOP ;
- contrat de tests et preuves ;
- reviewer et owner d'intégration ;
- dépendances de merge ;
- vérité de statut.

Représenter les dépendances par un DAG d'exécution. Paralléliser les missions réellement indépendantes, pas seulement des tâches qui semblent séparées dans une liste.

## 12. Agents de développement parallèles

Les agents parallèles n'augmentent le débit que si la propriété et l'intégration sont explicites.

### 12.1 Préconditions

Ne pas lancer d'agents de build parallèles avant que :

- la fondation active soit versionnée ;
- chaque mission référence les mêmes contrats acceptés ;
- workspaces ou branches soient isolés ;
- propriété des fichiers et modules ne se chevauche pas sans plan d'intégration ;
- entrées, sorties, tests, timeout et conditions d'arrêt soient explicites ;
- un owner d'intégration existe ;
- un reviewer indépendant soit assigné ;
- les conflits et résultats rejetés puissent être gérés sans perdre les preuves.

### 12.2 Contrat de mission

Chaque agent reçoit un ContextPack compact contenant uniquement :

- charte de mission ;
- version pertinente de la fondation ;
- fichiers ou modules possédés ;
- contrats et fixtures requis ;
- décisions et contraintes ;
- zone de sécurité et classe de données ;
- tests à lancer ;
- artefacts de handoff attendus ;
- actions interdites ;
- chemin d'escalade.

Les agents ne déduisent jamais la permission de modifier les contrats partagés. Ils ouvrent une Foundation Change Proposal si la mission révèle un défaut de contrat.

### 12.3 Prévention des conflits

Utiliser :

- worktrees, branches ou sandboxes isolés ;
- propriété unique des fichiers partagés pendant la mission ;
- tests de contrat avant intégration ;
- fixtures générées ou versionnées possédées par l'owner du contrat ;
- ordre de merge explicite dans le DAG ;
- branches d'intégration seulement avec owner nommé et politique de suppression.

Ne pas laisser plusieurs agents réécrire simultanément la même architecture, le même schéma, lockfile, root de navigation ou contrat partagé.

### 12.4 Rôles

Séparer lorsque le risque ou l'ampleur le justifie :

- builder ;
- exécuteur de gate ;
- reviewer ou editor ;
- proofreader ;
- integration owner ;
- acceptance owner ;
- publisher ou deployer.

Une même personne peut cumuler plusieurs rôles sur un petit travail, mais le builder ne doit pas être la seule source de preuve d'acceptation finale.

## 13. Cycle d'ingénierie de bout en bout

Le mouvement Construire couvre plus que la génération de code.

| Phase | Résultat requis | Preuve minimale |
| --- | --- | --- |
| Discovery technique | Contraintes, état réel, inconnues | Sources inspectées et carte des écarts |
| Comparaison d'architecture | Options et compromis | Critères de décision et options rejetées |
| Décision d'architecture | Choix structurel accepté | ADR si le choix est durable ou coûteux à inverser |
| Threat modeling | Actifs, acteurs, frontières de confiance, abuse cases | Threat model revu |
| Données et contrats | Propriété, schémas, API, événements, fixtures | Contrats versionnés et tests de contrat |
| Design UX | Parcours, surfaces, états, accessibilité | Flows révisables et états de vérité |
| Design System | Règles visuelles et d'interaction réutilisables | Composants testés ou tokens documentés selon le cas |
| Implémentation verticale | Comportement de bout en bout | Parcours fonctionnel à travers les couches concernées |
| Revue indépendante | Défauts et décision d'acceptation | Trace de revue distincte de l'affirmation du builder |
| Vérification | Preuves unitaires, intégration, end-to-end, accessibilité, performance et sécurité selon le risque | Sorties réelles de commandes et rapports |
| Revue supply-chain | Risques des dépendances et artefacts | Inventaire, provenance et vulnérabilités |
| Visual QA | États rendus et comportement responsive | Captures ou critères de revue enregistrés |
| Documentation | Exploitation, décisions, limites et handoff | Sources de vérité mises à jour |
| Packaging | Release candidate reproductible | Artefact de build et provenance |
| Readiness release | Déploiement, rollback, monitoring et incident plan | Gates de release réussies |
| Release supervisée | Changement externe autorisé | Cible, résultat et rollback vérifiés |
| Exploitation | Service observable et supportable | Preuves de monitoring et incidents |
| Apprentissage produit | Signaux réels et hypothèses révisées | Rapport d'apprentissage et propositions de changement |

Utiliser le cycle le plus léger qui protège le produit. Les petits outils locaux peuvent regrouper des phases. Les systèmes publics ou sensibles doivent garder leurs preuves distinctes.

## 14. Intégration et vérification

### 14.1 Paquet d'intégration

Chaque handoff de mission fournit :

- référence du commit ou patch ;
- versions de fondation et de contrats utilisées ;
- fichiers et modules modifiés ;
- décisions et écarts ;
- tests exécutés et résultats ;
- tests ignorés et raison ;
- nouvelles dépendances ;
- impact sécurité, confidentialité et coût ;
- échecs connus et rollback ;
- prochain état proposé.

### 14.2 Integration Gate

L'integration owner vérifie :

- le périmètre appartient à la mission ;
- les contrats restent compatibles ;
- les migrations sont ordonnées et réversibles quand nécessaire ;
- tests unitaires et de contrat réussissent ;
- les verticales pertinentes traversent les vraies frontières ;
- Experience Plane et Control Plane présentent une vérité compatible ;
- aucune donnée sensible n'entre dans les artefacts ou logs ;
- accessibilité, performance et sécurité sont vérifiées selon le risque ;
- un résultat de worker rejeté n'a pas été accepté silencieusement ;
- documentation et statut reflètent la réalité.

### 14.3 Vocabulaire des preuves

Garder ces états distincts :

- `specified` : contrat existant ;
- `implemented` : code ou configuration existants ;
- `unit-tested` : comportement isolé validé ;
- `fixture-integrated` : composants validés avec des substituts contrôlés ;
- `integrated` : composants réels exercés ensemble ;
- `end-to-end verified` : parcours représentatif passé à travers ses vraies frontières ;
- `user-validated` : preuves fournies par les utilisateurs cibles ;
- `release-ready` : toutes les gates applicables ont réussi ;
- `released` : déploiement autorisé et vérifié ;
- `operationally validated` : usage réel acceptable dans les limites déclarées.

Ne jamais appeler une fixture intégration réelle, une readiness autorisation, un prototype produit fini, ni un test local validation utilisateur.

### 14.4 Preuves du niveau premium

Premium est un état fondé sur des preuves, pas une intention de design. Un produit ne peut revendiquer un niveau premium que si les preuves applicables montrent que :

- le public principal termine le parcours central sans jargon interne ni charge cognitive évitable ;
- des valeurs par défaut adaptées aux débutants et des contrôles experts coexistent par divulgation progressive ;
- le parcours de bout en bout fonctionne à travers de vraies frontières et rapporte honnêtement les échecs ;
- les états de chargement, vide, partiel, erreur, récupération, permission refusée et rollback sont conçus et exercés ;
- accessibilité, performance, responsive et qualité du contenu respectent des seuils explicites ;
- coûts, incertitudes, comportement des modèles et effets externes sont visibles par l'acteur approprié ;
- les actions destructives ou conséquentes restent réversibles ou protégées par les gates requises ;
- support, exploitation et responsabilités d'incident sont définis pour l'usage réel ;
- les utilisateurs cibles et un reviewer indépendant ont accepté le résultat dans ses limites déclarées.

Le polish visuel peut renforcer ces preuves, mais ne remplace jamais un parcours manquant, un faux statut, une accessibilité faible, une automatisation dangereuse, un coût caché ni une récupération non testée. Appliquer le [Premium Standard](03-premium-standard.md) et enregistrer ses preuves dans le paquet d'acceptation.

## 15. Gates humaines et niveaux d'autonomie

### 15.1 Gates humaines

| Famille de gates | Décisions humaines explicites |
| --- | --- |
| Profiling | Consentement, correction de l'intention, acceptation d'inférences conséquentes, sources autorisées |
| Produit | Interprétation active, North Star, P0, alternatives rejetées, Foundation Freeze |
| Technique | Changement durable d'architecture, acceptation de risque sécurité, migration à impact matériel, exception de dépendance |
| Externe | Publication, production, finance, message externe, destruction, secrets ou credentials |

Une gate observe les preuves et retourne réussite, échec ou décision nécessaire. Elle ne corrige pas silencieusement le travail avant de s'approuver elle-même.

### 15.2 Niveaux d'autonomie

| Niveau | Description | Autorité typique |
| --- | --- | --- |
| A0 - Conseiller | Analyser et recommander | Aucune autorité d'écriture ou d'exécution |
| A1 - Rédiger | Créer propositions et artefacts locaux | Documents ou patches locaux réversibles |
| A2 - Exécuter un travail local borné | Implémenter et tester une mission acceptée | Actions vertes dans le périmètre déclaré |
| A3 - Intégrer sous supervision | Préparer et combiner des changements acceptés | Actions orange après proposition ou revue requise |
| A4 - Opérer avec gates explicites | Exécuter des workflows récurrents sous politique approuvée | Actions préautorisées avec audit, limites et gates humaines |
| A5 - Exploitation déléguée exceptionnelle | Exécuter des actions conséquentes très bornées | Seulement sous gouvernance explicite ; les actions rouges gardent leur approbation désignée |

L'autonomie est attribuée par capacité et action, pas par produit ou agent. Un système peut lancer ses tests en A2 tandis que la publication reste A0 jusqu'à approbation humaine.

## 16. Sécurité et Privacy by Design

### 16.1 Principes

- Minimiser données, permissions, contexte, rétention et exposition externe.
- Séparer identité, contenu, exploitation, facturation, télémétrie et secrets.
- Appliquer le moindre privilège et refuser les actions non déclarées.
- Garder les secrets hors des prompts, logs, dépôts, exemples et artefacts.
- Rendre les effets destructifs et externes explicites et révisables.
- Concevoir suppression, export, révocation, réponse aux incidents et rollback avant la release.
- Traiter les sorties des modèles et outils comme non fiables jusqu'à validation.

### 16.2 Classification conservatrice des données

| Classe | Exemple | Traitement par défaut |
| --- | --- | --- |
| S0 - Public | Documentation publiée et exemples synthétiques | Peut entrer dans les workflows publics approuvés |
| S1 - Interne | Planification non sensible et métadonnées opérationnelles ordinaires | Limiter aux participants autorisés du projet |
| S2 - Confidentiel | Plans non publiés, contenu client, informations commerciales | Accès selon besoin, rétention contrôlée, processors approuvés |
| S3 - Restreint | Données personnelles, contenu sensible, failles, éléments proches des secrets | Aucun provider de modèle externe selon la politique par défaut ; contrôles d'accès et d'audit forts |
| S4 - Critique | Credentials, clés privées, secrets de production, données à fort impact | Jamais dans le contexte d'un modèle ; utiliser des systèmes dédiés de secrets et de contrôle |

Une organisation peut raffiner ce schéma par une politique approuvée, mais ne doit pas déclasser silencieusement les données pour simplifier l'exécution.

### 16.3 Couverture du Threat Model

Évaluer au minimum :

- prompt injection et instructions dissimulées ;
- usage non autorisé d'outils ;
- élévation de privilèges ;
- exfiltration via contexte, logs, artefacts ou providers ;
- fuite entre projets ou tenants ;
- compromission de dépendance et supply-chain ;
- sources empoisonnées ;
- actions externes accidentelles ou malveillantes ;
- code ou commandes générés dangereux ;
- tempêtes de retries et déni de service par les coûts ;
- faux statuts et fabrication de preuves ;
- migrations destructives et absence de rollback ;
- abus des endpoints publics ;
- profiling sans consentement ni finalité.

### 16.4 Contrôles de confidentialité

Pour chaque flux de données, enregistrer finalité, source, base juridique ou organisationnelle, classe, champs, destinataires, lieu de traitement, rétention, suppression, export, contrôle d'accès, trace d'audit et owner d'incident.

La revue échoue si le produit collecte des données parce qu'elles pourraient servir plus tard, les conserve indéfiniment par défaut ou les réutilise pour une finalité matériellement différente sans nouvelle décision.

## 17. Produits privés, internes et publics

### 17.1 Produit privé ou personnel

Définir tout de même :

- emplacement local et backups ;
- frontières des appareils et comptes ;
- exposition aux providers ;
- rétention et suppression ;
- export et portabilité ;
- conséquences d'une perte ou compromission ;
- actions restant visibles à l'extérieur.

Privé ne signifie pas sans risque. Une automatisation personnelle peut exposer des credentials, publier, dépenser ou détruire des données.

### 17.2 Produit interne

Définir aussi :

- rôles organisationnels et moindre privilège ;
- frontières des données des employés ou prestataires ;
- ownership de l'audit et du support ;
- change management ;
- revue des vendors et processors ;
- continuité d'activité ;
- procédures internes d'incident et de revue d'accès.

### 17.3 Produit public ou commercial

Avant lancement, traiter selon le cas :

- information de confidentialité et contrôles transparents de consentement ou préférences ;
- base juridique et limitation des finalités ;
- cookies et choix de tracking ;
- cycle de vie des comptes et droits utilisateurs ;
- obligations d'accessibilité ;
- conditions et règles d'usage acceptable ;
- prévention des abus et modération ;
- support, réclamations et réponse aux incidents ;
- sécurité publique et traitement des vulnérabilités ;
- vendors et traitements transfrontaliers ;
- revue de réputation et communication ;
- preuves d'acceptation des parcours critiques.

### 17.4 Revue orientée RGPD

Pour les produits soumis au RGPD, identifier le responsable de traitement et les sous-traitants ; finalités et bases légales ; catégories de données ; données sensibles ; destinataires ; rétention ; transferts ; procédures d'accès, rectification, effacement, portabilité, opposition et limitation ; retrait du consentement lorsqu'il s'applique ; registre des traitements ; contrats de sous-traitance ; gestion des violations ; audit des logs ; possibilités de pseudonymisation ou anonymisation ; obligations relatives aux mineurs ; et nécessité d'une AIPD/DPIA.

Éviter le profilage clandestin et les décisions entièrement automatisées produisant des effets juridiques ou similaires significatifs, sauf si une revue qualifiée établit une base légale et des garanties adaptées.

Cette méthode fournit une checklist d'ingénierie, pas un conseil juridique ni un certificat de conformité. Une expertise juridique qualifiée reste une gate humaine lorsque les obligations sont matérielles ou incertaines.

## 18. Workers autonomes durables

Un worker durable est un runtime observable, pas une longue session de chat.

Il nécessite :

- wrapper externe ou superviseur ;
- session et workspace isolés ;
- queue de missions ordonnée par valeur de résultat ;
- état live et historique append-only des décisions ;
- logs avec redaction des données sensibles ;
- heartbeat et détection de run périmé ;
- fichier STOP ou mécanisme d'arrêt équivalent ;
- timeout de chaque appel externe et de la mission ;
- retries bornés avec backoff et escalade ;
- checkpoints et rapports périodiques ;
- registre des fichiers touchés et dépendances ;
- tests et rapport final ;
- reprise après interruption ;
- notifications supervisées ;
- limites explicites des actions externes.

La boucle est orientée résultats :

```text
Sélectionner le résultat non bloqué de plus forte valeur
  -> produire un résultat borné
  -> le tester et le challenger
  -> enregistrer preuves et décisions
  -> intégrer ou rejeter
  -> ouvrir un gap si nécessaire
  -> reprioriser selon les preuves actuelles
```

La durée n'est pas l'autonomie. Un worker continu ne doit pas remplir le temps artificiellement. Arrêter ou changer de mouvement lorsque les retries se répètent sans preuve, que la valeur marginale baisse, que les budgets approchent leurs limites ou qu'une gate indépendante est requise.

Voir [Autonomous Worker Runtime](13-autonomous-worker-runtime.md) pour le contrat runtime.

## 19. Gouvernance des modèles

Router le travail selon le rôle et les preuves attendues, pas selon une dépendance aveugle à un modèle unique.

| Classe de travail | Stratégie adaptée |
| --- | --- |
| Cadrage ambigu, arbitrage d'architecture, synthèse finale, revue à haut risque | Modèle de raisonnement fort avec revue indépendante |
| Exploration, implémentation bornée, analyse d'intégration, revue éditoriale | Modèle équilibré choisi par évaluation représentative |
| Extraction, formatage, fixtures, tests répétitifs, checks déterministes | Modèle économique ou outil déterministe avec contrat strict |

La gouvernance exige :

- classification des données avant routing ;
- ContextPacks compacts ;
- benchmarks représentatifs plutôt que classements génériques ;
- modèle, version, provider, politique et date enregistrés ;
- handoffs durables indépendants de la mémoire du modèle ;
- cache lorsque les sources et la politique le permettent ;
- limites de coût, latence et retries ;
- escalade lorsque confiance ou vérification sont insuffisantes ;
- aucune décision critique confiée uniquement à un modèle économique ;
- aucune donnée S3 ou S4 envoyée à un provider externe selon la politique par défaut ;
- audit indépendant pour les changements de fondation.

Une recommandation de modèle est sensible au temps. La réévaluer avec la documentation officielle actuelle et des tâches représentatives avant d'en faire une dépendance durable.

## 20. Complétude sans théâtre de la complétude

### 20.1 Dimensions

Évaluer séparément :

- couverture conceptuelle ;
- cohérence des domaines ;
- maturité des inférences ;
- readiness de la fondation ;
- couverture des contrats ;
- verticales P0 intégrées ;
- qualité UX et accessibilité ;
- sécurité et confidentialité ;
- preuves de tests ;
- intégration réelle ;
- readiness de déploiement ;
- readiness opérationnelle ;
- validation humaine et utilisateur ;
- revue de conformité ;
- capacité de rollback.

Le nombre de fichiers, cartes, tests, tokens ou heures n'est pas une mesure de complétude.

### 20.2 Échelle de preuve

Noter chaque dimension applicable indépendamment :

| Niveau | Signification |
| --- | --- |
| 0 - Inconnu | Aucune preuve exploitable |
| 1 - Cadré | Périmètre et risques décrits |
| 2 - Spécifié | Contrats et critères d'acceptation existants |
| 3 - Exercé | Implémentation ou processus représentatif testé |
| 4 - Accepté indépendamment | Preuves revues par l'acceptance owner désigné |
| 5 - Validé en exploitation | Usage réel confirmant le résultat dans les limites déclarées |

Un pourcentage global n'est autorisé que comme estimation pondérée explicite. Il doit montrer scores par dimension, preuves, confiance, inconnues et dimensions exclues. Ne jamais l'augmenter matériellement sans nouvelles preuves intégrées.

### 20.3 Rapport périodique

Rapporter :

- estimation pondérée totale et confiance ;
- couverture conceptuelle ;
- readiness de fondation ;
- statut de l'alpha locale ;
- statut d'intégration réelle ;
- nouvelles preuves acceptées ;
- inconnues et hypothèses ;
- risques et décisions bloquantes ;
- prochain jalon pouvant légitimement modifier l'estimation ;
- avertissement de réalisme.

Ne pas déclarer 99 % sans acceptation indépendante, validation humaine, déploiement vérifié, preuves d'exploitation et acceptation explicite des limites restantes. Dans la plupart des travaux préproduction, 99 % n'est ni utile ni crédible.

## 21. Sources de vérité et adaptation des artefacts

### 21.1 Hiérarchie

Appliquer cet ordre en cas de désaccord :

1. North Star.
2. Vision produit active.
3. Foundation Freeze active.
4. ADR et contrats acceptés.
5. Roadmap.
6. Build Mission Portfolio.
7. Spécifications des workers.
8. Résultats et rapports vérifiés.
9. Incubateur.
10. Historique remplacé.

Ne pas utiliser le chat comme seule source de vérité, le backlog comme vision produit, le kanban comme architecture, le rapport du worker comme preuve d'acceptation ni le nombre de tâches comme maturité.

### 21.2 Catalogue d'artefacts

Un système ambitieux peut utiliser :

- `PROJECT_CHARTER.md`
- `PROJECT_PROFILE.md`
- `AUDIENCE_PROFILES.md`
- `SITUATIONAL_PROFILE.md`
- `VISION_MAP.md`
- `ASSUMPTION_REGISTER.md`
- `INFERENCE_REGISTRY.jsonl`
- `DOMAIN_ATLAS.md`
- `CAPABILITY_ATLAS.md`
- `MODULE_MAP.md`
- `OBJECT_STATE_CATALOG.md`
- `CROSS_DOMAIN_COMPOSITIONS.md`
- `UI_SURFACE_MAP.md`
- `RISK_REGISTER.md`
- `PRIVACY_AND_DATA_MAP.md`
- `ROADMAP.md`
- `BUILD_MISSION_PORTFOLIO.md`
- `FOUNDATION_FREEZE_CANDIDATE.md`
- `FOUNDATION_CHANGE_PROPOSALS.md`
- `ARCHITECTURE.md`
- `ADR/`
- `EXECUTION_DAG.md`
- `WORKER_SPECS/`
- `TEST_STRATEGY.md`
- `ACCEPTANCE_GATE.md`
- `ROLLBACK.md`
- `LIVE_STATUS.md`
- `DECISIONS_NEEDED.md`
- `COMPLETENESS_ESTIMATE.md`
- `RUN_REPORT.md`
- `LEARNING_REPORT.md`

C'est un catalogue, pas un ordre de créer trente fichiers. Un petit projet doit regrouper ces préoccupations dans le [Vision-to-Product Control Pack Template](../templates/vision-to-product-control-pack-template.md). Séparer un artefact uniquement s'il possède un owner, un cycle de vie, une sensibilité, une gate de revue ou une fréquence de mise à jour distincts.

## 22. Acceptation indépendante

Le producteur n'est pas le juge final de son propre résultat.

L'acceptation indépendante vérifie :

- utilité pour le public cible ;
- cohérence avec North Star et Foundation Freeze ;
- vérité des contrats et de l'intégration ;
- clarté UX et accessibilité ;
- sécurité et confidentialité ;
- performance et coût d'exploitation ;
- obligations de conformité ;
- rollback et récupération ;
- honnêteté du statut et des limites ;
- absence d'effet externe non autorisé.

L'acceptance owner retourne :

- `accepted` avec preuves et limites ;
- `accepted-with-reservations` avec suivi possédé ;
- `rejected` avec constats bloquants ;
- `decision-needed` lorsqu'il manque autorité ou preuve.

Un reviewer peut identifier et proposer des corrections. L'enregistrement d'acceptation distingue toujours le travail du producteur, les changements du reviewer et la décision finale.

## 23. Boucle d'apprentissage post-livraison

```text
Usage réel
  -> signaux et feedback
  -> incidents et performance
  -> explications concurrentes
  -> inférences corrigées
  -> profil projet révisé
  -> capacité candidate ou proposition de changement
  -> nouvelle verticale de falsification
  -> fondation et release suivantes
```

Règles :

- une métrique ne dicte pas seule la direction produit ;
- corrélation n'est pas causalité ;
- un feedback isolé n'est pas une vérité universelle ;
- un état utilisateur temporaire n'est pas une identité ;
- la correction explicite prime sur une inférence non vérifiée ;
- les décisions rejetées restent recherchables ;
- l'apprentissage est versionné avec source et date ;
- les hypothèses invalidées sont retirées ou remplacées ;
- les preuves de production ne contournent pas la limitation des finalités ;
- un incident urgent peut déclencher une correction de sécurité bornée avant une révision produit plus large.

Utiliser [Feedback Integration](15-feedback-integration.md) et capturer le résultat dans un rapport d'apprentissage ou une source de vérité équivalente.

## 24. Catalogue des anti-patterns

| Anti-pattern | Symptôme | Cause et risque | Détection | Correction |
| --- | --- | --- | --- | --- |
| Coder avant de comprendre | Le premier artefact est du code | Le wording brut devient architecture accidentelle | Aucun profil ni challenge | Revenir à l'amorçage et borner une verticale de falsification |
| Questionnaire générique | Beaucoup de questions, peu de décisions changées | Fatigue et théâtre de l'intake | Les réponses n'altèrent pas la trajectoire | Budget de questions et test de valeur d'information |
| Profiling clandestin | Inférences personnelles sans finalité ni consentement | Atteinte à la vie privée et perte de confiance | Aucune source, correction ou rétention | Minimiser, informer, obtenir le consentement requis et retirer les données injustifiées |
| Effet Barnum | Affirmations séduisantes mais universelles | Fausse confiance | Aucune condition de réfutation | Réécrire en hypothèse testable avec contre-preuves |
| Dump de profil | Contexte massif copié à chaque worker | Fuite, coût et contradiction | ContextPack non pertinent | Charger des références compactes par mission |
| Exploration infinie | Les cartes croissent sans décision | Aucune règle de saturation ou curation | Nouveaux candidats synonymes | Tester la saturation et curer les dispositions |
| Explosion de capacités synonymes | Centaines de capacités qui se chevauchent | Vocabulaire pris pour architecture | Pas d'acteur, résultat ou contrat unique | Fusionner, renommer, scinder et assigner des owners |
| Micro-gates récursives | Chaque action mineure attend une approbation | Modèle de risque non proportionné | Le travail vert s'arrête sans cesse | Affecter les gates selon l'action et la conséquence |
| Time-box theatre | Worker actif pour remplir une durée | Temps pris pour valeur | Sorties répétitives à faible valeur | Queue de résultats et arrêt quand la valeur marginale baisse |
| Auto-félicitation du worker | Le rapport final est la seule preuve | Auto-certification du producteur | Aucune revue ni sortie de tests | Séparer builder, gate et acceptance owner |
| Complétude au nombre de fichiers | Le progrès augmente avec les documents | Activité prise pour maturité | Aucune preuve dimensionnelle | Noter les dimensions et l'intégration réelle |
| Console technique prise pour le produit | L'utilisateur final navigue dans les logs et workers | Experience et Control Planes mélangés | Le parcours principal exige du jargon interne | Concevoir des surfaces distinctes avec divulgation progressive |
| Mock présenté comme réel | Les fixtures semblent être des capacités live | Vocabulaire de statut faible | Aucune provenance ni état d'intégration | Étiqueter la vérité des fixtures et tester les vraies frontières |
| Statut global unique | « Done » masque des états incompatibles | Compression de la vérité | Tests, release et validation inséparables | Rapporter les états de preuve séparément |
| Déploiement sans rollback | Changement externe sans récupération | Pression de release | Rollback absent ou non testé | Bloquer la release et tester la récupération |
| Worker sans STOP | Run impossible à interrompre | Runtime traité comme prompt | Aucun kill ni timeout | Ajouter wrapper, STOP, timeout et détection de staleness |
| Agents parallèles sur les mêmes fichiers | Conflits et écrasements | Propriété absente | Périmètres d'écriture chevauchants | Isoler les workspaces et assigner un owner unique |
| Agent local modifiant la fondation | Le contrat partagé dérive dans une mission | Autorité trop large | Contrat modifié sans proposition | Isoler le changement et ouvrir une Foundation Change Proposal |
| Dépendance non inspectée | Package ajouté par facilité | Risque supply-chain et maintenance ignoré | Aucune provenance ni alternative | Revue de dépendance et acceptation explicite |
| Secret dans un prompt ou artefact | Credential dans le contexte ou les logs | Chemin de manipulation dangereux | Secret scan ou log provider | Révoquer si nécessaire, retirer l'exposition et utiliser un secret store |
| Données personnelles sans finalité | Données gardées pour plus tard | Violation de minimisation et confiance | Aucune finalité ni rétention | Supprimer ou isoler, puis définir base et contrôles |
| Refus humain ignoré | L'agent repropose une direction rejetée | Optimisation prioritaire sur autorité | Retour sans preuve nouvelle | Conserver le refus et exiger une nouvelle décision humaine |
| Tests déclarés mais non exécutés | Rapport « vérifié » sans sortie | Pression de complétude | Pas de commande ni artefact | Marquer non vérifié et lancer le check applicable |
| Techniquement complet, inutilisable | Composants présents mais parcours cassés | Build horizontal sans preuve produit | Aucun résultat end-to-end | Replanifier autour des parcours et tests utilisateurs |
| Automatiser une mauvaise décision | Le système amplifie un workflow non validé | Automatisation prise pour progrès | Aucune preuve d'utilité | Rouvrir le challenge et tester une alternative réversible |

## 25. Exemple canonique et checklists finales

L'exemple synthétique complet est [D'une vision d'activité créative à un produit supervisé](../examples/example-vision-to-product.md). Il démontre profils séparés, interprétations concurrentes, correction d'inférences, cartes produit, Foundation Freeze Candidate, trois missions parallèles, intégration, release supervisée, décisions rejetées et révision post-livraison.

### 25.1 Avant autonomie

- [ ] Vision assez cadrée pour le prochain mouvement.
- [ ] Public identifié ou explicitement inconnu.
- [ ] Commanditaire, public et situation non confondus.
- [ ] Sources autorisées et interdites explicites.
- [ ] Données classifiées et minimisées.
- [ ] Charte de mission et niveau d'autonomie acceptés.
- [ ] Gates humaines nommées.
- [ ] STOP, timeout, récupération et rollback présents selon le cas.
- [ ] Politiques de reporting, coût, modèles et outils définies.
- [ ] Tests, preuves attendues et hors périmètre explicites.

### 25.2 Avant Foundation Freeze

- [ ] Domaines requis avec owners et frontières.
- [ ] Synonymes et doublons curés.
- [ ] Objets, états, transitions et invariants partagés explicites.
- [ ] Couches de vérité et états de preuve définis.
- [ ] Permissions et autonomie cartographiées.
- [ ] P0 et verticales de falsification exercées.
- [ ] Contrats et checks de compatibilité existants.
- [ ] Risques sécurité, confidentialité et coûts revus.
- [ ] Alternatives et décisions rejetées conservées.
- [ ] Incubateur séparé de la fondation active.
- [ ] Owners produit et ingénierie acceptent la candidate.

### 25.3 Avant workers de développement parallèles

- [ ] Version de fondation référencée.
- [ ] Workspaces et périmètres d'écriture isolés.
- [ ] Propriété des fichiers partagés et contrats explicite.
- [ ] Entrées et sorties de mission définies.
- [ ] Fixtures et tests de contrat versionnés.
- [ ] Budget, timeout, retries et STOP définis.
- [ ] Ordre de merge et dépendances représentés.
- [ ] Owners de l'intégration et de la revue indépendante assignés.
- [ ] Les workers ne peuvent pas changer silencieusement les contrats de fondation.

### 25.4 Avant intégration

- [ ] Résultats réels des tests unitaires et de contrat.
- [ ] Résultats réels des parcours d'intégration et end-to-end pertinents.
- [ ] Contrats et migrations compatibles.
- [ ] Checks sécurité, confidentialité, accessibilité, performance et coûts proportionnés au risque.
- [ ] Experience Plane et Control Plane montrent une vérité compatible.
- [ ] Rollback ou compensation disponible.
- [ ] Aucune donnée sensible exposée dans code, artefacts, logs ou prompts.
- [ ] Résultats des workers rejetables sans corrompre la source de vérité.
- [ ] Documentation et statut mis à jour.

### 25.5 Avant action externe

- [ ] Approbation humaine désignée présente.
- [ ] Cible et environnement exacts vérifiés.
- [ ] Payload ou change set revu.
- [ ] Données minimisées et base documentée.
- [ ] Preuve de dry-run ou sandbox si possible.
- [ ] Rollback, compensation ou récupération prêts.
- [ ] Logs redacted et auditables.
- [ ] Gate exécutable vérifiant le périmètre autorisé.
- [ ] Aucun secret visible ni copié dans le canal d'approbation.
- [ ] Vérification du résultat définie avant exécution.

### 25.6 Avant toute déclaration à 99 %

- [ ] Produit réel exécuté sur des parcours représentatifs.
- [ ] Verticales P0 intégrées, pas seulement mockées.
- [ ] Tests applicables réussis avec preuves conservées.
- [ ] Revue et acceptation indépendantes terminées.
- [ ] UX et accessibilité validées.
- [ ] Revues sécurité, confidentialité et conformité adaptées au risque.
- [ ] Déploiement et monitoring vérifiés.
- [ ] Réponse aux incidents et rollback exercés.
- [ ] Documentation d'exploitation et utilisateur actuelle.
- [ ] Validation humaine existante.
- [ ] Limites restantes explicites et acceptées.
- [ ] Estimation pondérée, confiance et preuves encore crédibles après challenge.

## Points d'entrée opérationnels

- Utiliser le [Vision-to-Product Control Pack Template](../templates/vision-to-product-control-pack-template.md) pour exécuter la méthode dans un artefact compact.
- Utiliser le [Vision-to-Product Orchestrator](../prompts/system-prompts/vision-to-product-orchestrator.md) pour configurer un agent selon ce protocole.
- Utiliser l'[exemple canonique](../examples/example-vision-to-product.md) pour examiner le niveau de profondeur et de preuve attendu.
- Utiliser [Quality Gates](14-quality-gates.md), [Testing and Sandboxing](17-testing-and-sandboxing.md) et [Public Method Limitations](19-public-method-limitations.md) avant toute affirmation de maturité, sécurité, conformité ou readiness de release.

## Cadres de référence

Utiliser des sources actuelles et officielles lorsqu'un projet transforme ces préoccupations méthodologiques en exigences contraignantes :

- le [Règlement (UE) 2016/679 (RGPD)](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32016R0679) pour les obligations européennes applicables de protection des données ;
- les [lignes directrices de l'EDPB sur les décisions automatisées et le profilage](https://www.edpb.europa.eu/documents/guideline/automated-decision-making-and-profiling_en) pour l'interprétation du profilage et des décisions automatisées significatives au titre du RGPD ;
- les [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/) pour des critères testables d'accessibilité web ;
- le [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) et son [Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence) pour des pratiques volontaires de gestion des risques IA.

Ces références ne s'appliquent pas automatiquement à toutes les juridictions ni à tous les contextes. Les suivre ne prouve pas à lui seul la conformité juridique, la conformité accessibilité, la sécurité ni une exploitation responsable. Enregistrer la version, le périmètre, la cible et le reviewer qualifié applicables au produit.
