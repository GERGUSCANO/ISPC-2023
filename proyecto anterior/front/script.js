let cad = `
<div id="card" class="card">
      <h1 class="title">Ingrese sus datos</h1>
      <form class="form" name="formulario" method="get">
          <p>Usuario</p>
          <input type="text" name="usuario" id="usuario" placeholder="Ingrese su usuario">
          <p>Contraseña</p>
          <input type="text" name="contraseña" id="contraseña" placeholder="Ingrese su contraseña" maxlength="6">
          <br><br>
          <input type="submit" class="button" id="btn" name="btn" value="Ingresar">
          <a href="../FRONTEND/form_registro.html"><p>¿Ya está registrado?</p></a>
          <a href="../FRONTEND/recuperacion.html"><p>¿Olvidó su contraseña?</p></a>
        </form>
</div>
`

document.getElementById("idform").innerHTML = cad;

(function(){
    var formulario = document.getElementsByName('formulario')[0],
        boton = document.getElementById('btn');

    var validarUsuario = function(e){
        if (formulario.usuario.value == 0){
            alert("Completa el campo usuario");
            e.preventDefault();
        }
    };

    var validarContraseña = function(e){
        if (formulario.contraseña.value == 0){
            alert("Completa el campo contraseña");
            e.preventDefault();
        }
    };

    var validar = function(e){
        validarUsuario(e);
        validarContraseña(e);
    };
    formulario.addEventListener("submit", validar);
}())
