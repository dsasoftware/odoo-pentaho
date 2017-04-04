## Modul reports

### 04.04.2017
#### ADD
Leistungsbeschreibungsreport benefits_description.prpt hinzugefügt

### 30.03.2017
#### FIX
Rechnungsreport: Fix der Steuersumme


### 22.02.2017
#### CHG
Filter innerhalb der Reports gelöscht

### 22.02.2017
#### ADD/IMP
Neue Reports und Erweiterungen:
- Neu:Einkauf
- Neu:Einkaufs-Anfrage
- Rechnungen:Pagebreak, Währungen, DE-Texte, Adressunterschied Kunde/Company
- Verkauf:Pagebreak, Währungen, DE-Texte
- Lieferschein: Falsche Felder löschen, Abstände korrigieren, Anschrift verbessern
- Pickliste: Diverse Verbesserungen


### 17.02.2017
#### CHG
Rechnungs-Report: Nun auch deutsche Produkt-Mengeneinheit

### 17.02.2017
#### CHG
Rechnungs-Report: Enthält nun auch Plain Fuß & Kopftext
Somit ist der Rechnungsreport bereit zum testen


### 16.02.2017
#### IMP
Rechnungs-Report: Mehrere Anpassungen...
- Rabatt-Spalte funktioniert jetzt nun korrekt
- Zeichnungsnummer hinzugefügt
- Kd Ust-ID-Nr (wenn EU-Firma)
- Sämtliche Titel berücksichtigt (proforma, Gutschrift, Liefer-Rechnung usw)
- Zwischensumme & Übertrag nun korrekt
- Weitere Anpassungen an Abständen im Detail-Band

### 15.02.2017
#### IMP
Rechnungs-Report: Nun auch mit Detailband-Informationen

### 13.02.2017
#### CHG
Rechnungs-Report und Fertigungs-Report überarbeitet (Fertigungsreport nun großteils aufgebaut)

### 10.02.2017
#### ADD/CHG
Neu: Rechnungs-Report (erste Version); Änderung: kleine Anpassungen an Lieferschein und Pickliste

### 09.02.2017
#### ADD
Neu: Fertigungsauftrag
- Grundelemente und Positionen erstellt (Datenbankverbindung konnte aber noch nicht aufgebaut werden zu dem MODEL)

### 08.02.2017
#### ADD/CHG
Neu: Packliste; Änderungen: Lieferschein
- Lieferschein wurde nun getrennt und es gibt zusätzlich auch die Packliste
- Verschiedene Elemente aus der Packliste wurden entfernt, ebenso aus dem Lieferschein welche nicht benötigt werden.



### 07.02.2017
#### IMP
Lieferschein-Report: Neuer verbesserter Stand
- Felder hinzugefügt
- Optik und Abstände verbessert
- If-Abfragen für diverse Felder gesetzt.

### 07.02.2017
#### CHG
SaleOrder-Report: Verlinkungen der Feldnamen einheitlicher umgesetzt.


### 06.02.2017
#### IMP
SaleOrder-Report: Diverse Anpassungen:
- Ausblenden des Übertrags auf der 1. Seite 
- Übertrag nun korrekt mit Währungszeichen formatiert
- Kopf- und Fußtexte PLAINTEXT nun implementiert
- Rabatt-Spalte funktioniert nun korrekt (sobald min. 1 Artikel einen Rabatt-Wert enthält)
- Übersetzung für die Units (Stück/Stunde usw)
- Zeilenhöhe für mehrzeilige Texte nun korrekt
- optischer Helfer für die Anschrift nun ausgeblendet


### 03.02.2017
#### IMP
SaleOrder-Report: Diverse Anpassungen:
- Fax beim Ansprechpartner hinzugefügt
- "Angebot gültig bis" hinzugefügt
- Anschrift von Rechnungsadresse auf Kunden-Kontakt umgestellt
- Schriftlaufweiten und Höhen angepasst
- Übertrag & Zwischensumme angepasst
- Währungszeichen hinzugefügt
- Rechnungsadresse und Lieferadresse sauber eingebaut, inkl. Abfrage für Abweichung vom Kontakt.
- Sämtliche Block-Objekte und Texte so umgebaut das sie nachrücken wenn ein darüber-liegendes Objekt fehlt oder "null" ist.


### 01.02.2017
#### IMP
- SaleOrder-Report: Erweiterung um neue Funktionen und Logik, die Joe hier definiert hat (https://equitania.atlassian.net/browse/ODOO-711)

### 31.01.2017
#### IMP
Lieferschein-Report: Erweitern um mehrere Felder und Bänder.

### 31.01.2017
#### ADD
Erste Version des Lieferschein-Reports mit selected fields

### 30.01.2017
#### IMP
Neue Version des Sale.Order
- Optisch passender zu unserem Basis-Report
- Mehr Felder
- Kontaktperson eingefügt
- Footer überarbeitet
- Hausnummer in der Anschrift
- Tabellen-Header und Zwischensumme erstellt

### 22.08.2016
#### ADD
- Sale.order Pentaho Report Zwischenstand