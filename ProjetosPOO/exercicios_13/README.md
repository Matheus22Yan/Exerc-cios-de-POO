## 📁 Pasta: Capítulo 13

📌 Descrição:
Exercícios e exemplos práticos do capítulo sobre Interface Gráfica com Tkinter, abordando a criação de interfaces gráficas interativas, manipulação de eventos, uso de widgets como botões, caixas de texto, rótulos e menus, além de técnicas para desenhar elementos gráficos e capturar entradas do usuário.

O programa principal controla um cadastro de sites interessantes, exibindo-os em uma tabela com opções para adicionar, editar e remover entradas.

## 📂 Estrutura dos Arquivos:

* `app.py` — Arquivo principal da interface gráfica.
* `gerente.py` — Gerencia os dados dos sites.
* `janela.py` — Janela para edição e adição de sites.
* `dados.json` — Dados iniciais dos sites em JSON.
* `data.py` — Define um widget personalizado de seleção de data (dia, mês, ano) para uso na interface gráfica.
* `modelo_site.py` — Define a classe `Site`, que representa um site individual com atributos como URL, categoria, data e notas, incluindo a geração de IDs únicos.


---

## 🚀 Como Executar o Aplicativo (`app.py`)

Para rodar o aplicativo principal, siga estes passos:

1.  **Abra o seu Prompt de Comando (CMD)** (no Windows) ou **Terminal** (no Linux/macOS).

2.  **Navegue até a pasta `exercicios_13`** (ou `Capítulo 13`) onde o arquivo `app.py` e os outros arquivos (`gerente.py`, `janela.py`, `dados.json`) estão localizados.
    * **Exemplo de Comando:**
        ```bash
        # No Windows:
        cd C:\Users\SeuNomeDeUsuario\Documents\Exerc-cios-de-POO-main\ProjetosPOO\exercicios_13
        ```
        *(Ajuste o caminho `C:\Users\SeuNomeDeUsuario\...` conforme a localização exata no seu computador. Use a tecla `Tab` para autocompletar e `dir` para listar os conteúdos das pastas.)*

3.  **Execute o arquivo `app.py`:**
    * Uma vez dentro da pasta `exercicios_13` no seu Terminal/CMD, digite o seguinte comando e pressione Enter:
        ```bash
        python app.py
        ```
    * A interface gráfica do aplicativo deverá ser iniciada.

---
