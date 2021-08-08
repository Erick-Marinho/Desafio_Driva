# Desafio_Driva_Opção_01
Neste repositório encontram-se as resoluções para o desafio proposto pela empresa Driva.

Foram disponibilzadas pela empresa, através de seu CTO - **Wagner Agostinho**,  duas opções de desafios, logo, neste repositório, encontram-se as soluções para a 1º opção. 

## :panda_face: Desafio Opção 01

Na opção 01, foi pedido para elaborar um pequeno código em Python utilizando a biblioteca Pandas e que atendesse aos seguintes requisitos.

Neste momento, decidi organizar meu projeto em pequenos desafios, dividi para <s>*não se perder*</s> conquistar, enumerando os desafios do 1º ao 8º, já contidos os desafios EXTRAS, assim como também resolvi usar checkboxs para marcação de tarefas concluídas e/ou não concluídas.

**Checklist**

- [x] Leia o arquivo "DadosEmpresa.csv";
- [x] Print no terminal as colunas desse arquivo;
- [x] Print no terminal as primeiras linhas desse arquivo;
- [x] Print no terminal o total de empresas nesse arquivo que tem a coluna "opcao_pelo_simples" com o valor "SIM";
- [x] Print no terminal a soma do "capital_social" de todas as empresas;
- [x] Print no terminal todas as empresas que tem "capital_social" maior que 10.000 e menor que 20.000;
- [x] **EXTRA**: Leia o arquivo "DadosEndereco.csv";
- [x] **EXTRA**: Faça um merge entre os dois arquivos pela coluna "cnpj" e salve um arquivo CSV com todas as empresas que são de "CURITIBA";
    - [x] Faça um merge entre os dois arquivos pela coluna "cnpj";
    - [x] salve um arquivo CSV com todas as empresas que são de "CURITIBA";

## :computer: Desenvolvimento

Posteriormente a organização das tarefas, <s>*depois de 2 xícaras de café*</s> prontamente, criei um ambiente virtual no diretório do meu projeto e fui para a execução das tarefas.

Criei um repositório no github e fui para a instalação de dependências e bibliotecas que otimizariam e organizariam o desenvolvimento da minha análise de dados.

Os dados a serem analisados inicialmente estavam em uma planilha, na qual, no fim das atividades, foi pedido que fosse mergeada com uma outra planilha e após o feito, pediu-se para salvar um arquivo .csv com novas informações.

Particularmente, tenho grande admiração pela biblioteca Pandas, pois trata-se de uma ferramenta poderosa no quesito análise de dados, o que me ajudou bastante na execução do que foi pedido.

Algumas dúvidas surgiram no meio do caminho, e a documentação estava ali para salvar-me, definitivamente sua documentação é esplêndida!

No desafio **Print no terminal o total de empresas nesse arquivo que tem a coluna "opcao_pelo_simples" com o valor "SIM";** fiquei um pouco com dúvida. Não sabia exatamente se a função .value_counts já poderia me conteplar com o resultado, pois ela retorna um objeto contendo contagens de valores únicos, logo, seria retornado a quantidade de SIM e NÃO na mesma consulta, então decidi executar de uma outra forma, trazendo apenas a coluna pedida com a quantidade de valores SIM.

Já no desafio **Print no terminal a soma do "capital_social" de todas as empresas** por se tratar de valores de retorno alto e monetário, a saída fica um pouco ilegível. Resolvi então aplicar uma formatação para melhorar um pouco mais, porém acabou que não fiquei muito seguro quanto ao resultado. Algo que conseguiria sanar aprofundando-me um pouco mais nas informações obtidas dataframe ou fazendo uma pergunta ao Wagner :).

Enfim, os demais desafios, consegui chegar as soluções a contento.

## :wrench: Construido com

[Pandas](https://pandas.pydata.org/) - Biblioteca de análise e manipulação de dados.
[Flake8](https://flake8.pycqa.org/en/latest/) - Ferramenta que verifica o estilo do código com base na gloriosa PEP8.
[MyPy](https://mypy.readthedocs.io/en/stable/) - Verificador de tipo estático.
[Autopep8](https://pypi.org/project/autopep8/) - ferramenta que formata automaticamente o código Python de acordo com o PEP8.

## :flags: Versão

Usei o [GitHub](github.com) para o controle de versão.

## ✒️ Autores

* **Desenvolvedor Web** - *Desenvolvimento* - [Erick Marinho](https://github.com/Erick-Marinho)

## :blush: Expressões de gratidão

* Agradecimento especial ao [Wagner Agostinho](https://www.linkedin.com/in/wagnerrua/) pela oportunidade oferecida, assim sendo possível está realizando este desafio, que com certeza, ajudou-me a desafiar-me e principalmente, ajudou-me a aprender mais. 🤓

---
⌨️ com ❤️ [Erick Marinho](https://github.com/Erick-Marinho)

