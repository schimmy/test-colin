import requests
from django.db import models


class Inspections(models.Model):
  title = models.CharField(max_length=250)
  inspectorName = models.CharField(max_length=100)
  itemsOk = models.IntegerField()
  issuesWarningCount = models.IntegerField()
  issuesCriticalCount = models.IntegerField()
  company = models.CharField(max_length=100)

  def __repr__(self):
    return f"{self.title}: company: {self.company}, inspector: {self.inspectorName}"


def get_fakesolar_data():
  # TODO put in settings or similar
  BASE_URL = "https://6244305b3da3ac772b0c7854.mockapi.io/fakeSolar/3rdParty/"
  inspections_url = BASE_URL + "inspections"
  inspectors_url = BASE_URL + "inspectors"
  try:
    r = requests.get(inspections_url)
    if r.status_code != 200:
      raise Exception("error retrieving inspections")
    inspections = r.json()
  except requests.exceptions.RequestException as e:
    # TODO
    raise e

  try:
    r = requests.get(inspectors_url)
    if r.status_code != 200:
      raise Exception("error retrieving inspectors")
    inspectors = r.json()
  except requests.exceptions.RequestException as e:
    # TODO
    raise e

  valid_inspectors = set()
  for insp in inspectors:
    if "SolarGrade" in insp["availableIntegrations"]:
      valid_inspectors.add(insp['id'])

  out_inspections = []
  for inspect in inspections:
    if str(inspect["inspectorId"]) in valid_inspectors:
      out_inspections.append(inspect)

  return {'data': out_inspections}


def get_inspections(company=''):
  print(f"getting company: {company}")
  # grab from FakeSolar API if requested
  if company.lower() == 'fakesolar':
    return get_fakesolar_data()

  # else get from DB
  # probably want to filter in the future
  return list(Inspections.objects.order_by('title').values())
