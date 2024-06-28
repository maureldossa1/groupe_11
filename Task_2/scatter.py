import pandas as pd
import matplotlib.pyplot as plt

# Spécifiez le chemin vers votre fichier CSV
file_path = '/content/Housing.csv'

# Chargez le fichier CSV dans un DataFrame pandas
df = pd.read_csv(file_path)


# Afficher les premières lignes du DataFrame
print("Premières lignes:")
print(df.head())

# Création du graphique de dispersion
plt.scatter(df['area'], df['price'])
plt.xlabel('Area')
plt.ylabel('Price')
plt.title('Scatter plot of Area vs Price')
plt.show()

"""Le graphique de dispersion (scatter plot)  montre la relation entre les variables 'area' (superficie) et 'price' (prix). Voici une interprétation de ce graphique :

Observations Générales
Tendance Générale :

Il semble y avoir une tendance générale à la hausse entre la superficie (area) et le prix (price). En d'autres termes, à mesure que la superficie augmente, le prix tend également à augmenter. Cela est attendu puisque des propriétés plus grandes ont tendance à coûter plus cher.
Dispersion des Données :

Les points sont assez dispersés, indiquant une variabilité significative dans les prix pour une superficie donnée. Cela suggère que d'autres facteurs en plus de la superficie influencent le prix.
Concentration des Données :

Il y a une concentration de points dans les zones de superficie entre 2000 et 8000 et de prix entre 2e6 et 8e6. Cela peut indiquer que la plupart des propriétés dans cet échantillon se situent dans cette gamme de tailles et de prix.
Outliers :

Quelques points sont éloignés des autres, indiquant des outliers. Par exemple, il y a des propriétés avec des prix très élevés même pour des superficies similaires à d'autres propriétés moins chères.
Interprétation Spécifique
Clusters de Données : Il y a plusieurs clusters ou groupes visibles dans le graphique, ce qui pourrait indiquer des segments de marché différents ou des caractéristiques spécifiques des propriétés qui les rendent plus ou moins chères à taille égale.

Non-linéarité : La relation entre la superficie et le prix n'est pas strictement linéaire. Il y a des cas où des petites augmentations de la superficie conduisent à des augmentations significatives du prix, et d'autres où de grandes superficies n'entraînent qu'une augmentation modérée du prix.


En résumé, ce scatter plot montre une corrélation positive générale entre la superficie et le prix, mais aussi une grande variabilité qui suggère que d'autres facteurs influencent le prix des propriétés.
"""