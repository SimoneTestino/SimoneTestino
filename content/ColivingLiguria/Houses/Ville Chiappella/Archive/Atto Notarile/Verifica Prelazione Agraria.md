---
date: 2025-10-26
draft: false
language: IT/EN
---
>[!Abstract]
>Questo report documenta la procedura di verifica del [[Diritto di Prelazione Agraria]] eseguita nel contesto dell'acquisto delle [[Ville Chiappella]]. Descrive l'identificazione dei confinanti, l'uso di un software proprietario per analizzare le particelle catastali, e la generazione di una lista di 25 codici fiscali. Dettaglia infine la verifica delle qualifiche (CD/IAP) tramite visura camerale. Questo documento è parte integrante della preparazione per l'[[Atto Notarile Ville Chiappella]].

Questo documento descrive la procedura di verifica eseguita in merito al [[Diritto di Prelazione Agraria]] per la compravendita degli immobili [[Ville Chiappella]] siti in Cairo Montenotte. Questa analisi è un allegato tecnico fondamentale per la stesura dell'[[Atto Notarile Ville Chiappella]].

## Identificazione e Acquisizione Dati Catastali

La fase iniziale di analisi è consistita nell'identificazione dei proprietari dei terreni confinanti. Utilizzando i servizi telematici dell'Agenzia delle Entrate (Catasto), abbiamo ottenuto gli estratti di mappa e le visure catastali per immobile relative a tutte le particelle che confinano con i terreni oggetto di compravendita.

Questo include i terreni confinanti a:
* [[Terreni Lungotorrente]]
* [[Terreni oltre Torrente]]
* [[Terreni alla Fonte]]
* Tutte le particelle classificate come pertinenze agricole delle unità abitative.

### Metodologia e Software di Analisi

Per gestire questa complessa mappatura di relazioni tra particelle, abbiamo sviluppato un'applicazione software proprietaria in Python, parte del [[Software for ColivingLiguria|Software per ColivingLiguria]]. Questo strumento modella ogni singola particella catastale (sia nostra che dei confinanti) come un oggetto software (`CadastralParcel`).

Ad ogni particella vengono associati i suoi dati fondamentali, derivati dalle visure:
* Se è di tipo **agricolo** (rilevante per la prelazione).
* Se è una **proprietà target** (una di quelle che stiamo acquistando).
* L'elenco dei **codici fiscali** dei suoi proprietari.

Il programma esegue poi un'analisi incrociata: identifica tutti i confinanti di ogni nostra particella agricola, filtra automaticamente i confinanti non rilevanti (ad esempio quelli non agricoli o quelli già di nostra proprietà) e genera una lista consolidata di tutti i codici fiscali unici che appartengono a proprietari di terreni agricoli confinanti.

Nel pieno rispetto della normativa sulla privacy (GDPR), i file contenenti i dati catastali sensibili e i codici fiscali dei soggetti coinvolti non sono pubblici e rimangono strettamente confidenziali.

**Output:** Al termine di questa fase, il software ha generato una lista consolidata di **25 codici fiscali** unici, appartenenti ai proprietari dei terreni confinanti agricoli.

### Utilizzo per Consulenza

Questo strumento software proprietario, sviluppato per questa analisi specifica, può essere adattato ed utilizzato come parte dei servizi offerti nella mia attività di consulenza [[Project Launch Consultancy; Funding & Bureaucracy in Italy]], per assistere clienti che necessitano di una mappatura e analisi del rischio di prelazione agraria per i loro progetti.

## Verifica delle Qualifiche Professionali

Successivamente, si è proceduto alla **Verifica delle Qualifiche Professionali** per i 25 codici fiscali identificati. L'obiettivo era determinare quali (e se) tra i soggetti identificati possedessero la qualifica di **Coltivatore Diretto (CD)** o **Imprenditore Agricolo Professionale (IAP)**, come dettagliato nelle note sul [[Diritto di Prelazione Agraria]].

Questa verifica è stata effettuata tramite una **Visura Camerale Ordinaria** per ogni singolo codice fiscale, utilizzando il portale ufficiale [registroimprese.it](https://www.registroimprese.it). Come previsto, la ricerca per codice fiscale ha permesso di identificare immediatamente i soggetti non iscritti (per i quali non sussiste il diritto), e di acquistare la visura solo per i casi in cui la ricerca dava esito positivo.

## Esito della Verifica e Conclusioni Operative
Tramite [visureinrete.it](https://www.visureinrete.it/landing-page/ricerca-gratuita.asp?gad_source=1&gad_campaignid=1911285827&gbraid=0AAAAAD_ez1zXGZNEdC0qIE3S8aZQxEfO5&gclid=Cj0KCQjwsPzHBhDCARIsALlWNG12blZPGllXoX78l_QySeX-6IBoeShbxqDwiR69bmcmwrM-LmCd9_waAl94EALw_wcB) possiamo partire da Nome e Cognome e verificare tutto, ahime pero abbiamo memorizzato solo i codici fiscali -_-