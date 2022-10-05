FROM python:3.10.7-slim

RUN python -m venv /opt/venv
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

RUN adduser --system --group app

RUN pip install --upgrade pip

WORKDIR /app

COPY --chown=app:app requirements.txt .
RUN pip install -r requirements.txt

COPY --chown=app:app . .

USER app


