import Connector
import GeographicRecommendation
from geopy import Point

my_location = Point(-31.42008329999999, -64.1887761)

connection = Connector.create_conn()
theaters = Connector.get_query(connection, 'SELECT * FROM Teatros;')
theaters = GeographicRecommendation.assign_weights_for_distance(theaters, my_location, 10) # de la ubicación a 10km
