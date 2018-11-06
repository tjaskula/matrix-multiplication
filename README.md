# matrix-multiplication
Spark matrix multiplication project

Alexia: Voici le mapper et reducer que j'ai fais pour le moment.
Voici des remarques et questions:
- Pour le mapper: j'ai utilisé range(nb de colonne de b +1) ceci est codé en dur dans mon code car je ne sais pas comment on va procéder pour récupérer cette information.
- Pour le fichier utilisé sur lequel j'ai fais mes tests il se présente de la manière suivante:
A,i,j,v => Nom de la matrice, indice de la ligne, indice de la colonne, valeur
...
B,i,j,v 
Je ne sais pas comment générer des matrices de manière aléatoire de telle sorte que ça soit sous ce format là. 
- J'ai la version python 3, et j'ai utilisé un sort +1 -2 entre le map et reduce 

