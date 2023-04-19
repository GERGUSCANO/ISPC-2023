var name = document.getElementById('name');
var email = document.getElementById('email');
var password = document.getElementById('password');
var rePassW = document.getElementById('recuperar');


error.style.color='red';

function enviarForm (){
    console.log("Formulario enviado");
    var mensajeError = [];

    if (nam.value === null || nam.value === ''){
        mensajeError.push('Ingresa tu nombre');
    }
    if (email.value === null || email.value === ''){
        mensajeError.push('Ingresa tu email');
    }
    if (password.value === null || password.value === ''){
        mensajeError.push('Ingresa tu contraseña');
    }
    if (rePassW.value === null || rePassW.value === ''){
        mensajeError.push('Repita la contraseña');
    }
    if (password.value != rePassW.value){
        mensajeError.push('Las contraseñas no soy iguales, ingrese nuevamente')
    }
    
    error.innerHTML = mensajeError.join(', ')
    return false;
}
