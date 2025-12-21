import streamlit as st

st.set_page_config(
  layout = "wide",
  page_icon = "./assets/icons/mortarboard.png",
  page_title = "Tableau de bord - Licences professionnelles"
)

st.markdown(
  """
  <style>
    [data-testid = "stMetric"] { text-align: center; }
  </style>
  """,
  unsafe_allow_html = True
)

st.logo("./assets/icons/mortarboard.png", size = "large")
pg = st.navigation(position = "top", pages = [
  st.Page("./pages/dashboard.py", title = "Tableau de bord", default = True),
  st.Page("./pages/analysis.py", title = "Analyse des données")
]).run()
