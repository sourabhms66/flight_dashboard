import streamlit as st
import plotly.express as px
from db_helper import DB
db = DB()

# adding the side bar
st.sidebar.title('Flight data analysis')

# add a dropdown
user_option = st.sidebar.selectbox('Menu',['Select one','Check Flights','Analytics'])
if user_option == 'Check Flights':

    st.title("Check Flights")
    col1,col2 = st.columns(2)
    city = db.fletch_city_name()
    with col1:
        source = st.selectbox("Source",sorted(city))
    with col2:
        destination = st.selectbox("Destination", sorted(city))
    if st.button('Search'):
        results = db.fletch_all_flights(source,destination)
        st.dataframe(results)

elif user_option =='Analytics':
    st.title("Analytics")
    airline,freq1 = db.fletch_airline_frequency()
    data = {
        'Labels': airline,
        'Values': freq1
    }
    # Create the pie chart using Plotly
    fig = px.pie(data, names='Labels', values='Values', title='Airline frequency')

    # Streamlit app
    st.title('Airline frequency')

    # Display the pie chart in Streamlit
    st.plotly_chart(fig)

    # to plot the bar chart

    #st.title("Analytics")
    city,freq2 = db.busy_airport()

    data = {
        'Labels': city,
        'Values': freq2
    }

    # Create the bar chart using Plotly
    fig = px.bar(data, x='Labels', y='Values', title='Airports')

    # Streamlit app
    st.title('Airports')

    # Display the bar chart in Streamlit
    st.plotly_chart(fig)
    # for line plot
    date,freq3 = db.daily_frequency()
    data = {
        'X': date,
        'Y': freq3
    }

    # Create the line chart using Plotly
    fig = px.line(data, x='X', y='Y', title='Line Plot Example', markers=True)

    # Streamlit app
    st.title('Line Plot Example')

    # Display the line chart in Streamlit
    st.plotly_chart(fig)




else:
    st.title(""" This project is about Historical Data Analysis.
    Here's some key features that are included in this project
    1. Flight Search and Filters
    2. Departure and Arrival Information
    3. Airline Performance Analytics
    4. Interactive Data Visualization
    """)


