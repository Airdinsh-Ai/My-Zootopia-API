# Zootopia mit API

Generiert eine HTML-Seite mit Tierinformationen basierend auf einer Suche über
die Animals API von API Ninjas.

## Installation

Repository klonen und Abhängigkeiten installieren:

pip install -r requirements.txt

Erstelle eine `.env`-Datei im Projektordner mit deinem eigenen API-Key:

API_KEY='dein_api_key'

## Nutzung

python animals_web_generator.py

Das Programm fragt nach einem Tiernamen und erzeugt daraus die Datei
`animals.html`.
