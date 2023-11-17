// 90 dias
// const Downloads = 149.578;
// const Trials = 6731;
// const Pagos = 3634;

// Estimativa 30 dias
const Downloads = 49859;
const Trials = 2245;
const Pagos = 1212;
const Payment = 19.5;

// Expectativa de 2 anos

let inscritos = Pagos;
let loss = 0.2;
Print(
  `Mês de Trial: 
    Usuários: ${inscritos}
    100% em relação ao inicial.
    Receita: R$ ${(inscritos * Payment).toFixed(2)}`
);
for (let i = 0; i < 24; i++) {
  inscritos = inscritos * (1 - loss);
  if (loss > 0.1) {
    loss -= 0.01;
  }
  Print(
    `${i + 1}° Mês: 
    Usuários: ${inscritos.toFixed(0)}
    ${((inscritos / Pagos) * 100).toFixed(2)}% em relação ao inicial.
    Receita: R$ ${(inscritos * Payment).toFixed(2)}`
  );
}

function Print(string) {
  console.log(string);
}
