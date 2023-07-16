import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { User } from './user';
import { newUser } from './newuser';



//TODO: a CHEQUEAR Y CORREGIR


@Injectable({
  providedIn: 'root'
})
export class RegisterService {
   url = 'http://localhost/3000/user'
  constructor(private http: HttpClient) { }

  register(credentials: newUser): Observable<any> {
    return this.http.post(this.url, credentials)
  }
}
