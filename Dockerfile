# # files(app.py) in src folder sample
# FROM python:3.10.1-alpine3.15
# WORKDIR /app
# COPY requirements.txt .
# RUN pip install -r requirements.txt
# COPY src src
# ENV PORT 5001
# EXPOSE 5001
# ENTRYPOINT ["python", "./src/app.py"]
# CMD ["app.py"]


# # Original sample
# FROM python:3.10.1-alpine3.15
# WORKDIR /app
# COPY . .
# RUN pip install -r requirements.txt
# CMD [ "python", "./app.py"]


# For Mac M1 sample, if you are Mac M1, the generate practice of Dockerfile is not work
FROM --platform=linux/x86-64 python
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD [ "python", "./app.py"]