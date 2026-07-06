# Pattern wrapper et checkpoint

Les workers longs ont besoin d'une limite runtime.

## Responsabilités du wrapper

Le wrapper doit :

- démarrer le worker ;
- passer un paquet de contexte borné ;
- faire respecter temps et quota ;
- collecter les logs ;
- écrire le statut ;
- détecter les échecs répétés ;
- arrêter en cas de risque critique ;
- demander approbation humaine si nécessaire ;
- vérifier que le rapport final existe.

## Forme du checkpoint

Chaque checkpoint doit enregistrer :

- tâche courante ;
- artefacts modifiés ;
- tests ou checks lancés ;
- échecs ;
- état quota ;
- prochaine action autorisée ;
- approbation nécessaire.

## Autorité finale

Le worker peut proposer la complétion. Le wrapper, superviseur ou reviewer humain l'accepte ou la rejette selon les gates et les preuves.
