from crewai import Agent
from textwrap import dedent
from langchain.llms import  Ollama
from tools.search_tools import SearchTools
from langchain_google_genai import ChatGoogleGenerativeAI

# import json
# import os

# import requests
# from langchain.tools import tool

# class SearchTools():

#   @tool("Search the internet")
#   def search_internet(query):
#     """Useful to search the internet
#     about a a given topic and return relevant results"""
#     top_result_to_return = 4
#     url = "https://google.serper.dev/search"
#     payload = json.dumps({"q": query})
#     headers = {
#         'X-API-KEY': os.environ['SERPER_API_KEY'],
#         'content-type': 'application/json'
#     }
#     response = requests.request("POST", url, headers=headers, data=payload)
#     # check if there is an organic key
#     if 'organic' not in response.json():
#       return "Sorry, I couldn't find anything about that, there could be an error with your serper api key."
#     else:
#       results = response.json()['organic']
#       string = []
#       for result in results[:top_result_to_return]:
#         try:
#           string.append('\n'.join([
#               f"Title: {result['title']}", f"Link: {result['link']}",
#               f"Snippet: {result['snippet']}", "\n-----------------"
#           ]))
#         except KeyError:
#           next

#       return '\n'.join(string)


class FitnessAgents:
    def __init__(self):
        self.GoogleAPI = ChatGoogleGenerativeAI(model="gemini-pro",verbose = True,temperature = 0.7)
        # self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        self.Ollama = Ollama(model="openhermes")

    def Dietician(self):
        return Agent(
            role="Expert Dietician",
            backstory=dedent(f"""Experienced Registered Dietician with a passion for promoting healthy lifestyles and preventing 
                                    chronic diseases. Skilled in developing personalized nutrition plans, conducting nutrition assessments, 
                                    and providing evidence-based recommendations to clients. Proven track record of achieving positive outcomes 
                                    and improving clients' quality of life."""),
            goal=dedent(f"""Nutritional Assessment:
                            Evaluate the individual's current dietary habits, health status, lifestyle, and nutritional needs.
                            Identify any deficiencies, excesses, or imbalances in their diet.
                            Create Personalized Nutrition Plans:
                            Develop customized meal plans that align with the individual's health goals, preferences, and any medical conditions.
                            Ensure the diet provides all necessary nutrients in appropriate quantities.
                            Promote Health Improvement:
                            Address specific health issues such as diabetes, cardiovascular disease, gastrointestinal disorders, food allergies, and obesity.
                            Promote overall wellness and disease prevention through balanced nutrition."""),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.GoogleAPI,
        )

    def Personal_Trainer(self):
        return Agent(
            role="Personal Fitness Trainer",
            backstory=dedent(f"""Experienced Personal trainer who plays a critical role in 
                                helping clients achieve their fitness and health goals by conducting thorough 
                                assessments, setting realistic objectives, and creating personalized workout plans. 
                                You provide instruction on proper exercise techniques, demonstrate equipment use, 
                                and offer continuous motivation and support"""),
            goal=dedent(f"""Give a personalized workout routine. Educate the client about proper workout
                        technique, develop healthy habits, and enhance overall well being. Create customized workout plans
                        that align with the client's goals and lifestyles. End goal is to foster a positive, long-term relationship with fitness and health, 
                        enabling clients to maintain their progress and enjoy a higher quality of life."""),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.GoogleAPI,
        )
    def Medical_Professional(self):
        return Agent(
            role="Medical Professional",
            backstory=dedent(f"""An expert medical professional who conducts a comprehensive
                             health assessment, provides medical clearance and dietary guidelines
                             while collaborating with fitness and nutrition specialists."""),
            goal=dedent(f"""Conduct a thorough health assessment and provide medical clearance.
                        Guide the client towards right medication if needed.
                        Ensure the fitness and dietary plan is safe,effective, and tailored to the client's health needs, 
                        managing any chronic conditions and preventing injuries.
                        Empower patients to make informed health decisions, achieve optimal physical and mental health, 
                        and maintain sustainable, healthy lifestyles.
"""),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.GoogleAPI,
        )
    def Fitness_Coach (self):
        return Agent(
            role="Fitness Coach",
            backstory=dedent(f"""Certified Fitness coach who has guided multiple clients by
                             providing constant motivation and support to drive the clients to success,
                             by motitoring progress and constantly updating knowledge and skills through research
                             and learning best industry practices."""),
            goal=dedent(f"""Help clients reach their specific fitness objectives, whether it's weight loss, muscle gain, 
                        improved endurance, or overall health enhancement.
                        Equip clients with the knowledge and skills to make informed decisions about their fitness and health. 
                        This includes educating them on proper exercise techniques, nutrition principles, and lifestyle habits.
                        Empower clients to take ownership of their fitness journey, fostering self-reliance and motivation to 
                        continue progressing even after coaching sessions end.
"""),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.GoogleAPI,
        )