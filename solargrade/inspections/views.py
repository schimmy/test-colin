from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from inspections.models import get_inspections


def get_fakesolar_data():
  response = {'data': [{'title': 'test'}]}
  return response


def get_inspections_from_db(company=''):
  # splitting out based on company should be handled at the model layer
  # views should not care whether the FakeSolar data is accessed via API
  # or whether that data is in the DB
  response = get_inspections(company)
  print(f"got inspections: {response}")
  return response


# API endpoint for Angular
def inspections(request):
  data = get_inspections_from_db(company=request.GET.get('company', ''))
  return JsonResponse(data, safe=False)


def index(request):
  data = get_inspections_from_db(company='FakeSolar')
  return render(request, 'index.html', data)
