FROM python:3.11.9-slim

RUN pip install flask flask-cors fastapi uvicorn pydantic
COPY . .
EXPOSE 5000
#CMD ["python", "db1.py"]
CMD ["python", "back.py"]