# Glossaire français

Ce glossaire fixe les termes français recommandés pour la traduction officielle. L'anglais reste la source canonique. Certains termes restent en anglais quand ils correspondent à un nom de méthode, un intitulé d'artefact, une commande, un nom de fichier ou un terme déjà stable dans les outils.

## Règle générale

Utiliser le français quand cela améliore la compréhension. Garder l'anglais quand le terme est un nom propre, un identifiant, un intitulé de fichier, un nom d'outil, une commande, un événement, ou quand la traduction rendrait le concept moins stable.

| Terme anglais | Rendu français recommandé | Notes |
| --- | --- | --- |
| Autonomous Product Engineering Method | Méthode d'ingénierie produit autonome | Garder le nom anglais dans les titres de dépôt ou quand il désigne le projet public. Utiliser la traduction dans le corps du texte. |
| ordinary language | langage courant | Éviter "langage ordinaire" si le contexte parle d'expression utilisateur naturelle. |
| premium | premium | Garder "premium". Expliquer que le terme signifie clarté, fiabilité, profondeur maîtrisée, coût explicite et absence de mauvaise surprise. |
| product profiling | profilage produit | Peut aussi être "profilage du produit" selon la phrase. |
| deductive product profiling | profilage produit déductif | Terme central de la méthode. |
| challenge gate | gate de challenge | Garder "gate" pour cohérence avec les autres quality gates. "Point de challenge" peut être utilisé dans une explication non technique. |
| North Star | North Star | Garder l'anglais comme terme produit stable. Expliquer comme "cap durable du produit" si nécessaire. |
| product vision | vision produit | Terme courant. |
| product-to-engineering layers | couches produit-vers-ingénierie | Utiliser aussi "chaîne de transformation produit-ingénierie" dans un texte plus naturel. |
| Vision-to-Product | Vision-to-Product | Garder l'anglais pour le nom de la méthode de bout en bout. Expliquer comme transformation gouvernée de la vision au produit. |
| project profiling | profilage projet | Compréhension structurée du commanditaire, du public et de la situation. Ne désigne pas un profil psychologique clandestin. |
| project inference | inférence projet | Déduction révisable sur le produit ou son contexte, avec source, contre-preuve et conséquence. |
| inference registry | registre d'inférences | Garder `INFERENCE_REGISTRY.jsonl` inchangé comme nom d'artefact. |
| falsification vertical | verticale de falsification | Tranche fonctionnelle minimale conçue pour réfuter une hypothèse risquée à travers de vraies frontières. |
| Foundation Freeze | Foundation Freeze | Baseline versionnée et acceptée des contrats produit et techniques. Ce n'est pas un verrou permanent. |
| Foundation Change Proposal | Foundation Change Proposal | Garder l'intitulé anglais pour l'artefact gouvernant un changement de fondation. |
| Build Mission Portfolio | portefeuille de missions de build | Garder le nom de fichier `BUILD_MISSION_PORTFOLIO.md` inchangé. |
| ContextPack | ContextPack | Paquet compact de contexte limité à une mission, ses contrats, ses contraintes et ses preuves. |
| completeness estimate | estimation de complétude | Estimation pondérée par dimensions et preuves, jamais fondée sur le nombre de fichiers ou tâches. |
| acceptance owner | acceptance owner | Rôle humain ou indépendant responsable de la décision finale d'acceptation. |
| domain map | carte des domaines | Ne pas traduire les noms de fichiers. |
| capability map | carte des capacités | Terme stable. |
| capability | capacité | Dans ce dépôt, une capacité est une fonction produit réutilisable avec entrées, sorties, coûts, risques et permissions. |
| capability graph | graphe de capacités | Terme stable. |
| context and capability mesh | maillage de contexte et de capacités | Éviter "mesh" seul en français sauf référence technique. |
| event stream | flux d'événements | Garder les noms d'événements exacts en anglais. |
| artifact | artefact | Terme technique accepté. |
| source-of-truth registry | registre des sources de vérité | Ne pas réduire à "registre" seul. |
| dual UI model | modèle de double UI | Garder "UI". Peut être expliqué comme séparation entre interface d'expérience et interface de pilotage. |
| Control Plane UI | interface de pilotage | Garder "Control Plane UI" dans les titres si l'anglais est utile, puis expliquer en français. |
| Experience Plane UI | interface d'expérience | Éviter "interface utilisateur finale" si le contraste avec Control Plane doit rester explicite. |
| worker mission charter | charte de mission du worker | Garder "worker" dans les contextes agentiques. |
| autonomous worker runtime | runtime de worker autonome | Garder "runtime" quand il désigne l'environnement d'exécution. |
| quality gate | gate qualité | Garder "gate" dans les intitulés de gates. |
| truth gate | Truth Gate / gate de vérité | Garder "Truth Gate" dans les listes officielles ; expliquer en français. |
| cost gate | Cost Gate / gate de coût | Garder "Cost Gate" dans les listes officielles ; expliquer en français. |
| safety gate | Safety Gate / gate de sécurité | Ne pas adoucir en "prudence". |
| feedback integration | intégration du feedback | "Retours utilisateur" peut être utilisé pour expliquer. |
| runbook | runbook | Garder "runbook" ; expliquer comme guide opérationnel exécutable. |
| adapter | adapter | Garder "adapter" pour les fichiers et le concept outil-spécifique. |
| sandbox | sandbox | Garder le terme anglais, éventuellement "environnement isolé" en explication. |
| smoke test | smoke test | Garder le terme. Expliquer comme vérification rapide de bon fonctionnement. |
| rollback | rollback | Garder le terme. Expliquer comme retour arrière contrôlé. |
| green/orange/red action zones | zones d'action verte/orange/rouge | Garder la couleur et le niveau de risque explicites. |

## Termes à ne pas traduire

Ne pas traduire les noms exacts suivants quand ils sont utilisés comme références :

- `README.md`
- `TRANSLATION_STATUS.md`
- `AGENTS.md`
- `git status`
- `git commit`
- `worker.mission.completed`
- `quality_gate.failed`
- Codex
- Hermes
- GitHub
- CLI

## Style français attendu

Préférer :

- phrases directes ;
- vocabulaire concret ;
- risques nommés clairement ;
- consignes actionnables ;
- ton sobre.

Éviter :

- "solution innovante de bout en bout" ;
- "synergie" ;
- "expérience augmentée" ;
- "transformation digitale" ;
- euphémismes autour de la sécurité.
