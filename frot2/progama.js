alert("ola Filipe");
console.log("mensagem no console");
var resposta = prompt("Qual o seu nome?");
console.log(resposta);


var qnt_faltas = prompt("Quantas faltas você tem?");
var aulas = (prompt("Quantas aulas foram ministradas?"));
var nota1 = prompt("Qual a sua primeira nota?");
var nota2 = prompt("Qual a sua segunda nota?"); 
var media = (parseFloat(nota1) + parseFloat(nota2)) / 2; //notas 1 e 2
var recupercao = (prompt("Qual a nota da sua recupercao ?"))  //nota de recuperacao
var porcentagem = (qnt_faltas / aulas) * 100;

console.log("Sua média é " + media);
console.log("Sua porcentagem de faltas é " + porcentagem + "%");  
console.log("Você tem " + qnt_faltas + " faltas de um total de " + aulas + " aulas ministradas");
console.log("Sua nota de recuperação é " + recupercao);  



if (media >= 7 && porcentagem <= 25) {
    alert("Parabéns, você foi aprovado!");
} else if (media < 7 && media >= 5 && porcentagem <= 25) {
    alert("Você fará a recuperação");
    recupercao = prompt("Qual a nota da sua recuperação?");
    var media_final = (media + parseFloat(recupercao)) / 2;
    if (media_final >= 5) {
        alert("Parabéns, você foi aprovado na recuperação");
    } else {
        alert("Você foi reprovado na recuperação");
    }

} else {
    alert("Você foi reprovado");  
}