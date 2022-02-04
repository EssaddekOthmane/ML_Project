import numpy as np
import pandas as pd
import streamlit as st
import altair as alt

df=pd.read_csv('heart.csv')
st.dataframe(df)
st.markdown("On propose en premier lieu de regarder quelques graphiques descriptive de notre base de donnée")

age_target=pd.crosstab(df['age'],df['target'])
sex_target=pd.crosstab(df.sex,df.target)
trestbps_target=pd.crosstab(df.trestbps,df.target)
chol_target=pd.crosstab(df.chol,df.target)

dica=age_target.to_dict()
dfa=pd.concat({k: pd.Series(v) for k, v in dica.items()}).reset_index()
dfa.columns = ['0_1', 'level','variable']

dictres=trestbps_target.to_dict()
dftres=pd.concat({k: pd.Series(v) for k, v in dictres.items()}).reset_index()
dftres.columns = ['0_1', 'level','variable']

dicsex=sex_target.to_dict()
dfsex=pd.concat({k: pd.Series(v) for k, v in dicsex.items()}).reset_index()
dfsex.columns = ['0_1', 'level','variable']

diccol=chol_target.to_dict()
dfcol=pd.concat({k: pd.Series(v) for k, v in diccol.items()}).reset_index()
dfcol.columns = ['0_1', 'level','variable']



gp_charta = alt.Chart(dfa).mark_bar().encode(
  alt.Column('0_1'), alt.X('level'),
  alt.Y('variable', axis=alt.Axis(grid=False)), 
  alt.Color('0_1'))

gp_chartcol = alt.Chart(dfcol).mark_bar().encode(
  alt.Column('0_1'), alt.X('level'),
  alt.Y('variable', axis=alt.Axis(grid=False)), 
  alt.Color('0_1'))


gp_charttres = alt.Chart(dftres).mark_bar().encode(
  alt.Column('0_1'), alt.X('level'),
  alt.Y('variable', axis=alt.Axis(grid=False)), 
  alt.Color('0_1'))

gp_chartsex = alt.Chart(dfsex).mark_bar().encode(
  alt.Column('0_1'), alt.X('level'),
  alt.Y('variable', axis=alt.Axis(grid=False)), 
  alt.Color('0_1'))



st.altair_chart(gp_charta, use_container_width=False)
st.altair_chart(gp_chartsex, use_container_width=False)
st.altair_chart(gp_chartcol, use_container_width=False)
st.altair_chart(gp_charttres, use_container_width=False)
plot_tab=pd.crosstab(df.age,df.target)

scater_age_col=alt.Chart(df).mark_point().encode(
    x='age',
    y='chol',
    color=alt.Color('target',  scale=alt.Scale(scheme='dark2'),legend=alt.Legend(title="age VS chol"))
)



#trestbps
st.altair_chart(scater_age_col, use_container_width=False)

class variable(str):
  
  def__init(self,str)__:
    
    if str=='Age':
      slef.name='age
    if str=='Cholesterol':
      self.name='chol'
    if str=='Sex':
      self.name='sex
    if str=='Chest pain':
      self.name='cp'
    if str=='Resting blood pressure':
      self.name='trestbps'
    if str=='Fasting blood sugar':
      self.name='fbs'
    if str=='Resting electrocardiographic results':
      self.name='restecg'
       
      
