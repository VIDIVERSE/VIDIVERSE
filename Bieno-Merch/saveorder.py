pip install PyGithub

import json
import os
from datetime import datetime
from github import Github, GithubException

# === KONFIGURATION ===
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Sicher im Environment speichern!
REPO_NAME = "DEIN_USERNAME/bestellungen"  # z.B. "maxmustermann/bestellungen"
DATEINAME = "bestellungen.json"

# === FUNKTION: Bestellung lokal speichern ===
def speichere_bestellung(bestellung):
    """Speichert eine Bestellung lokal in einer JSON-Datei."""
    daten = []
    if os.path.exists(DATEINAME):
        with open(DATEINAME, "r", encoding="utf-8") as f:
            try:
                daten = json.load(f)
            except json.JSONDecodeError:
                daten = []

    bestellung["zeitstempel"] = datetime.now().isoformat()
    daten.append(bestellung)

    with open(DATEINAME, "w", encoding="utf-8") as f:
        json.dump(daten, f, ensure_ascii=False, indent=4)

    print(f"✅ Bestellung lokal gespeichert: {bestellung}")

# === FUNKTION: Datei auf GitHub hochladen ===
def lade_zu_github_hoch():
    """Lädt die lokale JSON-Datei ins GitHub-Repository hoch oder aktualisiert sie."""
    if not GITHUB_TOKEN:
        raise ValueError("❌ GitHub Token fehlt! Bitte als Umgebungsvariable GITHUB_TOKEN setzen.")

    g = Github(GITHUB_TOKEN)
    try:
        repo = g.get_repo(REPO_NAME)
    except GithubException as e:
        print(f"❌ Repository nicht gefunden: {e}")
        return

    with open(DATEINAME, "r", encoding="utf-8") as f:
        inhalt = f.read()

    try:
        # Prüfen, ob Datei schon existiert
        file = repo.get_contents(DATEINAME)
        repo.update_file(file.path, "Update Bestellungen", inhalt, file.sha)
        print("🔄 Datei auf GitHub aktualisiert.")
    except GithubException:
        # Datei existiert noch nicht → neu anlegen
        repo.create_file(DATEINAME, "Neue Bestellungen hochgeladen", inhalt)
        print("📤 Datei neu auf GitHub hochgeladen.")

# === HAUPTPROGRAMM ===
if __name__ == "__main__":
    # Beispiel-Bestellung
    neue_bestellung = {
        "kunde": "Max Mustermann",
        "produkt": "Laptop",
        "anzahl": 2,
        "preis": 1299.99
    }

    speichere_bestellung(neue_bestellung)
    lade_zu_github_hoch()
