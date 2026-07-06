# Vue d'ensemble des adapters

Le cœur de la méthode est indépendant des outils. Les adapters traduisent la méthode dans les contraintes d'un environnement spécifique.

## Ce qu'un adapter définit

Un adapter doit définir :

- comment l'agent reçoit les missions ;
- comment le contexte est chargé ;
- où le statut est écrit ;
- comment les fichiers sont modifiés ;
- comment les tests sont lancés ;
- comment les approbations sont demandées ;
- comment les secrets sont évités ;
- comment les coûts sont estimés ;
- comment les rapports finaux sont produits ;
- ce que l'outil ne doit jamais faire automatiquement.

## Adapters disponibles

- [Codex](../adapters/codex.md) : travail local de dépôt, patches, tests, hygiène Git, rapports de revue.
- [Hermes](../adapters/hermes.md) : workers durables, wrappers, checkpoints, reporting.
- [Generic CLI Agent](../../adapters/generic-cli-agent.md) : agent autonome orienté terminal. Source anglaise non traduite dans cette passe.
- [Generic Chatbot](../../adapters/generic-chatbot.md) : chatbot sans accès filesystem par défaut. Source anglaise non traduite dans cette passe.

## Limite de l'adapter

Un adapter peut changer la mécanique d'exécution, mais il ne doit pas affaiblir la méthode centrale :

- pas de faux succès ;
- pas d'action rouge sans approbation ;
- pas d'exposition de secrets ;
- pas de code direct avant profilage et challenge pour un travail complexe ;
- pas d'UI hybride ;
- pas de boucles de coût non contrôlées.

## Créer un nouvel adapter

Partir de :

1. capacités de l'outil ;
2. limites de l'outil ;
3. modèle de sécurité ;
4. modèle de chargement de contexte ;
5. preuves d'exécution ;
6. contrat de reporting.

Puis écrire le plus petit runbook permettant à l'utilisateur d'opérer la méthode en sécurité dans cet outil.
