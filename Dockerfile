FROM python:3.10

COPY . /app
WORKDIR /app

RUN pip install pipenv

RUN pipenv install --system --deploy

# Run the application
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py"]
