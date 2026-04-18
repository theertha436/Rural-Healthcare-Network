import pandas as pd
import random

def load_data():

    villages = [
        ("Village_1", 12.9716, 77.5946),
        ("Village_2", 13.0827, 80.2707),
        ("Village_3", 11.0168, 76.9558),
        ("Village_4", 12.2958, 76.6394),
        ("Village_5", 10.8505, 76.2711),
        ("Village_6", 9.9252, 78.1198),
        ("Village_7", 11.1271, 78.6569),
        ("Village_8", 13.6288, 79.4192),
        ("Village_9", 12.9141, 74.8560),
        ("Village_10", 15.3173, 75.7139),
        ("Village_11", 17.3850, 78.4867),
        ("Village_12", 16.5062, 80.6480)
    ]

    disease = ["Malaria", "Dengue", "Flu"]
    phcs = ["PHC1", "PHC2", "PHC3"]

    data = []

    for v in villages:
        data.append({
            "Village": v[0],
            "Latitude": v[1],
            "Longitude": v[2],
            "DiseaseType": random.choice(disease),
            "PHC": random.choice(phcs),
            "Patients": random.randint(10, 100),
            "Distance": random.randint(1, 50)
        })

    return pd.DataFrame(data)