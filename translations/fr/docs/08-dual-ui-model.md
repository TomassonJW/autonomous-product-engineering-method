# Modèle de double UI

Tout produit sérieux doit distinguer deux plans d'interface.

Le modèle de double UI évite un échec fréquent : exposer les utilisateurs finaux à la machinerie interne tout en cachant la vérité opérationnelle aux personnes responsables du système.

## Experience Plane UI

L'Experience Plane est destinée aux utilisateurs finaux qui veulent utiliser les capacités du produit.

Elle doit être :

- simple ;
- centrée sur l'action ;
- écrite en langage courant ;
- focalisée sur les résultats ;
- claire sur ce que le système a compris ;
- capable de révéler progressivement la complexité ;
- débarrassée par défaut des logs internes, détails de workers, mécaniques de queue et jargon admin.

Exemple d'action principale :

> "Décrivez le produit que vous voulez construire."

Des contrôles avancés peuvent exister, mais ils ne doivent pas dominer le chemin par défaut.

## Control Plane UI

Le Control Plane est destiné aux développeurs, opérateurs, admins, QA, product owners et utilisateurs avancés.

Il doit exposer :

- runs ;
- workers ;
- queues ;
- logs ;
- traces ;
- gates qualité ;
- coûts ;
- échecs ;
- décisions ;
- permissions ;
- configuration ;
- état de rollback ;
- références de source de vérité.

Le Control Plane peut être technique, mais il doit rester clair et vrai.

## Hybride interdit

Ne pas mélanger :

- actions utilisateur finales ;
- logs bruts ;
- configuration admin ;
- internes de workers ;
- labels techniques ;
- débogage des coûts ;
- résultats utilisateur finaux ;
- statuts de pipeline non filtrés ;

dans un seul écran confus.

Si une UI force un utilisateur non technique à comprendre les opérations internes pour terminer sa tâche principale, le Dual UI Gate échoue.

## Règle de design

Premier écran simple. Contrôle profond derrière un chemin volontaire.

Le débutant ne doit pas être puni par la complexité. L'expert ne doit pas être piégé par la simplicité.
