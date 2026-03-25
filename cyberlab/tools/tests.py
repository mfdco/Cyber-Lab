from django.test import TestCase

from .utils import decode_base64, encode_base64


class ToolTests(TestCase):
    # This test checks that normal text is turned into the correct Base64 value.
    def test_encode_base64(self):
        result = encode_base64("hello")
        self.assertEqual(result, "aGVsbG8=")

    # This test checks that a Base64 value is turned back into normal text.
    def test_decode_base64(self):
        result = decode_base64("aGVsbG8=")
        self.assertEqual(result, "hello")
