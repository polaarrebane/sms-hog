FROM python:3.12-slim as python-base
RUN mkdir /app
WORKDIR  /app
COPY /pyproject.toml /app
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install 
COPY ./main.py /app/main.py
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:80"]
