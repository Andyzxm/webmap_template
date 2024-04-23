import streamlit as st
from streamlit_folium import folium_static
import folium
import ee
import watergeo

markdown = """
Web App URL: <https://watergeo.streamlit.app/>
GitHub Repository: <https://github.com/Andyzxm/webmap_template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://images-platform.99static.com/7WcMmZPzGbVHYpeaib5FcOYR314=/100x100:900x900/500x500/top/smart/99designs-contests-attachments/122/122380/attachment_122380314"
st.sidebar.image(logo)

st.title("Google Earth Engine") 

# Initialize Earth Engine
ee.Initialize()

# Create a folium map
folium_map = folium.Map(location=[40, -100], zoom_start=4)

# Add Earth Engine data or layers to the map
image = ee.Image('JRC/GSW1_2/GlobalSurfaceWater')
vis_params = {'bands': ['occurrence'], 'min': 0, 'max': 100, 'palette': ['blue']}
ee_image = folium.TileLayer(
    tiles=image.getMapId(vis_params)['tile_fetcher'].url_format,
    attr='Google Earth Engine',
    overlay=True,
    name='Global Surface Water',
)
folium_map.add_child(ee_image)

# Display the map in Streamlit
folium_static(folium_map)