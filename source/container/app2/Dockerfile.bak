# Use a Python base image
FROM python:3.13-slim
WORKDIR /app
# WORKDIR /usr/local/app

# Install the application dependencies
# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .

# ADD main.py /app/main.py
# ENTRYPOINT

CMD [ "python", "app.py" ]