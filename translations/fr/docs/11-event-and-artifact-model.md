# Modèle événements et artefacts

Les événements et artefacts permettent au système de rester cohérent sans couplage direct entre tous les modules.

## Artefact

Un artefact est une sortie durable qui peut être revue, réutilisée, versionnée ou référencée.

Exemples :

- brief produit ;
- rapport de challenge ;
- modèle UX ;
- spec de capacité ;
- charte de mission worker ;
- rapport de test ;
- résumé de run ;
- décision ;
- patch de code généré ;
- rapport de coût.

Les artefacts doivent inclure :

- titre ;
- but ;
- source ;
- version ou date ;
- auteur ou worker ;
- statut ;
- confiance ;
- dépendances ;
- limites connues.

## Événement

Un événement enregistre quelque chose qui s'est produit.

Exemples :

- `product.intent.received`
- `product.profile.created`
- `challenge.gate.failed`
- `capability.spec.accepted`
- `worker.mission.started`
- `worker.checkpoint.created`
- `quality_gate.failed`
- `feedback.submitted`
- `public_release.requested`

Les événements doivent inclure :

- nom ;
- timestamp ;
- acteur ;
- artefact lié ;
- domaine affecté ;
- zone de sécurité ;
- résultat ;
- prochaines actions autorisées.

## Vérité du statut

Le statut ne doit pas compresser des états incompatibles.

Mauvais :

> Done

Meilleur :

> Brouillon généré. Tests non lancés. Publication externe non approuvée.

## Discipline événementielle

Les événements doivent informer les capacités en aval, pas les exécuter secrètement. Une couche de suggestions peut proposer les actions suivantes à partir des événements, mais les actions rouges exigent toujours une approbation explicite.
