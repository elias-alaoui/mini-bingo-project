# 1. BASE IMAGE – full Python environment
FROM python:3.10

# 2. WORKING DIRECTORY – project root inside the container
WORKDIR /usr/src/app

# 3. DEPENDENCIES – copy and install Python libraries
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. APPLICATION CODE – copy the source code into the image
COPY src/ ./src
COPY README.md .
COPY LICENSE .

# 5. STARTUP COMMAND – run the bingo game in the terminal
CMD ["python", "src/main.py"]

