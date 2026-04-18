from pyvis.network import Network

def draw_graph(df):

    net = Network(height="600px", width="100%", bgcolor="#222", font_color="white")

    colors = [
        "#ff6b6b", "#1dd1a1", "#54a0ff",
        "#feca57", "#5f27cd", "#48dbfb"
    ]

    # Add PHC nodes
    phcs = df["PHC"].unique()
    for phc in phcs:
        net.add_node(phc, label=phc, color="orange", size=30)

    # Add village nodes
    for _, row in df.iterrows():

        color = colors[row["Cluster"] % len(colors)]

        net.add_node(
            row["Village"],
            label=row["Village"],
            color=color,
            size=20
        )

        # Bipartite edge
        net.add_edge(row["Village"], row["PHC"])

    return net.generate_html()