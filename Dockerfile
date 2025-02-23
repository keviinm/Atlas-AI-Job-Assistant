# ✅ Use Amazon Linux 2 (compatible with AWS Lambda)
FROM amazonlinux:2 as builder

# ✅ Install SQLite 3.35+ from Amazon's official repository
RUN amazon-linux-extras enable python3.10 && \
    yum install -y sqlite python3.10 python3-pip gcc gcc-c++ make tar gzip wget && \
    sqlite3 --version  # ✅ Confirm installed version

# ✅ Now, switch to AWS Lambda Base Image
FROM public.ecr.aws/lambda/python:3.10

# ✅ Copy SQLite binary from builder stage
COPY --from=builder /usr/bin/sqlite3 /usr/bin/sqlite3

# ✅ Set Working Directory
WORKDIR /var/task

# ✅ Copy Requirements First (for caching)
COPY requirements.txt .

# ✅ Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Define Build Arguments for API Keys
ARG OPENAI_API_KEY
ARG SERPER_API_KEY

# ✅ Set Environment Variables Inside the Container
ENV OPENAI_API_KEY=${OPENAI_API_KEY}
ENV SERPER_API_KEY=${SERPER_API_KEY}

# ✅ Copy the Rest of the App
COPY . .

# ✅ Set Command for AWS Lambda
CMD ["main.handler"]
