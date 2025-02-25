FROM python:3.11.11
WORKDIR /app

COPY main.py /app
COPY routes /app/routes
COPY schemas /app/schemas
COPY services /app/services
COPY utils /app/utils
COPY requirements.txt /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]