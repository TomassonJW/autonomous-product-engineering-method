# Préparer un plan de build Codex

## But

Préparer un plan d'implémentation spécifique à Codex pour un dépôt.

## Quand l'utiliser

Après profilage produit, challenge et clarification d'une tranche de build bornée.

## Sortie attendue

Plan d'inspection du dépôt, fichiers à lire, étapes d'implémentation, tests et contrat de rapport final.

## Prompt

```text
Prépare un plan de build Codex avec la Méthode d'ingénierie produit autonome.

Tâche :
<coller la tâche>

Contexte du dépôt :
<coller le contexte public et sûr du dépôt>

Règles :
- Lire d'abord les fichiers pertinents.
- Ne pas lire les secrets, .env, fichiers auth, logs privés, vaults ou credentials.
- Ne pas coder avant de comprendre les patterns locaux.
- Garder les changements bornés.
- Ajouter ou adapter les tests selon le risque.
- Lancer les checks disponibles.
- Relire le diff.

Produis :
1. Ce que Codex doit inspecter.
2. Ambiguïtés ou risques.
3. Petites étapes d'implémentation proposées.
4. Fichiers probablement affectés.
5. Tests ou checks à lancer.
6. Limites de sécurité.
7. Format de rapport final.

Limites de sécurité :
- Les actions rouges exigent une approbation explicite.
- Ne demande pas à l'utilisateur de coller des secrets.
- Ne force push pas.

Étape suivante :
Si le plan implique des changements d'architecture, propose d'abord une ADR. Sinon, poursuis l'implémentation bornée après approbation.
```
