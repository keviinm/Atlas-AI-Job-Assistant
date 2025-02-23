# ✅ Use AWS Lambda Python Image
FROM public.ecr.aws/lambda/python:3.10

# ✅ Install SQLite (3.35+)
RUN yum install -y gcc gcc-c++ make tar gzip wget && \
    wget https://www.sqlite.org/2024/sqlite-autoconf-3440000.tar.gz && \
    tar xvfz sqlite-autoconf-3440000.tar.gz && \
    cd sqlite-autoconf-3440000 && \
    ./configure --prefix=/usr && make && make install && \
    cd .. && rm -rf sqlite-autoconf-3440000 sqlite-autoconf-3440000.tar.gz && \
    sqlite3 --version  # ✅ Confirm installed version

# ✅ Set Working Directory
WORKDIR /var/task

# ✅ Copy Requirements First (for caching)
COPY requirements.txt .

# ✅ Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# ✅ Define build arguments for API keys
ARG OPENAI_API_KEY
ARG SERPER_API_KEY

# ✅ Set environment variables inside the container
ENV OPENAI_API_KEY=${OPENAI_API_KEY}
ENV SERPER_API_KEY=${SERPER_API_KEY}

# ✅ Copy the Rest of the App
COPY . .

# ✅ Set Command for AWS Lambda
CMD ["main.handler"]
