FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt --no-cache-dir
COPY . .
CMD coverage run --source=app --omit=*/tests/* -m pytest && coverage report -m
