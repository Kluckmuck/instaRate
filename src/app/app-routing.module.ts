import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ShirtComponent } from './shirt/shirt.component';
import { ShirtDetailComponent } from './shirtdetail/shirtdetail.component';
import { CheckoutComponent } from './checkout/checkout.component';

const routes: Routes = [
  { path: '', redirectTo: '/', pathMatch: 'full' },
  { path: 'shirts', component: ShirtComponent },
  { path: 'item/:id', component: ShirtDetailComponent },
  { path: 'checkout', component: CheckoutComponent }
];

@NgModule({
  exports: [ RouterModule ],
  imports: [ RouterModule.forRoot(routes) ],
})
export class AppRoutingModule {
 }
