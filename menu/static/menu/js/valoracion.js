const ratingInputs = document.querySelectorAll('input[type="radio"]');
const averageRatingElements = document.querySelectorAll('[id^="average-rating"]');
const finalRatingElement = document.getElementById('final-rating');

const productCount = 4;
let productRatings = new Array(productCount);
let totalRatings = new Array(productCount);
let totalVotes = new Array(productCount);

ratingInputs.forEach((input, index) => {
  input.addEventListener('change', () => {
    const ratingIndex = parseInt(input.name.split('-')[1]) - 1;
    const checkedInputs = document.querySelectorAll(`input[name="rating-${ratingIndex + 1}"]:checked`);
    let sum = 0;
    let average = 0;

    checkedInputs.forEach(checkedInput => {
      sum += parseInt(checkedInput.value);
    });

    productRatings[ratingIndex] = sum;
    totalRatings[ratingIndex] = sum;
    totalVotes[ratingIndex] = checkedInputs.length;

    if (totalVotes[ratingIndex] > 0) {
      average = sum / totalVotes[ratingIndex];
    }

    averageRatingElements[ratingIndex].textContent = `Promedio de valoración: ${average.toFixed(1)}`;

    let finalSum = 0;
    let finalAverage = 0;

    for (let i = 0; i < productCount; i++) {
      finalSum += productRatings[i] || 0;
    }

    const totalVoteCount = totalVotes.reduce((acc, val) => acc + val, 0);
    const maximumPossibleRating = productCount * 5;

    if (totalVoteCount > 0) {
      finalAverage = (finalSum / (totalVoteCount * 5)) * 100;
    }

    finalRatingElement.textContent = `Promedio final: ${finalAverage.toFixed(2)}%`;
  });
});
