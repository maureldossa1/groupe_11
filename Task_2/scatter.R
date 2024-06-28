
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


# Création du graphique de dispersion
ggplot(df, aes(x = area, y = price)) +
  geom_point() +
  labs(x = "Area", y = "Price", title = "Scatter plot of Area vs Price")

"""
Le deuxième graphique de dispersion (scatter plot) fourni montre également la relation entre les variables 'area' (superficie) en abscisse et 'price' (prix) en ordonnées. Voici une analyse détaillée de ce plot :

Observations Générales
Tendance Générale :

Comme dans le premier graphique, il semble y avoir une tendance générale où une augmentation de la superficie (area) est associée à une augmentation du prix (price). Cela indique une relation positive entre ces deux variables.
Dispersion des Données :

Les points sont assez dispersés, montrant une grande variabilité des prix pour des superficies similaires. Cela signifie qu'il y a d'autres facteurs en jeu qui influencent le prix en plus de la superficie.
Concentration des Données :

Une concentration notable de points se trouve dans les zones où la superficie est inférieure à 8000 et le prix est inférieur à 1e7. Cela pourrait indiquer que la majorité des propriétés de l'échantillon se situent dans cette gamme de taille et de prix.
Outliers :

Plusieurs outliers sont visibles dans le graphique, particulièrement pour des superficies comprises entre 8000 et 16000, et des prix dépassant 1e7. Ces points indiquent des propriétés dont les prix sont beaucoup plus élevés par rapport à leur superficie ou vice versa.
Interprétation Spécifique
Clusters de Données : Il y a des groupes de données plus denses vers le bas du graphique (superficie entre 2000 et 8000, prix entre 5e6 et 1e7) ce qui pourrait suggérer des segments de marché spécifiques ou des caractéristiques communes des propriétés dans ces gammes.

Non-linéarité : La relation entre la superficie et le prix ne semble pas strictement linéaire. Il y a des variations où certaines propriétés avec des superficies plus grandes n'entraînent pas nécessairement une augmentation proportionnelle du prix.

Analyse Potentielle
Pour une analyse plus approfondie de la relation entre la superficie et le prix, vous pourriez :

Ajouter une ligne de tendance : Utiliser une régression linéaire ou non-linéaire pour visualiser la tendance générale et mieux comprendre la relation entre la superficie et le prix.

Segmenter par d'autres variables : Par exemple, inclure des variables telles que la localisation, l'âge des propriétés, le nombre de chambres, etc., pour comprendre mieux les facteurs influençant les prix.

Étudier les outliers : Examiner les propriétés qui sont des outliers pour identifier pourquoi elles sont si différentes du reste. Cela pourrait inclure des facteurs comme des rénovations récentes, des emplacements particulièrement prisés, ou des caractéristiques uniques.

Conclusion
Ce scatter plot montre une relation positive entre la superficie et le prix des propriétés, mais aussi une grande variabilité qui suggère l'influence de nombreux autres facteurs. En ajoutant des lignes de tendance et en stratifiant par d'autres variables, vous pourriez obtenir une compréhension plus nuancée de la relation entre ces deux variables.





"""