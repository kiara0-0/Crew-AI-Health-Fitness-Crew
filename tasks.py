from crewai import Task
from textwrap import dedent

class FitnessTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def personalized_diet_plan(self, agent, weight, height, allergy, bodyfat):
        return Task(
            description=dedent(
                f"""
            **Task**: Develop a daily diet plan
            **Description**: Based on the client's weight, height, body fat and allergies,
            develop a healthy and sustainable diet plan that the client could use in order to 
            achieve their weight or health related goals. You MUST provide the best and most sustainable 
            diet plan for each day of the week. You MUST also take in their preferences 
            into consideration. Address specific health issues such as diabetes, cardiovascular disease, gastrointestinal disorders, food allergies, and obesity.
            Promote overall wellness and disease prevention through balanced nutrition.
            **Parameters**: 
            - Weight: {weight}
            - Height: {height}
            - BodyFat: {bodyfat}
            - Allergies: {allergy}
            **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
        )

    def personalized_workout_routine(self, agent, weight, height, bodyfat, physical_disability, interests):
        return Task(
            description=dedent(
                f"""
            **Task**: Develop a daily workout plan with suitable rest and recovery days
            **Description**: Based on the client's weight, height, body fat and physical disabilities,
            develop a workout routine which is sustainable and that the client could use in order to 
            achieve their weight or health related goals. You MUST provide the best and most sustainable 
            workout plan for each day of the week. You MUST also take in their preferences/ interests
            into consideration while curating the workout plan. Analyze the client's current workout routine, and make improvements in that in order
            for them to reach their goals.
            **Parameters**: 
            - Weight: {weight}
            - Height: {height}
            - BodyFat: {bodyfat}
            - Physical_disability: {physical_disability}
            - Interests: {interests}
            **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
        )
    
    def medical_help(self, agent, weight, height, bodyfat):
        return Task(
            description=dedent(
                f"""
            **Task**: Conducts a comprehensive health assessment and provide medical clearance for the client
            **Description**: You have to conduct a thorough health assessment and provide medical clearance.
                        You must guide the client towards right medication if needed and ensure the fitness and dietary plan is safe,effective, and tailored to the client's health needs, 
                        managing any chronic conditions and preventing injuries.
                        Empower patients to make informed health decisions, achieve optimal physical and mental health, 
                        and maintain sustainable, healthy lifestyles.
            **Parameters**: 
            - Weight: {weight}
            - Height: {height}
            - BodyFat: {bodyfat}
            **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
        )
    
    def fitness_help(self, agent, weight, height, bodyfat):
        return Task(
            description=dedent(
                f"""
            **Task**: Provide constant motivation to the client and monitor progress
            **Description**: You MUST Help clients reach their specific fitness objectives, whether it's weight loss, muscle gain, 
                        improved endurance, or overall health enhancement.
                        You have to equip clients with the knowledge and skills to make informed decisions about their fitness and health which 
                        includes educating them on proper exercise techniques, nutrition principles, and lifestyle habits.
                        You MUST empower clients to take ownership of their fitness journey by motivating them to 
                        continue progressing even after coaching sessions end.
            **Parameters**: 
            - Weight: {weight}
            - Height: {height}
            - BodyFat: {bodyfat}
            **Note**: {self.__tip_section()}
        """
            ),
            agent=agent,
        )
