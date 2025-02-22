
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from crew.crew_manager import JobApplicationCrewManager

router = APIRouter()



class JobRequest(BaseModel):
    job_posting_url: str
    github_url: str
    personal_writeup: str

@router.post("/apply")
def apply_for_job(job: JobRequest):
    """API Endpoint to start a job application process."""
    try:
        manager = JobApplicationCrewManager(
            job.job_posting_url,
            job.github_url,
            job.personal_writeup
        )
        response = manager.run()
        
        # Convert response to JSON if it's not already
        if isinstance(response, dict):
            return {"status": "success", "response": response}
        else:
            return {"status": "success", "response": str(response)}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Job application failed: {str(e)}")
