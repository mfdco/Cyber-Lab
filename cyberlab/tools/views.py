from django.http import JsonResponse
from django.shortcuts import render

from .utils import (
    decode_base64,
    decode_binary,
    decode_hex,
    decode_url,
    encode_base64,
    encode_binary,
    encode_hex,
    encode_url,
    rot13_text,
)


# This view takes user input, then either encodes or decodes it with Base64.
def base64_tool(request):
    result = ""

    if request.method == "POST":
        text = request.POST.get("text", "")
        action = request.POST.get("action", "")

        if action == "encode":
            result = encode_base64(text)
        elif action == "decode":
            result = decode_base64(text)

    return render(request, "tools/base64.html", {"result": result})


def binary_tool(request):
    result = ""

    if request.method == "POST":
        text = request.POST.get("text", "")
        action = request.POST.get("action", "")

        if action == "encode":
            result = encode_binary(text)
        elif action == "decode":
            try:
                result = decode_binary(text)
            except Exception:
                result = "Invalid binary input."

    return render(request, "tools/binary.html", {"result": result})


# This view handles Hex input and returns JSON so the frontend can wire it later.
def hex_tool(request):
    if request.method != "POST":
        return JsonResponse(
            {"message": "Send a POST request with text and action."},
            status=405,
        )

    text = request.POST.get("text", "")
    action = request.POST.get("action", "")

    try:
        if action == "encode":
            result = encode_hex(text)
        elif action == "decode":
            result = decode_hex(text)
        else:
            return JsonResponse({"error": "Invalid action."}, status=400)
    except Exception:
        return JsonResponse({"error": "Invalid hex input."}, status=400)

    return JsonResponse({"result": result})


# This view handles URL encoding and decoding and returns JSON results.
def url_tool(request):
    if request.method != "POST":
        return JsonResponse(
            {"message": "Send a POST request with text and action."},
            status=405,
        )

    text = request.POST.get("text", "")
    action = request.POST.get("action", "")

    if action == "encode":
        result = encode_url(text)
    elif action == "decode":
        result = decode_url(text)
    else:
        return JsonResponse({"error": "Invalid action."}, status=400)

    return JsonResponse({"result": result})


# This view handles ROT13 and returns JSON results for the frontend.
def rot13_tool(request):
    if request.method != "POST":
        return JsonResponse(
            {"message": "Send a POST request with text."},
            status=405,
        )

    text = request.POST.get("text", "")
    result = rot13_text(text)
    return JsonResponse({"result": result})
