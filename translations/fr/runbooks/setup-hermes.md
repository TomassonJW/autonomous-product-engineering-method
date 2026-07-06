# Setup Hermes

Utiliser ce runbook pour un environnement de worker autonome de style Hermes.

Hermes est traité ici comme un pattern de worker agentique durable, pas comme une exigence de la méthode.

## Pièces runtime requises

- charte de mission ;
- queue ou liste de travail ;
- wrapper ou superviseur ;
- fichier de statut ;
- logs ;
- checkpoints ;
- politique de quota ;
- fichier ou signal d'arrêt ;
- canal de rapport final ;
- chemin d'approbation humaine.

## Golden path

1. L'humain ou le superviseur crée une charte de mission.
2. Le worker charge seulement le contexte pertinent.
3. Le worker exécute un cycle borné.
4. Le worker écrit checkpoint et statut.
5. Le superviseur vérifie quota, gates et conditions d'arrêt.
6. Le worker continue, pause ou s'arrête.
7. Le rapport final est vérifié avant d'accepter la complétion.

## Détection de faux succès

Traiter comme échecs :

- message final sans artefacts ;
- "tests passés" sans preuve ;
- statut terminé après gates ignorés ;
- épuisement silencieux du quota ;
- erreurs cachées dans les logs ;
- rapports qui omettent les éléments bloqués.

## Reporting

Les rapports doivent inclure :

- mission ;
- cycles lancés ;
- sorties créées ;
- checks lancés ;
- échecs ;
- notes de coût ou quota ;
- approbations nécessaires ;
- prochaine action.

## Sécurité

Les workers Hermes ne doivent pas exécuter d'actions rouges sans approbation. Les rapports publics doivent être sanitizés et ne doivent contenir ni credentials, ni chemins privés, ni logs privés, ni contenu business sensible.
