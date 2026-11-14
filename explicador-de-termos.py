# Your code goes here
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

if not os.getenv("GOOGLE_API_KEY"):
    raise RuntimeError(
        "Defina GOOGLE_API_KEY no arquivo .env antes de executar o programa."
    )

prompt_template_str = """
Sua tarefa é explicar o conceito de **{concept}** para mim de uma forma que seja:

1. Clara e intuitiva
2. Concisa (em menos de 100 palavras)
3. Adaptada especificamente a mim e ao que eu já sei

Use as informações a seguir sobre mim para personalizar suas explicações:

- Formação: desenvolvedor Power Platform, no time de projetos
- Interesses profissionais: automações inteligentes e aplicações com LLM
- Interesses pessoais: ...

A personalização deve ser sutil e natural. Evite referências forçadas à minha formação ou aos meus interesses que não ajudem de fato a entender o conceito.
"""
# Cria o template de prompt
prompt_template = PromptTemplate.from_template(prompt_template_str)

# Define a variável de entrada
concept = "ia"

# Formata o prompt com a variável
prompt = prompt_template.format(concept=concept)

# Cria a interface do modelo
model = init_chat_model("gemini-3.8-flash", model_provider="google_genai")

# Chama o modelo com o prompt
response = model.invoke(prompt)

# Imprime o conteúdo gerado
print(response.content)