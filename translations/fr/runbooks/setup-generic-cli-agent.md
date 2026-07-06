# Setup agent CLI générique

Utiliser ce runbook pour des agents orientés terminal qui peuvent inspecter des fichiers, modifier des dépôts et lancer des commandes.

## Checklist de démarrage

- Confirmer le répertoire de travail.
- Vérifier le statut Git.
- Identifier les fichiers sûrs à lire.
- Exclure secrets et fichiers privés.
- Lire les docs avant le code pour tout travail non trivial.
- Classer la zone de sécurité.
- Définir les commandes de vérification.

## Pattern d'exécution

```text
inspecter -> planifier -> modifier -> tester -> diff -> rapporter
```

## Sécurité des commandes

L'agent doit éviter :

- commandes destructives ;
- suppressions récursives larges ;
- force pushes ;
- commandes qui impriment des variables d'environnement ;
- commandes qui uploadent, publient ou envoient des messages ;
- installations de packages sans approbation quand elles ajoutent risque ou coût réseau.

## Contrat de sortie

Le rapport final doit inclure :

- fichiers changés ;
- décisions ;
- commandes ;
- preuves ;
- checks ignorés ;
- limites ;
- risques ;
- prochaine action.

## Conditions d'arrêt

S'arrêter quand :

- la tâche nécessite un secret ;
- l'état du dépôt ne correspond pas aux hypothèses ;
- une action rouge est requise ;
- les tests ne peuvent pas tourner et aucune preuve alternative n'existe ;
- le scope dépasse la mission.
