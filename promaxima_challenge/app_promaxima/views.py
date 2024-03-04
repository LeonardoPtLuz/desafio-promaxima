from django.shortcuts import render
from .models import DadosRaspados
from django.http import JsonResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
from selenium.webdriver import ActionChains
from time import sleep
# Create your views here.

def home(request):
    return render(request, 'rotas/home.html')

def scraping(request):

    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    #driver.get(url)

    """SCROLLING_EDITAL
        Desce a página de acordo com a div selecionada pela variável XPATH
    """
    def scroll_edital(driver):
        try:
            scrolling_edital = driver.find_element(By.XPATH, xpath)
            ActionChains(driver).scroll_to_element(scrolling_edital).perform()
            return True
        except Exception as er:
            print(f"Edital não encontrado!  ERRO:{er}")
            return False

    """CLICK_NEXT
        scrolling_next_page: Clina no botão next no final da página!
    """
    def click_next(driver):
        try:
            sleep(2)
            scrolling_next_page = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-content"]/pncp-list/pncp-results-panel/pncp-tab-set/div/pncp-tab[1]/div/div[2]/div[2]/div[3]/pncp-pagination/nav/ul/li[11]/button')))
            ActionChains(driver).scroll_to_element(scrolling_next_page).perform()
            sleep(2)
            scrolling_next_page.click()
            sleep(2)
            return True
        except Exception as er:
            print(f"ERROR: Botão não encontrado!   ERRO:{er}")
            return False

    """CLICK_EDITAL
        Função clica na div atual da variável XPATH, para acesar a mesma!
    """
    def click_edital(driver):
        try:
            sleep(4)
            click_editais = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            click_editais.click()
            return True
        except Exception as er:
            print(f"Nenhum edital encontrado! ERRO:{er}")
            return False
        
    """FIND_ELEMENTS
        Encontra todas os elementos necessários, melhor forma no site foi atráves de xpath
    """     
    def find_elements(driver):
        try:
            objeto = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/pncp-item-detail/div/div[7]/div/p/span'))).text.strip()
            modalidade = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/pncp-item-detail/div/div[4]/div[1]/p/span'))).text.strip()
            comprador = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/pncp-item-detail/div/div[3]/div[3]/p/span'))).text.strip()
            descricao = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/pncp-item-detail/div/pncp-tab-set/div/pncp-tab[1]/div/div/pncp-table/div/ngx-datatable/div/datatable-body/datatable-selection/datatable-scroller/datatable-row-wrapper/datatable-body-row/div[2]/datatable-body-cell[2]/div/span'))).text.strip()
            unidade = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/pncp-item-detail/div/pncp-tab-set/div/pncp-tab[1]/div/div/pncp-table/div/ngx-datatable/div/datatable-body/datatable-selection/datatable-scroller/datatable-row-wrapper/datatable-body-row/div[2]/datatable-body-cell[4]/div/span'))).text.strip()
            quantidade = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/pncp-item-detail/div/pncp-tab-set/div/pncp-tab[1]/div/div/pncp-table/div/ngx-datatable/div/datatable-body/datatable-selection/datatable-scroller/datatable-row-wrapper/datatable-body-row/div[2]/datatable-body-cell[3]/div/span'))).text.strip()
            valor = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/pncp-item-detail/div/pncp-tab-set/div/pncp-tab[1]/div/div/pncp-table/div/ngx-datatable/div/datatable-body/datatable-selection/datatable-scroller/datatable-row-wrapper/datatable-body-row/div[2]/datatable-body-cell[5]/div/span'))).text.strip()

            return objeto, modalidade, comprador, descricao, unidade, quantidade, valor

        except Exception as e:
            print(f"Elemento não encontrado: {e}")
            return None, None, None, None, None, None, None

    try:
        sleep(4)

        """CLICA_XPATH
            Variável BASE
        """
        clica_xpath = (f'//*[@id="main-content"]/pncp-list/pncp-results-panel/pncp-tab-set/div/pncp-tab[1]/div/div[2]/div[2]/div[2]/pncp-items-list/div/div[')

        cont = 0

        while True:
            cont+=1
            url_pag = (f"https://pncp.gov.br/app/editais?q=&status=recebendo_proposta&pagina={cont}")
            driver.get(url_pag)

            print(f"\n{url_pag}\n")

            for i in range(1, 11):
                try:
                    sleep(2)
                    """XPATH
                        Variável XPATH recebe a CLICA_XPATH, mudando a numeração da div entre 1 à 10(quantidade de editais por página) baseado no loop FOR!
                    """
                    xpath = (f'{clica_xpath}{i}]')
                    print(f"\n{xpath}\n")

                    scroll_edital(driver)

                    click_edital(driver)

                    objeto, modalidade, comprador, descricao, unidade, quantidade, valor = find_elements(driver)

                    novo_dado = DadosRaspados(
                        objeto=objeto,
                        modalidade=modalidade,
                        comprador=comprador,
                        descricao=descricao,
                        unidade=unidade,
                        quantidade=quantidade,
                        valor=valor
                    )
                    novo_dado.save()

                    """PRINTS
                        Simples prints para ver o que estava sendo retornados dos text
                    """
                    print(f"Objeto: {objeto}")
                    print(f"Modalidade: {modalidade}")
                    print(f"Comprador: {comprador}")
                    print(f"Descrições: {descricao}")
                    print(f"Unidade: {unidade}")
                    print(f"Quantidade: {quantidade}")
                    print(f"Valor: {valor}")

                except (Exception, TimeoutException, NoSuchElementException, StaleElementReferenceException) as er:
                    print(f'ERROR:   {er}')

                finally:
                    """DRIVER.BACK
                        Volta para a página anterior
                    """
                    driver.back()

            try:
                click_next(driver)

            except (Exception, TimeoutException, NoSuchElementException, StaleElementReferenceException) as er:
                print(f'ERROR:   {er}')
                break

            if cont == 1001:
                try:
                    print("Última página!")
                    break

                except Exception as er:
                    print(f'ERROR:   {er}')

    except (Exception, TimeoutException, NoSuchElementException, StaleElementReferenceException) as er:
        print(f'ERROR:   {er}')

    finally:
        sleep(5)
        driver.close()

    return novo_dado

