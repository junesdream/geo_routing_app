# Logic to calculate the shortest route

from geopy.distance import geodesic

class RouteCalculator:
    def __init__(self, start_coords, end_coords):
        self.start_coords = start_coords
        self.end_coords = end_coords

    def calculate_shortest_distance(self):
        """Calculate the shortest distance between two coordinates using geodesic distance."""
        return geodesic(self.start_coords, self.end_coords).km
