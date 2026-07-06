# Auto-audit de la méthode

Cet audit challenge la fondation publique v0.1 de la Méthode d'ingénierie produit autonome.

## Où cette méthode peut-elle échouer ?

- Elle peut devenir trop abstraite si les artefacts sont créés sans valeur d'exécution.
- Elle peut ralentir les petits travaux si chaque tâche est traitée comme stratégique.
- Elle peut produire des documents soignés mais non testés sur de vrais projets.
- Elle peut trop dépendre de l'auto-reporting des agents si les gates ne sont pas appliqués extérieurement.

## Où peut-elle sur-promettre ?

- "Autonome" peut laisser croire que le système opère en sécurité sans supervision.
- "Premium" peut sembler subjectif si les preuves ne sont pas définies.
- "Méthode d'ingénierie produit" peut suggérer une complétude au-delà de la v0.1.

Mitigation : la documentation répète que c'est une fondation initiale, pas une garantie ou certification.

## Où les agents peuvent-ils mal interpréter les utilisateurs ?

- L'ambition peut être sous-lue, produisant un jouet.
- L'ambition peut être sur-lue, produisant une plateforme inutile.
- Un feedback émotionnel comme "c'est moche" peut être routé vers du styling de surface au lieu de la clarté de parcours.

Mitigation : profilage déductif, cartes d'ambiguïté et routage du feedback.

## Où les coûts peuvent-ils exploser ?

- Boucles longues de workers.
- Chargement large de contexte.
- Modèles forts utilisés pour tâches déterministes.
- Revues répétées sans nouvelle preuve.
- Appels API externes cachés.

Mitigation : Cost Gate, politique de budget, routage modèle, exécution consciente des quotas.

## Où la sécurité peut-elle échouer ?

- Des actions rouges peuvent être cachées dans une mission trop large.
- Des secrets peuvent être inclus accidentellement dans le contexte.
- Le reporting public peut exposer des détails opérationnels privés.
- Les agents peuvent traiter la publication GitHub comme routinière.

Mitigation : modèle d'actions rouges, exclusions de secrets, workflow GitHub sûr, scan public-safe.

## Où l'UX peut-elle devenir faussement premium ?

- Une UI raffinée peut cacher l'absence de parcours.
- Des réglages avancés peuvent submerger le premier écran.
- Des badges de statut peuvent tromper les utilisateurs.
- La vérité du Control Plane peut être omise pour raisons esthétiques.

Mitigation : Dual UI Gate, Truth Gate, Journey Gate.

## Où la documentation peut-elle devenir trop abstraite ?

- Les diagrammes de couches peuvent remplacer les décisions.
- Les cartes de capacités peuvent devenir décoratives.
- Les templates peuvent être remplis mécaniquement.

Mitigation : chaque artefact doit soutenir une décision, étape de build, revue ou handoff.

## Où les prompts peuvent-ils devenir dangereux ?

- Les prompts peuvent donner trop d'autonomie.
- Les prompts peuvent omettre les limites d'approbation.
- Les utilisateurs peuvent coller des secrets dans le chat.
- Les prompts spécifiques à un outil peuvent supposer des capacités que l'outil n'a pas.

Mitigation : chaque prompt inclut contraintes, limites de sécurité et prochaine étape.

## Ce qui n'est volontairement pas résolu

- Product-market fit.
- Conformité juridique.
- Certification sécurité complète.
- Implémentation d'un runtime production.
- Authentification spécifique aux outils.
- Goût design métier-spécifique.
- Gouvernance enterprise.

## Verdict actuel

La méthode est assez cohérente pour un usage public v0.1 comme fondation documentaire et bibliothèque de prompts. Elle a encore besoin de tests terrain, d'exemples plus forts, de diagrammes visuels et de validation sur projets réels avant d'être présentée comme mature.
