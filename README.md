DESAFIO PROMAXIMA!

No diretório /desafio-promaxima/promaxima_challenge ou \desafio-promaxima\promaxima_challenge>
- use o comando: python manage.py runserver

Para inicalizar o scraping use a url: http://127.0.0.1:8000/api/scraper

Deve usar o navegador Google Chrome!

---------------------------------------------------------Documentação do Código---------------------------------------------------------

Web Scraping com Django e Selenium.

Objetivo:
  Este código foi desenvolvido para realizar a extração de dados do site Portal Nacional de Contratações Públicas(PNCP). 
  O objetivo é extrair as informações dos editais.

Lógica Implementada:
  """SCROLLING_EDITAL
          Desce a página de acordo com a div selecionada pela variável xpath!
      """
  """CLICK_NEXT
          Clica no botão next no final da página!
      """
  """CLICK_EDITAL
          Clica na div atual da variável XPATH, para acesar a mesma!
      """
  """FIND_ELEMENTS
          Encontra todos os elementos necessários, (Objeto, Modalidade, Comprador, Descrição, Unidade, Quantidade, Valor). Melhor forma no site foi atráves de xpath!
      """   
  """CLICA_XPATH
          Variável base!
  """
  """XPATH
          Variável XPATH recebe a CLICA_XPATH, mudando a numeração da div de 1 até 10(quantidade de editais por página) baseado no loop FOR!
  """
  """NOVO_DADO
          Variável novo_dado, recebe a classe DadosRaspados e atribui a cada variável da classe, uma variável correspondente da função find_elements as quais
          recebem os elementos do scraping!
  """
  """PRINTS
          Simples prints para ver o que estava sendo retornados dos text!
   """
  """DRIVER.BACK
          Volta para a página anterior!
  """

  ERROS:
    Provavelmente erro no driver.back().
    Quando um edital da segunda página em diante é aberto, no momento em que volta para url anterior, vai direto para a primeira e não para a url correta!
    Tentativas de correção foram feitas, mas sem sucesso. Uma possível solução que pensei, mas não consegui implementar por conta do prazo, seria abrir o edital em uma nova guia, assim não precisando trocar a url da guia atual!


