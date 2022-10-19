import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { IssueBoxComponent } from './issue-box/issue-box.component'
import { InspectionTableComponent } from './inspection-table/inspection-table.component'
import { Inspection } from './inspection'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit {
  title = 'SolarGrade - Colin';
  inspectionsInput: Inspection[] = [];
  // TODO: probably make this less FakeSolar-specific, allow for other companies
  api_url = '/inspections?company=FakeSolar'
  error = ''

  // TODO put this into a test
  numInspectionsWarning = 0;
  numIssuesWarning = 0;
  numInspectionsCritical = 0;
  numIssuesCritical = 0;

  fetch_inspections_from_api() {
    this.http.get<any>(this.api_url).subscribe({
      next: data => {
        this.inspectionsInput = data['data'] as Inspection[];
        this.recalculateIssueBoxes()
      },
      error: error => {
        console.error("error: ", error.message)
        this.error = "Error retrieving data: " + error.message
      }
    })
  }

  recalculateIssueBoxes() {
    for (var insp of this.inspectionsInput) {
      var warns = insp['issuesWarningCount'];
      var crits = insp['issuesCriticalCount'];
      if (warns > 0) {
        this.numInspectionsWarning += 1
        this.numIssuesWarning += warns
      }
      if (crits > 0) {
        this.numInspectionsCritical += 1;
        this.numIssuesCritical += crits;
      }
    }
  }

  constructor(private http: HttpClient) {
    this.fetch_inspections_from_api()
  }

  ngOnInit(): void {
  }
}
