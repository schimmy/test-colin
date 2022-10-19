import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InspectionTableComponent } from './inspection-table.component';

describe('InspectionTableComponent', () => {
  let component: InspectionTableComponent;
  let fixture: ComponentFixture<InspectionTableComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ InspectionTableComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(InspectionTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
