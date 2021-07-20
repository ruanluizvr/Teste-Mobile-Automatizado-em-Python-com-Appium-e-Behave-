#language: pt

Funcionalidade: Calculadora

    Cenário: somar 10 e 20
        Dado que eu abro a Calculadora
        Quando eu digito '1'
        E eu digito '0' 
        E eu digito '+'
        E eu digito '2'
        E eu digito '0'
        E eu digito '='
        Então o resultado deve ser '30'

    Cenário: subtrair 1 e 1
        Dado que eu abro a Calculadora
        Quando eu digito '1'
        E eu digito '-'
        E eu digito '1'
        E eu digito '='
        Então o resultado deve ser '0'

    Cenário: multiplicar 5 e 9
        Dado que eu abro a Calculadora
        Quando eu digito '5'
        E eu digito '*' 
        E eu digito '9'
        E eu digito '='
        Então o resultado deve ser '45'
    
    Cenário: dividir 15 e 3
        Dado que eu abro a Calculadora
        Quando eu digito '1'
        E eu digito '5'
        E eu digito '/' 
        E eu digito '3'
        E eu digito '='
        Então o resultado deve ser '5'
