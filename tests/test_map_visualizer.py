import unittest
import os
from src.map_visualizer import MapVisualizer


class TestMapVisualizer(unittest.TestCase):

    def test_visualize_route(self):
        # Define test coordinates
        berlin_coords = (52.5200, 13.4050)  # Berlin
        paris_coords = (48.8566, 2.3522)  # Paris

        # Define a test distance
        test_distance = 878.5  # km, approximate distance between Berlin and Paris

        # Create an instance of MapVisualizer
        map_visualizer = MapVisualizer(berlin_coords, paris_coords)

        # Call the method to generate the map
        map_visualizer.visualize_route(test_distance)

        # Check if the file 'route_map.html' has been created
        self.assertTrue(os.path.exists('route_map.html'))

        # Clean up by removing the generated file after the test
        if os.path.exists('route_map.html'):
            os.remove('route_map.html')


if __name__ == '__main__':
    unittest.main()
