# Logic to visualize routes on a map
import folium

class MapVisualizer:
    def __init__(self, start_coords, end_coords):
        self.start_coords = start_coords
        self.end_coords = end_coords

    def visualize_route(self, route_distance):
        """Visualize the route on a Folium map and save it as an HTML file."""
        m = folium.Map(location=self.start_coords, zoom_start=13)
        folium.Marker(self.start_coords, tooltip="Start").add_to(m)
        folium.Marker(self.end_coords, tooltip="End").add_to(m)
        folium.PolyLine([self.start_coords, self.end_coords], color="blue", weight=2.5, opacity=1).add_to(m)
        folium.Marker(
            self.end_coords,
            tooltip=f"Distance: {route_distance:.2f} km"
        ).add_to(m)
        m.save('route_map.html')
