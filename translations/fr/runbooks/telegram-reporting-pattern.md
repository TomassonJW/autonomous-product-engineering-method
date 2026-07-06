# Pattern de reporting Telegram

Telegram ou des notifications chat peuvent être utiles pour des workers longs, mais ce sont des messages externes et doivent être traités avec prudence.

## Quand l'utiliser

Utiliser les notifications pour :

- complétion de worker ;
- statut bloqué ;
- gates échoués ;
- pauses quota ;
- demandes d'approbation humaine ;
- arrêts urgents de sécurité.

## Quoi envoyer

Envoyer des résumés courts et sanitizés :

- nom de mission ;
- statut ;
- lien ou référence locale vers l'artefact clé ;
- approbation nécessaire ;
- prochaine action.

## Quoi ne pas envoyer

Ne pas envoyer :

- secrets ;
- logs privés ;
- stack traces brutes avec chemins sensibles ;
- données client non publiées ;
- informations personnelles ;
- prompts complets contenant du contexte privé.

## Approbation

Envoyer des messages est un effet externe. Pour tout nouveau canal de reporting, exiger une approbation explicite avant activation.

## Template de message

```text
Mission: <nom>
Status: <completed | blocked | failed | approval needed>
Evidence: <référence d'artefact sûre>
Risk: <none | low | medium | high>
Next: <action>
```
