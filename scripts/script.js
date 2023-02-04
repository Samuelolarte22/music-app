const formulario = document.getElementById("formulario");
const boton = document.getElementById("boton");
const texto = document.getElementById("texto");
const resultado = document.getElementById("resultado");

function agregarGuion(frase) {
  return frase.split(" ").join(" - ");
}

formulario.addEventListener("submit", (event) => {
  event.preventDefault();
  resultado.innerHTML = agregarGuion(texto.value);
});