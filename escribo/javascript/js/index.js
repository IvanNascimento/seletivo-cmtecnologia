/**
 * Retorna a soma de todos os números menores que a entrada
 * divisíveis por 3 ou 5
 * @param {int} numero
 * @return {int} total
 */
function somaMultiplos(numero) {
  let total = 0;

  for (let i = 0; i < numero; i++) {
    if (i % 3 === 0 || i % 5 === 0) {
      total += i;
    }
  }

  return total;
}

console.log(`10 => ${somaMultiplos(10)}`);
console.log(`11 => ${somaMultiplos(11)}`);
console.log(`20 => ${somaMultiplos(20)}`);
console.log(`25 => ${somaMultiplos(25)}`);
console.log(`100 => ${somaMultiplos(100)}`);
