# OpenRouteService API integration
"""
OpenRouteService API integration for retrieving real bicycle route distances.
"""

import requests


BASE_URL = "https://api.openrouteservice.org/v2/directions/cycling-regular"


def get_route_distance(origin_coords, destination_coords, api_key: str) -> float:
    headers = {
        "Authorization": api_key,
        "Content-Type": "application/json"
    }

    body = {
        "coordinates": [origin_coords, destination_coords]
    }

    response = requests.post(BASE_URL, json=body, headers=headers)
    response.raise_for_status()

    data = response.json()
    distance_meters = data["features"][0]["properties"]["segments"][0]["distance"]
    return distance_meters / 1000.0
