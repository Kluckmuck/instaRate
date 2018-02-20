import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ShirtComponent } from './shirt/shirt.component';
import { ShirtDetailComponent } from './shirtdetail/shirtdetail.component';
import { CheckoutComponent } from './checkout/checkout.component';
import { TermsComponent } from './terms/terms.component';
import { FirstPageComponent } from './firstpage/firstpage.component';

const routes: Routes = [
  { path: '', redirectTo: '/', pathMatch: 'full' },
  { path: 'shirts', component: ShirtComponent },
  { path: 'item/:id', component: ShirtDetailComponent },
  { path: 'checkout', component: CheckoutComponent },
  { path: 'terms', component: TermsComponent },
  { path: '', component: FirstPageComponent }
];

@NgModule({
  exports: [ RouterModule ],
  imports: [ RouterModule.forRoot(routes) ],
})
export class AppRoutingModule {
 }
