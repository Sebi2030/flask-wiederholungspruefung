---
title: Aufgabe 1
nav_order: 1
---

{: .label }
Sebastian Nieme

# [Aufgabe 1/3: SQLAlchemy und Flask-Login]
{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 1. SQLAlchemy
Zuerst habe ich Flask-SQLAlchemy und Flask-Login installiert, um die Interaktion mit der Datenbank und die Benutzerauthentifizierung zu erleichtern.

 Ich habe eine model.py-Datei im Verzeichnis flaskr erstellt. Dies ermöglicht eine bessere Organisation der Datenbankmodelle und der Authentifizierungsfunktionen an einem zentralen Ort.

In der model.py-Datei habe ich Flask-SQLAlchemy und Flask-Login initialisiert. Anschließend habe ich die Modelle für Benutzer, Blog-Posts und Likes definiert. Zusätzlich habe ich den Login-Manager initialisiert und den aktuellen Benutzer über die Benutzer-ID im Login-Manager geladen, um eine nahtlose Authentifizierung zu gewährleisten.

In der Datei blog.py habe ich den veralteten Datenbankcode entfernt. Stattdessen habe ich in der blog.py-Datei neuen Code gemäß der Flask-SQLAlchemy-Struktur geschrieben. Dies umfasst die Implementierung von Funktionen zum Erstellen, Aktualisieren und Löschen von Blog-Posts um die Benutzerinteraktion zu verbessern und die Benutzererfahrung zu optimieren. Zuletzt habe ich die Datei db.py gelöscht, da diese nicht mehr benötigt wird. Zu einer späteren Zeit wird dann noch die Funktion hinzukommen Posts zu liken.

## 2. Decision Record
# Einführung von Flask-SQLAlchemy zur Datenbankintegration in die Flask-Anwendung

# Status
Vorgeschlagen

# Kontext
In meinem vorgeschriebenen Flask-Webanwendungsprojekt wird derzeit SQLite3 direkt zur Datenbankintegration verwendet. Mit zunehmender Komplexität des Projekts besteht jedoch die Notwendigkeit, die Datenbanklösung neu zu bewerten, um Skalierbarkeit, Wartbarkeit und Kompatibilität mit dem Flask-Ökosystem zu gewährleisten. Außerdem besteht die Anforderung im Projekt darin die vorhandenen CRUD-Operationen durch geeignete SQLAlchemy-Methoden zu ersetzen.

# Entscheidung
Nach sorgfältiger Überlegung und Bewertung habe ich beschlossen, Flask-SQLAlchemy als Datenbanklösung für meine Flask-Anwendung zu übernehmen. Diese Entscheidung wird durch mehrere Faktoren motiviert:

## ORM-Fähigkeiten: 
Flask-SQLAlchemy bietet leistungsstarke Object-Relational Mapping (ORM)-Fähigkeiten, die Datenbankinteraktionen vereinfachen und die Codelesbarkeit und -wartbarkeit verbessern, indem sie mit Python-Objekten anstelle von Roh-SQL-Abfragen arbeiten.
## Flexibilität und Kompatibilität: 
Flask-SQLAlchemy integriert nahtlos mit Flask und bietet umfangreiche Unterstützung für verschiedene Flask-Erweiterungen. Diese Kompatibilität gewährleistet eine reibungslosere Integration mit anderen Flask-Komponenten und erleichtert die zukünftige Erweiterung und Verbesserung der Anwendung.
## Skalierbarkeit: 
Während SQLite3 für kleine Anwendungen geeignet ist, bietet Flask-SQLAlchemy bessere Skalierbarkeit und Leistungsoptimierungen, was es für größere Projekte mit höheren Anforderungen an die Parallelität geeigneter macht.
## Community-Unterstützung: 
Flask-SQLAlchemy verfügt über eine lebhafte Community und umfangreiche Dokumentation, die Ressourcen und Unterstützung für die Fehlerbehebung und Implementierung von bewährten Verfahren bereitstellt.
## Codeorganisation:
Die Nutzung der ORM-Fähigkeiten von Flask-SQLAlchemy führt zu einer besseren Codeorganisation und -wartbarkeit, was die Komplexität des mit der Datenbank verbundenen Codes reduziert und die Gesamtwartbarkeit des Projekts verbessert.

# Konsequenzen

## Verbesserte Entwicklungsworkflow: 
Die Nutzung der ORM-Fähigkeiten von Flask-SQLAlchemy wird die Datenbankinteraktionen optimieren, was die Entwicklungszeit reduziert und die Produktivität steigert.
## Erhöhte Skalierbarkeit: 
Die Optimierungen von Flask-SQLAlchemy für größere Projekte stellen sicher, dass meine Anwendung effektiv skalieren kann, um zukünftiges Wachstum und gesteigerten Traffic zu bewältigen.
## Lernkurve: 
Es könnte einige Zeit dauern, bis ich mich mit den ORM-Konzepten und Best Practices von Flask-SQLAlchemy vertraut gemacht habe. Dies kann jedoch durch Schulungssitzungen und die Nutzung verfügbarer Dokumentationsressourcen gemildert werden.
## Migrationsaufwand: 
Die Migration von SQLite3 zu Flask-SQLAlchemy erfordert Anstrengungen, um den vorhandenen datenbankbezogenen Code zu aktualisieren und die Kompatibilität mit dem neuen ORM-basierten Ansatz sicherzustellen.

# Fazit
Die Einführung von Flask-SQLAlchemy als Datenbanklösung entspricht den Projektzielen von Skalierbarkeit, Wartbarkeit und Kompatibilität mit dem Flask-Ökosystem. Diese Entscheidung ermöglicht es mir, ORM-Fähigkeiten zu nutzen, die Codeorganisation zu verbessern und den langfristigen Erfolg und die Skalierbarkeit meiner Flask-Anwendung zu gewährleisten.



## 3. Flask-Login

## 4. Decision Record
