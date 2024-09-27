import unittest
from unittest.mock import patch
from main import main
import os


class TestAppIntegration(unittest.TestCase):

    @patch('src.geo_data_analyzer.GeoDataAnalyzer.get_places_from_osm')
    @patch('src.route_calculator.RouteCalculator.calculate_shortest_distance')
    def test_main(self, mock_calculate_distance, mock_get_places):
        # Mock the return values for route calculation and POI fetching
        mock_calculate_distance.return_value = 878.5  # Mocked distance between Berlin and Paris
        mock_get_places.return_value = [
            {"name": "Restaurant A", "coords": (52.5200, 13.4050)},
            {"name": "Restaurant B", "coords": (52.5210, 13.4060)}
        ]

        # Run the main function
        main()

        # Check if the route_map.html was created
        self.assertTrue(os.path.exists('route_map.html'))

        # Check if the osm_places_map.html was created
        self.assertTrue(os.path.exists('osm_places_map.html'))

        # Clean up by removing generated files after the test
        if os.path.exists('route_map.html'):
            os.remove('route_map.html')
        if os.path.exists('osm_places_map.html'):
            os.remove('osm_places_map.html')


if __name__ == '__main__':
    unittest.main()
