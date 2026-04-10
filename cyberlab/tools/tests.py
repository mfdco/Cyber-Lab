from django.test import TestCase
from django.urls import reverse

from .utils import (
    decode_base64,
    decode_hex,
    decode_url,
    encode_base64,
    encode_hex,
    encode_url,
    rot13_text,
)


class ToolTests(TestCase):
    # This test checks that normal text is turned into the correct Base64 value.
    def test_encode_base64(self):
        result = encode_base64("hello")
        self.assertEqual(result, "aGVsbG8=")

    # This test checks that a Base64 value is turned back into normal text.
    def test_decode_base64(self):
        result = decode_base64("aGVsbG8=")
        self.assertEqual(result, "hello")

    # This test checks that text is turned into the correct hex value.
    def test_encode_hex(self):
        result = encode_hex("hello")
        self.assertEqual(result, "68656c6c6f")

    # This test checks that hex is turned back into normal text.
    def test_decode_hex(self):
        result = decode_hex("68656c6c6f")
        self.assertEqual(result, "hello")

    # This test checks that text is turned into the correct URL-encoded value.
    def test_encode_url(self):
        result = encode_url("hello world!")
        self.assertEqual(result, "hello%20world%21")

    # This test checks that URL-encoded text is turned back into normal text.
    def test_decode_url(self):
        result = decode_url("hello%20world%21")
        self.assertEqual(result, "hello world!")

    # This test checks that ROT13 shifts letters by 13 positions.
    def test_rot13_text(self):
        result = rot13_text("uryyb")
        self.assertEqual(result, "hello")

    # This test checks that the hex view returns JSON for a valid encode request.
    def test_hex_view(self):
        response = self.client.post(
            reverse("hex_tool"),
            {"text": "hello", "action": "encode"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["result"], "68656c6c6f")
