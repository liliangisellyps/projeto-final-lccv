import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './modules/belogings/components/home/home.component';
import { RegisterComponent } from './modules/belogings/components/register/register.component';
import { ListComponent } from './modules/belogings/components/list/list.component';

const routes: Routes = [
  { path: 'bens', component: HomeComponent },
  { path: 'cadastrar', component: RegisterComponent },
  { path: 'listar', component: ListComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
