---
title: Aufgabe 3
nav_order: 1
---

{: .label }
Sebastian Nieme

# [Aufgabe 3/3:  RESTful API]
{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 7. Erstellen Sie eine RESTful API
Ich habe die API durch eine schrittweise Vorgehensweise erstellt, beginnend mit der Erstellung der grundlegenden Struktur und Konfiguration. Dazu gehörte die Einrichtung der Dateien api_routes.py, schemas.py und die Konfiguration für OpenAPI Swagger UI. Ich habe sicherzustellen müssen, dass alle benötigten Importanweisungen vorhanden sind, um auf Flask-Views, Flask-Smorest Blueprint, Modelle und Schemas zuzugreifen. Als nächstes habe ich die Schemas PostSchema und PostUpdateSchema erstellt, um die Daten zu validieren und zwischen der API und der Datenbank zu serialisieren und zu deserialisieren. Dabei habe ich auch die Validierung von Feldern in PostUpdateSchema implementiert, um sicherzustellen, dass nur gültige Daten akzeptiert werden. Anschließend habe ich die Haupt-API-Routen und Endpunkte in der Datei api_routes.py definiert. Ich habe Methoden hinzugefügt, um verschiedene CRUD-Operationen auf Blog-Post-Objekten durchzuführen, und Endpunkte erstellt, um einzelne Blog-Posts abzurufen und neue Blog-Posts zu erstellen. Ich habe auch Blueprints für Authentifizierung und Blogging erstellt und in die API integriert. Dabei habe ich Duplikate entfernt und die Konfiguration aktualisiert, um sicherzustellen, dass die API ordnungsgemäß funktioniert und die Blueprints richtig registriert sind. Um die API zugänglicher zu machen, habe ich sie mit OpenAPI Swagger UI konfiguriert, um automatisch eine Dokumentation zu erstellen. Darüber hinaus habe ich eine Fehlerbehandlung hinzugefügt, um sicherzustellen, dass die API auf ungültige Anfragen oder nicht gefundene Ressourcen angemessen reagiert. Die Dokumentation der API wird im letzten Punkt nochmal ausführlicher erwähnt.

## 8. Decision Record

## Titel: 
Auswahl einer Flask API
## Status:
Vorgeschlagen

## Kontext: 
Als Entwickler musste ich eine Entscheidung darüber treffen, welche Erweiterung oder Bibliothek verwendet werden soll, um eine RESTful API in Flask zu implementieren. Die verfügbaren Optionen waren Flask-RESTful, Flask-Restless-NG, Flask-RESTX und Flask-Smorest.

## Entscheidung: 
Nach sorgfältiger Bewertung der verfügbaren Optionen habe ich mich für Flask-Smorest entschieden.

## Begründung:
1.	Dokumentation und Community-Support: Flask-Smorest bietet eine umfassende und gut strukturierte Dokumentation, die es mir leicht macht, mich mit der Bibliothek vertraut zu machen und sie effektiv zu nutzen. Außerdem gibt es eine aktive Community, die mir bei Fragen und Problemen unterstützen kann.
2.	Einfachheit und Benutzerfreundlichkeit: Flask-Smorest bietet eine einfache und intuitive Möglichkeit, RESTful APIs in Flask zu erstellen. Es verwendet Marshmallow für die Serialisierung von Daten, was eine saubere Trennung von Datenvalidierung und Datenpräsentation ermöglicht.
3.	Flexibilität und Erweiterbarkeit: Flask-Smorest baut auf Flask-Restful auf und erweitert es um zusätzliche Funktionen, die für die Erstellung von RESTful APIs nützlich sind. Es ermöglicht die einfache Integration von OpenAPI-Spezifikationen für die automatische Generierung von API-Dokumentationen.
4.	Aktive Entwicklung: Flask-Smorest wird aktiv entwickelt und gepflegt, was bedeutet, dass es regelmäßig Updates und neue Funktionen erhält. Dies stellt sicher, dass die Bibliothek mit den neuesten Best Practices und Anforderungen Schritt hält.
5.	Bekanntheit und Verbreitung: Flask-Smorest ist eine etablierte Bibliothek mit einer soliden Benutzerbasis. Durch die Verwendung einer weit verbreiteten Bibliothek kann ich von den Erfahrungen anderer Entwickler profitieren und auf eine breite Palette von Ressourcen und Bibliotheken zugreifen, die mit Flask-Smorest kompatibel sind.
## Konsequenzen: 
Die Entscheidung für Flask-Smorest als Basis für unsere RESTful API in Flask hat folgende Konsequenzen:
1.	Entwicklungskonsistenz: Durch die Verwendung einer gemeinsamen Bibliothek für die Implementierung unserer RESTful APIs wird die Entwicklungskonsistenz innerhalb des Teams erleichtert, da alle Entwickler mit den gleichen Werkzeugen arbeiten.
2.	Einfache Skalierbarkeit: Flask-Smorest bietet eine solide Basis für die Implementierung von RESTful APIs, die einfach skalierbar ist. Dies ermöglicht es uns, unsere API entsprechend den wachsenden Anforderungen unseres Projekts anzupassen.
3.	Einfache Wartung und Fehlerbehebung: Da Flask-Smorest gut dokumentiert und weit verbreitet ist, wird die Wartung und Fehlerbehebung unserer API erleichtert. Es gibt eine Fülle von Ressourcen und Beispielen, auf die ich zurückgreifen kann, um Probleme schnell zu lösen.
4.	Langfristige Unterstützung: Da Flask-Smorest aktiv entwickelt wird, kann ich sicher sein, dass wir langfristig Unterstützung und Aktualisierungen für unsere API erhalten, um sicherzustellen, dass sie mit zukünftigen Versionen von Flask und anderen Abhängigkeiten kompatibel ist.


## 9. API-Referenz-Dokumentation


