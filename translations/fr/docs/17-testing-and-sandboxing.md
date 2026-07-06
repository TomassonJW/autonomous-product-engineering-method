# Tests et sandboxing

Le travail autonome doit être testable. Un artefact généré ne suffit pas.

## Types de tests

Utiliser les tests adaptés à la tranche produit :

- tests unitaires ;
- tests d'intégration ;
- smoke tests ;
- checks HTTP ;
- tests de parcours UI ;
- checks d'accessibilité ;
- checks statiques de sécurité ;
- tests sans écriture externe ;
- tests de rollback ;
- tests de vérité du statut ;
- checks de budget coût ;
- checks de structure documentaire ;
- checks de liens.

## Règle de sandbox

Les effets externes doivent être remplacés par des modes sandbox, dry-run ou mock jusqu'à approbation de l'action réelle par l'utilisateur.

Exemples :

- rédiger un message au lieu de l'envoyer ;
- préparer une release GitHub au lieu de la publier ;
- utiliser une base de test au lieu de la production ;
- simuler un paiement au lieu de facturer ;
- produire un plan de migration avant de l'appliquer.

## Preuve

Un rapport final doit inclure :

- commandes lancées ;
- sorties ou preuves résumées ;
- tests ignorés et pourquoi ;
- écarts connus ;
- vérifications manuelles nécessaires, le cas échéant.

Ne pas écrire "tester manuellement" sans étapes exactes, résultats attendus et critères OK/KO.

## L'échec est une donnée

Un test échoué n'est pas une raison de cacher le statut. C'est un artefact qui doit mettre à jour le plan, le registre de risques ou la mission worker.
