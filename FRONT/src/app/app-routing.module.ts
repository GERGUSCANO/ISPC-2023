import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MainPageComponent } from './main-page/main-page.component';
import { FormRegistroComponent } from './form-registro/form-registro.component';
import { FormRecuperarComponent } from './form-recuperar/form-recuperar.component';
import { NotfoundComponent } from './notfound/notfound.component';
import { FormLoginComponent } from './form-login/form-login.component';

//rutas de navegacion
const routes: Routes = [
  {path:'', redirectTo:'main-page', pathMatch:'full'},
  {path: 'main-page', component: MainPageComponent},
  {path: 'form-registro', component: FormRegistroComponent},
  {path: 'form-recuperar', component: FormRecuperarComponent},
  {path: 'form-login', component: FormLoginComponent},
  {path: '**', component: NotfoundComponent}, //**es el comodin-> "cualquien ruta", poner a lo ultimo

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
