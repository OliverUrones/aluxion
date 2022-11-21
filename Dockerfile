FROM python:3.6
EXPOSE 8000
WORKDIR /src
ENV VIRTUAL_ENV=/src/aluxionvenv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY . /src/
RUN pip3 install -r requirements.txt --no-cache-dir
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]