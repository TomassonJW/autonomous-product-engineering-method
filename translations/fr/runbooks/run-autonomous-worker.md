# Lancer un worker autonome

Ce runbook définit un cycle de vie générique pour worker autonome.

## 1. Créer la charte de mission

Utiliser [worker-mission-charter-template.md](../templates/worker-mission-charter-template.md).

La charte doit définir objectif, scope, zone de sécurité, budget, checkpoints, gates, conditions d'arrêt et exigences de rapport final.

## 2. Préparer le paquet de contexte

Inclure seulement :

- mission ;
- artefacts pertinents ;
- décisions acceptées ;
- contraintes ;
- outils autorisés ;
- fichiers ou systèmes affectés ;
- politiques de sécurité et coût.

Ne pas inclure de secrets ni d'historique inutile.

## 3. Exécuter par cycles

Chaque cycle doit :

1. sélectionner la prochaine tâche ;
2. agir dans le scope ;
3. écrire un artefact ou checkpoint ;
4. lancer les checks pertinents ;
5. mettre à jour le statut ;
6. décider continuer, pause ou arrêt.

## 4. Appliquer les gates

Avant complétion, vérifier :

- Truth Gate ;
- Safety Gate ;
- Cost Gate ;
- Journey Gate ;
- Product Honesty Gate.

## 5. Rapport final

Le rapport final doit distinguer :

- terminé avec preuve ;
- terminé avec écarts connus ;
- partiellement terminé ;
- bloqué ;
- échoué.

Ne pas accepter "done" comme statut sans preuve de support.
