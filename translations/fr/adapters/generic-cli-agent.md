# Adapter agent CLI générique

Un agent CLI générique peut opérer localement, mais sa sécurité dépend de la discipline des commandes, des limites de contexte et de la vérification.

## Forces

- Inspection de fichiers.
- Éditions locales.
- Exécution de scripts.
- Runs de tests.
- Workflow Git.

## Risques

- Commandes shell destructives.
- Lectures de fichiers trop larges.
- Fuite d'environnement.
- Appels réseau.
- Écritures cachées.
- Preuve finale faible.

## Adaptation de la méthode

Exiger :

- confirmation du répertoire de travail ;
- exclusion des secrets ;
- statut Git avant modifications ;
- plan avant changements non triviaux ;
- éditions bornées ;
- tests ou checks ;
- revue de diff ;
- rapport final.

## Biais de commande sûre

Préférer l'inspection en lecture seule avant mutation. Éviter les commandes qui impriment des variables d'environnement, uploadent des données, suppriment récursivement ou modifient des systèmes externes.

## Runbook utile

Utiliser [setup-generic-cli-agent.md](../runbooks/setup-generic-cli-agent.md).
