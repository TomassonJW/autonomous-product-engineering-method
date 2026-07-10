# Exemple : d'une vision d'activité créative à un produit supervisé

Cet exemple est synthétique et publiable. Il démontre des décisions méthodologiques et des états de preuve. Il ne prétend pas que le produit fictif a été construit ou validé juridiquement.

## 1. Vision initiale

Un utilisateur dit :

> « Je veux un système intelligent pour gérer les contenus, les photos, le site et le développement de mon activité créative. »

Maturité initiale : fragmentaire. La phrase nomme plusieurs zones, mais ne définit ni le problème principal, ni le public, ni le modèle d'exploitation, ni la frontière d'autonomie.

## 2. Première interprétation

`[HYPOTHÈSE]` L'utilisateur veut un workspace unique qui transforme des contenus créatifs bruts en mises à jour de site revues, tout en lui laissant le contrôle de la publication.

Cette interprétation n'est pas encore acceptée, car « développement » peut désigner le développement commercial, le site, le logiciel ou les trois.

## 3. Questions adaptatives

Le profiler pose cinq questions.

| Question | Décision Qu'Elle Peut Modifier | Réponse |
| --- | --- | --- |
| Quel résultat prend actuellement le plus de temps : organiser, produire le contenu, mettre à jour le site ou coordonner le travail technique ? | Parcours P0 et interprétation active | Produire et publier un contenu cohérent à partir de photos et notes dispersées |
| Qui utilise d'abord le système et qui consomme le résultat ? | Profils du commanditaire et du public, Experience Plane | Un responsable de studio l'utilise ; clients existants et prospects consomment le résultat public |
| Le système peut-il publier seul ? | Autonomie et gate externe | Non. Il peut préparer un brouillon, mais chaque publication exige l'approbation du responsable |
| Que signifie « développement » dans cette première version ? | Domaines et roadmap | Améliorer le site et préparer de futurs outils numériques, pas piloter automatiquement la stratégie commerciale |
| Où se trouvent aujourd'hui photos et notes ? | Flux de données, intégrations et confidentialité | Dossiers locaux et cloud drive ; la politique d'accès n'est pas définie |

Décision de sortie d'entretien :

- Le problème et le public principal sont explicites.
- La publication est une action rouge avec approbation humaine.
- L'accès au cloud drive reste `[INCONNU]`, donc la première verticale utilise un dossier d'import local.
- Les questions restantes seront résolues à moindre coût par un prototype réversible et une revue d'utilisabilité.

## 4. Profils séparés

### 4.1 Profil du commanditaire

- `[FAIT]` Le responsable du studio est le premier opérateur et l'approbateur des publications.
- `[FAIT]` Il veut réduire le travail répétitif de préparation.
- `[CONTRAINTE]` Il n'autorise pas la publication autonome.
- `[INDICE]` Il souhaite que le système puisse plus tard coordonner des projets numériques.
- `[INCONNU]` Le coût récurrent acceptable n'est pas chiffré.

Aucun trait de personnalité ni profil psychologique n'est inféré.

### 4.2 Profil du public

Public externe principal :

- prospects consultant les travaux récents ;
- clients existants consultant le portfolio ;
- visiteurs mobiles disposant de peu de temps.

Besoins :

- chargement rapide ;
- contexte clair des projets ;
- images et légendes accessibles ;
- dates de publication véridiques ;
- aucune exposition des brouillons ou notes internes.

### 4.3 Profil situationnel

- `[FAIT]` Les sources sont réparties entre dossiers locaux, cloud et notes.
- `[FAIT]` Le site exige des mises à jour manuelles.
- `[HYPOTHÈSE]` Le retard vient davantage de la curation et de la revue que de l'écriture seule.
- `[CONTRAINTE]` La première alpha doit fonctionner localement et produire uniquement des brouillons.
- `[INCONNU]` L'API de publication et le rollback du site n'ont pas été audités.

## 5. Registre d'inférences

| ID | Statut | Affirmation | Support | Contre-Preuve | Conséquence Produit | Risque Si Faux |
| --- | --- | --- | --- | --- | --- | --- |
| INF-001 | FAIT | Toute publication exige l'approbation du responsable | Réponse explicite | Aucune | La publication reste A0 avant approbation, puis action externe bornée | Changement public non autorisé |
| INF-002 | HYPOTHÈSE | Un workspace doit couvrir contenu, médias et revue du site | L'utilisateur regroupe ces activités | Des outils spécialisés séparés peuvent être plus clairs | Explorer une Experience Plane unifiée avec domaines modulaires | Workspace surdimensionné |
| INF-003 | HYPOTHÈSE | La curation photo est le principal goulot | Sources dispersées et publications retardées | La qualité rédactionnelle peut être le vrai problème | La première verticale inclut une vraie sélection photo | Mauvaise priorité P0 |
| INF-004 | DÉDUCTION FORTE | L'exploitation interne doit être séparée du workflow public | Un opérateur non technique, plusieurs étapes internes, public externe | Aucune trouvée | Experience Plane et Control Plane séparés | UI confuse ou dangereuse |
| INF-005 | INCONNU | L'intégration cloud est adaptée au P0 | Emplacement actuel des sources | Accès, coût, provider et rétention indéfinis | Garder l'intégration dans l'incubateur | Dépendance et exposition prématurées |

### Résultat de red team

INF-002 disait initialement : « L'utilisateur a besoin d'un système d'exploitation unifié pour toute son activité. » Le reviewer l'a rejetée comme trop large et peu falsifiable. Elle a été remplacée par l'hypothèse plus étroite ci-dessus.

## 6. Trois interprétations produit

### Interprétation A : assistant de publication

Un outil ciblé importe photos et notes choisies, propose un article structuré et prépare un brouillon de site pour approbation.

- Avantage : petit et testable.
- Risque : ne traite pas la curation plus large de l'activité.

### Interprétation B : workspace d'activité créative

Un workspace modulaire gère sources, projets éditoriaux, revue et livraison web, avec extensions futures pour la planification numérique.

- Avantage : correspond au workflow regroupé et à l'ambition long terme.
- Risque : peut devenir une console interne large au lieu d'un produit utilisable.

### Interprétation C : agence numérique autonome

Un système multi-agent gère stratégie de contenu, médias, site, développement, analytics et croissance.

- Avantage : capture l'ambition maximale implicite.
- Risque : périmètre sans preuve, autonomie dangereuse et forte charge d'exploitation.

### Décision

`[DÉCISION]` L'interprétation B est la vision active, implémentée d'abord par la verticale de publication de l'interprétation A. L'interprétation C va dans l'incubateur et n'est pas une roadmap engagée.

## 7. Registre de challenge

Contre-hypothèse la plus forte :

> Une convention de dossiers rigoureuse et un template de brouillon web pourraient résoudre l'essentiel sans nouveau produit.

Approche de falsification :

- Exécuter manuellement un workflow structuré avec les objets et états proposés.
- Mesurer temps de préparation, informations manquantes, cycles de révision et confusion.
- Si le workflow apporte peu, ne pas l'automatiser.

Extensions rejetées ou différées :

- publication autonome : rejetée par le commanditaire ;
- ingestion automatique du cloud : différée avant revue accès et confidentialité ;
- recommandations de développement commercial : incubées, hors P0 ;
- collaboration multi-utilisateur : différée jusqu'à l'existence d'un second opérateur réel.

## 8. Domain Atlas

| Domaine | Finalité | Dedans | Dehors | Owner |
| --- | --- | --- | --- | --- |
| Bibliothèque de sources | Enregistrer et curer les sources approuvées | Imports, métadonnées, sélection, provenance | Publication publique | Product owner |
| Projets éditoriaux | Transformer une sélection en brouillon structuré | Brief, draft, revue, révision | Credentials du site | Editorial owner |
| Livraison | Préparer et vérifier les packages publiables | Preview, validation, demande d'approbation, preuve de release | Stratégie éditoriale | Integration owner |
| Exploitation | Exposer runs, échecs, coûts, permissions et audit | Jobs, logs, gates, rollback | Parcours éditorial utilisateur | Opérateur |
| Incubateur projet | Conserver les candidats futurs | Hypothèses, propositions, idées rejetées | Contrats P0 actifs | Product owner |

## 9. Capability Atlas

| Capacité | Domaine | Acteur Et Résultat | Entrées Et Sorties | Zone De Sécurité | Disposition |
| --- | --- | --- | --- | --- | --- |
| Enregistrer une source | Bibliothèque | L'owner crée une source traçable | Fichiers et notes -> source | Verte en local | Candidate de fondation |
| Curer un ensemble | Bibliothèque | L'owner sélectionne des sources pertinentes | Sources -> sélection approuvée | Verte | Candidate de fondation |
| Créer un brief éditorial | Projets éditoriaux | L'owner cadre la page ou l'article | Sélection et intention -> brief | Verte | Candidate de fondation |
| Générer un draft structuré | Projets éditoriaux | L'owner reçoit une proposition révisable | Brief -> draft avec provenance | Verte | P0 active |
| Revoir et réviser | Projets éditoriaux | L'owner corrige et accepte | Draft -> révision acceptée | Verte | P0 active |
| Construire un preview | Livraison | L'owner voit le résultat exact | Révision -> package de preview | Verte | P0 active |
| Demander l'approbation | Livraison | L'owner reçoit une gate explicite | Preview -> registre d'approbation | Proposition orange | P0 active |
| Publier sur le site | Livraison | Le contenu approuvé atteint la cible | Package approuvé -> résultat public | Rouge | Différée avant audit réel |
| Inspecter la vérité du run | Exploitation | L'opérateur voit statut, erreurs, coûts et gates | Runs -> Control Plane | Verte | Candidate de fondation |
| Suggérer un projet numérique | Incubateur | L'owner voit un candidat traçable | Signal -> proposition | Proposition verte seulement | Incubateur |

## 10. Module Map

| Module | Capacités | Propriété | Interdiction |
| --- | --- | --- | --- |
| `source-registry` | Enregistrement et curation | Sources et provenance | Publication web |
| `editorial-workbench` | Brief, draft, revue, révision | Projet éditorial et états de révision | Credentials ou déploiement public |
| `delivery-package` | Preview et demande d'approbation | Release candidate immuable | Mutation des sources |
| `operations-ledger` | Vérité des runs | Événements, gates, coûts, échecs | Contenu éditorial utilisateur |
| `incubator` | Suggestions de projets | Candidats non acceptés | Contrats de fondation actifs |

Ces modules illustrent des frontières d'ownership, pas des packages technologiques imposés.

## 11. Objets et états

### SourceItem

```text
discovered -> registered -> reviewed -> approved
                         -> rejected
approved -> archived
```

Invariant : seuls les `SourceItem` en état `approved` peuvent entrer dans une release candidate.

### EditorialProject

```text
idea -> framed -> drafting -> in_review -> accepted
                       -> changes_requested -> drafting
accepted -> packaged
```

Invariant : chaque révision acceptée référence sa sélection de sources et l'acteur d'approbation.

### ReleaseCandidate

```text
prepared -> previewed -> approval_requested -> approved
                                      -> rejected
approved -> released -> verified
                  -> failed -> rolled_back
```

Invariant : `released` exige une approbation distincte, non expirée et liée au payload et à la cible exacts.

## 12. Composition inter-domaines

Composition : créer une mise à jour de site revue.

```text
L'owner sélectionne les SourceItems approuvés
  -> le projet éditorial crée un brief
  -> le drafting produit une révision avec provenance
  -> l'owner demande des changements ou accepte
  -> la Livraison construit un package de preview immuable
  -> l'Exploitation enregistre checks et coûts
  -> l'owner approuve ou rejette le package exact
  -> la publication reste bloquée dans l'alpha locale
```

Échecs partiels :

- Une image sans droits ou provenance bloque le packaging avec référence précise.
- Un échec de génération laisse le projet en `drafting` sans modifier la release.
- Un échec de preview préserve la révision acceptée pour un nouveau packaging.
- Une approbation expirée renvoie le package à `previewed` pour nouvelle revue.

## 13. UI Surface Map

### Experience Plane

Écran principal : « Créer une mise à jour du site »

1. Sélectionner les sources.
2. Décrire le résultat attendu.
3. Revoir la structure proposée.
4. Corriger et accepter le contenu.
5. Inspecter le preview exact.
6. Demander l'approbation de publication.

Le parcours par défaut ne montre ni workers, ni routing de modèles, ni coût en tokens, ni queues, ni logs bruts. Les parcours avancés exposent provenance, comparaison des révisions, alertes d'accessibilité et coût estimé.

### Control Plane

Les surfaces opérateur exposent :

- état des runs et queues ;
- modèles et outils utilisés ;
- erreurs et nombre de retries ;
- résultats des gates ;
- classe de données ;
- état et expiration des approbations ;
- hash du package et cible ;
- readiness du rollback.

## 14. P0 et verticales de falsification

### P0-1 : workflow manuel structuré

Objectif : tester si le modèle d'objets et le parcours de revue réduisent la friction avant automatisation.

Preuves : un projet synthétique sûr, temps des étapes, champs manquants, nombre de révisions, feedback du responsable et états rejetés ou modifiés.

### P0-2 : verticale locale de draft

Objectif : traverser les frontières locales réelles des fichiers sélectionnés jusqu'au draft persisté et au preview.

```text
import local
  -> source registry
  -> projet éditorial
  -> draft généré
  -> révision de l'owner
  -> preview local
  -> preuves d'exploitation
```

Exclusion explicite : aucune intégration cloud et aucun appel au site public.

### P0-3 : probe du contrat d'approbation

Objectif : prouver que l'approbation est liée à la cible et au payload exacts, expire, peut être rejetée et n'implique pas l'exécution.

Cette probe peut utiliser un adapter de publication fictif. Son résultat est `fixture-integrated`, pas une intégration réelle.

## 15. Foundation Freeze Candidate 0.1

Fondation acceptée :

- North Star : aider un opérateur créatif à transformer des sources traçables en publications numériques cohérentes et revues sans perdre le contrôle des actions externes.
- Domaines actifs : Bibliothèque de sources, Projets éditoriaux, Livraison, Exploitation.
- Incubateur : projets numériques plus larges.
- Objets : SourceItem, EditorialProject, Revision, ReleaseCandidate, Approval, RunEvidence.
- Règle UI : Experience Plane éditoriale simple et Control Plane opérationnel séparé.
- Autonomie : préparation locale A2 ; préparation d'intégration A3 ; publication rouge avec approbation exacte.
- Données : P0 local ; aucun secret ou credential cloud dans le contexte modèle.
- Contrats P0 : provenance, révisions, package immuable, approbation bornée, preuves de run.

Non gelé : provider web, cloud drive, rôles multi-utilisateur, analytics, publication automatique et exploitation autonome durable.

Résultat de la Freeze Gate : `accepted-with-reservations` pour l'alpha locale. Le contrat de publication est spécifié, mais ni autorisé ni intégré.

## 16. Roadmap

### Fondation P0

- exercer le workflow manuel ;
- construire la verticale locale ;
- valider états et provenance ;
- valider le contrat d'approbation avec fixture ;
- exécuter les revues confidentialité et menaces.

### Première release utilisable

- projets éditoriaux locaux répétables ;
- preview accessible et correction ;
- exports versionnés ;
- vérité opérationnelle ;
- backup et restauration.

### Release opérationnelle

- auditer l'adapter réel du site ;
- isoler les credentials hors du modèle ;
- tester l'intégration sandbox ;
- tester rollback et vérification de cible ;
- définir monitoring, incidents et support ;
- terminer les revues juridiques et d'accessibilité du produit public.

### Incubateur

- synchronisation cloud ;
- revue multi-utilisateur ;
- planification numérique ;
- apprentissage par analytics ;
- portefeuille d'agents plus large.

## 17. Trois missions parallèles

Les missions ne démarrent qu'après acceptation de Foundation Freeze Candidate 0.1.

### DEV-01 : Source Registry

- Ownership : module `source-registry` et tests.
- Entrées : contrat SourceItem, politique d'import local, fixtures synthétiques.
- Sorties : enregistrement, provenance, états de revue, tests de contrat.
- Interdit : modifier les états partagés ou les contrats de Livraison.

### DEV-02 : Editorial Workbench

- Ownership : module `editorial-workbench` et verticale Experience Plane.
- Entrées : contrats EditorialProject et Revision, carte d'états UX.
- Sorties : brief, draft, révision, acceptation, preuves d'accessibilité.
- Interdit : modifier le registre d'exploitation ou la politique d'approbation.

### DEV-03 : Operations Ledger

- Ownership : événements de run, preuves de gates, coûts et erreurs.
- Entrées : contrat d'événements et exigences Control Plane.
- Sorties : registre append-only et vue opérateur.
- Interdit : modifier contenu éditorial ou prompts de modèles.

```text
Foundation 0.1
  -> DEV-01
  -> DEV-02
  -> DEV-03

DEV-01 + DEV-02 + DEV-03
  -> INT-01 Local Draft Integration
  -> REV-01 Independent Review
  -> ACC-01 Local Alpha Acceptance
```

Les agents utilisent des workspaces isolés. Tout défaut de contrat partagé produit une Foundation Change Proposal, pas une réécriture locale.

## 18. Integration Gate

INT-01 doit prouver :

- la provenance des SourceItems survit jusqu'au preview ;
- les états invalides ne peuvent pas entrer dans un package ;
- les révisions conservent l'historique ;
- Experience Plane et Control Plane présentent des états compatibles ;
- un échec de draft ne fait pas progresser la release ;
- les logs ne contiennent pas de contenu source au-delà des métadonnées autorisées ;
- les checks d'accessibilité couvrent clavier, labels, erreurs et alternatives des images ;
- coûts et modèles sont visibles par l'opérateur ;
- les affirmations distinguent intégration locale et intégration réelle du site.

Exemple de résultat rejeté : DEV-02 livre un beau preview lisant directement des images depuis un dossier temporaire non suivi. L'integration owner le rejette, car provenance et reproductibilité échouent. Le builder doit utiliser les références SourceItem approuvées.

## 19. Acceptation de l'alpha locale

| Zone | État De Preuve |
| --- | --- |
| Source registry | Intégré localement |
| Editorial workbench | Vérifié end-to-end en local |
| Operations ledger | Intégré localement |
| Contrat d'approbation | Fixture-integrated |
| Publication web | Spécifiée seulement |
| Import cloud | Inconnu et incubé |
| Validation utilisateur | Une session commanditaire, insuffisante pour un public large |
| Readiness de release publique | Non prête |

Verdict : `accepted-with-reservations` comme alpha locale. Ce n'est ni un produit production-ready, ni un produit validé publiquement.

## 20. Gates avant publication réelle

Avant toute proposition de publication :

- inspecter API, preview, authentification, limites et rollback du site réel ;
- garder les credentials dans un mécanisme dédié hors prompts et logs ;
- vérifier site, environnement, route, payload et médias exacts ;
- implémenter dry-run ou staging ;
- tester identité du package et expiration de l'approbation ;
- exécuter checks sécurité, confidentialité, accessibilité, performance et liens ;
- définir information de confidentialité, support et incidents selon le cas ;
- assigner publisher et acceptance owner ;
- obtenir l'approbation exacte de la release candidate ;
- vérifier le résultat public et conserver les preuves de rollback.

La readiness n'est pas l'autorisation. Une gate technique verte ne remplace pas l'approbation de publication.

## 21. Apprentissage post-release

Supposons que les releases supervisées montrent :

- les visiteurs atteignent les projets mais ouvrent rarement les descriptions longues ;
- le responsable passe plus de temps à sélectionner les images qu'à réviser le texte ;
- les images mobiles chargent trop lentement ;
- une revue trouve des alternatives textuelles incohérentes.

Explications concurrentes : descriptions trop longues, public surtout visuel, hiérarchie masquant le récit ou échantillon non représentatif.

Décisions :

- `[DÉDUCTION FORTE]` La sélection d'images reste un coût important sur plusieurs releases.
- `[HYPOTHÈSE]` Une capacité de curation guidée pourrait le réduire.
- `[DÉCISION]` Créer un candidat de curation dans l'incubateur, sans sélection ni publication automatiques.
- `[DÉCISION]` Faire de la performance des images et des alternatives textuelles des gates opérationnelles.
- `[REJETÉ]` Ne pas supprimer les descriptions à partir de la seule profondeur de clic.

## 22. Proposition Foundation 0.2

Changements proposés :

- ajouter un objet ImageVariant et un contrat de performance ;
- ajouter les preuves d'accessibilité à ReleaseCandidate ;
- ajouter une curation guidée en A1 ;
- conserver la sélection finale manuelle ;
- ajouter des seuils réels de performance et accessibilité.

Inchangés : North Star, séparation Experience et Control Planes, approbation humaine de publication, provenance et package immuable.

La proposition exige des revues produit, accessibilité et ingénierie avant activation.

## 23. Snapshot de complétude

| Dimension | Niveau 0-5 | Preuve |
| --- | --- | --- |
| Couverture conceptuelle | 4 | Revue indépendante des domaines actifs et exclusions |
| Maturité des inférences | 3 | Hypothèses clés exercées localement ; preuves du public encore faibles |
| Readiness de fondation | 4 pour l'alpha locale | Candidate acceptée avec réserves |
| Verticales P0 intégrées | 3 | Composants locaux réels ; adapter web fixture-only |
| UX et accessibilité | 3 | Parcours local testé ; validation large incomplète |
| Sécurité et confidentialité | 2 | Politiques spécifiées ; frontières réelles non exercées |
| Déploiement et exploitation | 1 | Cadrés seulement |
| Validation humaine et utilisateur | 2 | Preuves du commanditaire uniquement |
| Rollback | 1 | Récupération locale cadrée ; rollback public non testé |

Aucune déclaration globale à 99 % n'est crédible. Le prochain progrès légitime est une intégration sandbox avec le vrai site et des preuves de rollback, puis une revue indépendante de release publique.

## 24. Ce que démontre l'exemple

L'exemple montre comment la méthode :

- part d'un langage courant ambigu ;
- pose un ensemble borné de questions décisives ;
- évite le profilage personnel clandestin ;
- sépare faits, hypothèses et inconnues ;
- compare trois interprétations ;
- conserve le scope rejeté ;
- cartographie domaines, capacités, modules, objets, états, compositions et UI ;
- teste une fondation par verticales de falsification ;
- lance des agents isolés sur des contrats communs ;
- rejette une sortie esthétique mais invalide ;
- distingue fixture et intégration réelle ;
- garde la publication derrière une gate humaine ;
- révise la fondation à partir de preuves sans réécrire la North Star.
