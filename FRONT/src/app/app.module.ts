import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MainPageComponent } from './pages/main-page/main-page.component';
import { FormRegistroComponent } from './pages/form-registro/form-registro.component';
import { FormRecuperarComponent } from './pages/form-recuperar/form-recuperar.component';
import { NavbarComponent } from './layout/navbar/navbar.component';
import { NotfoundComponent } from './pages/notfound/notfound.component';
import { FormLoginComponent } from './pages/form-login/form-login.component';
import { FooterComponent } from './layout/footer/footer.component';
import { AboutusComponent } from './pages/aboutus/aboutus.component';
import { ProductsComponent } from './pages/products/products.component';

@NgModule({
  declarations: [
    AppComponent,
    MainPageComponent,
    FormRegistroComponent,
    FormRecuperarComponent,
    NavbarComponent,
    NotfoundComponent,
    FormLoginComponent,
    FooterComponent,
    AboutusComponent,
    ProductsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
