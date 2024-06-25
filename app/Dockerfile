FROM python:3.10-alpine AS builder

WORKDIR /app

COPY requirements.txt /app
RUN apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT ["python3"]
CMD ["main.py"]