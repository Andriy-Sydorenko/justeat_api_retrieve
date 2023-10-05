import json
import re
import traceback
from datetime import datetime

import requests
from requests import exceptions
from slugify import slugify


class JustEatException(Exception):
    pass


class Client:
    _BASE_URL = "https://uk.api.just-eat.io/restaurants/bypostcode/"

    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.172"  # noqa
    }

    @staticmethod
    def _write_data_to_file(data, postcode: str, filename: str = None) -> None:
        postcode = postcode.replace(" ", "")

        if not filename:
            filename = f"{slugify(postcode)}_{datetime.now().microsecond}.json"
        else:
            filename = f"{filename}.json"

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def _validate_postcode(postcode: str):
        pattern = r"^(GIR 0AA|[A-PR-UWYZ]([0-9]{1,2}|([A-HK-Y][0-9]([0-9ABEHMNPRV-Y])?)|[0-9][A-HJKPS-UW])\ [0-9][ABD-HJLNP-UW-Z]{2})$"  # noqa
        return bool(re.match(pattern, postcode))

    def _get_json_data_from_api(self, postcode: str):
        try:
            if not self._validate_postcode(postcode):
                raise JustEatException("Wrong postcode!")

            response = requests.get(
                url=f"{self._BASE_URL}{postcode}", headers=self.HEADERS
            )

            if response.status_code == 403:
                raise JustEatException(
                    "Access is forbidden! Maybe try using VPN?"
                )
            elif response.status_code == 404:
                raise JustEatException("URL not found!")

        except (
            JustEatException,
            exceptions.ConnectionError,
            exceptions.ConnectTimeout,
            exceptions.InvalidURL,
            exceptions.InvalidSchema,
            exceptions.MissingSchema,
        ) as error:
            traceback_str = traceback.format_exc()
            raise type(error)(f"{error}\n{traceback_str}") from error

        response_json = response.json()

        return response_json

    def by_postal_code(
        self, postcode: str, write_to_file: bool = False, filename: str = None
    ) -> list:
        json_data = self._get_json_data_from_api(postcode)

        restaurants = json_data["Restaurants"]
        result_restaurants = []

        for restaurant in restaurants:
            restaurant_name = restaurant["Name"]
            restaurant_city = restaurant["City"]
            restaurant_rating = restaurant["RatingStars"]
            restaurant_rating_info = restaurant["Rating"]
            restaurant_cuisines = restaurant["Cuisines"]

            result_restaurants.append(
                {
                    "Name": restaurant_name,
                    "City": restaurant_city,
                    "StarRating": restaurant_rating,
                    "RatingInfo": restaurant_rating_info,
                    "Cuisines": restaurant_cuisines,
                }
            )

        if write_to_file:
            self._write_data_to_file(
                data=result_restaurants, postcode=postcode, filename=filename
            )

        return result_restaurants

    def __str__(self) -> str:
        return "JustEatClient: A client to fetch restaurants by postcode."
