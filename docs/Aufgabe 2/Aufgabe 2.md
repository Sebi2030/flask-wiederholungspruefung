---
title: Aufgabe 2
nav_order: 1
---

{: .label }
Sebastian Nieme

# [Aufgabe 2/3: Like-Button]
{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## [5. Implementieren Sie einen Like-Button für einzelne Blog-Posts]
Das erste was ich gemacht habe, ist, dass ich in der index.html die Anzeige und Steuerung eines Like-Buttons für jeden Blog-Post implementiert habe. Zuerst wird die Anzahl der Likes angezeigt, dann wird überprüft, ob der Post bereits geliked wurde. Abhängig davon wird entweder ein gefülltes oder leeres Daumen-hoch-Symbol angezeigt. 

Die Interaktion mit dem Button wird durch eine JavaScript-Funktion verarbeitet, die dem Server mitteilt, ob der Post geliked oder unliked habe, und die Anzeige entsprechend aktualisiert, ohne die Seite neu zu laden.

Zusätzlich habe ich zwei Skriptdateien eingebunden: index.js, die meine benutzerdefinierte JavaScript-Funktion enthält. Die Funktion sendet eine Anfrage an den Server, um den Like-Status eines Blog-Posts zu ändern. Anschließend aktualisiert sie die Anzeige der Likes und den Stil des Like-Buttons entsprechend. Bei Fehlern wird eine Benachrichtigung angezeigt. Außerdem die Font Awesome-Bibliothek, die eine Vielzahl von Icons bereitstellt, darunter das Daumen-hoch-Symbol, das für meinen Like-Button verwendet wird.

## [6. Decision Record]


