# Auditer les risques de sécurité

## But

Trouver les risques d'autonomie dangereuse, publication, secrets, production, suppression et effets externes.

## Quand l'utiliser

Avant de lancer des workers, publier des dépôts ou activer des intégrations.

## Sortie attendue

Findings de risque avec sévérité, classe d'action, approbations requises et mitigations.

## Prompt

```text
Audite ce plan, prompt, dépôt ou mission worker pour les risques de sécurité.

Matériel :
<coller ou référencer le matériel>

Classe les actions :
- Verte : locale, réversible, testable, faible risque.
- Orange : structurante, coûteuse, ambiguë ou impactante.
- Rouge : irréversible, destructive, publique, financière, liée aux secrets, change la production ou envoie des messages externes.

Vérifie :
1. Exposition de secrets.
2. Risque de publication publique.
3. Effets externes.
4. Commandes destructives.
5. Changements production.
6. Gestion des credentials.
7. Approbations manquantes.
8. Rollback manquant.
9. Affirmations de faux succès.
10. Permissions de prompt dangereuses.

Contraintes :
- Findings d'abord.
- Sois spécifique.
- Ne suggère pas de contourner l'approbation.

Limites de sécurité :
- Ne demande jamais de secrets.
- Les actions rouges doivent être derrière approbation.

Étape suivante :
Retourne les mitigations requises avant exécution.
```
