import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {NgbModule} from '@ng-bootstrap/ng-bootstrap';

import { AppComponent } from './app.component';
import { ShirtComponent } from './shirt/shirt.component';
import { AppRoutingModule } from './/app-routing.module';
import { ShirtDetailComponent } from './shirtdetail/shirtdetail.component';
import { CheckoutComponent } from './checkout/checkout.component';


@NgModule({
  declarations: [
    AppComponent,
    ShirtComponent,
    ShirtDetailComponent,
    CheckoutComponent,
  ],
  imports: [
    NgbModule.forRoot(),
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
