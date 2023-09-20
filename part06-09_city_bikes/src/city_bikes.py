
def get_station_data(filename: str):
    station_data = {}
    with open(filename) as file: 
        for line in file: 
            line = line.split(";")
            if line[0] == "Longitude":
                continue
            station_data[line[3]] = (float(line[0]), float(line[1]))
    return station_data

def  distance(stations: dict, station1: str, station2: str):
    for k, v in stations.items():
        if k == station1:
            longitude1 = (v[0])
            latitude1 = (v[1])
        if k == station2:
            longitude2 = (v[0])
            latitude2 = (v[1])

    import math
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km


def greatest_distance(stations: dict):
    dist = 0
    for stat1 in stations:
        for stat2 in stations: 
            way = distance(stations, stat1, stat2)
            if way > dist:
                dist = way
                tuple = (stat1, stat2, dist)

    return tuple



# stations = get_station_data('stations1.csv')
# station1, station2, greatest = greatest_distance(stations)
# print(station1, station2, greatest)
