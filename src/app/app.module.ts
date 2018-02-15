import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { HttpClientModule }    from '@angular/common/http';

import { AppComponent } from './app.component';
import { ShirtComponent } from './shirt/shirt.component';
import { AppRoutingModule } from './/app-routing.module';
import { ShirtDetailComponent } from './shirtdetail/shirtdetail.component';
import { CheckoutComponent } from './checkout/checkout.component';
import { TermsComponent } from './terms/terms.component';
import { ProductService } from './services/product.service';


@NgModule({
  declarations: [
    AppComponent,
    ShirtComponent,
    ShirtDetailComponent,
    CheckoutComponent,
    TermsComponent,
  ],
  imports: [
    NgbModule.forRoot(),
    BrowserModule,
    HttpClientModule,
    AppRoutingModule
  ],
  providers: [ProductService],
  bootstrap: [AppComponent]
})
export class AppModule { }
