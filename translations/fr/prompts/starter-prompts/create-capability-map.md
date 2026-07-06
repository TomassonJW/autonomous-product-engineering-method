# Créer une carte de capacités

## But

Mapper les capacités produit comme unités connectées, bornées et réutilisables.

## Quand l'utiliser

Après profilage produit et avant architecture ou planification worker.

## Sortie attendue

Liste de capacités avec entrées, sorties, artefacts, événements, coût, risque, exposition UI et triggers.

## Prompt

```text
Crée une carte de capacités pour ce produit.

Contexte :
<coller brief produit, vision ou carte des domaines>

Pour chaque capacité, définis :
1. Nom.
2. But.
3. Utilisateurs.
4. Entrées.
5. Sorties.
6. Artefacts.
7. Événements émis.
8. Événements consommés.
9. Profil de coût.
10. Profil de risque.
11. Ce qu'elle peut déclencher.
12. Ce qu'elle ne doit pas déclencher.
13. Exposition Experience Plane.
14. Exposition Control Plane.
15. Gates qualité.

Contraintes :
- Tout doit être connectable.
- Rien ne doit dépendre directement de tout.
- Ne crée pas de silos fonctionnels isolés.
- N'invente pas de systèmes externes sans justification.

Limites de sécurité :
- Marque les triggers rouges comme approbation requise.
- Ne laisse pas les suggestions devenir une automatisation cachée.

Étape suivante :
Identifie la première capacité à spécifier en détail.
```
