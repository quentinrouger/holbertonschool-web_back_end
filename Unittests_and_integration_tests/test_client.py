#!/usr/bin/env python3
"""Test_client module
"""
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class"""

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org: str, mock_get_json) -> None:
        """Tests the org method"""
        mock_get_json.return_value = {}

        client = GithubOrgClient(org)
        result = client.org
        self.assertEqual(result, {})
        mock_get_json.assert_called_once()

    def test_public_repos_url(self):
        """Test the public_repos_url property
        """
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mock_public_repos_url:

            mock_public_repos_url.return_value = {"http://example.com"}
            client = GithubOrgClient("test")
            result = client.org
            self.assertEqual(result, {"http://example.com"})

    def test_public_repos(self):
        """Test the public_repos method
        """
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_public_repos_url:

            mock_public_repos_url.return_value = "http://example.com"
            with patch("client.get_json") as mock_get_json:
                mock_get_json.return_value = [{"name": "test"}]
                client = GithubOrgClient("test")
                result = client.public_repos()
                self.assertEqual(result, ["test"])
                mock_get_json.assert_called_once_with("http://example.com")
