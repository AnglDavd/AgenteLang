import os

from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)

load_dotenv()

OPENAI_MODEL = "gpt-3.5-turbo"
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

PROMPT_COUNTRY_INFO = """
    Provee informacion aceca de {country}.
    """

def main():
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name=OPENAI_MODEL)
    
    #pregunta al usuario
    country = input("Ingresa el nombre del país: ")

    message = HumanMessagePromptTemplate.from_template(template=PROMPT_COUNTRY_INFO)
    chat_prompt = ChatPromptTemplate.from_messages(messages=[message])
    chat_prompt_with_values = chat_prompt.format_prompt(country=country)

    response = llm(chat_prompt_with_values.to_messages())
    print(response)

if __name__ == "__main__":
    main()