# Workflow GitHub sûr

Utiliser ce runbook avant de publier cette méthode ou tout dépôt projet sur GitHub.

## Préconditions

- L'historique Git est compris.
- L'arbre de travail est propre ou volontairement staged.
- Le dépôt possède un `.gitignore`.
- Le scan de secrets évident est passé.
- Le README est public-safe.
- La licence est présente.
- Aucun fichier source privé n'a été copié accidentellement.

## Checks locaux

Lancer :

```text
git status --short --branch
git log --oneline --decorate -n 10
git remote -v
```

Scanner chaînes et fichiers sensibles avant publication.

## GitHub CLI

Si `gh` est installé et authentifié :

```text
gh auth status
gh repo create autonomous-product-engineering-method --public --description "An open method for turning ordinary-language product visions into safe, premium, autonomous AI-assisted software engineering workflows." --source . --remote origin --push
```

Ne collez pas de tokens dans le chat. Si l'authentification manque, lancer `gh auth login` localement.

## Actions rouges

Créer un dépôt public et y pousser est une action rouge. C'est autorisé seulement quand le dépôt a été scanné et que l'utilisateur a explicitement demandé la publication publique.

## Après le push

Vérifier :

- URL du dépôt ;
- rendu README ;
- fichiers présents ;
- absence de données privées ;
- branche par défaut.
