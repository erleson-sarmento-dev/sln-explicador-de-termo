# Your code goes here
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
import gradio as gr
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
prompt_template = PromptTemplate.from_template(prompt_template_str)
model = init_chat_model("gemini-3.8-flash", model_provider="google_genai")

def generate_explanation(concept):
    prompt = prompt_template.format(concept=concept)
    response = model.invoke(prompt)
    if isinstance(response.content, str):
        return response.content

    text_blocks = [
        block["text"]
        for block in response.content
        if isinstance(block, dict)
        and block.get("type") == "text"
        and isinstance(block.get("text"), str)
    ]
    if not text_blocks:
        raise RuntimeError("A resposta do modelo não contém texto.")
    return "".join(text_blocks)

demo = gr.Interface(
    fn=generate_explanation,
    inputs=[gr.Textbox(label="Termo", lines=1)],
    outputs=[gr.Textbox(label="Explicação", lines=5)],
    flagging_mode="never",
    title="Explicador de Termos",
    description="Digite um termo e receba uma explicação personalizada"
)

demo.launch()