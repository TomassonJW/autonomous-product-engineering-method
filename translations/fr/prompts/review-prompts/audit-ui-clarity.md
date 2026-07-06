# Auditer la clarté UI

## But

Vérifier si une interface est claire, respecte la double UI et est premium dans son comportement.

## Quand l'utiliser

Avant d'accepter un travail UX/UI ou d'appeler une tranche produit premium.

## Sortie attendue

Findings sur clarté, qualité du parcours, séparation double UI, vérité du statut et prochaines corrections.

## Prompt

```text
Audite cette UI ou ce plan UX pour sa clarté.

Matériel :
<coller description d'écran, notes de screenshot, design ou route>

Vérifie :
1. L'action principale est-elle évidente ?
2. Un débutant peut-il avancer sans jargon ?
3. Un expert peut-il accéder à un contrôle plus profond ?
4. Experience Plane et Control Plane sont-ils séparés ?
5. Les données mockées, inférées, réelles et inconnues sont-elles étiquetées ?
6. Les erreurs sont-elles compréhensibles ?
7. Les actions rouges sont-elles derrière approbation ?
8. Le parcours est-il testable de bout en bout ?
9. L'UI est-elle vraiment utile, ou seulement scaffoldée ?

Contraintes :
- Findings d'abord.
- Ne traite pas le polish visuel comme qualité produit.
- Recommande des corrections UX concrètes.

Limites de sécurité :
- Signale toute UI qui permet de publier, supprimer, dépenser, exposer ou envoyer sans approbation.

Étape suivante :
Retourne un plan minimal de correction et un résultat de gate UI.
```
