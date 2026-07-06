# Pattern de probe d'autonomie

Une probe d'autonomie est un petit run contrôlé qui teste si un worker peut opérer en sécurité avant de lui donner une responsabilité plus large.

## Design de la probe

Définir :

- mission ;
- fichiers ou systèmes autorisés ;
- cycles maximum ;
- artefact attendu ;
- gates qualité ;
- conditions d'arrêt ;
- format de rapport.

## Ce que la probe mesure

- Le worker comprend-il le scope ?
- Évite-t-il les fichiers interdits ?
- Produit-il des artefacts utiles ?
- Rapporte-t-il les checks ignorés ?
- S'arrête-t-il quand il est bloqué ?
- Évite-t-il les faux succès ?

## Résultat de probe

Classer :

- prêt pour run plus large ;
- prêt avec scope plus étroit ;
- nécessite amélioration du wrapper ;
- dangereux pour autonomie.

## Pourquoi c'est important

Une probe coûte moins cher que découvrir pendant un long run que le worker ne respecte pas scope, coûts ou vérité du statut.
