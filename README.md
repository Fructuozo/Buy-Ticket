<h1>Bot de Compra de Ingressos - Flamengo</h1>

<p>Este projeto é um <strong>bot automatizado</strong> criado com <code>Python</code> e <code>Selenium</code> com o objetivo de <strong>automatizar o processo de login e compra de ingressos</strong> no site oficial de ingressos do Flamengo: <a href="https://ingressos.flamengo.com.br/" target="_blank">https://ingressos.flamengo.com.br/</a>.</p>

<h2>⚠️ Aviso Legal</h2>
<p><strong>Este é um projeto pessoal feito exclusivamente para fins de estudo e aprendizado.</strong><br>
Não é recomendado utilizar este script em produção ou com frequência, pois pode violar os termos de uso do site. Nenhum dado pessoal sensível está incluso no repositório público.</p>

<h2>📌 Funcionalidades</h2>
<ul>
  <li>Abertura automatizada do navegador</li>
  <li>Login automático com e-mail e senha</li>
  <li>Busca por um jogo específico com critérios como visitante, campeonato e data</li>
  <li>Realiza clique automático no botão "Comprar", caso os critérios sejam atendidos</li>
</ul>

<h2>🛠️ Tecnologias utilizadas</h2>
<ul>
  <li>Python</li>
  <li>Selenium WebDriver</li>
  <li>ChromeDriver + webdriver_manager</li>
</ul>

<h2>📂 Estrutura do Projeto</h2>
<pre>
📁 raiz/
├── main.py              # Função principal que executa todas as etapas
├── browser.py           # Abre o navegador
├── login.py             # Realiza o login com credenciais
├── buy.py               # Lógica para encontrar e comprar o ingresso
├── xpaths.py            # Contém os caminhos dos elementos utilizados
</pre>

<h2>✅ Pré-requisitos</h2>
<pre>
pip install selenium
pip install webdriver-manager
</pre>

<h2>🚀 Como executar</h2>
<ol>
  <li>Clone este repositório</li>
  <li>Insira suas credenciais em <code>login.py</code></li>
  <li>Execute o arquivo <code>main.py</code></li>
</ol>

<h2>📸 Exemplo de uso</h2>
<pre>
[DEBUG] Visitante: Atlético MG | Campeonato: Brasileirão Série A | Data: 31|07|2025 - 21:30
[DEBUG] Critérios compatíveis. Verificando botão...
Jogo encontrado: Contra Atlético MG | Brasileirão Série A
</pre>

<h2>📬 Contato</h2>
<p>Caso tenha dúvidas, sugestões ou queira contribuir, fique à vontade para abrir uma <code>issue</code> ou <code>pull request</code>.</p>

<h2>🧪 Objetivo</h2>
<p>Este projeto tem como principal objetivo o aprendizado e prática de automações com Selenium.</p>
