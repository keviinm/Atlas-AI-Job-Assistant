# ✅ Use Amazon Linux 2023 instead of Amazon Linux 2
FROM public.ecr.aws/amazonlinux/amazonlinux:2023

# ✅ Install SQLite 3.35+ and Python3.10
RUN dnf install -y sqlite sqlite-devel python3.10 python3-pip gcc gcc-c++ make tar gzip wget \
    && sqlite3 --version  # ✅ Confirm installed version

# ✅ Set Working Directory
WORKDIR /var/task

# ✅ Copy Requirements First (for caching)
COPY requirements.txt .

# ✅ Install Dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Define build arguments for API keys
ARG OPENAI_API_KEY
ARG SERPER_API_KEY

# ✅ Set environment variables
ENV OPENAI_API_KEY=${OPENAI_API_KEY}
ENV SERPER_API_KEY=${SERPER_API_KEY}

# ✅ Copy the Rest of the App
COPY . .

# ✅ Set Command for AWS Lambda
CMD ["main.handler"]