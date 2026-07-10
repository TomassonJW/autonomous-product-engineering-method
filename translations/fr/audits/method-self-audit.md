# Auto-audit de la méthode

Cet audit challenge la fondation publique v0.2 de la Méthode d'ingénierie produit autonome.

## Où cette méthode peut-elle échouer ?

- Elle peut devenir trop abstraite si les artefacts sont créés sans valeur d'exécution.
- Elle peut ralentir les petits travaux si chaque tâche est traitée comme stratégique.
- Elle peut produire des documents soignés mais non testés sur de vrais projets.
- Elle peut trop dépendre de l'auto-reporting des agents si les gates ne sont pas appliqués extérieurement.
- Son protocole de bout en bout peut devenir trop lourd si chaque projet crée tout le catalogue d'artefacts.
- Foundation Freeze peut être détournée en verrou architectural permanent.
- Une estimation de complétude peut créer une fausse précision même avec des dimensions séparées.

## Où peut-elle sur-promettre ?

- "Autonome" peut laisser croire que le système opère en sécurité sans supervision.
- "Premium" peut sembler subjectif si les preuves ne sont pas définies.
- "Méthode d'ingénierie produit" peut suggérer une complétude au-delà des preuves disponibles en v0.2.

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

## Où Vision-to-Product peut-il devenir du théâtre de processus ?

- Les équipes peuvent créer chaque artefact nommé sans owner ni décision distincte.
- L'exploration peut continuer après l'effondrement de la valeur marginale d'information.
- Foundation Freeze peut protéger des hypothèses obsolètes au lieu de la cohérence du build.
- Des missions parallèles peuvent sembler indépendantes tout en concurrençant les mêmes contrats.
- Un tableau de complétude détaillé peut masquer l'absence d'intégration réelle ou de preuves utilisateur.

Mitigation : adapter les artefacts aux owners et cycles de vie, appliquer le test de saturation, exiger des verticales de falsification avant le gel, isoler l'ownership et garder les états de preuve indépendants.

## Ce qui n'est volontairement pas résolu

- Product-market fit.
- Conformité juridique.
- Certification sécurité complète.
- Implémentation d'un runtime production.
- Authentification spécifique aux outils.
- Goût design métier-spécifique.
- Gouvernance enterprise.

## Verdict actuel

La méthode est assez cohérente pour un usage public v0.2 comme fondation documentaire et bibliothèque de prompts. L'extension Vision-to-Product améliore fortement la continuité opérationnelle, le vocabulaire des preuves, la gouvernance de fondation et la coordination des workers parallèles. Elle doit encore être testée sur des tailles de produits, domaines, équipes, juridictions et outils agentiques variés avant d'être présentée comme mature.
