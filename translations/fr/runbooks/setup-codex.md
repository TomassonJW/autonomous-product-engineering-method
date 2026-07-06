# Setup Codex

Utiliser ce runbook quand la méthode est appliquée dans un workflow Codex sur dépôt local.

## Préconditions

- Le dépôt est local et versionné.
- La tâche est bornée.
- L'agent a le droit de lire les fichiers projet publics et sûrs.
- Les secrets sont exclus du contexte.
- Le statut Git est vérifié avant toute modification.

## Démarrage sûr

1. Lire la tâche.
2. Inspecter le statut du dépôt.
3. Lire les docs et fichiers source pertinents.
4. Identifier les fichiers sensibles à ne pas ouvrir.
5. Classer la tâche en verte, orange ou rouge.
6. Produire un plan court pour tout travail non trivial.

## Règles d'opération Codex

- Utiliser les patterns existants du projet.
- Faire des changements petits et bornés.
- Ajouter ou adapter les tests selon le risque.
- Lancer les checks disponibles.
- Relire le diff avant le rapport final.
- Ne jamais revert des changements utilisateur sans demande explicite.
- Ne jamais force push.
- Ne jamais demander à l'utilisateur de coller des secrets.

## Preuves à capturer

- fichiers modifiés ;
- commandes lancées ;
- résultats de tests ;
- checks ignorés et raisons ;
- risques connus ;
- prochaine action recommandée.

## Conditions d'arrêt

S'arrêter et demander avant :

- changements d'architecture sans ADR ;
- commandes destructives ;
- release publique ;
- changements production ;
- gestion de credentials ;
- appels externes coûteux ;
- propriété de fichiers incertaine.
