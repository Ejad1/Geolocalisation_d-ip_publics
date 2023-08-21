import requests, os

def get_location_from_ip(ip_address):
    url = f"http://ipinfo.io/{ip_address}/json"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if "city" in data:
            city = data["city"]
            region = data.get("region", "")
            country = data.get("country", "")
            location = data.get("loc", "").split(",")
            lat = location[0]
            lon = location[1]
            
            print(f"\nAdresse IP: {ip_address}")
            print(f"Position : {lat}, {lon}")
            print(f"Ville : {city}, Région : {region}, Pays : {country} \n")
        else:
            print("Impossible de récupérer les informations de localisation.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    ip_address = input("Entrez l'adresse IP : ")
    get_location_from_ip(ip_address)

os.system('pause')
