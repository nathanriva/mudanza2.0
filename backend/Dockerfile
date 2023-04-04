FROM python:3.10-slim-bullseye

ENV PYTHONUNBUFFERED True
WORKDIR /casa   
COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN 

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]   