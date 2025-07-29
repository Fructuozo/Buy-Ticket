#VAI RETORNA A ABA PRINCIPAL, CLICA E REALIZA TODA A COMPRA
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def buyticket(driver):

    wait = WebDriverWait(driver, 15)
    cards = wait.until(EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "div.swiper-slide.swipe-partida")
    ))

    visitante_desejado = "Atlético MG"
    campeonato_desejado = "Brasileirão Série A"
    data_desejado = "31|07|2025 - 21:30"

    jogo_encontrado = False

    for card in cards:
        visitante = card.get_attribute("data-visitante")
        campeonato = card.get_attribute("data-campeonato")
        data = card.get_attribute("data-dataevento")

        print(f"[DEBUG] Visitante: {visitante} | Campeonato: {campeonato} | Data: {data}")
        
        if (
            data_desejado.lower() in data.lower()
        ):
            print("[DEBUG] Critérios compatíveis. Verificando botão...")

            try:
                driver.execute_script("arguments[0].scrollIntoView(true);", card)
                actions = webdriver.ActionChains(driver)
                actions.move_to_element(card).perform()

                botao_comprar = card.find_element(By.XPATH, ".//*[contains(text(), 'Comprar')]")

                wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[contains(text(), 'Comprar')]")))
                print(f"Jogo encontrado: Contra {visitante} | {campeonato}")
                botao_comprar.click()
                jogo_encontrado = True
                input()
            except:
                print("Jogo encontrado, compra em breve.")
                jogo_encontrado = False
                break

        else:
            print(f"[DEBUG] ALGUM DADO ESTÁ DIFERENTE")

            print(visitante_desejado.lower(), visitante.lower(),
            campeonato_desejado.lower(), campeonato.lower(),
            data_desejado.lower(), data.lower())

    if not jogo_encontrado:
                print("Nenhum jogo foi encontrado.")