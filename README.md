# Parte Backend do aplicativo De Sinais a Palavras

## Como rodar a API:
### (Hospedado no Render)
- Clonar os arquivos do repositório para uma pasta na sua máquina
- Rodar no terminal da pasta:
```
uvicorn main:app --reload
```
- No browser, rodar o url:
```
http://127.0.0.1:8000/processar?img_path=minhaImagem.jpg
```
> Substitua ```minhaImagem```   pelo caminho da imagem
- O número de dedos levantados na imagem será exibido na tela

## Frontend:
- A API será integrada no Frontend do aplicativo para realizar a contagem dos dedos por meio do envio de dados entre o Frontend e o Backend
- Link do repositório contendo o Frontend: https://github.com/katbmbm/De-Sinais-a-Palavras-App-Mobile-Frontend

## Como funciona: 
### Requisitos Funcionais
- Acessar a câmera do dispositivo móvel para capturar os sinais em Libras em tempo
real
- Identificar gestos e sinais de Libras usando visão computacional (OpenCV,
MediaPipe) e modelos de Machine Learning (TensorFlow, Teachable Machine)
- Traduzir os sinais reconhecidos para palavras e frases em Língua Portuguesa
- Mostrar o texto traduzido na tela em tempo real.

### Requisitos Não-Funcionais
- Realizar a tradução de sinais em tempo real e com precisão
- Ser compatível com dispositivos Android e iOS
- A interface deve ser acessível, simples e adequada para diferentes perfis de
usuários

### Interação
- Para começar a interação entre o fontend e o backend decidimos fazer o aplicativo contar os dedos. Primeiro pegamos um código de python que já tínhamos que faz essa contagem e transformamos em api, hospedamos essa api no render, que é um site que faz hospedagem gratuita. E com a ajuda do andré foi feito uma aplicação react que manda os dados da câmera em forma de imagem para essa api hospedada, e a api é capaz de enviar os dados de volta para o frontend para serem exibidos na tela
