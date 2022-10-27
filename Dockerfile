# Use multistage approach
FROM python:3.8-alpine as build

WORKDIR /tmp/favicon
RUN python -m venv /tmp/favicon/.env
RUN source .env/bin/activate
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY main.py .
CMD ["python", "main.py"]


# # Use a specific image
# FROM python:3.8-alpine@sha256:41ea2b8caa7fa3740fd0f0a1cad0c26961707a7e3c7cc49559f54b277ef86fb3

# WORKDIR /tmp/favicon
# COPY --from=build /tmp/favicon/.env .
# COPY main.py .

# ENV PATH="/tmp/favicon/.env/bin:$PATH"
# CMD ["python", "main.py"]
