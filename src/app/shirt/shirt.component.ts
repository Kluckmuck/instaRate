import { Component, OnInit } from '@angular/core';
import { Shirt } from '../models/shirt';

@Component({
  selector: 'app-shirt',
  templateUrl: './shirt.component.html',
  styleUrls: ['./shirt.component.css']
})
export class ShirtComponent implements OnInit {

  picText = 'T-shirt';
  shirt: Shirt =  {
    id: 1,
    name: 'T-Shirt',
    img: 'https://tshirtstore.centracdn.net/client/dynamic/images/4116_16576eeaed-tove.jpg'
  };

  constructor() { }

  ngOnInit() {
  }

}