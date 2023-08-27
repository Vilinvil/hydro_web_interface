FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
EXPOSE 9000

COPY ./data_storage /code/data_storage
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "9000"]