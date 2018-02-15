import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';

import { Shirt } from '../models/shirt';

@Injectable()
export class ProductService {
  private url = 'http://127.0.0.1:8000/api/';  // URL to web api
  shirt: Shirt;

  constructor(private http: HttpClient) { }

  getProduct(id: number) {
    const url = `${this.url}product/${id}`;
    return this.http.get<Shirt>(url);
  }

  getCatalogCatagory(id: number): Observable<Shirt[]> {
    const url = `${this.url}cc/${id}`;
    return this.http.get<Shirt[]>(url);
  }
}
