import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { newUser } from 'src/app/services/auth/newuser';
import { RegisterService } from 'src/app/services/auth/register.service';



@Component({
  selector: 'app-form-registro',
  templateUrl: './form-registro.component.html',
  styleUrls: ['./form-registro.component.css']
})
export class FormRegistroComponent {

  regForm = this.fB.group({
    name: ['', [Validators.required]],
    email: ['', [Validators.required, Validators.email]],
    password: ['', [Validators.required, Validators.min(8)]]
  })

  constructor(private fB: FormBuilder, private router: Router, private registerService: RegisterService){

  }

//de esta forma controlaremos los datos ingresados en el registro utilizando lo especicado arriba dentro de regForm

  get name(){
    return this.regForm.controls.name;
  }
  get email() {
    return this.regForm.controls.email;
  }
  get password() {
    return this.regForm.controls.password;
  }


  newRegister() {
    //!primero verificamos si los datos de entrada son validos
    if (this.regForm.valid) {
      //!llamamos al servicio y pasamos los valores ingresados por el usuario como un tipo
      //!loginRequest (interface en service/auth)
      this.registerService.register(this.regForm.value as newUser).subscribe({
        next: (userData: newUser) => {
          console.log(userData)
        },
        error: (errorData: any) => {
          console.log(errorData)
        },
        complete: () => {
          //!ejecutamos la redireccion y el reseteo del loguin solo si se completa
          //!si handleError (del servicio) capta un error se permanecera en el login
          console.log("Register Done!")
          this.router.navigateByUrl('/form-login')
          this.regForm.reset();
        }
      }) //enviamos el valor del objeto loguinForm como un loguinRequest (interface creada)

    } else {
      this.regForm.markAllAsTouched();

    }

  }



}
