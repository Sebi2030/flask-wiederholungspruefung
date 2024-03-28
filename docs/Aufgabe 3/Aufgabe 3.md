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
Ich habe die API durch eine schrittweise Vorgehensweise erstellt, beginnend mit der Erstellung der grundlegenden Struktur und Konfiguration. Dazu gehörte die Einrichtung der Dateien api_routes.py, schemas.py und die Konfiguration für OpenAPI Swagger UI. Ich habe sicherzustellen müssen, dass alle benötigten Importanweisungen vorhanden sind, um auf Flask-Views, Flask-Smorest Blueprint, Modelle und Schemas zuzugreifen. Als nächstes habe ich die Schemas PostSchema und PostUpdateSchema erstellt, um die Daten zu validieren und zwischen der API und der Datenbank zu serialisieren und zu deserialisieren. Dabei habe ich auch die Validierung von Feldern in PostUpdateSchema implementiert, um sicherzustellen, dass nur gültige Daten akzeptiert werden. Anschließend habe ich die Haupt-API-Routen und Endpunkte in der Datei api_routes.py definiert. Ich habe Methoden hinzugefügt, um verschiedene CRUD-Operationen auf Blog-Post-Objekten durchzuführen, und Endpunkte erstellt, um einzelne Blog-Posts abzurufen und neue Blog-Posts zu erstellen. 

## 8. Decision Record

## 9. API-Referenz-Dokumentation


