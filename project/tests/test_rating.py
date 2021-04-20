import json
import unittest
from project.tests.base import BaseTestCase
from project.api.models import Rate
from project.api.models import db

RATE_BASE_URL = "/rating"
CONTENT_TYPE = "application/json"


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
