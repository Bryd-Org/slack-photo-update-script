FROM python:3.11-alpine

ENV WORKDIR_PATH /app
ENV XDG_DATA_HOME=${WORKDIR_PATH}
ENV UV_CACHE_DIR=./.uv-cache

WORKDIR $WORKDIR_PATH
#RUN apt-get update -y
COPY --from=ghcr.io/astral-sh/uv:0.5.31 /uv /uvx /bin/

COPY ./pyproject.toml .
COPY ./uv.lock .
COPY ./.python-version .

RUN uv sync --locked

COPY --chmod=0444 . .
RUN find $WORKDIR_PATH -type d -exec chown $USER_CONTAINER:$USER_CONTAINER {} \;
RUN find $WORKDIR_PATH -type d -exec chmod 755 {} \;

USER $USER_CONTAINER
CMD uv run main.py test
