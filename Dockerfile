FROM python:3.10

WORKDIR /app

COPY sum.py /app/

CMD [ "python", "sum.py" ]
