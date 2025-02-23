# ✅ Use AWS Lambda Python Image
FROM public.ecr.aws/lambda/python:3.10

# ✅ Set Working Directory
WORKDIR /var/task

# ✅ Copy Requirements First (for caching)
COPY requirements.txt .

# ✅ Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Define build arguments for API keys
ARG OPENAI_API_KEY
ARG SERPER_API_KEY

# Set environment variables inside the container
ENV OPENAI_API_KEY=${OPENAI_API_KEY}
ENV SERPER_API_KEY=${SERPER_API_KEY}

# ✅ Copy the Rest of the App
COPY . .

# ✅ Set Command for AWS Lambda
CMD ["main.handler"]
