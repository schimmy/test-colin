import requests

from datetime import datetime
from django.db import models
from django.conf import settings


class Inspections(models.Model):
  title = models.CharField(max_length=250)
  inspectorName = models.CharField(max_length=100)
  itemsOk = models.IntegerField()
  issuesWarningCount = models.IntegerField()
  issuesCriticalCount = models.IntegerField()
  company = models.CharField(max_length=100)

  def __repr__(self):
    return f"{self.title}: company: {self.company}, inspector: {self.inspectorName}"


# I'm going to assume that:
# - these inspections can be scheduled ahead of time, and that info is not relevant
# - createdAt could be the next day, perhaps they enter the data the next working day
# - the items for each inspection are all going to be assigned the 'createdAt' time
def convert_fakesolar(inspections):
  out_inspections = []
  for i in inspections:
    i_date : datetime = datetime.strptime(i['createdAt'], '%Y-%m-%dT%H:%M:%S.%fZ')
    issues = i['items']
    num_ok = sum([1 for x in issues if not x['isIssue']])
    num_warnings = sum([1 for x in issues if (x['isIssue'] and x['severity'] < 60)])
    num_critical = sum([1 for x in issues if (x['isIssue'] and x['severity'] >= 60)])
    insp = {
      'title': f"{i['city']} - {datetime.strftime(i_date, '%Y/%m/%d')}",
      'inspectorName': i['inspectorName'],
      'company': 'FakeSolar',
      'itemsOk': num_ok,
      'issuesWarningCount': num_warnings,
      'issuesCriticalCount': num_critical,
    }
    out_inspections.append(insp)
  return out_inspections


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

  valid_inspectors = {}
  for insp in inspectors:
    if "SolarGrade" in insp["availableIntegrations"]:
      valid_inspectors[insp['id']] = insp['name']

  out_inspections = []
  for inspect in inspections:
    inspector_id = str(inspect["inspectorId"])
    if inspector_id in valid_inspectors:
      # add in the inspector name for convenience later
      out_inspections.append(inspect | {'inspectorName': valid_inspectors[inspector_id]})

  converted_inspections = convert_fakesolar(out_inspections)
  return {'data': converted_inspections}


def get_inspections(company=''):
  print(f"getting company: {company}")
  # grab from FakeSolar API if requested
  if company.lower() == 'fakesolar':
    return get_fakesolar_data()

  # else get from DB
  # probably want to filter in the future
  return list(Inspections.objects.order_by('title').values())
