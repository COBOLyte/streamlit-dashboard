import streamlit as st
import altair as alt
from classes.gestion import GestionLP

df = GestionLP("./data/Projet_Sujet_defaut_LicencePRO.csv").getDf()

st.title("Tableau de bord")

with st.container() :
  st.subheader("Filtres")
  col_filter_salary, col_filter_year = st.columns(2, border = True)
  
  with col_filter_salary :
    salaries = df[df["Salaire_brut_annuel_estime"].notnull()]["Salaire_brut_annuel_estime"]
    selected_salaries = st.slider(
      "Salaire brut annuel estimé (en €)",
      min(salaries), max(salaries),
      (min(salaries), max(salaries))
    )

    if not selected_salaries : selected_salaries = salaries
    df = df[df["Salaire_brut_annuel_estime"].between(min(selected_salaries), max(selected_salaries))]

  with col_filter_year :
    years = df["Annee"].dt.strftime("%Y").sort_values().unique()
    selected_years = st.multiselect("Année", years, placeholder = "20XX")

    if not selected_years : selected_years = years
    df = df[df["Annee"].isin(selected_years)]

with st.container() :
  col_metrics, col_salary_per_discpline = st.columns([2, 6], vertical_alignment = "center")

  with col_metrics :
    st.metric(
      label = "Salaire brut annuel moyen",
      value = f"{df['Salaire_brut_annuel_estime'].mean().round(1)} €",
      border = True
    )
    st.metric(
      label = "Taux d'insertion moyen",
      value = f"{df['Taux_d_insertion'].mean().round(1)} %" if (df['Taux_d_insertion'].any()) else "N/A",
      border = True
    )
    st.metric(
      label = "Taux d'emploi moyen",
      value = f"{df['Taux_d_emploi'].mean().round(1)} %" if (df['Taux_d_emploi'].any()) else "N/A",
      border = True
    )

  with col_salary_per_discpline :
    with st.container(border = True) :
      st.header("Salaires bruts annuels par discipline")

      select = alt.selection_point(name = "select", on = "click")
      highlight = alt.selection_point(name = "highlight", on = "pointerover", empty = False)
      stroke_width = (
        alt.when(select).then(alt.value(2, empty = False))
        .when(highlight).then(alt.value(1))
        .otherwise(alt.value(0))
      )

      st.altair_chart(
        alt.Chart(
          df,
          config = alt.Config(scale = alt.ScaleConfig(bandPaddingInner = 0.2))
        ).mark_bar(cursor = "pointer").encode(
          x = alt.X("mean(Salaire_brut_annuel_estime):Q",
                    title = "Salaire brut annuel estimé (en €)"),
          y = "Discipline:N",
          color = "Discipline:N",
          fillOpacity = alt.when(select).then(alt.value(1)).otherwise(alt.value(0.3)), strokeWidth = stroke_width
        ).add_params(select, highlight)
      )

with st.container() :
  col_insertion_per_academy, col_employment_rate_evolution = st.columns(2)

  with col_insertion_per_academy :
    with st.container(border = True) :
      st.header("Taux d'insertion par établissement")

      selection = alt.selection_point(fields = ["Academie"], bind = "legend")

      st.altair_chart(
        alt.Chart(df).mark_bar().encode(
          x = alt.X("Etablissement:N", title = "Établissement"),
          y = alt.Y("mean(Taux_d_insertion):Q", title = "Taux d'insertion (en %)"),
          color = "Academie:N",
          opacity = alt.when(selection).then(alt.value(0.9)).otherwise(alt.value(0.2))
        ).add_params(selection)
      )

  with col_employment_rate_evolution :
    with st.container(border = True) :
      st.header("Pourcentages d'emplois stables, Taux de chômage par an")
      st.area_chart(
        data = df[["Annee", "Pourcent_emplois_stables", "Taux_de_chomage_regional"]].groupby("Annee").mean().round(1),
        x_label = "Période",
        y_label = "%"
      )

with st.container() :
  st.header('Données brutes')
  st.dataframe(df, hide_index = True)
