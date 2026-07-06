# Auditer coûts et ressources

## But

Vérifier coûts, quotas, routage modèle, runtime et risques de boucle répétée.

## Quand l'utiliser

Avant des runs autonomes, appels modèles coûteux, workflows production ou démos publiques.

## Sortie attendue

Risques de coût, politique de budget, recommandations de routage modèle, opportunités de cache et conditions d'arrêt.

## Prompt

```text
Audite ce plan, cette capacité ou cette mission worker pour les risques de coût et ressources.

Matériel :
<coller plan ou mission>

Vérifie :
1. Coût token.
2. Coût modèle.
3. Coût API.
4. Runtime.
5. Risque de boucle répétée.
6. Potentiel de cache.
7. Alternatives locales déterministes.
8. Coût de revue humaine.
9. Coût de maintenance.
10. Ratio valeur/coût.

Contraintes :
- Premium ne signifie pas maximal.
- Recommande des chemins fiables moins chers quand c'est pertinent.
- Ne cache pas l'incertitude dans les estimations de coût.

Limites de sécurité :
- Les actions externes coûteuses ou répétées exigent une politique de budget explicite.
- Les actions financières rouges exigent une approbation humaine explicite.

Étape suivante :
Retourne une politique de budget et tout gate de coût requis.
```
