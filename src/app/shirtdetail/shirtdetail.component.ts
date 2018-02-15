import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, ParamMap } from '@angular/router';
import { Location } from '@angular/common';

import { Shirt } from '../models/shirt';
import { ProductService } from '../services/product.service';

import 'rxjs/add/operator/switchMap';

@Component({
  selector: 'app-shirtdetail',
  templateUrl: './shirtdetail.component.html',
  styleUrls: ['./shirtdetail.component.css']
})
export class ShirtDetailComponent implements OnInit {

  shirt: Shirt;

  constructor(
    private route: ActivatedRoute,
    private productService: ProductService,
    private location: Location
  ) { }

  ngOnInit() {
    this.getShirt();
  }

  getShirt(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.productService.getProduct(id)
    .subscribe(data => this.shirt = { ...data });
  }

}
