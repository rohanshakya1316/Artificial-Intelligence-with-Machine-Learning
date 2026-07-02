# Python program for the implementation of vacuum cleaner

import random
import time

class VacuumEnvironment:
    def __init__(self):
        # Establish locations and randomly assign 'Clean' or 'Dirty' states
        self.locations = {'A': random.choice(['Clean', 'Dirty']), 
                          'B': random.choice(['Clean', 'Dirty'])}
        # Randomly place the vacuum agent in Room A or Room B
        self.agent_location = random.choice(['A', 'B'])

    def get_status(self, location):
        return self.locations[location]

    def clean_location(self, location):
        self.locations[location] = 'Clean'

    def display_env(self):
        print(f"Environment Status -> Room A: {self.locations['A']} | Room B: {self.locations['B']}")
        print(f"Vacuum Position    -> Room {self.agent_location}")
        print("-" * 45)


class ReflexVacuumAgent:
    def __init__(self):
        self.cost = 0  # Track performance cost (1 point per action)

    def program(self, location, status):
        """Determines the action based entirely on current percepts."""
        if status == 'Dirty':
            return 'Suck'
        elif location == 'A':
            return 'Right'
        elif location == 'B':
            return 'Left'


def run_simulation():
    # Initialize the environment and the reflex agent
    env = VacuumEnvironment()
    agent = ReflexVacuumAgent()
    
    print("=== Vacuum Cleaner Simulation Started ===")
    env.display_env()
    
    # Run the agent until both rooms are clean
    while 'Dirty' in env.locations.values():
        current_loc = env.agent_location
        current_status = env.get_status(current_loc)
        
        # Agent decides on an action based on current inputs
        action = agent.program(current_loc, current_status)
        agent.cost += 1
        
        print(f"[Percept] Location: {current_loc}, Status: {current_status}")
        print(f"[Action]  Agent decides to: {action}")
        
        # Execute the chosen action in the environment
        if action == 'Suck':
            env.clean_location(current_loc)
        elif action == 'Right':
            env.agent_location = 'B'
        elif action == 'Left':
            env.agent_location = 'A'
            
        time.sleep(1)  # Brief pause to simulate active cleaning
        env.display_env()
        
    print("=== Goal Reached: All Rooms Clean! ===")
    print(f"Total Actions Taken (Path Cost): {agent.cost}")


if __name__ == "__main__":
    run_simulation()
