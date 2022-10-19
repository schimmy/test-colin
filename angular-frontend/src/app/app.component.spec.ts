import { NO_ERRORS_SCHEMA } from '@angular/core'
import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { AppComponent } from './app.component';
import { INSPECTIONS } from './mock-inspections'

describe('AppComponent', () => {
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [HttpClientTestingModule],
      declarations: [
        AppComponent
      ],
      schemas: [NO_ERRORS_SCHEMA]
    }).compileComponents();
  });

  it('should create the app', () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.componentInstance;
    expect(app).toBeTruthy();
  });

  it(`should have as title 'SolarGrade - Colin'`, () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.componentInstance;
    expect(app.title).toEqual('SolarGrade - Colin');
  });

  it(`should set the proper numbers of issues per box`, () => {
    const fixture = TestBed.createComponent(AppComponent);
    const app = fixture.componentInstance;
    app.inspectionsInput = INSPECTIONS;
    app.recalculateIssueBoxes();
    expect(app.numIssuesWarning).toEqual(2);
    expect(app.numInspectionsWarning).toEqual(1);
    expect(app.numIssuesCritical).toEqual(5);
    expect(app.numInspectionsCritical).toEqual(3);
  });
});
