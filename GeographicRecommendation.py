from geopy import Point
from geopy.distance import geodesic

def assign_weights_for_distance(theaters, original_location, distance = 10):
    # Calcula las distancias a cada ubicación y las guarda en el diccionario
    for theater in theaters:
        if (theater['lat'] is None or theater['lng'] is None or theater['lat'] > 90 or theater['lat'] < -90 or theater['lng'] > 180 or theater['lng'] < -180):
            theater["distance"] = distance + 99999
            continue
        theater["distance"] = geodesic(original_location, Point(theater["lat"],theater["lng"])).kilometers

    # Ordena las ubicaciones por distancia
    theaters.sort(key=lambda x: x["distance"])

    # Imprime las ubicaciones ordenadas por distancia
    for theater in theaters:
        if (theater['distance'] < distance):
            theater['weight'] = 1 - theater['distance'] / distance
            print(f"{theater['Nombre']}: {theater['distance']} km - peso: {theater['weight']}")
        else:
            break;

    return theaters