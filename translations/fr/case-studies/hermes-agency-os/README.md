# Cas d'étude Hermes Agency OS

Ce cas d'étude est sanitizé et public-safe. Il ne contient pas de credentials privés, chemins privés, contenu client non publié, données personnelles, logs bruts ou détails opérationnels sensibles.

## Contexte

Hermes Agency OS est utilisé ici comme exemple de workflow agentique où des workers autonomes soutiennent des tâches produit, éditoriales ou opérationnelles répétables.

La leçon importante n'est pas l'outil précis. La leçon importante est la façon dont un workflow devient assez fiable pour être opéré.

## Du workflow au golden path

Un workflow précoce peut commencer comme une suite de prompts et checks manuels. Il devient un golden path quand :

- les entrées sont explicites ;
- les artefacts attendus sont connus ;
- le statut est vrai ;
- les modes d'échec sont nommés ;
- le worker a des checkpoints ;
- les rapports sont cohérents ;
- les points d'approbation humaine sont clairs.

## La fiabilité est devenue nécessaire

L'autonomie a exposé des problèmes faciles à manquer dans des runs manuels :

- la complétion partielle ressemblait à un succès ;
- les checks ignorés n'étaient pas toujours visibles ;
- les limites de quota pouvaient interrompre le travail silencieusement ;
- des scaffolds UI pouvaient ressembler à du progrès produit ;
- les logs existaient mais ne répondaient pas aux questions produit.

## Leçon réutilisable

Un workflow autonome durable a besoin de wrappers, checkpoints, statut observable, politique de quota et rapports finaux qui peuvent être challengés.

Cela dépasse Hermes : sessions Codex, agents CLI, chatbots outillés et automations planifiées ont besoin du même pattern de gouvernance.
