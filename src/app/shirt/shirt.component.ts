import { Component, OnInit } from '@angular/core';

import { Shirt } from '../models/shirt';
import { ProductService } from '../services/product.service';

@Component({
  selector: 'app-shirt',
  templateUrl: './shirt.component.html',
  styleUrls: ['./shirt.component.css']
})
export class ShirtComponent implements OnInit {

  picText = 'T-shirt';
  catalogCatagoryID = 2;
  shirts: Shirt[];


  constructor(
    private productService: ProductService
  ) { }

  ngOnInit() {
    this.getCatalogCatagory(this.catalogCatagoryID);
  }

  getCatalogCatagory(id: number) {
    this.productService.getCatalogCatagory(id)
      // clone the data object, using its known Config shape
      .subscribe(data => {
      this.shirts = data as Shirt[];
    });
  }

}
