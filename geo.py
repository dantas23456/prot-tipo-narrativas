from geopy.geocoders import Nominatim
import folium
import time

geolocator = Nominatim(user_agent="tcc_geo")

dados = [
    {
        "narrativa": "Narrativa anta esfolada",
        "endereco": "Goianinha, RN, Brasil"
    },
    {
        "narrativa": "haja pau",
        "endereco": "Natal, RN, Brasil"
    },
    {
        "narrativa": "papa figo",
        "endereco": "Parnamirim, RN, Brasil"
    },
    {
        "narrativa": "homem do lixo",
        "endereco": "São José de Mipibu, RN, Brasil"
    }
]


mapa = folium.Map(location=[-14.2350, -51.9253], zoom_start=5)


for item in dados:
    location = geolocator.geocode(item["endereco"])
    time.sleep(1)  # evita bloqueio do serviço

    if location:
        folium.Marker(
            [location.latitude, location.longitude],
            popup=f"<b>Narrativa:</b> {item['narrativa']}<br><b>Endereço:</b> {item['endereco']}"
        ).add_to(mapa)


mapa.save("mapa.html")

print("Mapa criado com sucesso!")