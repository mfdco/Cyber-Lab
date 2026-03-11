from django.shortcuts import render

from .utils import decode_base64, encode_base64


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
