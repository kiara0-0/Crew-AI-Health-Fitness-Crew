
from crewai import  Crew
from textwrap import dedent
from agents import FitnessAgents
from tasks import FitnessTasks

from dotenv import load_dotenv
load_dotenv()

class FitnessCrew:
    def __init__(self, weight, height, bodyfat, allergy, physical_disability,interests):
        self.weight = weight
        self.height = height
        self.bodyfat = bodyfat
        self.allergy = allergy
        self.pd = physical_disability
        self.interests = interests

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = FitnessAgents()
        tasks = FitnessTasks()

        # Define your custom agents and tasks here
        Dietician = agents.Dietician()
        Personal_Trainer = agents.Personal_Trainer()
        Medical_Professional = agents.Medical_Professional()
        Fitness_Coach = agents.Fitness_Coach()

        # Custom tasks include agent name and variables as input
        personalized_diet_plan = tasks.personalized_diet_plan(
            Dietician ,
            self.weight,self.height,self.bodyfat,self.allergy
        )

        personalized_workout_routine = tasks.personalized_workout_routine(
            Personal_Trainer,
            self.weight,self.height,self.bodyfat, self.pd, self.interests
        )

        medical_help = tasks.medical_help(
            Medical_Professional,
            self.weight,self.height,self.bodyfat
        )

        fitness_help = tasks.fitness_help(
            Fitness_Coach,
            self.weight,self.height,self.bodyfat
        )

        # Define your custom crew here
        crew = Crew(
            agents=[Dietician, Personal_Trainer, Medical_Professional, Fitness_Coach],
            tasks=[personalized_diet_plan, personalized_workout_routine, medical_help, fitness_help],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to the Fitness Crew!")
    print("-------------------------------")
    height = input(dedent("""Enter your height in cms"""))
    weight = input(dedent("""Enter your weight in kgs """))
    bodyfat = input(dedent("""Enter your bodyfat % """))
    allergy = input(dedent("""Enter any allergies if you have """))
    physical_disability = input(dedent("""Mention any physical disabilities that you may have"""))
    interests = input(dedent("""What are your interests while working out?"""))

    fitness_crew = FitnessCrew(weight, height, bodyfat, allergy, physical_disability,interests)
    result = fitness_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)
