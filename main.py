from numpy import number
import phonenumbers
import folium
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode

number = "+27653132285"
pepnumber =  phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)


service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))


key = 'ba156f57e2364ad39e46e0556105cd27'

geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)


try:
    device_lat = -33.9190
    device_lon = 18.4242
    import folium
    myMap = folium.Map(location=[device_lat, device_lon], zoom_start=9)
    folium.Marker([device_lat, device_lon], popup='Device_location').add_to(myMap)
    
    myMap.save("device_location.html")
except IndexError:
    print("Error: The result list is empty")
except KeyError:
    print("Error: Missing key in the dictionary")




