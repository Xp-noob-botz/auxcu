FROM python:3.10
WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt
RUN pip install motor
CMD ["python3", "bot.py"]
