# Bibliothèque de prompts

Ces prompts sont conçus pour être copiés dans Codex, Hermes, des agents CLI, des chatbots ou des systèmes agentiques personnalisés.

Ce ne sont pas des commandes magiques. Ce sont des contrats d'opération. Adaptez les noms d'outils, chemins de dépôt et règles d'approbation à votre environnement.

## Règles des prompts

Chaque prompt de cette bibliothèque doit :

- définir son but ;
- dire quand l'utiliser ;
- préciser la sortie attendue ;
- inclure les contraintes ;
- inclure les limites de sécurité ;
- définir l'étape suivante.

## Groupes de prompts

- [Prompts système](system-prompts/autonomous-product-architect.md) : contrats de rôle et comportement durables.
- [Prompts de démarrage](starter-prompts/start-new-product-method.md) : prompts pour démarrer un produit ou préparer un run.
- [Prompts de revue](review-prompts/audit-method-quality.md) : prompts de critique, sécurité, coût, UX et transversalité.

Pour le protocole complet, utiliser [Vision-to-Product Orchestrator](system-prompts/vision-to-product-orchestrator.md). Il coordonne profiling, inférences, exploration, Foundation Freeze, missions de build, intégration, acceptation et apprentissage post-livraison.

## Rappel sécurité

Ne collez jamais de secrets dans un prompt. Utilisez des placeholders et des flux d'authentification sûrs. Toute action qui publie, supprime, dépense de l'argent, envoie des messages, modifie la production ou manipule des secrets est une action rouge et exige une approbation explicite.
