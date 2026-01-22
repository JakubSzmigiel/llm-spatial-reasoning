# Hybrid LLM + Routing API agent
"""
Hybrid agent combining LLM reasoning with deterministic routing API calls.
"""

from routes_api import get_route_distance


class HybridRoutingAgent:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def estimate_distance(self, origin_coords, destination_coords):
        return get_route_distance(
            origin_coords,
            destination_coords,
            self.api_key
        )
