# Modéliser la double UI

## But

Créer un modèle clair d'Experience Plane et de Control Plane pour un produit.

## Quand l'utiliser

Avant de concevoir des écrans ou de revoir des interfaces confuses.

## Sortie attendue

Séparation double UI, flux utilisateurs, flux opérateurs, complexité cachée, vérité exposée et tests de gates.

## Prompt

```text
Modélise la double UI pour ce produit ou cette fonctionnalité.

Contexte :
<coller brief produit, capacité ou description de fonctionnalité>

Produis :
1. Types d'utilisateurs Experience Plane.
2. Action principale Experience Plane.
3. Parcours débutant.
4. Parcours avancé.
5. Complexité cachée par défaut.
6. Types d'utilisateurs Control Plane.
7. Vérité opérationnelle exposée dans le Control Plane.
8. Logs, coûts, gates, échecs, décisions et états de rollback nécessaires.
9. Risques d'UI hybride interdite.
10. Test du Dual UI Gate.

Contraintes :
- Ne mélange pas concepts admin/dev et workflows utilisateur finaux.
- Ne cache pas la vérité aux opérateurs.
- Utilise le langage courant pour le copy utilisateur.
- Garde les réglages avancés derrière une révélation progressive.

Limites de sécurité :
- Les actions rouges exigent une UI d'approbation explicite.
- Les données simulées ou inférées doivent être étiquetées.

Étape suivante :
Définis le premier parcours UI à tester de bout en bout.
```
