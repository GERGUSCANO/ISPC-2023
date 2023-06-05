import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { User } from './user';
import { newUser } from './newuser';


@Injectable({
  providedIn: 'root'
})
export class RegisterService {

  constructor(private http: HttpClient) { }

  register(credentials: newUser): Observable<any> {
    return this.http.post('../../../assets/newUser.json', credentials)
  }
}
