import { Inspection } from './inspection'

export const INSPECTIONS: Inspection[] = [
  {
    'title': "city1 - 2022/02/02",
    'inspectorName': 'inspectorName1', 'company': 'FakeSolar',
    'itemsOk': 1, 'issuesWarningCount': 2, 'issuesCriticalCount': 3
  },
  {
    'title': "city2 - 2022/02/03",
    'inspectorName': 'inspectorName3', 'company': 'FakeSolar',
    'itemsOk': 1, 'issuesWarningCount': 0, 'issuesCriticalCount': 1
  },
  {
    'title': "city3 - 2022/02/03",
    'inspectorName': 'inspectorName3', 'company': 'FakeSolar',
    'itemsOk': 0, 'issuesWarningCount': 0, 'issuesCriticalCount': 1
  },
]
