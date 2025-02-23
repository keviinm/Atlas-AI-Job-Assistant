# ✅ Use Amazon Linux 2023
FROM public.ecr.aws/lambda/python:3.10

# ✅ Set Working Directory
WORKDIR /var/task

# ✅ Copy Requirements First (for caching)
COPY requirements.txt .

# ✅ Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Define environment variables
ARG OPENAI_API_KEY
ARG SERPER_API_KEY
ENV OPENAI_API_KEY=${OPENAI_API_KEY}
ENV SERPER_API_KEY=${SERPER_API_KEY}

# ✅ Copy the Rest of the App
COPY . .

# ✅ Debug: Check SQLite Version
RUN sqlite3 --version || echo "SQLite not found!"

# ✅ Set Command for AWS Lambda
CMD ["main.handler"]
