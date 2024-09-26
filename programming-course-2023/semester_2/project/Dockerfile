FROM python:3.9-slim

ENV BOT_TOKEN=${BOT_TOKEN}
ENV TODOIST_API_TOKEN=${TODOIST_API_TOKEN}

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["python", "main.py"]