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
  out_inspections = []
  return {'data': out_inspections}


def get_inspections(company=''):
  print(f"getting company: {company}")
  # grab from FakeSolar API if requested
  if company.lower() == 'fakesolar':
    return get_fakesolar_data()

  # else get from DB
  # probably want to filter in the future
  return list(Inspections.objects.order_by('title').values())
