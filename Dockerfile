FROM python:3.10.7-slim-buster

RUN python -m venv /opt/venv
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

RUN adduser --system --group worker

RUN pip install --upgrade pip

WORKDIR /home/worker/app

COPY --chown=worker:worker requirements.txt .
RUN pip install -r requirements.txt

COPY --chown=worker:worker . .

USER worker


