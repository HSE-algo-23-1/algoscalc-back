FROM python:3.11
WORKDIR /code
COPY src/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code
ARG BACKEND_VERSION=local
RUN echo $BACKEND_VERSION > .version
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]
