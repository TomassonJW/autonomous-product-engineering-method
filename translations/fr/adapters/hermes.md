# Adapter Hermes

Hermes est traité comme un environnement de worker autonome durable.

## Forces

- Missions longues.
- Patterns wrapper et checkpoint.
- Boucles de reporting.
- Golden paths pour workflows répétés.
- Utile pour autonomie consciente des quotas.

## Risques

- Faux succès.
- Pauses quota silencieuses.
- Auto-certification par le worker.
- Logs sans statut exploitable.
- Rapports contenant du contexte privé.
- Notifications externes sans approbation.

## Adaptation de la méthode

Le travail Hermes doit être défini par :

- charte de mission ;
- golden path ;
- wrapper ;
- contrat de checkpoint ;
- fichier de statut ;
- politique de quota ;
- autorité de rapport final ;
- politique de notification.

## Besoins du Control Plane

Exposer :

- mission actuelle ;
- dernier checkpoint ;
- état de queue ;
- gates échoués ;
- état quota ;
- statut du rapport final ;
- besoins d'approbation.

## Prompt utile

Utiliser [prepare-hermes-worker-run.md](../prompts/starter-prompts/prepare-hermes-worker-run.md).
