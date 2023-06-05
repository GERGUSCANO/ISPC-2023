import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { LoginformService } from 'src/app/services/auth/loginform.service';
import { loguinRequest } from 'src/app/services/auth/loguinRequest';

@Component({
  selector: 'app-form-login',
  templateUrl: './form-login.component.html',
  styleUrls: ['./form-login.component.css']
})
export class FormLoginComponent {
  //!aqui validamos los datos de entrada
  loginForm = this.fB.group({
    email: ['', [Validators.required, Validators.email]],
    password: ['', [Validators.required]]
  })

  loguinError: string='';



  constructor(private fB: FormBuilder, private router: Router, private loginService: LoginformService) {

  }

  get email() {
    return this.loginForm.controls.email;
  }
  get password() {
    return this.loginForm.controls.password;
  }




  login() {
    //!primero verificamos si los datos de entrada son validos
    if (this.loginForm.valid) {
      //!llamamos al servicio y pasamos los valores ingresados por el usuario como un tipo
      //!loginRequest (interface en service/auth)
      this.loginService.login(this.loginForm.value as loguinRequest).subscribe({
        next: (userData) => {
          console.log(userData)
        },
        error: (errorData) => {
          console.log(errorData)
          this.loguinError = errorData;
        },
        complete: () => {
          //!ejecutamos la redireccion y el reseteo del loguin solo si se completa
          //!si handleError (del servicio) capta un error se permanecera en el login
          console.log("Login Complete")
          this.router.navigateByUrl('/products')
          this.loginForm.reset();
        }
      }) //enviamos el valor del objeto loguinForm como un loguinRequest (interface creada)

    } else {
      this.loginForm.markAllAsTouched();

    }
  }



}
