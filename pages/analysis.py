import streamlit as st

st.title("Analyse des données")

st.write(
  "" \
  "L'étude statistique porte sur plusieurs informations connues sur les licences professionnelles entre 2013 et 2020. Le tableau de bord résume une partie de ces informations sous la forme de KPI et de graphiques permettant de valoriser les liens qui nous intéressent entre ces informations. Nous cherchons à répondre à la problématique suivante : **quelle est la place des licences professionnelles sur le marché de l'éducation en matière d'employabilité ?**" \
  ""
)

st.write(
  "" \
  "Le taux d'emploi moyen est de 90.9 %, mais ce résultat ne correspond qu'à l'année 2020, du fait que nous ne possédons pas de chiffres pour les autres années. Le pourcentage d'emplois stables augmente continuellement, tandis que le taux de chômage diminue, dans le même temps. Ces 2 variables étant corrélées, on peut en déduire que plus l'une varie, plus l'autre variera dans le sens inverse. Puis, l'évolution des 2 variables étant continue dans le temps, on peut espérer que la progression reste ainsi, post-2020. Donc, ces résultats tendent à démontrer l'influence des licences professionnelles dans la hausse du nombre d'emplois et la baisse du chômage."
  ""
)

st.write(
  "" \
  "Le taux d'insertion moyen est de 93.2 %. La meilleure année, au vu des chiffres, est 2020 avec 94.4 %, et la moins bonne année est 2013 avec 91.6 %. Ce sont des taux qui restent stables et très élevés, chaque année, avec des valeurs supérieures à 90 %. Il en va de même, lorsque nous comparons les taux entre les établissements. Certains affichent des chiffres un peu en dessous de la moyenne, à savoir Avignon (85.5 %), Corse Pasquale Paoli (87 %) et Évry Val d'Essonne (85.2 %). L'académie d'appartenance ne semble pas expliquer ces résultats, car les autres établissements de la même académie n'ont pas des taux similaires. Ces chiffres pourraient hypothétiquement s'expliquer par l'offre en emplois dans la zone géographique et la qualité des formations, en termes de préparation et d'adaptabilité au marché de l'emploi."
  ""
)

st.write(
  "" \
  "Le salaire brut annuel moyen est de 25 841.1 €, et de 27 858 € en 2020. Les domaines d'étude les plus rémunérateurs sont l'informatique, les sciences de l'ingénieur et les sciences, technologies et santé, avec des salaires bruts annuels respectifs de 27 323 €, 27 021 € et 26 486 €. Ce sont donc surtout les domaines exigeant un certain niveau de technicité et des études longues qui voient leurs salaires, rehaussés. En 2020, ce sont le droit (30 100 €), l'informatique (25 971 €) et les sciences fondamentales (29 533 €) qui sont les domaines les plus rémunérés. Les moins rémunérateurs, en moyenne, correspondent à l'information-communication (23 462 €), aux sciences humaines et sociales (23 672 €), et aux sciences de la vie et de la terre (24 189 €), soit des études préparant à des métiers requérant plus de connaissances fondamentales que techniques."
  ""
)

st.write(
  "" \
  "Au terme de notre analyse, des réponses ont été apportées pour mieux comprendre la place des licences professionnelles sur le marché de l'éducation, d'un point de vue de l'employabilité. Afin d'améliorer la précision de l'étude et de mesurer la pertinence de ce type de formation par rapport à d'autres (BTS, BUT, masters, etc.), nous pensons qu'utiliser des données plus récentes et intégrer d'autres types de formation au jeu de données, le permettrait."
  ""
)
