from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def plan_itinerary(self, agent, city, travel_dates, interests):
        return Task(
            description=dedent(
                f"""
            **Task** : Develop a 7-day Travel Itinerary
            **Description** : Expand the city guide into a full 7-day travel itinerary with detailed per-day plans, including 
            weather forecasts, places to eat, packing suggestions, and a budget breakdown. We must suggest actual places to visit, and 
            actual hotels to stay, and actual restaurants to go to. This itinerary should cover all the aspects of the trip,
            from arrival to departure, integrating the city guide information with practical travel logistics. 

            **Parameters** :
            - City : {city}
            - Trip Date : {travel_dates}
            - Traveler Interests : {interests}

            **Note** : {self.__tip_section()}
        """
            ),
            agent=agent,
        )

    def task_2_name(self, agent):
        return Task(
            description=dedent(
                f"""
            Take the input from task 1 and do something with it.
                                       
            {self.__tip_section()}

            Make sure to do something else.
        """
            ),
            agent=agent,
        )
