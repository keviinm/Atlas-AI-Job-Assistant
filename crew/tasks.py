from crewai import Task

class CrewTasks:
    """Defines CrewAI tasks."""
    def __init__(self, agents, job_posting_url, github_url, personal_writeup):
        self.agents = agents

        self.research_task = Task(
            description="Extract job requirements from {job_posting_url}.",
            expected_output="A structured list of required skills, qualifications, and experience.",
            agent=self.agents.researcher,
            async_execution=True
        )

        self.profile_task = Task(
            description="Compile a professional profile from {github_url} and {personal_writeup}.",
            expected_output="A comprehensive document covering skills, projects, and experience.",
            agent=self.agents.profiler,
            async_execution=True
        )

        self.resume_strategy_task = Task(
            description="Tailor the resume based on job requirements and personal profile.",
            expected_output="An optimized resume aligned with job needs.",
            output_file="./data/tailored_resume.md",
            context=[self.research_task, self.profile_task],  # ✅ FIXED: Correct references
            agent=self.agents.resume_strategist
        )

        self.interview_preparation_task = Task(
            description="Generate interview questions and talking points.",
            expected_output="A document with key interview questions.",
            output_file="./data/interview_materials.md",
            context=[self.research_task, self.profile_task, self.resume_strategy_task],  # ✅ FIXED
            agent=self.agents.interview_preparer
        )

    def get_all_tasks(self):
        """Return all defined tasks as a list."""
        return [self.research_task, self.profile_task, self.resume_strategy_task, self.interview_preparation_task]