# Charger les bibliothèques nécessaires
library(readr)
library(ggplot2)

# Spécifier le chemin vers votre fichier CSV
file_path <- "/content/Housing.csv"

# Charger le fichier CSV dans un DataFrame R (data.frame)
df <- read_csv(file_path)

# Afficher les premières lignes du DataFrame pour vérifier le chargement
print("Premières lignes:")
print(head(df))

# Définir le thème de ggplot2 avec fond de grille foncé
theme_set(theme_dark())

# Créer le graphique d'histogramme avec courbe KDE
ggplot(df, aes(x = bedrooms, fill = factor(bedrooms))) +
  geom_histogram(binwidth = 1, color = "black", alpha = 0.7) +
  geom_density(color = "black", size = 1.5) +
  scale_fill_brewer(palette = "Set1") +  # Choisir une palette de couleurs
  labs(title = "Histogramme avec courbe KDE",
       x = "Nombre de chambres à coucher",
       y = "Fréquence") +
  theme(plot.title = element_text(size = 16, face = "bold"),
        axis.text = element_text(size = 12),
        axis.title = element_text(size = 14, face = "bold"),
        legend.position = "none")

# Afficher le graphique

"""Ce graphique présente la répartition du nombre de chambres à coucher dans les maisons. L'axe des x représente le nombre de chambres, et l'axe des y représente la fréquence des maisons ayant ce nombre de chambres. Le graphique inclut également une courbe KDE (estimation de la densité par noyau), qui est une représentation lisse de la distribution des données.

Principales observations

Le nombre de chambres le plus courant dans les maisons est de 3.
On trouve un nombre relativement important de maisons avec 2 et 4 chambres.
Les maisons avec 1, 5 ou 6 chambres sont moins nombreuses.
Les maisons avec 7 chambres ou plus sont très rares.
Remarques supplémentaires

Le graphique est basé sur un échantillon de maisons. Il est possible que la répartition du nombre de chambres dans la population totale des maisons soit différente.
Le graphique ne montre pas le nombre total de maisons dans l'échantillon.
Le graphique ne montre pas le prix ou d'autres caractéristiques des maisons.
Dans l'ensemble, le graphique montre que le nombre de chambres le plus courant dans les maisons est de 3. On trouve également un nombre relativement important de maisons avec 2 et 4 chambres.
:

"""

