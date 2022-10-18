from django.test import TestCase
from .models import convert_fakesolar


class ConvertFakeSolarTestCase(TestCase):
  def test_convert_fakesolar(self):
    input_list = [
      {
        "createdAt": "2021-07-07T04:32:28.478Z",
        "city": "New Clemenschester",
        "scheduledDate": "2021-10-09T04:58:13.787Z",
        "inspectorId": 7,
        "inspectorName": "name7",
        "id": "1",
        "items": [
          {
            "createdAt": "2022-04-20T10:48:49.067Z",
            "isIssue": True,
            "severity": 99,
            "label": "voluptas dolore sed",
            "id": "51",
            "inspectionId": "1"
          }
        ]
      },
      {
        "createdAt": "2021-07-30T03:12:31.495Z",
        "city": "Lake Stone",
        "scheduledDate": "2022-02-17T12:43:50.328Z",
        "inspectorId": 42,
        "inspectorName": "name42",
        "id": "2",
        "items": [
          {
            "createdAt": "2022-04-20T17:16:51.011Z",
            "isIssue": True,
            "severity": 10,
            "label": "veniam exercitationem consequuntur",
            "id": "52",
            "inspectionId": "2"
          },
          {
            "createdAt": "2022-04-20T17:16:51.011Z",
            "isIssue": False,
            "severity": 92,
            "label": "false 92 consequuntur",
            "id": "53",
            "inspectionId": "2"
          },
        ]
      },
      {
        "createdAt": "2022-02-21T13:52:31.059Z",
        "city": "West Loycefurt",
        "scheduledDate": "2021-05-05T01:32:29.471Z",
        "inspectorId": 54,
        "inspectorName": "name54",
        "id": "8",
        "items": []
      },
    ]

    out_inspections = convert_fakesolar(input_list)
    self.assertEqual(len(out_inspections), 3)
    new_clemen_output = {
      'title': 'New Clemenschester - 2021/07/07',
      'company': 'FakeSolar',
      'inspectorName': 'name7',
      'itemsOk': 0,
      'issuesWarningCount': 0,
      'issuesCriticalCount': 1,
    }
    self.assertDictEqual(out_inspections[0], new_clemen_output)

    lake_stone_output = {
      'title': 'Lake Stone - 2021/07/30',
      'company': 'FakeSolar',
      'inspectorName': 'name42',
      'itemsOk': 1,
      'issuesWarningCount': 1,
      'issuesCriticalCount': 0,
    }
    self.assertDictEqual(out_inspections[1], lake_stone_output)

    west_loyce_output = {
      'title': 'West Loycefurt - 2022/02/21',
      'company': 'FakeSolar',
      'inspectorName': 'name54',
      'itemsOk': 0,
      'issuesWarningCount': 0,
      'issuesCriticalCount': 0,
    }
    self.assertDictEqual(out_inspections[2], west_loyce_output)
