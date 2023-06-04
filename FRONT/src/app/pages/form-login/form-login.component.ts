import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-form-login',
  templateUrl: './form-login.component.html',
  styleUrls: ['./form-login.component.css']
})
export class FormLoginComponent {
    loginForm = this.fB.group({
      email: ['',[Validators.required, Validators.email]],
      password: ['', [Validators.required]]
    })



   constructor(private fB: FormBuilder, private router: Router){

   }

   get email(){
    return this.loginForm.controls.email;
   }
   get password(){
    return this.loginForm.controls.password;
   }




   login(){
    if(this.loginForm.valid){
      console.log("llamar al servicio de logueo");
      this.router.navigateByUrl('/products')
      this.loginForm.reset();
    }else{
      this.loginForm.markAllAsTouched();

    }
   }



}
