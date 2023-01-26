import exifread as ef
from geopy.geocoders import Nominatim

def _convert_to_degress(value):
    d = float(value.values[0].num) / float(value.values[0].den)
    m = float(value.values[1].num) / float(value.values[1].den)
    s = float(value.values[2].num) / float(value.values[2].den)
    return d + (m / 60.0) + (s / 3600.0)


def getGPS(filepath):
    with open(filepath, 'rb') as f:
        tags = ef.process_file(f)
        latitude = tags.get('GPS GPSLatitude')
        longitude = tags.get('GPS GPSLongitude')
        if latitude:
            lat_value = _convert_to_degress(latitude)
        if longitude:
            lon_value = _convert_to_degress(longitude)
        return lat_value, lon_value


if __name__ == "__main__":
    file_path = 'swan.jpg'
    latitude, longitude = getGPS(file_path)
    print(latitude)
    print(longitude)
    geolocator = Nominatim(user_agent="test3")
    location = geolocator.reverse(f"{latitude}, {longitude}")
    print(location.address)