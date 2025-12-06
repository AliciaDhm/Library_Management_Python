# 📚 Projet Python – Gestion d’une Librairie

## 🎯 Objectif

L’objectif est de **concevoir un programme Python** simulant la gestion d’une **librairie**.  
Le programme modélise les **livres**, les **utilisateurs**, et leurs **interactions** (emprunts, retours…).

---

## 🧩 Description Générale

Votre programme s’articule autour de **deux entités principales** :

- 📘 **Les livres**
- 👤 **Les utilisateurs**

Et leurs **interactions** : emprunter et rendre des livres.

---

## 1. 📘 Gestion des Livres

### Attributs d’un livre
- `id` : identifiant unique du livre  
- `titre` : titre du livre  
- `auteur` : auteur du livre  
- `status` : état du livre (`disponible` / `emprunté`)

### Fonctionnalités
- ➕ **Ajouter** un livre  
- 🗑️ **Supprimer** un livre *(uniquement s’il n’est pas emprunté)*  
- 🔁 **Modifier le statut** d’un livre (`disponible` ↔ `emprunté`)  
- 📜 **Lister** tous les livres disponibles  
- 🔍 **Rechercher** un livre par :
  - titre
  - auteur
  - mot-clé

---

## 2. 👤 Gestion des Utilisateurs

### Attributs d’un utilisateur
- `id` : identifiant unique de l’utilisateur  
- `nom` : nom de l’utilisateur  
- `livres_empruntés` : liste des identifiants de livres empruntés

### Fonctionnalités
- 🆕 **Créer** un utilisateur  
- 🗑️ **Supprimer** un utilisateur *(uniquement s’il n’a aucun livre emprunté)*  
- 📜 **Lister** tous les utilisateurs enregistrés

---

## 3. 🔄 Gestion des Emprunts et Retours

### Fonctionnalités
- 📥 **Emprunter** un livre *(si disponible)* :
  - Mettre à jour le statut du livre
  - Ajouter l’identifiant du livre à la liste de l’utilisateur
- 📤 **Rendre** un livre :
  - Remettre le statut du livre à `disponible`
  - Retirer l’identifiant du livre de la liste de l’utilisateur

---

## 4. 📊 Statistiques

La librairie doit pouvoir afficher des **statistiques globales** :

- 📚 Nombre total de livres
- 👥 Nombre total d’utilisateurs
- 📈 Distribution du nombre de livres empruntés par utilisateur

---

## 🧪 Remarques générales
- Vous pouvez demander à GPT ou faire un script pour générer des données "fake" pour vos tests.

### Critères d’évaluation
- ✅ **Maintenabilité** : code propre, testé, bien structuré.  
- ⚡ **Efficacité** : éviter les doublons, opérations inutiles ou coûteuses.  
- 🧭 **Principe de moindre surprise** : comportement intuitif et cohérent pour chaque fonctionnalité.
