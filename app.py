#first i load necessary libraries 
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
#load the api key from the .env
load_dotenv()
#prompt is usig to controll the llm behaviour i use chat_prompt_template for dynamic way to give input to the llm i simply we called a list of mesages
#sytem_mesage and user_mesage
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a story Generator,generate short creative and meaningfull story based on user input only and the story length is max 100-300 words "),
        ("user","{input}")
    ]
)
#next i initialize the model gemini-2.5-flash because it provides fast inference strong reasoning and flexible chat option
model= init_chat_model (
    model="gemini-2.5-flash",
    model_provider="google_genai"
)
#next i build a parser to structure the llm response
parser=StrOutputParser()
#next step is build a chain using lcel is a moder way to build a chain uning pipe operator all components are sequentially connect
#prompt sent to the -model response-parser structure
chain=prompt|model|parser
#next i use .invoke to run the chain 
response=chain.invoke(
{"input":"a box finds a mysterious box in his backyard"})
print(response)

