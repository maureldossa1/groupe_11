
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Spécifiez le chemin vers votre fichier CSV
file_path = '/content/Housing.csv'

# Chargez le fichier CSV dans un DataFrame pandas
df = pd.read_csv(file_path)


# Afficher les premières lignes du DataFrame
print("Premières lignes:")
print(df.head())

#Histogramme
# Définir la figure
plt.figure(figsize=(10, 6))

# Tracer l'histogramme par catégories pour appliquer différentes couleurs
n, bins, patches = plt.hist(df['bedrooms'], bins=10, edgecolor='black')

# Appliquer les couleurs
colors = ['blue', 'green', 'red', 'purple', 'orange', 'cyan', 'magenta', 'yellow', 'grey', 'brown']
for patch, color in zip(patches, colors):
    patch.set_facecolor(color)

# Titre du graphique et étiquettes des axes
plt.title('Histogramme')
plt.xlabel('Valeurs')
plt.ylabel('Fréquence')

# Afficher le graphique
plt.show()

# Définir le style avec Seaborn
sns.set(style="darkgrid")

# Définir la figure
plt.figure(figsize=(10, 6))

# Tracer l'histogramme par catégories pour appliquer différentes couleurs
n, bins, patches = plt.hist(df['bedrooms'], bins=10, edgecolor='black')

# Appliquer les couleurs
colors = ['blue', 'green', 'red', 'purple', 'orange', 'cyan', 'magenta', 'yellow', 'grey', 'brown']
for patch, color in zip(patches, colors):
    patch.set_facecolor(color)

# Ajouter la courbe KDE avec Seaborn
sns.kdeplot(df['bedrooms'], color='black', linewidth=2)


# Titre du graphique et étiquettes des axes
plt.title('Histogramme avec courbe KDE')
plt.xlabel('Nombre de chambres à coucher')
plt.ylabel('Fréquence')

# Afficher le graphique
plt.show()

# Définir le style avec Seaborn
sns.set(style="darkgrid")

# Tracer l'histogramme avec courbe KDE intégrée
plt.figure(figsize=(10, 6))
sns.histplot(df['bedrooms'], bins=10, kde=True, edgecolor='black', palette='viridis')

# Titre du graphique et étiquettes des axes
plt.title('Histogramme avec courbe KDE')
plt.xlabel('Nombre de chambres à coucher')
plt.ylabel('Fréquence')

# Afficher le graphique
plt.show()

