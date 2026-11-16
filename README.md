<p align="center">
  <a href="https://github.com/babeinlovexd"><img src="https://raw.githubusercontent.com/babeinlovexd/babeinlovexd/main/bxd-github-header.svg" width="520" alt="BxD / BabeinlovexD"></a>
</p>

# Chronix

[Fragen & Fehler](https://github.com/babeinlovexd/Chronix/issues)

**Chronix** ist eine Desktop-App für Worldbuilding, Fantasy- und Science-Fiction-Geschichten sowie Rollenspielwelten. Du definierst eigene Kalender und Zeiteinheiten und ordnest Ereignisse auf einer gemeinsamen Timeline ein.

<p align="center"><img src="assets/chronix_logo.png" alt="Chronix" width="180"></p>

## Funktionen

- Frei definierte Zeithierarchien statt fest vorgegebener 24-Stunden-Tage.
- Planeten mit unterschiedlichen Tages- und Jahreslängen und synchronisierter Zeitanzeige.
- Epochen, Monate, Wochentage, Feiertage und Schaltregeln.
- Sonnen und Monde mit berechneten Mondphasen.
- Kalenderansicht mit Ereignissen, Figuren, Orten und Handlungssträngen sowie Suche.
- Speicherung als `.worldcal`; Timeline-Export als Markdown und Kalenderexport als PNG.
- Oberfläche mit deutschen und englischen Texten.

Dies ist die aktuelle **PyQt6-Version** von Chronix. Das Repository hieß zuvor `CCE2`.

## Installation aus dem Quellcode

Benötigt werden Python mit `pip` und die in [requirements.txt](requirements.txt) aufgeführten Pakete, insbesondere `PyQt6>=6.5.0`.

```bash
git clone https://github.com/babeinlovexd/Chronix.git
cd Chronix
python -m venv .venv
```

Aktiviere die Umgebung unter Windows mit `.venv\Scripts\activate`, unter Linux/macOS mit `source .venv/bin/activate`. Installiere danach die Abhängigkeiten und starte die App:

```bash
python -m pip install -r requirements.txt
python main.py
```

## Erste Schritte

1. Im Welten- und Zeit-Editor die Zeiteinheiten und Planeten definieren.
2. Monate, Wochentage, Epochen, Feiertage und astronomische Daten ergänzen.
3. Die Welt als `.worldcal` speichern und den Kalender öffnen.
4. Ereignisse mit Figuren, Orten und Handlungssträngen eintragen; über die Suche wiederfinden.
5. Für die Weiterverwendung die Timeline als Markdown oder den Kalender als PNG exportieren.

Sichere bestehende Projektdateien vor umfangreichen Änderungen. Die Dateiendung allein garantiert keine Kompatibilität mit älteren Chronix-Implementierungen.

## Windows-Download & automatische Releases

Die fertige portable Windows-EXE und ihre SHA-256-Prüfsumme findest du unter [Releases](https://github.com/babeinlovexd/Chronix/releases). Eine separate Python-Installation ist für die EXE nicht erforderlich.

Die [Windows-Build-Action](.github/workflows/windows-release.yml) führt die Kalender-Tests und eine GUI-Startprüfung aus, baut die EXE mit PyInstaller und prüft ihren Start. Erst nach erfolgreichem Build veröffentlicht sie bei einem passenden Versions-Tag die EXE und `SHA256SUMS.txt` im Release.

Für neue Versionen `VERSION` aktualisieren und einen passenden Tag wie `v0.1.0` auf diesen Commit setzen. Ein manueller Action-Start baut zunächst nur ein herunterladbares Workflow-Artefakt; er veröffentlicht keinen Release.

### Lokal bauen

- **Windows:** [build.bat](build.bat) installiert Abhängigkeiten und erzeugt mit PyInstaller `dist/Chronix.exe`.
- **Linux/macOS:** [build.sh](build.sh) erzeugt den Build auf dem jeweiligen Hostsystem. Ein Build-Skript ist kein Nachweis für einen getesteten Installer auf jeder Plattform.

## Entwicklung & Fehlersuche

Die Benutzeroberfläche liegt in `cce/gui/`, die Kalender- und Zeitberechnung in `cce/core/`. Nach `python -m pip install -r requirements-build.txt` starten die vorhandenen Engine-Tests mit `python -m pytest -q`; `python ci/smoke_startup.py` prüft die GUI-Konstruktion ohne interaktive Sitzung.

- **PyQt6 fehlt:** Prüfe, ob die virtuelle Umgebung aktiv ist und `pip` zum verwendeten Python gehört.
- **Logo oder Icon fehlt im Build:** Den Build im Repository-Stamm ausführen; die Skripte binden `assets/` ein.
- **Unerwartete Zeitberechnung:** Tageslängen, Zeithierarchie und Schaltregeln der Welt prüfen und im Fehlerbericht ein kleines Beispiel beilegen.

---

## Mitmachen

Fragen, Fehlerberichte und Beiträge sind willkommen. Nenne bei einem [Issue](https://github.com/babeinlovexd/Chronix/issues) bitte Version, Aufbau und Schritte zum Nachstellen. Größere Änderungen besprechen wir am besten vor einem Pull Request.

[BxD / BabeinlovexD](https://github.com/babeinlovexd) · [Website](https://babeinlovexd.de/)
