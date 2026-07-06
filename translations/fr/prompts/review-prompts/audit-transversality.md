# Auditer la transversalité

## But

Vérifier si les capacités forment un maillage cohérent sans couplage dangereux.

## Quand l'utiliser

Après une cartographie des capacités ou avant l'implémentation d'architecture.

## Sortie attendue

Findings sur silos, couplage, événements, artefacts, triggers, suggestions et contexte partagé.

## Prompt

```text
Audite cette carte produit ou architecture pour sa transversalité.

Matériel :
<coller carte des domaines, carte des capacités ou notes d'architecture>

Vérifie :
1. Chaque capacité déclare-t-elle entrées et sorties ?
2. Les artefacts sont-ils explicites ?
3. Les événements sont-ils explicites ?
4. Les coûts et risques sont-ils attachés ?
5. Les suggestions sont-elles filtrées ?
6. Les triggers autorisés et interdits sont-ils définis ?
7. Le contexte partagé est-il chargé à la demande ?
8. Y a-t-il du couplage direct entre domaines non liés ?
9. Le Control Plane peut-il observer le maillage ?

Contraintes :
- Tout doit être connectable.
- Rien ne doit dépendre directement de tout.
- Évite l'abstraction sans usage opérationnel.

Limites de sécurité :
- Les suggestions ne doivent pas déclencher automatiquement des actions rouges.

Étape suivante :
Retourne une recommandation corrigée de maillage de capacités.
```
