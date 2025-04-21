import streamlit as st

# === TITLE ===
st.title("🏃 GPS Speed Tracker")

# === JAVASCRIPT TO GET GPS POSITION FROM BROWSER ===
st.markdown("""
<script>
navigator.geolocation.getCurrentPosition(
    function(pos) {
        const lat = pos.coords.latitude.toFixed(6);
        const lon = pos.coords.longitude.toFixed(6);
        const now = new Date().getTime();
        window.location.href = `?lat=${lat}&lon=${lon}&t=${now}`;
    },
    function(err) {
        alert("Please allow GPS access.");
    }
);
</script>
""", unsafe_allow_html=True)

# === READ POSITION DATA FROM URL PARAMS ===
params = st.query_params
lat = float(params.get("lat", [0])[0])
lon = float(params.get("lon", [0])[0])
timestamp = int(params.get("t", [0])[0])

if lat == 0.0 and lon == 0.0:
    st.info("📡 Waiting for location...")

st.metric("📍 Latitude", lat)
st.metric("📍 Longitude", lon)
