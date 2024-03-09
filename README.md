# Documentação da API Angels
## 1. Visão geral:
A API Angels é um dos projetos do curso de Engenharia de Software do da UPE e seu objetivo é prover uma maneira prática de integrar um modelo estatístico inteligente à seu sistema. O tema dessa aplicação é predição de morte fetal, portanto, os dados que alimentarão o modelo serão todos relacionados à gestação do bebê. 

[Clique para ver a documentação completa](https://docs.google.com/document/d/1Oo73vu2fbla72ETrUTWeGYBBJmSOepvY3r-mYGfSkEI/edit?usp=sharing)

## 2. Possíveis Erros:

O JSON de um request feito da forma correta conterá duas respostas diferentes referentes a predição da morte fetal:
- **Categórica:** Essa resposta indicará 1 para caso o modelo tenha previsto uma morte fetal ou 0 caso contrário.
- **Probabilística:** Essa resposta terá dois elementos, a probabilidade da morte ocorrer e seu complemento (chance de não ocorrer).

Em caso de encaminhamento com dados de tipos errados, você receberá um erro *entre 1 e 17* que você deverá interpretar como:

- **1:** O campo 'previous_weight' não é válido. ***Certifique-se de fornecer um valor do tipo float não-negativo.***


- **2:** O campo 'gestacional_risc' não é válido. ***Verifique se o valor fornecido para o risco gestacional seja um valor numérico entre 0 e 2, inclusive.***


- **3:** O campo 'schooling' não é válido. ***Garanta que o nível de escolaridade seja um valor numérico entre 0 e 8, inclusive.***


- **4:** O campo 'has_arterial_hypertension' não é válido. ***Verifique se este campo é um valor numérico de 0 ou 1, ou um valor booleano de True ou False.***


- **5:** O campo 'has_diabetes' não é válido. ***Verifique se este campo é um valor numérico de 0 ou 1, ou um valor booleano de True ou False.***


- **6:** O campo 'has_cirurgia_pelvica' não é válido. ***Verifique se este campo é um valor numérico de 0 ou 1, ou um valor booleano de True ou False.***


- **7:** O campo 'has_infeccao_urinaria' não é válido. ***Verifique se este campo é um valor numérico de 0 ou 1, ou um valor booleano de True ou False.***


- **8:** O campo 'has_malformacao_familiar' não é válido. ***Verifique se este campo é um valor numérico de 0 ou 1, ou um valor booleano de True ou False.***


- **9:** O campo 'has_gemelaridade_familiar' não é válido. ***Verifique se este campo é um valor numérico de 0 ou 1, ou um valor booleano de True ou False.***


- **10:** O campo 'quant_gest' não é válido. ***Forneça um valor inteiro não-negativo para a quantidade de gestações.***


- **11:** O campo 'quant_aborto' não é válido. ***Certifique-se de que o número de abortos seja um valor inteiro não negativo.***


- **12:** O campo 'quant_partos' não é válido. ***Verifique se o número de partos é um valor inteiro não negativo.***


- **13:** O campo 'quant_partos_cesarios' não é válido. ***Este campo deve ser um valor inteiro não negativo indicando o número de partos cesáreos.***


- **14:** A idade calculada com base nas datas fornecidas de não é válida. ***Certifique-se de que as datas de nascimento e início da gestação sejam válidas.***


- **15:** A data do primeiro pré-natal calculada com base nas datas fornecidas não é válida. ***Verifique se as datas de início da gestação e do primeiro pré-natal são consistentes.***


- **16:** O intervalo entre gestações calculado com base nas datas fornecidas não é válido. ***Garanta que as datas de início da gestação e do último parto sejam coerentes.***


- **17:** Alguma variável no json tem não tem o nome compatível aos padrões definidos pela documentação da API. ***Verifique a sessão de exemplo de como enviar uma requisição de forma correta para corrigir quaisquer possíveis erros de nomenclatura.***