import pandas as pd
import numpy as np
from sqlalchemy import create_engine

# Assume we have SQLAlchemy Engine as 'engine'
engine = create_engine('postgresql://user:password@localhost:5432/mydatabase')

GIVEN_LATITUDE = 40.7128  # replace with your latitude
GIVEN_LONGITUDE = -74.0060  # replace with your longitude

# Load data into pandas DataFrame
query = "SELECT * FROM navdata"
df = pd.read_sql(query, engine)

# Ensure latitude and longitude are float values
df['latitude'] = df['latitude'].astype(float)
df['longitude'] = df['longitude'].astype(float)

# Define the haversine function for the distance calculation
def haversine(lat1, lon1, lat2, lon2):
    R = 3956  # radius of the earth in miles
    phi1 = np.radians(lat1)
    phi2 = np.radians(lat2)
    delta_phi = np.radians(lat2 - lat1)
    delta_lambda = np.radians(lon2 - lon1)
    a = np.sin(delta_phi/2)**2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda/2)**2
    res = R * (2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)))
    return np.round(res, 2)

# Apply haversine function to each row in the DataFrame
df['distance'] = haversine(GIVEN_LATITUDE, GIVEN_LONGITUDE, df['latitude'], df['longitude'])

# Sort by distance and take the first 5
df_closest = df.sort_values('distance').head(5)

print(df_closest)
