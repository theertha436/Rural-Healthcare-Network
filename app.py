import streamlit as st
import folium
from streamlit_folium import st_folium

from dataset import load_data
from clustering import perform_clustering
from graph_builder import draw_graph

st.set_page_config(layout="wide")

# -----------------------------
# MAP FUNCTION
# -----------------------------
def show_map(data):

    m = folium.Map(location=[12.9, 77.5], zoom_start=5)

    colors = ["red","blue","green","purple","orange"]

    for _, row in data.iterrows():
        folium.Marker(
            location=[row["Latitude"], row["Longitude"]],
            popup=f"{row['Village']} (Cluster {row['Cluster']})",
            icon=folium.Icon(color=colors[int(row["Cluster"]) % 5])
        ).add_to(m)

    return m


# -----------------------------
# SESSION STATE INIT
# -----------------------------
if "clustered" not in st.session_state:
    st.session_state.clustered = None

# -----------------------------
# UI START
# -----------------------------
st.title("HealthGraph Dashboard")
st.subheader("Rural Healthcare Network Clustering Visualization")

data = load_data()

# -----------------------------
# BEFORE CLUSTERING
# -----------------------------
st.header("Village Data")
st.dataframe(data)

# -----------------------------
# BUTTON (FIXED)
# -----------------------------
if st.button("Run Clustering"):
    st.session_state.clustered = perform_clustering(data)

# -----------------------------
# SHOW RESULTS (PERSISTENT)
# -----------------------------
if st.session_state.clustered is not None:

    clustered = st.session_state.clustered

    st.header("Clusters")
    st.dataframe(clustered)

    # -----------------------------
    # CLUSTER BOXES
    # -----------------------------
    st.subheader("Cluster Groups")

    cluster_groups = clustered.groupby("Cluster")["Village"].apply(list)

    colors = [
        "#ff6b6b", "#1dd1a1", "#54a0ff",
        "#feca57", "#5f27cd"
    ]

    cols = st.columns(min(len(cluster_groups), 5))

    for idx, (cluster, villages) in enumerate(cluster_groups.items()):
        with cols[idx % 5]:
            st.markdown(
                f"""
                <div style="
                background-color:{colors[idx % len(colors)]};
                padding:15px;
                border-radius:10px;
                color:white;
                text-align:center;
                ">
                <b>Cluster {cluster}</b><br>
                {"<br>".join(villages)}
                </div>
                """,
                unsafe_allow_html=True
            )

    # -----------------------------
    # GRAPH
    # -----------------------------
    st.header("Graph Visualization")

    html = draw_graph(clustered)
    st.components.v1.html(html, height=600)

    # -----------------------------
    # MAP
    # -----------------------------
    st.header("Map Visualization")

    m = show_map(clustered)
    st_folium(m, height=500)