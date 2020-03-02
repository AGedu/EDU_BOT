*******
EDU_BOT
*******

Web scraping solution applicata al mondo dell’informazione sul web

Abstract
===================
EDU_BOT is a MIT licensed program built by EnergyWay developers with the aim to automatically collect and send news from several websites, related to themes such Education, Artificial Intelligence, Technology and Environmental Sustainability.
The BOT structure is divided into three main core development areas:

- *Scraping*: scripts are implemented in order to scrape news from web pages arbitrarily chosen. Each website has its own html structure, hence it will need its own code for extracting url and keywords from it.

- *Telegram*: this part regards the launching of news to the final user, which happens through a Telegram, and can be called by a user through the app. Moreover, the service will provide a graphic interface (basically, a poll) by which a news evaluation can be implemented and used to analyze user's preferences about news, and eventually exploit these information to better choose news.

- *Preferences analysis*: on the basis of preferences expressed by the user, a mathematical analysis of data will be performed, in order to generate a "matching degree" of each news to the user. This will make the user capable of calling news with an higher or lower degree of match. The analysis is done by means of a SVM algorithm.



Scraping
===================

Inserire una pagina per estrarre notizie
------------------
La maggior parte delle pagine web può potenzialmente essere analizzata al fine di estrarre contenuti. Nel nostro caso, le pagine analizzate sono siti di informazione, contenenti url di notizie quotidiane e ad accesso libero. L'attività di estrazione viene eseguita tramite le librerie Python *Selenium* e *BeautifulSoup*.

Processo:
----------
Il processo di estrazione consiste nei seguenti step:

- raccolta delle url di pagine di informazione free (servizi non a pagamento) e legate alle tematiche di interesse (vd. Abstract)

- per ogni pagina, vengono circostanziate le ultime dieci notizie pubblicate

- per ogni notizia, viene eseguito un controllo di data, attraverso il quale vengono mantenute solamente le notizie più recenti

- una volta mantenute le notizie del giorno corrente, da ognuna di esse sono isolate le parole chiave contenute nell'url stessa (es. in http://www.ansa.it/canale_scienza_tecnica/notizie/tecnologie/**intelligenza**-**artificiale**-**scopre**-**un**-**super**-**antibiotico** le parole chiave sono quelle in grassetto, ovvero quelle apposte al termine dell'url e separate da "-")

- al termine del processo di estrazione, per ogni pagina web analizzata si avranno le notizie estratte nella seguente struttura di Python:

  **Notizia_estratta** = (http://www.ansa.it/canale_scienza_tecnica/notizie/tecnologie/intelligenza-artificiale-scopre-un-super-antibiotico, [intelligenza, artificale, scopre, un, super, antibiotico]) *tupla*
  **Lista_di_notizie** = [Notizia_estratta1, Notizia_estratta2, ...] *lista*

  Si tratta dunque di una lista di tuple. Ogni notizia è racchiusa in una tupla,al cui interno sono contenuti l'url della notizia stessa e le parole chiave, a loro volta sotto forma di lista.

- Infine, per ogni notizia estratta, vengono confrontate le keywords con una lista di parole chiave di riferimento, legate alle tematiche di interesse principale. Se almeno una keyword di una notizia combacia con una parola inclusa nella lista di parole di riferimento, allora da quella notizia viene presa l'url e selezionata per essere inviata su Telegram

- Si crea, dunque, una lista finale di url che verranno inviate dal bot sul canale Telegram.

Librerie
------------------

- 'Selenium
<https://selenium-python.readthedocs.io/>'_

- 'BeautifulSoup
<https://www.crummy.com/software/BeautifulSoup/bs4/doc/>'_

Le due librerie vengono alternate in base alla pagina su cui fare scraping.

Entrambe le librerie permettono di puntare i diversi tag dal codice html ed estrarne il contenuto.

Beautiful soup è più "rapido", in quanto permette cercare il tag anche in base al contenuto interno. Selenium si muove dentro la pagina identificando i tag per tipologia, essendo dunque più strutturato ma meno flessibile di BS. Selenium permette inoltre di aprire il browser, cliccare su oggetti e aprire link.

L'oggetto Selenium, solitamente chiamato "browser", si appoggia a Chromedriver.exe, scaricato e presente sul dispositivo da cui il programma lavora, apre il browser all'url data in input e permette di navigare nel codice html, cliccare collegamenti e compilare campi.

L'oggetto BeautifulSoup, generalmente chiamato "soup", contiene prende in input "browser" e una url qualunque, estraendone per intero il codice html.

Strategia di estrazione
----------
Non esiste strategia univoca per estrarre notizie e parole chiave da un url. Generalmente, la procedura seguita per lo scraping si può riassiumere così:

- la pagina principale viene aperta tramite l'oggetto Selenium ed il suo codice è completamente estratto nell'oggetto "soup";

- il codice html della pagina viene ispezionato manualmente attraverso Chrome (tasto destro, Ispeziona). Usando il puntatore, l'area selezionata rimanda al codice ad esso collegato. Puntando le notizie principali, si vedrà dunque i tag a cui essi sono collegati, in modo tale da poter selezionare gli elementi ricorrenti e "spezzare" il codice in una lista di notizie, da cui verrà estratto l'url e la data;

- le notizie vengono analizzate una ad una tramite un ciclo for; viene estratta la data e confrontata con quella del giorno corrente, restituendo un booleano;

- in caso affermativo, dal codice relativo all'articolo viene estratto l'url e, da essa, le parole chiave, operando sulla stringa. Il tutto viene assembrato sotto forma di tupla, pronto ad essere confrontata con la lista di riferimento.


Telegram
===============

Come attivare il bot:
----------------------
Per attivare il bot e ricevere il link di un articolo, basta inviare ad EDU_BOT il comando /link su telegram

Poll:
-----
EDU_BOT, dopo aver inviato il link di un articolo all'utente, gli invierà una poll che semplicemente chiede all'utente se ha trovato l'articolo interessante e di suo gradimento

Analisi delle preferenze (beta)
===============
Acquisizione dati
----------------------
Ogni parola chiave viene storizzata all'interno di un dataframe Pandas sotto forma di variabile. Ad ognuna di esse viene associato un numero.

Se la notizia viene valutata positivamente dall'utente, il valore numerico associato alle parole chiave di quell'articolo aumenta di uno. Si avrà dunque un contatore di parole chiave presenti negli articoli piaciuti.

Sulla base di questo dataframe, nel momento in cui una notizia è pronta ad essere inviata su Telegram, verrà effettuata una regressione, tramite modello SVR, che permetterà di stabilire un indice di gradimento atteso riguardo a tale notizia.

La regressione avrà come variabili di input il valore numerico legato alle parole
