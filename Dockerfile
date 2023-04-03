FROM python:3.9

WORKDIR /code

ADD ./requirements.txt /code/

RUN pip install -r /code/requirements.txt

ADD . /code/

ENV PORT 80

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "$PORT"]