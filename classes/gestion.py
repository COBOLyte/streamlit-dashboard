import pandas as pd
import numpy as np

class GestionLP :
  def __init__(self, df) :
    self.df = pd.read_csv(df, sep = ";")

    self.df.rename(columns = str.capitalize, inplace = True)

    self.df.drop(
      columns = [
        "Diplome",
        "Numero_de_l_etablissement",
        "Code_de_l_academie",
        "Code_du_domaine",
        "Code_de_la_discipline",
        "Remarque",
        "Nombre_de_reponses",
        "Taux_de_reponse",
        "Poids_de_la_discipline",
        "Cle_etab",
        "Cle_disc",
        "Id_paysage"
      ],
      axis = 1,
      inplace = True
    )

    self.df.dropna(
      subset = [
        "Etablissement",
        "Academie",
        "Salaire_net_mensuel_median_regional",
        "Pourcent_emplois_cadre",
        "Pourcent_femmes"
      ],
      inplace = True
    )

    self.df.replace(["ns", "nd", "."], np.nan, inplace = True)

    self.df = self.df.convert_dtypes()
    self.df["Annee"] = pd.to_datetime(self.df["Annee"], format = "%Y")
    self.df.iloc[:, 7:len(self.df)] = self.df.iloc[:, 7:len(self.df)].astype("Float64")

    self.df.dropna(
      subset = ["Salaire_net_mensuel_median_regional"],
      inplace = True
    )

    self.df.reset_index(drop = True, inplace = True)

  def getDf(self) :
    return self.df
