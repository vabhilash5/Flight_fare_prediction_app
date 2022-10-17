FROM python:3.9
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=$PORT", "--server.address=0.0.0.0"]