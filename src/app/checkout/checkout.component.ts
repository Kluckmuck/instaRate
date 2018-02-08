import { Component } from '@angular/core';

import { Shirt } from '../models/shirt';

@Component({
  selector: 'app-checkout',
  templateUrl: './checkout.component.html',
  styleUrls: ['./checkout.component.css']
})
export class CheckoutComponent {

  SHIRTS = [
    { id:1, name:'T-Shirt' , img:'www.google.se'},
    { id:2, name:'T-SNOOK' , img:'www.google.se'},
    { id:3, name:'T-Blaze' , img:'www.google.se'},
    { id:4, name:'T-Sleeve' , img:'www.google.se'}
  ];


  constructor() { }

}
