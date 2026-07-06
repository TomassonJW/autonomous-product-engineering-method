# Maillage de contexte et de capacités

Les produits agentiques deviennent fragiles quand chaque module stocke sa propre vérité ou quand chaque worker charge tout en contexte.

La méthode utilise un modèle de maillage : les capacités sont connectées par des contrats explicites, du contexte partagé, des événements, des artefacts et des registres.

## Concepts centraux du maillage

- **Capacité** : fonction produit réutilisable avec entrées, sorties, artefacts, coûts, risques et permissions déclarés.
- **Couche de contexte** : information active nécessaire à un run.
- **Couche de contexte partagé** : faits, préférences, décisions et références stables.
- **Couche de suggestions** : recommandations transversales filtrées par pertinence, risque et coût.
- **Registre des sources de vérité** : endroit où le système enregistre artefacts, décisions et statuts autoritaires.
- **Flux d'événements** : ce qui s'est passé, quand, et avec quel effet.

## Règle du maillage

Tout doit être connectable, mais rien ne doit dépendre directement de tout.

Utiliser :

- artefacts typés ;
- noms d'événements ;
- contrats explicites de capacités ;
- petits paquets de contexte ;
- références durables ;
- contrôles de permission.

Éviter :

- état global implicite ;
- blocs de contexte copiés-collés ;
- workers qui lisent tous les fichiers par défaut ;
- imports directs entre domaines non liés ;
- suggestions qui déclenchent des actions sans revue.

## Chargement de contexte

Le système doit savoir où chercher, pas tout porter en contexte actif.

Un bon paquet de contexte inclut :

- mission ;
- couche produit pertinente ;
- liens de source de vérité ;
- décisions récentes ;
- contraintes ;
- fichiers ou domaines affectés ;
- zone de sécurité ;
- politique de budget ;
- sortie attendue.

## Discipline des suggestions

Une suggestion est utile seulement si elle est :

- pertinente ;
- compréhensible ;
- sûre à proposer ;
- consciente du coût ;
- non redondante ;
- fondée sur des données connues ou clairement marquées comme incertaines.

Les suggestions ne doivent pas devenir une automatisation cachée.
