# Adapter Hermes

Hermes est traité comme un environnement d'ingénierie autonome durable qui reprend un dépôt versionné, pas comme un chatbot obligé de reconstruire le produit depuis chaque note historique.

## Entrée préférée

Pour un projet durable ou complexe, Hermes démarre depuis un dépôt d'ingénierie ayant passé la gate Prêt à développer.

Le dépôt contient déjà :

- `AGENTS.md` ;
- une constitution produit active ;
- les gates d'acceptation ;
- un manifeste de compilation et une source map ;
- les versions épinglées de la méthode et des canons locaux ;
- un commit de baseline ;
- la première preuve bornée et les conditions d'arrêt.

Hermes n'a pas besoin d'un accès ordinaire à l'espace de mémoire produit d'origine.

## Séquence de reprise

1. Cloner ou mettre à jour le dépôt sans détruire de travail local.
2. Vérifier remote, branche, commit de baseline et manifeste.
3. Lire `AGENTS.md`, le manifeste et toute la constitution.
4. Produire une carte de couverture.
5. Remonter seulement contradictions matérielles, autorité manquante ou accès indispensable absent.
6. Créer ou mettre à jour roadmap, backlog, état, ADR et handoff.
7. Posséder Git opérationnel, implémentation, tests, intégration, déploiement et rollback.
8. Préserver les documents de fondation produit et proposer explicitement les changements matériels.
9. Exécuter le préflight borné.
10. Réaliser uniquement la première preuve autorisée et respecter chaque gate d'arrêt humain.

## Sessions ordinaires

Reprendre depuis :

- état Git live ;
- fichier d'état courant ;
- handoff courant ;
- backlog ou board actif ;
- ADR et contrats produit pertinents.

Ne pas rouvrir l'espace de mémoire produit sauf amendement explicite.

## Responsabilité Git

Hermes possède par défaut :

- clone local ;
- branches et worktrees ;
- commits d'implémentation ;
- intégration ;
- tags techniques ;
- corrections tests et CI ;
- rollback ;
- état et handoff.

Un architecte produit ou agent conversationnel peut compiler les baselines produit et préparer les pull requests d'amendement. Cela ne retire pas à Hermes la propriété quotidienne du Git d'ingénierie.

## Projets avec UI

Lorsqu'une UI existe :

- lire le canon UI épinglé et le contrat UI local avant conception ;
- charger la procédure UI canonique de l'environnement ;
- implémenter uniquement la première gate visible autorisée par le dépôt ;
- s'arrêter lorsque le contrat exige l'acceptation humaine ;
- ne pas déduire d'un build vert que le produit est accepté.

## Forces

- Missions longues.
- Git et état projet persistants.
- Patterns wrapper et checkpoint.
- Boucles de reporting.
- Golden paths pour workflows répétés.
- Autonomie consciente des quotas.
- Maintien de roadmap, état, handoff et preuves dans le dépôt.

## Risques

- Faux succès.
- Pauses quota silencieuses.
- Auto-certification du worker.
- Logs sans statut exploitable.
- Rapports contenant du contexte privé.
- Notifications externes sans approbation.
- Dérive produit lorsque l'implémentation modifie silencieusement la constitution.
- Relecture de mémoire brute au lieu de la baseline compilée.
- Propriété ambiguë entre Git de compilation produit et Git d'ingénierie.

## Adaptation de la méthode

Le travail Hermes est défini par :

- dépôt Prêt à développer ;
- charte de mission ;
- constitution produit ;
- golden path ;
- wrapper ;
- contrat de checkpoint ;
- fichier d'état ;
- handoff ;
- politique de quota ;
- autorité de rapport final ;
- politique de notification.

## Besoins du Control Plane

Exposer :

- dépôt et baseline ;
- mission actuelle ;
- dernier checkpoint ;
- état de queue ;
- gates échouées ;
- état quota ;
- statut du rapport final ;
- besoins d'approbation ;
- statut des amendements produit.

## Références utiles

- [De la mémoire produit au dépôt d'ingénierie](../docs/21-product-memory-to-engineering-repository.md)
- [Template de constitution du dépôt](../templates/engineering-repository-constitution-template.md)
- [Prompt de compilation](../prompts/starter-prompts/compile-product-memory-to-repository.md)
- [Préparer un run Hermes](../prompts/starter-prompts/prepare-hermes-worker-run.md)
