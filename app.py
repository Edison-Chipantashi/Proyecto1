import streamlit as st
import pandas as pd
import lasio
st.title("Aplicación para Registros de Pozos")
st.sidebar.title("Menú")
#widget necesita asignar variables
opciones_inicio=st.sidebar.radio("Seleccione una opción", ["Inicio", "Datos","Cálculos"])

##Leer el registro .LAS
archivo_las=lasio.read("Pozo-1.LAS")
df=archivo_las.df()

##

if opciones_inicio=="Inicio":
	st.write("Ingresó al Inicio")
	st.write(df)
if opciones_inicio=="Datos":
	st.write("Ingresó a Datos")
	barra_deslizador=st.slider("Seleccione un valor", 1, 100, 30)
	st.write("El valor selecciona es", barra_deslizador)
	ingreso_numero=st.number_input("Ingrese un valor", min_value=1.00, max_value=1000.00, value=300.00)
if opciones_inicio=="Cálculos":
	st.write("Ingresó a Cálculos")
	selection=st.selectbox("Seleccione una opción", [1,2,3,"A"])
	check1=st.checkbox("Activar")
	if check1==True: #comparacion con doble igual
		st.write("Check activo")
archivo_subido=st.sidebar.file_uploader("Cargar archivo excel", type=[".xls",".xlsx"])  #cargar archivo excel
if archivo_subido is not None:
	df2=pd.read_excel(archivo_subido)
	st.write(df2)

genre = st.radio("What's your favorite movie genre",("Comedy", "Drama", "Documentary"))
if genre =="Comedy":
	st.write("You selected comedy.")
else:
	st.write("You didn't select comedy.")
