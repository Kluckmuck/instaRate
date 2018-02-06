import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ShirtComponent } from './shirt/shirt.component';

const routes: Routes = [
  { path: '', redirectTo: '/', pathMatch: 'full' },
  { path: 'shirts', component: ShirtComponent },
];

@NgModule({
  exports: [ RouterModule ],
  imports: [ RouterModule.forRoot(routes) ],
})
export class AppRoutingModule {
 }
