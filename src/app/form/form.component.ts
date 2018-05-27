import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, ParamMap } from '@angular/router';
import { Location } from '@angular/common';

import { Question } from '../models/question';
import { ProductService } from '../services/product.service';

@Component({
  selector: 'app-form',
  templateUrl: './form.component.html',
  styleUrls: ['./form.component.css']
})
export class FormComponent implements OnInit {

  questions: Question[];
  formID: number;

  constructor(
    private route: ActivatedRoute,
    private productService: ProductService,
    private location: Location
  ) { }

  ngOnInit() {
    this.formID = +this.route.snapshot.paramMap.get('id');
    this.getFormQuestions(this.formID);
  }

  getFormQuestions(id: number): void {
    this.productService.getFormQuestions(id)
      // clone the data object, using its known Config shape
      .subscribe(data => {
      this.questions = data as Question[];
    });
  }

  addQuestion(value: string): void {
    this.productService.addQuestion(this.formID, value);
  }

  deleteQuestion(id: number): void {

  }
}
