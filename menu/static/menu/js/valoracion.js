//Selcciona los elementos de valoracion tipo radio y los guarda en la variable ratingInputs.
const ratingInputs = document.querySelectorAll('input[type="radio"]');
//Selecciona todos los elementos cuyo id comienza en " average-rating" y los guarda en  averageRatingElements.
const averageRatingElements = document.querySelectorAll('[id^="average-rating"]');
//Obtiene el elemento con id "final-rating" y lo guarda en finalRatingElement.
const finalRatingElement = document.getElementById('final-rating');
//Determina la cantidad de productos que va a valorar 
const productCount = 4;

//aqui se crean los arrays vacios para guardar las valoraciones(valoraciones totales, votos totales)
let productRatings = new Array(productCount);
let totalRatings = new Array(productCount);
let totalVotes = new Array(productCount);
//itera sobre cada elemeto de valoracion
ratingInputs.forEach((input, index) => {
  //agrega un evento de cambio a cada elemento de valoracion
  input.addEventListener('change', () => {
    //consigue el indice de valoracion a cada elemento de valoracion
    const ratingIndex = parseInt(input.name.split('-')[1]) - 1;
    //selecciona todos los elementos de valoracion del mismo indice 
    const checkedInputs = document.querySelectorAll(`input[name="rating-${ratingIndex + 1}"]:checked`);
    //inicia las variables para realizar los calculos
    let sum = 0;
    let average = 0;
    //calcula la suma de las valoraciones marcada 
    checkedInputs.forEach(checkedInput => {
      sum += parseInt(checkedInput.value);
    });
//almacena las sumas en los arrays correspondientes 
    productRatings[ratingIndex] = sum;
    totalRatings[ratingIndex] = sum;
    totalVotes[ratingIndex] = checkedInputs.length;
    //calcula el promedio de las valoraciones
    if (totalVotes[ratingIndex] > 0) {
      average = sum / totalVotes[ratingIndex];
    }
    //actualiza el contenido de los promedios de valoracion
    averageRatingElements[ratingIndex].textContent = `Promedio de valoración: ${average.toFixed(1)}`;
    //actualiza la suma final de todas las valoraciones 
    let finalSum = 0;
    let finalAverage = 0;

    for (let i = 0; i < productCount; i++) {
      finalSum += productRatings[i] || 0;
    }
    //calcula la cantidad total de votos y la valoracion maxima
    const totalVoteCount = totalVotes.reduce((acc, val) => acc + val, 0);
    const maximumPossibleRating = productCount * 5;

    if (totalVoteCount > 0) {
      finalAverage = (finalSum / (totalVoteCount * 5)) * 100;
    }
    //actualiza el contenido del elemento de promedio final
    finalRatingElement.textContent = `Promedio final: ${finalAverage.toFixed(2)}%`;
  });
});
