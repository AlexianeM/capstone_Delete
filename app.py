# Smart Charger Advisor: User interface

############################## Remarks ##############################
# st.download_button at the end for user to download result matrix


#####################################################################



# imports
import streamlit as st
import pandas as pd

#def main()

# theme and title config
st.set_page_config(page_title='Smart Charger Advisor: Illwerke und Ihre PV-Anlage')
st.title('Smart Charger Advisor: Illwerke und Ihre PV-Anlage')

# user inputs --> mehrere PV-Anlagen auf unterschiedliche Direktionen erlauben? (2. Taste 'andere PV-Anlage hinzufügen')
# auch möglich, default values zu übernehmen
flaeche = st.number_input('Panelfläche in Quadratmeter')
panelleistung = st.number_input('Panelleistung der PV-Anlage in kWp (typischerweise: 1kWp pro 7 m²)') #button 'About' to add
ausrichtung = st.slider('Ausrichtung des Gebäudes zw. -90 und 90 (Ost:-90, Süd:0, West:90)', min_value=-90, max_value=90, step=10)
dachneigung = st.slider('Dachneigung in ° (0° - horizontal, 90° - vertikal)', min_value=0, max_value=90, step=10)
temp_coeff = st.number_input('Temperaturkoeffizient der PV-Anlage in % (typischerweise: zw. 0.30 und 0.45)') #button 'About' to add
noct = st.number_input('NOCT in °C (typischerweise: 25°C)') #button 'About' to add
ladestation_id = st.text_input('ID Ihrer Ladestation (zB ___________)') 

# button to get smart charger advice
if st.button('Wie stimmt die Illwerke mit meiner PV-Anlage?'):
    if not flaeche: #or not panelleistung or not ausrichtung or not dachneigung or not temp_coeff or not noct or not ladestation_id:
        st.error('Bitte obige Parameter eingeben')
    else:
        try:
            #Funktion zur Outputberechnung
            st.text('Test success')
        except Exception as e:
            st.error(f'An error occured: {e}')