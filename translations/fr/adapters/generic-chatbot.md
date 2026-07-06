# Adapter chatbot générique

Un chatbot n'a généralement pas d'accès direct au filesystem, de logs durables, de tests ou d'autorité d'exécution. Le traiter comme une interface de raisonnement et de rédaction d'artefacts, sauf s'il est connecté à des outils.

## Forces

- Interaction en langage courant.
- Profilage produit.
- Rapports de challenge.
- Rédaction de prompts.
- Rédaction documentaire.
- Revue et critique.

## Risques

- Pas de vérification directe.
- L'utilisateur peut coller des secrets.
- Confiance excessive.
- État durable difficile à préserver.
- Faibles preuves d'exécution.

## Adaptation de la méthode

Utiliser les chatbots pour :

- découverte produit ;
- profilage déductif ;
- gates de challenge ;
- modélisation double UI ;
- cartographie de capacités ;
- remplissage de templates ;
- prompts de revue.

Ne pas compter sur un chatbot seul pour :

- vérification de code ;
- changements production ;
- gestion de secrets ;
- publication ;
- opérations destructives.

## Contrat de sortie

Demander des artefacts structurés qui peuvent être transférés dans un dépôt ou environnement d'exécution.
