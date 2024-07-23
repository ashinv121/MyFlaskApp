FROM python:3.13.0b4-slim
WORKDIR /app
COPY requirment.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD [ "python", "run.py" ]