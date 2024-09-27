import folium
import overpy

class GeoDataAnalyzer:
    def __init__(self, map_center):
        self.map_center = map_center
        self.api = overpy.Overpass()

    def get_places_from_osm(self, place_type):
        """Fetch places (e.g. restaurants, gas stations) from OSM using Overpass API."""
        query = f"""
        [out:json];
        node
          ["amenity"="{place_type}"]
          (around:5000,{self.map_center[0]},{self.map_center[1]});
        out body;
        """
        result = self.api.query(query)
        places = []
        for node in result.nodes:
            places.append({
                "name": node.tags.get("name", "Unknown"),
                "coords": (node.lat, node.lon)
            })
        return places

    def visualize_places(self, places):
        """Visualize places fetched from OSM on a Folium map."""
        m = folium.Map(location=self.map_center, zoom_start=13)
        for place in places:
            folium.Marker(place['coords'], tooltip=place['name']).add_to(m)
        m.save('osm_places_map.html')

if __name__ == "__main__":
    analyzer = GeoDataAnalyzer(map_center=(52.5200, 13.4050))  # Berlin

    # Fetch and visualize restaurants from OSM
    restaurants = analyzer.get_places_from_osm("restaurant")
    analyzer.visualize_places(restaurants)
    print("OSM Places map saved as 'osm_places_map.html'.")
