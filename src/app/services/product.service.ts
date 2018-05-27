import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';

import { Shirt } from '../models/shirt';
import { Form } from '../models/form';
import { Question } from '../models/question';

@Injectable()
export class ProductService {
  private url = 'http://127.0.0.1:8000/api/';  // URL to web api
  shirt: Shirt;
  event: Event;
  form: Form;

  constructor(private http: HttpClient) { }

  getProduct(id: number) {
    const url = `${this.url}product/${id}`;
    return this.http.get<Shirt>(url);
  }

  getCatalogCatagory(id: number): Observable<Shirt[]> {
    const url = `${this.url}cc/${id}`;
    return this.http.get<Shirt[]>(url);
  }

  getProductEvents(id: number): Observable<Event[]> {
    const url = `${this.url}product/${id}/events`;
    return this.http.get<Event[]>(url);
  }

  getEventForms(id: number): Observable<Form[]> {
    const url = `${this.url}event/${id}`;
    return this.http.get<Form[]>(url);
  }

  getFormQuestions(id: number): Observable<Question[]> {
    const url = `${this.url}form/${id}`;
    return this.http.get<Question []>(url);
  }

  addQuestion(id: number, value: string): Observable<Question>{
    const url = `${this.url}form/${id}`;
    return this.http.post<Question>(url, value);
  }
}
