import unittest
from geopy.distance import geodesic
from src.route_calculator import RouteCalculator


class TestRouteCalculator(unittest.TestCase):

    def test_calculate_shortest_distance(self):
        # Define test coordinates
        berlin_coords = (52.5200, 13.4050)  # Berlin
        paris_coords = (48.8566, 2.3522)  # Paris

        # Create an instance of RouteCalculator
        route_calculator = RouteCalculator(berlin_coords, paris_coords)

        # Calculate the distance
        distance = route_calculator.calculate_shortest_distance()

        # Calculate expected distance using geodesic
        expected_distance = geodesic(berlin_coords, paris_coords).km

        # Assert that the calculated distance is equal to the expected distance
        self.assertAlmostEqual(distance, expected_distance, places=2)


if __name__ == '__main__':
    unittest.main()
