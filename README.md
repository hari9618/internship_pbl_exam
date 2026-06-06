WELCOME TO MY  AI STORY GENERATOR USING LANGCHAIN APPLICATION
THIS APPLICATION GENERATES:a short and creative and meaningful story with in 100-300 and generates the response based on user input only.
first load The necesary libraries
Then from .env load dotenv 
then built a structure prompt using chat_prompt_template
initialize the model=gemini-2.5-flash
then build a parser to structure the response 
build a chain uning lcel to connect all the components
then invoke the chain to run the application
