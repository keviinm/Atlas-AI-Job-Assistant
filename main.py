from crew.crew_manager import JobApplicationCrewManager

def main():
    job_posting_url = 'https://jobs.lever.co/AIFund/6c82e23e-d954-4dd8-a734-c0c2c5ee00f1'
    github_url = 'https://github.com/keviinm?tab=repositories'
    personal_writeup = """
        Noah is an accomplished Software Engineering Leader with 18 years of experience,
        specializing in managing remote and in-office teams. He has a strong background in AI
        and data science and has successfully led major tech initiatives.
    """

    manager = JobApplicationCrewManager(job_posting_url, github_url, personal_writeup)
    manager.run()

if __name__ == "__main__":
    main()