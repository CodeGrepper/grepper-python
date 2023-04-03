import unittest
from unittest.mock import patch, Mock
from grepper_python.main import Grepper


class TestGrepper(unittest.TestCase):
    def setUp(self):
        self.api_key = "my_api_key"
        self.grepper = Grepper(self.api_key)

    @patch("grepper_python.main.requests.get")
    def test_search(self, mock_get):
        # Mock the response from the API
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "data": [
                {
                    "id": 1,
                    "content": "example content",
                    "author_name": "example author",
                    "author_profile_url": "https://example.com",
                    "title": "example title",
                    "upvotes": 10,
                    "downvotes": 2,
                }
            ]
        }
        mock_get.return_value = mock_response

        # Test the search function
        results = self.grepper.search(
            query="example query", similarity=80
        )
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].id, 1)
        self.assertEqual(results[0].content, "example content")
        self.assertEqual(results[0].author_name, "example author")
        self.assertEqual(
            results[0].author_profile_url, "https://example.com"
        )
        self.assertEqual(results[0].title, "example title")
        self.assertEqual(results[0].upvotes, 10)
        self.assertEqual(results[0].downvotes, 2)

        # Test that the API was called with the correct parameters
        mock_get.assert_called_once_with(
            "https://api.grepper.com/v1/answers/search",
            params={"query": "example query", "similarity": 80},
            auth=(self.api_key, ""),
        )

    @patch("grepper_python.main.exception_handler")
    @patch("grepper_python.main.requests.get")
    def test_search_with_error(self, mock_get, mock_exception_handler):
        # Mock the response from the API with an error status code
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # Test the search function with an error response
        with self.assertRaises(Exception):
            self.grepper.search(query="example query", similarity=80)

        # Test that the exception handler was called with the correct parameter
        mock_exception_handler.assert_called_once_with("404")
