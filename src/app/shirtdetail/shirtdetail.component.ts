import { Component, OnInit } from '@angular/core';

import { Shirt } from '../models/shirt';

@Component({
  selector: 'app-shirtdetail',
  templateUrl: './shirtdetail.component.html',
  styleUrls: ['./shirtdetail.component.css']
})
export class ShirtDetailComponent implements OnInit {

  shirt: Shirt =  {
    id: 1,
    name: 'T-Shirt',
    img: 'https://tshirtstore.centracdn.net/client/dynamic/images/4116_16576eeaed-tove.jpg'
  };

  constructor() { }

  ngOnInit() {
  }

}
