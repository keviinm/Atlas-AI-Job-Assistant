from crewai import Agent

class CrewAgents:
    """Defines CrewAI agents."""
    
    def __init__(self, tools):
        self.tools = tools
        self.researcher = self._create_researcher()
        self.profiler = self._create_profiler()
        self.resume_strategist = self._create_resume_strategist()
        self.interview_preparer = self._create_interview_preparer()

    def _create_researcher(self):
        return Agent(
            role="Tech Job Researcher",
            goal="Analyze job postings to extract key skills and qualifications.",
            tools=[self.tools.scrape_tool, self.tools.search_tool],
            verbose=True,
            backstory=(
                "You are a skilled tech job researcher who excels at analyzing job postings, "
                "identifying key skills, and helping job seekers tailor their applications for success."
            )
        )

    def _create_profiler(self):
        return Agent(
            role="Personal Profiler for Engineers",
            goal="Research job applicants to create comprehensive profiles.",
            tools=[self.tools.scrape_tool, self.tools.search_tool, self.tools.read_resume, self.tools.semantic_search_resume],
            verbose=True,
            backstory=(
                "You are an expert in analyzing personal and professional backgrounds, "
                "helping job seekers highlight their strengths and stand out in the job market."
            )
        )

    def _create_resume_strategist(self):
        return Agent(
            role="Resume Strategist",
            goal="Optimize resumes to align with job postings.",
            tools=[self.tools.scrape_tool, self.tools.search_tool, self.tools.read_resume, self.tools.semantic_search_resume],
            verbose=True,
            backstory=(
                "With years of experience in resume building and recruitment strategies, "
                "you specialize in crafting resumes that effectively showcase a candidate's skills and experience."
            )
        )

    def _create_interview_preparer(self):
        return Agent(
            role="Interview Preparer",
            goal="Generate interview questions and talking points.",
            tools=[self.tools.scrape_tool, self.tools.search_tool, self.tools.read_resume, self.tools.semantic_search_resume],
            verbose=True,
            backstory=(
                "You are an expert in technical interviews, coaching candidates to confidently answer questions "
                "and effectively communicate their skills during job interviews."
            )
        )

    def get_all_agents(self):
        return [self.researcher, self.profiler, self.resume_strategist, self.interview_preparer]
