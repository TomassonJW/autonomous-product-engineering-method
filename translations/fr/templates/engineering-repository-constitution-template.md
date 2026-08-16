# Template de constitution du dépôt d'ingénierie

Utiliser ce template pour compiler une mémoire produit riche en un dépôt qu'un agent de développement peut reprendre.

Le template définit des fonctions, pas un nombre obligatoire de fichiers. Un petit produit peut fusionner des sections ; un produit complexe peut les séparer davantage. Préserver l'ordre d'autorité et la provenance.

## Statut du dépôt

- Projet :
- Dépôt :
- Visibilité : privé / public
- Identifiant de mémoire produit :
- Version de mémoire produit :
- Date de compilation :
- Version de méthode :
- Versions des canons locaux :
- Branche de baseline :
- Commit de baseline :
- Tag de baseline :
- Prêt à compiler : pass / fail
- Prêt à développer : pass / fail
- Propriétaire du développement :
- Propriétaire de l'acceptation produit :

## `AGENTS.md`

Définir :

- mission du dépôt ;
- ordre d'autorité ;
- propriétaire du Git opérationnel ;
- politique de branches et worktrees ;
- politique de changement de fondation produit ;
- règles sécurité et secrets ;
- ordre de lecture obligatoire ;
- ouverture et clôture de session ;
- conditions d'arrêt ;
- attentes de reporting ;
- première preuve bornée ;
- gate UI et arrêt explicite lorsqu'une interface existe.

## `README.md`

Inclure :

- résumé produit en un paragraphe ;
- maturité actuelle ;
- carte du dépôt ;
- ordre de lecture canonique ;
- commande de démarrage de l'agent ;
- baseline actuelle ;
- déclaration de confidentialité ;
- liens vers constitution et provenance.

## `product/00-index.md`

- Version produit active :
- Finalité :
- Niveau d'ambition :
- Périmètre :
- Non-objectifs :
- Documents canoniques :
- Ordre de lecture :
- Décisions bloquantes :
- Première preuve bornée :
- Propriétaire de l'acceptation :
- Procédure d'amendement :

## `product/vision-and-value.md`

### Problème actuel

### État futur désiré

### Finalité du produit

### Valeur par groupe utilisateur

### Situations critiques

### Preuves de réussite

### Signaux d'échec et de dérive

### Alternatives sérieuses

## `product/users-and-journeys.md`

Pour chaque utilisateur ou rôle :

- responsabilités ;
- contexte et appareils ;
- niveau de maîtrise ;
- jobs critiques ;
- parcours principaux ;
- permissions ;
- besoins d'accessibilité ;
- besoins d'échec et de reprise.

## `product/domain-and-rules.md`

### Vocabulaire canonique

### Objets et propriété

### États et transitions

### Invariants

### Règles et exceptions

### Responsabilités humaines

### Sources de vérité

### Ambiguïtés à ne pas transformer automatiquement en concepts techniques

## `product/product-experience.md`

### Architecture de l'information

### Outils, modules, vues et pages

### Actions et permissions

### États vides, chargements, erreurs et confirmations

### Desktop, tablette et mobile

### Densité, thèmes, accessibilité et préférences

### Fixtures représentatives

### Sauvegarde, brouillon, Undo, historique et reprise

### Décisions sur les capacités UI

Accepter, différer ou rejeter explicitement onglets, split view, palette de commandes, workspaces, restauration de session, deep links, mode focus, actions groupées, drag and drop et notifications actionnables.

## `product/ui-contract.md`

Omettre ce fichier lorsqu'aucune interface n'existe.

Épingler :

- canon UI applicable et version ;
- exceptions locales ;
- modèle de navigation ;
- coquille persistante ;
- registre des pages ;
- politique responsive ;
- préférences et persistance ;
- première gate visible ;
- condition d'arrêt explicite ;
- preuves d'acceptation.

## `product/data-and-integrations.md`

### Sources existantes

### Propriété des données

### Données maîtresses, dérivées, calculées et temporaires

### Import, export, migration et synchronisation

### APIs obligatoires et optionnelles

### Données sensibles

### Rétention, suppression et portabilité

### Inconnues à auditer

## `product/scope-and-risks.md`

### Inclus

### Exclus

### Niveau d'ambition actuel

### Couverture attendue du premier prototype

### Conditions de changement d'échelle

### Sécurité et confidentialité

### Conformité

### Hébergement et exploitation

### Coûts et dépendances payantes

### Maintenance et réversibilité

### Dépendances humaines

### Risques actifs

## `product/decisions-and-unknowns.md`

Utiliser des statuts explicites :

- `[FACT]`
- `[DECISION]`
- `[HYPOTHESIS]`
- `[PROPOSAL]`
- `[UNKNOWN]`
- `[CONSTRAINT]`

Pour chaque élément matériel :

- énoncé ;
- propriétaire ;
- raison ou sources ;
- alternatives ;
- conséquence produit ;
- risque si faux ;
- statut bloquant ;
- déclencheur de revue.

## `product/acceptance-gates.md`

Séparer lorsque pertinent :

- cohérence de la mémoire ;
- Prêt à compiler ;
- Prêt à développer ;
- faisabilité ;
- conformité produit ;
- UX et lisibilité ;
- couverture ;
- cohérence des données ;
- correction technique ;
- sécurité et exploitation ;
- acceptation explicite du product owner.

Une réussite technique n'est pas une acceptation produit.

## `provenance/COMPILATION-MANIFEST.yml`

Utiliser [source-compilation-manifest-template.yml](../../../templates/source-compilation-manifest-template.yml).

## `provenance/SOURCE-MAP.md`

Pour chaque fonction compilée :

| Fichier ou section compilé | Identifiants sources | Statut | Notes |
| --- | --- | --- | --- |
| | | fait / décision / hypothèse / mixte | |

Lister aussi :

- sources non lues ;
- sources restreintes référencées sans copie ;
- branches omises ;
- redactions ;
- contradictions non résolues ;
- limites de fraîcheur connues.

## `provenance/PRODUCT-CHANGELOG.md`

Enregistrer baselines et amendements :

| Version | Date | Baseline ou PR | Changement produit | Version mémoire source | Propriétaire |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

## Checklist Prêt à développer

- [ ] Le dépôt est compréhensible sans l'espace de mémoire.
- [ ] `AGENTS.md` définit autorités et propriété du Git opérationnel.
- [ ] La constitution est cohérente et suffisante pour la première preuve bornée.
- [ ] Les contradictions bloquantes sont résolues ou explicites.
- [ ] La provenance et le mapping des sources existent.
- [ ] Secrets et données privées inutiles sont absents.
- [ ] Versions de méthode et canons locaux sont épinglées.
- [ ] Le commit de baseline est identifiable.
- [ ] La commande de démarrage existe.
- [ ] Le contrat UI et la première gate d'arrêt existent si nécessaire.
- [ ] L'acceptation du product owner n'est pas pré-déclarée.

## Commande de démarrage de l'agent

```text
Reprends ce projet depuis le dépôt [OWNER/REPO], baseline [TAG OU COMMIT]. Clone ou mets à jour le checkout local, puis lis AGENTS.md, le manifeste de compilation et toute la constitution produit dans l'ordre indiqué. Vérifie Prêt à développer. Tu possèdes le Git opérationnel, le pilotage local et l'implémentation. Ne rouvre pas l'espace de mémoire produit sauf amendement explicite. Exécute le préflight borné et uniquement la première preuve autorisée. Respecte chaque gate d'arrêt humain explicite.
```
