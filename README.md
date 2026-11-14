# Explicador de Termos

Aplicação Python que usa o Google Gemini para explicar conceitos técnicos de
forma clara, concisa e personalizada. A interface web foi construída com
Gradio.

## Como o projeto foi feito

O fluxo da aplicação é:

1. O usuário informa um termo na interface.
2. O programa insere o termo em um template de prompt.
3. O LangChain envia o prompt para o modelo Google Gemini.
4. A explicação retornada é exibida no campo de saída do Gradio.

Tecnologias utilizadas:

- Python
- Gradio
- LangChain
- Google Gemini API
- `python-dotenv`

## Pré-requisitos

- Python 3.13 ou compatível
- Uma chave da Google Gemini API
- Um projeto Google Cloud com a Gemini API habilitada
- Faturamento e cota disponíveis para a API

## Configuração

Na raiz do projeto, crie um arquivo chamado `.env`:

```env
GOOGLE_API_KEY=sua_chave_da_gemini
```

O arquivo `.env` é ignorado pelo Git para que a chave não seja publicada.
Use o arquivo `.env.example` apenas como referência. Nunca coloque uma chave
real no `.env.example` ou no código-fonte.

## Instalação

No PowerShell, dentro da pasta do projeto:

```powershell
python -m pip install -r requirements.txt
```

## Executar a aplicação web

```powershell
python .\gradio-explicador-de-termos.py
```

O terminal exibirá uma URL local semelhante a:

```text
http://127.0.0.1:7860
```

Abra essa URL no navegador, informe um termo e clique em **Submit**.

Para encerrar a aplicação, pressione `Ctrl+C` no terminal.

## Executar pelo terminal

O arquivo `explicador-de-termos.py` executa uma explicação usando o termo
definido diretamente no código:

```powershell
python .\explicador-de-termos.py
```

## Estrutura principal

```text
.
├── explicador-de-termos.py
├── gradio-explicador-de-termos.py
├── requirements.txt
├── .env.example
└── .gitignore
```

## Solução de problemas

### `GOOGLE_API_KEY` não configurada

Confirme se o arquivo `.env` existe na raiz do projeto e contém:

```env
GOOGLE_API_KEY=sua_chave_da_gemini
```

### Erro `402 RESOURCE_EXHAUSTED`

Esse erro indica que a cota ou os créditos da Gemini API foram esgotados.
Confirme se:

- a chave pertence ao mesmo projeto usado pela aplicação;
- a Gemini API está habilitada nesse projeto;
- o projeto está vinculado a uma conta de faturamento ativa;
- existem créditos ou cota disponíveis.

### A página fica em `processing`

Verifique o terminal onde a aplicação foi iniciada. A chamada ao modelo é
feita de forma síncrona e a interface permanece processando enquanto aguarda
a resposta da API.

## Segurança

- Não publique o arquivo `.env`.
- Não compartilhe chaves de API.
- Se uma chave for exposta, revogue-a imediatamente e crie outra.
