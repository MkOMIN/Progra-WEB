const rayoRegistro = [];

document.querySelector("#rayoregistro").addEventListener('submit', (e) => {
    e.preventDefault();
    let email = document.querySelector("#inputEmail").value;
    let email2 = document.querySelector("#inputEmail2").value;
    let nombre = document.querySelector("#nombre-txt").value;
    let edad = document.querySelector("#edad-int").value;
    let direccion = document.querySelector("#direccion-txt").value;
    let contrasena = document.querySelector("#inputPassword").value;
    let contrasena2 = document.querySelector("#inputPassword2").value;
    let siValido = true;

    document.querySelector("#inputEmail").classList.remove("is-invalid");
    document.querySelector("#inputEmail2").classList.remove("is-invalid");
    document.querySelector("#nombre-txt").classList.remove("is-invalid");
    document.querySelector("#edad-int").classList.remove("is-invalid");
    document.querySelector("#direccion-txt").classList.remove("is-invalid");
    document.querySelector("#inputPassword").classList.remove("is-invalid");
    document.querySelector("#inputPassword2").classList.remove("is-invalid");

    
    if (email.trim() == "") {
        document.querySelector("#inputEmail").classList.add("is-invalid");
        siValido = false;
    }
    if (email2.trim() == "") {
        document.querySelector("#inputEmail2").classList.add("is-invalid");
        siValido = false;
    }
    if (nombre.trim() == "") {
        document.querySelector("#nombre-txt").classList.add("is-invalid");
        siValido = false;
    }
    if (edad.trim() == "") {
        document.querySelector("#edad-int").classList.add("is-invalid");
        siValido = false;
    }
    if (direccion.trim() == "") {
        document.querySelector("#direccion-txt").classList.add("is-invalid");
        siValido = false;
    }
    if (contrasena.trim() == "") {
        document.querySelector("#inputPassword").classList.add("is-invalid");
        siValido = false;
    }
    if (contrasena2.trim() == "") {
        document.querySelector("#inputPassword2").classList.add("is-invalid");
        siValido = false;
    }
    if (siValido) {

        let rayoM = {};
        rayoM.email = email;
        rayoM.email2 = email2;
        rayoM.nombre = nombre;
        rayoM.edad = edad;
        rayoM.direccion = direccion;
        rayoM.contrasena = contrasena;
        rayoM.contrasena2 = contrasena2;

        rayoRegistro.push(rayoM);

        Swal.fire("Registro Confirmado", "Usuario Registrado", "info");

    }
    document.querySelector("#inputEmail").value = "";
    document.querySelector("#inputEmail2").value = "";
    document.querySelector("#nombre-txt").value = "";
    document.querySelector("#edad-int").value = "";
    document.querySelector("#direccion-txt").value = "";
    document.querySelector("#inputPassword").value = "";
    document.querySelector("#inputPassword2").value = "";


    console.log(rayoRegistro);
});

const rayoLogin = [];
document.querySelector("#rayologin").addEventListener('submit', (e) => {
    e.preventDefault();
    let email = document.querySelector("#inputEmail").value;
    let contrasena = document.querySelector("#inputPassword").value;
    let siValido = true;

    document.querySelector("#inputEmail").classList.remove("is-invalid");
    document.querySelector("#inputPassword").classList.remove("is-invalid");

    if (email.trim() == "") {
        document.querySelector("#inputEmail").classList.add("is-invalid");
        siValido = false;
    }
    if (contrasena.trim() == "") {
        document.querySelector("#inputPassword").classList.add("is-invalid");
        siValido = false;
    }

    if (siValido) {

        let rayoM = {};
        rayoM.email = email;
        rayoM.contrasena = contrasena;
        
        rayoLogin.push(rayoM);
        Swal.fire("Login Confirmado", "Usuario Registrado", "info");
    }
    document.querySelector("#inputEmail").value = "";
    document.querySelector("#inputPassword").value = "";
});