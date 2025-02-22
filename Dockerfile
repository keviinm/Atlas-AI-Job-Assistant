# ✅ Use AWS Lambda Python Image
FROM public.ecr.aws/lambda/python:3.10

# ✅ Set Working Directory
WORKDIR /var/task

# ✅ Copy Requirements First (for caching)
COPY requirements.txt .

# ✅ Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Copy the Rest of the App
COPY . .

# ✅ Set Command for AWS Lambda
CMD ["main.handler"]
