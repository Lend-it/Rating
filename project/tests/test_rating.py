import json
import unittest
from project.tests.base import BaseTestCase
from project.api.models import Rate
from project.api.models import db
from project.tests.utils import add_rate

RATE_BASE_URL = "/rating"
CONTENT_TYPE = "application/json"
FAKE_STARS = 3
FAKE_REVIEW = "Capotou meu corsa"
FAKE_REVIEWED = "maia@email.com"
FAKE_REVIEWER = "vinicius@email.com"
FAKE_REQUESTID = "c6554f6d-13b3-4aa5-aae2-d564fe4d9bac"


class TestRating(BaseTestCase):
    def test_create_rating(self):
        with self.client:
            response = self.client.post(
                RATE_BASE_URL,
                data=json.dumps(
                    {
                        "stars": 4,
                        "review": "Maia é uma boa pessoa, devolveu meu celta no prazo",
                        "report": False,
                    }
                ),
                headers={
                    "reviewer": "rogerio@email.com",
                    "reviewed": "esio@email.com",
                    "requestid": "fce61c6d-1cb0-488c-a2fa-6a90fdbe192d",
                },
                content_type=CONTENT_TYPE,
            )

            data = json.loads(response.data.decode())

            self.assertEqual(response.status_code, 201)
            self.assertIn("success", data["status"])

    def test_create_rating_invalid_json(self):
        with self.client:
            response = self.client.post(
                RATE_BASE_URL,
                data=json.dumps({}),
                headers={
                    "reviewer": "rogerio@email.com",
                    "reviewed": "esio@email.com",
                    "requestid": "fce61c6d-1cb0-488c-a2fa-6a90fdbe192d",
                },
                content_type="application/json",
            )

            data = json.loads(response.data.decode())

            self.assertEqual(response.status_code, 400)
            self.assertIn("Invalid payload.", data["message"])
            self.assertIn("fail", data["status"])

    def test_create_rating_invalid_header(self):
        with self.client:
            response = self.client.post(
                RATE_BASE_URL,
                data=json.dumps(
                    {
                        "stars": 4,
                        "review": "Maia é uma boa pessoa, devolveu meu celta no prazo",
                        "report": False,
                    }
                ),
                headers={},
                content_type=CONTENT_TYPE,
            )

            data = json.loads(response.data.decode())

            self.assertEqual(response.status_code, 400)
            self.assertIn("Invalid payload.", data["message"])
            self.assertIn("fail", data["status"])

    def teste_get_all_rates(self):
        add_rate(
            FAKE_STARS,
            FAKE_REVIEW,
            False,
            FAKE_REVIEWED,
            FAKE_REVIEWER,
            FAKE_REQUESTID
        )
        if self.client:
            response = self.client.get(RATE_BASE_URL)
            data = json.loads(response.data.decode())

            self.assertEqual(response.status_code, 200)
            self.assertIn("success", data["status"])

            self.assertEqual(len(data["data"]["rates"]), 1)
