# Vision-to-Product Control Pack Template

Utiliser cet artefact compact pour un projet petit ou moyen. Scinder les sections en sources de vérité dédiées lorsqu'elles acquièrent des owners, sensibilités, gates de revue ou rythmes de mise à jour différents.

## 1. Métadonnées de contrôle

- Projet :
- Version du Control Pack :
- Mouvement actif : Comprendre / Diverger / Stabiliser / Construire / Observer
- Product owner :
- Engineering owner :
- Acceptance owner :
- Version active de Foundation Freeze :
- Dernière revue :
- Prochain événement de revue obligatoire :

## 2. Vision brute

Conserver les mots d'origine.

> `<vision initiale de l'utilisateur>`

## 3. Interprétation active

### Intention reformulée

### État futur désiré

### Problème principal

### Interprétation produit active

### Interprétations rejetées ou différées

| Interprétation | Disposition | Preuves Et Raison |
| --- | --- | --- |
|  |  |  |

### North Star

> `<finalité durable du produit>`

### Non-objectifs

-

## 4. Trois vues de profilage

Ne collecter que les informations nécessaires à la finalité projet déclarée.

### Profil du commanditaire

- Objectifs :
- Autorité de décision :
- Préférences déclarées :
- Contraintes :
- Preuves de réussite :
- Corrections ou refus à conserver :

### Profil du public

| Public | Tâche | Contexte | Niveau De Maîtrise | Besoin D'Accessibilité | Risque Principal |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

### Profil situationnel

- Workflow existant :
- Produit ou contournement existant :
- Organisation et contexte d'exploitation :
- Environnement technique :
- Contraintes marché ou métier :
- Contexte réglementaire :
- Calendrier et ressources :

## 5. Registre des indices et inférences

| ID | Statut | Affirmation | Sources | Contre-Preuves | Conséquence Produit | Risque Si Faux | Owner | Déclencheur De Revue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| INF-001 | FAIT / INDICE / HYPOTHÈSE / DÉDUCTION FORTE / INCONNU / DÉCISION / CONTRAINTE / GATE HUMAINE |  |  |  |  |  |  |  |

### Corrections utilisateur

| Entrée | Correction | Affirmation Remplacée | Date | Conséquence |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## 6. Budget de questions adaptatives

| Question | Décision Qu'Elle Peut Modifier | Pourquoi Elle Ne Peut Pas Être Déduite Sûrement | Statut |
| --- | --- | --- | --- |
|  |  |  |  |

Preuve de sortie de l'entretien :

- [ ] Interprétation active explicite.
- [ ] Public et résultat principal exploitables.
- [ ] Contradictions majeures résolues ou possédées.
- [ ] Données et actions externes avec classes de risque préliminaires.
- [ ] Une question supplémentaire a peu de chances de changer la prochaine étape bornée.

## 7. Registre de challenge

- Contre-hypothèse la plus forte :
- Workflow concurrent plus simple :
- Interprétation système plus large :
- Preuve qui invaliderait l'interprétation active :
- Résultat probable techniquement complet mais inutilisable :
- Charge d'exploitation ou de conformité cachée :
- Responsable de décision :
- Résultat du challenge : réussite / échec / décision nécessaire

## 8. Cartographie produit

### Domain Atlas

| Domaine | Finalité | Dedans | Dehors | Owner | Classe De Données | Risque Principal |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

### Capability Atlas

| Capacité | Domaine | Acteur Et Résultat | Entrées Et Sorties | Parcours | Zone De Sécurité | Maturité | Disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |

### Module Map

| Module | Capacités Réalisées | Données Possédées | Contrats Publics | Dépendances Interdites | Frontière De Test | Owner |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

### Object And State Catalog

| Objet | Domaine Propriétaire | États | Transitions Valides | Permission De Transition | Invariant | Rétention |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

### Compositions inter-domaines

| Composition | Déclencheur | Capacités | Contrats | Échec Partiel | Vérité Utilisateur Finale | Preuve |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

### UI Surface Map

| Surface | Experience Ou Control Plane | Acteur | Tâche | Vérité Exposée | Parcours Avancé | Risque D'Accessibilité |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

### Carte des permissions et de l'autonomie

| Action | Demandeur | Approbateur | Exécuteur | Niveau D'Autonomie | Classe De Données | Effet Externe | Rollback | Preuve D'Audit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |

## 9. Exploration et curation

### Passages d'exploration

| Angle Ou Passage | Nouveaux Domaines | Nouveaux Objets Ou Invariants | Nouvelles Menaces | Nouveaux Parcours | Impact Décisionnel |
| --- | --- | --- | --- | --- | --- |
| Produit attendu |  |  |  |  |  |
| Concurrent plus simple |  |  |  |  |  |
| Système plus large |  |  |  |  |  |

### Décisions de curation

| Candidat | Disposition | Cible De Fusion Ou Division | Preuves | Owner De Décision |
| --- | --- | --- | --- | --- |
|  | active / foundation-candidate / incubator / deferred / merged / split / rejected / superseded |  |  |  |

### Résultat de saturation

- Deux passages d'exploration indépendants revus :
- Nouveau domaine P0 trouvé :
- Nouvel objet partagé ou invariant trouvé :
- Nouvelle action rouge ou menace matérielle trouvée :
- Contradiction non résolue bloquant la stabilisation :
- Saturé pour la décision actuelle : oui / non
- Preuves :

## 10. Foundation Freeze Candidate

- Version candidate :
- Version de North Star et vision :
- Domaines inclus :
- Capacités et compositions principales :
- Objets, états et invariants partagés :
- Principes Experience et Control Plane :
- Politique de permissions et autonomie :
- Politique données, confidentialité et sécurité :
- ADR et contrats acceptés :
- Concepts exclus, différés et incubés :
- Risques et inconnues :

### Verticales de falsification

| Verticale | Hypothèse Risquée Testée | Frontières Réelles Traversées | Résultat | Preuve | Conséquence Sur La Fondation |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

### Freeze Gate

| Exigence | Réussite / Échec / Décision Nécessaire | Preuve | Owner |
| --- | --- | --- | --- |
| Cartes curées |  |  |  |
| Objets et états partagés |  |  |  |
| Contrats versionnés |  |  |  |
| Verticales P0 de falsification |  |  |  |
| Alternatives et décisions rejetées |  |  |  |
| Revue sécurité et confidentialité |  |  |  |
| Stratégie de changement et rollback |  |  |  |
| Acceptation produit |  |  |  |
| Acceptation ingénierie |  |  |  |

## 11. Roadmap et portefeuille de missions de build

### Horizons

| Horizon | Résultat | Verticales Incluses | Explicitement Exclu | Preuve De Sortie |
| --- | --- | --- | --- | --- |
| Fondation P0 |  |  |  |  |
| Première release utilisable |  |  |  |  |
| Release opérationnelle |  |  |  |  |
| Incubateur |  |  |  |  |

### Portefeuille de missions

| Mission | Verticale | Dépendances | Workspace Et Ownership | Entrées | Sorties | Sécurité | Budget Et Timeout | Tests | Reviewer | Integration Owner |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |

### DAG d'exécution

```text
<graphe des dépendances de missions>
```

## 12. Sécurité, confidentialité et conformité

### Carte des données

| Donnée | Finalité | Source | Classe | Destinataire Ou Processor | Lieu | Rétention | Suppression | Accès | Owner D'Incident |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |

### Menaces et abuse cases

| Menace Ou Abuse Case | Actif | Acteur | Impact | Contrôle | Risque Résiduel | Owner De Gate |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

### Revue juridique et organisationnelle

- Contexte produit : privé / interne / public ou commercial
- Responsable de traitement et sous-traitants, si applicable :
- Finalités et bases légales, si applicable :
- Droits utilisateurs et contrôles de préférences :
- Politique de rétention et suppression :
- Revue des transferts et vendors :
- Obligations d'accessibilité :
- Obligations de modération ou prévention des abus :
- AIPD/DPIA ou revue juridique qualifiée nécessaire :
- Déclaration explicite : cet artefact n'est pas un certificat de conformité.

## 13. Intégration et acceptation

### Preuves d'intégration

| Mission | Patch Ou Commit | Version De Fondation | Contrats | Tests | État D'Intégration Réelle | Risques | Résultat |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |

### États de preuve

- Spécifié :
- Implémenté :
- Testé unitairement :
- Intégré avec fixtures :
- Intégré :
- Vérifié end-to-end :
- Validé utilisateur :
- Release-ready :
- Released :
- Validé en exploitation :

### Acceptation indépendante

- Builder :
- Reviewer :
- Integration owner :
- Acceptance owner :
- Publisher ou deployer :
- Résultat : accepted / accepted-with-reservations / rejected / decision-needed
- Preuves :
- Réserves et owners :

## 14. Estimation de complétude

| Dimension | Poids | Niveau 0-5 | Preuves | Confiance | Prochain Événement Légitime De Progression |
| --- | --- | --- | --- | --- | --- |
| Couverture conceptuelle |  |  |  |  |  |
| Cohérence des domaines |  |  |  |  |  |
| Maturité des inférences |  |  |  |  |  |
| Readiness de la fondation |  |  |  |  |  |
| Couverture des contrats |  |  |  |  |  |
| Verticales P0 intégrées |  |  |  |  |  |
| UX et accessibilité |  |  |  |  |  |
| Sécurité et confidentialité |  |  |  |  |  |
| Tests et intégration réelle |  |  |  |  |  |
| Déploiement et exploitation |  |  |  |  |  |
| Validation humaine et utilisateur |  |  |  |  |  |
| Revue de conformité |  |  |  |  |  |
| Capacité de rollback |  |  |  |  |  |

- Estimation pondérée :
- Confiance :
- Inconnues :
- Avertissement de réalisme :

## 15. Gate d'action externe

- Action exacte :
- Cible et environnement :
- Référence d'approbation humaine :
- Payload ou change set revu :
- Minimisation des données et base :
- Preuve de dry-run :
- Rollback ou compensation :
- Logs redacted :
- Check exécutable du périmètre :
- Vérification du résultat :
- Autorisation finale : accordée / refusée / expirée

## 16. Apprentissage et évolution de la fondation

| Signal, Feedback, Incident Ou Métrique | Source | Explications Concurrentes | Inférence Mise À Jour | Capacité Ou Changement Candidat | Décision |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

### Foundation Change Proposal

- Déclencheur et preuves :
- Contrats, domaines, parcours et workers affectés :
- Alternatives :
- Impact de compatibilité et migration :
- Tests :
- Rollback :
- Owner de décision :
- Version cible de fondation :

## 17. Vérité actuelle et prochaine action

- État actuellement vérifié :
- Ce qui reste simulé ou fixture-only :
- Ce qui reste inconnu :
- Décision bloquante :
- Résultat non bloqué de plus forte valeur :
- Action explicitement non autorisée :
