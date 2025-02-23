from logging_setup import get_logger
from crewai import Crew
from crew.environment import CrewEnvironment
from crew.tools import CrewTools
from crew.agents import CrewAgents
from crew.tasks import CrewTasks
from IPython.display import Markdown, display

class JobApplicationCrewManager:
    """Manages the execution of the job application crew."""
    def __init__(self, job_posting_url, github_url, personal_writeup):
        CrewEnvironment.configure()
        logger.info("Initializing JobApplicationCrewManager")
        self.tools = CrewTools()
        self.agents = CrewAgents(self.tools)
        self.tasks = CrewTasks(self.agents, job_posting_url, github_url, personal_writeup)

        self.crew = Crew(
            agents=self.agents.get_all_agents(),
            tasks=self.tasks.get_all_tasks(),
            verbose=True
        )

        self.inputs = {  
            'job_posting_url': job_posting_url,
            'github_url': github_url,
            'personal_writeup': personal_writeup
        }

    def run(self):
        """Run the crew execution and display results."""
        print("\n🚀 Running Job Application Crew...\n")
        self.crew.kickoff(inputs=self.inputs) 
        self.display_results()

    @staticmethod
    def display_results():
        """Display the generated resume and interview materials."""
        print("\n📄 Generated Resume:\n")
        display(Markdown("./data/tailored_resume.md"))

        print("\n🎤 Interview Preparation:\n")
        display(Markdown("./data/interview_materials.md"))