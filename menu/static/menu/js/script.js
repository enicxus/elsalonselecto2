//boton de registro del html con el id signUp
const signUpButton = document.getElementById('signUp');
//boton de inicio de sesion del html con el id signUp
const signInButton = document.getElementById('signIn');
//contendor del html con el id container
const container = document.getElementById('container');

//añade una reaccion al boton de registro
signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});
//añade una reaccion al boton de incio de sesion
signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});