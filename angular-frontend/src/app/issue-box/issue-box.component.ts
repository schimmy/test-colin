import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-issue-box',
  template: `
		<div class={{severityType}}>
			<p>{{numInspectionsAffected}} inspection(s) in {{severityType}} state</p>
			<p class='big-warn'>{{numIssues}} {{severityType}} issues</p>
		</div>
  `,
  styleUrls: []
})


export class IssueBoxComponent implements OnInit {

  constructor() {
    this.severityType = 'n/a'; // should be overwritten anyways, 'critical' or 'warning'
    this.numIssues = 0;
    this.numInspectionsAffected = 0;
  }

  @Input() severityType: string;
  @Input() numIssues: number;
  @Input() numInspectionsAffected: number;

  ngOnInit(): void {
  }

}
