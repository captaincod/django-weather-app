# Stage 1: Base build stage
FROM python:3.13-slim AS builder

RUN mkdir /weather_app

WORKDIR /weather_app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

RUN pip install --upgrade pip 

COPY requirements.txt /weather_app/

RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.13-slim
 
RUN useradd -m -r appuser && \
    mkdir /weather_app /static /init && \
    chown -R appuser /weather_app /static /init

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY --from=builder /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

WORKDIR /weather_app

COPY --chown=appuser:appuser . .
 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 
 
USER appuser

EXPOSE 8000 

ENTRYPOINT ["/entrypoint.sh"]