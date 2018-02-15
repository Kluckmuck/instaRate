import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Shirt } from '../models/shirt';

@Injectable()
export class ProductService {
  private url = 'http://127.0.0.1:8000/api/';  // URL to web api
  shirt: Shirt;

  constructor(private http: HttpClient) { }

  getProduct(id: number) {
    const url = `${this.url}product/${id}`;
    return this.http.get(url);
  }
}
