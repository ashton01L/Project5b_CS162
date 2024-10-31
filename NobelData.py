# Author: Ashton Lee
# Github User: ashton01L
# Date: 10/30/2024
# Description: Write a class named NobelData that reads a JSON file containing data on Nobel Prizes and allows the user
# to search that data.
import json


class NobelData:
    """
    A class to represent objects within NobelData
    """
    def __init__(self):
        """
        Initializes NobelData
        """
        # Initialize by reading the Nobel Prize data from nobels.json
        with open("nobels.json", "r") as file:
            self._data = json.load(file)

    def search_nobel(self, year, category):
        """
        Searches for Nobel Prize winners by year and category.

        :param year: The year of the prize as a string.
        :param category: The category of the prize.
        :return: A sorted list of laureate surnames in the specified year and category.
        """
        surnames = []

        # Navigate through the loaded JSON data to find the desired entries
        for prize in self._data.get("prizes", []):
            if prize.get("year") == year and prize.get("category") == category:
                # Gather laureates' surnames for the specified year and category
                for laureate in prize.get("laureates", []):
                    if "surname" in laureate:
                        surnames.append(laureate["surname"])

        # Sort the surnames alphabetically and return them
        return sorted(surnames)


# # Initialize the NobelData instance
# nd = NobelData()
#
# # Search for Economics Nobel winners in 2001
# print(nd.search_nobel("2001", "economics"))  # Example output: ['Akerlof', 'Spence', 'Stiglitz']
