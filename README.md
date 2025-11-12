# Parte Backend do aplicativo De Sinais a Palavras

## Como rodar a API:
### (Hospedado no Render)
- Clonar os arquivos do repositório para uma pasta na sua máquina;
- Rodar no terminal da pasta (com os arquivos e imagens):
```
uvicorn main:app --reload
```
- No browser, rodar o url:
```
http://127.0.0.1:8000/processar?img_path=minhaImagem.jpg
```
> Substitua ```minhaImagem```   pelo caminho da imagem
- O número de dedos levantados na imagem será exibido na tela

## Uso da API:
- A API será integrada no Frontend do aplicativo para realizar a contagem dos dedos por meio do envio de dados entre o Frontend e o Backend.
- Link do repositório contendo o Frontend: https://github.com/katbmbm/De-Sinais-a-Palavras-App-Mobile-Frontend
