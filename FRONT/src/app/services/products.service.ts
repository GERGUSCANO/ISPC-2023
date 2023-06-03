import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'; //!httpclient es un servicio
import { Observable } from 'rxjs';  //solo los componentes suscriptos a este servicio podran acceder

@Injectable({
  providedIn: 'root'
})
export class ProductsService {

  url: string = "http://localhost:3000/"  //esta ruta corresponderia al json

  constructor(private http:HttpClient) { } //!las dependencias siempre se inyecta siempre en el contructor

  getProductInfo(): Observable <any>
  {
    return this.http.get(this.url + "productos");
  }
}
