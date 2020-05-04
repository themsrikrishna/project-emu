FROM python:3.8.2-alpine
LABEL image for a very simple flask application
WORKDIR /project-emu
COPY . .
RUN ["pip3", "install", "pipenv"]
RUN ["pipenv", "install"]
CMD pipenv run python src/main.py
