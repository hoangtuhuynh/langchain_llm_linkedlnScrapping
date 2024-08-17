from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from third_parties.linkedln import scrape_linkedin_profile
if __name__ == "__main__":
    load_dotenv()

    print("Hello LangChain")
   
    summary_template = """
    given the Linkdln information  about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    #llm = ChatOllama(model="llama3")

    chain = summary_prompt_template | llm
    linkdln_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/hoang-tu-huynh-a02aa124a/")
    res = chain.invoke(input={"information": linkdln_data})

    print(res)
