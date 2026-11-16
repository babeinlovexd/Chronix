# Optional: eigener Windows-Installer

Die fertige portable EXE erhältst du unter [Releases](https://github.com/babeinlovexd/Chronix/releases/latest). Der Workflow [Windows build and release](.github/workflows/windows-release.yml) baut und prüft sie automatisch. Inno Setup ist dafür nicht erforderlich.

Wenn du selbst einen zusätzlichen Installationsassistenten verteilen möchtest, kannst du die mit PyInstaller gebaute `Chronix.exe` mit [Inno Setup](https://jrsoftware.org/isinfo.php) paketieren. Verwende dafür die EXE aus demselben Versionsstand wie deine Installer-Metadaten.

Eine Dateizuordnung für `.worldcal` allein implementiert noch kein automatisches Öffnen: Chronix lädt Projekte derzeit über die Oberfläche. Für das direkte Öffnen per Doppelklick wäre zusätzlich eine Verarbeitung des Dateipfads beim Programmstart nötig.
