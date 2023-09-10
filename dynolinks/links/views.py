from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import DynamicLink
import random
import string

# In-memory dictionary to store dynamic links (for testing)
dynamic_links = {}


def create_dynamic_link(request):
    if request.method == "POST":
        original_url = request.POST.get("original_url")
        dynamic_path = ''.join(random.choices(
            string.ascii_lowercase + string.digits, k=8))

        # Store the dynamic link in the in-memory dictionary
        dynamic_links[dynamic_path] = original_url

        absolute_url = request.build_absolute_uri(f"/links/{dynamic_path}")

        return HttpResponse(f"Dynamic Link Created: {absolute_url}")
    return render(request, "create_link.html")


def resolve_dynamic_link(request, dynamic_path):
    original_url = dynamic_links.get(dynamic_path)
    if original_url:
        return HttpResponseRedirect(original_url)
    return HttpResponse("Dynamic link not found!", status=404)
