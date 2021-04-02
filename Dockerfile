FROM python:latest

RUN pip3 install jinja2
COPY code .

CMD ["python3","MyDevServer.py","serve"]
