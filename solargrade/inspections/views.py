from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from inspections.models import get_inspections


def inspections(request):
  """API endpoint for Angular that gets data from the model layer.

  Splitting out based on company should be handled at the model layer
  views should not care whether the FakeSolar data is accessed via API
  or whether that data is in the DB
  """
  data = get_inspections(company=request.GET.get('company', ''))
  return JsonResponse(data, safe=False)


def index(request):
  """Homepage that we don't use, but was useful for testing"""
  data = get_inspections(company='FakeSolar')
  return render(request, 'index.html', data)
