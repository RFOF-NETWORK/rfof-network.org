# Wähle das Python Basis-Image
FROM python:3.9-slim

# Setze das Arbeitsverzeichnis
WORKDIR /workspace

# Kopiere die Anforderungen und installiere sie
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den Rest des Codes
COPY . .

# Setze den Standardbenutzer zu vscode
USER vscode
