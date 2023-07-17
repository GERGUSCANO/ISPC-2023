import { Injectable } from '@angular/core';
import { loguinRequest } from './loguinRequest';
import { Observable, catchError, throwError } from 'rxjs';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { User } from './user';

@Injectable({
  providedIn: 'root'
})
export class LoginformService {

  constructor( private http: HttpClient) {

  }

  login( credentials: loguinRequest ): Observable<User> {
<<<<<<< HEAD
    return this.http.get<User>('../../../assets/users.json').pipe(catchError(this.handleError))
  }

  //!vamos a utilizar un manejador de errores en funcion de las peticiones http
  //!muchas veces la respuesta de la bd/api puede contener errores. Por ello se utiliza catchError

  private handleError(error: HttpErrorResponse){ //creamos una instancia de HttpErrorResponse para acceder luego a sus propiedades
=======
    return this.http.get<User>('../../../asdsets/users.json').pipe(catchError(this.handleError))
  }

  //!vamo a utilizar un manejador de errores en funcion de las peticiones http
  //!muchas veces la respuesta de la bd/api puede contener errores. Por ello se utiliza catchError

  private handleError(error: HttpErrorResponse){
>>>>>>> 42767b70af306b12630d3e789717f11440c32a56
    //veremos si esta mal formulado el request o el problema esta en el back
    if(error.status == 0){
      console.log("Se ha producido un error" + error.error);
    }else{
<<<<<<< HEAD
      console.log("El backend retorno el codigo de estado", error.status, error.error); //.status .error son propiedades de HttpErrorResponse
=======
      console.log("El backend retorno el codigo de estado", error.status, error.error);
>>>>>>> 42767b70af306b12630d3e789717f11440c32a56
    }
    return throwError(()=> new Error('Algo fallo, por favor intente nuevamente'));
  }
}
