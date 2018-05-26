import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, ParamMap } from '@angular/router';
import { Location } from '@angular/common';

import { Form } from '../models/form';
import { ProductService } from '../services/product.service';

@Component({
  selector: 'app-event',
  templateUrl: './event.component.html',
  styleUrls: ['./event.component.css']
})
export class EventComponent implements OnInit {

  forms: Form[];

  constructor(
    private route: ActivatedRoute,
    private productService: ProductService,
    private location: Location
  ) { }

  ngOnInit() {
    this.getEventForms();
  }

  getEventForms(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.productService.getEventForms(id)
      // clone the data object, using its known Config shape
      .subscribe(data => {
      this.forms = data as Form[];
    });
  }

}
