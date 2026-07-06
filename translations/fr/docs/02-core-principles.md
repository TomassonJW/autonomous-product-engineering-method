# Principes fondamentaux

## 1. Langage courant en entrée, produit structuré en sortie

L'utilisateur peut décrire son intention avec un langage approximatif, émotionnel, incomplet ou non technique. Le système doit la traduire en structure produit et ingénierie.

La traduction doit préserver l'incertitude. Si les mots de l'utilisateur peuvent désigner plusieurs produits, le système doit le dire.

## 2. Déduire avant de demander

Ne pas poser de questions d'intake génériques quand la réponse peut être inférée sans risque.

Poser une question seulement si sa réponse change la trajectoire produit, le profil de risque, l'architecture, le coût ou le niveau d'autonomie.

## 3. Challenger avant de construire

Un travail ambitieux ou ambigu doit passer un gate de challenge. Le challenge doit être spécifique, utile et rédigé en langage clair. Il ne doit pas devenir un mur bureaucratique.

## 4. Premium signifie confiance

Premium signifie clarté, fiabilité, configurabilité, maîtrise des coûts et limites honnêtes. Un polish décoratif ne compense pas un faux statut, des flows cassés ou un risque caché.

## 5. Séparer expérience et pilotage

Tout produit sérieux a besoin d'une Experience Plane UI et d'une Control Plane UI. Mélanger les workflows utilisateur avec logs, workers internes, queues et contrôles admin crée de la confusion et une fausse qualité.

## 6. Tout connectable, rien entremêlé

Les capacités doivent déclarer entrées, sorties, événements, artefacts, coûts, risques et relations. Elles ne doivent pas dépendre directement de tous les autres modules.

Utiliser contrats, événements, artefacts typés, registres et chargement de contexte plutôt que du couplage implicite.

## 7. Le coût est une contrainte produit

Coût en tokens, coût API, runtime, cacheabilité, coût de revue humaine et coût de maintenance font partie du produit. Un système premium dépense de la profondeur là où elle compte.

## 8. L'autonomie doit être observable

Le travail autonome doit laisser des traces : statuts, logs, artefacts, décisions, tests, échecs et rapports finaux. Aucun worker ne doit être cru seulement parce qu'il affirme avoir réussi.

## 9. Les zones de sécurité sont obligatoires

Les actions vertes peuvent être autonomes. Les actions orange exigent une proposition et une revue. Les actions rouges exigent une approbation humaine explicite.

## 10. Le feedback met à jour la bonne couche

Tous les commentaires ne réécrivent pas la North Star. Le feedback doit être reformulé, classé, relié aux couches affectées, transformé en tâches, testé et documenté seulement là où c'est nécessaire.
