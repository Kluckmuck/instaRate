import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ShirtdetailComponent } from './shirtdetail.component';

describe('ShirtdetailComponent', () => {
  let component: ShirtdetailComponent;
  let fixture: ComponentFixture<ShirtdetailComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ShirtdetailComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ShirtdetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
