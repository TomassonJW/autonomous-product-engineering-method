# Intégration du feedback

Les utilisateurs peuvent donner du feedback en langage courant. Le système doit le traduire vers la bonne couche sans transformer chaque commentaire en réécriture complète de la vision.

## Flux de feedback

1. Reformuler le feedback.
2. Classer le niveau d'impact.
3. Identifier les couches affectées.
4. Dire ce qui doit changer.
5. Dire ce qui ne doit pas changer.
6. Proposer des tâches.
7. Proposer des tests.
8. Mettre à jour la documentation si nécessaire.
9. Exécuter seulement quand le scope est clair.

## Niveaux d'impact

- **Copy ou polish visuel** : petits changements UI ou wording.
- **Clarté de parcours** : affecte workflow, navigation ou hiérarchie d'information.
- **Comportement de capacité** : change ce que le produit peut faire.
- **Architecture** : change la structure système ou les contrats partagés.
- **Vision** : change direction produit, utilisateurs ou niveau d'ambition.
- **Sécurité** : change permissions, effets externes ou classe de risque.

## Exemple

Feedback :

> "C'est trop technique."

Couches possiblement affectées :

- copy de l'Experience Plane ;
- navigation ;
- réglages par défaut ;
- révélation progressive des options avancées ;
- onboarding ;
- exemples.

Souvent non affectés :

- architecture centrale ;
- graphe de capacités ;
- runtime worker.

## Contrat de feedback

Une bonne réponse au feedback dit :

- "Je comprends cela comme..."
- "Cela affecte..."
- "Cela ne nécessite pas de changer..."
- "La plus petite mise à jour utile est..."
- "Le test doit prouver..."

## Éviter la sur-réaction

Ne pas reconstruire la vision produit pour chaque commentaire.

Ne pas implémenter un feedback vague à l'aveugle.

Ne pas cacher l'incertitude derrière un langage design confiant.
