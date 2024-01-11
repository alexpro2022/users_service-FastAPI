FROM python:3.11-slim
WORKDIR /component
COPY component/requirements.txt .
RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt --no-cache-dir
COPY . .
CMD coverage run --source=component --omit=*/tests/* -m pytest && coverage report -m
