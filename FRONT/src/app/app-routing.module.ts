import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MainPageComponent } from './pages/main-page/main-page.component';
import { FormRegistroComponent } from './pages/form-registro/form-registro.component';
import { FormRecuperarComponent } from './pages/form-recuperar/form-recuperar.component';
import { NotfoundComponent } from './pages/notfound/notfound.component';
import { FormLoginComponent } from './pages/form-login/form-login.component';
import { AboutusComponent } from './pages/aboutus/aboutus.component';
import { ProductsComponent } from './pages/products/products.component';

//rutas de navegacion
const routes: Routes = [
  {path:'', redirectTo:'main-page', pathMatch:'full'},
  {path: 'main-page', component: MainPageComponent},
  {path: 'form-registro', component: FormRegistroComponent},
  {path: 'form-recuperar', component: FormRecuperarComponent},
  {path: 'form-login', component: FormLoginComponent},
  {path: 'aboutus', component: AboutusComponent},
  {path: 'products', component: ProductsComponent},
  {path: '**', component: NotfoundComponent}, //**es el comodin-> "cualquien ruta", poner a lo ultimo

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
