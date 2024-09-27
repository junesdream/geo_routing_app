import unittest
from unittest.mock import patch
from src.geo_data_analyzer import GeoDataAnalyzer


class TestGeoDataAnalyzer(unittest.TestCase):

    @patch('src.geo_data_analyzer.GeoDataAnalyzer.get_places_from_osm')
    def test_get_places_from_osm(self, mock_get_places):
        # Simuliere API-Ergebnis mit Mocking
        mock_get_places.return_value = [
            {"name": "Restaurant A", "coords": (52.5200, 13.4050)},
            {"name": "Restaurant B", "coords": (52.5210, 13.4060)}
        ]

        analyzer = GeoDataAnalyzer(map_center=(52.5200, 13.4050))
        places = analyzer.get_places_from_osm("restaurant")

        self.assertEqual(len(places), 2)
        self.assertEqual(places[0]['name'], "Restaurant A")
        self.assertEqual(places[1]['coords'], (52.5210, 13.4060))

    def test_visualize_places(self):
        analyzer = GeoDataAnalyzer(map_center=(52.5200, 13.4050))
        places = [
            {"name": "Restaurant A", "coords": (52.5200, 13.4050)},
            {"name": "Restaurant B", "coords": (52.5210, 13.4060)}
        ]

        # Test ob das Visualisierungsfile erstellt wird
        analyzer.visualize_places(places)
        # Hier könnte man testen, ob die Datei 'osm_places_map.html' existiert
        # Beispiel:
        with open("osm_places_map.html") as f:
            self.assertIn("Restaurant A", f.read())


if __name__ == '__main__':
    unittest.main()
