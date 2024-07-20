import os
from dotenv import load_dotenv
from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI
from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools

# Load environment variables from .env file
load_dotenv()

class TravelAgents:
    def __init__(self):
        openai_api_key = os.getenv("OPENAI_API_KEY")
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7, openai_api_key=openai_api_key)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7, openai_api_key=openai_api_key)
        # Commented out as Ollama is not defined
        # self.Ollama = Ollama(model="openhermes")

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent("""
                             Expert in travel planning and logistics.
                             I have decades of experience making travel itineraries.
                             """),
            goal=dedent("""
                        Create a 7-day itinerary with detailed per-day plans,
                        include budget, packing suggestions, and safety tips.
                        """),
            tools=[
                SearchTools.search_internet, 
                CalculatorTools.calculate
            ],
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def city_selection_agent(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent("""
                            Expert at analyzing travel data to pick ideal destinations
                            """),
            goal=dedent(""" 
                        Select the best cities based on weather, season,
                        prices, and traveler interests
                        """),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.OpenAIGPT35,
        )
        
    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent("""
                            Knowledgeable local guide with extensive information
                             about the city, its attractions, and customs
                            """),
            goal=dedent("""
                        Provide the BEST insights about the selected city
                        """),
            tools=[SearchTools.search_internet],
            verbose=True,
            llm=self.OpenAIGPT35,
        )

# Usage
if __name__ == "__main__":
    trip_crew = TravelAgents()
    result = trip_crew.run()
