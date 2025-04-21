import streamlit as st
# from streamlit_folium import st_folium
# import folium

st.set_page_config(layout="wide")
st.title("📱 Demo Workout App")

# Refresh every ~20 seconds
st.experimental_rerun() if st.experimental_get_query_params().get("refresh") else None
st.markdown('<meta http-equiv="refresh" content="20">', unsafe_allow_html=True)

# Inject JavaScript to get geolocation
st.markdown("""
    <script>
    navigator.geolocation.getCurrentPosition(
        (pos) => {
            const coords = `${pos.coords.latitude},${pos.coords.longitude}`;
            window.location.href = `?coords=${coords}&refresh=true`;
        },
        (err) => alert("Location permission is required.")
    );
    </script>
""", unsafe_allow_html=True)

# Get coords from URL
params = st.experimental_get_query_params()
coords = params.get("coords", ["0,0"])[0].split(",")
lat, lon = float(coords[0]), float(coords[1])

# Display location on map
# st.write(f"📍 Your Current Location is: \n{lat = }\n{lon  = }")
# m = folium.Map(location=[lat, lon], zoom_start=17)
# folium.Marker([lat, lon], tooltip="You").add_to(m)
# st_folium(m, width=700, height=500)
