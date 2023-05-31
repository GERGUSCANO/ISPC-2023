import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FormRecuperarComponent } from './form-recuperar.component';

describe('FormRecuperarComponent', () => {
  let component: FormRecuperarComponent;
  let fixture: ComponentFixture<FormRecuperarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FormRecuperarComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FormRecuperarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
