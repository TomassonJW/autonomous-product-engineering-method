# Auditer la qualité de la méthode

## But

Vérifier si une méthode, un document ou un plan produit est utile, concret et honnête.

## Quand l'utiliser

Avant de publier une documentation de méthode ou de l'utiliser pour l'exécution d'un worker.

## Sortie attendue

Findings, sévérité, documents affectés et corrections concrètes.

## Prompt

```text
Audite cette méthode ou documentation pour sa qualité.

Matériel :
<coller ou référencer le matériel>

Vérifie :
1. Est-ce assez concret pour être utilisé ?
2. Est-ce que cela sur-promet ?
3. Les hypothèses sont-elles distinguées des faits ?
4. Les sorties sont-elles clairement définies ?
5. Y a-t-il des exemples quand c'est nécessaire ?
6. Le texte évite-t-il le langage startup vague ?
7. Les gates de sécurité, coût et test sont-ils préservés ?
8. Un autre agent peut-il reprendre à partir de cela ?

Donne d'abord les findings, classés par sévérité. Inclus des références de fichier ou section quand elles existent.

Contraintes :
- Ne résume pas avant les findings.
- Ne fais pas de compliment vague.
- Recommande des corrections spécifiques.

Limites de sécurité :
- Signale toute instruction qui pourrait exposer des secrets ou autoriser des actions rouges.

Étape suivante :
Retourne une liste de corrections groupées en must-fix et should-fix.
```
