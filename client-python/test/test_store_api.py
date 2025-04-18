# coding: utf-8

"""
    Agent Protocol

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.6
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ap_client.api.store_api import StoreApi


class TestStoreApi(unittest.TestCase):
    """StoreApi unit test stubs"""

    def setUp(self) -> None:
        self.api = StoreApi()

    def tearDown(self) -> None:
        pass

    def test_delete_item(self) -> None:
        """Test case for delete_item

        Delete Store Item
        """
        pass

    def test_get_item(self) -> None:
        """Test case for get_item

        Get Store Item
        """
        pass

    def test_list_namespaces(self) -> None:
        """Test case for list_namespaces

        List namespaces
        """
        pass

    def test_put_item(self) -> None:
        """Test case for put_item

        Insert or Update Item
        """
        pass

    def test_search_items(self) -> None:
        """Test case for search_items

        Search Store Items
        """
        pass


if __name__ == '__main__':
    unittest.main()
