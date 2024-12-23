import streamlit as st

welcome_page = st.Page("welcomepage.py", title="Strona powitalna", icon="👋")
stations_page = st.Page("stations.py", title="Stacje", icon="🗼")
sensor_data_page = st.Page("current/sensor_data.py", title="Dane z sensorów", icon="📡")
plot_page = st.Page("current/plot.py", title="Wykres najnowszych pomiarów", icon="📈")

if 'selected_station_id' not in st.session_state:
    st.session_state.selected_station_id = None
if 'selected_station_name' not in st.session_state:
    st.session_state.selected_station_name = None
if 'selected_sensor_id' not in st.session_state:
    st.session_state.selected_station_id = None
if 'selected_station_attribute' not in st.session_state:
    st.session_state.selected_station_attribute = None
    
pg = st.navigation({"Ogólne": [welcome_page, stations_page], "Aktualne dane": [sensor_data_page, plot_page]})
pg.run()