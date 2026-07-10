# Anti-patterns

Cette liste compacte couvre les échecs récurrents de la méthode. Le [catalogue Vision-to-Product](../docs/20-autonomous-vision-to-product.md#24-catalogue-des-anti-patterns) ajoute symptôme, cause, risque, détection et correction pour le profiling, l'exploration, la fondation, le build parallèle, l'intégration, la sécurité et l'exploitation.

## Coder depuis l'intention brute

Commencer l'implémentation avant profilage, challenge et calibration du scope.

## Jouet au lieu de produit

Construire une petite démo alors que l'utilisateur attendait un produit ou une plateforme sérieuse.

## Plateforme au lieu de workflow

Construire une grande architecture alors que l'utilisateur avait besoin d'une action simple et utile.

## UI hybride

Mélanger workflows utilisateur finaux, contrôles admin, logs, statuts de workers et configuration technique dans une interface confuse.

## Faux premium

Ajouter du polish visuel alors que les parcours, la vérité du statut, les erreurs et la sécurité restent faibles.

## Coût invisible

Lancer des modèles coûteux, API externes ou boucles répétées sans politique de budget.

## Auto-certification worker

Accepter le message "done" d'un worker sans tests, artefacts ou preuves de gates.

## Inondation de contexte

Charger chaque fichier, décision et log en contexte actif au lieu d'utiliser des références ciblées de source de vérité.

## Spam de suggestions

Générer beaucoup de suggestions transversales redondantes, risquées, coûteuses ou incompréhensibles.

## Théâtre documentaire

Créer des artefacts qui ne guident aucune décision, étape de build, revue ou passation.

## Dérive de fondation

Laisser des missions locales modifier des contrats partagés sans Foundation Change Proposal versionnée.

## Fixture présentée comme réalité

Présenter une intégration mockée ou avec fixture comme preuve de validation des vrais composants, utilisateurs ou systèmes externes.

## Théâtre du pourcentage de complétude

Augmenter un pourcentage global selon les fichiers, tâches, cartes ou tests au lieu de dimensions produit revues indépendamment.
