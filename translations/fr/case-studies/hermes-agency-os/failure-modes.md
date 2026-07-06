# Modes d'échec

## Faux succès

Le worker rapporte la complétion mais l'artefact est incomplet, non testé ou non connecté à un vrai parcours.

Mitigation :

- exiger des preuves ;
- vérifier les gates ;
- garder l'autorité finale hors du worker.

## Épuisement silencieux du quota

Le worker s'arrête à cause du quota mais le statut ne le dit pas clairement.

Mitigation :

- statut de quota explicite ;
- rapports de pause ;
- instructions de reprise.

## Log sans décision

Les logs bruts existent, mais personne ne sait ce qui a changé ni quoi faire ensuite.

Mitigation :

- résumés de checkpoint structurés ;
- rapports de run ;
- sections décisions et blocages.

## Fuite de contexte privé

Les rapports incluent chemins privés, contenu brut ou détails opérationnels sensibles.

Mitigation :

- sanitiser les rapports ;
- utiliser des placeholders ;
- séparer logs privés et artefacts publics.

## Illusion de progrès UI

L'UI existe, mais aucun workflow de bout en bout ne fonctionne.

Mitigation :

- Journey Gate ;
- tests d'acceptation ;
- exemples côté utilisateur.
