import { Component, OnInit } from '@angular/core';
import { IssueBoxComponent } from './issue-box/issue-box.component'
import { InspectionTableComponent } from './inspection-table/inspection-table.component'
import { Inspection } from './inspection'
import { INSPECTIONS } from './mock-inspections'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit {
  title = 'SolarGrade - Colin';
  inspectionsInput: Inspection[] = INSPECTIONS;

  // TODO put this into a test
  numInspectionsCritical = 0;
  numIssuesCritical = 0;



  constructor() {
    // TODO: add in getter from API backend

    for (var insp of this.inspectionsInput) {
      var warns = insp['issuesWarningCount'];
      var crits = insp['issuesCriticalCount'];
      if (crits > 0) {
        this.numInspectionsCritical += 1;
        this.numIssuesCritical += crits;
      }
      //if (warns > 0) {
      //  numInspectionsWarning += 1
      //  numIssuesWarning += crits
      //}
    }
  }

  ngOnInit(): void {
  }
}
