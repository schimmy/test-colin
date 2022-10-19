import { Component, OnInit, Input } from '@angular/core';
import { Inspection } from '../inspection'

@Component({
  selector: 'app-inspection-table',
  templateUrl: './inspection-table.component.html',
  styleUrls: []
})
export class InspectionTableComponent implements OnInit {

  constructor() {
    this.inspections = [];
  }

  @Input() inspections: Inspection[];

  ngOnInit(): void {
  }

}
