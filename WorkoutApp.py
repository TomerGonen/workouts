import streamlit as st

# === TITLE ===
st.title("📍 Get My Location")

# Button to trigger location request
st.markdown("""
<button onclick="getLocation()">Get My Location</button>

<script>
function getLocation() {
    navigator.geolocation.getCurrentPosition(
        function(pos) {
            const lat = pos.coords.latitude;
            const lon = pos.coords.longitude;
            window.location.href = `?lat=${lat}&lon=${lon}`;
        },
        function(err) {
            alert("GPS access denied or unavailable.");
        }
    );
}
</script>
""", unsafe_allow_html=True)

# Read from query params
params = st.query_params
lat = params.get("lat", [None])[0]
lon = params.get("lon", [None])[0]

# Show result if available
if lat and lon:
    st.success(f"Latitude: {lat}")
    st.success(f"Longitude: {lon}")
else:
    st.info("Tap the button to get your location.")

