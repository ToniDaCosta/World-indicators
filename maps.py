import plotly.express as px
import streamlit as st
import pandas as pd
import folium
import pydeck as pdk
from streamlit_folium import st_folium

df = pd.read_csv(r"C:\Users\ateso\Desktop\CO2 files\data\Trasnformed_data.csv")

df_cleaned = df.dropna(subset=['latitude', 'longitude'])
df = df_cleaned




app_title = "World Status by 2023"
sub_title = "Data sourced from the World BankData"



def main():

    st.set_page_config(app_title)
    st.title(app_title)
    st.caption(sub_title)

    total_population = df['population'].sum()
    formatted_population = '{:,}'.format(total_population)
    st.title("195 Countries")
    st.write("World Population:", formatted_population)

    st.sidebar.write("Country Details")

    unique_countries = df["country"].unique()

    selected_country = st.sidebar.selectbox("Select a country",unique_countries)

    if selected_country in df["country"].unique():

        st.subheader(selected_country)
        
        filtered_df = df[df["country"] == selected_country]

        st.subheader("Country Information")
        st.write(filtered_df)
        st.map(filtered_df[['latitude', 'longitude']], zoom=4)
       

    else:
        st.subheader("No Data Available For the Country Selected")

    option = st.sidebar.selectbox("Select Dashboard", ("Pollution", "Population", 
    "Birth Rate", "Death Rate" ))

#Need to fix the Co2 emissions not showing.

    if option == "Pollution":
        st.header("Most Polluted Countries")
        map = pdk.Deck(
        map_style='mapbox://styles/mapbox/dark-v9',
        initial_view_state=pdk.ViewState(
        latitude=0,
        longitude=0,
        zoom=1,
        pitch=50,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=df,
                get_position='[longitude, latitude]',
                get_radius='emissions / 1000',  # Adjust radius based on population
                get_fill_color='[250, 0, 0, 80]',  # Red color for population
                pickable=True,
                auto_highlight=True,
            ),
        ],
    )
        st.pydeck_chart(map)
    
        top_10_polluted = df.sort_values(by="emissions", ascending=False).head(10)
        selected_columns = ["country", "emissions", "agricultural land( %)", "urban population percentage", "continent"]
        top_10_selected = top_10_polluted[selected_columns]

        st.write("Top 10 countries Most Polluted")
        st.write(top_10_selected)
       
 

    elif option == "Population":
        st.header("Population Size per Country")
        map = pdk.Deck(
        map_style='mapbox://styles/mapbox/dark-v9',
        initial_view_state=pdk.ViewState(
        latitude=0,
        longitude=0,
        zoom=1,
        pitch=50,
        ),
        layers=[
            pdk.Layer(
            'ScatterplotLayer',
            data=df,
            get_position='[longitude, latitude]',
            get_radius='population / 1000',  # Adjust radius based on population
            get_fill_color='[0, 255, 0, 80]',  # Red color for population
            pickable=True,
            auto_highlight=True,
            ),
        ],
    )
        st.pydeck_chart(map)
    
        top_10_population = df.sort_values(by="population", ascending=False).head(10)
        selected_columns = ["country", "population", "urban_population", "armed forces size", "continent"]
        top_10_selected = top_10_population[selected_columns]

        st.write("Top 10 countries with Most Population")
        st.write(top_10_selected)
    
    elif option == "Birth Rate":
        st.header("Birth Rate per Country")
        map = pdk.Deck(
        map_style='mapbox://styles/mapbox/dark-v9',
        initial_view_state=pdk.ViewState(
        latitude=0,
        longitude=0,
        zoom=1,
        pitch=50,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=df,
                get_position='[longitude, latitude]',
                get_radius='birth / 1000',  # Adjust radius based on population
                get_fill_color='[250, 0, 0, 80]',  # Red color for population
                pickable=True,
                auto_highlight=True,
            ),
        ],
    )
        st.pydeck_chart(map)
    
        top_10_polluted = df.sort_values(by="birth", ascending=False).head(10)
        selected_columns = ["country", "birth","population", "continent"]
        top_10_selected = top_10_polluted[selected_columns]

        st.write("Top 10 Countries with High Birth Rate")
        st.write(top_10_selected)
  
    
    elif option == "Death Rate":
        st.header("Infant Mortality  per Country")
        map = pdk.Deck(
        map_style='mapbox://styles/mapbox/dark-v9',
        initial_view_state=pdk.ViewState(
        latitude=0,
        longitude=0,
        zoom=1,
        pitch=50,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=df,
                get_position='[longitude, latitude]',
                get_radius='imortality / 10',  # Adjust radius based on population
                get_fill_color='[250, 0, 0, 80]',  # Red color for population
                pickable=True,
                auto_highlight=True,
            ),
        ], 
    )
        st.pydeck_chart(map)
    
        top_10_polluted = df.sort_values(by="imortality", ascending=False).head(10)
        selected_columns = ["country", "imortality","population", "continent"]
        top_10_selected = top_10_polluted[selected_columns]

        st.write("Top 10 Countries with High Infant Mortality")
        st.write(top_10_selected)
        st.write()
    
    #elif option == "None":
        #st.write("Please select a dashboard option from the sidebar.")


  

if __name__ == "__main__":
    main()    