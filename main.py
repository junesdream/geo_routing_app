from src.route_calculator import RouteCalculator
from src.map_visualizer import MapVisualizer
from src.geo_data_analyzer import GeoDataAnalyzer

def main():
    # Define start and end coordinates (Berlin to Paris for example)
    start_coords = (52.5200, 13.4050)  # Berlin
    end_coords = (48.8566, 2.3522)     # Paris

    # Calculate the shortest route
    route_calculator = RouteCalculator(start_coords, end_coords)
    distance = route_calculator.calculate_shortest_distance()
    print(f"The shortest distance between the two points is {distance:.2f} km.")

    # Visualize the route
    map_visualizer = MapVisualizer(start_coords, end_coords)
    map_visualizer.visualize_route(distance)
    print("Route map saved as 'route_map.html'.")

    # Now fetch and visualize POIs from OpenStreetMap using Overpass API
    analyzer = GeoDataAnalyzer(map_center=start_coords)

    # Fetch and visualize restaurants
    restaurants = analyzer.get_places_from_osm("restaurant")
    if restaurants:
        analyzer.visualize_places(restaurants)
        print(f"Found {len(restaurants)} restaurants. Map saved as 'osm_places_map.html'.")
    else:
        print("No restaurants found in the area.")

if __name__ == "__main__":
    main()
