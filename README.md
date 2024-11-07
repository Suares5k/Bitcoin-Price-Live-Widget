
# **Programa de Verificação de Preço do Bitcoin (BTC)**

Este é um programa simples em **Python** que permite verificar o preço atual do Bitcoin (BTC) em tempo real. O programa busca os dados de uma **API** e exibe o valor atual de **BTC**, além de permitir a conversão de moeda (**USD/REAL**) e visualização de valorização do preço.

## **Funcionalidades**

- **Exibição do preço atual** do Bitcoin (BTC) em USD.
- **Conversão de valores** entre USD e BRL (Real).
- **Exibição da valorização** percentual do preço do Bitcoin em um intervalo de tempo.
- Interface gráfica intuitiva.
- Para mudar Real para Dolar so clicar no nome Real ou Dolar

## **Como rodar o programa**

Este programa foi desenvolvido em **Python** e pode ser executado de duas maneiras: diretamente no ambiente Python ou criando um executável **.exe** com o **PyInstaller**. 

**⚠️ Aviso Importante**: Não disponibilizamos o arquivo **.exe** diretamente, pois ele pode ser detectado como falso positivo por antivírus devido à compactação do **PyInstaller**. Portanto, você deve gerar o arquivo executável em sua máquina.

### **Pré-requisitos**

Antes de executar o programa, certifique-se de que você possui o **Python** instalado e as dependências necessárias. Você pode instalar as dependências utilizando o seguinte comando:

```bash
pip install -r requirements.txt
``````````
``
## **Gerando o Arquivo Executável (.exe)**
``
    Após garantir que todas as dependências estão instaladas, você pode gerar o arquivo executável usando o PyInstaller.
``
    No terminal, navegue até o diretório do seu projeto e execute o comando abaixo:

``
pyinstaller --onefile --windowed --noconsole seu_script.py
    ``
- --onefile: Cria um único arquivo executável.
- --windowed: Impede a abertura de uma janela de terminal ao executar o programa (ideal para interfaces gráficas).
- --icon=icone.ico: Opcional, se você quiser adicionar um ícone personalizado ao executável.
`
    Após a execução do PyInstaller, o arquivo .exe será gerado na pasta dist dentro do diretório do seu projeto.

## **Executando o Programa**

Após gerar o arquivo .exe, basta executá-lo diretamente no seu computador para visualizar o preço atual do Bitcoin e interagir com as funcionalidades.

## **Printscreens**

![Tela de Exemplo](https://raw.githubusercontent.com/Suares5k/Bitcoin-Price-Live-Widget/refs/heads/master/Screenshot_129.png)
![Tela de Exemplo](https://raw.githubusercontent.com/Suares5k/Bitcoin-Price-Live-Widget/refs/heads/master/Screenshot_130.png)



Se você deseja contribuir para este projeto, sinta-se à vontade para criar um fork, fazer alterações e enviar pull requests. Agradecemos suas contribuições!
