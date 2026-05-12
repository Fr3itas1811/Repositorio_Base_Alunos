programa {
  funcao inicio() {
 real valor_desconto, valor_original,valor_final,porcentagem_desconto 

 escreva ("digite o valor do produto: ")
 leia (valor_original)

 escreva ("digite a porcentagem do desconto: ")
 leia (porcentagem_desconto)

 valor_desconto = valor_original * porcentagem_desconto / 100

 valor_final = valor_original - valor_desconto

 escreva ("o valor do desconto é valor_original - valor_desconto: ", valor_final )


  }
}
