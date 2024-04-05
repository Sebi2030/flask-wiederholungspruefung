---
title: Aufgabe 1
nav_order: 1
---

{: .label }
Sebastian Nieme

# Aufgabe 1/3: SQLAlchemy und Flask-Login
{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

# 1. SQLAlchemy
Zuerst habe ich Flask-SQLAlchemy und Flask-Login installiert, um die Interaktion mit der Datenbank und die Benutzerauthentifizierung zu erleichtern.

Ich habe eine model.py-Datei im Verzeichnis flaskr erstellt. Dies ermöglicht eine bessere Organisation der Datenbankmodelle und der Authentifizierungsfunktionen an einem zentralen Ort.

In der model.py-Datei habe ich Flask-SQLAlchemy und Flask-Login initialisiert. Anschließend habe ich die Modelle für Benutzer, Blog-Posts und Likes definiert. Zusätzlich habe ich den Login-Manager initialisiert und den aktuellen Benutzer über die Benutzer-ID im Login-Manager geladen, um eine nahtlose Authentifizierung zu gewährleisten.

In der Datei blog.py habe ich den veralteten Datenbankcode entfernt. Stattdessen habe ich in der blog.py-Datei neuen Code gemäß der Flask-SQLAlchemy-Struktur geschrieben. Dies umfasst die Implementierung von Funktionen zum Erstellen, Aktualisieren und Löschen von Blog-Posts um die Benutzerinteraktion zu verbessern und die Benutzererfahrung zu optimieren. Zuletzt habe ich die Datei db.py gelöscht, da diese nicht mehr benötigt wird. Zu einer späteren Zeit wird dann noch die Funktion hinzukommen Posts zu liken.

# 2. Decision Record
## Einführung von Flask-SQLAlchemy zur Datenbankintegration in die Flask-Anwendung

## Status
Vorgeschlagen

## Kontext
In meinem vorgeschriebenen Flask-Webanwendungsprojekt wird derzeit SQLite3 direkt zur Datenbankintegration verwendet. Mit zunehmender Komplexität des Projekts besteht jedoch die Notwendigkeit, die Datenbanklösung neu zu bewerten, um Skalierbarkeit, Wartbarkeit und Kompatibilität mit dem Flask-Ökosystem zu gewährleisten. Außerdem besteht die Anforderung im Projekt darin die vorhandenen CRUD-Operationen durch geeignete SQLAlchemy-Methoden zu ersetzen.

## Entscheidung
Nach sorgfältiger Überlegung und Bewertung habe ich beschlossen, Flask-SQLAlchemy als Datenbanklösung für meine Flask-Anwendung zu übernehmen. Diese Entscheidung wird durch mehrere Faktoren motiviert:

### ORM-Fähigkeiten: 
Flask-SQLAlchemy bietet leistungsstarke Object-Relational Mapping (ORM)-Fähigkeiten, die Datenbankinteraktionen vereinfachen und die Codelesbarkeit und -wartbarkeit verbessern, indem sie mit Python-Objekten anstelle von Roh-SQL-Abfragen arbeiten.
### Flexibilität und Kompatibilität: 
Flask-SQLAlchemy integriert nahtlos mit Flask und bietet umfangreiche Unterstützung für verschiedene Flask-Erweiterungen. Diese Kompatibilität gewährleistet eine reibungslosere Integration mit anderen Flask-Komponenten und erleichtert die zukünftige Erweiterung und Verbesserung der Anwendung.
### Skalierbarkeit: 
Während SQLite3 für kleine Anwendungen geeignet ist, bietet Flask-SQLAlchemy bessere Skalierbarkeit und Leistungsoptimierungen, was es für größere Projekte mit höheren Anforderungen an die Parallelität geeigneter macht.
### Community-Unterstützung: 
Flask-SQLAlchemy verfügt über eine große Community und umfangreiche Dokumentation, die Ressourcen und Unterstützung für die Fehlerbehebung und Implementierung von bewährten Verfahren bereitstellt.
### Codeorganisation:
Die Nutzung der ORM-Fähigkeiten von Flask-SQLAlchemy führt zu einer besseren Codeorganisation und -wartbarkeit, was die Komplexität des mit der Datenbank verbundenen Codes reduziert und die Gesamtwartbarkeit des Projekts verbessert.

## Konsequenzen

### Verbesserte Entwicklungsworkflow: 
Die Nutzung der ORM-Fähigkeiten von Flask-SQLAlchemy wird die Datenbankinteraktionen optimieren, was die Entwicklungszeit reduziert und die Produktivität steigert.
### Erhöhte Skalierbarkeit: 
Die Optimierungen von Flask-SQLAlchemy für größere Projekte stellen sicher, dass meine Anwendung effektiv skalieren kann, um zukünftiges Wachstum und gesteigerten Traffic zu bewältigen.
### Lernkurve: 
Es könnte einige Zeit dauern, bis ich mich mit den ORM-Konzepten und Best Practices von Flask-SQLAlchemy vertraut gemacht habe. Dies kann jedoch durch Schulungssitzungen und die Nutzung verfügbarer Dokumentationsressourcen gemildert werden.
### Migrationsaufwand: 
Die Migration von SQLite3 zu Flask-SQLAlchemy erfordert Anstrengungen, um den vorhandenen datenbankbezogenen Code zu aktualisieren und die Kompatibilität mit dem neuen ORM-basierten Ansatz sicherzustellen.
## Fazit
Die Einführung von Flask-SQLAlchemy als Datenbanklösung entspricht den Projektzielen von Skalierbarkeit, Wartbarkeit und Kompatibilität mit dem Flask-Ökosystem. Diese Entscheidung ermöglicht es mir, ORM-Fähigkeiten zu nutzen, die Codeorganisation zu verbessern und den langfristigen Erfolg und die Skalierbarkeit meiner Flask-Anwendung zu gewährleisten.



# 3. Flask-Login
Um Funktionen wie Anmeldung, Registrierung und Abmeldung mit Flask-Login und SQLAlchemy nutzen zu können, habe ich diese in der auth.py-Datei umgeschrieben und angepasst, wobei ich mich stark auf die Datenbankinteraktion mittels SQLAlchemy konzentriert habe.

Für die Benutzerregistrierung habe ich SQLAlchemy-Methode filter_by genutzt, um zu überprüfen, ob der Benutzername bereits in der Datenbank vorhanden ist. Falls nicht, habe ich einen neuen Benutzer mit der Methode add zur Datenbank hinzugefügt. Dabei habe ich das Passwort mithilfe der generate_password_hash-Funktion gehasht, um die Sicherheit zu gewährleisten.

Bei der Benutzeranmeldung habe ich die eingegebenen Anmeldeinformationen mit den in der Datenbank gespeicherten verglichen. Hierbei habe ich zuerst den Benutzer mithilfe von filter_by abgerufen und dann das eingegebene Passwort mit dem gehashten Passwort in der Datenbank mittels check_password_hash verglichen. Wenn die Überprüfung erfolgreich war, habe ich die Benutzer-ID in der Sitzung gespeichert, um den Benutzer als angemeldet zu markieren.

Zusätzlich zur Datenbankinteraktion habe ich unnötigen Code entfernt, der durch die Implementierung von Flask-Login. Dazu gehörten auch Anpassungen des HTML-Codes, wie das Hinzufügen der Checkbox für die "Remember Me"-Funktionalität in login.html. In der base.html-Datei habe ich außerdem die Weiterleitung zur add Post-Funktion hinzugefügt.

Während des Prozesses gab es einige Herausforderungen bei der Anpassung der index.html-Datei, die jedoch erfolgreich gelöst wurden, um eine reibungslose Integration der neuen Funktionen zu gewährleisten.

# 4. Decision Record
## Flask-Login für die Benutzerauthentifizierung in die Flask-Anwendung implementieren

## Status
Vorgeschlagen

## Kontext
In meinem Flask-Webanwendungsprojekt verwende ich derzeit eine sitzungsbasierte Authentifizierung für die Benutzerverwaltung. Da sich die Projektanforderungen jedoch weiterentwickeln, muss der Mechanismus zur Benutzerauthentifizierung neu bewertet werden, um Sicherheit, Skalierbarkeit und Wartbarkeit zu gewährleisten.

## Entscheidung
Nach sorgfältiger Überlegung und Bewertung habe ich mich entschieden, Flask-Login für die Benutzerauthentifizierung in meiner Flask-Anwendung zu implementieren. Diese Entscheidung ist durch mehrere Faktoren motiviert:

### Sicherheit: 
Flask-Login bietet sichere Mechanismen zur Benutzerauthentifizierung, einschließlich Passwort-Hashing und Schutz vor gängigen Sicherheitslücken wie CSRF-Angriffen.
### Skalierbarkeit: 
Flask-Login vereinfacht die Verwaltung der Benutzerauthentifizierung und lässt sich nahtlos in Flask integrieren, was die Skalierung der Anwendung bei steigenden Benutzerzahlen erleichtert.
### Wartbarkeit: 
Die Nutzung der in Flask-Login integrierten Funktionen für die Benutzerauthentifizierung reduziert die Komplexität der Implementierung benutzerdefinierter Authentifizierungslösungen, was zu einer besseren Codeorganisation und Wartbarkeit führt.
### Flexibel: 
Flask-Login bietet Flexibilität bei der Handhabung von Benutzersitzungen, ermöglicht die Anpassung an die Projektanforderungen und bietet Unterstützung für verschiedene Authentifizierungsmethoden.
## Konsequenzen

### Verbesserte Sicherheit: 
Die in Flask-Login eingebauten Sicherheitsfunktionen verbessern die allgemeine Sicherheitslage der Anwendung und verringern das Risiko von unbefugtem Zugriff und Datenverletzungen.
### Vereinfachte Entwicklung: 
Flask-Login vereinfacht die Verwaltung der Benutzerauthentifizierung und reduziert die Entwicklungszeit und den Aufwand für die Implementierung und Pflege der Benutzerauthentifizierungsfunktionen.
### Lernkurve: 
Es kann einige Zeit dauern, bis ich mich mit den Funktionen und Best Practices von Flask-Login vertraut gemacht habe. Dies kann jedoch durch Schulungen und die Nutzung der verfügbaren Dokumentationsressourcen gemildert werden.
### Aufwand für die Migration: 
Die Umstellung von der sitzungsbasierten Authentifizierung auf Flask-Login erfordert eine Aktualisierung des vorhandenen authentifizierungsbezogenen Codes und die Gewährleistung der Kompatibilität mit dem neuen Authentifizierungsmechanismus.
## Fazit
Die Implementierung von Flask-Login als Benutzerauthentifizierungsmechanismus entspricht den Projektzielen Sicherheit, Skalierbarkeit und Wartbarkeit. Diese Entscheidung wird es mir ermöglichen, die in Flask-Login eingebauten Sicherheitsfunktionen zu nutzen, die Entwicklung zu vereinfachen und den langfristigen Erfolg und die Sicherheit meiner Flask-Anwendung zu gewährleisten.
