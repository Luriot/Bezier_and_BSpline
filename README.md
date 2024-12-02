# Visualisation des Courbes de Bézier et B-Spline

Ce projet Python permet de générer et de visualiser des courbes de Bézier et B-spline à partir de points de contrôle. Les courbes sont tracées à l'aide de la bibliothèque `matplotlib` pour une représentation claire et dynamique.

## Fonctionnalités

- **Courbe de Bézier** :
  - Générée à l'aide de l'algorithme de De Casteljau.
  - Points de contrôle personnalisables pour créer des formes dynamiques.

- **Courbe B-Spline** :
  - Supporte des degrés variables (linéaire, quadratique, cubique, etc.).
  - Permet de personnaliser les points de contrôle et les vecteurs de nœuds.

- **Personnalisation Facile** :
  - Toutes les variables modifiables sont regroupées en haut du script pour plus de simplicité.
  - Ajustez les points de contrôle, le degré et la résolution directement.

## Prérequis

- Python 3.8 ou version ultérieure
- Bibliothèques nécessaires :
  - `numpy`
  - `matplotlib`
  - `scipy`

Installez les dépendances avec la commande suivante :
```bash
pip install numpy matplotlib scipy
