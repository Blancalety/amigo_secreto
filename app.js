// El principal objetivo de este desafío es fortalecer tus habilidades en lógica de programación. Aquí deberás desarrollar la lógica para resolver el problema.
// Array de amigos
let amigos = [];

// Función para actualizar la lista en el HTML
function actualizarLista() {
    const lista = document.getElementById("listaAmigos"); // Obtener la lista
    lista.innerHTML = ""; // Limpiar la lista antes de agregar nuevos elementos

    for (let amigo of amigos) {
        const li = document.createElement("li"); // Crear un nuevo elemento 
        li.textContent = amigo; // Asignar el nombre del amigo
        lista.appendChild(li); // Agregarlo a la lista
    }
}

// Función para agregar un amigo al array y actualizar la lista
function agregarAmigo() {
    const input = document.getElementById("amigo"); // Obtener el input
    const nombre = input.value.trim(); // Obtener el valor sin espacios extra

    if (nombre !== "") {
        amigos.push(nombre); // Agregar al array
        actualizarLista(); // Actualizar la lista en el HTML
        input.value = ""; // Limpiar el input
    } else {
        alert("Por favor, ingresa un nombre válido.");
    }
}

function sortearAmigo() {
    const resultado = document.getElementById("resultado"); // Obtener el elemento donde se mostrará el resultado

    // Validar que haya al menos un amigo en la lista
    if (amigos.length === 0) {
        resultado.innerHTML = "<li>No hay amigos para sortear.</li>";
        return;
    }

    // Generar un índice aleatorio
    const indiceAleatorio = Math.floor(Math.random() * amigos.length);

    // Obtener el nombre sorteado
    const amigoSorteado = amigos[indiceAleatorio];

    // Resultado en la lista de resultados
    resultado.innerHTML = `<li>${amigoSorteado} es el amigo secreto 🎉</li>`;
}