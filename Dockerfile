# Use a multistage approach
FROM python:3.8-alpine as build

# Install all dependencies to a temporary directory
WORKDIR /install
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt --target /install


# Use a specific image
FROM python:3.8-alpine@sha256:41ea2b8caa7fa3740fd0f0a1cad0c26961707a7e3c7cc49559f54b277ef86fb3

# Copy a directory containing a virtual environment to a draft image
WORKDIR /favicon
COPY --from=build /install ./.env
COPY main.py .

# Add a directory with virtual environment to PYTHONPATH
ENV PYTHONPATH="/favicon/.env:$PYTHONPATH"
CMD ["python", "main.py"]
