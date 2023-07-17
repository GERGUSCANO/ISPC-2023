import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { User } from './user';
import { newUser } from './newuser';


<<<<<<< HEAD

//TODO: a CHEQUEAR Y CORREGIR


=======
>>>>>>> 42767b70af306b12630d3e789717f11440c32a56
@Injectable({
  providedIn: 'root'
})
export class RegisterService {
<<<<<<< HEAD
   url = 'http://localhost/3000/user'
  constructor(private http: HttpClient) { }

  register(credentials: newUser): Observable<any> {
    return this.http.post(this.url, credentials)
=======

  constructor(private http: HttpClient) { }

  register(credentials: newUser): Observable<any> {
    return this.http.post('../../../assets/newUser.json', credentials)
>>>>>>> 42767b70af306b12630d3e789717f11440c32a56
  }
}
