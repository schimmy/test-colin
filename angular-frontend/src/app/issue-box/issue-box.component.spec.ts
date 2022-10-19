import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CriticalBoxComponent } from './critical-box.component';

describe('CriticalBoxComponent', () => {
  let component: CriticalBoxComponent;
  let fixture: ComponentFixture<CriticalBoxComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CriticalBoxComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CriticalBoxComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
