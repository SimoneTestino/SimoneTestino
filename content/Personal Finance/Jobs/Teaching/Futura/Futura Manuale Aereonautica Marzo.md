---
draft: true
date: 2025-03-13
---
I paste here the relevant code for the second document described in [[Futura Math Didactic Document]]. The source code is available in the project [Overleaf: Documento 03.25](https://www.overleaf.com/read/njtwzjnxvgpb#c86992).

The `name`package refers to [[LaTeX Commands]] on date 13.03.2025.
### Unione
````LaTeX
\include{name}
\usepackage{booktabs}
\setcounter{tocdepth}{2}

\renewcommand{\contentsname}{Indice}
\newcommand{\subsectionstar}[1]{%
  \subsection*{#1}%
  \addcontentsline{toc}{subsection}{#1}%
}
\title{Manuale per l'Orale di Matematica\\
\Large Documento Comprensivo di Entrambe le Prove}

\begin{document}

\maketitle

\tableofcontents
\newpage

\section{Progressioni Matematiche}
In matematica, esistono vari tipi di successioni numeriche, comunemente note come progressioni, che seguono schemi specifici. Tra queste, le due tipologie più fondamentali sono le \textit{progressioni aritmetiche} e le \textit{progressioni geometriche}. 

Nel corso dei prossimi approfondimenti, analizzeremo in dettaglio entrambe le tipologie: le progressioni aritmetiche, in cui ogni termine è ottenuto aggiungendo una costante al termine precedente, e le progressioni geometriche, in cui ogni termine si forma moltiplicando il termine precedente per un fattore costante. Questi due modelli rappresentano le basi per lo studio delle successioni numeriche e trovano applicazioni in numerosi ambiti della matematica.

\paragraph{Sequenze}
\smallskip
\noindent
Una \textit{sequenza} di numeri è un insieme \textit{ordinato} di valori in cui ciascun elemento compare in una posizione ben precisa (o \textit{indice}) e in cui le \textit{ripetizioni} sono permesse. In altre parole, se consideriamo una sequenza \( (a_n) \), ogni termine \( a_n \) occupa la \(n\)-esima posizione all’interno della sequenza. Il concetto di “ordine” è fondamentale: a differenza di un insieme, dove i membri non hanno un ordine intrinseco, in una sequenza la disposizione dei termini determina la \textit{natura} stessa della collezione. 

\smallskip
\noindent
Un esempio di sequenza è la \textit{successione dei numeri naturali} \( (1, 2, 3, 4, \ldots) \), in cui ciascun termine \(a_n\) coincide con \(n\). Oppure, possiamo avere una sequenza che ammette ripetizioni, come \( (2, 2, 5, 2, 5, 5, 2, \ldots) \). In questo caso, pur avendo elementi ripetuti, l’ordine con cui compaiono stabilisce una struttura diversa da un semplice insieme non ordinato.

\smallskip
\noindent
È quindi fondamentale saper distinguere le sequenze numeriche dagli insiemi numerici. Tipicamente indichiamo le sequenze numeriche tra parentesi tonde mentre gli insiemi tra parentesi graffe. Alcune differenze fondamentali sono che negli insiemi, ripetizioni ed ordine dei numeri non sono permessi, o per meglio dire, due insiemi che si distinguono solo per ordine dei numeri o per ripetizioni sono uguali. Notiamo infatti che $$\{2, 2, 3, 5\} = \{5, 3, 2\}$$ Tuttavia questo, come abbiamo visto, non è affatto il caso per le sequenze, notiamo infatti che $$(2, 2, 3, 5) \not = (5, 3, 2)$$

\paragraph{Insiemi}
Ora che abbiamo distinto le nozioni di insieme e di sequenza, è importante tenere a mente diverse operazioni che si possono fare con gli insiemi, come quella di unione, intersezione e sottrazione. Queste operazioni saranno alle basi di moltissimi concetti matematici che vedremo e per quanto semplici costituiscono le fondamenta della matematica.

\noindent
\textit{Unione.} Dati due insiemi \(A\) e \(B\), la loro unione \(A \cup B\) è l’insieme di tutti gli elementi che appartengono \textit{almeno} a uno dei due:
\[
A \cup B = \{\,x \mid x \in A \;\text{o}\; x \in B\,\}.
\]
\textit{Intersezione.} L’intersezione \(A \cap B\) raccoglie gli elementi che \textit{appartengono a entrambi} gli insiemi:
\[
A \cap B = \{\,x \mid x \in A \;\text{e}\; x \in B\,\}.
\]
\textit{Differenza.} La differenza \(A \setminus B\) contiene gli elementi di \(A\) \textit{non presenti} in \(B\):
\[
A \setminus B = \{\,x \mid x \in A \;\text{e}\; x \notin B\,\}.
\]

\newpage

\subsectionstar{[31] Progressioni Aritmetiche}
Una progressione aritmetica è una successione numerica in cui ciascun termine, a partire dal secondo, si ottiene aggiungendo ad esso una costante detta \textit{differenza comune}. In termini matematici, se indichiamo con \( a_1 \) il primo termine della successione e con \( d \) la differenza costante, il termine generico \( a_n \) si esprime come:
\[
a_n = a_1 + (n-1) \cdot d.
\]

È importante osservare che una progressione aritmetica è determinata unicamente da due valori: il valore iniziale \( a_1 \) e la differenza comune \( d \). Questi due parametri permettono, infatti, di ricostruire completamente la successione, poiché ogni termine successivo si ottiene incrementando il precedente di \( d \).

Per esempio, consideriamo la progressione aritmetica con \( a_1 = 3 \) e \( d = 4 \). I primi termini di questa successione sono:
\[
\begin{array}{rcl}
a_1 &=& 3, \\
a_2 &=& 3 + 4 = 7, \\
a_3 &=& 3 + 2 \cdot 4 = 11, \\
a_4 &=& 3 + 3 \cdot 4 = 15, \\
\vdots & & \vdots
\end{array}
\]

Per vedere un esempio un po' diverso, consideriamo la progressione aritmetica con \( a_1 = 5 \) e \( d = -3 \). I primi termini di questa successione sono:
\[
\begin{array}{rcl}
a_1 &=& 5, \\
a_2 &=& 5 + (-3) = 2, \\
a_3 &=& 5 + 2 \cdot (-3) = -1, \\
a_4 &=& 5 + 3 \cdot (-3) = -4, \\
\vdots & & \vdots
\end{array}
\]
Notiamo quindi che quando la $d$ è negativa allora la sequenza diventa descrescente ed arriverà anche nei numeri negativi, le proprietà ed il comportamento della progressione però rimangono invariati.

Un altro esempio si ottiene considerando una progressione aritmetica con termini decimali, ad esempio ponendo \( a_1 = 4{,}5 \) e \( d = 0{,}3 \). In questo caso la successione risulta crescente, e i primi termini saranno:
\[
\begin{array}{rcl}
a_1 &=& 4{,}5, \\
a_2 &=& 4{,}5 + 0{,}3 = 4{,}8, \\
a_3 &=& 4{,}5 + 2 \cdot 0{,}3 = 5{,}1, \\
a_4 &=& 4{,}5 + 3 \cdot 0{,}3 = 5{,}4, \\
\vdots & & \vdots
\end{array}
\]
Notiamo quindi che è possibile trovare sequenze che non coinvolgano unicamente numeri interi ma che possono anche coinvolgere numeri razionali, lo stesso lo si può immaginare, per quanto meno comune, con numeri irrazionali, come $\pi $ o $\sqrt{2}$.

\paragraph{Calcolo della Somma}
Inoltre, è possibile calcolare la somma dei primi \( n \) termini di una progressione aritmetica utilizzando la formula:
\[
S_n = \frac{n}{2} \left( 2a_1 + (n-1)d \right).
\]
Questa espressione evidenzia come la somma sia legata in maniera diretta sia al valore iniziale che alla differenza comune, permettendo così di determinare in maniera semplice il totale dei primi \( n \) termini.

In sintesi, una progressione aritmetica non solo è definita dalla coppia \((a_1, d)\), ma permette anche di determinare facilmente la somma parziale attraverso una formula esplicita. Questa caratterizzazione ne fa uno strumento fondamentale nell'analisi delle successioni numeriche.
\medskip

Supponiamo di avere una progressione aritmetica con \textit{primo termine} \(a_1\) e \textit{differenza comune} \(d\). Vogliamo calcolare la \textit{somma dei primi} \(n\) termini, denotata \(S_n\).


\noindent
Ad esempio, scegliamo \(\,n = 6\), ma \textit{non} specifichiamo ancora i valori numerici di \(a_1\) e \(d\); useremo la \textit{formula generale}:
\[
S_n = \frac{n}{2} \Bigl(2a_1 + (n-1)\,d\Bigr).
\]
Con \(n = 6\), si ha
\[
S_6 = \frac{6}{2}\,\Bigl(2a_1 + 5\,d\Bigr)
= 3\,\bigl(2a_1 + 5d\bigr)
= 6\,a_1 + 15\,d.
\]
Questa espressione mostra come, \textit{senza} dover conoscere i termini intermedi della successione, sia sufficiente sapere il \textit{primo termine} \(a_1\) e la \textit{differenza comune} \(d\) per determinare la somma \(S_6\). Se, ad esempio, \(a_1 = 3\) e \(d = 4\), otteniamo
\[
S_6 = 6 \times 3 \;+\; 15 \times 4
= 18 \;+\; 60
= 78.
\]
Pertanto, i primi 6 termini di questa progressione aritmetica \((3,\,7,\,11,\,15,\,19,\,23)\) hanno somma \(78\), in piena coerenza con la formula. In generale, \(\,S_n\) si può calcolare agevolmente \textit{per qualsiasi} \(n\) voluto, \textit{solo} conoscendo \(a_1\) e \(d\). 

\medskip

Infine, per avere una rappresentazione grafica della progressione aritmetica, consideriamo:

\begin{center}
\begin{tikzpicture}[scale=0.4, line cap=round, line join=round]

% Assi cartesiani per la rappresentazione discreta
\draw[->] (0,0) -- (7,0) node[right] {\small $k$};
\draw[->] (0,0) -- (0,15) node[left] {\small valore};

% Disegno di una progressione aritmetica: a1=3, d=2, n=6
% y_k = a1 + (k-1)*d = 3 + (k-1)*2
\foreach \k in {1,...,6}{
  \pgfmathtruncatemacro{\val}{3 + (\k-1)*2} % valore aritmetico
  % Tracciamo un piccolo reticolo
  \fill (\k,\val) circle(2pt) node[above left] {\small $\val$};

  % Collegamento dei punti con una linea continua per mostrarne l'andamento
  \ifnum\k>1
    \pgfmathtruncatemacro{\oldval}{3 + (\k-2)*2}
    \draw[dashed] (\k-1,\oldval) -- (\k,\val);
  \fi
}

% Etichette di riferimento
\node at (0.2,-0.5) {\small 0};
\node at (-0.3,0) {\small 0};

\end{tikzpicture}
\end{center}
Notiamo quindi che una progressione aritmetica è, in fin dei conti, una retta della quale osserviamo solamente i valori interi. Capiremo quindi ancora meglio le progressioni aritemtiche, una volta capite le equazione lineari in algebra e le rette in geometria.

\newpage

\subsectionstar{[32] Progressioni Geometriche}
Una \textit{progressione geometrica} è una successione di numeri in cui ciascun termine, a partire dal secondo, si ottiene moltiplicando il termine precedente per una costante detta \textit{rapporto} della progressione.

Data una progressione geometrica, i suoi termini sono indicati con:
\[
a_1,\; a_2,\; a_3,\; \ldots,\; a_n,
\]
dove ciascun termine è legato al precedente dalla relazione:
\[
a_n = a_{n-1} \cdot r,
\]
con:
\begin{itemize}
    \item \(a_1\) che rappresenta il primo termine della progressione;
    \item \(r\) il rapporto, un numero reale diverso da zero;
    \item \(a_n\) l'ennesimo termine.
\end{itemize}

Se desideriamo esprimere in forma esplicita il termine generico della progressione, possiamo scrivere:
\[
a_n = a_1 \cdot r^{\,n-1}.
\]
Questa formula ci permette quindi di riuscire ad individuare un qualsiasi numero della progressione sapendounicmanete il numero di partenza $a_1$ ed il rapporto della progressione $r$. Passiamo ora ad alcuni esempi e proprietà per rendere più concreta l'idea.

Spesso si richiede di \textit{individuare} \(a_1\) e \(r\) a partire da alcuni termini noti. In particolare, conoscendo due termini consecutivi \(a_n\) e \(a_{n+1}\), la relazione si ricava da \(r=\frac{a_{n+1}}{a_n}\). Ad esempio, se \(a_3=12\) e \(a_4=36\), si ha \(r=\frac{36}{12}=3\). La conoscenza di \(r\) e \(a_1\) consente di descrivere completamente la progressione e di comprenderne il comportamento di crescita o decrescita. 

\subsubsection*{Segno dei Termini}
Il segno dei termini di una progressione geometrica dipende dalla ragione \(r\). Se \(r\) è positivo, tutti i termini della progressione manterranno lo stesso segno del primo termine \(a_1\). Se \(r\) è negativo, i termini alterneranno il segno, ossia la successione oscillerà tra valori positivi e negativi.

\textbf{Esempi:}
\begin{itemize}
    \item Se \(a_1=4\) e \(r=2\), i termini della progressione sono:
    \[
    4,\; 8,\; 16,\; 32,\; 64,\; \ldots
    \]
    Tutti i termini sono positivi, in quanto \(r\) è positivo.
    
    \item Se \(a_1=4\) e \(r=-2\), la progressione diventa:
    \[
    4,\; -8,\; 16,\; -32,\; 64,\; \ldots
    \]
    In questo caso, i segni dei termini si alternano.
\end{itemize}

Questa proprietà risulta particolarmente utile in diverse applicazioni, ad esempio in fisica per lo studio di fenomeni oscillatori o in elettronica per l'analisi di segnali alternanti.

\subsubsection*{Monotonia della Progressione}
La monotonia di una progressione geometrica dipende dal valore della ragione \(r\):
\begin{itemize}
    \item Se \(r > 1\), la progressione è \textit{crescente}; ogni termine è maggiore del precedente, portando a una crescita esponenziale.
    \item Se \(0 < r < 1\), la progressione è \textit{decrescente}; i termini si avvicinano progressivamente a zero.
    \item Se \(r < 0\), la progressione non è monotona, poiché i segni dei termini oscillano tra positivo e negativo, impedendo una crescita o decrescita uniforme.
\end{itemize}

\textbf{Esempi:}
\begin{itemize}
    \item Con \(a_1=5\) e \(r=2\), la progressione è:
    \[
    5,\; 10,\; 20,\; 40,\; 80,\; \ldots
    \]
    ed è crescente.
    
    \item Con \(a_1=5\) e \(r=0.5\), la successione diventa:
    \[
    5,\; 2.5,\; 1.25,\; 0.625,\; 0.3125,\; \ldots
    \]
    ed è decrescente, tendendo a zero.
    
    \item Con \(a_1=5\) e \(r=-2\), otteniamo:
    \[
    5,\; -10,\; 20,\; -40,\; 80,\; \ldots
    \]
    che mostra un comportamento alternato.
\end{itemize}

Comprendere la monotonia di una progressione geometrica è fondamentale per prevedere il comportamento delle serie numeriche in vari contesti, come il calcolo degli interessi composti in economia o lo studio della crescita delle popolazioni in biologia.

\subsubsection*{Somma dei Primi \(n\) Termini}
La somma \(S_n\) dei primi \(n\) termini di una progressione geometrica si calcola con la formula:
\[
S_n = a_1 \cdot \frac{1 - r^n}{1 - r}, \quad \text{se } r \neq 1.
\]
Questa formula risulta particolarmente utile in ambiti quali la finanza (ad esempio, nel calcolo degli interessi composti) e in fisica (per l'analisi di onde e vibrazioni).\\
\noindent
\textbf{Esempio:} consideriamo una progressione geometrica con \(a_1=2\) e \(r=3\). Vogliamo determinare la \textit{somma} dei primi \(4\) termini. Applicando la formula
\[
S_n = a_1 \cdot \frac{1 - r^n}{1 - r},
\]
si ottiene
\[
S_4 = 2 \cdot \frac{1 - 3^4}{\,1 - 3\,}
= 2 \,\cdot \frac{1 - 81}{\,-2\,}
= 2 \,\cdot \frac{-80}{-2}
= 2 \,\times 40
= 80.
\]
I primi 4 termini della successione (\(2,\; 6,\; 18,\; 54\)) sommano infatti a \(80\). 
\newpage
\subsectionstar{Approfondimenti sulle Progressioni}
In questo documento si affronta il tema delle progressioni aritmetiche, illustrando due approcci principali per interpretarle. Il primo approccio è quello \textbf{indicizzato}, dove la successione viene definita in base ad un indice naturale, mentre il secondo approccio è quello \textbf{iterativo}, che parte da un valore iniziale $k$ e definisce la successione attraverso l'applicazione ripetuta di una funzione.

Nel primo approccio, le progressioni sono espresse mediante una successione indicizzata, per esempio:
\[
f(1),\quad f(2),\quad f(3),\quad \ldots
\]
dove ogni termine $f(n)$ è definito in funzione del suo indice $n$. Questo metodo risulta particolarmente intuitivo per rappresentare sequenze in cui il termine generale è direttamente legato all'indice, come ad esempio la tabellina del 5:
\[
f(1)=5,\quad f(2)=10,\quad f(3)=15,\quad f(4)=20,\quad \ldots
\]
qui si nota come il termine $f(n)$ possa essere espresso come
\[
f(n) = 5 \cdot n.
\]
Questo rappresenta chiaramente il metodo indicizzato, in cui ogni termine dipende esplicitamente da un indice.

Nel secondo approccio, detto \textbf{iterativo}, si parte da un valore iniziale $k$ e la successione viene definita applicando ripetutamente una funzione, per esempio:
\[
f(k),\quad f(f(k)),\quad f(f(f(k))),\quad \ldots
\]
Un esempio di questo metodo è l'iterazione che parte da un valore iniziale, ad esempio $k=0$, e ad ogni passo si aggiunge 5:
\[
\begin{array}{rcl}
f(0) &=& 0, \\
f(f(0)) &=& 5, \\
f(f(f(0))) &=& 10, \\
f(f(f(f(0)))) &=& 15, \\
&\vdots&
\end{array}
\]
Questi esempi evidenziano come la stessa progressione (ad esempio la tabellina del 5) possa essere interpretata sia tramite l'approccio indicizzato, sia tramite quello iterativo. Ciascun metodo presenta vantaggi specifici: l'approccio indicizzato è utile quando si ha una formula esplicita in funzione dell'indice, mentre l'approccio iterativo si rivela più naturale in contesti in cui la successione è definita tramite la relazione di ricorrenza, ovvero dipende direttamente dal termine precedente.

È importante sottolineare che, nella pratica, le successioni possono essere molto più complesse e non si limitano semplicemente a dipendere dal termine precedente. In questo contesto, la funzione \( f \) considerata può essere qualunque funzione; infatti, la nostra formazione matematica ci insegna che esistono molte tipologie di funzioni, anche definite su numeri reali (che includono numeri con la virgola, frazioni, numeri negativi, ecc.). Tuttavia, è fondamentale precisare che, se utilizziamo l'approccio indicizzato, la funzione deve essere definita su un sottoinsieme discreto, tipicamente i numeri naturali, poiché consideriamo un passaggio ad ogni passo successivo, senza includere infiniti valori intermedi. Al contrario, nell'approccio iterativo, la funzione può essere presa in tutta la sua generalità, includendo funzioni polinomiali, radicali, esponenziali, logaritmiche e altre, che in linea teorica potrebbero apparire in molti contesti matematici, anche se nella pratica spesso ci si limita alle forme più semplici. Tra queste, le funzioni polinomiali rappresentano un esempio fondamentale. È noto che la forma grafica di una funzione polinomiale dipende fortemente dal suo grado; le funzioni lineari, ovvero i polinomi di primo grado, sono tipicamente esemplificate dalla formula
\[
f(n)=an+b,
\]
ma non mancano esempi di funzioni di grado superiore, come quelle di secondo, terzo grado e oltre. Queste osservazioni saranno approfondite in seguito, nella parte algebrica, quando si affronteranno sistemi di equazioni di secondo grado, l'equazione della retta e altre applicazioni correlate.

Un ulteriore esempio emblematico è la sequenza di Fibonacci, che, sebbene non sia aritmetica, rappresenta una delle successioni più note. La sequenza di Fibonacci è definita brevemente da:
\[
F(1)=1,\quad F(2)=1,\quad F(n)=F(n-1)+F(n-2) \quad \text{per } n\geq 3.
\]

E quindi otteniamo:
% I primi 15 valori della sequenza di Fibonacci, considerando F(1)=1, F(2)=1
\[
1,\quad 1,\quad 2,\quad 3,\quad 5,\quad 8,\quad 13,\quad 21,\quad 34,\quad 55,\quad 89,\quad 144,\quad 233,\quad 377,\quad 610.
\]
Questa sequenza, con radici storiche risalenti al Medioevo, ha numerose applicazioni in matematica, natura e informatica, vedi \hro{TED Talk}{https://www.youtube.com/watch?v=SjSHVDfXHQ4}. È importante comprendere come diverse tipologie di successioni, inclusa quella di Fibonacci, possano ispirare lo studio di altre sequenze aritmetiche o ricorrenti.

Infine, è utile ricordare alcuni consigli pratici: conoscere le sequenze fondamentali può semplificare notevolmente la risoluzione di problemi matematici. Ad esempio, la sequenza degli esponenti di 2:
\[
2, \; 4, \; 8, \; 16, \; 32, \; 64, \; 128, \; 256, \; 512, \; 1024,
\]
e la sequenza dei quadrati:
\[
1, \; 4, \; 9, \; 16, \; 25, \; 36, \; 49, \; 64, \; 81, \; 100, \; 121, \; 144, \; 169, \; 196, \; 225,
\]
sono esempi che illustrano come la familiarità con tali sequenze possa essere estremamente utile. Comprendere le caratteristiche di queste successioni, sia in forma indicizzata che iterativa, permette di scegliere l'approccio più appropriato a seconda del contesto e della natura del problema da affrontare.
\newpage

\section{Probabilità}
Prima di entrare nella sostanza matematica che sarà essenziale per la preparazione in probabilità, porto un'introduzione al concetto filosofico di probabilità per mostrare quanto delle semplici proposizioni riguardanti la probabilità nascondano spesso un signficicato molto complesso da capire con precisione.

Il concetto di probabilità non è affatto semplice da definire in maniera generale, poiché il significato di probabilità può variare notevolmente a seconda del contesto. In linea di massima, tuttavia, possiamo iniziare definendo la probabilità di una proposizione come il rapporto tra il numero dei casi favorevoli e il numero totale dei casi possibili. In altre parole, data una certa proposizione, la probabilità \( P \) si calcola mediante la formula
\[
P = \frac{\text{casi favorevoli}}{\text{casi totali}}.
\]

Questo significa che per ogni evento, è necessario identificare con precisione quali siano i casi in cui la proposizione risulta vera e quantificare l’insieme complessivo dei casi possibili. Tale approccio, seppur intuitivo, si rivela molto complicato in contesti reali. Ad esempio, consideriamo l’affermazione: "Vi è una probabilità del 70\% che nei prossimi 20 anni si verifichi un terremoto nel Sud Italia." In questo caso, risulta difficile comprendere cosa significhi esattamente che la probabilità sia del 70\%, poiché occorre definire quali siano i "casi totali" presi in considerazione e come distinguere casi estremamente simili tra loro.

Va inoltre osservato che, nelle applicazioni pratiche come quelle meteorologiche o sismiche, il calcolo delle probabilità si basa su modelli matematici estremamente complessi, i quali tengono conto di innumerevoli variabili. Al contrario, negli esercizi che affronteremo, ci concentreremo su modelli matematici molto più semplici, in cui i casi totali sono chiaramente dati e intuitivi. Il primo passo fondamentale, dunque, è avere una visione chiara dell’insieme dei casi possibili e della distinzione tra i casi favorevoli (quelli in cui la proposizione è vera) e il totale dei casi.

Un esempio emblematico che capiremo meglio nella lettura dei prossimi capitoli è quello del lancio dei due dadi.

\noindent
Nel lancio di due dadi a sei facce, la \textit{somma} dei valori ottenuti varia da 2 a 12. La distribuzione di probabilità di tali somme assume la forma di un istogramma “a campana”, poiché alcune somme (come 7) risultano più probabili di altre (come 2 o 12). Il grafico sottostante mostra la probabilità (sull’asse verticale) in funzione della somma (sull’asse orizzontale). Si osserva che la somma 7, ottenuta in 6 modi diversi, ha la probabilità più elevata \(\tfrac{6}{36}=\tfrac{1}{6}\), mentre 2 e 12 sono i casi più rari, con un’unica combinazione \(\bigl((1,1)\text{ o }(6,6)\bigr)\).

\begin{center}
\begin{tikzpicture}[scale=0.9, line cap=round, line join=round, yscale=4.5]
    % Definiamo i modi possibili per ogni somma (2..12)
    \pgfmathsetmacro{\WaysTwo}{1}
    \pgfmathsetmacro{\WaysThree}{2}
    \pgfmathsetmacro{\WaysFour}{3}
    \pgfmathsetmacro{\WaysFive}{4}
    \pgfmathsetmacro{\WaysSix}{5}
    \pgfmathsetmacro{\WaysSeven}{6}
    \pgfmathsetmacro{\WaysEight}{5}
    \pgfmathsetmacro{\WaysNine}{4}
    \pgfmathsetmacro{\WaysTen}{3}
    \pgfmathsetmacro{\WaysEleven}{2}
    \pgfmathsetmacro{\WaysTwelve}{1}

    % Asse x
    \draw[->] (1,0) -- (13,0) node[right] {\small Somma};
    % Asse y
    \draw[->] (1,0) -- (1,0.3) node[left] {\small Probabilità};

    % Dati in un array {sum, ways}
    % Creiamo un array manualmente
    \foreach \x/\ways in {2/\WaysTwo, 3/\WaysThree, 4/\WaysFour, 5/\WaysFive,
                          6/\WaysSix, 7/\WaysSeven, 8/\WaysEight, 9/\WaysNine,
                          10/\WaysTen, 11/\WaysEleven, 12/\WaysTwelve}{
        \pgfmathparse{\ways/36} % calcoliamo la probabilita'
        \let\prob=\pgfmathresult

        % Disegno del rettangolo da (x-0.4,0) a (x+0.4, prob)
        \draw[fill=blue!40] (\x-0.4,0) rectangle (\x+0.4,\prob);
        % Etichetta in alto
        \node[above] at (\x,\prob) {\small \(\frac{\ways}{36}\)};
    }

    % Tacche sull'asse x (2..12)
    \foreach \s in {2,...,12} {
      \draw (\s,0.0) -- (\s,-0.005);
      \node[below] at (\s,0) {\small \s};
    }
\end{tikzpicture}
\end{center}

\noindent
Il valore più frequente è 7, con probabilità \(\frac{6}{36}=\frac{1}{6}\), mentre 2 e 12 sono i casi più rari, con \(\frac{1}{36}\) di probabilità ciascuno. Somme intermedie, come 6 e 8, hanno probabilità \(\frac{5}{36}\), e così via, a formare la caratteristica forma “a campana” della distribuzione delle somme dei due dadi. 
\newpage


\subsectionstar{[27] Probabilità di un Evento}
\paragraph{Spazio Campione ed Eventi} Per iniziare a lavorare con la probabilità, definiamo innanzitutto lo \textit{spazio campione}, che indicheremo con \(S\). Esso rappresenta l’insieme di tutti i \textit{casi possibili} di un esperimento. Un \textit{evento} \(E\) è un \textit{sottoinsieme} di \(S\), ovvero un insieme di alcuni (o di tutti, o di nessuno) degli elementi dello spazio campione che soddisfano una certa proposizione o \textit{condizione} \(C\).

Come esempio, consideriamo il lancio di un dado a sei facce. Lo spazio campione è:
\[
S = \{1, 2, 3, 4, 5, 6\}.
\]
Se la nostra condizione \(C\) consiste nell’“ottenere un valore maggiore di 3”, l’evento corrispondente è:
\[
E = \{4, 5, 6\}.
\]
In questo caso, \(C\) è vero per i risultati 4, 5 o 6, ma non per 1, 2 o 3.

Quando si parla di \textit{probabilità} associata a un evento \(C\), ci si riferisce, in forma elementare, a:
\[
P(C) \;=\; \frac{\lvert E \rvert}{\lvert S \rvert},
\]
dove \(\lvert E \rvert\) è il numero di elementi dell’evento (cioè quanti risultati concretamente soddisfano la nostra condizione) e \(\lvert S \rvert\) è il numero di tutti i casi possibili. 

\paragraph{Eventi incompatibili e indipendenti}

Due eventi \(A\) e \(B\), entrambi sottoinsiemi di \(S\), si dicono:
\begin{itemize}
    \item \textit{Incompatibili} (o \textit{mutuamente esclusivi}) se \(A \cap B = \varnothing\), ossia non ci sono esiti che appartengono contemporaneamente a entrambi.
\item \textit{Compatibili} se \(A \cap B \neq \varnothing\), cioè esiste almeno un caso che rientra in entrambi.
\item \textit{Indipendenti} se il verificarsi di uno non influisce sulla probabilità dell’altro; in termini formali:
  \[
  P(A \cap B) \;=\; P(A)\cdot P(B).
  \]
  In caso contrario, gli eventi si definiscono \textit{dipendenti}.
\end{itemize}
\paragraph{Esempi}
Consideriamo l’esperimento di lanciare \textit{due} dadi a sei facce. Lo spazio campione è costituito dalle coppie \((x,y)\) con \(x,y \in \{1,2,3,4,5,6\}\), dunque
\[
\lvert S \rvert = 6 \times 6 = 36.
\]
Se vogliamo calcolare la probabilità di ottenere la somma pari a 4, l’evento è:
\[
E = \big\{(1,3),\,(2,2),\,(3,1)\big\},
\]
con \(\lvert E \rvert = 3\). La probabilità relativa è:
\[
P(\text{somma} = 4) \;=\; \frac{3}{36} \;=\; \frac{1}{12}.
\]

\subsubsection*{Dimostrare l'Indipendenza tra Eventi}
Consideriamo due dadi a sei facce, con spazio campione:
\[
S = \{(x,y) \mid x,y \in \{1,2,3,4,5,6\}\}, 
\quad \lvert S \rvert = 36.
\]
Definiamo i seguenti eventi:
\[
A = \{\,(x,y) \in S \mid x \text{ è pari}\},
\quad
B = \{\,(x,y) \in S \mid y \le 2\}.
\]
Nello specifico, l’evento \(A\) si verifica quando sul \textit{primo} dado esce un numero pari (\(2, 4\) o \(6\)), mentre l’evento \(B\) si verifica quando il \textit{secondo} dado mostra \(1\) o \(2\).
\[
\lvert A \rvert 
= 3 \times 6 \;=\; 18
\quad(\text{primo dado pari } \{2,4,6\}\text{, secondo dado qualunque } \{1,\dots,6\}),
\]
\[
\lvert B \rvert
= 6 \times 2 \;=\; 12
\quad(\text{primo dado qualunque } \{1,\dots,6\}\text{, secondo dado } \le 2 \text{ ovvero } \{1,2\}).
\]
Da cui
\[
P(A) = \frac{18}{36} = \frac{1}{2}, 
\quad
P(B) = \frac{12}{36} = \frac{1}{3}.
\]

Per trovare \(P(A \cap B)\), cioè la probabilità che il \textit{primo} dado sia pari \textit{e} il \textit{secondo} dado sia \(1\) o \(2\), contiamo le coppie \((x,y)\) dove \(x \in \{2,4,6\}\) e \(y \in \{1,2\}\):
\[
\lvert A \cap B \rvert 
= 3 \;\times\; 2 
= 6 
\quad\Longrightarrow\quad 
P(A \cap B) = \frac{6}{36} = \frac{1}{6}.
\]

Verifichiamo ora l’indipendenza di \(A\) e \(B\) confrontando \(P(A \cap B)\) con il prodotto \(P(A)\,P(B)\):
\[
P(A)\,P(B) 
= \frac{1}{2} \,\times\, \frac{1}{3} 
= \frac{1}{6},
\]
\[
P(A \cap B) 
= \frac{1}{6}.
\]
Poiché 
\[
P(A \cap B) = P(A)\,P(B),
\]
concludiamo che gli eventi \(A\) e \(B\) sono \textit{indipendenti}.
\subsubsection*{Proprietà delle Probabilità}
\begin{enumerate}
    \item \textbf{Additività}: se due eventi \(A\) e \(B\) sono \textit{incompatibili} (ossia \(A \cap B = \varnothing\)), allora
    \[
    P(A \cup B) \;=\; P(A) + P(B).
    \]
    In questo caso, la probabilità che si verifichi almeno uno dei due eventi è la somma delle probabilità di ciascun evento.

    \item \textbf{Complementarità}: data un evento \(A\) e il suo complementare \(A^c\), cioè l’evento “\(A\) non si verifica”, vale la relazione
    \[
    P(A^c) \;=\; 1 - P(A).
    \]
    Per esempio, se la probabilità che piova è 0,3, la probabilità che non piova è 0,7.

    \item \textbf{Moltiplicatività per eventi indipendenti}: se due eventi \(A\) e \(B\) sono \textit{indipendenti}, la probabilità che si verifichino entrambi è data dal prodotto delle loro probabilità:
    \[
    P(A \cap B) \;=\; P(A)\,P(B).
    \]
    Ad esempio, se la probabilità di ottenere “testa” lanciando una moneta è 0,5 e la probabilità di ottenere un 6 lanciando un dado è \(\tfrac{1}{6}\), la probabilità di ottenere contemporaneamente “testa” e un 6 è
    \[
    0,5 \times \frac{1}{6} = \frac{1}{12}.
    \]
\end{enumerate}
\newpage

\subsectionstar{[9] Calcolo Combinatorio}
Il calcolo combinatorio è quella branca della matematica che si occupa di contare, organizzare e disporre elementi di un insieme secondo determinate regole. È particolarmente utile in problemi di probabilità, statistica e informatica.

\begin{itemize}
    \item \textit{Fattoriale di un numero}: indicato con \(n!\), rappresenta il prodotto dei numeri interi positivi da \(1\) a \(n\). Formalmente:
    \[
    n! = n \times (n-1) \times (n-2) \times \cdots \times 1,
    \]
    con la convenzione \(0! = 1\).

    \item \textit{Principio fondamentale del conteggio}: se un evento può avvenire in \(m\) modi e un altro evento in \(n\) modi, allora la sequenza di entrambi gli eventi può avvenire in \(m \times n\) modi.
\end{itemize}

Le \textit{disposizioni} (o \textit{arrangiamenti}) riguardano i modi di ordinare un certo numero di elementi di un insieme, senza necessariamente utilizzare l’intero insieme.

\paragraph{Disposizioni semplici.}
Le disposizioni \textit{semplici} di \(n\) elementi presi a gruppi di \(k\) (\(k \le n\)) sono date dalla formula:
\[
D_{n,k} = \frac{n!}{(n-k)!}.
\]
\textit{Esempio}: supponiamo di avere 5 lettere \(\{\text{A, B, C, D, E}\}\) e di voler formare sequenze di 3 lettere diverse. Le possibili disposizioni sono:
\[
D_{5,3} 
= \frac{5!}{(5-3)!}
= \frac{5!}{2!}
= \frac{120}{2} 
= 60.
\]

\paragraph{Disposizioni con ripetizione.}
Se gli elementi possono essere ripetuti, la formula diventa:
\[
D'_{n,k} = n^k.
\]
\textit{Esempio}: se vogliamo formare \textit{sequenze} di 2 lettere (quindi \(k=2\)) partendo da 3 diverse lettere \(\{\text{A, B, C}\}\) (\(n=3\)) con possibilità di ripetizione, si ottiene:
\[
D'_{3,2} = 3^2 = 9.
\]
Le 9 disposizioni, in cui l’ordine conta e le lettere possono ripetersi, sono:
\[
\{\text{AA, AB, AC, BA, BB, BC, CA, CB, CC}\}.
\]

\paragraph{Permutazioni.}
Le \textit{permutazioni} sono un caso particolare di disposizione in cui vengono utilizzati \textit{tutti} gli \(n\) elementi dell’insieme.

\paragraph{Permutazioni semplici.}
La formula per le permutazioni di \(n\) elementi distinti è:
\[
P_n = n!.
\]
\textit{Esempio}: quante diverse \textit{permutazioni} è possibile formare con le lettere \(\{\text{A, B, C}\}\)?
\[
P_3 = 3! = 6.
\]
Le possibili permutazioni sono: \(\text{ABC, ACB, BAC, BCA, CAB, CBA}\).

\paragraph{Permutazioni con ripetizioni.}
Se in una collezione di \(n\) elementi alcuni si ripetono più volte, la formula per le \textit{permutazioni distinte} è:
\[
P_{n}^{a,b,\dots}
= \frac{n!}{a!\,b!\,\cdots},
\]
dove \(a, b, \dots\) sono le molteplicità dei vari elementi ripetuti.

\textit{Esempio}: quante permutazioni \textit{distinte} si possono formare con la parola \(\text{MAMMA}\)? Le lettere sono 5 in totale: \(\{\text{M, A, M, M, A}\}\), in cui \(\text{M}\) compare 3 volte e \(\text{A}\) 2 volte. Si ha
\[
\frac{5!}{3!\,2!} 
= \frac{120}{6 \times 2} 
= 10.
\]

\paragraph{Combinazioni.}
Le \textit{combinazioni} riguardano i gruppi di elementi in cui l’ordine non conta.

\paragraph{Combinazioni semplici.}
La formula per le combinazioni di \(n\) elementi presi a gruppi di \(k\) è:
\[
C_{n,k} 
= \binom{n}{k}
= \frac{n!}{k!\,(n-k)!}.
\]
\textit{Esempio}: quanti \textit{gruppi} di 3 lettere si possono formare con \(\{\text{A, B, C, D, E}\}\), senza considerare l’ordine?
\[
C_{5,3} 
= \binom{5}{3}
= \frac{5!}{3!\,2!}
= 10.
\]
I gruppi possibili sono: \small\[\{\text{A, B, C}\}, \{\text{A, B, D}\}, \{\text{A, B, E}\}, \{\text{A, C, D}\}, \{\text{A, C, E}\}, \{\text{A, D, E}\}, \{\text{B, C, D}\}, \{\text{B, C, E}\}, \{\text{B, D, E}\}, \{\text{C, D, E}\}\]
\normalem
\paragraph{Combinazioni con ripetizione.}
Se gli elementi possono \textit{ripetersi}, la formula diventa:
\[
C'_{n,k} 
= \binom{n + k - 1}{k} 
= \frac{(n+k-1)!}{k!\,(n-1)!}.
\]
\textit{Esempio}: supponiamo di avere 2 tipi di caramelle (ad esempio gusto \textit{Fragola} e gusto \textit{Menta}) e di voler formare \textit{gruppi} di 3 caramelle, \textit{senza} curarci dell’ordine e ammettendo che una caramella possa ripetersi più volte. Qui \(n=2\) e \(k=3\). Calcoliamo:
\[
C'_{2,3} 
= \binom{2 + 3 - 1}{3}
= \binom{4}{3}
= \frac{4!}{3!\,1!}
= 4.
\]
I possibili gruppi sono:
\[
\{\text{F, F, F}\}, 
\quad \{\text{F, F, M}\}, 
\quad \{\text{F, M, M}\}, 
\quad \{\text{M, M, M}\}.
\]
\newpage

\subsectionstar{[18] Frequenza Relative ed Assoluta e le Rappresentazioni Grafiche}
\paragraph{Frequenza Assoluta.}
La \textit{frequenza assoluta} di un dato rappresenta quante volte esso compare all’interno di un insieme di osservazioni. Se un dato \(x\) compare \(f\) volte, allora \(f\) è la frequenza assoluta di \(x\).

\textit{Esempio}: in una classe di 30 studenti, se il voto “8” compare 6 volte, la frequenza assoluta di “8” è \(6\).

\paragraph{Frequenza Relativa.}
La \textit{frequenza relativa} di un dato si ottiene dividendo la sua frequenza assoluta per il numero totale di osservazioni:
\[
\text{Frequenza relativa} 
\;=\; 
\frac{\text{Frequenza assoluta}}{\text{Numero totale di osservazioni}}.
\]
\textit{Esempio}: nel caso precedente, la frequenza relativa del voto “8” è
\[
\frac{6}{30} \;=\; 0{,}2,
\]
ovvero il 20\% degli studenti ha ottenuto quel voto.

\noindent
In generale, la \textit{frequenza assoluta} risulta utile quando si desidera evidenziare \textit{il numero concreto} di volte in cui un dato compare (ad esempio, quanti studenti hanno preso un certo voto). D’altro canto, la \textit{frequenza relativa} permette di confrontare i dati in termini \textit{percentuali} o \textit{proporzionali} rispetto al totale (per esempio, la quota percentuale di studenti con quel voto), risultando particolarmente significativa se si mettono a paragone gruppi di dimensioni diverse. 

\subsubsection*{Rappresentazioni Grafiche di un’Indagine Statistica}

\paragraph{Ideogrammi.}
Gli ideogrammi rappresentano i dati tramite \textit{simboli} o \textit{icone}, ciascuno dei quali corrisponde a una determinata quantità. Nell’immagine allegata, per esempio, viene mostrata la popolazione di alcune province calabresi (Cosenza, Vibo Valentia, Catanzaro, Reggio Calabria, Crotone) utilizzando omini stilizzati. Ogni omino corrisponde, ad esempio, a \(\mathbf{100{.}000}\) abitanti. Il numero di omini impiegati per ogni provincia è proporzionale al numero di abitanti di tale provincia.

\begin{center}
\includegraphics[width=0.3\textwidth]{IMG_0773.jpeg}
\end{center}

In questo modo, si ottiene una rappresentazione visiva immediata: più è alto il numero di omini, maggiore è la popolazione di quella provincia. Ad esempio, se una provincia ha il doppio degli omini rispetto a un’altra, si comprende a colpo d’occhio che ha all’incirca il doppio degli abitanti. È importante anche notare che il numero di icone non deve necessariamente essere intero, è infatti possibile rappresentarne la metà o diverse altre frazioni intermedie.

\paragraph{Istogrammi.}
Gli \textit{istogrammi} rappresentano la distribuzione di dati quantitativi, raggruppati in classi o categorie, mediante rettangoli la cui altezza è proporzionale alla frequenza o al valore associato a ciascuna categoria. Nella figura seguente sono rappresentati i consumi di tre categorie di alimenti (carne, pesce, latticini) in quattro Regioni italiane (Puglia, Veneto, Lazio, Umbria). 

\begin{center}
\includegraphics[width=0.5\textwidth]{IMG_0776.jpeg}
\end{center}

Ogni gruppo di barre corrisponde a una Regione, mentre il colore di ciascuna barra indica la tipologia di alimento. I valori esatti mostrati nell'istogramma possono essere riassunti nella seguente tabella:

\[
\begin{array}{c|ccc}
\textbf{Regione} & \textbf{Carne} & \textbf{Pesce} & \textbf{Latticini} \\
\hline
\text{Puglia} & 40 & 80 & 30 \\
\text{Veneto} & 70 & 30 & 90 \\
\text{Lazio}  & 50 & 70 & 60 \\
\text{Umbria} & 90 & 20 & 40 \\
\end{array}
\]

In questo modo, l’istogramma rende immediato il confronto tra le diverse categorie di alimenti (sull’asse verticale) e tra le varie Regioni (sull’asse orizzontale). L’altezza di ciascuna barra misura la quantità rilevata nella specifica categoria e Regione.

\paragraph{Ortogrammi.}
Gli ortogrammi (o \textit{diagrammi a barre}) si utilizzano principalmente per rappresentare dati \textit{qualitativi} o \textit{quantitativi discreti}. A differenza di un istogramma, in cui gli intervalli dell’asse orizzontale (le classi) sono adiacenti e formano un continuum, nell’ortogramma le categorie non hanno continuità tra loro e le barre risultano separate. In pratica, un istogramma che mostra distribuzioni di variabili continue, se “ruotato” (invertendo gli assi delle ascisse e delle ordinate) e modificato in modo che ogni categoria sia chiaramente distinta, può essere considerato un ortogramma. L’idea di base è che, laddove le categorie non seguano un andamento continuo (come gli intervalli di classi), ma siano valori discreti o attributi qualitativi, l’ortogramma risulta lo strumento preferito per la rappresentazione grafica.

\noindent \textbf{Rappresentare Frequenza Relativa o Assoluta}

Gli \textit{ideogrammi} rappresentano i dati tramite \textit{icone} o \textit{simboli}, ciascuno dei quali corrisponde a un certo numero di unità (persone, oggetti, ecc.). Si possono usare \textit{sia} con frequenze assolute \textit{sia} con frequenze relative, ma sono più immediati da interpretare quando si vuol dare un colpo d’occhio ai \textit{valori concreti} (frequenze assolute). Nell'esempio sopra abbiamo rappresentato la frequenza assoluta.

Gli \textit{istogrammi} si utilizzano per dati \textit{continui}, suddivisi in \textit{classi} adiacenti. Le barre hanno basi contigue (senza spazi) e l’area di ciascuna barra è proporzionale alla frequenza. Anche qui, la scelta tra frequenze assolute o relative dipende da come si desidera interpretare l’altezza delle barre (numero di occorrenze \textit{vs} percentuale sul totale). Nell'esempio sopra abbiamo rappresentato la frequenza relativa.

Gli \textit{ortogrammi} (o \textit{diagrammi a barre}) mostrano dati qualitativi o discreti con barre \textit{separate}, la cui altezza (o lunghezza) può esprimere \textit{frequenze assolute} (se si vuol sottolineare “quante volte” un dato appare) oppure \textit{frequenze relative} (per evidenziare la quota percentuale).

\newpage

\section{Algebra}
\noindent
\textbf{Introduzione all’Algebra}

\smallskip
\noindent
L’\textit{Algebra} è quella parte della matematica che studia \textbf{equazioni}, \textbf{polinomi} e le relazioni tra quantità variabili. Nel corso di questa sezione, ci concentreremo in particolare sull’analisi di \textit{polinomi} di vario grado (e sulla loro scomposizione mediante i \textit{prodotti notevoli}), nonché sulla risoluzione di \textit{equazioni} ed \textit{inequazioni} in forme diverse. Ricordiamo che i \textit{prodotti notevoli} costituiscono un insieme di formule fondamentali che permettono di scomporre e manipolare velocemente le espressioni algebriche. Elenco successivamente i prodotti notevoli più importanti, è necessario per comprendere a pieno gli esempi che seguiranno ricordare chiaramente queste equazioni. Nel caso in cui non le si avesse affrontate già in passato, il loro significato sarà più chiaro una volta dopo aver letto i primi due argomenti di questa sezione.

\smallskip
\noindent
Nel dettaglio, affronteremo i \textbf{polinomi} (somme di monomi), la loro \textit{fattorizzazione} e le tecniche di \textit{semplificazione}, per poi passare allo studio di \textit{equazioni} di vario grado e \textit{disequazioni} che richiedono metodi più o meno avanzati. L’Algebra ci offre quindi un linguaggio simbolico per descrivere, analizzare e risolvere problemi che vanno dalle semplici equazioni di primo grado a situazioni più complesse che incontreremo successivamente anche in geometria analitica. 


\paragraph{Prodotti notevoli: introduzione generale all’Algebra.}
Prima di addentrarci nello studio di equazioni, disequazioni e altri argomenti più avanzati, è fondamentale richiamare i principali \textit{prodotti notevoli}, che costituiscono una risorsa essenziale per la semplificazione e la manipolazione delle espressioni algebriche. Nel prosieguo dei capitoli, infatti, daremo per \textit{acquisite} queste formule, utilizzandole spesso in modo diretto per fattorizzare, risolvere o verificare calcoli.

\begin{itemize}
    \item \(\mathbf{(a + b)^2 = a^2 + 2ab + b^2}\).
    \item \(\mathbf{(a - b)^2 = a^2 - 2ab + b^2}\).
    \item \(\mathbf{(a + b)(a - b) = a^2 - b^2}\).
    \item \(\mathbf{(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3}\).
    \item \(\mathbf{(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3}\).
    \item \(\mathbf{a^3 + b^3 = (a + b)(a^2 - ab + b^2)}\).
    \item \(\mathbf{a^3 - b^3 = (a - b)(a^2 + ab + b^2)}\).
\end{itemize}

Queste identità, pur non appartenendo esclusivamente al tema delle \textit{equazioni irrazionali} o di un singolo argomento, sono \textit{trasversali} e di grande utilità in tutto lo \textit{studio dell’Algebra}. Avere dimestichezza con i prodotti notevoli è fondamentale per effettuare scomposizioni, risolvere equazioni di vario grado, analizzare il segno di un’espressione e molto altro ancora. Saranno quindi ripetutamente impiegati negli esempi e negli esercizi delle sezioni successive. 
\newpage

\subsectionstar{[13] Equazioni Intere e Fratte}
\paragraph{Equazioni intere e cenni sui Polinomi}

\paragraph{Polinomi.}
In matematica, un \textit{polinomio} è un’espressione formata da una somma (o differenza) di \textit{termini}, ciascuno dei quali è il prodotto di una costante (un numero intero, reale o complesso, a seconda del contesto) e di variabili elevate a potenze intere non negative. Nel caso dei numeri interi, possiamo pensare a un generico polinomio in una variabile \(x\) come:
\[
p(x) \;=\; a_n\,x^n + a_{n-1}\,x^{n-1} \;+\; \cdots \;+\; a_1\,x + a_0,
\]
dove \(a_0, a_1, \dots, a_n\) sono numeri interi e \(n\) rappresenta il \textit{grado} del polinomio (posto che \(a_n \neq 0\)). Se \(n=1\) parliamo di un polinomio di \textit{primo grado}, se \(n=2\) di \textit{secondo grado}, e così via.

\paragraph{Equazioni polinomiali.}
Un’equazione polinomiale di grado \(n\) in una variabile \(x\) ha la forma:
\[
p(x) = 0,
\]
dove \(p(x)\) è un polinomio di grado \(n\). L’insieme delle soluzioni (cioè i valori di \(x\) che soddisfano l’uguaglianza) dipende dal grado e dai coefficienti del polinomio stesso. In generale, \textit{un polinomio di grado \(n\) può avere al più \(n\) soluzioni reali} (o complesse, se consideriamo l’insieme dei numeri complessi).

\paragraph{Equazioni di primo grado.}
Le equazioni di primo grado sono del tipo:
\[
a_1\,x + a_0 = 0, 
\]
dove \(a_1 \neq 0\). Per risolvere questa equazione, si isola la variabile \(x\) con i passaggi algebrici di base:
\[
a_1\,x = -\,a_0
\quad\Longrightarrow\quad
x = -\,\frac{a_0}{a_1}.
\]
\textit{Esempio}: risolviamo \(2x + 4 = 0\). Spostando \(4\) a destra, otteniamo:
\[
2x = -4 
\quad\Longrightarrow\quad
x = -2.
\]

\paragraph{Equazioni di secondo grado.}
Le equazioni di secondo grado si presentano nella forma:
\[
a_2\,x^2 + a_1\,x + a_0 = 0,
\quad
a_2 \neq 0.
\]
Per risolverle, si utilizza la \textit{formula risolutiva}, fondata sul \(\Delta\) (o \textit{discriminante}):
\[
\Delta = a_1^2 - 4\,a_2\,a_0.
\]
\[
x = \frac{-\,a_1 \;\pm\; \sqrt{\Delta}}{2\,a_2}.
\]
Il numero di soluzioni dipende dal segno di \(\Delta\):
\begin{itemize}
    \item \(\Delta > 0\): due soluzioni distinte.
    \item \(\Delta = 0\): una sola soluzione (o soluzione doppia).
    \item \(\Delta < 0\): nessuna soluzione reale (due soluzioni complesse coniugate).
\end{itemize}

\textit{Esempio}: risolviamo \(x^2 - 5x + 4 = 0\). Calcoliamo il discriminante:
\[
\Delta = (-5)^2 - 4 \cdot 1 \cdot 4 = 25 - 16 = 9.
\]
Poiché \(\Delta = 9 > 0\), abbiamo due soluzioni:
\[
x = \frac{5 \pm \sqrt{9}}{2} 
= \frac{5 \pm 3}{2}.
\]
Ne derivano \(x_1 = \tfrac{8}{2} = 4\) e \(x_2 = \tfrac{2}{2} = 1\).

\paragraph{Equazioni di grado superiore.}
Per \textit{terzo} e \textit{quarto} grado (e oltre) esistono formule risolutive \textit{generali}, ma risultano molto complesse da utilizzare. In molti casi pratici, si preferisce procedere con metodi di fattorizzazione e riduzione a equazioni di secondo grado. Se ad esempio un’equazione di terzo grado ammette come fattore un binomio lineare (per esempio \(x\), oppure \((x-1)\), ecc.), la si può scomporre e convertire il problema a un’equazione di grado inferiore.

\paragraph{Esempi di equazioni di terzo grado semplificate.}

\textit{Esempio 1}: \(x^3 - 4x = 0\).

    Qui si nota che ogni termine contiene un fattore \(x\):
    \[
    x\,(x^2 - 4) = 0.
    \]
    Dunque la prima radice è \(x=0\). Il restante fattore \(x^2 - 4\) si risolve come un’equazione di secondo grado:
    \[
    x^2 - 4 = 0 
    \;\;\Longrightarrow\;\; x^2 = 4 
    \;\;\Longrightarrow\;\; x = \pm 2.
    \]
    In totale, abbiamo 3 soluzioni reali: \(\{\,0, -2, 2\}.\)

\textit{Esempio 2}: \(x^3 - x^2 = 0\).

    Anche qui è possibile estrarre un \(x^2\):
    \[
    x^2(x - 1) = 0.
    \]
    Le soluzioni sono \(x=0\) (con molteplicità 2, quindi “soluzione doppia”) e \(x=1\).

\textit{Esempio 3}: \(2x^3 - 6x = 0\).

    Raccolta in evidenza:
    \[
    2x(x^2 - 3) = 0,
    \]
    da cui \(x=0\) oppure \(x=\pm\sqrt{3}\).

Al di fuori di questi casi relativamente semplici, la risoluzione di equazioni di grado superiore richiede metodi più avanzati (come la formula di Cardano per il terzo grado), che tuttavia vanno oltre il livello di complessità trattato qui. Nella pratica, quando si incontrano polinomi di grado 3 o 4, spesso si ricorre a fattorizzazioni, trasformazioni specifiche o all’ausilio di calcoli numerici, se non si presentano già in forme facilmente riconducibili a fattori di primo o secondo grado.

\paragraph{Equazioni frazionarie (o razionali).}
Oltre alle equazioni \textit{intere} (ossia polinomiali), possiamo incontrare equazioni in cui compaiono \textit{frazioni} con polinomi al numeratore e al denominatore. La forma generale è:
\[
\frac{P(x)}{Q(x)} = 0,
\]
dove \(P(x)\) e \(Q(x)\) sono polinomi. Per risolvere un’equazione di questo tipo, si procede osservando che:
\[
\frac{P(x)}{Q(x)} = 0
\quad\Longleftrightarrow\quad
P(x) = 0 
\quad\text{e}\quad
Q(x) \neq 0.
\]
In altre parole, una frazione è nulla soltanto quando il \textit{numeratore} è zero, \textit{purché} il \textit{denominatore} non sia zero (altrimenti l’espressione non è definita).

Nel caso in cui l’equazione sia più complessa, ad esempio
\[
\frac{P(x)}{Q(x)} = R(x),
\]
per risolverla è tipico moltiplicare entrambi i membri per \(Q(x)\), ottenendo un’equazione polinomiale in \(x\). Contemporaneamente, \textit{dobbiamo imporre} che \(Q(x)\neq 0\), poiché la moltiplicazione per \(Q(x)\) sarebbe altrimenti priva di senso. Al termine della risoluzione, è necessario verificare che le soluzioni trovate non annullino il denominatore, escludendo quelle che rendono \(Q(x)=0\).

Un ragionamento analogo si adotta per le \textit{disequazioni} frazionarie, imponendo in ogni passaggio le condizioni di non annullamento del denominatore e verificando la validità delle soluzioni finali.

\newpage
\subsectionstar{[13 - 7] Disequazioni Intere e Fratte}
\paragraph{Introduzione alle disequazioni.}
Oltre alle equazioni, in cui cerchiamo i valori di \(x\) che rendono un’espressione \textit{uguale} a zero (o a un’altra espressione), è fondamentale imparare a risolvere le \textit{disequazioni} (o \textit{inequazioni}), ovvero quelle espressioni in cui compare un segno di \(<\), \(\le\), \(>\) o \(\ge\). Ad esempio:
\[
x^2 - 5x + 4 \;<\; 0,
\quad\text{o}\quad
\frac{P(x)}{Q(x)} \;\ge\; 0.
\]

\subparagraph{Intervalli e notazione.}
Il \textit{risultato} di una disequazione è un insieme di valori di \(x\), spesso descritti attraverso \textit{intervalli} sulla retta reale. Quando includiamo un estremo nell’intervallo, utilizziamo la parentesi \textbf{quadra} \([\,\,]\); se l’estremo non appartiene all’insieme, utilizziamo la parentesi \textbf{tonda} \((\,\,)\). Ad esempio:
\[
x \;\in\; [-1,\,3)
\]
significa che \(x\) può assumere valori da \(-1\) \textit{compreso} fino a \(3\) \textit{escluso}.

\subparagraph{Metodi per risolvere le disequazioni.}
Le strategie per le disequazioni \textit{polinomiali} o \textit{frazionarie} spesso ricalcano il seguente schema generale:
\begin{enumerate}
    \item \textbf{Individuare i punti critici.} Questi includono gli \textit{zeri} dei polinomi al numeratore (dove l’espressione può cambiare di segno) e i valori che annullano il denominatore (ove l’espressione non è definita). 
    \item \textbf{Suddividere la retta in intervalli.} I punti critici dividono la retta reale in vari intervalli aperti: ad esempio, se i punti critici sono \(x_1\) e \(x_2\) con \(x_1 < x_2\), la retta viene divisa negli intervalli \((-\infty, x_1)\), \((x_1, x_2)\) e \((x_2, +\infty)\).
    \item \textbf{Determinare il segno dell’espressione in ciascun intervallo.} Può essere fatto valutando un \textit{punto di test} all’interno di ogni intervallo (la cosiddetta \textit{analisi del segno}), oppure osservando la \textit{struttura} di fattori nel numeratore e nel denominatore.
    \item \textbf{Individuare gli intervalli di soluzione.} In base al segno richiesto (\(<0\), \(\le0\), \(>0\), \(\ge0\)), si selezionano gli intervalli in cui l’espressione soddisfa la disequazione, \textit{controllando} se includere o escludere i punti critici. 
        \begin{itemize}
            \item Se la disequazione è \(\le 0\) o \(\ge 0\), si può includere un punto critico \textit{solo} se l’espressione è definita in quel punto \textit{e} se risulta effettivamente uguale a 0 in quel punto.
            \item Se è \(<0\) o \(>0\), i punti in cui l’espressione si annulla (o non è definita) vanno esclusi.
        \end{itemize}
\end{enumerate}

\noindent \textbf{Esempio di analisi del segno.}
Se dobbiamo risolvere
\[
x^2 - 5x + 4 \;<\; 0,
\]
procediamo come per un’equazione, trovando gli zeri:
\[
x^2 - 5x + 4 = 0 \quad\Longrightarrow\quad (x - 4)(x - 1) = 0,
\]
che fornisce \(x = 1\) e \(x = 4\). Tali punti dividono la retta in tre intervalli: \((-\infty, 1)\), \((1, 4)\) e \((4, +\infty)\). Analizziamo il segno di \((x - 4)(x - 1)\) in ciascun intervallo:
\[
\begin{array}{lcl}
x < 1 &\Longrightarrow& (x-1)<0 \text{ e } (x-4)<0,\text{ quindi il prodotto è }(-)\cdot(-) = (+)\\[6pt]
1 < x < 4 &\Longrightarrow& (x-1)>0 \text{ e } (x-4)<0,\text{ quindi il prodotto è } (-). \\[6pt]
x > 4 &\Longrightarrow& (x-1)>0 \text{ e } (x-4)>0,\text{ quindi il prodotto è } (+).
\end{array}
\]
Si verifica così che l’espressione \((x-4)(x-1)\) è negativa solo nell’intervallo \((1,4)\). Di conseguenza:
\[
x^2 - 5x + 4 \;<\; 0
\quad\Longrightarrow\quad
x \in (1,\,4).
\]

Questo approccio, basato sull’individuazione degli zeri e sull’analisi del segno nei vari intervalli, si applica in modo analogo alle disequazioni frazionarie, tenendo presente l’ulteriore condizione che il denominatore non deve essere nullo in alcun punto delle soluzioni. 

\paragraph{Disequazioni frazionarie: l’analisi del segno.}
Quando affrontiamo una \textit{disequazione frazionaria}, ad esempio
\[
\frac{P(x)}{Q(x)} > 0
\quad\text{oppure}\quad
\frac{P(x)}{Q(x)} < 0,
\]
dobbiamo tenere conto sia degli \textit{zeri} di \(P(x)\) (il numeratore) sia degli \textit{zeri} di \(Q(x)\) (il denominatore), che rappresentano punti di non definizione. La strategia di risoluzione segue questi passaggi:

\begin{enumerate}
    \item \textbf{Trova gli zeri di \(P(x)\).}  
    Se \(P(x) = 0\) ammette soluzioni \(x_1, x_2, \dots\), esse saranno punti in cui la frazione può cambiare segno.
    \item \textbf{Trova gli zeri (o punti di non definizione) di \(Q(x)\).}  
    Se \(Q(x) = 0\) ammette soluzioni \(y_1, y_2, \dots\), ciascuna di queste va esclusa dal dominio, poiché la frazione non è definita in tali punti. Questi stessi valori, però, dividono la retta in sottointervalli ed è spesso lì che il segno dell’espressione cambia.
    \item \textbf{Suddividi la retta in intervalli.}  
    Metti in ordine tutti i punti critici (zeri di \(P(x)\) e di \(Q(x)\)) e suddividi la retta reale in intervalli aperti determinati da tali punti.
    \item \textbf{Analizza il segno della frazione in ciascun intervallo.}  
    Per ogni intervallo, si sceglie un \textit{punto di prova} o si esamina direttamente la struttura del numeratore e del denominatore. In particolare:
    \begin{itemize}
        \item Se il \textit{numeratore} \(P(x)\) in un certo intervallo risulta positivo (o negativo) e il \textit{denominatore} \(Q(x)\) risulta anch’esso positivo (o negativo), la frazione \(\frac{P(x)}{Q(x)}\) avrà il segno corrispondente al prodotto dei segni di numeratore e denominatore.
        \item Ricorda che nei punti in cui \(Q(x) = 0\), la frazione è \textit{non definita} e dunque non potrà far parte delle soluzioni.
    \end{itemize}
    \item \textbf{Seleziona gli intervalli che soddisfano la disequazione.}  
    Infine, in base al segno richiesto (\(<0\), \(\le0\), \(>0\), \(\ge0\)), identifichi gli intervalli in cui la frazione verifica tale condizione. Verifica anche se i punti in cui \(P(x)=0\) possono o meno essere inclusi (ad esempio, nel caso di \(\ge0\) o \(\le0\)), mentre i punti in cui \(Q(x)=0\) vanno sempre esclusi.
\end{enumerate}

\paragraph{Esempio.}
Consideriamo la disequazione
\[
\frac{x^2 - 5x + 4}{x - 2} > 0.
\]
\begin{itemize}
    \item Il numeratore \(x^2 - 5x + 4\) si annulla per \(x=1\) e \(x=4\).  
    \item Il denominatore \(x - 2\) si annulla per \(x=2\), punto da escludere poiché rende la frazione non definita.  
    \item I punti critici sono quindi \(1,\,2,\,4\). Dividono la retta negli intervalli \((-\infty,1)\), \((1,2)\), \((2,4)\), \((4,+\infty)\).  
    \item In ciascun intervallo, verifichiamo il segno di \(P(x)\) e \(Q(x)\), e quindi della frazione.  
    \item Confrontando il risultato con il segno \((>0)\) richiesto, otteniamo la soluzione finale:  
    \[
    x \in (-\infty,\,1) \;\cup\; (1,\,2) \;\cup\; (4,\,+\infty).
    \]
\end{itemize}
In questo modo, abbiamo individuato gli intervalli in cui la frazione risulta positiva, escludendo il punto \(x=2\) dal dominio e verificando che \(x=1\) e \(x=4\) siano zeri del numeratore (\(P(x)=0\)), dunque non rendono la frazione strettamente positiva.

\newpage

\subsectionstar{[14] Equazioni e Disequazioni Irrazionali}
\paragraph{Equazioni irrazionali.}
Finora abbiamo affrontato principalmente \textit{equazioni polinomiali} (in cui le incognite compaiono con esponenti naturali) ed estensioni come le \textit{equazioni frazionarie} (in cui la variabile può apparire anche al denominatore). Possiamo spingerci oltre e introdurre le \textit{equazioni irrazionali}, in cui la variabile \(x\) compare \textit{all’interno di una radice} (radice quadrata, cubica, ecc.) o in generale con esponenti \textit{razionali}. Questo rispecchia la progressiva generalizzazione delle potenze, che dai naturali si estendono agli interi (introducendo le “parti frazionarie”) e successivamente ai razionali (introducendo le radici).

\subparagraph{Dominio di definizione.}
La prima operazione fondamentale nella risoluzione di un’equazione irrazionale è stabilire il \textit{dominio} in cui l’equazione ha senso. Ad esempio, se compare una radice quadrata \(\sqrt{f(x)}\), è necessario che \(f(x) \ge 0\) per tutti i valori di \(x\) considerati (se si lavora nell’insieme dei numeri reali). Analogamente, se \(x\) compare al denominatore di una frazione, abbiamo la condizione \(x \neq 0\) o, più in generale, \(g(x) \neq 0\).

\subparagraph{Metodologia di risoluzione.}
Una volta stabilito il dominio, spesso il passo risolutivo cruciale consiste nel \textit{isolare la radice} (quando possibile) su un lato dell’equazione. Ad esempio, se l’equazione presenta
\[
\sqrt{f(x)} = h(x),
\]
e \(h(x)\) è definita e non negativa nell’intervallo di interesse, allora possiamo \textit{elevare entrambi i membri al quadrato}:
\[
\sqrt{f(x)} = h(x)
\quad\Longrightarrow\quad
f(x) = \bigl(h(x)\bigr)^2.
\]
Attenzione, però: l’elevamento al quadrato (o ad altra potenza) introduce \textit{soluzioni spurie}, poiché l’operazione non è strettamente biunivoca. Dopo aver risolto la nuova equazione (che potrà essere di grado elevato, ma spesso riducibile), si devono \textit{verificare} le soluzioni nel dominio di partenza, escludendo quelle che non soddisfano le condizioni iniziali (ad esempio, punti in cui \(f(x) < 0\), \(\sqrt{f(x)}\neq h(x)\) per cambio di segno, oppure denominatori nulli).

\subparagraph{Esempio schematico.}
Combinando il materiale del capitolo scorso, vediamo un'equazione del tipo:
\[
\frac{\sqrt{f(x)}}{g(x)} = h(x),
\]
con \(g(x)\neq 0\) e \(f(x)\ge 0\). I passaggi principali sono:
\begin{enumerate}
    \item Determinare il \textit{dominio}, imponendo \(f(x)\ge 0\) e \(g(x)\neq 0\).
    \item Isolare la radice, ad esempio moltiplicando per \(g(x)\):
    \[
    \sqrt{f(x)} = g(x)\,h(x).
    \]
    \item Elevare al quadrato:
    \[
    f(x) = \bigl(g(x)\,h(x)\bigr)^2.
    \]
    \item Risolvere l’equazione risultante (che potrebbe essere di grado superiore o frazionaria), semplificando e ricorrendo, se necessario, a fattorizzazioni o regole algebriche.
    \item Sottoporre le soluzioni trovate a \textit{verifica}, controllando che rispettino il dominio e che soddisfino effettivamente l’equazione di partenza.
\end{enumerate}

\paragraph{Disequazioni irrazionali.}
La stessa logica si applica alle \textit{disequazioni}:
\[
\sqrt{f(x)} \;\gtrless\; h(x),
\]
con la differenza che, per stabilire in quali intervalli la disequazione è verificata, occorre svolgere un’analisi del \textit{segno} in ciascun sottointervallo del dominio, tenendo conto del comportamento di \(\sqrt{f(x)}\) e di \(h(x)\).

\paragraph{Esempio 1: Equazione irrazionale semplice.}
\[
\sqrt{x+1} \;=\; 2 - x.
\]
\begin{itemize}
    \item \textbf{Dominio}: \(\sqrt{x+1}\) richiede \(x+1\ge 0 \Rightarrow x\ge -1\). Inoltre, per avere \(2 - x \ge 0\), si deve avere \(x \le 2\). Quindi il \textit{dominio} è \([-1,\,2]\).
    \item \textbf{Isolamento}:
    \[
    \sqrt{x+1} = 2 - x.
    \]
    Dato che è già isolata la radice, eleviamo al quadrato:
    \[
    x + 1 = (2 - x)^2 = x^2 - 4x + 4.
    \]
    \item \textbf{Risoluzione}: 
    \[
    x^2 - 4x + 4 = x + 1 
    \;\Longrightarrow\; 
    x^2 - 5x + 3 = 0.
    \]
    Il discriminante:
    \(\Delta = 25 - 12 = 13\). 
    \[
    x = \frac{5 \pm \sqrt{13}}{2}.
    \]
    \item \textbf{Verifica nel dominio}:  
    I due valori approssimativi sono \(x_1 \approx 0.697\), \(x_2 \approx 4.303\). Tuttavia, \(x_2\approx 4.303\) esce dal dominio \([-1,\,2]\). Rimane solo \(x_1 \approx 0.697\), che rientra in \([-1,2]\). Bisogna inoltre controllare che \(2 - x_1 \ge 0\) (vero, perché \(x_1<2\)). Dunque la soluzione \(\frac{5 - \sqrt{13}}{2}\) è valida; l’altra è da scartare. Per poter fare questo passaggio a mente, non è chiaramente necessario dover fare i calcoli delle radici fino a diversi numeri dopo la virgola, ma è sufficiente notare se appartengano o meno al dominio, operazione che è spesso molto più immediata e richiede pochi calcoli.
\end{itemize}

\paragraph{Considerazioni finali.}
Le \textit{equazioni} e \textit{disequazioni irrazionali} non richiedono \textit{necessariamente} la presenza di frazioni: la variabile può comparire sotto radice e in polinomi \textit{semplici}. Tuttavia, è anche possibile incontrare problemi \textit{misti}, in cui convivono radici e denominatori. In ogni caso, la \textbf{determinazione del dominio}, l’\textbf{isolamento} delle radici (quando fattibile) e la \textbf{verifica} delle soluzioni restano i cardini di un approccio corretto, supportato dai \textbf{prodotti notevoli} per eventuali scomposizioni e semplificazioni algebriche. 
\newpage

\subsectionstar{[34 - 35] Sistemi di Equazioni di Secondo Grado}
\paragraph{Metodo grafico e interpretazione geometrica.}
Un altro modo per comprendere (e talvolta risolvere) i sistemi di equazioni consiste nel \textit{rappresentarne i grafici} in un piano (se il numero di variabili è 2) o nello spazio (se il numero di variabili è 3). In particolare:

\begin{itemize}
    \item \textbf{Equazioni di primo grado in 2 variabili} (\(x, y\)) rappresentano \textit{rette} nel piano cartesiano. Il sistema di 2 equazioni in 2 incognite corrisponde a \textit{due rette}. La soluzione, se esiste, è \textit{il punto di intersezione} di tali rette.
    \begin{itemize}
        \item Se le rette non sono parallele, si incrociano in un \textit{unico} punto (\(\rightarrow\) soluzione unica).
        \item Se le rette sono parallele e distinte, non si incontrano mai (\(\rightarrow\) nessuna soluzione).
        \item Se le rette coincidono, ogni punto è comune (\(\rightarrow\) infinite soluzioni).
    \end{itemize}
    \item \textbf{Equazioni di secondo grado in 2 variabili} (\(x, y\)) rappresentano coniche nel piano: \textit{parabole}, \textit{cerchi}, \textit{ellissi}, \textit{iperboli}, a seconda della forma e dei coefficienti. Il sistema di 2 equazioni in 2 incognite può corrispondere, ad esempio, a \textit{due parabole}: la soluzione è data dai \textit{punti di intersezione} di queste curve, che possono essere \textit{zero}, \textit{uno}, \textit{due} o anche un numero maggiore (se, in casi particolari, le due coniche coincidono parzialmente).
    \begin{itemize}
        \item Se le parabole (o altre coniche) non si incontrano \(\rightarrow\) nessuna soluzione).
        \item Se si toccano in un unico punto (\(\rightarrow\) soluzione unica).
        \item Se si intersecano in due punti (\(\rightarrow\) due soluzioni).
        \item Se coincidono o hanno parti in comune più estese (\(\rightarrow\) infinite soluzioni).
    \end{itemize}
\end{itemize}

La rappresentazione grafica è un valido \textit{strumento di supporto} per comprendere il comportamento di un sistema di equazioni, soprattutto quando si tratta di \textit{due variabili} (rette, parabole, coniche in genere). Può evidenziare immediatamente i casi senza soluzioni (nessun punto di intersezione), soluzioni uniche (un solo punto di intersezione) o infinite soluzioni (coincidenza parziale delle curve). 

Tuttavia, per ottenere soluzioni numeriche \textit{esatte}, si ricorre in genere ai metodi algebrici (sostituzione, riduzione, scomposizioni, ecc.), illustrati nei paragrafi successivi. Il metodo grafico resta quindi un ottimo strumento complementare, utile per controllare e interpretare i risultati e per comprendere perché talvolta un sistema \textit{non} sia risolubile. Ad esempio, nel caso di \textit{due parabole} che non si incontrano, possiamo vedere graficamente che non esistono punti comuni, dunque \textit{nessuna} soluzione. Nel caso di due rette parallele, nessun punto di intersezione \(\rightarrow\) sistema impossibile, mentre due rette coincidenti indicano \textit{infinità} di soluzioni. 

\paragraph{Metodi Algebrici di Risoluzione di Sistemi}
Quando ci troviamo di fronte a un \textit{sistema di equazioni}, ovvero un insieme di più equazioni con le stesse incognite, possiamo adottare diversi \textit{metodi algebrici} per individuare le soluzioni. Due dei metodi più classici e versatili sono:
\begin{itemize}
    \item \textbf{Metodo di Sostituzione}.
    \item \textbf{Metodo di Riduzione}.
\end{itemize}
Inizieremo illustrandoli su \textit{sistemi lineari} (equazioni di primo grado), che costituiscono la base più semplice per comprendere la filosofia di ciascun approccio. Successivamente, mostreremo come la stessa logica si possa applicare, con gli opportuni adattamenti, a \textit{sistemi di grado superiore} (ad esempio, di secondo grado).

\subparagraph{1. Metodo di Sostituzione.}
Si \textit{isola} una delle variabili in una delle equazioni, ricavandola in funzione delle altre, e si \textit{sostituisce} questa espressione nelle restanti equazioni. In questo modo, il numero di incognite da risolvere si riduce progressivamente, fino a poter determinare tutti i valori.

\subparagraph{Esempio}
\noindent
Come primo esempio, consideriamo il sistema lineare a due incognite
\[
\begin{cases}
x + 2y = 5,\\
3x - y = 4.
\end{cases}
\]
Dalla prima equazione isoliamo \(x\), ottenendo
\[
x = 5 - 2y.
\]
Sostituiamo poi \(x = 5 - 2y\) nella seconda:
\[
3(5 - 2y) - y = 4 
\quad\Longrightarrow\quad
15 - 6y - y = 4
\quad\Longrightarrow\quad
15 - 7y = 4.
\]
A questo punto risolviamo in \textit{un’unica} incognita:
\[
-7y = 4 - 15 = -11
\quad\Longrightarrow\quad
y = \frac{11}{7}.
\]
Per determinare \(x\), sostituiamo \(y\) nella forma isolata:
\[
x = 5 - 2\Bigl(\tfrac{11}{7}\Bigr)
= 5 - \tfrac{22}{7}
= \tfrac{35}{7} - \tfrac{22}{7}
= \tfrac{13}{7}.
\]
La soluzione del sistema risulta dunque
\[
\Bigl(\tfrac{13}{7}, \tfrac{11}{7}\Bigr).
\]

\textit{Lo stesso metodo} si estende a sistemi con più incognite o di grado superiore, isolando un’espressione dalla prima equazione (spesso la variabile “più facile” da estrarre) e sostituendola nelle altre. L’eventuale comparsa di potenze e radici richiede scomposizioni o passaggi aggiuntivi, ma l’idea resta immutata.

\subparagraph{2. Metodo di Riduzione }
Si \textit{combinano linearmente} le equazioni per \textit{eliminare} via via le variabili. Nel caso di due incognite, si moltiplicano o dividono opportunamente le equazioni, in modo da poter sommare (o sottrarre) e annullare una variabile alla volta. Analogamente, con più incognite, si ripete l’operazione fino a ridurre il sistema a un numero minore di variabili.

\subparagraph{Esempio (lineare, 2 incognite) con sottrazione diretta.}
Consideriamo il seguente sistema di primo grado:
\[
\begin{cases}
x + 3y = 10, \\
x - 2y = 5.
\end{cases}
\]
Qui \textit{notiamo} che la variabile \(x\) ha lo stesso coefficiente \(1\) in \textit{entrambe} le equazioni. Questo rende il \textit{metodo di riduzione} (detto anche “eliminazione”) particolarmente \textit{agevole}, perché possiamo semplicemente \textit{sottrarre} le due equazioni per far “sparire” \(x\).

\begin{itemize}
    \item \textit{Fase 1: Scegli la variabile da eliminare.}  
    In questo esempio, scegliamo di eliminare \(x\) perché ha il medesimo coefficiente in entrambe le equazioni (coefficiente \(1\)).

    \item \textit{Fase 2: Sottrai una delle due equazioni dall’altra.}  
    Scegliamo di fare \((1^\text{a} \text{ eq.}) - (2^\text{a} \text{ eq.})\):
    \[
    (x + 3y) \;-\; (x - 2y) 
    = 10 - 5.
    \]
    Svolgendo la sottrazione, otteniamo:
    \[
    x + 3y - x + 2y 
    = 10 - 5 
    \;\;\Longrightarrow\;\;
    5y = 5.
    \]
    \[
    \Longrightarrow
    y = 1.
    \]

    \item \textit{Fase 3: Sostituisci il valore di \(y\) in una delle due equazioni originali.}  
    Utilizziamo la prima:
    \[
    x + 3 \cdot 1 = 10 
    \;\;\Longrightarrow\;\;
    x + 3 = 10
    \;\;\Longrightarrow\;\;
    x = 7.
    \]

    \item \textit{Soluzione}: \(\Bigl(7,\,1\Bigr)\).
\end{itemize}

\paragraph{Osservazione sul metodo di riduzione.}
Il \textit{vantaggio} di usare la \textbf{riduzione} (o eliminazione) è particolarmente evidente quando \textit{almeno} una variabile si presenta con lo stesso coefficiente (o con coefficienti facilmente “opponibili”) in due equazioni. In tal caso, \textit{basta} sommare o sottrarre direttamente le equazioni per \textit{eliminare} quella variabile con un’unica operazione, semplificando il calcolo. Se invece i coefficienti non sono già uguali (in valore assoluto), si procede a moltiplicare ciascuna equazione per un fattore opportuno, in modo da rendere i coefficienti della variabile scelta uguali (ma con segni opposti) e poi si sommano o sottraggono le equazioni. 

In sintesi, il \textit{metodo di riduzione} può talvolta ridurre drasticamente la complessità del sistema, poiché non si deve affrontare la fase di “isolamento” e sostituzione di una variabile, ma ci si affida a una singola operazione di combinazione lineare (sommatoria o sottrazione) per passare a un sistema in una variabile in meno. 

\subparagraph{Generalizzazione a Sistemi di Secondo Grado.}
I principi di sostituzione e riduzione \textit{non} si limitano ai casi lineari. Quando le equazioni contengono termini quadratici (o di grado superiore), i passaggi di base rimangono gli stessi:
\begin{itemize}
    \item \textit{Sostituzione}: si isola un’espressione da un’equazione (ad esempio, \(y = 3 - x\), oppure \(x^2 = 4 - y^2\)) e la si inserisce nell’altra.  
    \item \textit{Riduzione}: si possono ancora tentare combinazioni (specialmente se una delle equazioni è scomponibile).  
\end{itemize}
Naturalmente, l’algebra si fa più impegnativa (possono comparire radici, denominatori, prodotti notevoli), e i risultati possono includere \textit{più soluzioni}, \textit{nessuna soluzione}, o \textit{soluzioni coincidenti} con un intero insieme (come una curva comune). Un esempio tipico:

\[
\begin{cases}
x + y = 3, \\
x^2 + y^2 = 9.
\end{cases}
\]
Con il \textit{metodo di sostituzione}, \(y = 3 - x\). Inserendo nella seconda, \(x^2 + (3-x)^2 = 9\). Dopo aver risolto, si trovano due coppie di soluzioni, \((0,3)\) e \((3,0)\).
\newpage

\subsectionstar{[35] Sistemi di Equazioni di Grado Superiore}
\paragraph{Sistemi con equazioni di grado superiore (terzo, quarto, ecc.).}
Quando le equazioni coinvolte in un sistema superano il \textit{secondo grado}, la risoluzione può diventare decisamente più impegnativa. Nonostante ciò, i \textit{principi generali} (sostituzione, riduzione, e scomposizioni) restano validi, sebbene l’algebra richiesta possa risultare molto più elaborata. Ecco alcune linee guida:

\begin{itemize}
    \item \textbf{Approccio di sostituzione anche in gradi superiori.}  
    Se una delle equazioni è relativamente “semplice” da isolare in una variabile (o in un’espressione polinomiale), si può comunque procedere con il \textit{metodo di sostituzione}. Ad esempio, in un sistema:
    \[
    \begin{cases}
    x^3 - 4x = y^2, \\
    y^3 = x + 2,
    \end{cases}
    \]
    si potrebbe, se opportuno, isolare \(x\) o \(y\) da una delle due e sostituirlo nell’altra. È chiaro che la complessità delle espressioni può crescere rapidamente, ma il \textit{concetto} resta identico a quello visto nei gradi inferiori.

    \item \textbf{Scomposizioni e “blocchi polinomiali” ricorrenti.}  
    Spesso, nelle equazioni di terzo o quarto grado, o in sistemi che miscelano vari gradi, compaiono strutture riconducibili a \textit{prodotti notevoli} o a \textit{polinomi fattorizzabili}. Un esempio tipico: 
    \[
    x^4 - 5x^2 + 4 = 0
    \]
    può essere visto come un’equazione “bi-quadratica” \(\,(x^2)^2 - 5(x^2) + 4=0\). Oppure, potremmo avere fattori come \(a^3 - b^3\) o \(a^3 + b^3\). Riconoscere \(\,(x^2 - 4) = (x-2)(x+2)\) o \(\,(x^3 + 1) = (x+1)(x^2 - x + 1)\) permette di \textit{ridurre} l’ordine dell’equazione, rendendo più semplice l’applicazione della sostituzione o della riduzione.
    \end{itemize}


% I am 97% sure this code is correct.

\paragraph{Esempio di sostituzione con equazioni cubiche}

Consideriamo il sistema:
\[
\begin{cases}
y = 3x - x^3,\\
y = 4 - 2x^2.
\end{cases}
\]
Per \textit{risolvere} il sistema, cerchiamo i punti \((x,y)\) in cui queste curve si \textit{intersecano}, ossia dove i due valori di \(y\) coincidono. Vediamo sotto un grafico delle due curve con i relativi punti di incidenza, di questi ne vediamo due segnati ed intuiamo la presenza di un terzo all'incisione del proseguire delle curve nella derstra del grafico.

\begin{center}
\begin{tikzpicture}[scale=0.8]
    % Assi cartesiani (più compatti)
    \draw[->] (-2.5,0)--(2.5,0) node[right]{$x$};
    \draw[->] (0,-2.5)--(0,3) node[above]{$y$};

    % Curva blu: y = 3x - x^3, con dominio -2.2 : 2.2
    \draw[samples=200, domain=-2.2:2.2, smooth, variable=\x, thick, blue]
        plot(\x,{3*\x - (\x)^3});

    % Curva rossa: y = 4 - 2x^2, con dominio -2 : 2
    \draw[samples=200, domain=-2:2, smooth, variable=\x, thick, red]
        plot(\x,{4 - 2*(\x)^2});

    % Intersezione 1: x=(1 - sqrt17)/2
    \pgfmathsetmacro{\xinf}{(1 - sqrt(17))/2}
    \pgfmathsetmacro{\yinf}{3*(\xinf) - (\xinf)^3}
    \filldraw (\xinf,\yinf) circle(2pt);

    % Intersezione 2: x=1 => y=2
    \filldraw (1,2) circle(2pt);

    % Etichette delle curve (posizionate in modo approssimativo)
    \node[blue] at (1.6,-1.5) {\small $y = 3x - x^3$};
    \node[red] at (1.6,0.5) {\small $y = 4 - 2x^2$};

\end{tikzpicture}
\end{center}
 Dalla prima equazione: \(y = 3x - x^3\). Impostiamo l’uguaglianza con la seconda: 
    \[
    3x - x^3 = 4 - 2x^2.
    \]
    Portiamo tutti i termini a primo membro:
    \[
    -\,x^3 + 2x^2 + 3x - 4 = 0.
    \]
    Per comodità, riscriviamo:
    \[
    -\bigl(x^3 - 2x^2 - 3x + 4\bigr) = 0 
    \;\;\Longrightarrow\;\;
    x^3 - 2x^2 - 3x + 4 = 0.
    \]
Proviamo eventuali \textit{soluzioni intere} semplici (come \(x = 1, -1, 2, -2\), ecc.). Verifichiamo \(x=1\):
\[
1^3 - 2\cdot1^2 - 3\cdot1 + 4 = 1 - 2 - 3 + 4 = 0.
\]
Dunque \(x = 1\) è una radice. Sfruttando la divisione o la \textit{fattorizzazione}, otteniamo:
\[
x^3 - 2x^2 - 3x + 4 = (x - 1)\,\bigl(x^2 - x - 4\bigr).
\]
Le soluzioni si ricavano quindi da:
\[
x - 1 = 0 
\quad\Longrightarrow\quad 
x = 1,
\]
oppure
\[
x^2 - x - 4 = 0 
\quad\Longrightarrow\quad
x = \frac{1 \pm \sqrt{1 + 16}}{2} 
= \frac{1 \pm \sqrt{17}}{2}.
\]
Quindi abbiamo \textit{tre} soluzioni reali per \(x\). Per ciascun valore di \(x\), troviamo \(y\) sostituendo nella prima (o nella seconda) equazione. Usando \(y = 3x - x^3\), otteniamo:

\begin{itemize}
    \item \(\mathbf{x = 1}\): 
    \[
    y = 3(1) - (1)^3 = 3 - 1 = 2 
    \;\;\Longrightarrow\;\;
    \bigl(x,y\bigr) = \bigl(1,\,2\bigr).
    \]
    \end{itemize}
Notiamo poi che i calcoli per ottenere la $y$ richiederanno un po' di tempo, dato che partiamo con un numero più complessso come $\tfrac{1 + \sqrt{17}}{2}$ ma il lettore è invitato a seguire con cura i passaggi e ripassando quindi le proprietà delle radici e delle potenze:
\begin{itemize}
    \item \(\mathbf{x = \tfrac{1 + \sqrt{17}}{2}}\): 
    \[
    x^2 = \left(\tfrac{1 + \sqrt{17}}{2}\right)^2 
         = \tfrac{(1 + \sqrt{17})^2}{4} 
         = \tfrac{1 + 2\sqrt{17} + 17}{4} 
         = \tfrac{18 + 2\sqrt{17}}{4} 
         = \tfrac{9 + \sqrt{17}}{2},
    \]
    \[
    x^3 = x \cdot x^2 
         = \left(\tfrac{1 + \sqrt{17}}{2}\right)
           \left(\tfrac{9 + \sqrt{17}}{2}\right) 
         = \tfrac{(1 + \sqrt{17})(9 + \sqrt{17})}{4} 
         = \tfrac{26 + 10\sqrt{17}}{4} 
         = \tfrac{13}{2} + \tfrac{5\sqrt{17}}{2}.
    \]
    Dunque
    \[
    y = 3\left(\tfrac{1 + \sqrt{17}}{2}\right) 
        \;-\;
        \left(\tfrac{13}{2} + \tfrac{5\sqrt{17}}{2}\right)
    = \tfrac{3 + 3\sqrt{17}}{2} 
      \;-\;
      \tfrac{13 + 5\sqrt{17}}{2}
    \]
    \[
    = \tfrac{3 - 13}{2} 
      \;+\;
      \tfrac{3\sqrt{17} - 5\sqrt{17}}{2}
    = -5 \;-\; \sqrt{17}.
    \]
    \[
    \Longrightarrow
    \bigl(x,y\bigr) 
    = \Bigl(\tfrac{1 + \sqrt{17}}{2},\;-5 - \sqrt{17}\Bigr).
    \]

    \item \(\mathbf{x = \tfrac{1 - \sqrt{17}}{2}}\): 
    \[
    x^2 = \left(\tfrac{1 - \sqrt{17}}{2}\right)^2
         = \tfrac{(1 - \sqrt{17})^2}{4} 
         = \tfrac{1 - 2\sqrt{17} + 17}{4}
         = \tfrac{18 - 2\sqrt{17}}{4} 
         = \tfrac{9 - \sqrt{17}}{2},
    \]
    \[
    x^3 = \left(\tfrac{1 - \sqrt{17}}{2}\right)
           \left(\tfrac{9 - \sqrt{17}}{2}\right)
         = \tfrac{(1 - \sqrt{17})(9 - \sqrt{17})}{4}
         = \tfrac{26 - 10\sqrt{17}}{4}
         = \tfrac{13}{2} - \tfrac{5\sqrt{17}}{2}.
    \]
    Quindi
    \[
    y = 3\left(\tfrac{1 - \sqrt{17}}{2}\right)
        \;-\;
        \left(\tfrac{13}{2} - \tfrac{5\sqrt{17}}{2}\right)
    = \tfrac{3 - 3\sqrt{17}}{2} 
      \;-\;
      \tfrac{13 - 5\sqrt{17}}{2}
    \]
    \[
    = \tfrac{3 - 13}{2} 
      \;+\;
      \tfrac{-3\sqrt{17} -(-5\sqrt{17})}{2}
    = -5 + \sqrt{17}.
    \]
    \[
    \Longrightarrow
    \bigl(x,y\bigr) 
    = \Bigl(\tfrac{1 - \sqrt{17}}{2},\;-5 + \sqrt{17}\Bigr).
    \]
\end{itemize}

\[
\boxed{\text{Soluzioni reali}: 
\quad
\bigl(1,\,2\bigr),
\quad
\Bigl(\tfrac{1 + \sqrt{17}}{2},\;-5 - \sqrt{17}\Bigr),
\quad
\Bigl(\tfrac{1 - \sqrt{17}}{2},\;-5 + \sqrt{17}\Bigr).
}
\]
\newpage


\subsectionstar{[6] Le Potenze}
\paragraph{Potenze con esponente naturale.}
Cominciamo definendo il concetto di potenza quando l’esponente è un numero \textit{naturale} (cioè un intero positivo). Dato un numero reale \(a\) (detto \textit{base}) e un numero naturale \(n\), la \textit{potenza} di \(a\) con esponente \(n\) si indica con \(a^n\) e si definisce come:
\[
a^n 
\;=\; 
\underbrace{a \times a \times \cdots \times a}_{n \text{ volte}},
\quad
n \in \mathbb{N}.
\]
Nel caso \(n=0\), per convenzione poniamo
\[
a^0 = 1 
\quad (\text{per } a \neq 0).
\]

\begin{itemize}
    \item \(\mathbf{a^m \cdot a^n = a^{m+n}}\).  
    \item \(\mathbf{\frac{a^m}{a^n} = a^{m-n}}\) (per \(a \neq 0\)).  
    \item \(\mathbf{(a^m)^n = a^{m\cdot n}}\).  
    \item \(\mathbf{a^1 = a}\).  
\end{itemize}

\paragraph{Generalizzazione alle potenze con esponente intero.}
Estendiamo ora la definizione di potenza agli esponenti \textit{interi} (positivi, negativi, o zero). Se \(n\) è un intero positivo, poniamo:
\[
a^{-n} = \frac{1}{a^{|-n|}} = \frac{1}{a^{n}}
\quad (\text{per } a \neq 0).
\]
Così possiamo conservare le stesse proprietà viste per gli esponenti naturali, a patto di fare attenzione a non usare la base \(a=0\) quando l’esponente è negativo.

\paragraph{Potenze con esponente razionale.}
Ulteriore passo è considerare gli \textit{esponenti frazionari}. Per esempio, se \(m\) e \(n\) sono interi e \(n>0\), una potenza con esponente \(\tfrac{m}{n}\) (numero razionale) è definita come:
\[
a^{\frac{m}{n}} 
\;=\; 
\Bigl(a^m\Bigr)^{\tfrac{1}{n}}
\;=\;
\sqrt[n]{a^m}
\quad(\text{se } a > 0\text{, o con opportune attenzioni se }a \leq 0).
\]
In particolare, se l’esponente è \(\tfrac{1}{n}\), \(\,a^{\tfrac{1}{n}}\) è la \textit{radice n-esima} di \(a\). Questa definizione mantiene la coerenza con le regole fondamentali sulle potenze. Pertanto:
\[
a^{\frac{m}{n}} \cdot a^{\frac{p}{q}}
= a^{\,\frac{m}{n} + \frac{p}{q}}
,\quad
\bigl(a^{\frac{m}{n}}\bigr)^r
= a^{\frac{m}{n}\,\cdot\,r},
\]
con i dovuti requisiti di positività della base (o, in certi casi, con interpretazioni estese ai numeri complessi). Vediamo ora alcuni esempi:
\begin{itemize}
    \item \(\bigl(-\tfrac{1}{2}\bigr)^3 
    = -\,\tfrac{1}{8}\).
    \item \(\bigl(-\tfrac{1}{2}\bigr)^{-2}
    = \bigl(-2\bigr)^2 
    = 4 \quad\text{(ammesso che consideriamo il }-\tfrac{1}{2} \neq 0\text{)}.\)
    \item \(\Bigl(\tfrac{4}{9}\Bigr)^{\tfrac{1}{2}}
    = \sqrt{\tfrac{4}{9}}
    = \tfrac{2}{3}.\)
    \item \(\Bigl(2\Bigr)^{-\tfrac{3}{2}}
    = \tfrac{1}{2^{\tfrac{3}{2}}}
    = \frac{1}{\sqrt{2^3}}
    = \tfrac{1}{2\sqrt{2}}.\)
\end{itemize}

\paragraph{Esempi complessi con esponenti razionali.}
Quando si combinano più potenze con esponenti frazionari, bisogna fare attenzione alle regole di semplificazione degli esponenti e all’eventuale presenza di basi negative. Di seguito alcuni esempi:

\begin{itemize}
    \item \(\bigl(a^{\tfrac{2}{3}}\bigr)^{\tfrac{3}{4}}\)
    \quad In questo caso, si sfrutta la regola \((a^m)^n = a^{m \cdot n}\):
    \[
    \bigl(a^{\tfrac{2}{3}}\bigr)^{\tfrac{3}{4}}
    = a^{\,\tfrac{2}{3} \,\cdot\, \tfrac{3}{4}}
    = a^{\tfrac{2 \cdot 3}{3 \cdot 4}}
    = a^{\tfrac{2}{4}}
    = a^{\tfrac{1}{2}}
    = \sqrt{a}
    \quad (\text{ammesso } a>0 \text{ se vogliamo restare nei reali}).
    \]

    \item \(\dfrac{a^{\tfrac{5}{6}}}{a^{\tfrac{1}{6}}}\)
    \quad Usiamo la regola \(\frac{a^m}{a^n} = a^{m-n}\):
    \[
    \dfrac{a^{\tfrac{5}{6}}}{a^{\tfrac{1}{6}}}
    = a^{\,\tfrac{5}{6} - \tfrac{1}{6}}
    = a^{\tfrac{4}{6}}
    = a^{\tfrac{2}{3}}.
    \]

    \item \(\Bigl(\,\tfrac{9}{16}\Bigr)^{\tfrac{3}{2}}\)  
    Possiamo interpretare questo come:
    \[
    \Bigl(\tfrac{9}{16}\Bigr)^{\tfrac{3}{2}}
    = \Bigl(\tfrac{9}{16}\Bigr)^{1 + \tfrac{1}{2}}
    = \Bigl(\tfrac{9}{16}\Bigr)\,\bigl(\tfrac{9}{16}\bigr)^{\tfrac{1}{2}}.
    \]
    Calcolando separatamente:
    \[
    \tfrac{9}{16} = \Bigl(\tfrac{9}{16}\Bigr),
    \quad
    \bigl(\tfrac{9}{16}\bigr)^{\tfrac{1}{2}} 
    = \sqrt{\tfrac{9}{16}}
    = \tfrac{3}{4}.
    \]
    Di conseguenza:
    \[
    \Bigl(\tfrac{9}{16}\Bigr)^{\tfrac{3}{2}}
    = \tfrac{9}{16} \;\times\; \tfrac{3}{4}
    = \tfrac{27}{64}.
    \]

    \item \(\left(-\,\tfrac{8}{27}\right)^{\tfrac{2}{3}}\)  
    Qui è necessario essere prudenti, poiché la base è negativa. Tuttavia, se il denominatore dell’esponente è un numero pari, la radice potrebbe non essere definita nei numeri reali. In questo esempio \(\tfrac{2}{3} = \tfrac{2}{3}\), dove il \(\sqrt[3]{\phantom{x}}\) può gestire anche valori negativi, ma il successivo \(\bigl(\cdot\bigr)^2\) rende il risultato necessariamente positivo. Formalmente:
    \[
    \left(-\,\tfrac{8}{27}\right)^{\tfrac{2}{3}}
    = \Bigl(\,\bigl(-\,\tfrac{8}{27}\bigr)^{\frac{1}{3}}\Bigr)^2
    = \Bigl(-\,\sqrt[3]{\tfrac{8}{27}}\Bigr)^2.
    \]
    E poiché \(\sqrt[3]{\tfrac{8}{27}} = \tfrac{2}{3}\):
    \[
    \bigl(-\,\tfrac{2}{3}\bigr)^2 
    = \tfrac{4}{9}.
    \]
    Quindi:
    \[
    \left(-\,\tfrac{8}{27}\right)^{\tfrac{2}{3}}
    = \tfrac{4}{9}.
    \]
\end{itemize}

Questi esempi mostrano come, usando le regole di base delle potenze, sia possibile semplificare anche espressioni con esponenti frazionari più complessi, tenendo conto di eventuali restrizioni sul segno della base e delle potenziali radici. L’importante è ricordare che:
\begin{itemize}
    \item \(\bigl(a^m\bigr)^n = a^{mn}\).
    \item \(\tfrac{a^m}{a^n} = a^{m-n}\) (per \(a \neq 0\)).
    \item Se il denominatore dell’esponente è pari (ad esempio, \(\tfrac{1}{2}\) o \(\tfrac{3}{4}\)), bisogna considerare che la radice di indice pari non è definita per \(a < 0\) nei reali (salvo ulteriori interpretazioni nei numeri complessi).
\end{itemize}

\newpage
\subsectionstar{[30*] Esponenti Reali}
\noindent
Nel passaggio dagli \textit{esponenti razionali} a quelli \textit{reali}, l’idea centrale consiste nel prolungare la definizione di \(a^x\) (per \(a>0\)) a \textit{tutti} i valori \(x \in \mathbb{R}\). Un modo efficace per farlo sfrutta la \textbf{funzione esponenziale} e il \textbf{logaritmo naturale}: si definisce
\[
a^x = e^{\,x\,\ln(a)},
\]
dove \(\ln(a)\) è il logaritmo naturale di \(a\). Questa scelta coincide con la definizione precedente quando \(x\) è razionale, poiché:
\[
a^{\frac{m}{n}}
= \sqrt[n]{a^m}
\quad
\text{diventa}
\quad
e^{\frac{m}{n}\,\ln(a)},
\]
garantendo \textit{continuità} e \textit{coerenza} con le regole delle potenze già note. 

Per \(a \le 0\), la definizione di \(a^x\) non è in generale possibile all’interno dei numeri reali (poiché \(\ln(a)\) non è definito per \(a \le 0\)); di conseguenza, la \textit{base} si assume \(\,a>0\). Le proprietà fondamentali delle potenze (come \(\,a^{x+y} = a^x \cdot a^y\) o \((a^x)^y = a^{xy}\)) restano valide e discendono dalla definizione via \(\,e^{x \ln(a)}\). 

In tal modo, per ogni reale \(x\), la quantità \(a^x\) è ben definita e continua, rendendo posibili \textit{limiti}, \textit{derivate} e altre operazioni analitiche, fondamentali nello studio di funzioni esponenziali reali. 

\noindent
Le \textit{equazioni esponenziali} sono quelle in cui l’incognita compare nell’\textit{esponente} di una potenza, come nel caso di \(a^{x} = b\). Per risolvere un’equazione di questo tipo, occorre spesso ricorrere a trasformazioni che coinvolgano i \textit{logaritmi}. Un esempio classico è l’equazione
\[
3^{x} = 10.
\]
Se \(x\) è l’incognita, si passa alla forma logaritmica applicando, ad esempio, il logaritmo naturale:
\[
x \ln(3) = \ln(10)
\quad \Longrightarrow \quad
x = \frac{\ln(10)}{\ln(3)}.
\]
In maniera analoga, se l’equazione esponenziale presenta somme o differenze tra potenze di basi diverse, come in \(2^{x} + 3^{x} = 5\), si possono usare strategie numeriche o la definizione di funzioni ausiliarie per isolare l’incognita.

Le \textit{disequazioni esponenziali} sono quelle in cui occorre determinare i valori di \(x\) per cui un’espressione esponenziale soddisfa un segno di \(<\), \(\le\), \(>\) o \(\ge\). Ad esempio, la disequazione
\[
2^{x} > 7
\]
può essere risolta, in maniera simile al caso delle equazioni, usando i logaritmi:
\[
2^{x} > 7
\quad \Longrightarrow \quad
x \ln(2) > \ln(7)
\quad \Longrightarrow \quad
x > \frac{\ln(7)}{\ln(2)}.
\]
Per le disequazioni, è fondamentale tenere conto che se la base dell’esponenziale è \((0,1)\) anziché \((1,+\infty)\), la \textit{direzione} del segno si \textit{inverte} durante la trasformazione logaritmica, poiché la funzione \(a^{x}\) risulta \textit{decrescente} in quel caso. Un esempio:

\[
\bigl(\tfrac12\bigr)^{x} < 4.
\]
Ponendo \(a = \tfrac12\), si sa che \(a^{x}\) è \textit{decrescente} in \(x\). Con la forma logaritmica,
\[
x \ln\!\bigl(\tfrac12\bigr) < \ln(4).
\]
Poiché \(\ln\!\bigl(\tfrac12\bigr) < 0\), il segno della disequazione si inverte:
\[
x > \frac{\ln(4)}{\ln\!\bigl(\tfrac12\bigr)}.
\]
Prestare attenzione a questi aspetti è essenziale per gestire correttamente la risoluzione di equazioni e disequazioni esponenziali, in cui le basi e le trasformazioni logaritmiche rivestono un ruolo centrale.

\noindent
\textbf{Esempio di Equazione Esponenziale:} risolviamo \(2^x = 5\).

\smallskip
\noindent
\textit{Passaggio 1.} Riscriviamo l’equazione in forma logaritmica. Se \(2^x = 5\), allora prendendo il logaritmo (ad esempio \(\ln\)) di entrambi i membri:
\[
x \ln(2) = \ln(5).
\]

\smallskip
\noindent
\textit{Passaggio 2.} Isoliamo l’incognita \(x\):
\[
x = \frac{\ln(5)}{\ln(2)} 
\;\approx\; 2.3219.
\]

\smallskip
\noindent
\textit{Interpretazione grafica.} La soluzione corrisponde al \textit{punto di intersezione} tra la curva \(y=2^x\) e la retta orizzontale \(y=5\). Nel piano cartesiano, tracciando il grafico di \(2^x\) (una funzione crescente per \(x \in \mathbb{R}\)) e la retta \(y=5\), la \textit{x}-ascissa del punto in cui si incontrano fornisce proprio \(x \approx 2.3219\).

\begin{center}
\begin{tikzpicture}[scale=1.0, line cap=round, line join=round]
  % Assi
  \draw[->] (-1,0) -- (5,0) node[right] {\small $x$};
  \draw[->] (0,-1) -- (0,6) node[above] {\small $y$};

  % Curva y=2^x, da x=-1 a x=4
  \draw[domain=-1:2.6, samples=100, thick, blue]
       plot(\x, {2^(\x)}) node[right] {\small $y=2^x$};

  % Retta y=5
  \draw[thick, red] (-1,5) -- (5,5) node[pos=0.96,right] {\small $y=5$};

  % Intersezione: x = ln(5)/ln(2) ~ 2.3219
  \coordinate (Xint) at (2.321928,5);
  \fill (Xint) circle (2pt);
  \node[above right] at (Xint) {\small $(2.32,\;5)$};

  % Tacche e label sugli assi (opzionali)
  \foreach \xx in {-1,1,2,3,4} {
    \draw (\xx,0.1) -- (\xx,-0.1);
    \node[below] at (\xx,0) {\small \xx};
  }
  \foreach \yy in {1,2,3,4,5} {
    \draw (0.1,\yy) -- (-0.1,\yy);
    \node[left] at (0,\yy) {\small \yy};
  }
\end{tikzpicture}
\end{center}

\noindent
Il punto nero indica la \textit{soluzione} dell’equazione, ossia \(x = \frac{\ln(5)}{\ln(2)}\). 

\newpage


\subsectionstar{[11] Equazione Particolari}
\paragraph{Equazioni Biquadratiche.}
Un’\textit{equazione biquadratica} è un’equazione polinomiale di \textit{quarto grado} che si presenta nella forma:
\[
a\,x^4 \;+\; b\,x^2 \;+\; c \;=\; 0,
\quad
\text{con } a \neq 0.
\]
La strategia di base consiste nell’effettuare la sostituzione
\[
y = x^2
\quad\Longrightarrow\quad
y^2 = x^4,
\]
trasformando così l’equazione iniziale in un’equazione di secondo grado in \(y\):
\[
a\,y^2 + b\,y + c = 0.
\]
Una volta risolta per \(y\), si riportano le soluzioni nell’espressione \(x^2 = y\) per determinare i possibili valori di \(x\).

\subparagraph{Esempio di risoluzione.}
\[
3\,x^4 \;-\; 10\,x^2 \;-\; 8 = 0.
\]
\begin{enumerate}
    \item \textbf{Sostituzione}: poniamo \(y = x^2\). L’equazione diventa
    \[
    3\,y^2 \;-\; 10\,y \;-\; 8 = 0.
    \]
    \item \textbf{Risolviamo l’equazione in \(y\)}:
    \[
    \Delta = (-10)^2 - 4 \cdot 3 \cdot (-8)
    = 100 + 96 = 196,
    \]
    \[
    y = \frac{\,10 \pm \sqrt{196}\,}{2 \cdot 3}
    = \frac{10 \pm 14}{6}.
    \]
    Otteniamo due valori:
    \[
    y_1 = \frac{10 + 14}{6} = \frac{24}{6} = 4,
    \quad
    y_2 = \frac{10 - 14}{6} = \frac{-4}{6} = -\tfrac{2}{3}.
    \]
    \item \textbf{Ritorno a \(x\)}:
    \begin{itemize}
        \item Da \(y_1 = 4 \implies x^2 = 4\), si ha \(x = \pm 2\).
        \item Da \(y_2 = -\tfrac{2}{3}\), non si ottengono soluzioni reali (perché \(x^2\) non può essere negativo nei reali). Se si considerano i numeri complessi, allora \(x = \pm\,\sqrt{-\tfrac{2}{3}}\).
    \end{itemize}
\end{enumerate}
Le soluzioni reali, dunque, sono \(x=2\) e \(x=-2\).  

\paragraph{Equazioni Trinome generalizzate (\(a\,x^{2n} + b\,x^n + c = 0\)).}
Una \textit{generalizzazione} del concetto di biquadratica consiste in considerare equazioni della forma:
\[
a\,x^{2n} + b\,x^{n} + c \;=\; 0,
\]
dove \(n\) è un numero intero positivo e \(a, b, c\) sono coefficienti reali con \(a \neq 0\). Analogamente alla biquadratica (\(n=2\)), si introduce la sostituzione:
\[
y = x^n
\quad\Longrightarrow\quad
y^2 = x^{2n}.
\]
L’equazione diventa quindi una \textit{quadratica} in \(y\):
\[
a\,y^2 + b\,y + c = 0,
\]
che si risolve con i metodi standard (fattorizzazione o formula risolutiva). Una volta trovati i valori di \(y\), si risolve
\[
x^n = y
\]
per ottenere le soluzioni in \(x\).

\subparagraph{Esempio:}
\[
2\,x^{6} - 7\,x^3 + 3 = 0.
\]
\begin{itemize}
    \item Poniamo \(y = x^3\). L’equazione si trasforma in
    \[
    2\,y^2 - 7\,y + 3 = 0.
    \]
    \item Risolviamo in \(y\). Il discriminante \(\Delta\) è 
    \[
    (-7)^2 - 4\cdot 2 \cdot 3 = 49 - 24 = 25.
    \]
    \[
    y = \frac{7 \pm \sqrt{25}}{4} 
    = \frac{7 \pm 5}{4}.
    \]
    Otteniamo
    \[
    y_1 = \frac{12}{4} = 3, 
    \quad
    y_2 = \frac{2}{4} = \tfrac{1}{2}.
    \]
    \item Reintrodotta la variabile \(x\): 
    \[
    x^3 = 3 
    \quad\Longrightarrow\quad
    x = \sqrt[3]{3},
    \]
    \[
    x^3 = \tfrac{1}{2} 
    \quad\Longrightarrow\quad
    x = \sqrt[3]{\tfrac{1}{2}}.
    \]
    Se si ammettono soluzioni complesse, ciascuna di queste equazioni di terzo grado potrà avere fino a 3 radici (una reale e due complesse coniugate). Nei reali, si ottiene una soluzione reale per \(x^3=3\) e una soluzione reale per \(x^3=\tfrac{1}{2}\).
\end{itemize}

\paragraph{Equazioni Reciproche.}
Un’\textit{equazione reciproca} di grado \(n\) è un’equazione polinomiale in cui i coefficienti dei termini “simmetrici” rispetto al grado coincidono; per esempio, nel caso di quarto grado:
\[
a\,x^4 + b\,x^3 + c\,x^2 + b\,x + a = 0.
\]
Per risolvere queste equazioni, un metodo comune consiste nell’effettuare la sostituzione
\[
X = x + \frac{1}{x},
\]
che, se \(x \neq 0\), consente di “ridurre” il grado dell’equazione trasformandola in una di grado inferiore (tipicamente di grado 2). Va poi prestata attenzione alle soluzioni spure introdotte o eventualmente perdute nel passaggio.

\subparagraph{Esempio}
\[
x^4 + 2\,x^3 + 3\,x^2 + 2\,x + 1 = 0.
\]
\begin{itemize}
    \item Si riconosce la reciprocità: il coefficiente di \(x^4\) e di \(x^0\) (cioè la costante) è 1; il coefficiente di \(x^3\) e di \(x^1\) è 2; quello di \(x^2\) è 3.
    \item Poniamo \(X = x + \frac{1}{x}\). Allora:
    \[
    X^2 = \left(x + \tfrac{1}{x}\right)^2 
    = x^2 + 2 + \tfrac{1}{x^2}.
    \]
    Da cui
    \[
    x^2 + \frac{1}{x^2} = X^2 - 2.
    \]
    \item L’equazione originale si riscrive, raggruppando i termini:
    \[
    (x^4 + \tfrac{1}{x^4}) + 2\,(x^3 + \tfrac{1}{x^3}) + 3\,(x^2 + \tfrac{1}{x^2}) + \text{ (eventuali termini semplificati) }=0.
    \]
    In pratica, sostituendo opportunamente \(x + \tfrac{1}{x} = X\) e \(x^2 + \tfrac{1}{x^2} = X^2 -2\), si ottiene un polinomio in \(X\).  
    \item Risolta l’equazione in \(X\), si passa nuovamente a \(x\) risolvendo \(x + \tfrac{1}{x} = X\). Occorrerà poi verificare che le soluzioni non annullino alcun denominatore (come \(x \neq 0\)) e che siano effettivamente soluzioni dell’equazione originale.
\end{itemize}
\newpage

\subsectionstar{[23] I Logaritmi}
% Sono sicuro al 95% della correttezza di questo testo e degli esempi.

\subsubsection*{Definizione di Logaritmo}
\paragraph{Concetto di base.}
Il \textit{logaritmo} di un numero positivo \(b\) in una base \(a>0\) (con \(a \neq 1\)) è l’esponente al quale bisogna elevare la base \(a\) per ottenere \(b\). In formule:
\[
a^x = b
\quad \Longleftrightarrow \quad
x = \log_a b.
\]
\textbf{Esempio}: \(2^3 = 8\). Ne consegue che \(\log_2 8 = 3\) perché 2, elevato alla terza potenza, dà 8.

\paragraph{Logaritmi particolari.}
\begin{itemize}
    \item \textbf{Logaritmo decimale}: Base 10, indicato spesso con \(\log b\) (o \(\log_{10} b\)).
    \item \textbf{Logaritmo naturale}: Base \(e\) (numero di Nepero, circa \(2{,}718\)), indicato con \(\ln b\) (o \(\log_e b\)).
\end{itemize}

\subsubsection*{Proprietà dei Logaritmi}
I logaritmi possiedono una serie di proprietà che ne semplificano l’utilizzo e i calcoli.

\paragraph{Proprietà.}
\begin{itemize}
    \item \(\log_a 1 = 0\), poiché \(a^0 = 1\).
    \item \(\log_a a = 1\), poiché \(a^1 = a\).
    \item \(\log_a b = \frac{\log_c b}{\log_c a}\), per qualsiasi base \(c>0\), \(c \neq 1\).
\end{itemize}

\paragraph{Proprietà Operative.}
\begin{itemize}
    \item \(\log_a (b \cdot c) = \log_a b + \log_a c\).
    \item \(\log_a \bigl(\tfrac{b}{c}\bigr) = \log_a b - \log_a c\).
    \item \(\log_a (b^c) = c \,\log_a b\).
\end{itemize}

\subsubsection*{Equazioni Logaritmiche}
Un’equazione logaritmica è tale quando l’incognita compare \textit{all’interno} di un logaritmo.

\paragraph{Tipologie di Equazioni.}
\begin{itemize}
    \item \(\log_a (f(x)) = c \;\Longrightarrow\; f(x) = a^c\).  
    \item \(\log_a (f(x)) = \log_a (g(x)) \;\Longrightarrow\; f(x) = g(x)\).
\end{itemize}

\paragraph{Considerazioni sulle Equazioni.}
\begin{itemize}
    \item \textbf{Dominio}: l’argomento di ogni logaritmo deve essere positivo.
    \item \textbf{Verifica}: dopo la risoluzione, controllare che le soluzioni appartengano effettivamente al dominio.
\end{itemize}

\subsubsection*{Disequazioni Logaritmiche}
Le disequazioni logaritmiche contengono il logaritmo dell’incognita e si risolvono applicando le proprietà logaritmiche e, se necessario, trasformandole in forma esponenziale.

\paragraph{Principio di Monotonia.}
\begin{itemize}
    \item Se \(a>1\), \(\log_a(x)\) è crescente: \(\log_a(f(x)) > \log_a(g(x)) \;\Longrightarrow\; f(x) > g(x)\).
    \item Se \(0<a<1\), \(\log_a(x)\) è decrescente: \(\log_a(f(x)) > \log_a(g(x)) \;\Longrightarrow\; f(x) < g(x)\).
\end{itemize}

\noindent \textbf{Esempio}
\[
\log_2\!\bigl((x+2)(x-1)\bigr) \;-\; \log_2(x)
\;=\;
3 \;-\; \log_2(x-1).
\]

Affinché tutti i logaritmi siano definiti, occorre:
\begin{itemize}
    \item \(x-1 > 0 \quad\Longrightarrow\quad x > 1,\)
    \item \(x+2 > 0 \quad\Longrightarrow\quad x > -2,\)
    \item \(x > 0.\)
\end{itemize}
Notiamo che dobbiamo imporre direttamente $x+2 > 0$ anziche $(x+2)(x-1)>0$ dato che abbiamo gia imposto $x-1 > 0$.
Combinando le tre condizioni, si ottiene il \textit{dominio}:
\[
x > 1.
\]

Riorganizziamo l’equazione:
\[
\log_2\!\bigl((x+2)(x-1)\bigr) \;-\; \log_2(x)
\;=\;
3 \;-\; \log_2(x-1).
\]
Portiamo i logaritmi su un unico lato e riconosciamo che \(3\) si può interpretare come \(\log_2(8)\):
\[
\log_2\!\bigl((x+2)(x-1)\bigr) 
\;-\; \log_2(x)
\;+\; \log_2(x-1)
\;=\;
\log_2(8).
\]
Grazie alla \textit{proprietà} \(\log_a A - \log_a B = \log_a \frac{A}{B}\) e \(\log_a A + \log_a B = \log_a(AB)\), possiamo combinare i logaritmi a sinistra:
\[
\log_2\!\Bigl(\tfrac{(x+2)(x-1)}{x}\Bigr)
\;+\;
\log_2(x-1)
\;=\;
\log_2(8).
\]
\[
\log_2\!\Bigl(\tfrac{(x+2)(x-1)}{x} \,\cdot\, (x-1)\Bigr)
\;=\;
\log_2(8).
\]
Ne risulta:
\[
\log_2\!\Bigl(\tfrac{(x+2)(x-1)^2}{x}\Bigr)
\;=\;
\log_2(8).
\]
Poiché \(\log_2 A = \log_2 B \Longrightarrow A=B\) (con \(A,B>0\)), deduciamo:
\[
\tfrac{(x+2)\,(x-1)^2}{x} 
\;=\;
8.
\]

Moltiplichiamo ambo i membri per \(x\):
\[
(x+2)\,(x-1)^2 = 8\,x.
\]
Espandiamo \((x-1)^2 = x^2 - 2x + 1\):
\[
(x+2)\,\bigl(x^2 - 2x + 1\bigr) = 8x.
\]
\[
x(x^2 - 2x + 1) + 2(x^2 - 2x + 1) 
= 8x.
\]
\[
x^3 - 2x^2 + x + 2x^2 - 4x + 2 
= 8x.
\]
\[
x^3 - 3x + 2 
= 8x.
\]
\[
x^3 - 11x + 2 
= 0.
\]

Notiamo quindi in questo caso che abbiamo raggiunto un'equazione di terzo grado e per risolverla dovremo ricorrere ai metodi classici visti nelle sezioni precedenti. Nel caso di questa equazione in particolare non abbiamo alcuna soluzione che si possa trovare con quei metodi, infatti il metodo più intuitivo per procedere sarebbe usando parti della formula risolutiva di terzo grado che non abbiamo visto. Nal caso di esercizi vi sarà richiesto o di fermarvi alla forma polinomiale o sarà un polinomio facilmente risolvibile con i metodi visti in precedenza. Quanto è importante da tenere a mente è di selezionare poi solo quelle soluzioni che appartengono al dominion di partenza.

Vediamo quindi un secondo esempio più semplice ma che coinvolge anche le disequazioni:
\iffalse
\paragraph{Esempio 2}
\[
\ln\bigl(x^2 - 4\bigr) 
\;>\;
\ln\bigl(2x - 1\bigr).
\]

\subparagraph*{1. Dominio}
Per avere \(\ln(\cdot)\) definito, occorre:
\[
x^2 - 4 > 0 
\quad\Longrightarrow\quad
x < -2 \;\;\text{o}\;\; x > 2,
\]
\[
2x - 1 > 0 
\quad\Longrightarrow\quad
x > \tfrac{1}{2}.
\]
Combinando le condizioni:
\begin{itemize}
    \item Se \(x < -2\), non soddisfa \(x>\tfrac{1}{2}\).  
    \item Se \(x>2\), allora soddisfa anche \(x>\tfrac{1}{2}\). 
\end{itemize}
\(\Longrightarrow\) \textit{dominio} della disequazione: \(x>2\).
\subparagraph*{2. Principio di Monotonia del Logaritmo Naturale}
Poiché la funzione \(\ln(\cdot)\) è \textit{crescente} per definizione (base \(e>1\)),  
\[
\ln\bigl(x^2 - 4\bigr) > \ln\bigl(2x - 1\bigr)
\;\Longrightarrow\;
x^2 - 4 > 2x - 1.
\]

\subparagraph*{3. Risoluzione dell’inequazione}
\[
x^2 - 4 > 2x - 1
\quad\Longrightarrow\quad
x^2 - 2x - 3 > 0
\quad\Longrightarrow\quad
x^2 - 2x - 3 = (x - 3)(x + 1).
\]
L’espressione \((x-3)(x+1)\) è \textit{positiva} quando:
\[
x < -1 \quad\text{oppure}\quad x > 3.
\]
Ma il \textit{dominio} era \(x>2\). Dunque, intersecando \(x>2\) con \(\bigl(x<-1 \,\text{o}\, x>3\bigr)\), resta \(\,x>3\).

\subparagraph*{4. Soluzione Finale}
\[
\boxed{x > 3}, 
\]
sempre considerando \(x>2\) per il logaritmo. (L’intervallo \(2<x\le3\) non soddisfa l’inequazione \((x-3)(x+1)>0\).)

\noindent
\textbf{Osservazione}: in questa disequazione compaiono \textit{logaritmi} di espressioni polinomiali. Il passaggio cruciale è stato applicare la \textit{monotonia} del logaritmo (\(\ln\)) e poi risolvere la disuguaglianza polinomiale, sempre tenendo conto del \textit{dominio} iniziale.
\fi
\newpage

\section{Punti e Rette}

\noindent
Iniziamo ora un percorso attraverso i capitoli di studio della \textit{geometria}, partendo dalle nozioni fondamentali della \textbf{geometria piana}. Per prima cosa, esamineremo i concetti più elementari, come i \textit{punti} e le \textit{rette}, e le loro proprietà di base. Successivamente, passeremo alla costruzione di figure sul piano, quali i \textit{poligoni} e, in particolare, i \textit{triangoli}.

Proseguiremo poi collegando quanto appreso in \textit{algebra} con questa parte di geometria, introducendo la \textbf{geometria analitica}, in cui equazioni e coordinate si fondono con linee e curve nel piano. Infine, allargheremo lo sguardo alla \textbf{geometria solida}, applicando molte delle idee e delle tecniche già viste, ma in uno spazio tridimensionale. Questa sezione conclusiva, riguardante lo studio di volumi e figure nello spazio, fa parte della \textit{seconda tabella} di argomenti.

Nel corso di tutto questo itinerario incontreremo anche la \textbf{trigonometria}, dove introdurremo alcune funzioni (dette \textit{goniometriche}) che permettono di stabilire relazioni tra gli angoli e i lati, sia in ambito piano sia nelle configurazioni a tre dimensioni.

\paragraph{Il Punto ed il Piano Cartesiano}In geometria, un \textit{punto} rappresenta l’entità più semplice, priva di dimensioni, che possiamo collocare su un piano o nello spazio. Quando si lavora su un \textit{piano cartesiano}, ogni punto è identificato da una coppia di numeri \((x,\,y)\), detti \textit{coordinate}, che indicano la sua posizione rispetto a due assi perpendicolari (asse \(x\) e asse \(y\)). In questo modo, il \textit{piano cartesiano} non è altro che un sistema di riferimento formato da due rette orientate e perpendicolari, i cui punti di incrocio con il piano permettono di assegnare a ogni posizione una coppia di valori numerici, associando così l’algebra (i numeri) alla geometria (i punti del piano).

\noindent
Prima di approfondire lo studio delle \textit{coordinate}, osserviamo un esempio concreto sul \textbf{piano cartesiano}. Nel disegno sottostante, gli assi \(x\) e \(y\) si intersecano nell’origine \((0,0)\), e il punto \((2,1)\) è marcato da sottili linee tratteggiate che ne evidenziano le proiezioni orizzontali e verticali. In tal modo, risulta chiaro come la coppia di numeri \((2,1)\) indichi la posizione del punto: \(2\) unità lungo l’asse \(x\) e \(1\) unità lungo l’asse \(y\). Questa rappresentazione illustra la potenza del sistema di coordinate, che permette di tradurre la \textit{posizione geometrica} in un semplice \textit{insieme di valori numerici}. 

\begin{center}
\begin{tikzpicture}[scale=1.1, line cap=round, line join=round]

% Assi cartesiani
\draw[->] (-1,0) -- (4,0) node[right] {$x$};
\draw[->] (0,-1) -- (0,3) node[left] {$y$};

% Tacca e label sugli assi (opzionale, per contesto)
\foreach \x in {-1,1,2,3}{
  \draw (\x,0) -- (\x,0.1);
  \node[below] at (\x,0) {\small \x};
}
\foreach \y in {-1,1,2}{
  \draw (0,\y) -- (0.1,\y);
  \node[left] at (0,\y) {\small \y};
}

% Punto P(2,1)
\coordinate (P) at (2,1);

% Disegno del punto
\fill (P) circle(2pt);
\node[above right] at (P) {\small $(2,1)$};

% Linee tratteggiate sottili per segnare le coordinate
\draw[densely dotted, thin] (2,0) -- (2,1);
\draw[densely dotted, thin] (0,1) -- (2,1);

\end{tikzpicture}
\end{center}

\noindent
Un singolo punto \((x, y)\) è soltanto l’inizio: allo stesso modo, possiamo \textit{marcare interi insiemi di punti} su un piano cartesiano, e descriverli tramite \textit{equazioni}. Ogni equazione in due variabili \(x\) e \(y\) individua, infatti, un insieme di coppie \((x, y)\) che ne soddisfano la relazione, e la loro rappresentazione grafica è una \textit{figura geometrica} (una retta, una curva, o una regione del piano). Questo modo di collegare \textit{algebra} e \textit{geometria} sarà approfondito nella parte di \textbf{geometria analitica}, dove vedremo come studiare in dettaglio le forme, le posizioni e le proprietà di tali insiemi di punti. 

\newpage

\subsectionstar{[12] Rette e Fasci di Rette}
\subsubsection*{Rette nel Piano Cartesiano: Forme e Caratteristiche}

\paragraph{Equazione in Forma Esplicita: $y = m\,x + q$.}
Nel piano cartesiano \(\mathbb{R}^2\), una retta può essere descritta come
\[
y = m\,x + q,
\]
dove:
\begin{itemize}
    \item \(\,m\) è il \textbf{coefficiente angolare} (o \textbf{pendenza});
    \item \(\,q\) è il \textbf{termine noto} (o \textbf{intercetta} sull’asse \(y\)).
\end{itemize}

\begin{itemize}
    \item Se \(m>0\), la retta è \textit{crescente}; se \(m<0\), è \textit{decrescente}.
    \item Se \(|m|\) è \textit{grande}, la retta è più \textit{ripida}; se \(|m|\) è \textit{piccolo}, la retta è più \textit{piatta}.
    \item \(q\) indica il \textit{punto} in cui la retta \textit{incrocia l’asse \(y\)}, cioè il valore di \(y\) per \(x=0\).
\end{itemize}

\paragraph{Equazione in Forma Implicita: $a\,x + b\,y + c = 0$.}
Un’altra rappresentazione di retta:
\[
a\,x + b\,y + c = 0,
\]
con \((a,b)\neq(0,0)\). Questa forma è utile per includere anche le \textit{rette verticali} (dove altrimenti \(m\) sarebbe infinito).

\begin{itemize}
    \item \(\mathbf{Retta\;propria}\): se \((a,b)\neq(0,0)\) e l’insieme di soluzioni è un \textit{sottoinsieme} infinito di \(\mathbb{R}^2\).
    \item \(\mathbf{Retta\;impropria}\): casi degeneri, ad es. \(0\cdot x +0\cdot y +c=0\) con \(c\neq0\) (nessun punto) o \(c=0\) (l’intero piano).
\end{itemize}

\paragraph{Esempio Grafico: Varie Rette nel Piano.}
Nel diagramma seguente (\texttt{tikz}) mostriamo diverse rette, mettendo in evidenza come i parametri \((m,q)\) o \((a,b,c)\) ne determinino pendenza, posizione e parallelismo.

\begin{center}
\begin{tikzpicture}[scale=0.9]
    % Assi cartesiani
    \draw[->] (-3.5,0)--(3.5,0) node[right]{$x$};
    \draw[->] (0,-3.5)--(0,3.5) node[above]{$y$};

    % 1) Retta y = x + 1
    \draw[domain=-3:3, samples=200, thick, blue]
        plot(\x,{(\x) +1});
    \node[blue] at (1.6,2.7) {$y = x + 1$};

    % 2) Retta y = -2x + 2
    \draw[domain=-1.5:3, samples=200, thick, red]
        plot(\x,{(-2)*\x +2});
    \node[red] at (-2,4) {$y = -\,2x + 2$};

    % 3) Retta y = 0.5x - 1
    \draw[domain=-3:3, samples=200, thick, teal]
        plot(\x,{0.5*\x -1});
    \node[teal] at (1.6, -0.3) {$y = 0.5\,x - 1$};

    % 4) Retta verticale x = -1
    \draw[purple, thick] (-1,-3.5)--(-1,3.5);
    \node[purple] at (-0.8,3.2) {$x = -1$};

    % 5) Retta orizzontale y = 2
    \draw[orange, thick] (-3.5,2)--(3.5,2);
    \node[orange] at (3.2,2.3) {$y = 2$};

    % Origine
    \filldraw (0,0) circle(1.2pt) node[below left]{$O$};

\end{tikzpicture}
\end{center}

\paragraph{Osservazioni sul Grafico.}
\begin{itemize}
    \item \(\mathbf{y = x +1}\): pendenza \(m=1\) (retta crescente), intercetta \(+1\).
    \item \(\mathbf{y = -2x +2}\): pendenza negativa \(m=-2\), intercetta \(+2\).
    \item \(\mathbf{y = 0.5x -1}\): pendenza \(m=0.5\) (crescente ma meno ripida), intercetta \(-1\).
    \item \(\mathbf{x = -1}\): retta verticale, non definibile come \(y=mx+q\).
    \item \(\mathbf{y = 2}\): retta orizzontale, con \(m=0\).
\end{itemize}

\subsubsection*{Rette Parallele e Perpendicolari}
\begin{itemize}
    \item \(\mathbf{Parallele}\): In forma esplicita, due rette \(y=m_1x +q_1\) e \(y=m_2x +q_2\) sono \textit{parallele} se \(m_1=m_2\). In forma implicita, \(a_1x + b_1y + c_1=0\) e \(a_2x + b_2y + c_2=0\) sono parallele se \((a_1,b_1)\) è \textit{proporzionale} a \((a_2,b_2)\).
    \item \(\mathbf{Perpendicolari}\): In forma esplicita, due rette con pendenze \(m_1\) e \(m_2\) sono \textit{perpendicolari} se \(m_1\,m_2 = -1\) (purché non verticali/orizzontali).
\end{itemize}
\subsubsection*{Fasci di Rette: Definizione Essenziale}

Un \textbf{fascio di rette} è un insieme infinito di rette che condividono una caratteristica comune. Si distinguono due tipi principali:

\paragraph{Fascio Proprio (o Convergente).}
Tutte le rette passano per \textit{uno stesso punto} \(P=(x_0,y_0)\). In forma esplicita:
\[
y - y_0 = m\,(x - x_0),
\]
dove \(m\) varia su \(\mathbb{R}\). Ciascun valore di \(m\) definisce una retta differente, tutte convergenti nel punto \(P\).

\paragraph{Fascio Improprio (o Parallelo).}
Tutte le rette hanno la \textit{stessa pendenza} e dunque sono \textit{parallele} fra loro. In forma esplicita:
\[
y = m\,x + q,
\]
dove \(m\) è fisso e \(q\) varia su \(\mathbb{R}\). Ogni diverso \(q\) sposta la retta parallelamente verso l’alto o il basso, mantenendo la medesima inclinazione \(m\).

\paragraph{Osservazione.}
Nel \textit{fascio proprio}, il “centro” è un punto finito del piano. Nel \textit{fascio improprio}, il “centro” può considerarsi idealmente all’infinito, poiché le rette non si incontrano mai (sono parallele).
\newpage

\subsectionstar{[14*] Equazione Segmentaria della Retta} 
Una delle forme più intuitive per rappresentare una retta nel piano cartesiano è quella in cui la retta è descritta in termini degli \textit{intercetti} con gli assi. Se una retta interseca l'asse \(x\) nel punto \((p,0)\) e l'asse \(y\) nel punto \((0,q)\), la sua equazione in forma segmentaria (o intercettale) è:
\[
\frac{x}{p} + \frac{y}{q} = 1.
\]
Questa equazione ha un significato geometrico immediato: ogni punto \((x,y)\) appartenente alla retta soddisfa il fatto che la frazione del segmento \(OP\) (lunghezza \(p\)) occupata da \(x\) sommata alla frazione del segmento \(OQ\) (lunghezza \(q\)) occupata da \(y\) è uguale a 1. In altre parole, se un punto si trova, ad esempio, a metà strada lungo l'intercetta sull'asse \(x\) (\(x=p/2\)), allora per appartenere alla retta deve valere anche che \(y\) sia pari a \(q/2\) (cioè \(y/q = 1/2\)), in modo tale che:
\[
\frac{p/2}{p}+\frac{q/2}{q}=\frac{1}{2}+\frac{1}{2}=1.
\]

\begin{center}
\begin{tikzpicture}[scale=1.0]
  % Disegno del sistema di assi
  \draw[->, thick] (-1,0) -- (6,0) node[right] {\(x\)};
  \draw[->, thick] (0,-1) -- (0,5) node[above] {\(y\)};
  
  % Punti di intercetta
  \coordinate (P) at (5,0); % Intercetta sull'asse x
  \coordinate (Q) at (0,4); % Intercetta sull'asse y
  
  % Etichette degli intercetti
  \node[below] at (P) {\((p,0)\), con \(p=5\)};
  \node[left] at (Q) {\((0,q)\), con \(q=4\)};
  
  % Disegno della retta in forma segmentaria
  \draw[thick, red] (P) -- (Q);
  
  % Etichetta della retta
  \node at (3,2.5) {\(\frac{x}{5}+\frac{y}{4}=1\)};
\end{tikzpicture}
\end{center}

\medskip

Notiamo che la formula classica della retta, che siamo soliti notare con $y = mx + q$, è equivalente a quest formula. Entrambe le equazioni descrivono una retta, sono riformulate però in termini diversi in modo da spostare il focus su fenomeni diversi. Se volessimo, partendo dai punti di incidenza, e quindi dalla retta nella forma segmentaria, tornare alla formulazione classica, basta seguire i seguenti passaggi.

Si parte dai punti noti \((p,0)\) e \((0,q)\). Il coefficiente angolare della retta è:
\[
m = \frac{q-0}{0-p}=-\frac{q}{p}.
\]

Otteniamo quindi:
\[
y-0=-\frac{q}{p}(x-p)\quad\Longrightarrow\quad y=-\frac{q}{p}x+q.
\]

Notiamo che questa formula è il caso specifico della formula che ci permette di trovare il coefficiente angolare della retta dati qualsiasi due punti appartenenti alla retta, questa infatti è:
Utilizzando il punto \(A(p,0)\) e la forma punto-pendenza, l'equazione è:
\[
m = \frac{y_2 - y_1}{x_2 - x_1}.
\]


\noindent\textbf{Esempio}
Supponiamo di avere una retta espressa in forma pendenza-intercettale:
\[
y = -\frac{1}{3}x + \frac{17}{3}.
\]
Da questa forma possiamo calcolare gli intercetti:
\begin{itemize}
  \item Intercetta sull'asse \(y\): ponendo \(x=0\), si ha \(y=\frac{17}{3}\). Quindi la retta interseca l'asse \(y\) in \((0,\frac{17}{3})\).
  \item Intercetta sull'asse \(x\): ponendo \(y=0\), risolviamo
  \[
  0=-\frac{1}{3}x+\frac{17}{3}\quad\Longrightarrow\quad x=17.
  \]
  Quindi l'intercetta sull'asse \(x\) è \((17,0)\).
\end{itemize}
La forma segmentaria (o intercettale) della retta è dunque:
\[
\frac{x}{17}+\frac{y}{\frac{17}{3}}=1 \quad\Longrightarrow\quad \frac{x}{17}+\frac{3y}{17}=1,
\]
che, moltiplicando per 17, diventa
\[
x+3y=17.
\]
Questa trasformazione evidenzia come si possa passare dalla forma pendenza-intercettale alla forma segmentaria, identificando chiaramente gli intercetti.

\bigskip

\noindent\textbf{Esempio}
Supponiamo di avere due punti \(A(2,5)\) e \(B(8,3)\) appartenenti a una retta (entrambi non situati sugli assi). Per determinare l'equazione della retta in forma segmentaria, seguiamo questi passaggi:

   \[
   m=\frac{y_B-y_A}{x_B-x_A}=\frac{3-5}{8-2}=\frac{-2}{6}=-\frac{1}{3}.
   \]


\noindent   Utilizzando il punto \(A(2,5)\):
   \[
   y-5=-\frac{1}{3}(x-2) \quad\Longrightarrow\quad y=-\frac{1}{3}x+ \frac{2}{3}+5=-\frac{1}{3}x+\frac{17}{3}.
   \]


\noindent Per l'intercetta sull'asse \(y\): con \(x=0\),
       \[
       y=\frac{17}{3}.
       \]
\noindent Per l'intercetta sull'asse \(x\): con \(y=0\),
       \[
       0=-\frac{1}{3}x+\frac{17}{3}\quad\Longrightarrow\quad x=17.
       \]

\noindent   La forma segmentaria diventa quindi:
   \[
   \frac{x}{17}+\frac{y}{\frac{17}{3}}=1,
   \]
\noindent   che equivale a
   \[
   x+3y=17.
   \]

\begin{center}
\begin{tikzpicture}[scale=0.5]
  % Assi cartesiani
  \draw[->, thick] (-1,0) -- (20,0) node[right] {\(x\)};
  \draw[->, thick] (0,-1) -- (0,8) node[above] {\(y\)};
  
  % Punti dati non sugli assi
  \fill[blue] (2,5) circle (3pt) node[above right] {\(A(2,5)\)};
  \fill[blue] (8,3) circle (3pt) node[above right] {\(B(8,3)\)};
  
  % Disegno della retta passante per A e B
  \draw[red, thick] (2,5) -- (8,3);
  % Estendiamo la retta fino agli assi:
  \draw[red, thick] (17,0) -- (0,17/3);
  
  % Etichette degli intercetti
  \fill[black] (17,0) circle (2pt) node[below] {\((17,0)\)};
  \fill[black] (0,{17/3}) circle (2pt) node[left] {\(\Bigl(0,\frac{17}{3}\Bigr)\)};
  
  % Scriviamo la forma segmentaria
  \node at (8, -1) {\( \frac{x}{17}+\frac{y}{17/3}=1 \quad\Longleftrightarrow\quad x+3y=17 \)};
\end{tikzpicture}
\end{center}


\newpage
\subsectionstar{[8] Distanza}

Il \textit{piano cartesiano} \(\mathbb{R}^2\) è costituito da tutti i \textit{punti} identificati da una coppia ordinata di numeri reali \((x,y)\). In altre parole, un \textit{punto} \(P\) è definito dalla sua \textit{ascissa} \(x\) (posizione orizzontale) e dalla sua \textit{ordinata} \(y\) (posizione verticale). Per sviluppare al meglio l'intuizione di come sia costituito questo spazio, vedi l'introduzione alla sezione. Una seconda nozione fondamentale che ci serve è quella di spazio metrico che ci permette di misurare la distanza all'interno del piano cartesiano.

Un \textit{spazio metrico} è un insieme \(X\), che nel nostro caso sarà $\b{R}^2$ che abbiamo introdotto prima, dotato di una funzione \textit{distanza} \(d(\cdot,\cdot)\) che, per ogni coppia di punti \(p,q \in X\), restituisce un numero reale non negativo.

Nel \textit{piano euclideo} \(\mathbb{R}^2\), la \textit{distanza} fra due punti \(P=(x_1,y_1)\) e \(Q=(x_2,y_2)\) è definita da:
\[
d(P,Q) 
= \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}.
\]
Questa formula discende dal \textit{teorema di Pitagora}, è infatti semplice vedere come questo rispecchi il modo che abbiamo intuitivamente di misurare la distanza tra due punti come la misura del segmento che li collega. La misura di quel segmento, guardando alle sue componenti nelle ascisse e nelle ordinate, può infatti essere facilmente calcolato con il teorema di Pitagora.

Una \textit{retta} in \(\mathbb{R}^2\) è l’insieme dei punti che soddisfano un’equazione \textit{lineare} del tipo:
\[
a\,x \;+\; b\,y \;+\; c = 0,
\]
con \(a,b \in \mathbb{R}\) non entrambi nulli. Questa forma si chiama \textit{forma implicita}. Un punto \((x,y)\) appartiene alla retta se, sostituendo le sue coordinate nell’equazione, l’uguaglianza risulta vera.

Dato un punto \(P=(x_0,y_0)\) e una retta \(r\colon a\,x + b\,y + c=0\), la \textit{distanza} fra \(P\) e \(r\) è la lunghezza del \textit{segmento perpendicolare} che collega \(P\) alla retta \(r\). In termini analitici, si ottiene con la formula:
\[
d\bigl(P,\,r\bigr)
= \frac{\bigl|\,a\,x_0 + b\,y_0 + c\,\bigr|}
       {\sqrt{a^2 + b^2}}.
\]
Questa espressione garantisce che, fra tutte le possibili distanze da \(P\) a un punto generico della retta, la più \textit{corta} sia proprio quella \textit{perpendicolare}.

Ribadiamo quindi quale sia il significato geometrico della distanza tra due punti e della distanza tra un punto ed una retta. Metteremo a breve in pratica queste nozioni con degli esempi e dei disegni.
\begin{itemize}
    \item \textbf{Distanza fra due punti}: è la \textit{lunghezza} del segmento che li unisce; in geometria euclidea, il percorso più breve fra due punti è sempre il \textit{segmento} che li collega.
    \item \textbf{Distanza fra un punto e una retta}: è la \textit{minima} distanza che si possa ottenere spostandosi dal punto \(P\) a uno qualunque dei punti della retta. Il segmento corrispondente è \textit{perpendicolare} alla retta.
\end{itemize}

L’idea di \textit{distanza} come \textit{minimo percorso} è coerente con la definizione di spazio metrico:
\begin{itemize}
    \item La distanza fra punti \(\,(x_1,y_1)\) e \((x_2,y_2)\)\, rispetta la \textit{triangolarità}: data un terzo punto \(R\), la somma \(d(P,R)+d(R,Q)\) non è mai minore di \(d(P,Q)\).
    \item La \textit{distanza fra un punto e una retta} nasce dall’applicazione di questa stessa metrica, cercando fra \textit{tutti} i punti della retta quello che minimizza la distanza dal punto esterno.
\end{itemize}

\subsubsection*{Esempio: Distanza fra Due Punti}
Siano \(P=(1,3)\) e \(Q=(4,7)\). La distanza \(PQ\) è data da
\[
PQ = \sqrt{(4 - 1)^2 + (7 - 3)^2}
    = \sqrt{3^2 + 4^2}
    = 5.
\]
Nel seguente diagramma mostriamo i punti \(P\) e \(Q\) nel piano cartesiano e il segmento \(PQ\).

\begin{center}
\begin{tikzpicture}[scale=0.8]
    % Assi cartesiani
    \draw[->] (-1,0)--(6,0) node[right]{$x$};
    \draw[->] (0,-1)--(0,8) node[above]{$y$};

    % Griglia facoltativa (commentare se non serve)
    %\draw[step=1,lightgray,thin] (-1,-1) grid (6,8);

    % Punti
    \coordinate (P) at (1,3);
    \coordinate (Q) at (4,7);

    % Disegno i punti
    \filldraw[blue] (P) circle(2pt) node[below right] {$P(1,3)$};
    \filldraw[blue] (Q) circle(2pt) node[above right] {$Q(4,7)$};

    % Segmento PQ
    \draw[thick] (P)--(Q);

    % Eventuali linee ausiliarie orizzontali/verticali
    %\draw[dashed] (P) -- ++(0,4) -- (Q);

    % Etichetta distanza
    \node at ($(P)!0.5!(Q) + (1.2,0.0)$) {$PQ = 5$};

    % Origine
    \filldraw (0,0) circle(1pt) node[below left]{$O$};

\end{tikzpicture}
\end{center}


\subsubsection*{Esempio: Distanza fra un Punto e una Retta}
Siano la retta \(r\) di equazione \(2x - y + 1 = 0\) e il punto \(P=(3,2)\). La distanza fra \(P\) e \(r\) si calcola con
\[
d(P,r) 
= \frac{|\,2\cdot3 -1\cdot2 +1\,|}{\sqrt{2^2 +(-1)^2}}
= \frac{|\,6 -2 +1\,|}{\sqrt{4 +1}}
= \frac{5}{\sqrt{5}}
= \sqrt{5}.
\]
Nel grafico sottostante, mostriamo la retta \(r\) e il punto \(P\). Tracciamo la perpendicolare a \(r\) passante per \(P\) e individuiamo il piede \(H\) sulla retta. Il segmento \(PH\) rappresenta la distanza cercata.

\begin{center}
\begin{tikzpicture}[scale=0.8]
    % Assi cartesiani
    \draw[->] (-1,0)--(5,0) node[right]{$x$};
    \draw[->] (0,-1)--(0,5) node[above]{$y$};

    % Griglia facoltativa (commentare se non serve)
    %\draw[step=1,lightgray,thin] (-1,-1) grid (5,5);

    % Retta r: 2x - y +1=0 => y=2x+1
    % Disegno la retta su un certo intervallo di x, ad es. x in [-1,4].
    \draw[domain=-1:3, thick, red]
        plot(\x,{2*\x +1});

    % Punto P
    \coordinate (P) at (3,2);

    % Disegno P
    \filldraw[blue] (P) circle(2pt) node[below left]{$P(3,2)$};

    % Calcolo del piede H
    % r: y=2x+1, slope=2
    % Perp: slope=-1/2, eq => y-2= -1/2(x-3)
    % => y= -1/2 x + 3/2 +2= -1/2 x +7/2
    % Intersezione con r => 2x+1= -1/2 x +7/2 => ...
    % Da calcoli, H=(1,3).

    \coordinate (H) at (1,3);
    \filldraw (H) circle(2pt) node[above right]{$H$};

    % Disegno il segmento PH
    \draw[dashed,blue] (P)--(H);

    % Indico la distanza
    \node at ($(P)!0.5!(H) + (0.0,0.5)$) {$\sqrt{5}$};

    % Origine
    \filldraw (0,0) circle(1pt) node[below left]{$O$};

\end{tikzpicture}
\end{center}
\newpage

\subsectionstar{[4] Rette Parallele e Perpedicolari}
\noindent
In \(\mathbb{R}^2\), due rette possono presentarsi in \textbf{tre} modi fondamentali:

\begin{itemize}
    \item \textbf{Parallele}: non si incontrano mai (o coincidono interamente se condividono ogni punto).
    \item \textbf{Coincidenti}: in realtà è un caso particolare di rette parallele, ma in cui ogni loro punto coincide.
    \item \textbf{Incidenti}: si intersecano in un \emph{unico} punto. Se l’angolo formato è di \(90^\circ\), si parla di \emph{rette perpendicolari}.
\end{itemize}

Nel disegno seguente, le prime due rette (in rosso e blu) sono \textit{parallele}, mentre la terza (in verde) è \textit{perpendicolare} alle prime due:

\begin{center}
\begin{tikzpicture}[scale=0.8]
    % Assi
    \draw[->] (-3,0)--(3,0) node[right]{$x$};
    \draw[->] (0,-2.5)--(0,2.5) node[above]{$y$};

    % Retta 1: y = 0.5x + 1 (rossa)
    \draw[domain=-3:3, thick, red] 
        plot(\x,{0.5*\x + 1});

    % Retta 2: y = 0.5x - 1 (blu, parallela a retta 1)
    \draw[domain=-3:3, thick, blue] 
        plot(\x,{0.5*\x -1});

    % Retta 3: y = -2x (verde, perpendicolare alle prime due)
    \draw[domain=-2:2, thick, green!70!black] 
        plot(\x,{(-2)*\x});

    % Origine
    \filldraw (0,0) circle(1.2pt);
\end{tikzpicture}
\end{center}
Vediamo ora come poter determinare dall'equazione di dure rette se queste sono parallele o se queste sono perpendicolari.

\paragraph{Condizione Analitica per Rette Parallele.}
Se due rette sono in \textit{forma esplicita}:
\[
r_1: y = m_1\,x + q_1,
\quad
r_2: y = m_2\,x + q_2,
\]
allora \(\,r_1\) e \(\,r_2\) sono \textbf{parallele} se e solo se 
\[
m_1 = m_2.
\]
Questo significa che hanno la stessa pendenza e differiscono solo nel termine noto (\(q_1\neq q_2\)). Vediamo rapidamente un semplice esempio:
\[
r_1:\;y=2x+3,
\quad
r_2:\;y=2x-5.
\]
Entrambe hanno coefficiente angolare \(m=2\), quindi sono parallele.

\paragraph{Condizione Analitica per Rette Perpendicolari.}
Se \(\,r_1:\;y=m_1\,x+q_1\) e \(\,r_2:\;y=m_2\,x+q_2\), allora \(\,r_1\) e \(\,r_2\) sono \textbf{perpendicolari} se e solo se
\[
m_1\,m_2 = -1,
\]
purché nessuna delle due sia verticale. In caso di retta verticale \((x=k)\) e retta orizzontale \((y=c)\), esse sono perpendicolari a prescindere dalla formula. Vediamo rapidamente un semplice esempio:
\[
r_1:\;y=\tfrac{1}{2}x+2,
\quad
r_2:\;y=-2x+1.
\]
I loro coefficienti angolari sono \(m_1=\tfrac{1}{2}\) e \(m_2=-2\). Poiché \(\tfrac{1}{2}\cdot(-2)=-1\), le due rette sono perpendicolari.

\noindent
\textbf{Rette e Sistemi di Equazioni di Primo Grado}

\smallskip
\noindent
Come abbiamo visto quindi ogni polinomio di primo grado in una variabile, una volta eguagliato ad $y$, corrisponde ad una certa retta. È importante per poter connettere questo argomento con la parte di algebra, capire a fondo questa corrispondenza. Quando parlaimo di rette parallele, coincidenti o incidenti, ci stiamo riferendo a coppie di rette, ci aspettiamo quindi che il modo di indagare queste relazioni dal punto di vista algebraico coinvolda due polinomi di primo grado. Negli esempi seguenti vedremo infatti come le i punti di intersezione tra le rette possono essere investigati guardando alle soluzioni dei sistemi tra le equazioni dei corrispondenti polinomi. Teniamo a mente la seguente corrispondenza e vedimola in pratica in alcuni esempi:

\begin{itemize}
  \item \textbf{Parallele}: non hanno punti in comune \(\Longrightarrow\) il \emph{sistema} di equazioni corrispondente \emph{non ha soluzioni} (\textit{impossibile}).
  \item \textbf{Coincidenti}: coincidono interamente \(\Longrightarrow\) il sistema ammette \emph{infinite soluzioni} (\textit{indeterminato}).
  \item \textbf{Incidenti}: si intersecano in un solo punto \(\Longrightarrow\) il sistema ha \emph{un’unica soluzione} (\textit{determinato}).
\end{itemize}

\smallskip
\noindent
\textbf{Esempi di Sistemi:}
\begin{itemize}
  \item \emph{Senza soluzioni (rette parallele)}: 
  \[
    \begin{cases}
      y - x = -1,\\
      y - x = 2.
    \end{cases}
  \]
  Qui i due polinomi hanno lo stesso coefficiente angolare (\(y-x\)) ma costanti diverse (\(-1\) e \(2\)): le rette non si incontrano, quindi \emph{nessuna} coppia \((x,y)\) soddisfa entrambe le equazioni.

  \item \emph{Infinite soluzioni (rette coincidenti)}: 
  \[
    \begin{cases}
      y - x = -1,\\
      y - x = -1.
    \end{cases}
  \]
  Le due equazioni descrivono la \emph{stessa} retta, per cui \emph{tutti} i punti della retta sono soluzioni (sistema \textit{indeterminato}).

  \item \emph{Un’unica soluzione (rette incidenti)}:
  \[
    \begin{cases}
      y - x = -1,\\
      y + 2x = 2.
    \end{cases}
  \]
  I due polinomi hanno coefficienti angolari diversi, dunque le rette si incrociano in \emph{un solo} punto, dando \emph{un’unica soluzione} (sistema \textit{determinato}).
\end{itemize}

\smallskip
\noindent
In seguito, tratteremo più nel dettaglio i \emph{metodi} per risolvere i sistemi di equazioni (sostituzione, riduzione) e torneremo a discutere del rapporto fra \emph{algebra} e \emph{geometria} nella parte dedicata alla \textbf{geometria analitica}, dove queste idee costituiranno la base per comprendere a fondo l’interpretazione geometrica dei sistemi. 

\newpage


\subsectionstar{[30] Rette Parallele Intersecate da una Trasversale}
\noindent
Per iniziare, ricordiamo la terminologia di base per poter parlare di angoli:

\begin{center}
\renewcommand{\arraystretch}{1.2}
\begin{tabular}{|l|p{8.5cm}|}
\hline
\textbf{Termine} & \textbf{Definizione o Descrizione} \\
\hline
\textit{Angolo acuto} & Misura minore di \(90^\circ\). \\
\hline
\textit{Angolo retto} & Misura esattamente \(90^\circ\). \\
\hline
\textit{Angolo ottuso} & Misura compresa tra \(90^\circ\) e \(180^\circ\). \\
\hline
\textit{Angoli complementari} & La loro somma è \(90^\circ\). \\
\hline
\textit{Angoli supplementari} & La loro somma è \(180^\circ\). \\
\hline
\textit{Angoli adiacenti} & Due angoli che condividono un \textit{lato} e i cui altri lati sono semirette opposte. \\
\hline
\end{tabular}
\end{center}
Passiamo ora alla figura geometrica di interesse per questa sezione.

Questo argomento si bassa su una costruzione geometrica particolarmente semplice e che per questo ritroveremo in tanti cotesti diversi. Utilizzeremo infatti questa costruzione in futuro per vedere diversi risultati che ne seguono. Partiamo dal definire i tre elementi principali della costruzione, ci serviranno infatti due rette parallele ed una retta incidente.

Consideriamo due \textit{rette parallele} \(r_1\) e \(r_2\) (non si intersecano mai) e una \textit{retta trasversale} \(t\) che le \textit{taglia} in due punti distinti. Nei punti di intersezione si formano \textit{otto} angoli.

\begin{center}
\begin{tikzpicture}[scale=0.8]
    % Disegno le parallele
    \draw[thick] (-3,1)--(3,1) node[right]{$r_1$};
    \draw[thick] (-3,-1)--(3,-1) node[right]{$r_2$};

    % Disegno la trasversale t
    \draw[thick] (-2.5,-2)--(2.5,2) node[right]{$t$};

\end{tikzpicture}
\end{center}

\noindent
Per comprendere i risultati elencati nella tabella sottostante, immaginiamo di disegnare due rette parallele, che indicheremo con \(r_1\) e \(r_2\), e una retta trasversale che le interseca. Sul disegno, si formano diverse coppie di angoli. Possiamo distinguere:

\begin{itemize}
  \item \textit{Angoli corrispondenti}: prendiamo un angolo in alto a sinistra (rispetto alla trasversale) su \(r_1\) e il “corrispondente” angolo in alto a sinistra su \(r_2\). Analogamente, si identificano altre coppie con la stessa “posizione” rispetto alle due rette parallele. Dal disegno, risulta evidente che quando \(r_1 \parallel r_2\), la trasversale forma angoli “uguali” in quelle posizioni corrispondenti.

  \item \textit{Angoli alterni interni}: sono gli angoli che si trovano fra le due rette parallele, ma su lati opposti della trasversale (ad esempio, uno in alto a sinistra, l’altro in basso a destra). Osservando il disegno, si nota che se \(r_1 \parallel r_2\), la trasversale taglia entrambe con la stessa inclinazione, generando angoli “speculari” che risultano uguali.

  \item \textit{Angoli alterni esterni}: in modo analogo, questi angoli si trovano “fuori” dalle due parallele, pur rimanendo su lati opposti della trasversale. Il disegno mostra come tali angoli siano effettivamente congruenti quando le rette sono parallele, poiché la trasversale crea lo stesso “schema” di intersezione fuori da \(r_1\) e \(r_2\).

  \item \textit{Angoli coniugati interni} (o interni dallo stesso lato): qui si considerano gli angoli che stanno entrambi “dentro” alle due parallele, ma sullo stesso lato della trasversale (per esempio, in alto a sinistra e in basso a sinistra, o viceversa). Dalla figura, si nota che la somma di tali angoli si “chiude” su una linea retta se \(r_1\parallel r_2\). Pertanto, questi due angoli risultano \textit{supplementari}, ossia la loro somma è \(180^\circ\).

\end{itemize}

\noindent
La chiave per giungere a queste conclusioni sta nel riconoscere che, con \(\,r_1 \parallel r_2,\) la trasversale forma \textit{angoli uguali} o \textit{angoli supplementari} in determinate posizioni, poiché gli “angoli corrispondenti” replicano la stessa inclinazione, e gli “angoli alterni” appaiono come immagini speculari rispetto a una retta. Nel caso degli “angoli coniugati interni”, la rettifica geometrica dimostra che se un angolo “interno” si allarga, l’altro si riduce, fino a completare una linea retta. Tutti questi fatti sono verificabili sul disegno osservando con attenzione la configurazione e misurando (o ragionando sulle parallele e i prolungamenti) gli angoli formati dalla trasversale. 


\begin{center}
\renewcommand{\arraystretch}{1.2}
\begin{tabular}{|l|p{7cm}|p{4cm}|}
\hline
\textbf{Termine} & \textbf{Definizione} & \textbf{Risultato con} $\boldsymbol{r_1\parallel r_2}$ \\
\hline
\textit{Angoli corrispondenti} 
& Occupano la “stessa posizione” rispetto a due rette $r_1$ e $r_2$ e alla trasversale. 
& Risultano \textit{uguali}. \\
\hline
\textit{Angoli alterni interni} 
& Si trovano tra le due parallele, su lati opposti della trasversale. 
& Risultano \textit{uguali}. \\
\hline
\textit{Angoli alterni esterni} 
& Stanno “fuori” dalle parallele, sempre su lati opposti della trasversale. 
& Risultano \textit{uguali}. \\
\hline
\textit{Angoli coniugati interni} 
& Detti anche \textit{interni dallo stesso lato}, sono gli angoli che si trovano entrambi tra le due rette e sullo stesso lato della trasversale. 
& Sono \textit{supplementari}. \\
\hline
\end{tabular}
\end{center}

\smallskip
\noindent
Consideriamo due rette parallele \(r_1\) e \(r_2\), intersecate da una trasversale \(t\). Supponiamo di conoscere \textit{un solo angolo} formato tra la trasversale e \(r_1\), precisamente l’\textit{angolo in basso a sinistra} di \(60^\circ\). Poiché \(r_1 \parallel r_2\), gli altri angoli che si formano — siano essi corrispondenti, alterni interni o esterni — risultano \textit{uguali} a \(60^\circ\) o \textit{supplementari} (ossia \(120^\circ\)) in base alla loro posizione. In tal modo, \textit{conoscendo un solo angolo}, si possono ricostruire \textit{tutti} i valori angolari nella configurazione, grazie alle proprietà delle parallele tagliate da una trasversale.

\begin{center}
\begin{tikzpicture}[scale=0.6, line cap=round, line join=round]

% Rette parallele r1: y=0 e r2: y=-2
\draw[thick] (-1,0) -- (5,0) node[right] {\small $r_1$};
\draw[thick] (-1,-2) -- (5,-2) node[right] {\small $r_2$};

% Punto P su r1
\coordinate (P) at (2,0);

% Costruiamo la trasversale in modo da creare un angolo di 60° in basso a sinistra
% Definiamo slope=tan(60)=sqrt(3), passante per P
% Intersezione con r2: y=-2 => -2 = sqrt(3)(x-2) => x=2 - 2/sqrt(3)
\coordinate (Q) at ({2 - 2/sqrt(3)},-2);

% Disegno della trasversale (estendendola un po' oltre i punti P e Q)
\draw[thick] ($(Q)+(-0.6,{-0.6*sqrt(3)})$) -- ($(P)+(0.6,{0.6*sqrt(3)})$);

% Marcatura dei punti P e Q
\fill (P) circle(2pt) node[above left] {\small $P$};
\fill (Q) circle(2pt) node[below right] {\small $Q$};

\end{tikzpicture}
\end{center}

\noindent
Le proprietà sulle rette parallele e gli angoli ci consentono di dimostrare che, in un \textit{parallelogramma}, gli angoli opposti risultano \textbf{uguali} a coppie. Infatti, un parallelogramma è definito da due coppie di lati \textit{opposti e paralleli}: se consideriamo i lati \(AB \parallel DC\) e \(AD \parallel BC\), possiamo trattare ciascuna coppia di lati paralleli come \textit{rette parallele} tagliate dalle \textit{trasversali} che congiungono i vertici, concludendo che gli \textit{angoli opposti} coincidono (o sono \textit{congruenti}).

\begin{center}
\begin{tikzpicture}[scale=0.7, line cap=round, line join=round]

% Vertici del parallelogramma ABCD
\coordinate (A) at (0,0);
\coordinate (B) at (3,0);
\coordinate (C) at (4,2);
\coordinate (D) at (1,2);

% Disegno del parallelogramma
\draw[thick] (A)--(B)--(C)--(D)--cycle;

% Etichette dei vertici con i nomi degli angoli
\node[below left] at (A) {\small A};
\node[below right] at (B) {\small B};
\node[above right] at (C) {\small C};
\node[above left] at (D) {\small D};

\end{tikzpicture}
\end{center}

\noindent
Nella figura, i lati \(AB\) e \(DC\) risultano \textit{paralleli}, così come \(AD\) e \(BC\). Considerando ciascuna coppia di lati paralleli come \textit{rette parallele} e gli altri due lati come \textit{trasversali}, si applicano le nozioni di \textit{angoli corrispondenti}, \textit{alterni interni}, \textit{alterni esterni} e \textit{coniugati interni}. Da queste relazioni segue che 
\[
\angle A = \angle C
\quad\text{e}\quad
\angle B = \angle D,
\]
ma anche
\[
\angle A + \angle B = 180^\circ
\quad\text{e}\quad
\angle C + \angle D = 180^\circ,
\]
dimostrando che gli angoli opposti in un parallelogramma sono \textit{uguali} a coppie, mentre gli angoli adiacenti sono \textit{supplementari}. 
\newpage

\subsectionstar{[20] Proporizioni e Teorema di Talete}
Il \textit{Teorema di Talete} stabilisce che, se due rette parallele intersecano i lati di un angolo (o i loro prolungamenti), i segmenti che ne derivano sono in \textit{proporzione}. 

\begin{center}
\begin{tikzpicture}[scale=0.9]

% Due linee orizzontali (rette parallele) "r" e "s"
\draw[thick] (-1,0)--(5,0) node[right]{$r$};
\draw[thick] (-1,-2)--(5,-2) node[right]{$s$};

% Definiamo i punti estremi delle due semirette oblique (in basso si incontrano in M)
% Prima semiretta: da (0,1) a (2,-3)
% Seconda semiretta: da (4,1) a (2,-3)
\draw[thick] (0,1)--(2,-3);
\draw[thick] (4,1)--(2,-3);

% Calcoliamo le intersezioni con r (y=0) e s (y=-2) per ciascuna semiretta
% Semiretta 1: (0,1) --> (2,-3)
%   Intersezione con y=0: A=(0.5,0)
%   Intersezione con y=-2: B=(1.5,-2)
\coordinate (A) at (0.5, 0);
\coordinate (B) at (1.5, -2);

% Semiretta 2: (4,1) --> (2,-3)
%   Intersezione con y=0: A'=(3.5,0)
%   Intersezione con y=-2: B'=(2.5,-2)
\coordinate (A') at (3.5, 0);
\coordinate (B') at (2.5, -2);

% Punto M in basso, incrocio delle due semirette
\coordinate (M) at (2, -3);

% Disegno i punti di intersezione
\fill (A) circle(1.2pt) node[above right]{$A$};
\fill (B) circle(1.2pt) node[below left]{$B$};
\fill (A') circle(1.2pt) node[above left]{$A'$};
\fill (B') circle(1.2pt) node[below right]{$B'$};
\fill (M) circle(1.2pt) node[below]{$M$};

\end{tikzpicture}
\end{center}

Nella figura, le due rette parallele orizzontali sono indicate con $r$ e $s$. Le due semirette oblique, che si incontrano nel punto $M$ al di sotto delle parallele, intersecano $r$ nei punti $A$ e $A'$ e $s$ nei punti $B$ e $B'$. Il Teorema di Talete afferma che, se $r \parallel s$, allora i segmenti $AM$, $MB$, $A'M$ e $MB'$ risultano in proporzione. In particolare, si possono stabilire relazioni come
\[
\frac{AM}{A'M} \;=\; \frac{MB}{MB'}.
\]

In termini algebrici, pareliamo di proporizioni scrivendole similmente nella forma:
\[
\frac{a}{b} = \frac{c}{d}.
\]
Quando si conoscono tre di questi valori e il quarto è incognito, lo si determina tramite il \textit{prodotto incrociato}: 
\[
a \cdot d = b \cdot c.
\]

\noindent
\paragraph{Risolvere proporzioni}
Le proporzioni consentono di risolvere uguaglianze del tipo \(\tfrac{a}{b} = \tfrac{c}{d}\) passando ai \textit{prodotti incrociati}, cioè \(a \cdot d = b \cdot c\). Se in una proporzione compare un’incognita \(x\), occorre individuare con cura dove si trova (\(x\) al numeratore o al denominatore) e verificare che i denominatori non risultino nulli.

Un caso classico è \(\tfrac{x}{b} = \tfrac{c}{d}\), dove si scrive \(x \cdot d = b \cdot c\) e si isola \(x\). Se invece compare \(\tfrac{a}{x} = \tfrac{c}{d}\), allora si impone \(a \cdot d = x \cdot c\) e si ricava \(x = \tfrac{a \cdot d}{c}\), con \(x \neq 0\).

Alcuni esempi mostrano l’uso di questa tecnica:

\[
\frac{x}{4} = \frac{9}{6} 
\quad\Longrightarrow\quad
x \cdot 6 = 4 \cdot 9 
\quad\Longrightarrow\quad
6x = 36 
\quad\Longrightarrow\quad
x = 6.
\]
\[
\frac{5}{x} = \frac{7}{14}
\quad\Longrightarrow\quad
5 \cdot 14 = 7 \cdot x
\quad\Longrightarrow\quad
70 = 7x
\quad\Longrightarrow\quad
x = 10.
\]

Talvolta l’incognita compare più volte nella stessa proporzione, come in \(\tfrac{x}{x+1} = \tfrac{5}{7}\). In tal caso si passa a un’equazione lineare: \(x \cdot 7 = 5(x+1)\). Sviluppando, si ottiene \(7x = 5x + 5\) e quindi \(2x = 5\), da cui \(x = \tfrac52\). Se la proporzione è del tipo \(\tfrac{x}{3} = \tfrac{3}{x}\), incrociando si ha \(x \cdot x = 3 \cdot 3\), cioè \(x^2 = 9\) e quindi \(x=3\) (scartando l’eventuale valore negativo, se ci si riferisce a lunghezze). Questo tipo di problema risulta particolarmente utile nella risoluzione di esercizi geometrici in cui un medesimo segmento compare più volte in rapporti diversi.

\noindent Vediamo ora un secondo insieme più complesso. Consideriamo il seguente sistema, in cui compaiono due incognite \(x\) e \(y\):
\[
\begin{cases}
\dfrac{x}{\,y+2\,} = \dfrac{2}{3},\\[6pt]
\dfrac{y}{\,x\,} = \dfrac{4}{5}.
\end{cases}
\]
Vogliamo trovare i valori di \(x\) e \(y\) che soddisfino contemporaneamente entrambe le proporzioni.

\smallskip
\noindent
\textbf{Prima Proporzione} \(\displaystyle \frac{x}{y+2} = \frac{2}{3}\).  
Incrociando i prodotti, si ha
\[
3 \,x = 2 \,\bigl(y + 2\bigr).
\]
Sviluppando,
\[
3x = 2y + 4,
\]
\[
2y = 3x - 4,
\]
\[
y = \frac{3x - 4}{2}.
\]
In questo modo, la \textit{prima equazione} ci fornisce \(y\) in funzione di \(x\).

\smallskip
\noindent
\textbf{Seconda Proporzione} \(\displaystyle \frac{y}{\,x\,} = \frac{4}{5}\).  
Di nuovo, eseguiamo il prodotto incrociato:
\[
5 \,y = 4 \,x
\quad\Longrightarrow\quad
y = \frac{4}{5}\,x.
\]
Ora disponiamo di due \textit{espressioni} per \(y\): una derivata dalla prima proporzione e l’altra dalla seconda. Uguagliandole, otteniamo
\[
\frac{3x - 4}{2}
\;=\;
\frac{4}{5}\,x.
\]
\textbf{Risoluzione del Sistema}  
Moltiplichiamo entrambi i membri per 2 per eliminare il denominatore a sinistra:
\[
3x - 4 
= 
\frac{8}{5}\,x.
\]
Per liberarsi dal denominatore 5, moltiplichiamo tutto per 5:

\[
5(3x - 4) = 8x \;\;\Longrightarrow\;\; 15x - 20 = 8x \;\;\Longrightarrow\;\; 7x = 20 \;\;\Longrightarrow\;\; x = \frac{20}{7}.
\]

\noindent Una volta noto \(x\), troviamo \(y\) sostituendo \(x=\tfrac{20}{7}\) in \(y = \tfrac{4}{5}\,x\):
\[
y 
= 
\frac{4}{5} \times \frac{20}{7}
= 
\frac{80}{35}
= 
\frac{16}{7}.
\]
\textbf{Verifica}  
Controlliamo nella prima proporzione:
\[
\frac{x}{\,y+2\,}
= 
\frac{\frac{20}{7}}{\frac{16}{7}+2}
= 
\frac{\tfrac{20}{7}}{\tfrac{16}{7} + \tfrac{14}{7}}
= 
\frac{\tfrac{20}{7}}{\tfrac{30}{7}}
= 
\frac{20}{7} \times \frac{7}{30}
= 
\frac{20}{30}
= 
\frac{2}{3}.
\]
Quindi la proporzione è soddisfatta. Analogamente, la seconda proporzione \(\tfrac{y}{x}=\tfrac{4}{5}\) risulta vera con \(x=\tfrac{20}{7}, y=\tfrac{16}{7}\). Concludiamo dunque che il sistema di proporzioni
\[
\begin{cases}
\dfrac{x}{\,y+2\,} = \dfrac{2}{3},\\
\dfrac{y}{\,x\,} = \dfrac{4}{5},
\end{cases}
\]
ammette la \textit{soluzione} \(\displaystyle x=\frac{20}{7},\; y=\frac{16}{7}\). 

\smallskip
\noindent
Questo esempio mostra come, in problemi con più di una proporzione e più incognite, si possano trasformare le proporzioni in equazioni e risolverle in maniera sistematica, incrociando i risultati e ricavando i valori delle variabili. 

\subsectionstar{[5] Costruzione del Quarto e del Medio Proporzionale}
In matematica il concetto di proporzione è fondamentale per lo studio della geometria e dell'algebra, abbiamo precedentemente introdotto questo concetto tramite il teorema di Talete che ne rappresenta la prima intuizione geometrica. In questa sezione vedremo sia una componente piu rigorosa algebrica e vedremo infine come le proporizioni possono aiutarci nel capire numeri della forma $\sqrt{a \cdot b}$. Una proporzione è un'uguaglianza tra due rapporti. Ad esempio, dati quattro numeri \(a\), \(b\), \(c\) e \(d\), si dice che essi formano una proporzione se:
\[
a : b = c : d.
\]
In questa relazione, \(a\) e \(d\) sono detti estremi, mentre \(b\) e \(c\) sono detti medi della proporzione. Tale concetto viene utilizzato per confrontare quantità e mantenere relazioni costanti tra variabili; ad esempio, se una ricetta prevede 2 tazze di farina per 3 tazze di zucchero, aumentando la farina a 4 tazze lo zucchero dovrà diventare 6 tazze, mantenendo la proporzione:
\[
2 : 3 = 4 : 6.
\]

\medskip

\paragraph{Costruzione del Quarto Proporzionale}  
Dato un rapporto tra due numeri \(a\) e \(b\), il quarto proporzionale rispetto ai numeri \(a\), \(b\) e \(c\) è il numero \(d\) tale che:
\[
a : b = c : d.
\]
Il numero \(d\) è quello che completa la proporzione mantenendo costante il rapporto tra le coppie di termini.

\medskip

Per determinare \(d\) si risolve l'equazione:
\[
a \cdot d = b \cdot c,
\]
da cui:
\[
d = \frac{b \cdot c}{a}.
\]

\medskip

Supponiamo di avere \(a = 4\), \(b = 6\) e \(c = 8\). Allora il quarto proporzionale \(d\) si calcola come:
\[
d = \frac{6 \cdot 8}{4} = \frac{48}{4} = 12.
\]
La proporzione risultante è:
\[
4 : 6 = 8 : 12.
\]

\medskip

\paragraph{Costruzione del Medio Proporzionale}  

Il medio proporzionale tra due numeri \(a\) e \(b\) è un numero \(x\) tale che:
\[
a : x = x : b.
\]
Questa relazione, nota anche come proporzione continua, è particolarmente importante in geometria, ad esempio nella costruzione di figure simili.

\medskip

Dalla definizione si ottiene:
\[
x^2 = a \cdot b,
\]
quindi:
\[
x = \sqrt{a \cdot b}.
\]

\medskip

Supponiamo di voler trovare il medio proporzionale tra \(a = 4\) e \(b = 9\). Allora:
\[
x = \sqrt{4 \cdot 9} = \sqrt{36} = 6.
\]
La proporzione risultante è:
\[
4 : 6 = 6 : 9.
\]
Questo concetto viene frequentemente utilizzato nelle costruzioni geometriche e nei problemi di similitudine. Vediamo un esempiodi problema geometrico in cui possiamo applicare questa teoria.

\noindent
\textbf{Esempio Geometrico} Vogliamo costruire in modo geometrico il \textit{medio proporzionale} tra due segmenti di lunghezza \(a = 4\) e \(b = 9\). Ricordiamo che il medio proporzionale \(x\) soddisfa la proporzione continua \(a : x = x : b\), equivalentemente \(x^2 = a \cdot b\). In questo caso, il valore numerico risulta \(x = \sqrt{4 \cdot 9} = 6\), ma l’obiettivo è mostrare una costruzione puramente geometrica che renda evidente il significato di \(\sqrt{a \cdot b}\).

\medskip
\noindent
\textbf{Descrizione della Costruzione.}
Si consideri un segmento \(AB\) di lunghezza \(a + b = 13\). Si individua sul segmento un punto \(C\) tale che \(AC = a = 4\) e \(CB = b = 9\). Su \(AB\) si disegna il \textit{semicerchio} con \(AB\) come diametro. Quindi si erige da \(C\) una \textit{perpendicolare} al segmento \(AB\), intersecando il semicerchio in un punto \(D\). Si può dimostrare (mediante il \textit{teorema di Pitagora} e proprietà dei triangoli rettangoli inscritti in una semicirconferenza) che \(CD\) risulta esattamente il medio proporzionale tra \(AC\) e \(CB\). 

\begin{center}
\begin{tikzpicture}[scale=1, line cap=round, line join=round]
  % Puntiamo il centro del semicerchio in A(0,0)
  % Definiamo B(9,0) come estremo del raggio AB=9
  \coordinate (A) at (0,0);
  \coordinate (B) at (9,0);

  % Disegno dell'asse orizzontale
  \draw[thick,->] (A) -- (10,0) node[below] {$x$};

  % Tracciamo il semicerchio centrato in A, raggio=AB=9
  % Lo disegniamo da 0° a 180° per "aprire" verso l'alto
  \draw[thick] (B) arc[start angle=0, end angle=180, radius=4.5];

  % Punto C su AB, con AC=4 => C(4,0)
  \coordinate (C) at (4,0);

  % Disegno dei segmenti AC e CB
  \draw[dashed] (A) -- (C) node[midway,below] {};
  \draw[dashed] (C) -- (B) node[midway,below] {}; % 9-4=5

  % Costruiamo la perpendicolare da C e troviamo D
  % D e' l'intersezione con il semicerchio: eq. (x-0)^2 + (y-0)^2=81 => x=4 => y= sqrt(81-16)= sqrt(65)
  \coordinate (D) at (4,{sqrt(65)/2+0.435});

  % Disegno della perpendicolare
  \draw[dashed] (C)--(D);

  % Etichette dei punti
  \fill (A) circle(1.5pt) node[left]  {\small $A$};
  \fill (B) circle(1.5pt) node[below] {\small $B$};
  \fill (C) circle(1.5pt) node[below] {\small $C$};
  \fill (D) circle(1.5pt) node[above]  {\small $D$};

  % Distanze
  \node at (2,0) [below] {\small $AC$};
  \node at (6.5,0) [below] {\small $CB$};
\end{tikzpicture}
\end{center}

\noindent
\textbf{Spiegazione del Risultato.}
Il triangolo \(ADC\) è retto in \(C\) (perché \(AB\) è diametro del semicerchio e \(D\) giace sul semicerchio). Applicando il teorema di Pitagora, si mostra che \((CD)^2 = AC \cdot CB\). Poiché \(AC=4\) e \(CB=9\), si deduce \((CD)^2 = 36\) e quindi \(CD=6\). Ne segue che \(CD\) è \textit{medio proporzionale} tra 4 e 9, cioè 
\[
\frac{4}{6} = \frac{6}{9}.
\]
In modo più generale, se un segmento \(AB\) di lunghezza \(a+b\) è diametro di un semicerchio, e \(C\) divide \(AB\) in parti \(a\) e \(b\), allora il segmento verticale \(CD\) verso il semicerchio è \(\sqrt{a\,b}\), cioè il \textit{medio proporzionale} fra \(a\) e \(b\). Questo esempio mostra una \textit{costruzione geometrica} che traduce in immagini il concetto algebrico \(\sqrt{a \cdot b}\).



\newpage




\section{Triangoli}

\noindent
\textbf{I Triangoli sul Piano Cartesiano}

\smallskip
\noindent
Un modo semplice per \textit{costruire} un triangolo consiste nel scegliere \textbf{tre punti} \((A, B, C)\) in un piano cartesiano e congiungerli con segmenti. Se i tre punti \textit{non} sono allineati, formano un \textit{triangolo} vero e proprio; se invece i punti giacciono su un’unica retta, si parla di \textit{triangolo degenere}, ovvero un semplice \textit{segmento} con un punto intermedio. 

\begin{center}
\begin{tikzpicture}[scale=1.0, line cap=round, line join=round]

% Assi cartesiani
\draw[->] (-0.5,0) -- (5.5,0) node[right] {$x$};
\draw[->] (0,-0.5) -- (0,4.5) node[left] {$y$};

% Punti A,B,C scelti non allineati
\coordinate (A) at (1,1);
\coordinate (B) at (4,2);
\coordinate (C) at (3,3.5);

% Disegno dei segmenti AB, BC, CA
\draw[thick] (A)--(B)--(C)--cycle;

% Marcatura dei punti
\fill (A) circle(2pt) node[below left] {\small $A$};
\fill (B) circle(2pt) node[below right] {\small $B$};
\fill (C) circle(2pt) node[above] {\small $C$};

\end{tikzpicture}
\end{center}

\noindent
Nella figura, i tre punti \((A, B, C)\) non giacciono su un’unica retta, e quindi i segmenti \(\overline{AB}\), \(\overline{BC}\) e \(\overline{CA}\) formano un triangolo. In questa sezione, indagheremo le principali \textit{proprietà} dei triangoli: in che modo due triangoli si possono considerare \textit{simili}, quali sono i \textit{punti notevoli} (come le \textit{mediane}, le \textit{bisettrici} e le \textit{altezze}), e come si definiscono \textit{perimetro} e \textit{area} di un triangolo. Osserveremo, ad esempio, che:
\[
\text{Perimetro} = AB + BC + CA,
\quad
\text{Area} = \frac{1}{2} \times (\text{base}) \times (\text{altezza}).
\]

\noindent
Nella tabella seguente elenchiamo alcuni termini importanti per lo studio dei triangoli. Alcuni di questi (come \textit{lato}, \textit{angolo} e \textit{vertice}) sono già noti, mentre altri (\textit{bisettrice}, \textit{mediana}, \textit{altezza}, \textit{baricentro}) verranno introdotti e approfonditi nei prossimi capitoli, insieme a molte altre proprietà e risultati.

\begin{center}
\renewcommand{\arraystretch}{1.1 }
\begin{tabular}{|l|p{9cm}|}
\hline
\textit{Lato} & Segmento che unisce due \textit{vertici} di un triangolo. Un triangolo ha tre lati. \\
\hline
\textit{Angolo Interno} & Angolo formato in ciascun vertice del triangolo dai due lati incidenti. \\
\hline
\textit{Angolo Esterno} & Angolo adiacente a un angolo interno, ottenuto prolungando uno dei lati del triangolo. \\
\hline
\textit{Vertice} & Punto di intersezione di due lati (il triangolo ha tre vertici). \\
\hline
\textit{Perimetro} & Somma delle lunghezze dei tre lati. \\
\hline
\textit{Semiperimetro} & Metà del perimetro, spesso indicato con \(p\). \\
\hline
\textit{Area} & Misura dell’estensione superficiale del triangolo; per un triangolo di base \(b\) e altezza \(h\) si calcola come \(\tfrac12\,b\,h\). \\
\hline
\textit{Bisettrice} & Segmento che, da un vertice, \textit{divide a metà} l’angolo interno corrispondente. \\
\hline
\textit{Mediana} & Segmento che unisce un vertice al \textit{punto medio} del lato opposto. \\
\hline
\textit{Altezza} & Segmento condotto da un vertice \textit{perpendicolarmente} al lato opposto (o al suo prolungamento). \\
\hline
\textit{Baricentro} & Punto di intersezione delle tre \textit{mediane}, che possiede importanti proprietà di equilibrio. \\
\hline
\end{tabular}
\end{center}
 

\newpage
\subsectionstar{[41] Criteri di Similitudine}
\textit{Introduzione: Triangoli Scaleni e Similitudine}

Quando due triangoli hanno gli \textit{angoli} corrispondenti \textbf{uguali} e i \textit{lati} corrispondenti \textbf{in proporzione}, si dicono \textbf{simili}. Ciò significa che, pur potendo avere dimensioni diverse ed essere ruotati o traslati in zone differenti del piano, \textit{mantengono la stessa forma} (gli stessi angoli) e \textit{rapporti} tra i lati. Di seguito, mostriamo due triangoli \textit{scaleni} (con lati tutti diversi) che sono simili, ma si trovano in posizioni e con orientamenti differenti.

\begin{center}
\begin{tikzpicture}[scale=0.9]

% Primo triangolo scaleno (A,B,C)
\coordinate (A) at (1,1);
\coordinate (B) at (4,1);
\coordinate (C) at (3,4);

\draw[thick] (A)--(B)--(C)--cycle;
\fill (A) circle(1.2pt) node[below left]{$A$};
\fill (B) circle(1.2pt) node[below right]{$B$};
\fill (C) circle(1.2pt) node[left]{$C$};

\coordinate (A2) at (1.5*1+4, 1.5*1);
\coordinate (B2) at (1.5*4+4, 1.5*1);
\coordinate (C2) at (1.5*3+4, 1.5*4);

\draw[thick] (A2)--(B2)--(C2)--cycle;
\fill (A2) circle(1.2pt) node[below left]{$A'$};
\fill (B2) circle(1.2pt) node[below right]{$B'$};
\fill (C2) circle(1.2pt) node[left]{$C'$};

\end{tikzpicture}
\end{center}

\paragraph{Introduzione ai Criteri di Similitudine}
Quando due triangoli condividono la \textit{stessa forma} (angoli uguali e lati in proporzione), si dicono \textbf{simili}. Per riconoscere questa uguaglianza di forma, esistono alcuni \textbf{criteri} che, se verificati, garantiscono la similitudine. I tre criteri principali sono \textit{Lato-Lato-Lato}, \textit{Lato-Angolo-Lato} e \textit{Angolo-Angolo}.

\paragraph{Criterio Lato-Lato-Lato (LLL)}
Se i \textit{tre lati} di un triangolo sono \textbf{proporzionali} ai \textit{tre lati} di un altro triangolo, i due triangoli risultano simili. In simboli:
\[
\frac{AB}{A'B'} = \frac{BC}{B'C'} = \frac{CA}{C'A'} 
\quad\Longrightarrow\quad
\triangle ABC \sim \triangle A'B'C'.
\]
\textit{Spiegazione}: conoscere i rapporti fra \textit{tutti} i lati ci assicura che gli angoli corrispondenti coincidano, poiché non c’è libertà di “allungare” un lato senza cambiare la forma complessiva.

\paragraph{Criterio Lato-Angolo-Lato (LAL)}
Se due coppie di \textit{lati} sono \textbf{proporzionali} e l’\textit{angolo} compreso fra di essi è \textbf{uguale}, i due triangoli sono simili:
\[
\frac{AB}{A'B'} = \frac{BC}{B'C'}
\quad\text{e}\quad
\angle ABC = \angle A'B'C'.
\]
\textit{Spiegazione}: la proporzione sui due lati stabilisce un \textit{rapporto fisso} tra le lunghezze, mentre l’uguaglianza dell’angolo \textit{vincola} la rotazione. Combinando questi vincoli, il triangolo risulta “bloccato” nella stessa forma.

\begin{center}
\begin{tikzpicture}[scale=0.8]

% Primo triangolo con lato AB e BC colorati, e angolo ABC evidenziato
\coordinate (A) at (1,1);
\coordinate (B) at (4,1);
\coordinate (C) at (3,3);

% Lati
\draw[ultra thick, red] (A)--(B) node[midway, below] {\small $AB$};
\draw[ultra thick, blue] (B)--(C) node[midway, right] {\small $BC$};
\draw[thick] (C)--(A);


% Secondo triangolo, simile, più grande
\coordinate (A2) at (6,2);
\coordinate (B2) at (10,2);
\coordinate (C2) at (9,5);

\draw[ultra thick, red] (A2)--(B2) node[midway, below] {\small $A'B'$};
\draw[ultra thick, blue] (B2)--(C2) node[midway, right] {\small $B'C'$};
\draw[thick] (C2)--(A2);


\end{tikzpicture}
\end{center}

\textit{Nella figura}, i lati $AB$ e $BC$ del primo triangolo (in rosso e blu) sono in proporzione con i lati $A'B'$ e $B'C'$ del secondo triangolo, e l’angolo $\angle ABC$ coincide con $\angle A'B'C'$. Secondo il criterio LAL, ciò assicura la \textit{similitudine} dei due triangoli.

\paragraph{Criterio Angolo-Angolo (AA)}
Se in due triangoli \textit{almeno due angoli} corrispondenti sono \textbf{uguali}, i due triangoli sono simili. Infatti, il terzo angolo risulta determinato dalla somma a $180^\circ$. In formule, 
\[
\angle A = \angle A',\quad \angle B = \angle B'
\quad\Longrightarrow\quad
\triangle ABC \sim \triangle A'B'C'.
\]
Vediamo ora un esempio che applichi queste nozioni. 

\noindent\textbf{Esempio} 
Un \textit{triangolo equilatero} possiede tre lati congruenti. Nella figura sottostante, si consideri il triangolo \(ABC\) con \(AB = BC = CA\). Se tracciamo dal vertice \(A\) la retta che divide in due parti uguali l'angolo in $A$ incontrando \(BC\) e individua il punto \(M\) su \(BC\), vogliamo dimostrare che \(M\) è il punto medio di \(BC\). In altre parole, l’\textit{bisettrice} del triangolo coincide anche con la sua \textit{mediana}.

\medskip
\noindent
Si osservino i due triangoli \(\triangle ABM\) e \(\triangle ACM\). Innanzitutto, poiché \(ABC\) è equilatero, i lati \(AB\) e \(AC\) risultano congruenti. Inoltre, il segmento \(AM\) è \textit{comune} a entrambi i triangoli. L’angolo \(\angle BAM\) coincide con \(\angle CAM\) poiché, essendo \(AM\) un’unica retta, questi due angoli rappresentano lo stesso angolo \(\angle BAC\) “spezzato” dalla perpendicolare in \(M\). Di conseguenza, ciascun lato di \(\triangle ABM\) corrisponde al lato omologo di \(\triangle ACM\) in modo che:

\begin{enumerate}
\item \(AB = AC\) (lati dell’equilatero),
\item  \(AM\) è \textit{comune},
\item \(\angle BAM = \angle CAM\) dato che $AM$ è la bisettrice
\end{enumerate}

In base al \textit{criterio Lato-Angolo-Lato} di congruenza, i due triangoli \(\triangle ABM\) e \(\triangle ACM\) risultano \textit{congruenti}. Ne segue che i lati \(\overline{BM}\) e \(\overline{MC}\) sono uguali, poiché corrispondono ai lati opposti all’angolo uguale nei due triangoli. In altre parole, \(BM = MC\). Dunque il punto \(M\) è il \textit{punto medio} del segmento \(BC\). In un triangolo equilatero, l’altezza dal vertice coincide quindi con la mediana, dimostrando che la stessa retta \(\overline{AM}\) è contemporaneamente \textit{altezza} e \textit{mediana}.

\begin{center}
\begin{tikzpicture}[scale=0.8, line join=round, line cap=round]
  % Coordinate di un triangolo equilatero di lato 6
  % B(0,0), C(6,0), A(3, sqrt(6^2 - 3^2))= (3, sqrt(27))= (3, 5.196)
  \coordinate (B) at (0,0);
  \coordinate (C) at (6,0);
  \coordinate (A) at (3,{sqrt(27)});

  % Punto M come piede dell'altezza da A su BC => M(3,0)
  \coordinate (M) at (3,0);

  % Disegno dei lati
  \draw[thick] (B)--(C)--(A)--cycle;

  % Altezza e mediana
  \draw[dashed] (A)--(M);

  % Etichette dei punti
  \fill (B) circle(1.5pt) node[below left]  {\small B};
  \fill (C) circle(1.5pt) node[below right] {\small C};
  \fill (A) circle(1.5pt) node[above]       {\small A};
  \fill (M) circle(1.5pt) node[below]       {\small M};
\end{tikzpicture}
\end{center}

\noindent
Nella figura, i due triangoli \(\triangle ABM\) e \(\triangle ACM\) sono congruenti per \textit{LAL}: \(AB = AC\), \(AM\) in comune, e l’angolo \(\angle BAM\) coincide con \(\angle CAM\). Da questa congruenza segue \(BM = MC\). Quindi la retta \(\overline{AM}\), tracciata come altezza, è anche la mediana di \(BC\). 

\noindent Possiamo infine notare che una dimostazione simile ci porta a concludere che mediana e bisettrice coincidono anche con l'altezza, è sufficiente infatti sostituire il terzo punto con il fatto che entrambi gli angoli che si creano in $M$ sono rettangoli, il che segue dalla definizione di altezza.

\newpage

\subsectionstar{[25] Punti Notevoli del Triangolo}
\noindent
In un triangolo esistono tre segmenti notevoli che assumono un ruolo fondamentale: la \textbf{mediana}, la \textbf{bisettrice} e l’\textbf{altezza}. Ognuno di questi elementi presenta caratteristiche geometriche peculiari e contribuisce allo studio delle proprietà del triangolo. In alcune circostanze speciali, come nel triangolo equilatero, tali segmenti possono persino coincidere. Vedremo anche come, dal punto di vista delle coordinate, il \textbf{baricentro} (o \textit{centro di gravità}) del triangolo si ottenga come intersezione delle mediane e possa essere calcolato facilmente.

\paragraph{Mediana}
In un triangolo \(ABC\), la mediana relativa a un vertice è il segmento che congiunge tale vertice con il punto medio del lato opposto. Nel disegno, si considera un triangolo scaleno e si indica con \(M\) il punto medio di \(BC\). La mediana dal vertice \(A\) è dunque il segmento \(AM\), tracciato con linea tratteggiata:

\[
\begin{tikzpicture}[scale=0.8]
  % Stesso triangolo scaleno di prima: A(0,0), B(7,0), C(2,4)
  \coordinate (A) at (0,0);
  \coordinate (B) at (7,0);
  \coordinate (C) at (2,4);

  % Disegno del triangolo
  \draw[thick] (A)--(B)--(C)--cycle;

  % Calcolo del punto M, punto medio di BC
  % B(7,0), C(2,4) => M((7+2)/2, (0+4)/2) = (4.5,2)
  \coordinate (M) at (4.5,2);

  % Disegno della mediana AM in linea tratteggiata
  \draw[dashed] (A)--(M);

  % Etichette dei vertici
  \node[below left] at (A) {\(A\)};
  \node[below] at (B) {\(B\)};
  \node[above] at (C) {\(C\)};
  
  % Etichetta del punto M
  \node[right] at (M) {\(M\) (punto medio di \(BC\))};
\end{tikzpicture}
\]

\noindent La mediana \(\overline{AM}\) divide il triangolo in due parti di uguale area. Analogamente, si possono tracciare mediane da \(B\) e da \(C\).

\paragraph{Bisettrice}
La bisettrice di un angolo di un triangolo è il segmento che, partendo dal vertice dell’angolo, ne divide l’ampiezza in due parti uguali e incontra il lato opposto. Nel triangolo \(ABC\), se consideriamo la bisettrice dell’angolo \(\angle A\), il segmento parte da \(A\) e incontra il lato \(BC\) in un punto \(D\). Il disegno illustra una bisettrice in linea tratteggiata:

\[
\begin{tikzpicture}[scale=0.8]
  % Coordinate dei vertici di un triangolo scaleno
  % A(0,0), B(7,0), C(2,4)
  \coordinate (A) at (0,0);
  \coordinate (B) at (7,0);
  \coordinate (C) at (2,4);

  % Disegno del triangolo
  \draw[thick] (A)--(B)--(C)--cycle;

  % Lati (per verifica)
  % AB = 7
  % AC = sqrt((2-0)^2 + (4-0)^2) = sqrt(4 +16) = sqrt(20) ~ 4.4721
  % BC = sqrt((2-7)^2 + (4-0)^2) = sqrt(25+16)= sqrt(41) ~ 6.4031
  % Rapporto AB:AC ~ 7 : 4.4721 ~ 1.565
  % Se D e' su BC e AD e' bisettrice di angolo A, BD:DC = AB:AC ~ 1.565
  % BC=6.4031 => t= BD/BC => t/(1-t)=1.565 => t~0.61
  % D= B + t*(C-B)= (7,0)+0.61*((2-7),(4-0))= (7,0)+0.61*(-5,4)= (7-3.05,0+2.44)= (3.95,2.44)

  % Calcolo del punto D
  \coordinate (D) at (3.95,2.44);

  % Disegno bisettrice in linea tratteggiata
  \draw[dashed] (A)--(D);

  % Etichette dei vertici
  \node[below left] at (A) {\(A\)};
  \node[below right] at (B) {\(B\)};
  \node[above] at (C) {\(C\)};
  
  % Etichetta del punto D
  \node[above right] at (D) {\(D\)};

\end{tikzpicture}
\]

\noindent Il segmento \(\overline{AD}\) divide l’angolo \(\angle A\) in due parti uguali. Allo stesso modo, si definiscono le bisettrici degli angoli \(\angle B\) e \(\angle C\).

\paragraph{Altezza}
L’altezza (o altitudine) di un triangolo è il segmento tracciato da un vertice perpendicolarmente al lato opposto (o al suo prolungamento). Se \(H\) è il piede della perpendicolare da \(A\) sul lato \(BC\), l’altezza è \(AH\). Questo significa che il segmento $AH$ forma due angoli retti nell'incidenza con $CB$. Nell’esempio seguente, \(AH\) è in linea tratteggiata:

\[
\begin{tikzpicture}[scale=0.8]
  % Stesso triangolo scaleno: A(0,0), B(7,0), C(2,4)
  \coordinate (A) at (0,0);
  \coordinate (B) at (7,0);
  \coordinate (C) at (2,4);

  % Disegno del triangolo
  \draw[thick] (A)--(B)--(C)--cycle;

  % Calcolo del piede dell'altezza da A sul lato BC.
  % Equazione retta BC: passante per B(7,0) e C(2,4)
  %   Slope m = (4-0)/(2-7) = 4/-5 = -4/5
  %   Forma esplicita: y = -4/5 x + 28/5 (poiché passa per x=7,y=0)
  % Equazione retta perpendicolare da A(0,0) a BC => slope = 5/4 => y=(5/4)x
  % Risolviamo il sistema:
  %   (5/4)x = -4/5 x + 28/5
  %   Moltiplicando per 20 => 25x = -16x + 112 => 41x=112 => x=112/41
  %   y=(5/4)*(112/41)=140/41
  % H = (112/41, 140/41) ~ (2.73, 3.41)

  \coordinate (H) at ({112/41},{140/41});

  % Disegno dell'altezza in linea tratteggiata
  \draw[dashed] (A)--(H);

  % Etichette dei vertici
  \node[below left] at (A) {\(A\)};
  \node[below] at (B) {\(B\)};
  \node[above] at (C) {\(C\)};

  % Etichetta del punto H
  \node[right] at (H) {\(H\)};

\end{tikzpicture}
\]

\noindent L’altezza \(\overline{AH}\) è ortogonale a \(BC\). Le altre due altezze si tracciano da \(B\) e da \(C\) in modo analogo.

\paragraph{Coincidenza nel Triangolo Equilatero}
In un triangolo equilatero di lato \(l\), mediana, bisettrice e altezza coincidono se tracciate dallo stesso vertice, poiché tutti gli angoli misurano \(60^\circ\) e i lati sono uguali. Di conseguenza, la retta che parte da un vertice e cade sul lato opposto è simultaneamente mediana, bisettrice e altezza.
\[
\begin{tikzpicture}[scale=1.0]
  % Triangolo equilatero di lato 4: 
  %   A(0,0), B(4,0), C(2,3.464)  (3.464 ~ 4 * sqrt(3)/2)
  \coordinate (A) at (0,0);
  \coordinate (B) at (4,0);
  \coordinate (C) at (2,3.464);

  % Disegno del triangolo
  \draw[thick] (A)--(B)--(C)--cycle;
  
  % Calcolo dei punti medi
  % M_BC = midpoint di B(4,0) e C(2,3.464)
  % M_AC = midpoint di A(0,0) e C(2,3.464)
  % M_AB = midpoint di A(0,0) e B(4,0)
  \coordinate (MBC) at ($(B)!0.5!(C)$);
  \coordinate (MAC) at ($(A)!0.5!(C)$);
  \coordinate (MAB) at ($(A)!0.5!(B)$);

  % Disegno delle mediane in linea tratteggiata
  %   A -> MBC
  %   B -> MAC
  %   C -> MAB
  \draw[dashed] (A)--(MBC);
  \draw[dashed] (B)--(MAC);
  \draw[dashed] (C)--(MAB);

  % Etichette dei vertici
  \node[below left] at (A) {\(A\)};
  \node[below right] at (B) {\(B\)};
  \node[above] at (C) {\(C\)};

  % Etichette dei punti medi
  \node at ($(MBC)+(0.35,0.2)$) {\(M_{BC}\)};
  \node at ($(MAC)+(-0.4,0.2)$) {\(M_{AC}\)};
  \node at ($(MAB)+(0,-0.3)$) {\(M_{AB}\)};
\end{tikzpicture}
\]

\paragraph{Baricentro}
Il \textit{baricentro} (o \textit{centro di gravità}) di un triangolo è il punto di intersezione delle tre mediane. In coordinate cartesiane, se i vertici del triangolo sono \(A(x_A,y_A)\), \(B(x_B,y_B)\), \(C(x_C,y_C)\), il baricentro \(G\) ha coordinate
\[
G\Bigl(\frac{x_A+x_B+x_C}{3},\,\frac{y_A+y_B+y_C}{3}\Bigr).
\]

\noindent Per un esempio numerico, si consideri il triangolo con vertici \(A(0,0)\), \(B(6,0)\) e \(C(3,4)\). Le mediane si intersecano in un punto \(G\) le cui coordinate si calcolano facendo la media delle coordinate dei vertici:
\[
x_G = \frac{0 + 6 + 3}{3} = 3,\quad
y_G = \frac{0 + 0 + 4}{3} = \frac{4}{3}.
\]
Quindi il baricentro è \(G(3,\tfrac{4}{3})\).  

\paragraph{Calcolo Algebrico}
In alcuni casi, lo studio dei segmenti notevoli di un triangolo (mediana, bisettrice, altezza) si limita all’aspetto puramente geometrico. Sul piano algebrico, invece, è relativamente comune il calcolo del \textit{baricentro}, determinato come intersezione delle mediane e ricavabile dalle coordinate dei vertici. Esistono formule analitiche anche per calcolare sia la lunghezza sia l’equazione (in termini di coordinate) della mediana, della bisettrice e dell’altezza, ma esse risultano più articolate e possono essere derivate tramite strumenti trigonometrici o combinando il teorema del coseno con la definizione dei segmenti. In genere, lo studente ha già a disposizione le basi necessarie per ricostruire tali relazioni, qualora sia richiesto un approccio più approfondito. 
\newpage

\subsectionstar{[39] Teoremi di Euclide e Pitagora}

\paragraph{Teorema di Euclide (Altitudine sull’Ipotenusa)}
In un \textit{triangolo rettangolo}, si consideri l’altitudine condotta dall’\textit{angolo retto} all’\textit{ipotenusa}. Tale altitudine divide l’ipotenusa in due segmenti. Il \textbf{Teorema di Euclide} afferma che:
\begin{itemize}
    \item L’altitudine è \textit{media proporzionale} fra i due segmenti dell’ipotenusa.  
    \item Ogni cateto è \textit{media proporzionale} fra l’ipotenusa e la proiezione del cateto stesso sull’ipotenusa.
\end{itemize}

\begin{center}
\begin{tikzpicture}[scale=0.9]

% Triangolo rettangolo ABC con angolo retto in A
% B(4,0), C(0,3). D è il piede dell'altitudine da A sull'ipotenusa BC

\coordinate (A) at (0,0);
\coordinate (B) at (4,0);
\coordinate (C) at (0,3);

% Disegno i lati del triangolo
\draw[thick] (A)--(B)--(C)--cycle;

% Etichette e punti
\fill (A) circle(1.2pt) node[below left]{$A$};
\fill (B) circle(1.2pt) node[below right]{$B$};
\fill (C) circle(1.2pt) node[above left]{$C$};

% Angolo retto in A (piccolo quadratino)
\draw (0.3,0) -- (0.3,0.3) -- (0,0.3);

% Calcolo coordinate D come piede dell'altitudine da A a BC
% BC: eq. y-0=(-3/4)(x-4) => y=(-3/4)x+3
% AD perpendicolare => slope 4/3 => eq. y=(4/3)x
% Intersezione => x=36/25=1.44, y=48/25=1.92
\coordinate (D) at (1.44,1.92);

% Altitudine AD
\draw[dashed] (A)--(D);
\fill (D) circle(1.2pt) node[above right]{$D$};

% Perpendicolarità in D (opzionale)
\draw (1.44,1.92) + (0.2,0) -- + (0.2,0.2) -- +(0,0.2);

\end{tikzpicture}
\end{center}

\textit{Primo Teorema di Euclide (o Altitudine):}  
Nel triangolo rettangolo \(ABC\), se \(D\) è il piede dell’altitudine dall’angolo retto \(A\) sull’ipotenusa \(BC\), allora
\[
AD^2 = BD \cdot DC.
\]
In altre parole, l’altitudine \(AD\) è \textit{media proporzionale} fra i segmenti \(BD\) e \(DC\) in cui l’ipotenusa risulta divisa dal punto \(D\).

\textit{Secondo Teorema di Euclide (o dei Cateti):}  
Nello stesso triangolo rettangolo, ciascun \textit{cateto} è \textit{media proporzionale} fra l’ipotenusa e la \textit{proiezione} del cateto stesso sull’ipotenusa:
\[
AB^2 = BD \cdot BC,
\quad
AC^2 = DC \cdot BC.
\]
Qui \(AB\) e \(AC\) sono i cateti, \(BC\) l’ipotenusa, e \(BD\) e \(DC\) i segmenti in cui l’ipotenusa è divisa da \(D\). Queste relazioni permettono di calcolare lunghezze e risolvere problemi metrici su triangoli rettangoli. 

\paragraph{Teorema di Pitagora}
Nel \textit{triangolo rettangolo}, il \textbf{Teorema di Pitagora} afferma che \textit{la somma dei quadrati dei cateti} è \textit{uguale} al \textit{quadrato dell’ipotenusa}:
\[
AB^2 + AC^2 = BC^2
\quad (\text{se } \angle A=90^\circ).
\]
\begin{center}
\begin{tikzpicture}[scale=0.9]
    % Triangolo rettangolo con angolo retto in A
    \coordinate (A) at (0,0);
    \coordinate (B) at (4,0);
    \coordinate (C) at (0,3);

    \draw[thick] (A)--(B)--(C)--cycle;

    % Label
    \fill (A) circle(1.2pt) node[below left]{$A$};
    \fill (B) circle(1.2pt) node[below right]{$B$};
    \fill (C) circle(1.2pt) node[left]{$C$};

    \draw (0.3,0) -- (0.3,0.3) -- (0,0.3); % angolo retto in A

    \node[below] at ($(A)!0.5!(B)$) {\small $AB$};
    \node[left]  at ($(A)!0.5!(C)$) {\small $AC$};
    \node[above right] at ($(B)!0.5!(C)$) {\small $BC$};

\end{tikzpicture}
\end{center}

\paragraph{Diagonale di un Quadrato}
Se un quadrato ha lato $1$, la \textit{diagonale} si calcola tramite il Teorema di Pitagora, considerandolo come \textit{triangolo rettangolo} con cateti entrambi di lunghezza $1$:
\[
\text{diagonale} 
= \sqrt{1^2 + 1^2} 
= \sqrt{2}.
\]
\textit{Osservazione storica}: la scoperta che $\sqrt{2}$ \textit{non} potesse esprimersi come frazione \((\tfrac{p}{q})\) fu uno dei primi esempi di \textit{numero irrazionale}, provocando notevole stupore nell’antichità.

\begin{center}
\begin{tikzpicture}[scale=2]

% Vertici del quadrato di lato 1
\coordinate (A) at (0,0);
\coordinate (B) at (1,0);
\coordinate (C) at (1,1);
\coordinate (D) at (0,1);

% Disegno del quadrato
\draw[thick] (A)--(B)--(C)--(D)--cycle;

% Disegno della diagonale AC
\draw[dashed] (A)--(C);

% Punti e label
\fill (A) circle(0.8pt) node[below left]{$A$};
\fill (B) circle(0.8pt) node[below right]{$B$};
\fill (C) circle(0.8pt) node[above right]{$C$};
\fill (D) circle(0.8pt) node[above left]{$D$};

% Etichette dei lati e della diagonale
\node[below] at ($(A)!0.5!(B)$) {\small 1};
\node[right]  at ($(B)!0.5!(C)$) {\small 1};
\node at (0.6,0.5) {\small $\sqrt{2}$};

\end{tikzpicture}
\end{center}

\paragraph{Diagonale di un Rettangolo}
Più in generale, un rettangolo di lati $a$ e $b$ si può considerare come \textit{triangolo rettangolo} con cateti $a$ e $b$. Applicando Pitagora, la \textit{diagonale} misura
\[
\sqrt{a^2 + b^2}.
\]
Questo risulta utile per calcolare lunghezze in figure geometriche o per problemi di \textit{misurazione} in contesti pratici (planimetrie, progetti edilizi, ecc.).

\paragraph{Esempio su un Trapezio}
\noindent
Vogliamo calcolare l’area di un \emph{trapezio isoscele} conoscendo la misura di tutti i lati, senza ricorrere direttamente alla classica formula del trapezio. Supponiamo di avere il trapezio \(ABCD\), con \(AB\) come base maggiore, \(CD\) come base minore, e i lati obliqui \(AD\) e \(BC\) di uguale lunghezza.

Nel disegno, tracciamo la perpendicolare dal vertice \(D\) alla base \(AB\) e indichiamo con \(E\) il punto di intersezione. In modo analogo, dal vertice \(C\) tracciamo la perpendicolare a \(AB\), ottenendo il punto \(F\). Poiché \(AB\parallel CD\), i segmenti \(DE\) e \(CF\) sono entrambi \emph{perpendicolari} ad \(AB\).

Se osserviamo la figura, ci accorgiamo che l’area del trapezio può essere suddivisa in tre parti: il \emph{rettangolo} \(EFCB\) e i due \emph{triangoli} \(AED\) e \(BFC\) posti ai lati. Notiamo anche che i triangoli \(AED\) e \(BFC\) risultano \emph{congruenti}, poiché hanno i lati \(AD\) e \(BC\) uguali (per ipotesi di trapezio isoscele), le basi \(AE\) e \(BF\) corrispondenti (derivate dalla stessa differenza delle basi maggiore e minore, suddivisa in parti uguali), e le altezze \(DE\) e \(CF\) comuni in modulo (sono entrambi perpendicolari alla stessa base \(AB\)). Questa congruenza si giustifica con i criteri di uguaglianza dei triangoli (ad esempio, \emph{Lato-Angolo-Lato}).

\begin{center}
\begin{tikzpicture}[scale=0.8, line cap=round, line join=round]

\coordinate (A) at (0,0);
\coordinate (B) at (10,0);
\coordinate (D) at (2,{sqrt(21)});
\coordinate (C) at (8,{sqrt(21)});
\coordinate (E) at (2,0);
\coordinate (F) at (8,0);

\draw[thick] (A)--(B)--(C)--(D)--cycle;
\draw[dashed] (D)--(E);
\draw[dashed] (C)--(F);

\node[below left] at (A) {\small A};
\node[below right] at (B) {\small B};
\node[above left] at (D) {\small D};
\node[above right] at (C) {\small C};
\node[below] at (E) {\small E};
\node[below] at (F) {\small F};

\end{tikzpicture}
\end{center}

Per trovare l’area complessiva, si può quindi calcolare l’area del rettangolo \(EFCB\), sommata all’area di uno dei due triangoli (che va poi raddoppiata, essendo l’altro congruente). In tal modo, se si conoscono le lunghezze di \(AB\), \(CD\) e dei lati obliqui, è possibile ricavare i segmenti \(AE\), \(DE\), \(BF\), \(CF\) e dunque ottenere l’area totale senza usare direttamente la formula \(\tfrac{(AB + CD)}{2}\,\times\,\text{altezza}\).
\newpage

\subsectionstar{[31] Risoluzione di un Triangolo Rettangolo}
\textbf{Definizione del problema}\\
Un triangolo rettangolo è un triangolo che ha un \textit{angolo retto} (90°). Il lato opposto all’angolo retto si chiama \textit{ipotenusa}, mentre gli altri due lati sono detti \textit{cateti}. Risolvere un triangolo rettangolo significa determinare la misura di tutti i suoi lati e angoli, partendo da alcune informazioni iniziali (come un lato e un angolo, o due lati, ecc.).

\textbf{Classificazione dei triangoli rettangoli}\\
A seconda della relazione tra i cateti e gli angoli acuti, un triangolo rettangolo può essere:
\begin{itemize}
    \item \textit{Isoscele}: quando i due cateti sono uguali e gli angoli acuti misurano entrambi 45°.
    \item \textit{Scaleno}: quando i cateti hanno lunghezze diverse e gli angoli acuti misure differenti.
    \item \textit{Speciale} (30°–60°–90° oppure 45°–45°–90°): in questi casi si applicano \textit{relazioni trigonometriche} particolari che semplificano i calcoli.
\end{itemize}

\textbf{Elementi fondamentali di un triangolo rettangolo}
\begin{itemize}
    \item \textit{Ipotenusa}: è sempre il lato più lungo e si oppone all’angolo retto.
    \item \textit{Cateti}: sono i lati che formano l’angolo retto.
    \item \textit{Angoli acuti}: la loro somma è sempre 90°.
    \item \textit{Altezza relativa all’ipotenusa}: se si traccia dal vertice dell’angolo retto, divide il triangolo rettangolo in due \textit{triangoli simili}.
\end{itemize}

\textbf{Metodi per la risoluzione}
\textit{1. Teorema di Pitagora.}\\
In un triangolo rettangolo di cateti \(a,b\) e ipotenusa \(c\):
\[
a^2 + b^2 = c^2.
\]
Questo permette di calcolare un lato se si conoscono gli altri due.

\textit{2. Utilizzo della trigonometria.}\\
Le funzioni trigonometriche (\(\sin\), \(\cos\), \(\tan\)) permettono di trovare gli elementi mancanti del triangolo (lati o angoli) conoscendo una combinazione di angoli e/o lati. Ad esempio:
\[
\sin \alpha = \frac{\text{cateto opposto}}{\text{ipotenusa}},
\quad
\cos \alpha = \frac{\text{cateto adiacente}}{\text{ipotenusa}},
\quad
\tan \alpha = \frac{\text{cateto opposto}}{\text{cateto adiacente}}.
\]

Vedremo molte più nozioni necessarie per risolvere un triangolo rettangolo generico nella sezione di trigonometria di questo manuale.

\noindent
Nei triangoli rettangoli con \emph{angoli particolari}, sono di particolare interesse quelli con misure \(30^\circ\text{–}60^\circ\text{–}90^\circ\) e quelli con misure \(45^\circ\text{–}45^\circ\text{–}90^\circ\). Nel primo caso, il cateto opposto all’angolo di \(30^\circ\) è la metà dell’ipotenusa, mentre l’altro cateto misura \(\sqrt{3}/2\) volte l’ipotenusa. Nel secondo, i due cateti sono \emph{uguali} e l’ipotenusa è \(\sqrt{2}\) volte ciascun cateto.

\begin{center}
\begin{tikzpicture}[scale=1.0, line cap=round, line join=round]

% Triangolo 30-60-90 (hypotenuse=2)
\coordinate (A) at (0,0);
\coordinate (B) at (2,0); 
% cateto opposto 30°=1 => cateto opposto 60°= sqrt(3) => ipotenusa=2
\coordinate (C) at (0, {sqrt(3)});

\draw[thick] (A)--(B)--(C)--cycle;
\node[below left] at (A) {\small $A$};
\node[below right] at (B) {\small $B$};
\node[above left] at (C) {\small $C$};
\node[below] at ($(A)!0.5!(B)$) {\small 2};
\node[left] at ($(A)!0.5!(C)$) {\small 1};
\node[right] at ($(B)!0.5!(C)$) {\small $\sqrt{3}$};


% Triangolo 45-45-90 (cateto=1 => ipotenusa= sqrt(2))
\coordinate (D) at (4,0);
\coordinate (E) at (5,0);
\coordinate (F) at (4,1);

\draw[thick] (D)--(E)--(F)--cycle;
\node[below left] at (D) {\small $D$};
\node[below right] at (E) {\small $E$};
\node[left] at (F) {\small $F$};
\node[below] at ($(D)!0.5!(E)$) {\small 1};
\node[left] at ($(D)!0.5!(F)$) {\small 1};
\node[right] at ($(E)!0.5!(F)$) {\small $\sqrt{2}$};

\end{tikzpicture}
\end{center}

Un’altra categoria di \emph{triangoli speciali} è data dai \textbf{triangoli rettangoli} che presentano lati \emph{interi} in base al \emph{Teorema di Pitagora}. In tal caso, i tre lati formano una \textbf{terna pitagorica}, cioè un triplo di numeri interi \((a, b, c)\) con \(a^2 + b^2 = c^2\). Sotto sono rappresentati tre esempi di triangoli rettangoli con terne pitagoriche note:

\begin{center}
\begin{tikzpicture}[scale=0.3, line cap=round, line join=round]

% --- Primo triangolo (3,4,5) ---
\coordinate (A1) at (0,0);
\coordinate (B1) at (3,0);
\coordinate (C1) at (3,4);

\draw[thick] (A1)--(B1)--(C1)--cycle;

\node[below] at ($(A1)!0.5!(B1)$) {\small 3};
\node[right] at ($(B1)!0.5!(C1)$) {\small 4};
\node[sloped, above left] at ($(A1)!0.5!(C1)$) {\small 5};

% --- Secondo triangolo (5,12,13) ---
\coordinate (A2) at (6,0);
\coordinate (B2) at (11,0);
\coordinate (C2) at (11,12);

\draw[thick] (A2)--(B2)--(C2)--cycle;

\node[below] at ($(A2)!0.5!(B2)$) {\small 5};
\node[right] at ($(B2)!0.5!(C2)$) {\small 12};
\node[sloped, above left] at ($(A2)!0.5!(C2)$) {\small 13};

% --- Terzo triangolo (8,15,17) ---
\coordinate (A3) at (14,0);
\coordinate (B3) at (22,0);
\coordinate (C3) at (22,15);

\draw[thick] (A3)--(B3)--(C3)--cycle;

\node[below] at ($(A3)!0.5!(B3)$) {\small 8};
\node[right] at ($(B3)!0.5!(C3)$) {\small 15};
\node[sloped, above left] at ($(A3)!0.5!(C3)$) {\small 17};

\end{tikzpicture}
\end{center}

I primi otto \emph{tripli} di numeri interi che soddisfano \(a^2 + b^2 = c^2\) sono
\[
(3,4,5),\quad
(5,12,13),\quad
(6,8,10),\quad
(7,24,25),\quad
(8,15,17),\quad
(9,40,41),\quad
(10,24,26),\quad
(12,35,37).
\]

\paragraph{Esempio: Scala appoggiata a un muro (Teorema di Pitagora)}
Immaginiamo una \textit{scala} di lunghezza 5 metri appoggiata a un muro, con la base a 3 metri dalla parete. Vogliamo trovare l’altezza \(h\) a cui arriva la scala. Dal Teorema di Pitagora:
\[
h^2 = 5^2 - 3^2 = 25 - 9 = 16
\quad\Longrightarrow\quad
h = 4\,\text{m}.
\]

\begin{center}
\begin{tikzpicture}[scale=0.9]
    % Parete verticale: x=0
    \draw[thick] (0,0)--(0,5) node[above] {\small parete};

    % Pavimento orizzontale: y=0
    \draw[thick] (-0.5,0)--(6,0) node[right] {\small pavimento};

    % Punto base scala: B(3,0)
    \coordinate (B) at (3,0);
    % Punto in alto scala: A(0,4)
    \coordinate (A) at (0,4);

    % Scala
    \draw[thick, dashed] (B)--(A);

    \fill (A) circle(1.2pt) node[left]{$A$};
    \fill (B) circle(1.2pt) node[below]{$B$};

    % Segmenti e label
    \draw[<->] (0,-0.4)--(3,-0.4) node[midway,below]{$3\,\text{m}$};
    \draw[<->] (3,0)--(3,4) node[midway,right]{$h=4\,\text{m}$};
    \draw[<->, dashed] (-0.4,0)--(-0.4,4) node[midway,left]{$4\,\text{m}$};

    \node at ($(B)!0.5!(A) + (0.5,0.3)$) {\small $5\,\text{m}$};
\end{tikzpicture}
\end{center}

\paragraph{Esempio: Albero e angolo di elevazione (Trigonometria)}
Supponiamo di voler misurare l’altezza di un \textit{albero} senza scalarlo. Ci poniamo a 10\,m di distanza dalla base e misuriamo un \textit{angolo di elevazione} di 30°. Vogliamo calcolare \(h\).

\[
\tan(30^\circ) 
= \frac{h}{10}
\quad\Longrightarrow\quad
h = 10 \cdot \tan(30^\circ)
= 10 \cdot 0.577 \approx 5.77\,\text{m}.
\]

\begin{center}
\begin{tikzpicture}[scale=0.6]
    % Albero
    \draw[thick, green!70!black] (6,0)--(6,5.77)
        node[above]{\small Albero};

    \fill (6,0) circle(1.2pt) node[below]{$\text{Base}$};

    % Osservatore a (0,0)
    \fill (0,0) circle(1.2pt) node[below left]{\small Osservatore};

    % Terreno
    \draw[thick] (-1,0)--(8,0);

    % Angolo di elevazione
    \draw[dashed] (0,0)--(6,5.77);
    \draw (0.8,0) arc (0:18.4349:0.8); 
    % 18.4349° ~ rad(30° in deg) but we want 30°, let's approximate

    % Distanza 10m
    \draw[<->] (0,-0.5)--(6,-0.5) node[midway,below]{$10\,\text{m}$};

    % Altezza h
    \draw[<->] (6,0)--(6,5.77) node[midway,right]{$5.77\,\text{m}$};
\end{tikzpicture}
\end{center}
\newpage

\subsectionstar{[32] Risoluzione di un Triangolo Qualunque}
Risolvere un triangolo significa determinare la misura di tutti i suoi lati e angoli, a partire da alcune informazioni iniziali che possono essere lati o angoli dati. Questa procedura, chiamata risoluzione del triangolo, si applica a triangoli qualunque, senza necessariamente un angolo retto. Nei risultati che vedremo useremo seno e coseno che non abbiamo ancora visto ma che vedremo a breve, ad ora possiamo solo considerarli come delle funzioni che si applicano sugli angoli i quali valori vedremo meglio a breve.

Questo argomento lo si trova come parte della sezione sui triangoli, dato che ha propriamente a che fare con il materiale sui triangoli, tuttavia una vera e propria comprensione di come risolvere un triangolo qualsiasi è solo possibile dopo aver visto la sezione di trigonometria. Si consiglia allo studente di non soffermarsi troppo su parti di questo argomento che non potranno ancora essere chiare ma invece di rileggerlo una volta dopo aver concluso la parte di trigonometria.

Per prima cosa introduciamo a due teoremi fondamentali nella risoluzione di triangoli generali. Successivamente vediamo un esempio in cui questi ed altri struemnti possono essere applicati per la risoluzione.

\subsubsection*{Teorema dei seni}
Il teorema dei seni afferma che, dato un triangolo qualsiasi con lati \(a, b, c\) e angoli opposti rispettivamente \(\alpha, \beta, \gamma\), vale la seguente relazione:
\[
\frac{a}{\sin \alpha} = \frac{b}{\sin \beta} = \frac{c}{\sin \gamma}.
\]

\paragraph{Esempio numerico (applicazione del teorema dei seni)}
Dato un triangolo \(ABC\), siano noti i seguenti dati:
\[
\alpha=30^\circ,\quad \beta=45^\circ,\quad c=8\,cm.
\]

Per determinare il terzo angolo \(\gamma\):
\[
\gamma = 180^\circ - (\alpha+\beta) = 180^\circ - (30^\circ + 45^\circ) = 105^\circ.
\]

Calcoliamo poi il lato \(a\):
\[
\frac{a}{\sin\alpha} = \frac{c}{\sin\gamma} \;\Longrightarrow\; a=\frac{c\sin\alpha}{\sin\gamma} = \frac{8\cdot\sin30^\circ}{\sin105^\circ}\approx4.14\,cm.
\]

Analogamente, per il lato \(b\):
\[
b=\frac{c\sin\beta}{\sin\gamma}=\frac{8\cdot\sin45^\circ}{\sin105^\circ}\approx5.86\,cm.
\]

Abbiamo così risolto completamente il triangolo.

\subsubsection*{Teorema del coseno}
Il teorema del coseno generalizza il teorema di Pitagora e permette di determinare un lato di un triangolo qualsiasi conoscendo gli altri due lati e l'angolo compreso. La sua formula generale è:
\[
c^2=a^2+b^2-2ab\cos\gamma.
\]

\paragraph{Esempio del teorema del coseno}
Dati due lati \(a=7\,cm\), \(b=5\,cm\) e l’angolo \(\gamma=60^\circ\), determinare il lato \(c\):

Applicando il teorema del coseno si ha:
\[
c^2 = a^2 + b^2 - 2ab\cos\gamma = 7^2+5^2-2\cdot 7\cdot 5\cdot\cos60^\circ.
\]

Poiché \(\cos60^\circ=0.5\), abbiamo:
\[
c^2 = 49 + 25 - 35 = 39 \quad\Longrightarrow\quad c=\sqrt{39}\approx 6.25\,cm.
\]

\paragraph{Esempio su un Triangolo Scaleno}
A partire dal valore ottenuto per \(c\), è possibile determinare facilmente gli altri angoli con le analoghe formule del teorema.

\noindent
Un \emph{triangolo scaleno} è caratterizzato da tre lati e tre angoli \emph{tutti diversi} fra loro. Supponiamo di conoscere in partenza due \emph{angoli} e un \emph{lato} non adiacente a questi angoli, e di voler ricavare tutte le restanti misure. Consideriamo, ad esempio, il triangolo \(ABC\) in cui:

\[
\angle A = 43^\circ, 
\quad
\angle B = 67^\circ,
\quad
BC = 12.
\]
\begin{center}
\begin{tikzpicture}[scale=0.3, line cap=round, line join=round]

% Definiamo i punti B, C, A in modo semplice, senza calcoli di intersezione
\coordinate (B) at (0,0);
\coordinate (C) at (12,0);
\coordinate (A) at (3,7); % Posizione arbitraria che rende il triangolo non degenere

% Disegno del triangolo
\draw[thick] (B)--(C)--(A)--cycle;

% Etichette dei vertici con i (supposti) angoli
\node[below left]  at (B) {\small B ($67^\circ$)};
\node[below right] at (C) {\small C};
\node[above]       at (A) {\small A ($43^\circ$)};

% Etichetta BC=12
\node[below] at ($(B)!0.5!(C)$) {\small 12};

\end{tikzpicture}
\end{center}

Dal momento che in un triangolo la somma degli angoli è \(180^\circ\), deduciamo

\[
\angle C = 180^\circ - (43^\circ + 67^\circ) = 70^\circ.
\]

A questo punto, se indichiamo con \(a = BC\), \(b = AC\) e \(c = AB\), allora \(a=12\) e dobbiamo trovare \(b\) e \(c\). Per farlo, possiamo sfruttare la \emph{Legge dei Seni}:

\[
\frac{a}{\sin A} 
= \frac{b}{\sin B}
= \frac{c}{\sin C}.
\]

Poiché \(a = 12\) e \(\angle A = 43^\circ\), otteniamo

\[
\frac{12}{\sin 43^\circ} 
= \frac{b}{\sin 67^\circ}
= \frac{c}{\sin 70^\circ}.
\]

Se ci focalizziamo su \( \tfrac{12}{\sin 43^\circ} = \tfrac{b}{\sin 67^\circ} \), isoliamo \(b\):

\[
b = \frac{\sin 67^\circ}{\sin 43^\circ} \,\times\, 12.
\]
Calcolando (anche approssimando), troviamo il valore numerico di \(b\). Analogamente,

\[
c = \frac{\sin 70^\circ}{\sin 43^\circ} \,\times\, 12.
\]

Una volta noti i lati \(b\) e \(c\), possiamo voler determinare l’altezza relativa a uno di essi o, più in generale, \emph{l’area} del triangolo. Ad esempio, se preferiamo usare la formula \( \tfrac{1}{2}\,b\,c\,\sin A \) (dato che \(A\) è l’angolo fra i lati \(b\) e \(c\)), è sufficiente inserire i valori numerici:

\[
\text{Area} 
= \frac{1}{2} \times b \times c \times \sin A.
\]

Se invece ci interessa l’altezza \(h_a\) (quella relativa al lato \(BC\)), possiamo utilizzare la definizione di area:

\[
\text{Area} 
= \frac{1}{2} \times (\text{base}) \times (\text{altezza}),
\]
quindi, scegliendo come base \(BC = 12\),
\[
h_a = \frac{2 \times \text{Area}}{12}.
\]

\section{Poligoni}
\subsectionstar{[36] Somma degli Angoli Interni}
Un \textit{poligono} è una figura geometrica bidimensionale delimitata da una successione finita di segmenti retti collegati per formare un percorso chiuso. I segmenti, chiamati lati, si incontrano nei vertici, e l’insieme di tali lati costituisce la figura. Per questa ragione, ogni figura che soddisfa questa definizione è un poligono.

I poligoni si suddividono in due categorie principali. I \textit{poligoni regolari} sono quelli in cui tutti i lati sono congruenti e tutti gli angoli interni hanno la stessa ampiezza. Per ogni \(n \geq 3\) esiste esattamente un poligono regolare a \(n\) lati. Ad esempio, il triangolo equilatero, con tre lati e tre angoli di \(60^\circ\), è il poligono regolare a tre lati. I \textit{poligoni irregolari}, invece, non presentano questa uniformità: i loro lati e/o i loro angoli interni possono variare pur mantenendo la proprietà della chiusura.

Una caratteristica fondamentale di ogni poligono, sia esso regolare o irregolare, è la somma degli angoli interni \(S\). Questa è data dalla formula
\[
S = (n-2) \times 180^\circ,
\]
dove \(n\) rappresenta il numero di lati. Nel caso di un poligono regolare, ciascun angolo interno \(\theta\) si ottiene dividendo \(S\) per \(n\):
\[
\theta = \frac{(n-2) \times 180^\circ}{n}.
\]
Questa formula è molto utile per determinare le proprietà angolari della figura, indipendentemente dal fatto che il poligono sia regolare o irregolare.

La seguente discussione analizza alcune figure che rappresentano poligoni, evidenziando le loro caratteristiche distintive:

\textbf{Triangolo Equilatero.}  
Si tratta di un poligono a tre lati in cui tutti i lati sono uguali e ogni angolo interno misura \(60^\circ\). Questa figura è il caso più semplice di poligono regolare ed è un esempio fondamentale per comprendere la definizione stessa di poligono.

\begin{center}
\textbf{Triangolo Equilatero}\\[1ex]
\begin{tikzpicture}[scale=1]
  \draw (0,0) -- (2,0) -- (1,1.732) -- cycle;
  \foreach \coord in {(0,0), (2,0), (1,1.732)} {
    \fill \coord circle (2pt);
  }
\end{tikzpicture}
\end{center}

\textbf{Pentagono Regolare.}  
Il pentagono regolare è caratterizzato da cinque lati di lunghezza uguale e da angoli interni tutti congruenti, ciascuno misurante \(108^\circ\) (poiché la somma degli angoli interni è \(540^\circ\)). La sua simmetria rende il pentagono un esempio didattico importante per illustrare le proprietà geometriche dei poligoni regolari.

\begin{center}
\textbf{Pentagono Regolare}\\[1ex]
\begin{tikzpicture}[scale=1]
  \draw (90:2) 
    \foreach \angle in {162,234,306,18} { -- (\angle:2) } -- cycle;
  \foreach \angle in {90,162,234,306,18} {
    \fill (\angle:2) circle (2pt);
  }
\end{tikzpicture}
\end{center}

\textbf{Rettangolo.}  
Il rettangolo è un poligono a quattro lati che, pur presentando quattro angoli retti (ciascuno di \(90^\circ\)) e quindi una somma degli angoli interni pari a \(360^\circ\), è considerato irregolare se non è un quadrato. In un rettangolo non quadrato, solo le coppie di lati opposti sono congruenti, mentre i lati adiacenti hanno lunghezze diverse. Questo esempio evidenzia come un poligono possa rispettare la formula degli angoli interni pur non avendo tutti i lati uguali.
\begin{center}
\textbf{Rettangolo}\\[1ex]
\begin{tikzpicture}[scale=0.8]
  \draw (0,0) -- (4,0) -- (4,2) -- (0,2) -- cycle;
  \foreach \point in {(0,0), (4,0), (4,2), (0,2)} {
    \fill \point circle (2pt);
  }
\end{tikzpicture}
\end{center}

\textbf{Rombo.}  
Il rombo è un poligono a quattro lati in cui tutti i lati sono congruenti, ma gli angoli interni non sono necessariamente retti. Ciò significa che, pur avendo una certa uniformità nei lati, il rombo non è considerato un poligono regolare a causa della variazione degli angoli, che possono essere maggiori o minori di \(90^\circ\).

\begin{center}
\textbf{Rombo}\\[1ex]
\begin{tikzpicture}[scale=0.8]
  \draw (0,0) -- (3,1) -- (4,3) -- (1,2) -- cycle;
  \foreach \point in {(0,0), (3,1), (4,3), (1,2)} {
    \fill \point circle (2pt);
  }
\end{tikzpicture}
\end{center}

\textbf{Esagono Regolare.}  
L’esagono regolare possiede sei lati uguali e la somma degli angoli interni è \(720^\circ\), da cui si deduce che ogni angolo interno misura \(120^\circ\). Questo poligono è un ulteriore esempio di figura regolare, in cui la simmetria angolare e laterale è perfettamente mantenuta.

\begin{center}
\textbf{Esagono Regolare}\\[1ex]
\begin{tikzpicture}[scale=1]
  \draw (0:2) 
    \foreach \angle in {60,120,180,240,300} { -- (\angle:2) } -- cycle;
  \foreach \angle in {0,60,120,180,240,300} {
    \fill (\angle:2) circle (2pt);
  }
\end{tikzpicture}
\end{center}

\paragraph*{Conclusioni.} In sintesi, la formula 
\[
S = (n-2) \times 180^\circ,
\]
che esprime la somma degli angoli interni, è valida per ogni poligono, indipendentemente dal fatto che esso sia regolare o irregolare. In particolare, anche se nei poligoni irregolari le ampiezze degli angoli interni possono variare, il legame tra il numero di lati \(n\) e la somma complessiva degli angoli rimane invariato, sottolineando così la generalità e l’importanza della suddetta relazione.
\newpage

\subsectionstar{[40] Trapezi e Parallelogrammi}
\subsubsection*{Trapezi}

Un \textit{trapezio} è un quadrilatero con almeno una coppia di lati paralleli, detti basi, mentre i lati non paralleli sono detti obliqui. Di seguito si espongono i vari tipi di trapezi, il calcolo dell'area e del perimetro, e una discussione sugli angoli.

\subsubsection*{Tipi di Trapezi}

\begin{itemize}
  \item \textbf{Trapezio scaleno:} È il trapezio generico, in cui le basi sono parallele ma i lati obliqui hanno lunghezze differenti.
  \item \textbf{Trapezio rettangolo:} In questo trapezio, uno dei lati obliqui coincide con l'altezza, essendo perpendicolare alle basi.
  \item \textbf{Trapezio isoscele:} I lati obliqui sono congruenti e gli angoli alla base sono uguali.
\end{itemize}

\subsubsection*{Calcolo dell'Area e del Perimetro}

L'area \(A\) si calcola con:
\[
A = \frac{(b_1 + b_2)}{2} \times h,
\]
dove \(b_1\) e \(b_2\) sono le lunghezze delle basi e \(h\) l'altezza, ossia la distanza perpendicolare tra le basi.

Il perimetro \(P\) è:
\[
P = b_1 + b_2 + \ell_1 + \ell_2,
\]
con \(\ell_1\) e \(\ell_2\) le lunghezze dei lati obliqui.

\subsubsection*{Note sugli Angoli}

Negli angoli di un trapezio:
\begin{itemize}
  \item Nel trapezio rettangolo, almeno un angolo è \(90^\circ\).
  \item Nel trapezio isoscele, gli angoli alla base sono congruenti.
  \item Nel trapezio scaleno non vi sono vincoli particolari, ad eccezione della somma totale degli angoli interni, che è sempre \(360^\circ\), come abbiamo visto essere valido in generale per tutti i quadrilateri.
\end{itemize}

\subsubsection*{Esempi di Trapezi}

\textbf{Trapezio scaleno:}\\  
Si consideri un trapezio con base maggiore di lunghezza 6 e base minore di lunghezza 3, dove i lati obliqui hanno lunghezze differenti. I lati \(AB\) e \(DC\) sono le basi (lunghezze 6 e 3 rispettivamente), mentre \(AD\) e \(BC\) sono i lati obliqui (di lunghezze approssimativamente \(\sqrt{1^2+3^2}\approx3.16\) e \(\sqrt{2^2+3^2}\approx3.61\) rispettivamente).

\begin{center}
\textbf{Trapezio scaleno}\\[1ex]
\begin{tikzpicture}[scale=0.9]
  \coordinate (A) at (0,0);
  \coordinate (B) at (6,0);
  \coordinate (C) at (4,3);
  \coordinate (D) at (1,3);
  \draw (A) -- (B) -- (C) -- (D) -- cycle;
  \foreach \pt in {(A), (B), (C), (D)} {
    \fill \pt circle (2pt);
  }
  \draw[dashed] (D) -- ++(0,-3);
  \node at ($(D)+(0,-1.5)$) [left] {\(h\)};
\end{tikzpicture}
\end{center}

\bigskip

\textbf{Trapezio rettangolo:}\\  
In questo trapezio, uno dei lati obliqui coincide con l'altezza.
Il lato \(AD\) è verticale e rappresenta l'altezza \(h=3\). Le basi sono \(AB\) (lunghezza 5) e \(DC\) (lunghezza 3), mentre il lato \(BC\) è obliquo.

\begin{center}
\textbf{Trapezio rettangolo}\\[1ex]
\begin{tikzpicture}[scale=0.9]
  \coordinate (A) at (0,0);
  \coordinate (B) at (5,0);
  \coordinate (C) at (3,3);
  \coordinate (D) at (0,3);
  \draw (A) -- (B) -- (C) -- (D) -- cycle;
  \foreach \pt in {(A), (B), (C), (D)} {
    \fill \pt circle (2pt);
  }
  \draw[dashed] (D) -- (0,0);
  \node at (0,1.5) [left] {\(h\)};
\end{tikzpicture}
\end{center}

\bigskip

\textbf{Trapezio isoscele:}\\  
Si consideri un trapezio con basi di lunghezza 7 e 3, in cui i lati obliqui sono congruenti. I lati obliqui \(AD\) e \(BC\) sono congruenti, e gli angoli alla base sono uguali.

\begin{center}
\textbf{Trapezio isoscele}\\[1ex]
\begin{tikzpicture}[scale=0.9]
  \coordinate (A) at (0,0);
  \coordinate (B) at (7,0);
  \coordinate (C) at (5,3);
  \coordinate (D) at (2,3);
  \draw (A) -- (B) -- (C) -- (D) -- cycle;
  \foreach \pt in {(A), (B), (C), (D)} {
    \fill \pt circle (2pt);
  }
  \draw[dashed] (D) -- ++(0,-3);
  \node at ($(D)+(0,-1.5)$) [left] {\(h\)};
\end{tikzpicture}
\end{center}
\subsubsection*{Parallelogrammi}

Un \textit{parallelogramma} è un quadrilatero in cui ciascuna coppia di lati opposti è parallela. In un parallelogramma i lati opposti sono congruenti e gli angoli opposti sono uguali, mentre gli angoli adiacenti sono supplementari (cioè la loro somma è \(180^\circ\)).

La formula per il calcolo dell'area \(A\) è:
\[
A = b \times h,
\]
dove \(b\) rappresenta la lunghezza della base e \(h\) l'altezza, ossia la distanza perpendicolare tra la base e il lato opposto. Il perimetro \(P\) si ottiene sommando la lunghezza di tutti i lati:
\[
P = 2(b + \ell),
\]
dove \(\ell\) è la lunghezza del lato obliquo.

\subsubsection*{Esempio di Parallelogramma Generico}

Prendiamo un esempio di parallelogramma generico:

\begin{center}
\textbf{Parallelogramma Generico}\\[1ex]
\begin{tikzpicture}[scale=0.9]
  \coordinate (A) at (0,0);
  \coordinate (B) at (6,0);
  \coordinate (C) at (7,3);
  \coordinate (D) at (1,3);
  \draw (A) -- (B) -- (C) -- (D) -- cycle;
  \foreach \pt in {(A), (B), (C), (D)} {
    \fill \pt circle (2pt);
  }
  \draw[dashed] (D) -- ++(0,-3);
  \node at ($(D)+(0,-1.5)$) [left] {\(h\)};
\end{tikzpicture}
\end{center}

In questo caso, la base \(AB\) misura 6, l'altezza (la distanza perpendicolare da \(D\) a \(AB\)) è \(h\), e il lato obliquo \(AD\) ha una lunghezza determinata dalla distanza tra \(A\) e \(D\).

Esistono inoltre altre tipologie di parallelogrammi, ottenute imponendo ulteriori condizioni:
\begin{itemize}
  \item \textbf{Rettangolo:} Un parallelogramma in cui tutti gli angoli interni sono retti (\(90^\circ\)). In questo caso, l'area si calcola con \(A = b \times h\) (con \(h\) uguale alla lunghezza del lato perpendicolare alla base) e il perimetro con \(P = 2(b + \ell)\).
  \item \textbf{Rombo:} Un parallelogramma in cui tutti i lati sono congruenti, anche se gli angoli non sono retti. Le diagonali di un rombo si intersecano perpendicolarmente, e l'area può essere calcolata anche con la formula \(A = \frac{d_1 \times d_2}{2}\), dove \(d_1\) e \(d_2\) sono le lunghezze delle diagonali.
  \item \textbf{Quadrato:} Un caso particolare di parallelogramma che è sia rettangolo che rombo. In un quadrato tutti i lati sono uguali e tutti gli angoli interni sono retti. L'area si calcola con \(A = l^2\) e il perimetro con \(P = 4l\), dove \(l\) è la lunghezza del lato.
\end{itemize}
\newpage

\section{Geometria Analitica \& Coniche}
\noindent
La \textbf{Geometria Analitica} nasce dall’idea di associare a ogni punto del piano una coppia \((x,y)\) di numeri reali, in modo da descrivere le figure geometriche come \textit{soluzioni} di determinate equazioni. Se in precedenza abbiamo studiato la geometria piana con strumenti puramente geometrici (teoremi, costruzioni, proprietà), e l’algebra come disciplina autonoma, la geometria analitica fonde questi due mondi. Attraverso i \textit{polinomi in due variabili} \(x\) e \(y\), si individua l’insieme di tutti i punti \((x,y)\) che soddisfano una determinata relazione algebrica, e questo insieme, disegnato sul piano cartesiano, rappresenta l’\textit{oggetto geometrico} corrispondente.

Se, per esempio, prendiamo un polinomio \(\,F(x,y) = x^4 + y^4 - 1\), la \textit{figura} associata a questo polinomio è l’insieme di tutti i \((x,y)\) per cui
\[
x^4 + y^4 = 1.
\]
Si tratta di una curva chiusa, detta a volte \q{supercerchio} di esponente 4, la cui forma è simile a un quadrato con spigoli smussati. Nel piano cartesiano, rappresentiamo quindi tutte quelle coppie di numeri $x$ e $y$ tali per cui suddosifino l'equazione sopra, formalmente i punti che disegnamo sul grafico sono quelli appartenenti al seguente insieme:$$\c{V}_F = \{(x, y) \in \b{R}^2 : x^4 + y^4 = 1\}$$Notiamo ad esempio che $(0, 0) \not \in \c{V}_F$ dato che $0^4 + 0^4 \not = 1$ ed infatti non lo disegnamo sul grafico, tuttavia notiamo che $1^4 + 0^4 = 1$ e quindi deduciamo che $(1, 0) \in \c{V}_F$ e perciò disegnamo $(1, 0)$ sul grafico; procedendo così per ogni coppia di numeri reali $(x, y)$ andiamo a descrivere tutti i punti in $\c{V}_F$, i quali possiamo poi disegnare sul piano cartesiano per avere tutto il grafico dell'equazione:

\medskip

\begin{center}
\begin{tikzpicture}[scale=2.0]
  % Assi cartesiani
  \draw[->] (-1.3,0) -- (1.3,0) node[right] {$x$};
  \draw[->] (0,-1.3) -- (0,1.3) node[above] {$y$};
  
  % 1) Curva vista come y = ±(1 - x^4)^(1/4)
  %    domain in x in [-1,1]
  \draw[smooth,domain=-1:1,samples=1000,variable=\xx]
       plot ({\xx},{(1-(\xx)^4)^(1/4)});
  \draw[smooth,domain=-1:1,samples=1000,variable=\xx]
       plot ({\xx},{-(1-(\xx)^4)^(1/4)});

  % 2) Curva vista come x = ±(1 - y^4)^(1/4)
  %    domain in y in [-1,1]
  \draw[smooth,domain=-1:1,samples=1000,variable=\yy]
       plot ({(1-(\yy)^4)^(1/4)},{\yy});
  \draw[smooth,domain=-1:1,samples=1000,variable=\yy]
       plot ({-(1-(\yy)^4)^(1/4)},{\yy});

  % Origine e label
  \node[below left] at (0,0) {$O$};
  \node at (1.1,1.1) {$x^4 + y^4 = 1$};
\end{tikzpicture}
\end{center}

\medskip

In questo modo, \textit{geometria} e \textit{algebra} si integrano a vicenda: il polinomio \(\,F(x,y)=0\) descrive l’ente geometrico nel piano, e l’analisi di \(\,F\) con strumenti algebrici (risoluzione di sistemi, fattorizzazioni, studio dei gradi e delle soluzioni) consente di comprendere meglio la figura stessa. Viceversa, molte nozioni di geometria (posizioni reciproche, tangenti, aree, ecc.) si possono affrontare sfruttando la risoluzione di equazioni e l’uso di metodi di grado superiore (equazioni di secondo grado, sistemi di grado elevato, ecc.).
\newpage

\subsectionstar{[2 - 24] Il Cerchio}
In queste note si riassumono le proprietà fondamentali del cerchio, come definite nel documento di riferimento. Un \textbf{cerchio} è l'insieme di tutti i punti di un piano che si trovano ad una distanza costante dal centro. Tale distanza è chiamata \textbf{raggio} (\(r\)), mentre il \textbf{diametro} (\(d\)) è il segmento che passa per il centro e collega due punti del cerchio, con la relazione
\[
d = 2r.
\]
La \textbf{circonferenza} è il perimetro del cerchio, calcolata tramite
\[
C = 2\pi r,
\]
e l'\textbf{area} del cerchio è data da
\[
A = \pi r^2.
\]

\begin{center}
\setlength{\tabcolsep}{12pt}
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{|l|p{10cm}|}
\hline
\textbf{Termine} & \textbf{Definizione} \\ \hline
Cerchio & Insieme di tutti i punti di un piano ad una distanza costante dal centro. \\ \hline
Raggio (\(r\)) & Distanza dal centro a qualsiasi punto del cerchio. \\ \hline
Diametro (\(d\)) & Segmento che passa per il centro e collega due punti, con \(d = 2r\). \\ \hline
Circonferenza & Perimetro del cerchio, calcolato con \(C = 2\pi r\). \\ \hline
Area & Regione interna al cerchio, calcolata con \(A = \pi r^2\). \\ \hline
\end{tabular}
\end{center}

\begin{center}
\begin{tikzpicture}[scale=1]
  % Cerchio principale
  \draw (0,0) circle (2cm);
  % Raggio e diametro
  \draw[red, very thick, ->] (0,0) -- (2,0) node[midway, below] {\(r\)};
  \draw[blue, very thick, <->] (0,-2) -- (0,2) node[midway, left] {\(d\)};
  % Centro e punto sul cerchio
  \fill (0,0) circle (2pt) node[below left] {Centro};
  \fill (2,0) circle (2pt) node[below right] {Punto};
\end{tikzpicture}
\end{center}

\subsubsection*{Angoli, Archi e Settori Circolari}
Consideriamo ora le porzioni del cerchio relative agli angoli e agli archi. Un \textbf{angolo al centro} ha il vertice nel centro del cerchio ed è determinato da due raggi; tale angolo, indicato con \(\alpha\), intercetta un arco della circonferenza. Un \textbf{angolo iscritto} ha il vertice su un punto della circonferenza ed intercetta lo stesso arco; questo angolo si indica con \(\beta\) e, per un noto teorema, soddisfa la relazione
\[
\beta = \frac{\alpha}{2}.
\]

Le formule per la lunghezza dell'arco \(L\) e l'area del settore \(A_{\text{settore}}\) sono le seguenti. Se l'angolo \(\alpha\) è espresso in radianti:
\[
L = r\alpha,\quad A_{\text{settore}} = \frac{1}{2}r^2\alpha.
\]
Se l'angolo è espresso in gradi, le formule diventano:
\[
L = \frac{\alpha}{360^\circ} \cdot 2\pi r,\quad A_{\text{settore}} = \frac{\alpha}{360^\circ} \cdot \pi r^2.
\]

Il diagramma seguente illustra la relazione tra l'angolo al centro \(\alpha\) e l'angolo iscritto \(\beta\):
\begin{center}
\begin{tikzpicture}[scale=1, every node/.style={font=\small}]
  % Definire i punti fondamentali
  \coordinate (O) at (0,0);
  \coordinate (A) at (2,0);
  \coordinate (B) at (40:2cm);
  
  % Disegnare il cerchio e le due raggi che formano l'angolo al centro (α)
  \draw (O) circle (2cm);
  \draw[thick] (O) -- (A);
  \draw[thick] (O) -- (B);
  
  % Etichettare l'angolo centrale α
  \draw (0.5,0) arc (0:40:0.5cm);
  \node at (0.7,0.3) {\(\alpha\)};
  
  % Segnare i punti A e B sulla circonferenza
  \fill (A) circle (2pt) node[below right] {A};
  \fill (B) circle (2pt) node[above right] {B};
  
  % Scegliere un punto C sulla circonferenza, posizionato sul lato opposto rispetto al centro per avere l'angolo iscritto
  \coordinate (C) at (200:2cm);
  \fill (C) circle (2pt) node[below left] {C};
  
  % Disegnare i segmenti che collegano C con A e B
  \draw[thick] (C) -- (A);
  \draw[thick] (C) -- (B);
  
  % Utilizzare il comando pic per segnare l'angolo iscritto β in C (che intercetta lo stesso arco AB)
  \usetikzlibrary{angles,quotes}
  \pic [draw, "$\beta$", angle eccentricity=1.5, angle radius=0.5cm] {angle = A--C--B};
\end{tikzpicture}
\end{center}

Questo diagramma evidenzia come l'angolo iscritto \(\beta\) (con vertice in C) sia la metà dell'angolo al centro \(\alpha\) e come ciò sia coerente con le formule per la lunghezza dell'arco e l'area del settore.

\begin{center}
\begin{tabular}{|l|p{10cm}|}
\hline
\textbf{Termine} & \textbf{Definizione} \\ \hline
Angolo al centro (\(\alpha\)) & Angolo con vertice nell'origine \(O\), formato dai raggi \(OA\) e \(OB\). \\ \hline
Angolo alla circonferenza (\(\beta\)) & Angolo con vertice su un punto della circonferenza, che intercetta l'arco compreso tra \(A\) e \(B\). \\ \hline
Arco & Porzione della circonferenza delimitata dai punti \(A\) e \(B\). \\ \hline
Settore circolare & Regione del cerchio costituita dall'arco \(AB\) e dai raggi \(OA\) e \(OB\). \\ \hline
Corda & Segmento di retta che collega i punti \(A\) e \(B\). \\ \hline
\end{tabular}
\end{center}

\paragraph{Esempio}
Supponiamo di avere un cerchio con raggio \(r = 5\,\text{cm}\). L'area \(A\) del cerchio si calcola con la formula
\[
A = \pi r^2.
\]
Sostituendo \(r = 5\,\text{cm}\) si ottiene:
\[
A = \pi\cdot 5^2 = 25\pi\,\text{cm}^2.
\]

\paragraph{Esempio}
Supponiamo che, in un settore circolare, sia noto che l'angolo iscritto misura \(\beta = 30^\circ\) e che la lunghezza dell'arco corrispondente sia \(L = 10\,\text{cm}\). Ricordando che l'angolo al centro associato è il doppio di quello iscritto, si ha:
\[
\alpha = 2\beta = 60^\circ.
\]
Convertiamo \(\alpha\) in radianti:
\[
\alpha = 60^\circ = \frac{\pi}{3}\,\text{rad}.
\]
La relazione tra la lunghezza dell'arco e il raggio \(r\) è
\[
L = r\alpha.
\]
Da cui si ricava il raggio:
\[
r = \frac{L}{\alpha} = \frac{10}{\pi/3} = \frac{30}{\pi}\,\text{cm}.
\]
Una volta determinato il raggio, l'area del cerchio si calcola con:
\[
A = \pi r^2 = \pi\left(\frac{30}{\pi}\right)^2 = \frac{900}{\pi}\,\text{cm}^2.
\]
\newpage

\subsectionstar{[3] La Circonferenza}
\paragraph{Premessa}
Disegnare un'equazione su un piano cartesiano significa rappresentare graficamente l'insieme di tutte le coppie \((x,y)\) che soddisfano la relazione data. A differenza di una funzione, in cui ad un valore di \(x\) corrisponde un unico valore di \(y\), un'equazione in due variabili definisce una curva che può avere, per lo stesso \(x\) (o \(y\)), molteplici soluzioni. In altre parole, si tratta di individuare e tracciare tutti quei punti nel piano che rispettano l'equazione. Questo procedimento è fondamentale per la rappresentazione delle coniche, quali la circonferenza, l'ellisse, l'iperbole e la parabola. Iniziamo con la circonferenza, poiché abbiamo già visto la definizione del cerchio, e dimostriamo come, partendo dalla sua equazione, si possano calcolare la lunghezza (circonferenza) e l'area.



\subsubsection*{Circonferenza Unitaria}
La circonferenza unitaria è la circonferenza centrata nell'origine \(O(0,0)\) con raggio \(r=1\). La sua equazione è:
\[
x^2 + y^2 = 1.
\]
Nella figura sottostante viene rappresentata la circonferenza unitaria su un piano cartesiano.

\begin{center}
\begin{tikzpicture}[scale=1]
  % Assi cartesiani
  \draw[->] (-1.5,0) -- (1.5,0) node[right] {\(x\)};
  \draw[->] (0,-1.5) -- (0,1.5) node[above] {\(y\)};
  % Cerchio unitario
  \draw[thick, blue] (0,0) circle (1cm);
  % Origine
  \fill (0,0) circle (1.5pt) node[below left] {\(O\)};
\end{tikzpicture}
\end{center}

\subsubsection*{Equazioni della Circonferenza: Forma Generica e Forma Canonica}
Esistono diversi modi per scrivere l'equazione di una circonferenza. Un'equazione generica in due variabili di secondo grado può rappresentare una circonferenza se, completando il quadrato, è possibile riscriverla nella forma canonica
\[
(x-h)^2+(y-k)^2=r^2.
\]
In questa forma il punto \(C(h,k)\) è il centro della circonferenza e \(r\) è il raggio, ottenuto come radice quadrata del termine costante che compare sul lato destro dell'equazione.

Ad esempio, consideriamo l'equazione
\[
x^2+y^2+4x-6y+9=0.
\]
Per portarla alla forma canonica, completiamo il quadrato per \(x\) e \(y\):
\[
x^2+4x\quad \text{e}\quad y^2-6y.
\]
Si aggiungono i termini necessari:
\[
x^2+4x+4+(y^2-6y+9)= -9+4+9,
\]
cioè
\[
(x+2)^2+(y-3)^2=4.
\]
Da questa forma risulta chiaramente che il centro è \(C(-2,3)\) e il raggio \(r=2\).

Una volta ottenuta la forma canonica, possiamo facilmente calcolare altre grandezze, quali la lunghezza della circonferenza
\[
C=2\pi r,
\]
e l'area del cerchio
\[
A=\pi r^2.
\]

Variando i parametri \(h\), \(k\) e \(r\) si ottengono circonferenze differenti. Ad esempio:
\begin{itemize}
  \item La circonferenza unitaria, con \(h=0\), \(k=0\) e \(r=1\), ha equazione \(x^2+y^2=1\).
  \item La circonferenza con centro in \(C(2,1)\) e raggio \(r=2\) ha equazione \((x-2)^2+(y-1)^2=4\) e la vediamo disegnata in rosso.
  \item La circonferenza con centro in \(C(-1,-1)\) e raggio \(r=0.5\) ha equazione \((x+1)^2+(y+1)^2=0.25\) e la vediamo disegnata in verde.
\end{itemize}
La figura seguente illustra queste variazioni su un piano cartesiano:

\begin{center}
\begin{tikzpicture}[scale=0.8, every node/.style={font=\small}]
  % Assi cartesiani
  \draw[->] (-5,0) -- (5,0) node[right] {\(x\)};
  \draw[->] (0,-5) -- (0,5) node[above] {\(y\)};
  
  % Definizione delle tre circonferenze in forma canonica:
  % c1: centro in (0,0) e raggio 1: x^2+y^2=1
  % c2: centro in (2,1) e raggio 2: (x-2)^2+(y-1)^2=4
  % c3: centro in (-2,-1) e raggio 1.5: (x+2)^2+(y+1)^2=2.25
  
  % Disegna c1 (blu)
  \draw[blue, thick] (0,0) circle (1);
  
  % Disegna c2 (rosso)
  \draw[red, thick] (2,1) circle (2);
  
  % Disegna c3 (verde)
  \draw[green!70!black, thick] (-2,-1) circle (0.5);
  
  % Etichette dei centri
  \fill (0,0) circle (1.5pt) node[below left] {\(O\)};
  \fill (2,1) circle (1.5pt) node[above right] {\(C_2\)};
  \fill (-2,-1) circle (1.5pt) node[below left] {\(C_3\)};
\end{tikzpicture}
\end{center}
\paragraph*{Conclusioni.} In conclusione, la circonferenza unitaria, definita come la circonferenza centrata nell'origine con raggio pari a 1, riveste un ruolo fondamentale non solo nella geometria analitica e solida, ma soprattutto in trigonometria. Essa rappresenta il punto di partenza per la definizione delle funzioni trigonometriche, fornendo un legame diretto tra coordinate cartesiane e angoli, e costituendo quindi uno strumento indispensabile per lo studio di molteplici fenomeni geometrici e analitici che incontreremo in seguito.
\newpage

\subsectionstar{[33] Similitudini tra Figure Piane}
\paragraph{Similarità tra Figure Piane}
La \textbf{similarità} fra figure piane (in particolare fra triangoli) si basa sull’uguaglianza degli angoli corrispondenti e sulla proporzionalità dei lati. In due triangoli simili, ad esempio, gli angoli sono a due a due congruenti, e i lati opposti a tali angoli risultano in proporzione costante. Questa proprietà è fondamentale per dedurre relazioni metriche senza dover ricorrere a misurazioni dirette, consentendo di risolvere problemi geometrici in modo elegante e di estendere i risultati anche a figure più complesse (poligoni regolari, figure composte, ecc.).

\paragraph{Teoremi di Euclide}
I \textit{Teoremi di Euclide} si riferiscono principalmente alle proprietà dei triangoli rettangoli. In particolare, consideriamo un triangolo rettangolo \(ABC\) con ipotenusa \(BC\) e angolo retto in \(A\). L’altitudine dal vertice retto \(A\) sull’ipotenusa \(BC\) la divide in due segmenti, che indichiamo con \(BD\) e \(DC\), dove \(D\) è il piede dell’altitudine. I teoremi di Euclide stabiliscono che:
\[
\text{(1) } AD^2 = BD \cdot DC,
\quad\quad
\text{(2) } AB^2 = BD \cdot BC,
\quad\quad
\text{(3) } AC^2 = DC \cdot BC.
\]
Nel primo teorema si afferma che l’altitudine \(AD\) è media proporzionale tra i due segmenti in cui essa divide l’ipotenusa. Nel secondo e nel terzo, ciascun cateto risulta media proporzionale tra l’intera ipotenusa e la proiezione di quel cateto su di essa.

\paragraph{Corda di una Circonferenza}
In una circonferenza, la \textbf{corda} è un segmento i cui estremi appartengono alla circonferenza stessa. Se consideriamo un cerchio con centro \(O\) e raggio \(r\), e prendiamo due punti \(A\) e \(B\) sulla circonferenza, il segmento \(AB\) è una corda. Nel disegno, la linea tratteggiata indica la corda:

\[
\begin{tikzpicture}[scale=1.0]
  % Centro O e raggio
  \coordinate (O) at (0,0);
  \draw[thick] (O) circle (2);
  % Punti A e B sulla circonferenza
  \coordinate (A) at ({2*cos(30)},{2*sin(30)});
  \coordinate (B) at ({2*cos(150)},{2*sin(150)});
  % Disegno della corda AB
  \draw[dashed] (A)--(B);
  % Etichette
  \node at (O) [below left] {\(O\)};
  \node[right] at (A) {\(A\)};
  \node[left] at (B) {\(B\)};
\end{tikzpicture}
\]

\noindent La corda non passa necessariamente per il centro (se lo facesse, sarebbe un diametro). La lunghezza di una corda \(AB\) dipende dalla posizione di \(A\) e \(B\) sulla circonferenza.

\paragraph{Secante e Tangente a una Circonferenza: Definizione e Differenze}

Consideriamo la circonferenza con centro nell’origine \(O(0,0)\) e raggio \(r\), descritta dall’equazione
\[
x^2 + y^2 = r^2.
\]
Una \textit{retta} generica nel piano può essere espressa in forma esplicita come
\[
y = m\,x + q,
\]
dove \(m\) è il coefficiente angolare e \(q\) l’ordinata all’origine. Per individuare il tipo di intersezione tra la retta e la circonferenza, si risolve il sistema
\[
\begin{cases}
x^2 + y^2 = r^2,\\
y = m\,x + q.
\end{cases}
\]
Sostituendo \(y=m\,x+q\) nella prima equazione si ottiene
\[
x^2 + (m\,x + q)^2 = r^2,
\]
cioè
\[
x^2 + m^2\,x^2 + 2\,m\,q\,x + q^2 - r^2 = 0,
\]
che si riscrive come
\[
(m^2+1)\,x^2 + 2\,m\,q\,x + (q^2 - r^2) = 0.
\]
Il comportamento della retta rispetto alla circonferenza dipende dal \textit{discriminante} \(\Delta\) di questa equazione di secondo grado in \(x\):
\[
\Delta = \bigl(2\,m\,q\bigr)^2 - 4\,(m^2+1)\,(q^2 - r^2).
\]
Se \(\Delta>0\), la retta interseca la circonferenza in \textit{due punti reali e distinti}, e si parla di \textbf{retta secante}. Se \(\Delta=0\), la retta tocca la circonferenza in \textit{un solo punto} (soluzione unica), definendosi così \textbf{retta tangente}. Se \(\Delta<0\), non esistono soluzioni reali e la retta non incontra la circonferenza (retta \textit{esterna}).

\medskip

\noindent
La \textit{tangente} a una circonferenza è dunque caratterizzata dal caso \(\Delta=0\). In particolare, dalla condizione \(\Delta=0\) si può ricavare la \textit{formula della tangente} in funzione di \(m\) e \(r\). Ad esempio, imponendo \(\Delta=0\) e semplificando, si trova una relazione fra \(m\) e \(q\) (ordinata all’origine) che descrive tutte le tangenti possibili con pendenza \(m\). Questo permette di calcolare la posizione esatta del punto di tangenza sulla circonferenza.

\paragraph{Esempio}
Si consideri la circonferenza con centro nell’origine \(O(0,0)\) e raggio \(r=5\), descritta dall’equazione
\[
x^2 + y^2 = 25.
\]
Analizziamo tre rette orizzontali di equazioni \(y=3\), \(y=5\) e \(y=6\) e vediamo come si comportano rispetto a questa circonferenza.

\[
\begin{cases}
\text{Circonferenza: } x^2 + y^2 = 25,\\
\text{Retta 1 (secante): } y = 3,\\
\text{Retta 2 (tangente): } y = 5,\\
\text{Retta 3 (esterna): } y = 6.
\end{cases}
\]

\noindent
\textbf{Retta 1: \(y=3\).} Sostituendo \(y=3\) nell’equazione del cerchio si ottiene
\[
x^2 + 3^2 = 25 \;\;\Longrightarrow\;\; x^2 + 9 = 25 \;\;\Longrightarrow\;\; x^2=16 \;\;\Longrightarrow\;\; x=\pm4.
\]
I punti di intersezione sono \((4,3)\) e \((-4,3)\). Ciò significa che la retta \(y=3\) incontra la circonferenza in \textit{due punti reali e distinti}, quindi è una \textit{retta secante}.

\smallskip
\noindent
\textbf{Retta 2: \(y=5\).} Sostituendo \(y=5\) nell’equazione del cerchio si ottiene
\[
x^2 + 5^2 = 25 \;\;\Longrightarrow\;\; x^2 + 25 = 25 \;\;\Longrightarrow\;\; x^2=0 \;\;\Longrightarrow\;\; x=0.
\]
Esiste \textit{un solo punto di contatto}, \((0,5)\). La retta \(y=5\) è dunque \textit{tangente} alla circonferenza (caso discriminante \(\Delta=0\)).

\smallskip
\noindent
\textbf{Retta 3: \(y=6\).} Sostituendo \(y=6\) si ha
\[
x^2 + 6^2 = 25 \;\;\Longrightarrow\;\; x^2 + 36 = 25 \;\;\Longrightarrow\;\; x^2=-11,
\]
che non possiede soluzioni reali. La retta \(y=6\) non interseca la circonferenza, per cui è una \textit{retta esterna} (discriminante \(\Delta<0\)).

\newpage

\subsectionstar{[26] La Parabola}
Le parabole sono rappresentate dall'equazione generale
\[
y = Ax^2 + Bx + C,
\]
dove i coefficienti \(A\), \(B\) e \(C\) determinano la forma e la posizione della curva.

\paragraph{Influenza del Coefficiente \(A\)}
Il coefficiente \(A\) incide sulla "apertura" della parabola:
\begin{itemize}
  \item \(\lvert A \rvert\) maggiore comporta una parabola più stretta (più "compatta");
  \item se \(A>0\) la parabola si apre verso l'alto (il vertice è un minimo), mentre se \(A<0\) si apre verso il basso (il vertice è un massimo).
\end{itemize}

\begin{center}
\begin{tikzpicture}[scale=0.8, every node/.style={font=\small}]
  % Asse cartesiani
  \draw[->] (-3,0) -- (3,0) node[right] {\(x\)};
  \draw[->] (0,-3) -- (0,3) node[above] {\(y\)};
  % Parabola con A = 1 (normale)
  \draw[blue, thick, domain=-2:2, samples=100] plot (\x, {(\x)^2});
  \node[blue] at (2.5,4) {\(A=1\)};
  % Parabola con A = 2 (più stretta)
  \draw[red, thick, domain=-1.5:1.5, samples=100] plot (\x, {2*(\x)^2});
  \node[red] at (2.5,5) {\(A=2\)};
\end{tikzpicture}
\end{center}

\paragraph{Influenza dei Coefficienti \(B\) e \(C\)}
I coefficienti \(B\) e \(C\) determinano la traslazione della parabola. Il vertice, punto di minimo se \(A>0\) (o massimo se \(A<0\)), si calcola con:
\[
x_v = -\frac{B}{2A},\quad y_v = C - \frac{B^2}{4A}.
\]
Modificando \(B\) e \(C\) si sposta la posizione del vertice e, di conseguenza, l'intera parabola. Vediamo ora due esempi di parabole e vediamo l'influenza dell'aver cambiato i valori $B$ e $C$:

\begin{center}
\begin{tikzpicture}[scale=0.8, every node/.style={font=\small}]
  % Disegno degli assi cartesiani
  \draw[->] (-4,0) -- (4,0) node[right] {\(x\)};
  \draw[->] (0,-2) -- (0,6) node[above] {\(y\)};
  
  % Parabola base: y = x^2 (linea blu)
  \draw[blue, thick, domain=-2:2, samples=100] plot (\x, {(\x)^2});
  
  % Parabola traslata: y = x^2 - 2x + 2 (linea rossa)
  \draw[red, thick, domain=-1.2:2.5, samples=100] plot (\x, {(\x)^2 - 2*(\x) + 2});
  
  % Evidenzia il vertice della parabola traslata con un punto nero (senza etichetta)
  \fill (1,1) circle (2pt);
\end{tikzpicture}
\end{center}

La linea blu rappresenta la parabola base \(y=x^2\), mentre la linea rossa rappresenta la parabola traslata \(y=x^2-2x+2\). Il punto nero evidenzia il vertice della parabola traslata, che si trova in \(V(1,1)\).

\paragraph{Calcolo del Vertice e Punto di Minimo/Massimo}
Per una parabola \(y = Ax^2+Bx+C\):
\begin{itemize}
  \item Se \(A>0\), il vertice rappresenta il punto di minimo.
  \item Se \(A<0\), il vertice rappresenta il punto di massimo.
\end{itemize}
Il vertice si ottiene con:
\[
x_v = -\frac{B}{2A},\quad y_v = C - \frac{B^2}{4A}.
\]
Ad esempio, per la parabola
\[
y = 2x^2 - 4x + 1,
\]
si calcola:
\[
x_v = -\frac{-4}{2\cdot2}=1,\quad y_v = 1-\frac{(-4)^2}{4\cdot2}=1-\frac{16}{8}=1-2=-1.
\]
Quindi il vertice è \(V(1,-1)\), punto di minimo.

\paragraph{Esempio di Disequazione di Secondo Grado}
Consideriamo la disequazione
\[
2x^2 - 4x + 1 \leq 0.
\]
Poiché \(A=2>0\), la parabola si apre verso l'alto e il vertice \(V(1,-1)\) rappresenta il punto di minimo. Per risolvere la disequazione, prima troviamo le radici dell'equazione
\[
2x^2 - 4x + 1 = 0.
\]
Il discriminante è
\[
\Delta = (-4)^2 - 4\cdot2\cdot1 = 16 - 8 = 8.
\]
Le soluzioni sono:
\[
x = \frac{4 \pm \sqrt{8}}{4} = 1 \pm \frac{\sqrt{2}}{2}.
\]
Pertanto, la disequazione è soddisfatta per:
\[
1 - \frac{\sqrt{2}}{2} \leq x \leq 1 + \frac{\sqrt{2}}{2}.
\]

\paragraph{Grafico della Disequazione}
Il grafico seguente mostra la parabola \(y=2x^2-4x+1\) (in blu) e la retta orizzontale \(y=0\) (in rosso tratteggiata). L'intervallo compreso tra i punti di intersezione rappresenta la soluzione della disequazione.

\begin{center}
\begin{tikzpicture}[scale=1, every node/.style={font=\small}]
  % Assi cartesiani
  \draw[->] (-1,0) -- (3,0) node[right] {\(x\)};
  \draw[->] (0,-3) -- (0,2) node[above] {\(y\)};
  
  % Disegna la parabola y = 2x^2 - 4x + 1
  \draw[blue, thick, domain=-0.5:2.5, samples=100] plot (\x, {2*(\x)^2 - 4*(\x) + 1});
  
  % Evidenzia i punti di intersezione
  \coordinate (P1) at ({1 - sqrt(2)/2},0);
  \coordinate (P2) at ({1 + sqrt(2)/2},0);
  \fill (P1) circle (2pt) node[below left] {\(1-\frac{\sqrt{2}}{2}\)};
  \fill (P2) circle (2pt) node[below right] {\(1+\frac{\sqrt{2}}{2}\)};
  
  % Evidenzia il vertice
  \fill (1,-1) circle (2pt) node[below right] {\(V(1,-1)\)};
  
  % Sfumatura per la regione in cui la disequazione è soddisfatta
  \fill[blue!20, domain={1 - sqrt(2)/2}:{1 + sqrt(2)/2}] 
    plot (\x, {2*(\x)^2 - 4*(\x) + 1}) -- 
    plot (\x, {0}) -- cycle;
\end{tikzpicture}
\end{center}


\subsectionstar{[22] L'Iperbole}
Disegnare l'equazione di un'iperbole sul piano cartesiano significa rappresentare l'insieme di tutte le coppie \((x,y)\) che soddisfano l'equazione data. A differenza della circonferenza, l'iperbole è composta da due rami separati e presenta asintoti, che sono le rette guida verso cui i rami tendono quando \(x\) o \(y\) si avvicinano all'infinito.

\paragraph{Forma Generale e Forma Canonica.}
Un'equazione conica di secondo grado può rappresentare un'iperbole se, tramite il completamento del quadrato, si riesce a riscriverla nella forma canonica. Ad esempio, per un'iperbole con asse trasverso verticale la forma canonica è:
\[
\frac{(y-k)^2}{a^2} - \frac{(x-h)^2}{b^2} = 1.
\]
In questa espressione:
\begin{itemize}
  \item \(C(h,k)\) è il centro dell'iperbole;
  \item \(a\) rappresenta la distanza dal centro ai vertici lungo l'asse verticale (l'asse trasverso);
  \item \(b\) determina la pendenza degli asintoti, che sono le rette date da
    \[
    y-k=\pm\frac{a}{b}(x-h).
    \]
\end{itemize}

\paragraph{Esempio di Conversione in Forma Canonica.}
Consideriamo l'equazione generica:
\[
x^2 - y^2 - 2x + 4y - 1 = 0.
\]
Raggruppiamo i termini relativi a \(x\) e \(y\):
\[
(x^2-2x) - (y^2-4y) - 1 = 0.
\]
Completiamo il quadrato per ciascun gruppo:
\[
x^2-2x = (x-1)^2-1,\quad y^2-4y = (y-2)^2-4.
\]
Sostituendo, otteniamo:
\[
(x-1)^2 - 1 - \big[(y-2)^2-4\big] - 1 = 0,
\]
che semplifica a:
\[
(x-1)^2 - (y-2)^2 + 2 = 0 \quad\Longrightarrow\quad (x-1)^2 - (y-2)^2 = -2.
\]
Moltiplichiamo entrambi i lati per \(-1\):
\[
(y-2)^2 - (x-1)^2 = 2.
\]
Dividendo per 2, si ottiene la forma canonica:
\[
\frac{(y-2)^2}{2} - \frac{(x-1)^2}{2} = 1.
\]
Da qui risulta che il centro è \(C(1,2)\), con \(a^2=2\) e \(b^2=2\); gli asintoti sono dunque:
\[
y-2=\pm (x-1).
\]

\paragraph{Influenza dei Parametri.}
I parametri \(a\) e \(b\) influenzano la forma dell'iperbole:
\begin{itemize}
  \item Aumentando \(a\) (mantenendo \(b\) costante) i rami si allungano maggiormente lungo l'asse trasverso.
  \item Aumentando \(b\) (mantenendo \(a\) costante) gli asintoti diventano meno ripidi, aprendo ulteriormente la curva.
  \item La traslazione del centro \(C(h,k)\) sposta l'intera iperbole nel piano.
\end{itemize}

\paragraph{Figura: Tre Iperboli.}
La figura seguente mostra tre iperboli espresse in forma canonica, ciascuna con centro e parametri differenti, per evidenziare come la variazione dei coefficienti modifichi la forma della curva.

\begin{center}
\begin{tikzpicture}[scale=0.8, every node/.style={font=\small}]
  % Disegno degli assi cartesiani
  \draw[->] (-6,0) -- (6,0) node[right] {\(x\)};
  \draw[->] (0,-6) -- (0,6) node[above] {\(y\)};
  
  %-------------------------
  % Iperbole h1: Iperbole orizzontale con centro in (0,0)
  % Equazione:  \(\frac{x^2}{4} - \frac{y^2}{9} = 1\)
  % Questa iperbole ha rami a destra e a sinistra.
  % Dominio ridotto per ottenere una curva più contenuta.
  %-------------------------
  \draw[blue, thick, domain=2:4, samples=100] 
    plot (\x, {sqrt(9*(\x*\x/4-1))});
  \draw[blue, thick, domain=2:4, samples=100] 
    plot (\x, {-sqrt(9*(\x*\x/4-1))});
  \draw[blue, thick, domain=-4:-2, samples=100] 
    plot (\x, {sqrt(9*(\x*\x/4-1))});
  \draw[blue, thick, domain=-4:-2, samples=100] 
    plot (\x, {-sqrt(9*(\x*\x/4-1))});
  \node[blue] at (3.5,4.5) {\(h_1: \frac{x^2}{4}-\frac{y^2}{9}=1\)};
  
  %-------------------------
  % Iperbole h2: Iperbole verticale con centro in (2,1)
  % Equazione:  \(\frac{(y-1)^2}{2} - \frac{(x-2)^2}{3} = 1\)
  % Questa iperbole ha rami sopra e sotto il centro.
  % Dominio esteso a sinistra per mostrare meglio l'allungamento del ramo.
  %-------------------------
  \begin{scope}[shift={(2,1)}]
    \draw[red, thick, domain=-2:1.5, samples=100]
      plot ({2 + sqrt(3)*(sinh(\x))}, {1 + sqrt(2)*(cosh(\x))});
    \draw[red, thick, domain=-2:1.5, samples=100]
      plot ({2 + sqrt(3)*(sinh(\x))}, {1 - sqrt(2)*(cosh(\x))});
    \node[red] at (3,5) {\(h_2: \frac{(y-1)^2}{2}-\frac{(x-2)^2}{3}=1\)};
  \end{scope}
  
  %-------------------------
  % Iperbole h3: Iperbole orizzontale con centro in (-2,-1)
  % Equazione:  \(\frac{(x+2)^2}{9} - \frac{(y+1)^2}{4} = 1\)
  % Questa iperbole ha rami a destra e a sinistra.
  %-------------------------
  \begin{scope}[shift={(-2,-1)}]
    \draw[green!70!black, thick, domain=3:7, samples=100]
      plot (\x, {sqrt(4*((\x*\x)/9-1))});
    \draw[green!70!black, thick, domain=3:7, samples=100]
      plot (\x, {-sqrt(4*((\x*\x)/9-1))});
    \draw[green!70!black, thick, domain=-7:-3, samples=100]
      plot (\x, {sqrt(4*((\x*\x)/9-1))});
    \draw[green!70!black, thick, domain=-7:-3, samples=100]
      plot (\x, {-sqrt(4*((\x*\x)/9-1))});
    \node[green!70!black] at (-4,-4) {\(h_3: \frac{(x+2)^2}{9}-\frac{(y+1)^2}{4}=1\)};
  \end{scope}
  
\end{tikzpicture}
\end{center}


\begin{itemize}
  \item \textbf{Iperbole Blu (\(h_1\)):} Con equazione \(\frac{x^2}{4}-\frac{y^2}{9}=1\) e centro in \((0,0)\), questa iperbole ha rami orizzontali. Il dominio ridotto (da \(2\) a \(4\) e da \(-4\) a \(-2\)) produce una curva più contenuta, mostrando come i coefficienti influenzino la "stretta" della curva.
  \item \textbf{Iperbole Rossa (\(h_2\)):} Definita da \(\frac{(y-1)^2}{2}-\frac{(x-2)^2}{3}=1\), ha rami verticali e il centro traslato in \((2,1)\). L'estensione maggiore del dominio (da \(-3\) a \(1.5\)) consente di visualizzare chiaramente come il ramo sinistro si allunghi, evidenziando l'effetto dei parametri sull'apertura della curva.

  \item \textbf{Iperbole Verde (\(h_3\)):} Espressa da \(\frac{(x+2)^2}{9}-\frac{(y+1)^2}{4}=1\) e centrata in \((-2,-1)\), presenta rami orizzontali. I parametri utilizzati indicano una maggiore estensione orizzontale, con conseguente allungamento della curva.
\end{itemize}

\subsectionstar{[10] L'Ellisse}
Disegnare l'equazione di un'ellisse sul piano cartesiano significa rappresentare l'insieme di tutte le coppie \((x,y)\) che soddisfano la relazione
\[
\frac{(x-h)^2}{a^2}+\frac{(y-k)^2}{b^2}=1.
\]
In questa equazione il punto \((h,k)\) rappresenta il centro dell'ellisse, \(a\) è la lunghezza del semiasse maggiore e \(b\) quella del semiasse minore. È importante notare che, se \(a=b\), l'ellisse si riduce a un cerchio. Pertanto, l'ellisse può essere vista come una generalizzazione della circonferenza.

\paragraph{Forma Canonica e Confronto con la Circonferenza.}
L'equazione canonica dell'ellisse è:
\[
\frac{(x-h)^2}{a^2}+\frac{(y-k)^2}{b^2}=1.
\]
Nel caso in cui \(a=b=r\), essa diventa:
\[
\frac{(x-h)^2}{r^2}+\frac{(y-k)^2}{r^2}=1 \quad\Longrightarrow\quad (x-h)^2+(y-k)^2=r^2,
\]
cioè l'equazione della circonferenza con centro \((h,k)\) e raggio \(r\). In questo modo, l'ellisse è un caso più generale e flessibile rispetto al cerchio.

\paragraph{Influenza dei Parametri.}
I parametri \(a\), \(b\) e \((h,k)\) influenzano la forma e la posizione dell'ellisse:
\begin{itemize}
  \item \textbf{Semiasse Maggiore \(a\):} Determina l'estensione dell'ellisse lungo l'asse in cui la curva è più allungata.
  \item \textbf{Semiasse Minore \(b\):} Determina l'estensione nella direzione perpendicolare a quella del semiasse maggiore.
  \item \textbf{Centro \((h,k)\):} Trasla l'ellisse nel piano.
\end{itemize}

\paragraph{Esempio di Conversione in Forma Canonica.}
Consideriamo l'equazione generica
\[
4x^2+9y^2-8x+36y+4=0.
\]
Per riportarla nella forma canonica, raggruppiamo e completiamo il quadrato:
\[
4x^2-8x+9y^2+36y=-4.
\]
Dividiamo in termini di \(x\) e \(y\):
\[
4(x^2-2x) + 9(y^2+4y) = -4.
\]
Completiamo il quadrato:
\[
x^2-2x=(x-1)^2-1,\quad y^2+4y=(y+2)^2-4.
\]
Sostituendo:
\[
4[(x-1)^2-1]+9[(y+2)^2-4] = -4,
\]
\[
4(x-1)^2-4+9(y+2)^2-36=-4,
\]
\[
4(x-1)^2+9(y+2)^2=36.
\]
Dividendo entrambi i membri per 36:
\[
\frac{(x-1)^2}{9}+\frac{(y+2)^2}{4}=1.
\]
Questa è la forma canonica dell'ellisse con centro \((1,-2)\), semiasse maggiore \(a=3\) (lungo \(x\)) e semiasse minore \(b=2\) (lungo \(y\)).

\paragraph{Figura: Tre Ellissi.}
La figura seguente mostra tre ellissi espresse in forma canonica, per evidenziare come la variazione dei parametri modifichi la forma della curva.

\begin{center}
\begin{tikzpicture}[scale=0.8, every node/.style={font=\small}]
  % Disegno degli assi cartesiani
  \draw[->] (-8,0) -- (8,0) node[right] {\(x\)};
  \draw[->] (0,-6) -- (0,6) node[above] {\(y\)};
  
  % Ellisse e1: Centro (0,0), a=4, b=3
  \draw[blue, thick] (0,0) ellipse (4 and 3);
  
  % Ellisse e2: Centro (2,1), a=3, b=1.5
  \begin{scope}[shift={(2,1)}]
    \draw[red, thick] (0,0) ellipse (3 and 1.5);
  \end{scope}
  
  % Ellisse e3: Centro (-3,-2), a=2, b=4
  \begin{scope}[shift={(-3,-2)}]
    \draw[green!70!black, thick] (0,0) ellipse (2 and 4);
  \end{scope}
  
\end{tikzpicture}
\end{center}

\paragraph{Commento sulle Ellissi:}
\begin{itemize}
  \item \textbf{Ellisse Blu (\(e_1\)):} Con centro in \((0,0)\), semiasse maggiore \(a=4\) e semiasse minore \(b=3\). La sua equazione è 
  \[
  \frac{x^2}{16}+\frac{y^2}{9}=1.
  \]
  Se \(a\) e \(b\) fossero uguali, l'ellisse diventerebbe un cerchio.
  \item \textbf{Ellisse Rossa (\(e_2\)):} Traslata in \((2,1)\) con \(a=3\) e \(b=1.5\). La sua equazione è 
  \[
  \frac{(x-2)^2}{9}+\frac{(y-1)^2}{2.25}=1.
  \]
  La riduzione del valore di \(b\) rispetto ad \(a\) produce un'ellisse più allungata orizzontalmente.
  \item \textbf{Ellisse Verde (\(e_3\)):} Con centro in \((-3,-2)\), \(a=2\) e \(b=4\). La sua equazione è 
  \[
  \frac{(x+3)^2}{4}+\frac{(y+2)^2}{16}=1.
  \]
  In questo caso, il semiasse maggiore è in direzione verticale, rendendo l'ellisse allungata verticalmente.
\end{itemize}

\paragraph*{Conclusioni.} Le ellissi rappresentano una naturale generalizzazione del cerchio; infatti, quando i due semiasse \(a\) e \(b\) coincidono, l'ellisse si riduce al cerchio. Questo concetto permette di estendere le proprietà del cerchio a una classe più ampia di coniche, offrendo così strumenti fondamentali per l'analisi geometrica e applicazioni in vari rami della matematica.
\newpage




\section{Geometria Solida}
\noindent
Dopo aver esplorato la geometria piana, possiamo estendere i concetti visti finora allo \textbf{spazio tridimensionale}, dando avvio allo studio della \textit{geometria solida}. Qui emergono nuovi elementi: \textbf{piani}, \textbf{rette sghembe}, \textbf{angoli diedri}, \textbf{poliedri} (prismi, piramidi) e \textbf{solidi di rotazione} (cilindri, coni, sfere). Molti risultati e tecniche visti in geometria piana trovano un corrispettivo nello spazio, ma si arricchiscono di ulteriori proprietà e definizioni (ad esempio, il concetto di parallelepipedo come estensione del parallelogramma, o la nozione di sezione piana di un solido).  

Come in geometria piana, è possibile anche un \textit{approccio analitico} alla geometria solida: anziché descrivere i punti con due coordinate \((x,y)\), si utilizzano \textit{tre} coordinate \((x,y,z)\). Con tali strumenti, possiamo definire l’equazione di un piano o di una superficie (come un paraboloide, un ellissoide) e studiarne le intersezioni e le proprietà metriche. Tuttavia, l’analisi che condurremo nel seguito si concentrerà principalmente sull’aspetto \textit{piano} dell’analisi geometrica, rimandando la trattazione sistematica della geometria analitica nello spazio a eventuali approfondimenti futuri.  

Nella geometria solida classica, si affronteranno concetti come:
\begin{itemize}
  \item \textbf{Volumi} e \textbf{aree di superfici} di solidi regolari (prismi, piramidi, cilindri, coni, sfere);
  \item \textbf{Sezioni} di solidi (piani che “tagliano” un solido, producendo figure piane);
  \item \textbf{Relazioni metriche} tra spigoli e diagonali di poliedri (analoghe a quelle tra lati e diagonali in poligoni piani);
  \item \textbf{Posizioni reciproche} di piani e rette (parallele, incidenti, perpendicolari) e \textbf{angoli diedri} (generalizzazione dell’angolo tra due rette).
\end{itemize}
In questo modo, la geometria solida rappresenta la naturale estensione della geometria piana, aggiungendo una dimensione in più, e consentendoci di interpretare e descrivere oggetti tridimensionali in modo sistematico, esattamente come la geometria analitica in due dimensioni permette di studiare curve e figure piane mediante equazioni in \((x,y)\).

\paragraph{Da Due a Tre Dimensioni}
Vedremo diversi modi per passare dalla geometria bidimensionale che abbiaom visto fin'ora a quella tridimensionale. Un modo, uno di quelli più affascianti, è tramite i solidi di rotazione. Questi emergono dal prendere delle figure piane e notando che spazio coprono quando ruotate attorno ad un'asse. Un esempio emblematico è quello della costruzione del toro.

Il toro può essere costruito partendo da una circonferenza nel piano, la quale viene ruotata attorno ad un asse esterno al suo piano (che non interseca la circonferenza stessa). In questo modo, ogni punto della circonferenza descrive una traiettoria circolare nello spazio, dando origine ad una superficie chiusa: appunto il toro. Questo procedimento di rotazione, che trasforma una figura piana in un solido, è un classico esempio di solido di rotazione, e rappresenta un ponte concettuale tra la geometria piana, che abbiamo studiato finora, e la geometria solida. Nel nostro percorso, esploreremo sia i solidi di rotazione, come il toro, sia i poliedri, ampliando così la nostra visione e comprensione delle strutture geometriche in tre dimensioni.

\begin{tabular}{cc}
  % Primo toro: campionamento dei cerchi con intervalli di 10°
  \tdplotsetmaincoords{70}{110}
  \begin{tikzpicture}[tdplot_main_coords]
    \def\R{2}  % Distanza dal centro del toro al centro del tubo
    \def\r{0.8} % Raggio del tubo
    % Il toro è ottenuto tracciando, per vari valori dell'angolo \(\theta\) (che posiziona il cerchio lungo il toro),
    % una sezione circolare ottenuta tracciando i punti della circonferenza con step di 10° (samples=36)
    \foreach \theta in {0,10,...,360} {
      \draw[domain=0:360, samples=36, variable=\phi, blue, smooth]
        plot ({(\R+\r*cos(\phi))*cos(\theta)},
              {(\R+\r*cos(\phi))*sin(\theta)},
              {\r*sin(\phi)});
    }
  \end{tikzpicture}
  &
  % Secondo toro: campionamento dei cerchi con intervalli di 1°
  \tdplotsetmaincoords{50}{30}
  \begin{tikzpicture}[tdplot_main_coords]
    \def\R{2}
    \def\r{0.8}
    % In questo caso, ogni cerchio viene disegnato con una maggiore risoluzione, usando step di 1° (samples=361)
    \foreach \theta in {0,10,...,360} {
      \draw[domain=0:360, samples=36, variable=\phi, blue, smooth]
        plot ({(\R+\r*cos(\phi))*cos(\theta)},
              {(\R+\r*cos(\phi))*sin(\theta)},
              {\r*sin(\phi)});
    }
  \end{tikzpicture}
\end{tabular}

\newpage

\subsectionstar{[1*] Angoloidi}
\noindent
Gli \textbf{angoloidi} rappresentano la naturale estensione dell’angolo piano al caso tridimensionale. In due dimensioni, un angolo è la porzione di piano delimitata da due semirette con la stessa origine. Passando allo spazio a tre dimensioni, l’anguloide è la regione spaziale delimitata da più semirette (o superfici) che partono da un unico vertice \(V\).

\medskip

\paragraph{Angoloide tra Semirette}
Un esempio per visualizzare un angoloide consiste nel considerare quattro semirette che si dipartono da \(V\) e definiscono una sorta di \q{piramide} senza base. Nel disegno seguente, le semirette \(\overline{VA}\), \(\overline{VB}\), \(\overline{VC}\) e \(\overline{VD}\) delimitano la superficie dell’anguloide, mentre l’interno (la porzione di spazio compresa fra queste semirette) ne rappresenta il volume:

\begin{center}
\begin{tikzpicture}[scale=1.0]
  % Disegno degli assi 3D con origine O(0,0,0)
  \draw[->] (0,0,0) -- (4,0,0) node[anchor=north east] {$x$};
  \draw[->] (0,0,0) -- (0,4,0) node[anchor=north west] {$y$};
  \draw[->] (0,0,0) -- (0,0,4) node[anchor=south] {$z$};

  % Definizione del vertice V (angoloide) NON coincidente con l'origine
  % Scegliamo ad esempio V(1,2,1)
  \coordinate (V) at (1,2,1);

  % Definizione dei 4 punti della base (appartengono al piano y=0, come richiesto)
  % In tal modo, la base è una sorta di quadrilatero nel piano y=0.
  \coordinate (A) at (2,0,0);
  \coordinate (B) at (4,0,2);
  \coordinate (C) at (3,0,4);
  \coordinate (D) at (1,0,3);

  % Disegno della base (A-B-C-D) con linee piene
  \draw[dashed] (A)--(B)--(C)--(D)--cycle;

  % Disegno delle semirette (V--A, V--B, V--C, V--D) in linea tratteggiata
  \draw[thick] (V)--(A);
  \draw[thick] (V)--(B);
  \draw[thick] (V)--(C);
  \draw[thick] (V)--(D);

  % Etichette
  \node[left] at (0,0,0) {$O$};
  \node[above] at (V) {$V$};
  \node[below] at (A) {$A$};
  \node[right] at (B) {$B$};
  \node[below] at (C) {$C$};
  \node[left]  at (D) {$D$};
\end{tikzpicture}
\end{center}

\noindent
In questo esempio, l’\textit{anguloide} può essere descritto in diversi modi. In generale, viene spesso comodo consisderare un certo piano, in questo caso il piano delle assi $x, z$ (ossia determnato dall'equazione $y = 0$) e i quattro punti \(A\), \(B\), \(C\), \(D\) che giacciono su tale piano, insieme al vertice \(V\). La regione spaziale compresa tra le semirette \(\overline{VA}\), \(\overline{VB}\), \(\overline{VC}\), \(\overline{VD}\) ed il poligono \(\overline{ABCD}\) (inteso come \q{base}) costituisce l’anguloide; figure di questo tipo sono note come \textit{piramidi} a base quadrilatera. 

\paragraph{Angoloide di Rotazione}
Misurare ora numericamente l'angoloide non è una questione semplice. Per angoloidi semplici come questo, che sono definiti da una piramide a base quadrilatera, sarebbe sufficiente fornire gli angoli che partono in $V$ che definiscono le proiezioni delle quattro semirette. Tuttavia vogliamo trovare un modo untiario di definire un angoloide anche quando la base della piramide ha più lati ed è irregolare o persino quando non si tratta affatto di una piramide ma invece di un cono, come nel caso di quelli che chiamiamo \textit{angoloidi di rotazione}, come nel caso: 

\begin{center}
\begin{tikzpicture}[scale=1.0]
  % Assi 3D
  \draw[->] (0,0,0) -- (4,0,0) node[anchor=north east] {$x$};
  \draw[->] (0,0,0) -- (0,4,0) node[anchor=north west] {$y$};
  \draw[->] (0,0,0) -- (0,0,4) node[anchor=south] {$z$};

  % Vertice del cono
  \coordinate (V) at (2,3,3);

  % Cerchio di base nel piano y=0 (lo approssimiamo con un'ellisse)
  % Centro (2,0,2), raggio in xz plane
  \coordinate (O_base) at (2,0,2);

  % Disegno ellittico della base
  % per x in [0,360], r=1.5 (solo approssimazione)
  \draw[dashed] plot[domain=0:360,samples=60,variable=\t]
       ({2 + 1.5*cos(\t)},{0},{2 + 0.8*sin(\t)});

  % Tracciamo due generatrici del cono con linee tratteggiate (V -> circonferenza)
  % Esempio: prendo due punti sulla base
  \coordinate (A) at (3.5,0,2);
  \coordinate (B) at (0.5,0,2);
  \draw[thick] (V)--(A);
  \draw[thick] (V)--(B);
\end{tikzpicture}
\end{center}

\paragraph{Misurare un Angoloide}
\noindent
Per comprendere come misurare un angolo in due dimensioni, si pensa a quanta porzione di circonferenza esso “copre” partendo da un centro. Se un angolo in un cerchio di 360 gradi ne occupa un quarto (come l’angolo retto di 90 gradi), significa che la sua ampiezza è proprio un quarto del cerchio. Passando allo spazio tridimensionale, l’idea si estende sostituendo la circonferenza con una \textit{superficie sferica}: per misurare l’ampiezza di un \textit{anguloide} con vertice \(V\), si considera una sfera (di raggio 1, detta \textit{sfera unitaria}) centrata in \(V\) e si osserva quale porzione di tale sfera è “coperta” dalle semirette che delimitano l’anguloide.

\medskip

\noindent
Nel caso specifico, si vuole calcolare l’ampiezza dell’anguloide rappresentato nella prima figura, con vertice
\[
V(1,2,1)
\quad\text{e spigoli}\quad
\overline{VA},\;\overline{VB},\;\overline{VC},\;\overline{VD},
\]
dove
\[
A(2,0,0),\quad B(4,0,2),\quad C(3,0,4),\quad D(1,0,3).
\]
Il primo passo consiste nello \textit{spostare} \(V\) all’origine, tramite una traslazione che manda \((1,2,1)\) in \((0,0,0)\). In questo modo, i punti \(A,B,C,D\) diventano
\[
A' = (2,0,0) - (1,2,1) = (1,-2,-1),
\]
\[
B' = (4,0,2) - (1,2,1) = (3,-2,1),
\]
\[
C' = (3,0,4) - (1,2,1) = (2,-2,3),
\]
\[
D' = (1,0,3) - (1,2,1) = (0,-2,2).
\]
Ognuno di questi quattro nuovi punti \(A',B',C',D'\) può essere normalizzato per portarli sulla sfera unitaria centrata nell’origine. Se si indica con \(\|A'\|\) la lunghezza (norma) del segmento \(\overline{OA'}\), la normalizzazione produce
\[
aA = \frac{A'}{\|A'\|},\quad
bB = \frac{B'}{\|B'\|},\quad
cC = \frac{C'}{\|C'\|},\quad
dD = \frac{D'}{\|D'\|}.
\]
I punti \(aA,bB,cC,dD\) si trovano tutti sulla superficie della sfera unitaria. Notiamo che ci stiamo riferendo ad $aA$ come un punto in quanto composto da due cordinate, infatti $$\frac{A'}{\|A'\|} = \frac{(A'_X, A'_Y)}{\|A'\|}:= (\frac{A'_X}{\|A'\|}, \frac{A'_Y}{\|A'\|})$$ Collegandoli sulla sfera si ottiene un quadrilatero sferico, la cui area (espressa in \textit{steradianti}) è la misura dell’anguloide. Per calcolare tale area, si sfrutta il fatto che la somma degli angoli interni di un quadrilatero sferico (indichiamoli con \(\alpha,\beta,\gamma,\delta\)) supera di \(2\pi\) la somma degli angoli di un quadrilatero piano. In particolare, la \textit{formula} per l’area \(S\) del quadrilatero sferico è
\[
S \;=\; \alpha + \beta + \gamma + \delta \;-\; 2\pi.
\]
Gli angoli interni \(\alpha,\beta,\gamma,\delta\) si determinano studiando i \textit{piani} che contengono le coppie di semirette (per esempio, per \(\alpha\) si considerano i piani generati da \(\{aA,bB\}\) e \(\{aA,dD\}\)), calcolando i vettori normali a tali piani e infine usando il \textit{prodotto scalare} per ricavare il coseno dell’angolo tra i due vettori normali. Una volta determinati i quattro angoli sferici, si sommano e si sottrae \(2\pi\). Il risultato numerico (in steradianti) fornisce l’ampiezza dell’anguloide con vertice \(V\) e spigoli \(\overline{VA},\overline{VB},\overline{VC},\overline{VD}\). 

\medskip
\noindent
Questo approccio, pur essendo talvolta laborioso, generalizza la nozione di “arco di circonferenza” che serve a misurare un angolo piano: qui, si tratta invece di “porzione di sfera” che quantifica la misura dell’angolo solido.

\newpage
\subsectionstar{[5* - 6*] Diedri e Piani Perpendicolari}
\paragraph{Diedro}
Un diedro è la parte di spazio compresa fra due piani che si intersecano lungo una retta \(r\). Possiamo immaginarlo come un “angolo solido” con “cerniera” su \(r\). Per misurarlo, si considera un piano ortogonale a \(r\): la sezione di questo piano con i due piani in esame produce due semirette che formano un angolo piano, e l’ampiezza di tale angolo (in gradi o radianti) è la misura del diedro.

\begin{center}
\begin{tikzpicture}[scale=1.2]
  % Disegno degli assi 3D con origine O(0,0,0)
  \draw[->] (0,0,0) -- (4,0,0) node[anchor=north east] {$x$};
  \draw[->] (0,0,0) -- (0,4,0) node[anchor=north west] {$y$};
  \draw[->] (0,0,0) -- (0,0,4) node[anchor=south] {$z$};

  % Piano 1: x=0 (yz-plane). Creiamo un poligono in questo piano:
  % (0,3,3) -> (0,3,-1) -> (0,-1,-1) -> (0,-1,3).
  \fill[blue!20,opacity=0.5]
    (0,3,3) -- (0,3,-1) -- (0,-1,-1) -- (0,-1,3) -- cycle;

  % Piano 2: y=0.5*x. Definiamo un poligono in xz-plane con y=0.5*x:
  % Per x=-1 => y=-0.5, z=-1 => P1
  %            y=-0.5, z=3  => P2
  % Per x= 3 => y=1.5,  z=3 => P3
  %            y=1.5,  z=-1 => P4
  \coordinate (P1) at (-1,-0.5,-1);
  \coordinate (P2) at (-1,-0.5,3);
  \coordinate (P3) at (3,1.5,3);
  \coordinate (P4) at (3,1.5,-1);

  % Riempimento piano 2 in verde
  \fill[green!20,opacity=0.5]
    (P1) -- (P2) -- (P3) -- (P4) -- cycle;

  % Retta di intersezione r: Se x=0 e y=0, rimane z libero => asse z
  % Disegniamo un tratto da z=-1 a z=3
  \draw[thick,red] (0,0,-1) -- (0,0,3) node[above left] {$r$};

  % Etichette dell'origine O
  \node[below left] at (0,0,0) {$O$};
\end{tikzpicture}
\end{center}

\noindent
Nella figura, la retta rossa \(r\) rappresenta il punto d’intersezione delle due semirette che si ottengono tagliando i piani con un piano ortogonale a \(r\). L’insieme dei punti compresi fra i due piani (blu e verde) forma il diedro. Per determinarne l’ampiezza, si riduce tutto a un problema bidimensionale: si osserva la sezione perpendicolare a \(r\), che genera due rette nel piano. Nel nostro esempio, tali rette sono \(x=0\) e \(y=0.5\,x\). Il punto rosso \((0,0)\) è la loro intersezione.

\begin{center}
\begin{tikzpicture}[scale=1.0]
  % Assi cartesiani 2D
  \draw[->] (-1,0) -- (4,0) node[right] {$x$};
  \draw[->] (0,-1) -- (0,3) node[left] {$y$};

  % Linea 1: x=0 (retta verticale)
  \draw[blue, thick] (0,-1) -- (0,2);

  % Linea 2: y=0.5x
  \draw[green, thick] (-1,-0.5) -- (3,1.5);

  % Punto di intersezione r (x=0 => y=0.5*0=0)
  % Quindi r=(0,0)
  \fill[red] (0,0) circle (2pt) node[above right] {$r$};

  % Angolo tra le due rette (indicativo con un arco)
  % Per disegnare un piccolo arco
  \draw[red] (0.4,0) arc (0:atan(0.5):0.4);

  % Etichette delle linee
  \node[left] at (0,2) {\(x=0\)};
  \node[above right] at (3,1.5) {\(y=0.5\,x\)};
\end{tikzpicture}
\end{center}

\noindent
Per calcolare l’angolo tra le due rette si considera la \textit{pendenza} (coefficiente angolare). La retta \(y=0.5\,x\) ha pendenza \(m=0.5\), quindi forma un angolo \(\alpha=\arctan(0.5)\) rispetto all’asse \(x\). La retta \(x=0\) è verticale, dunque corrisponde a un angolo di \(90^\circ\) (o \(\tfrac{\pi}{2}\) radianti) rispetto all’asse \(x\). L’ampiezza \(\theta\) fra le due linee è la differenza:
\[
\theta \;=\;\bigl|\arctan(0.5) - \tfrac{\pi}{2}\bigr|
\;=\;\bigl|0.4636\,-1.5708\bigr|
\;\approx\;1.1072\,\text{radianti}
\;\approx\;63.43^\circ.
\]
Questo valore è la misura del diedro: unendo nuovamente il ragionamento allo spazio tridimensionale, si riconosce che l’angolo fra i due piani è esattamente l’angolo tra le due semirette in cui si è scomposto il problema. Il risultato numerico (\(\approx 63.43^\circ\)) definisce l’ampiezza del diedro senza dover ricorrere a calcoli di prodotto scalare o vettori normali.

\paragraph{Piani Perpendicolari}
\noindent
La \textbf{definizione di un piano} nello spazio tridimensionale si basa su un’equazione lineare in tre variabili, del tipo \(\,a\,x + b\,y + c\,z = d\). I coefficienti \((a,b,c)\) definiscono un vettore perpendicolare al piano, mentre \(d\) determina la posizione del piano rispetto all’origine. Se consideriamo, ad esempio, il piano
\[
\pi_1: \; x + 2y + 3z = 6,
\]
ogni punto \((x,y,z)\) che soddisfa questa relazione appartiene al piano \(\pi_1\). Se poi introduciamo un secondo piano, come
\[
\pi_2: \; 2x - 4y + z = 0,
\]
possiamo chiedere se i due piani siano \textit{perpendicolari}. L’analogia con la geometria piana è che, nel piano, due rette sono perpendicolari quando i loro coefficienti angolari soddisfano una certa condizione (\(m_1\cdot m_2=-1\)). Nello spazio, la stessa idea si traduce nel fatto che i \textit{vettori} \((a,b,c)\) associati ai piani risultino perpendicolari se il \textit{prodotto scalare} è zero: se \(\pi_1\) ha normale \((a_1,b_1,c_1)\) e \(\pi_2\) ha normale \((a_2,b_2,c_2)\), allora \(\,\pi_1\perp \pi_2\) se
\[
a_1 a_2 + b_1 b_2 + c_1 c_2 = 0.
\]
Nel nostro esempio, \(\pi_1\) ha normale \(\,(1,2,3)\) e \(\pi_2\) ha normale \(\,(2,-4,1)\). Il loro prodotto scalare risulta
\[
(1)\cdot(2)\;+\;(2)\cdot(-4)\;+\;(3)\cdot(1)
=\;2\;-\;8\;+\;3
=\;-3,
\]
che non è zero, quindi i due piani non sono perpendicolari. Se al contrario si ottiene un risultato nullo, i piani sarebbero ortogonali. 

Un altro modo per vedere lo stesso concetto, è proprio usando i diedri che abbiamo visto nella pagina precedente. Due piani infatti sono perpendicolari se e solo se il diedro che formano è di $90^\circ$.

\noindent \textbf{Esempio}: Vediamo quindi un caso in cui due piani sono perpendicolari e li riusciamo a dimostrare tali. Consideriamo i piani
\[
\pi_1:\, x+y=0
\quad\text{e}\quad
\pi_2:\, x-y=0.
\]
Ognuno di essi è descrivibile da un’equazione lineare in \((x,y,z)\). Nel primo caso, \(x+y=0\) equivale a \(x+y+0\cdot z=0\), e dunque un \textit{vettore normale} al piano è \((1,1,0)\). Nel secondo caso, \(x-y=0\) equivale a \(x - y +0\cdot z=0\), con vettore normale \((1,-1,0)\).  

\smallskip
\noindent
Due piani si dicono \textit{perpendicolari} se e solo se i rispettivi vettori normali sono \textit{ortogonali}, cioè il loro prodotto scalare è zero. Nel nostro esempio, il prodotto scalare tra \((1,1,0)\) e \((1,-1,0)\) risulta
\[
1\cdot1 \;+\; 1\cdot(-1) \;+\; 0\cdot0 \;=\; 1 - 1 + 0 \;=\; 0,
\]
per cui i due piani sono \textit{perpendicolari}. Se si volesse misurare l’angolo tra di essi in modo “geometrico”, si potrebbe tagliare lo spazio con un piano ortogonale alla retta di intersezione (che in questo caso è l’asse \(z\)), ottenendo due semirette nel piano di sezione, formanti un angolo retto. In termini algebrici, il risultato del prodotto scalare fornisce direttamente la conferma dell’ortogonalità dei piani. 


\newpage

\subsectionstar{[6*] Rette Sghembe}
\noindent
Nel piano bidimensionale, due rette possono presentarsi in \textbf{tre} modi diversi:
\begin{itemize}
  \item \textbf{Coincidenti}: se le loro equazioni sono essenzialmente la stessa (una è multiplo dell’altra), ogni punto di una appartiene anche all’altra, e il sistema lineare corrispondente possiede \textit{soluzioni infinite}.
  \item \textbf{Parallele}: se hanno lo stesso coefficiente angolare (stessa pendenza) ma termini costanti diversi, non si incontrano mai; il sistema lineare corrispondente non ha \textit{alcuna soluzione}.
  \item \textbf{Incidenti in un solo punto}: se non sono parallele né coincidenti, si intersecano esattamente in un unico punto; il sistema lineare associato ammette \textit{una sola soluzione}.
\end{itemize}

\noindent
Questa corrispondenza tra la geometria delle rette e l’algebra dei sistemi di primo grado in due variabili mostra come:
\begin{itemize}
  \item Rette \textit{coincidenti} \(\longleftrightarrow\) sistema con \textit{infinite soluzioni};
  \item Rette \textit{parallele} \(\longleftrightarrow\) sistema \textit{impossibile} (nessuna soluzione);
  \item Rette \textit{incidenti} \(\longleftrightarrow\) sistema con \textit{unica soluzione}.
\end{itemize}

\noindent
\begin{center}
\begin{tikzpicture}[scale=0.8]
  % Assi cartesiani
  \draw[->] (-1,0) -- (5,0) node[right] {$x$};
  \draw[->] (0,-2.5) -- (0,4.5) node[left] {$y$};

  % Retta r1: y = x - 1
  % Se x=-1 => y=-2, se x=4 => y=3
  \draw[thick] (-1,-2) -- (4,3) node[pos=0.8,above] {\small $r_1$};

  % Retta r2: y = x + 2 (parallela a r1, intercetto diverso)
  % Se x=-1 => y=1, se x=4 => y=6
  \draw[thick] (-1,1) -- (4,6) node[pos=0.5,above] {\small $r_2$};

  % Retta r3: y = -2x + 2 (inclinazione diversa, NON perpendicolare)
  % Se x=-1 => y=4, se x=4 => y=-6
  \draw[thick] (-1,4) -- (3,-4) node[pos=0.5,above left] {\small $r_3$};
\end{tikzpicture}
\end{center}

\noindent
Le tre rette rappresentate nel disegno sono:
\[
r_1:\, y = x - 1, \quad
r_2:\, y = x + 2, \quad
r_3:\, y = -2x + 2.
\]
Dal punto di vista algebrico, queste rette si traducono in tre \textit{equazioni lineari} in due variabili \((x,y)\). Possiamo quindi costruire \textit{tre diversi sistemi} di equazioni, ciascuno con un esito differente (nessuna soluzione, infinite soluzioni, un’unica soluzione).

\medskip
\noindent
Consideriamo tre diversi sistemi di equazioni lineari in due variabili, che illustrano i tre possibili casi di due rette nel piano:

\[
\text{(a)}\quad
\begin{cases}
y - x = -1,\\
y - x = 2,
\end{cases}
\qquad
\text{(b)}\quad
\begin{cases}
y - x = -1,\\
2y - 2x = -2,
\end{cases}
\qquad
\text{(c)}\quad
\begin{cases}
y - x = -1,\\
y + 2x = 2.
\end{cases}
\]

Nel sistema (a), le due equazioni hanno la stessa forma \(y - x = \text{costante}\) ma costanti diverse (\(-1\) e \(2\)): le rette sono \textit{parallele} e non si incontrano mai, perciò non esiste alcuna coppia \((x,y)\) che risolva entrambe (nessuna soluzione). Nel sistema (b), la seconda equazione ripete la prima, per cui entrambe descrivono la stessa retta, con \textit{infinite soluzioni}. Nel sistema (c), le due rette (\(y=x-1\) e \(y=-2x+2\)) hanno pendenze diverse e si intersecano in un unico punto. Risolvendo
\[
x - 1 = -2x + 2 \;\;\Longrightarrow\;\; 3x=3 \;\;\Longrightarrow\;\; x=1,\quad y=0,
\]
si ottiene un’unica soluzione. In sintesi, i tre casi corrispondono a \textit{rette parallele} (nessuna soluzione), \textit{rette coincidenti} (infinite soluzioni) e \textit{rette incidenti} (una sola soluzione). 
\paragraph{Rette Sghembe}
\noindent
In \(\mathbb{R}^3\), una \textit{retta} può essere descritta come \textit{intersezione di due piani}, ciascuno rappresentato da un’equazione lineare in tre variabili. Ad esempio, la retta \(\ell_1\) si ottiene risolvendo contemporaneamente
\[
\begin{cases}
x - 2y \;=\; 1,\\
y - z \;=\; 2,
\end{cases}
\]
mentre la retta \(\ell_2\) è definita dal sistema
\[
\begin{cases}
x - y + 2z \;=\; 2,\\
2x + y - 3z \;=\; 1.
\end{cases}
\]
Ciascuno di questi insiemi di due equazioni individua un’unica retta, poiché ogni singolo piano è descritto da un’equazione lineare a tre incognite.

\smallskip
\noindent
Se \(\ell_1\) e \(\ell_2\) avessero punti in comune, esisterebbero valori \((x,y,z)\) che soddisfano entrambe le coppie di equazioni. In altre parole, dovremmo risolvere l’insieme
\[
\begin{cases}
x - 2y \;=\; 1,\\
y - z \;=\; 2,\\
x - y + 2z \;=\; 2,\\
2x + y - 3z \;=\; 1.
\end{cases}
\]
Questo sistema di \textit{quattro} equazioni lineari in tre variabili, se privo di soluzioni, conferma che \(\ell_1\) e \(\ell_2\) non condividono alcun punto. Inoltre, per verificare che non siano parallele, si osserva che non esiste un semplice “fattore di proporzionalità” che renda le prime due equazioni multipli delle ultime due; altrimenti, i piani di \(\ell_1\) risulterebbero gli stessi (o multipli) di quelli di \(\ell_2\), producendo una retta parallela o coincidente.

\smallskip
\noindent
In questo modo, si dimostra che \(\ell_1\) e \(\ell_2\) \textit{non} sono parallele (poiché le rispettive coppie di piani non si riducono a semplici multipli) e, allo stesso tempo, il sistema complessivo non possiede soluzioni, quindi non esiste alcun punto in comune. Ne segue che le due rette sono \textbf{sghembe}: non coincidono, non sono parallele e non si intersecano.

È importante quindi notare che le rette possono dirsi \textit{sghembe} solo in tre dimensioni, è quindi un quarto caso che diventa possibile ma che non lo era quando esaminavamo le rette in due dimensioni.

Anticipiamo in fine che i piani, nelle tre dimensioni sono a loro volta, coincidenti, incidenti (su una retta) o paralleli. Con un ragionamento analogo al precedente, potremmo quindi indovinare che, in quattro dimensioni, anche i piani potranno essere sghembi. Questo tuttavia eccede lo scopo di queste note, passeremo ora ad altri elementi di geometria solida.

Rimanendo in tre dimensioni, vedremo nella prossima sezione come rette e piani possono essere disposti in tre dimensioni.
\newpage

\subsectionstar{[34* - 35*] Rette e Piani Perpendicolari e Paralleli}
\noindent
Nel piano algebrico, i piani paralleli si riconoscono dal fatto che condividono lo stesso vettore normale ma presentano costanti differenti nelle loro equazioni. Ad esempio, se consideriamo:
\[
\pi_1: \; x + 2y + 3z = 4
\quad\text{e}\quad
\pi_2: \; x + 2y + 3z = 8,
\]
vediamo che entrambi hanno la “parte sinistra” identica \((x + 2y + 3z)\), quindi lo stesso normale \((1,2,3)\), ma la parte destra cambia (\(4\) e \(8\)). Questo implica che i piani non si intersecano mai e non possiedono alcun punto in comune, poiché non esiste \((x,y,z)\) che possa soddisfare contemporaneamente \((x+2y+3z=4)\) e \((x+2y+3z=8)\).  

\begin{center}
\begin{tikzpicture}[scale=1.0]
  \draw[->] (0,0,0) -- (4,0,0) node[anchor=north east] {$x$};
  \draw[->] (0,0,0) -- (0,4,0) node[anchor=north west] {$y$};
  \draw[->] (0,0,0) -- (0,0,4) node[anchor=south] {$z$};

  \coordinate (A1) at (4,0,0);    % Esempio di punto su pi1
  \coordinate (B1) at (0,2,0);    % x+2y+3z=4 => 0+2*2+0=4
  \coordinate (C1) at (1,0,1);    % 1+0+3*1=4

  \fill[blue!20,opacity=0.5] (A1)--(B1)--(C1)--cycle;

  \coordinate (A2) at (8,0,0);    % x+2y+3z=8 => 8+0+0=8
  \coordinate (B2) at (0,4,0);    % 0+2*4+0=8
  \coordinate (C2) at (2,0,2);    % 2+0+3*2=2+6=8

  \fill[green!20,opacity=0.5] (A2)--(B2)--(C2)--cycle;

  \node[left] at (0,0,0) {$O$};
  \node[blue] at (2,1,0.5) {$\pi_1$};
  \node[green] at (3,2,1.5) {$\pi_2$};
\end{tikzpicture}
\end{center}


\noindent
La parte in blu rappresenta una porzione di \(\pi_1\), mentre quella in verde corrisponde a \(\pi_2\). Poiché le due equazioni lineari differiscono solo per il termine costante, i due piani non si incontrano mai e risultano paralleli, confermando anche in senso geometrico che non esiste soluzione comune al sistema
\[
\begin{cases}
x+2y+3z=4,\\
x+2y+3z=8.
\end{cases}
\]
Sottraendo la prima equazione dalla seconda si ottiene \(0=4\), una contraddizione. Di conseguenza, non esiste alcun punto \((x,y,z)\) che soddisfi simultaneamente entrambe le equazioni. Sul piano geometrico, ci troviamo di fronte a due \textit{piani paralleli} che non si incontrano mai.

\medskip
\noindent
In generale, dati due piani nello spazio, descritti da:
\[
\pi_1:\; a_1 x + b_1 y + c_1 z = d_1,
\quad
\pi_2:\; a_2 x + b_2 y + c_2 z = d_2,
\]
possono verificarsi tre situazioni:

\begin{itemize}
    \item \textbf{Coincidenti:} se \((a_2,b_2,c_2)\) risulta multiplo di \((a_1,b_1,c_1)\) e anche i termini noti \(d_1\) e \(d_2\) rispettano lo stesso fattore di proporzionalità, i due piani descrivono la \textit{stessa} superficie. In tal caso, l’insieme di punti comuni è l’intero piano (soluzioni infinite).

    \item \textbf{Paralleli:} se \((a_2,b_2,c_2)\) è multiplo di \((a_1,b_1,c_1)\) ma \(d_1\) e \(d_2\) non lo sono nello stesso rapporto, i piani non si incontrano

    \item \textbf{Incidenti in una retta:} se i vettori normali \((a_1,b_1,c_1)\) e \((a_2,b_2,c_2)\) non sono multipli l’uno dell’altro, i due piani si \textit{tagliano} in una \textit{retta} comune. Ogni punto su tale retta soddisfa entrambe le equazioni, generando un insieme di soluzioni \textit{infinito} ma unidimensionale (l’intera linea d’intersezione). In tal modo, l’intersezione di due piani non paralleli (e non coincidenti) in \(\mathbb{R}^3\) risulta sempre una retta.  
\end{itemize}

Abbiamo visto approfonditamente il caso in cui sono paralleli ed è semplice comprendere il caso in cui i piani sono coincidenti. Focalizziamoci quindi ora sul terzo ed ultimo caso, per farlo vediamo un esempio di due piani incidenti e calcoliamo la retta di incisione. Teniamo a mente che i piani perpendicolari sono un caso particolare di piani incidenti.

\noindent
Consideriamo i piani
\[
\pi_1:\; x + 2y + 3z = 6,
\quad
\pi_2:\; 2x - y + z = 4.
\]
Per determinare la retta di intersezione, risolviamo il sistema:
\[
\begin{cases}
x + 2y + 3z = 6,\\
2x - y + z = 4.
\end{cases}
\]
Dalla seconda equazione, ad esempio, ricaviamo \(x\) in funzione di \(y\) e \(z\). Scrivendo \(2x = 4 + y - z\), si ottiene
\[
x = 2 + \tfrac{1}{2}y - \tfrac{1}{2}z.
\]
Sostituiamo questa espressione in \(\pi_1\):
\[
\bigl(2 + \tfrac12 y - \tfrac12 z\bigr) + 2y + 3z = 6.
\]
Raggruppando i termini:
\[
2 + \tfrac12 y + 2y - \tfrac12 z + 3z = 6,
\]
\[
2 + \tfrac52 y + \tfrac52 z = 6,
\]
\[
\tfrac52 y + \tfrac52 z = 4,
\]
\[
y + z = \tfrac{8}{5}.
\]
Ora, scegliamo come \textit{parametro} una delle variabili, ad esempio \(z = t\). Allora \(y = \tfrac{8}{5} - t\). Infine, rimpiazziamo \(y\) e \(z\) in \(x = 2 + \tfrac12 y - \tfrac12 z\):
\[
x = 2 + \tfrac12\bigl(\tfrac{8}{5} - t\bigr) - \tfrac12 t
  = 2 + \tfrac{4}{5} - \tfrac12 t - \tfrac12 t
  = \tfrac{14}{5} - t.
\]
Riassumendo, la retta d’intersezione \(\ell\) si può parametrizzare in funzione di \(t\) come:
\[
\ell:\quad
\begin{cases}
x = \tfrac{14}{5} - t,\\
y = \tfrac{8}{5} - t,\\
z = t.
\end{cases}
\]
In forma vettoriale, possiamo anche scriverla come
\[
(x,y,z)
= \Bigl(\tfrac{14}{5},\;\tfrac{8}{5},\;0\Bigr)
\;+\;
t\,\bigl(-1,\,-1,\;1\bigr),
\]
dove \(t\in\mathbb{R}\). Questa retta rappresenta l’insieme di tutti i punti \((x,y,z)\) che soddisfano simultaneamente le equazioni di \(\pi_1\) e \(\pi_2\). Essendo non paralleli (i loro vettori normali non sono multipli), i due piani si \textit{incontrano} precisamente in \textit{questa} retta. 
\newpage 

\subsectionstar{[33*] Proiezioni di Rette}
\noindent
Quando si vuole \textit{proiettare ortogonalmente} una retta \(\ell\) su un piano \(\pi\), si procede “abbassando” (o “alzando”, a seconda del verso) ogni punto della retta in direzione \textit{perpendicolare} al piano. Se \(\ell\) è data in forma parametrica,
\[
\ell:\;\bigl(x,y,z\bigr)=\bigl(x_0,y_0,z_0\bigr)+t\,(u,v,w),
\]
allora il segmento di proiezione di un punto \(\bigl(x_0+tu,\;y_0+tv,\;z_0+tw\bigr)\) è la retta ortogonale a \(\pi\) passante per tale punto. Intersecando tale retta con il piano \(\pi\), si ottiene il punto proiettato. Se il piano, ad esempio, è \(\{z=0\}\), ogni proiezione ortogonale “annulla” la coordinata \(z\). In modo simile, se il piano ha equazione \(\alpha x + \beta y + \gamma z = d\), si risolve un piccolo sistema per trovare il valore di \(t\) che “porta” il punto su \(\pi\) con un vettore \textit{perpendicolare} a \(\pi\).

\smallskip
\noindent
\textbf{Esempio:}  
Sia il piano \(\pi:\,z=0\) (piano orizzontale) e la retta
\[
\ell:\;\begin{cases}
x=1+2t,\\
y=2+t,\\
z=3-4t,
\end{cases}
\]
dove \(t\in\mathbb{R}\). Proiettando ortogonalmente ogni punto \(\bigl(1+2t,\;2+t,\;3-4t\bigr)\) su \(\pi\), si “elimina” la componente \(z\). Di conseguenza, il punto proiettato risulta \(\bigl(1+2t,\;2+t,\;0\bigr)\). La collezione di tutti questi punti, al variare di \(t\), forma una retta nel piano \(\{z=0\}\). Se la direzione \((u,v,w)\) della retta \(\ell\) fosse parallela all’asse \(z\), l’intera retta si proietterebbe in un \textit{punto} singolo (quello corrispondente a \(x=x_0,y=y_0\) in \(\pi\)).

\smallskip
\noindent
Nella figura seguente, si rappresenta un piano \(\pi\) come un rettangolo, mentre i punti \(P\) e \(Q\) appartengono a una retta \(\ell\) sopra di esso. Le semirette di proiezione (in questo esempio, linee verticali o comunque perpendicolari a \(\pi\)) collegano i punti originali \(P\) e \(Q\) ai corrispondenti punti proiettati \(P'\) e \(Q'\) nel piano.

\begin{center}
\begin{tikzpicture}[scale=1.0]
  % Piano pi
  \draw[thick] (0,0) rectangle (4,2);

  % Due punti P e Q "sopra" il piano
  \coordinate (P) at (1,3); % fittizio
  \coordinate (Q) at (3,4.5); % fittizio
  \fill[blue] (P) circle(1.5pt) node[left] {\small $P$};
  \fill[blue] (Q) circle(1.5pt) node[right] {\small $Q$};
  \draw[blue,thick] (P)--(Q) node[midway,above] {\small $\ell$};

  % Proiezioni P' e Q' sul piano (in rosso)
  % Le disegniamo con coordinate "schiacciate" verticalmente
  \coordinate (Pp) at (1,1);
  \coordinate (Qp) at (3,1.8);
  \fill[red] (Pp) circle(1.5pt) node[below] {\small $P'$};
  \fill[red] (Qp) circle(1.5pt) node[below] {\small $Q'$};

  % Segmenti verticali di proiezione (ortogonali al piano)
  \draw[dashed,red] (P)--(Pp);
  \draw[dashed,red] (Q)--(Qp);

\end{tikzpicture}
\end{center}

\noindent
Qui, la retta \(\ell\) (in blu) è sopra il piano \(\pi\). La proiezione ortogonale “abbassa” \(P\) a \(P'\) e \(Q\) a \(Q'\) in direzione perpendicolare a \(\pi\). Collegando tutti i punti proiettati, si ottiene la retta \(\ell'\subset\pi\) che è l’immagine ortogonale di \(\ell\). A seconda della posizione di \(\ell\) rispetto a \(\pi\), questa immagine può essere una retta o un punto, se \(\ell\) è perpendicolare a \(\pi\). Abbiamo visto che il caso in cui consideriamo il piano $z = 0$ è algebraicamente molto semplice, vediamone ora come procedere uno con un piano ed una retta arbitrari.

\noindent
Per determinare la proiezione ortogonale di una retta su un piano in \(\mathbb{R}^3\), si parte dalla descrizione della retta e del piano. La retta può essere espressa in forma parametrica, per esempio
\[
(x,y,z) \;=\; (x_0,\,y_0,\,z_0) \;+\; t\,(u,\,v,\,w),
\]
dove \((x_0,y_0,z_0)\) è un punto iniziale e \((u,v,w)\) il vettore direzione, mentre il piano ha equazione lineare
\[
\alpha\,x \;+\; \beta\,y \;+\; \gamma\,z \;=\; d,
\]
il cui vettore normale è \((\alpha,\beta,\gamma)\). Per proiettare ortogonalmente la retta sul piano, si prende un generico punto \(\,(x_0+tu,\,y_0+tv,\,z_0+tw)\) della retta e lo si sposta lungo la direzione normale \(\,(\alpha,\beta,\gamma)\) fino a raggiungere il piano. Ciò si formalizza introducendo un parametro \(\lambda\) che indica “quanto” ci si muove in direzione normale, e si scrive
\[
(x',\,y',\,z') 
\;=\;
\bigl(x_0 + tu,\;y_0 + tv,\;z_0 + tw\bigr)
\;+\;
\lambda\,(\alpha,\,\beta,\,\gamma).
\]
Il punto \(\,(x',y',z')\) deve soddisfare l’equazione del piano, quindi si impone
\[
\alpha\,x' \;+\; \beta\,y' \;+\; \gamma\,z' \;=\; d.
\]
Sostituendo \(\,(x',y',z')\) si ottiene un’equazione in \(\,t\) e \(\lambda\). Risolvendola rispetto a \(\lambda\), si esprime \(\lambda\) come funzione di \(\,t\). A quel punto, si rimpiazza \(\lambda\) nella formula di \(\,(x',y',z')\), in modo da ottenere le coordinate di ogni punto proiettato sul piano in funzione del parametro \(\,t\). Il risultato è un’ulteriore \textit{retta} nel piano (a meno di casi speciali), poiché per ogni \(t\) esiste un solo valore di \(\lambda\) che porta il punto \(\,(x_0+tu,y_0+tv,z_0+tw)\) sul piano in direzione normale. La collezione di tali punti \(\,(x',y',z')\) forma l’immagine ortogonale della retta sul piano. 


\noindent
Per illustrare in modo semplice la procedura, consideriamo la retta
\[
\ell:\;\begin{cases}
x=2 + t,\\
y=1 + 2t,\\
z=3 - t,
\end{cases}
\quad t\in\mathbb{R},
\]
e il piano
\[
\pi:\; x + y + z = 6.
\]
Il vettore normale di \(\pi\) è \((1,1,1)\). Per proiettare ortogonalmente un punto \(\bigl(2+t,\;1+2t,\;3-t\bigr)\) della retta su \(\pi\), ci spostiamo di un tratto \(\lambda\) lungo la direzione \(\,(1,1,1)\) fino a raggiungere il piano. Definiamo dunque
\[
(x',\,y',\,z')
\;=\;
\bigl(2 + t,\;1 + 2t,\;3 - t\bigr)
\;+\;
\lambda\,(1,\,1,\,1).
\]
Questo punto deve soddisfare l’equazione \(\,x' + y' + z' = 6\). Sostituiamo:

\[
(2 + t + \lambda)
\;+\;
(1 + 2t + \lambda)
\;+\;
(3 - t + \lambda)
\;=\;
6.
\]
Sommando i termini:
\[
(2 + t) + (1 + 2t) + (3 - t) \;+\; \lambda + \lambda + \lambda \;=\; 6.
\]
\[
(2 + 1 + 3) \;+\; (t + 2t - t) \;+\; 3\lambda \;=\; 6.
\]
\[
6 + 2t + 3\lambda \;=\; 6.
\]
\[
2t + 3\lambda = 0
\quad\Longrightarrow\quad
3\lambda = -2t
\quad\Longrightarrow\quad
\lambda = -\tfrac{2t}{3}.
\]
Rimpiazzando \(\lambda\) in \(\,(x',y',z')\):

\[
x' = (2 + t) + \bigl(-\tfrac{2t}{3}\bigr),
\quad
y' = (1 + 2t) + \bigl(-\tfrac{2t}{3}\bigr),
\quad
z' = (3 - t) + \bigl(-\tfrac{2t}{3}\bigr).
\]
Semplificando, si ottengono le coordinate di ogni punto proiettato in funzione di \(t\). Ad esempio:
\[
x' = 2 + t - \tfrac{2t}{3}
= 2 + \tfrac13\,t,
\quad
y' = 1 + 2t - \tfrac{2t}{3}
= 1 + \tfrac{4t}{3},
\quad
z' = 3 - t - \tfrac{2t}{3}
= 3 - \tfrac{5t}{3}.
\]
Variando \(t\) sull’intera retta \(\ell\), i punti \(\,(x',y',z')\) tracciano la \textit{retta proiettata} di \(\ell\) sul piano \(\pi\). Abbiamo quindi eseguito la \textbf{proiezione ortogonale} di ogni punto di \(\ell\) nella direzione \(\,(1,1,1)\) (normale a \(\pi\)), trovando in modo esplicito l’immagine geometrica della retta su \(\pi\). 
\newpage

\subsectionstar{[29*] Poliedri, Prismi e Piramidi}
\paragraph{Poliedri} Un \textit{poliedro} è un solido geometrico tridimensionale delimitato da un numero finito di \textit{poligoni}, detti \textit{facce}. Queste facce si incontrano lungo segmenti detti \textit{spigoli}, i quali, a loro volta, si congiungono in \textit{vertici}. Esempi di poliedri sono il cubo, il parallelepipedo, la piramide e il prisma. Nello studio dei poliedri si analizzano aspetti quali il numero di facce, spigoli e vertici, l’angolo diedro fra le facce e le loro proiezioni in due dimensioni.

\noindent
Un \textit{poliedro regolare} è un solido tridimensionale le cui \textit{facce} sono \textbf{poligoni regolari} e i cui \textit{vertici} presentano tutti la stessa disposizione angolare (in altre parole, ogni faccia ha la stessa forma e dimensione, e l’angolo solido in ogni vertice è identico). Gli unici poliedri regolari sono i \textit{poliedri platonici}: tetraedro, cubo, ottaedro, dodecaedro e icosaedro. Un \textit{poliedro irregolare}, invece, è un solido i cui poligoni di faccia non sono tutti congruenti e/o la cui struttura angolare nei vertici non è omogenea.

\noindent Il \textit{cubo} (o esaedro regolare) è un tipico esempio di poliedro regolare: tutte le sue facce sono \textit{quadrati} congruenti, e in ogni vertice si incontrano tre spigoli di uguale lunghezza, formando sempre lo stesso angolo diedro. Al contrario, un parallelepipedo generico, pur avendo 6 facce quadrangolari, non è regolare perché le facce non sono tutte \textit{congruenti} e gli angoli possono differire da \(90^\circ\). 

\begin{center}
\begin{tikzpicture}[scale=1.0]
  % Disegno di un cubo come esempio di poliedro
  \coordinate (A) at (0,0);
  \coordinate (B) at (2,0);
  \coordinate (C) at (2,2);
  \coordinate (D) at (0,2);
  % Secondo quadrato spostato
  \coordinate (E) at (0.5,1.0);
  \coordinate (F) at (2.5,1.0);
  \coordinate (G) at (2.5,3.0);
  \coordinate (H) at (0.5,3.0);

  % Faccia inferiore
  \draw[thick] (A)--(B)--(C)--(D)--cycle;
  % Faccia superiore

  \draw[thick] (F)--(G);
  \draw[thick] (G)--(H);
  \draw[dashed] (H)--(E);
  \draw[dashed] (E)--(F);
  % Spigoli verticali
  \draw[dashed] (A)--(E);
  \draw[thick] (B)--(F);
  \draw[thick] (C)--(G);
  \draw[thick] (D)--(H);
\end{tikzpicture}
\end{center}

\paragraph{Formula di Eulero}
La \textit{formula di Eulero} fornisce un’elegante relazione tra il numero di vertici (\(V\)), spigoli (\(S\)) e facce (\(F\)) di un poliedro convesso. Essa afferma che:
\[
V \;-\; S \;+\; F \;=\; 2.
\]
Ad esempio, per un cubo (poliedro con 8 vertici, 12 spigoli e 6 facce) si verifica:
\[
8 \;-\; 12 \;+\; 6 \;=\; 2.
\]

\paragraph{Prisma} Un \textit{prisma} è un poliedro caratterizzato da due \textit{basi} congruenti e parallele, solitamente poligonali, unite da un insieme di \textit{facce laterali} a forma di parallelogramma. In termini più specifici, se il poligono di base ha \(n\) lati, allora il prisma risulta avere \(n+2\) facce totali (le due basi e le \(n\) facce laterali). Se gli spigoli laterali sono \textit{perpendicolari} alle basi, si parla di \textit{prisma retto}; in caso contrario, il prisma è obliquo. Esempi comuni sono il \textit{prisma triangolare}, con basi triangolari e tre facce laterali rettangolari, e il \textit{prisma quadrangolare} (o parallelepipedo) con basi quadrangolari. 
\[
\tdplotsetmaincoords{60}{40}
\begin{tikzpicture}[scale=1.4]
  % Definiamo i vertici del triangolo di base (z=0)
  % A(0,0,0), B(2,0,0), C(1,1.5,0)
  \coordinate (A) at (0,0,0);
  \coordinate (B) at (2,0,0);
  \coordinate (C) at (1,1.5,0);

  % Definiamo i vertici del triangolo superiore (z=2)
  % A'(0,0,2), B'(2,0,2), C'(1,1.5,2)
  \coordinate (Au) at (0,0,2);
  \coordinate (Bu) at (2,0,2);
  \coordinate (Cu) at (1,1.5,2);

  % Disegno del triangolo di base
  \draw[dashed] (A) -- (B);
  \draw[thick] (B) -- (C);
  \draw[dashed] (C) -- (A);

  % Disegno del triangolo superiore
  \draw[thick] (Au) -- (Bu) -- (Cu) -- cycle;

  % Collegamenti verticali (spigoli laterali)
  \draw[dashed] (A) -- (Au);
  \draw[thick] (B) -- (Bu);
  \draw[thick] (C) -- (Cu);
\end{tikzpicture}
\]

\paragraph{Area e Volume di un Prisma}
Per \textit{calcolare il volume} di un prisma, si utilizza la formula
\[
\text{Volume} \;=\; \text{Area di base} \times \text{Altezza},
\]
dove l’“area di base” si riferisce a quella del poligono che costituisce una delle due facce parallele (spesso detta “base”), mentre l’altezza è la distanza ortogonale tra i due piani contenenti le basi. L’\textit{area laterale} si ottiene moltiplicando il perimetro della base per l’altezza (se il prisma è retto, le facce laterali sono rettangoli), mentre l’\textit{area totale} è la somma dell’area laterale e di due volte l’area di base.

\smallskip
\noindent
\textbf{Esempio:} Consideriamo un \textit{prisma triangolare retto} la cui base è un triangolo di lati 3, 4 e 5 (quindi un triangolo rettangolo) e l’altezza del prisma (cioè la distanza tra le due basi parallele) è \(6\). L’area della base si calcola con la formula di Erone (o riconoscendo che 3,4,5 è un triangolo rettangolo di cateti 3 e 4):
\[
\text{Area}_{\text{base}} = \tfrac12 \times 3 \times 4 = 6.
\]
Il \textit{volume} del prisma risulta dunque
\[
V \;=\; 6 \times 6 \;=\; 36.
\]
Per l’\textit{area laterale}, notiamo che il \textit{perimetro} del triangolo di base è \(3 + 4 + 5 = 12\). Essendo il prisma retto, l’area laterale si ottiene da \(\,12 \times 6 = 72\). Infine, l’\textit{area totale} è l’area laterale più \(\,2\) volte l’area di base:
\[
\text{Area}_{\text{totale}}
= 72 + 2 \times 6
= 72 + 12
= 84.
\]
In questo modo, si è calcolato in modo semplice volume e aree (laterale e totale) di un prisma con base triangolare. 

\paragraph{Piramide}
\noindent
Una \textit{piramide} è un poliedro che ha per \textit{base} un poligono (di qualunque forma e dimensione) e per \textit{facce laterali} dei triangoli che congiungono ciascun lato della base a un \textit{vertice} (o \textit{apice}). Se il poligono di base possiede \(n\) lati, la piramide risulta avere \(n+1\) facce (la base poligonale e le \(n\) facce triangolari). Quando la piramide è \textit{retta}, il vertice si trova sulla perpendicolare condotta dal \textit{baricentro} (o dal centro, se la base è regolare) della base; altrimenti, si parla di piramide \textit{obliqua}.

\paragraph{Area e Volume di una Piramide}
Se \(p\) è il \textit{perimetro} della base e \(a\) è l’\textit{apotema laterale} (cioè l’altezza di ciascuna faccia triangolare, misurata dal lato di base fino al vertice della piramide), l’\textit{area laterale} della piramide si calcola come
\[
\text{Area laterale} 
= \frac{p \times a}{2}.
\]
L’\textit{area totale} si ottiene poi sommando l’area laterale e l’area della base:
\[
\text{Area totale}
= \text{Area laterale} + \text{Area di base}.
\]

\smallskip
\noindent
Il \textit{volume} di una piramide si esprime mediante la formula
\[
V 
= \frac{1}{3} \,\bigl(\text{Area di base}\bigr) \times \bigl(\text{altezza}\bigr).
\]
Qui, per \textit{altezza} si intende la distanza perpendicolare dal vertice al piano che contiene la base. Se la base ha un’area \(B\) e l’altezza della piramide è \(h\), allora
\[
V = \tfrac{1}{3} \, B \, h.
\]
Se la base è un poligono regolare e la piramide è retta, l’apotema laterale coincide con l’altezza di ciascuna faccia triangolare, ma in una piramide \textit{generica} (obliqua o con base irregolare) occorre considerare singolarmente i triangoli laterali per determinare la loro area, e la definizione di \textit{altezza} resta la distanza ortogonale dal vertice al piano di base. 

\newpage


\subsectionstar{[16*] Solidi di Rotazione}
\noindent
Quando si parla di \textit{solidi di rotazione}, ci si riferisce a quei \textbf{solidi tridimensionali} che si ottengono facendo \textit{ruotare} una figura bidimensionale attorno a un asse. In altre parole, si parte da un’area o da una curva semplice nel piano e, mediante un movimento di \textit{rotazione} completo (generalmente \(360^\circ\)), si genera un corpo nello spazio. Questa costruzione è particolarmente studiata in geometria e analisi, perché le formule di volume e superficie di tali solidi spesso presentano una forma relativamente “pulita”, grazie alla simmetria di rotazione.

\smallskip
\noindent
\textbf{Dal 2D al 3D per rotazione.}
L’idea di base è: si prende una \textit{curva} o un \textit{poligono} o addirittura un’area delimitata da funzioni nel piano \((x,y)\). Scelto un \textit{asse} (ad esempio, l’asse \(x\) o l’asse \(y\)), si ruota questa figura di \(360^\circ\) attorno a tale linea. Ogni punto della figura, descrivendo una circonferenza (o un arco di cerchio) attorno all’asse, crea una \textit{superficie} o un \textit{volume} nello spazio.

\smallskip
\noindent
\textbf{Esempi classici di solidi di rotazione.}
\begin{itemize}
  \item \textit{Cilindro circolare retto:} si ottiene ruotando un rettangolo attorno a uno dei suoi lati (che funge da asse). Più precisamente, se si ruota un rettangolo di base \(r\) e altezza \(h\) attorno al lato di lunghezza \(h\), la base \(r\) genera il \textit{raggio} del cilindro.
  \item \textit{Cono circolare retto:} nasce dalla rotazione di un triangolo rettangolo attorno a uno dei suoi cateti. Il cateto usato come asse resta “fermo”, mentre l’altro cateto descrive il \textit{raggio} di base e l’ipotenusa diventa la \textit{superficie} del cono.
  \item \textit{Sfera:} ruotando un semicerchio attorno al suo diametro, si genera una sfera. In tal caso, ogni punto del semicerchio traccia un cerchio parallelo all’asse, e l’insieme di questi cerchi forma la superficie sferica.
  \item \textit{Toro (ciambella):} si ottiene prendendo una circonferenza e ruotandola attorno a un asse che non la \textit{interseca}, producendo un solido “ad anello” (come una ciambella). In pratica, si ruota un cerchio in modo che il centro del cerchio stesso descriva un cerchio più grande.
\end{itemize}

\smallskip
\noindent
\textbf{Osservazione sulle Formule di Volume e Superficie.}
Molti solidi di rotazione hanno formule note di volume e area. Ad esempio:
\begin{itemize}
  \item \textit{Cilindro} di raggio \(r\) e altezza \(h\): volume \(V = \pi r^2\,h\), superficie laterale \(2\pi r\,h\).
  \item \textit{Cono} di raggio \(r\) e altezza \(h\): volume \(V = \tfrac13 \pi r^2\,h\), area laterale \(\pi r\,\sqrt{r^2 + h^2}\).
  \item \textit{Sfera} di raggio \(r\): volume \(V = \tfrac43 \pi r^3\), superficie \(4\pi r^2\).
  \item \textit{Toro} con cerchio interno di raggio \(r\) e distanza dal centro dell’asse di rotazione \(R\): volume \(V = 2\pi^2 R\,r^2\), area \(4\pi^2 R\,r\).
\end{itemize}

\paragraph{Esempio}
\noindent
Supponiamo di avere un cono in cui conosciamo:
\begin{itemize}
  \item Il \textit{raggio} \(r\) della base (la distanza dal centro della base al bordo);
  \item La \textit{lunghezza laterale} \(l\), cioè la distanza dal vertice del cono a un punto qualsiasi della circonferenza di base.
\end{itemize}
Vogliamo trovare il \textit{volume} del cono, sapendo che la formula generale è
\[
V \;=\;\frac{1}{3}\,\pi\,r^2\,h,
\]
dove \(h\) è l’altezza (la distanza ortogonale dal vertice al centro della base). Poiché conosciamo \(r\) e \(l\), possiamo ricavare \(h\) dal \textit{teorema di Pitagora} applicato al triangolo rettangolo che ha per cateti \(h\) e \(r\), e per ipotenusa \(l\). In simboli:
\[
l^2 \;=\; h^2 \;+\; r^2
\quad\Longrightarrow\quad
h \;=\;\sqrt{\,l^2 - r^2}\,.
\]
Una volta determinato \(h\), si sostituisce nella formula del volume:
\[
V \;=\;\frac{1}{3}\,\pi\,r^2\,\sqrt{l^2 - r^2}.
\]

\begin{center}
\begin{tikzpicture}[scale=1.0, line join=round, line cap=round]

  %--- Prima figura (falso 3D) del cono ---
  % Base del cono (cerchio approssimato come ellisse)
  \draw[thick] (0,0) ellipse (1.3cm and 0.4cm);

  % Vertice del cono (in alto)
  \coordinate (V) at (0,4);

  % Cerchio di base (centro O a (0,0))
  \coordinate (O) at (0,0);

  % Disegno delle linee laterali del cono
  \draw[thick] (V) -- (-1.3,0);
  \draw[thick] (V) -- (1.3,0);

  % Etichette del cono
  \node at (0.4,0.25) {\small $r$}; % Raggio
  \draw[dashed] (O) -- (0,4) node[midway,right] {\small $h$};

  % Una linea tratteggiata per la "lunghezza laterale" (slant) dal vertice a un punto del bordo
  \draw[dashed] (V) -- (1.3,0) node[midway,right,xshift=2pt] {\small $l$};

  %--- Seconda figura (triangolo rettangolo) per illustrare h, r, l ---
  % Spostiamo la seconda figura a destra
  \begin{scope}[xshift=4.5cm,yshift=0cm]
    % Triangolo con base r e altezza h, ipotenusa l
    \coordinate (A) at (0,0); % vertice in basso a sinistra
    \coordinate (B) at (2,0); % vertice in basso a destra
    \coordinate (C) at (0,3); % vertice in alto a sinistra

    \draw[thick] (A)--(B)--(C)--cycle;
    % Etichette
    \node[below] at (1,0) {\small $r$}; 
    \node[left] at (0,1.5) {\small $h$};
    \node[above right] at (0.7,1.8) {\small $l$};

    % Angolo retto
    \draw (A) ++(0.3,0) -- ++(0,0.3) -- ++(-0.3,0);

    % Puntini
    \fill (A) circle(1pt) node[below left] {\small $A$};
    \fill (B) circle(1pt) node[below right] {\small $B$};
    \fill (C) circle(1pt) node[above left] {\small $C$};

  \end{scope}

\end{tikzpicture}
\end{center}

\smallskip
\noindent
Supponiamo di avere un cono in cui:
\[
r = 3,
\quad
l = 7.
\]
Vogliamo determinare \textit{volume} e \textit{area totale} del cono, sapendo che:
\[
h = \sqrt{\,l^2 - r^2\,}
\quad\text{(altezza via Pitagora)},
\quad
V = \tfrac13\,\pi\,r^2\,h,
\quad
\text{Area laterale} = \pi\,r\,l,
\quad
\text{Area totale} = \pi\,r\,l + \pi\,r^2.
\]

\smallskip
\noindent
Calcolo dell’altezza $h$:
\[
h = \sqrt{\,7^2 - 3^2\,}
= \sqrt{\,49 - 9\,}
= \sqrt{\,40\,}
= 2\,\sqrt{10}.
\]

\smallskip
\noindent
Volume:
\[
V = \tfrac13\,\pi \,(3)^2\,\bigl(2\,\sqrt{10}\bigr)
= \tfrac13 \,\pi \,9 \,\bigl(2\,\sqrt{10}\bigr)
= 6\,\pi\,\sqrt{10}.
\]
In forma approssimata, se volessimo un valore numerico, \(6\,\sqrt{10} \approx 6 \times 3.1623 \approx 18.9738\), dunque \(V \approx 18.97\,\pi \approx 59.59.\)

\smallskip
\noindent
Area laterale e totale:
\[
\text{Area laterale} = \pi \, r \, l = \pi \times 3 \times 7 = 21\,\pi,
\quad
\text{Area di base} = \pi \,r^2 = \pi \times 9 = 9\,\pi.
\]
\[
\text{Area totale} = 21\,\pi \;+\; 9\,\pi = 30\,\pi.
\]
Quindi il cono con raggio \(3\) e lunghezza laterale \(7\) ha un volume \(6\,\pi\,\sqrt{10}\) (circa \(59.59\) in unità cubiche) e un’area totale \(30\,\pi\) (circa \(94.25\) in unità quadrate). 
\newpage


\subsectionstar{[15*] Principio di Cavalieri}

\smallskip
\noindent
Il \textit{principio di Cavalieri} stabilisce che, se due solidi nello spazio hanno la \textit{stessa altezza} e ogni \textit{sezione trasversale} (ottenuta tagliandoli con un piano parallelo alla base) ha \textit{uguale area} in entrambi i solidi, allora i due solidi possiedono \textit{uguale volume}. L’idea chiave è che, “sfogliando” il solido orizzontalmente a diversi livelli, si ritrovano sezioni di identica forma e misura, e la “sovrapposizione” di tutte queste sezioni in altezza genera lo stesso volume.

\noindent
\paragraph{Applicazioni Generali} Vediamo ora alcuni casi applicativi del principio di Cavalieri:\\

\smallskip
\noindent
\textit{1. Confronto di Volumi tra Cilindro e Solido con Base Variabile.}  
Se consideriamo un \textit{cilindro} retto di altezza \(h\) e un altro solido di uguale altezza, e scopriamo che a ogni quota \(z\) (da 0 a \(h\)) le sezioni trasversali \textit{parallele alla base} hanno la \textit{stessa area}, allora i due solidi hanno medesimo volume. Questo principio permette di dimostrare, ad esempio, l’uguaglianza di volume fra un \textit{cilindro} e un “cilindro obliquo” (o prismoide) di pari altezza, quando le aree di sezione orizzontale combaciano.

\smallskip
\noindent
\textit{2. Volume del Cono e Delimitazione con un Cilindro.}  
Un esempio più noto è il calcolo del \textit{volume del cono} tramite il principio di Cavalieri, confrontando il cono con una piramide “equivalente” o con un \textit{cilindro} parzialmente riempito, dimostrando che \(\displaystyle V_{\text{cono}} = \tfrac{1}{3}\,(\text{area base})\cdot (\text{altezza})\). In questo caso, si considera un cilindro e un cono (di uguale raggio e altezza) e si confrontano le sezioni orizzontali: quella del cilindro è sempre un cerchio di raggio costante, mentre quella del cono è un cerchio di raggio lineare con la quota \(z\). La differenza di area mostra il fattore \(\tfrac13\). Se però si costruisce opportunamente un solido che “colmi” la differenza, si applica Cavalieri per stabilire la formula definitiva.

\smallskip
\noindent
\textit{3. Solidi a Sezione Trasversale Costante.}  
Un caso molto semplice, ma emblematico, riguarda due solidi di \textit{uguale altezza} con \textit{sezione trasversale identica} a ogni livello. Se a ciascuna quota \(\,z\) i due solidi presentano lo stesso poligono di area \(A(z)\), allora i volumi coincidono. Questo può apparire ovvio, ma è la formalizzazione del principio di Cavalieri: se non cambia l’“ingombro” a ogni “piano orizzontale,” i due solidi occupano la stessa quantità di spazio. Pensiamo ad esempui a due cilindri, il primo retto ed il secodo obliquo:
\begin{center}
\begin{tikzpicture}[scale=0.8, line cap=round, line join=round]

% -- PRIMO SOLIDO: CILINDRO A SINISTRA --
\coordinate (CylBaseCenter) at (0,0);
\def\CylRadius{1.2}
\def\CylHeight{3}

% Base ellittica (in basso) del cilindro
\draw[thick] (CylBaseCenter) ellipse (\CylRadius cm and 0.4cm);

% Linee verticali del cilindro
\draw[thick] ($(CylBaseCenter)+(-\CylRadius,0)$) -- ++(0,\CylHeight);
\draw[thick] ($(CylBaseCenter)+(\CylRadius,0)$) -- ++(0,\CylHeight);

% Ellisse in alto (top) del cilindro
\coordinate (CylTopCenter) at ($(CylBaseCenter)+(0,\CylHeight)$);
\draw[thick] (CylTopCenter) ellipse (\CylRadius cm and 0.4cm);

% Sezioni orizzontali (dashed) nel cilindro
\foreach \y in {1.0,2.0}{
  \draw[dashed] ($(CylBaseCenter)+(0,\y)$) ellipse (\CylRadius cm and 0.4cm);
}

% Etichetta "Cilindro"
\node at (0,\CylHeight+0.6) {\small Cilindro};


% -- SECONDO SOLIDO: PARALLELEPIPEDO A DESTRA --
\coordinate (ParaBaseCenter) at (5,0);
\def\ParaRadius{1.2}
\def\ParaHeight{3}
\def\ShiftX{1.2} % spostamento orizzontale per la "sommità" del parallelepipedo

% Base ellittica (in basso) del parallelepipedo
\draw[thick] (ParaBaseCenter) ellipse (\ParaRadius cm and 0.4cm);

% Ora definiamo la "top" come un'ellisse identica spostata di \ShiftX a destra e \ParaHeight in alto
\coordinate (ParaTopCenter) at ($(ParaBaseCenter)+(\ShiftX,\ParaHeight)$);

% Ellisse in alto: i segmenti davanti sono continui, quelli dietro sono dashed
\draw[thick] (ParaTopCenter) ellipse (\ParaRadius cm and 0.4cm);

% Disegno degli spigoli verticali (faux 3D):
% Avanti
\draw[thick] ($(ParaBaseCenter)+(-\ParaRadius,0)$) -- ++(\ShiftX,\ParaHeight);
\draw[thick] ($(ParaBaseCenter)+(\ParaRadius,0)$) -- ++(\ShiftX,\ParaHeight);

% Disegno spigoli "dietro" (dashed)
% Questi connettono la parte posteriore dell'ellisse base a quella dell'ellisse top
% (E' un disegno semplificato: base e top sono ellissi identiche)
\draw[dashed] ($(ParaBaseCenter)+(0,0)$) -- ($(ParaTopCenter)+(0,0)$);

% Sezioni orizzontali (dashed) nel parallelepipedo
% Ad ogni y, la sezione e' un'ellisse spostata di \ShiftX*(y/\ParaHeight)
\foreach \y in {1.0,2.0}{
  \pgfmathsetmacro{\delta}{\ShiftX*(\y/\ParaHeight)}
  \draw[dashed] ($(ParaBaseCenter)+( \delta,\y )$) ellipse (\ParaRadius cm and 0.4cm);
}

% Etichetta "Parallelepipedo"
\node at ($(ParaTopCenter)+(0,0.7)$) {\small Parallelepipedo};

\end{tikzpicture}
\end{center}
\paragraph{Esempio}
\noindent
Consideriamo un \textit{cilindro retto} di raggio \(r=2\) e altezza \(h=4\). A ogni quota orizzontale \(z\), la \textit{sezione} del cilindro è un \textit{cerchio} di raggio 2, quindi l’area della sezione è \(4\pi\). Il volume del cilindro risulta
\[
V_{\text{cilindro}}
= \bigl(\text{area base}\bigr)\times \bigl(\text{altezza}\bigr)
= \pi \cdot (2)^2 \cdot 4
= 16\,\pi.
\]
Vogliamo confrontarlo con un \textit{parallelepipedo obliquo} avente la stessa altezza \(4\) e sezioni orizzontali di \textit{uguale area}. Supponiamo che la base del parallelepipedo sia un rettangolo di dimensioni \(2\) per \(2\pi\), in modo che la sua area sia \(2 \times 2\pi = 4\pi\). In questo modo, a ogni livello orizzontale \(z\), la sezione risulta nuovamente un rettangolo di area \(4\pi\), e l’altezza totale è 4. Vediamo quindi i due solidi in figura, si noti che per convenienza grafica il secondo solido è appoggiato sulla faccia più lunga, avendo quindi l'altezza parallela al piano orizzontale dello spettatore:

\begin{center}
\begin{tikzpicture}[scale=1.0, line cap=round, line join=round]

% ======================
% PRIMO SOLIDO: CILINDRO A SINISTRA
% ======================
\coordinate (CylBaseCenter) at (0,0);
\def\CylRadius{2}  % Raggio ellittico orizzontale per il disegno 2D
\def\CylHeight{4}    % Altezza fittizia nel disegno

% Base ellittica (in basso)
\draw[thick] (CylBaseCenter) ellipse (\CylRadius cm and 0.4cm);

% Linee verticali
\draw[thick] ($(CylBaseCenter)+(-\CylRadius,0)$) -- ++(0,\CylHeight);
\draw[thick] ($(CylBaseCenter)+(\CylRadius,0)$) -- ++(0,\CylHeight);

% Ellisse in alto (top)
\coordinate (CylTopCenter) at ($(CylBaseCenter)+(0,\CylHeight)$);
\draw[thick] (CylTopCenter) ellipse (\CylRadius cm and 0.4cm);

% Sezioni orizzontali (dashed)
\foreach \y in {1.0,2.0}{
  \draw[dashed] ($(CylBaseCenter)+(0,\y)$) ellipse (\CylRadius cm and 0.4cm);
}

% ======================
% SECONDO SOLIDO: PARALLELEPIPEDO OBLIQUO A DESTRA
% ======================
\coordinate (ParaBaseCenter) at (5,0);

% Vogliamo che la base abbia area ~ 4\pi, come il cerchio (r=2 => area=4\pi).
% Scegliamo base ~ 2.2 x 5.7 => ~ 12.54, che approssima 4\pi=12.566...
% e un'altezza "fittizia" nel disegno ~ 3 (uguale al cilindro).
\def\RectWidth{2.0}
\def\RectHeight{4}  % area base ~ 2.2*5.7 ~ 12.54 ~ 4\pi
\def\RectLength{6.28}
\def\ParaShiftX{1.0}  % spostamento orizzontale del top
\def\ParaShiftY{3.0}  % spostamento verticale, =CylHeight

% Vertici della base (A-B-C-D)
\coordinate (A) at (ParaBaseCenter);
\coordinate (B) at ($(A)+(\RectWidth,0)$);
\coordinate (C) at ($(B)+(0,\RectHeight)$);
\coordinate (D) at ($(A)+(0,\RectHeight)$);

\draw[thick] (A)--(B)--(C)--(D)--cycle;

% Vertici "top" Aup-Bup-Cup-Dup (spostati di (ParaShiftX, ParaShiftY))
\coordinate (Aup) at ($(A)+(\ParaShiftX,\ParaShiftY)$);
\coordinate (Bup) at ($(B)+(\ParaShiftX,\ParaShiftY)$);
\coordinate (Cup) at ($(C)+(\ParaShiftX,\ParaShiftY)$);
\coordinate (Dup) at ($(D)+(\ParaShiftX,\ParaShiftY)$);

% Disegno del top
\draw[thick] (Aup)--(Bup)--(Cup)--(Dup)--cycle;

% Spigoli obliqui
\draw[thick] (A)--(Aup);
\draw[thick] (B)--(Bup);
\draw[thick] (C)--(Cup);
\draw[thick] (D)--(Dup);

% Sezioni orizzontali (dashed) ad altezze intermedie
\foreach \yRatio in {0.33,0.66}{
  \coordinate (Asec) at ($(A) !\yRatio! (Aup)$);
  \coordinate (Bsec) at ($(B) !\yRatio! (Bup)$);
  \coordinate (Csec) at ($(C) !\yRatio! (Cup)$);
  \coordinate (Dsec) at ($(D) !\yRatio! (Dup)$);
  \draw[dashed] (Asec)--(Bsec)--(Csec)--(Dsec)--cycle;
}

\end{tikzpicture}
\end{center}

\medskip
\noindent

Notiamo che per poter applicare il principio di Cavalieri quello che ci interessa, dopo aver notato che l'altezza è uguale, sono le sezioni dei solidi. Le vediamo quindi in figura:

\begin{center}
\begin{tikzpicture}[line cap=round, line join=round, scale=1.0]

% ------------------
% Cerchio di raggio 2, centro in O(0, 3.1415)
% ------------------
\coordinate (O) at (0,{3.1415});
\def\Rc{2}
\draw[thick] (O) circle(\Rc);

% Etichetta raggio = 2, senza frecce aggiuntive
% Tracciamo un segmento orizzontale da O verso destra, ma etichettiamo "2" accanto
\draw[dashed] (O) -- ++(\Rc,0);
\node at ($(O)+(0.5*\Rc,0.25)$) {\small 2};

% ------------------
% Rettangolo 2 x 2pi, in (6,0) con base=2 e altezza=6.283
% ------------------
\def\RectW{2}
\def\RectH{6.283}

% Disegno del rettangolo
\draw[thick] (6,0) rectangle ++(\RectW,\RectH);

% Etichetta base=2: posizioniamo "2" appena sopra la base
\node at ($(6,0) + (1,0.2)$) {\small 2};

% Etichetta altezza=6.283: posizioniamo "6.283" vicino al lato destro
\node[rotate=90] at ($(8,0) + (0.2,0.5*\RectH)$) {\small $2 \cdot \pi$};

\end{tikzpicture}
\end{center}

\noindent \textbf{Applicazione del Principio di Cavalieri.}  
A ogni quota orizzontale \(z\), il cilindro possiede una \textit{sezione} (cerchio) di area \(4\pi\), mentre il parallelepipedo obliquo ha una \textit{sezione} (rettangolo) della stessa area \(4\pi\). Poiché entrambe le figure hanno \[\textit{stessa altezza}=4 \textit{ e } \textit{sezioni orizzontali di eguale area}\] per tutti i valori di \(z\), il \textit{principio di Cavalieri} garantisce che i due solidi abbiano lo \textit{stesso volume}. Nel caso del parallelepipedo, il volume risulta \[\bigl(\text{area base}\bigr)\times \bigl(\text{altezza}\bigr) = 4\pi \times 4 = 16\pi\] esattamente il medesimo del cilindro.  

\medskip
\noindent
In questo esempio numerico, nonostante il parallelepipedo appaia inclinato e abbia un \textit{rettangolo} come sezione, e il cilindro abbia un \textit{cerchio} di raggio 2, le \textit{aree} coincidono a ogni quota e l’altezza è identica, quindi il \textit{principio di Cavalieri} dimostra la loro \textit{uguaglianza di volume}. 



\newpage



\section{Trigonometria}
In questo capitolo di trigonometria verranno presentate numerose formule utili per i calcoli trigonometrici. Di seguito è riportata una tabella riassuntiva che raccoglie tutte le formule studiate: questa tabella servirà come riferimento per lo studente, che potrà confrontare e ripassare le formule durante lo svolgimento degli esercizi.

\begin{center}
\begin{tabular}{|l|l|}
\hline
\textbf{Categoria} & \textbf{Formule/Definizioni} \\
\hline
Identità Pitagoriche & 
\(\sin^2\theta + \cos^2\theta = 1\) \\[2mm]
& \(1 + \tan^2\theta = \sec^2\theta\) \\[2mm]
& \(1 + \cot^2\theta = \csc^2\theta\) \\
\hline
Identità di Simmetria & 
\textbf{Complementari:} \(\sin(90^\circ-\theta)=\cos\theta,\quad \cos(90^\circ-\theta)=\sin\theta\) \\[2mm]
& \textbf{Supplementari:} \(\sin(180^\circ-\theta)=\sin\theta,\quad \cos(180^\circ-\theta)=-\cos\theta\) \\[2mm]
& \textbf{Esplementari:} \(\sin(360^\circ-\theta)=-\sin\theta,\quad \cos(360^\circ-\theta)=\cos\theta\) \\
\hline
Formule di Somma e Sottrazione & 
\(\sin(\alpha+\beta)=\sin\alpha\,\cos\beta+\cos\alpha\,\sin\beta\) \\[2mm]
& \(\sin(\alpha-\beta)=\sin\alpha\,\cos\beta-\cos\alpha\,\sin\beta\) \\[2mm]
& \(\cos(\alpha+\beta)=\cos\alpha\,\cos\beta-\sin\alpha\,\sin\beta\) \\[2mm]
& \(\cos(\alpha-\beta)=\cos\alpha\,\cos\beta+\sin\alpha\,\sin\beta\) \\[2mm]
& \(\tan(\alpha+\beta)=\frac{\tan\alpha+\tan\beta}{1-\tan\alpha\,\tan\beta}\) \\
\hline
Formule di Duplicazione & 
\(\sin(2\theta)=2\sin\theta\,\cos\theta\) \\[2mm]
& \(\cos(2\theta)=\cos^2\theta-\sin^2\theta\) \\[2mm]
& \(\cos(2\theta)=2\cos^2\theta-1\) \\[2mm]
& \(\cos(2\theta)=1-2\sin^2\theta\) \\
\hline
Formule di Prostaferesi & 
\(\sin\alpha+\sin\beta=2\sin\frac{\alpha+\beta}{2}\cos\frac{\alpha-\beta}{2}\) \\[2mm]
& \(\sin\alpha-\sin\beta=2\cos\frac{\alpha+\beta}{2}\sin\frac{\alpha-\beta}{2}\) \\[2mm]
& \(\cos\alpha+\cos\beta=2\cos\frac{\alpha+\beta}{2}\cos\frac{\alpha-\beta}{2}\) \\[2mm]
& \(\cos\alpha-\cos\beta=-2\sin\frac{\alpha+\beta}{2}\sin\frac{\alpha-\beta}{2}\) \\
\hline
Teorema dei Seni & 
\(\displaystyle \frac{a}{\sin\alpha} = \frac{b}{\sin\beta} = \frac{c}{\sin\gamma}\)\\
\hline
Teorema del Coseno & 
\(\displaystyle a^2 = b^2 + c^2 - 2\,b\,c\,\cos\alpha\) \\
\hline
Formule di Briggs per \(\alpha\) & 
\(\displaystyle \alpha = \sqrt{\frac{(p-b)(p-c)}{b\,c}}\), \(\displaystyle \sqrt{\frac{p\,(p-a)}{b\,c}}\), \(\displaystyle \sqrt{\frac{(p-b)(p-c)}{p\,(p-a)}}\) \\
\hline
Formule di Briggs per \(\beta\) & 
\(\displaystyle \beta = \sqrt{\frac{(p-a)(p-c)}{a\,c}}\), \(\displaystyle \sqrt{\frac{p\,(p-b)}{a\,c}}\), \(\displaystyle \sqrt{\frac{(p-a)(p-c)}{p\,(p-b)}}\) \\
\hline
Formule di Briggs per \(\gamma\) & 
\(\displaystyle \gamma = \sqrt{\frac{(p-a)(p-b)}{a\,b}}\), \(\displaystyle \sqrt{\frac{p\,(p-c)}{a\,b}}\), \(\displaystyle \sqrt{\frac{(p-a)(p-b)}{p\,(p-c)}}\) \\
\hline
\end{tabular}
\end{center}
\newpage

\subsectionstar{[1] Equazioni Goniometriche}
Le equazioni goniometriche sono fondamentali per descrivere i rapporti tra gli angoli e le lunghezze in un triangolo rettangolo. In un triangolo rettangolo, il \textit{seno} di un angolo \(\theta\) è definito come il rapporto tra la lunghezza del cateto opposto a \(\theta\) e l'ipotenusa, mentre il \textit{coseno} è il rapporto tra la lunghezza del cateto adiacente a \(\theta\) e l'ipotenusa. Queste definizioni permettono di estendere il concetto di seno e coseno ad angoli di qualsiasi misura. Da queste definizioni derivano anche le altre funzioni goniometriche:
\[
\tan\theta=\frac{\sin\theta}{\cos\theta},\quad \sec\theta=\frac{1}{\cos\theta},\quad \csc\theta=\frac{1}{\sin\theta}.
\]

\paragraph{Grafici di \(\sin(x)\) e \(\cos(x)\).}
Le funzioni \(\sin(x)\) e \(\cos(x)\) sono funzioni periodiche, dette anche sinusoidi per la loro caratteristica forma ondulata. Questo significa che, dopo un intervallo di lunghezza \(2\pi\), esse si ripetono inalterate. La figura seguente mostra i grafici di \(\sin(x)\) (in blu) e \(\cos(x)\) (in rosso) sul loro periodo fondamentale.

\begin{center}
\begin{tikzpicture}[scale=1]
  % Disegno degli assi cartesiani
  \draw[->] (-0.5,0) -- (7,0) node[right] {\(x\)};
  \draw[->] (0,-1.5) -- (0,1.5) node[above] {\(y\)};
  
  % Grafico di sin(x) in blu (dominio 0 - 2pi)
  \draw[domain=0:6.283, smooth, variable=\x, blue, thick] 
    plot ({\x}, {sin(deg(\x))});
  
  % Grafico di cos(x) in rosso (dominio 0 - 2pi)
  \draw[domain=0:6.283, smooth, variable=\x, red, thick] 
    plot ({\x}, {cos(deg(\x))});
  
  % Etichette per le funzioni
  \node[blue] at (6,0.5) {\(\sin(x)\)};
  \node[red] at (6,1.5) {\(\cos(x)\)};
  
  % Marcature sull'asse x per i punti chiave: 0, pi/2, pi, 3pi/2, 2pi
  \foreach \x/\xtext in {0/0, 1.57/\(\frac{\pi}{2}\), 3.14/\(\pi\), 4.71/\(\frac{3\pi}{2}\), 6.28/\(2\pi\)} {
    \draw[shift={(\x,0)}] (0pt,2pt) -- (0pt,-2pt);
    \node at (\x,-0.3) {};}
\end{tikzpicture}
\end{center}

\paragraph{Tabella dei Valori.}
Le funzioni goniometriche, come \(\sin(x)\) e \(\cos(x)\), accettano in genere come argomento valori espressi in radianti; tuttavia, è possibile utilizzare anche i gradi, poiché i due sistemi sono intercambiabili. Ad esempio, \(90^\circ\) corrispondono a \(\frac{\pi}{2}\) radianti. La tabella seguente mostra la corrispondenza tra gradi e radianti per alcuni angoli fondamentali, insieme ai valori esatti di \(\sin\), \(\cos\) e \(\tan\).

\begin{center}
\setlength{\tabcolsep}{10pt}
\renewcommand{\arraystretch}{1.4}
\begin{tabular}{|c|c|c|c|c|}
\hline
\(\theta\) (gradi) & \(\theta\) (radianti) & \(\sin\theta\) & \(\cos\theta\) & \(\tan\theta\) \\ \hline
\(0^\circ\)  & \(0\)              & \(0\)              & \(1\)             & \(0\) \\ \hline
\(18^\circ\) & \(\frac{\pi}{10}\)  & \(\frac{\sqrt{5}-1}{4}\)    & \(\frac{\sqrt{10+2\sqrt{5}}}{4}\) & \(\frac{\sqrt{5}-1}{\sqrt{10+2\sqrt{5}}}\) \\ \hline
\(30^\circ\) & \(\frac{\pi}{6}\)  & \(\frac{1}{2}\)    & \(\frac{\sqrt{3}}{2}\) & \(\frac{1}{\sqrt{3}}\) \\ \hline
\(45^\circ\) & \(\frac{\pi}{4}\)  & \(\frac{\sqrt{2}}{2}\) & \(\frac{\sqrt{2}}{2}\) & \(1\) \\ \hline
\(60^\circ\) & \(\frac{\pi}{3}\)  & \(\frac{\sqrt{3}}{2}\) & \(\frac{1}{2}\)    & \(\sqrt{3}\) \\ \hline
\(90^\circ\) & \(\frac{\pi}{2}\)  & \(1\)              & \(0\)             & \(-\) \\ \hline
\end{tabular}
\end{center}

Gli angoli possono essere misurati sia in gradi che in radianti. La conversione da gradi a radianti si ottiene mediante la formula
\[
\theta_{\text{rad}}=\theta_{\text{deg}}\cdot \frac{\pi}{180^\circ},
\]
mentre quella inversa è data da
\[
\theta_{\text{deg}}=\theta_{\text{rad}}\cdot \frac{180^\circ}{\pi}.
\]
Queste relazioni consentono di passare agevolmente da un sistema di misura all'altro, garantendo la corretta valutazione delle funzioni goniometriche.

Notiamo anche che la funzione \(\tan(\theta)\) è definita come
\[
\tan(\theta)=\frac{\sin(\theta)}{\cos(\theta)}.
\]
Poiché la divisione per zero non è ammessa, se \(\cos(\theta)=0\) la funzione \(\tan(\theta)\) risulta indefinita. Ad esempio, per \(\theta=90^\circ\) (cioè \(\frac{\pi}{2}\) radianti), essendo \(\cos(90^\circ)=0\), la tangente non ha un valore definito, lo stesso capita per secante e cosecante. Vediamo ora il grafico della tangente.

La funzione \(\tan(x)\) è periodica con periodo \(\pi\) e presenta asintoti verticali nei punti in cui \(\cos(x)=0\), ad esempio in \(x=\frac{\pi}{2}\). Di conseguenza, la funzione non è definita in tali punti. Il grafico seguente mostra la funzione \(\tan(x)\) (in verde) per un periodo, evidenziando la sua forma ondulata (sinusoidale) e l'asintoto verticale.

\begin{center}
\begin{tikzpicture}[scale=1]
  % Disegno degli assi cartesiani
  \draw[->] (-0.5,0) -- (3.5,0) node[right] {\(x\)};
  \draw[->] (0,-3) -- (0,3) node[above] {\(y\)};
  
  % Grafico di tan(x) in verde: disegnato in due rami per evitare il punto di discontinuità in pi/2
  \draw[domain=0:1.3, smooth, variable=\x, green, thick] plot ({\x}, {tan(deg(\x))});
  \draw[domain=1.85:3.14, smooth, variable=\x, green, thick] plot ({\x}, {tan(deg(\x))});
  
  % Disegno dell'asintoto verticale in x = pi/2
  \draw[dashed] (1.57,-3) -- (1.57,3);
  
  % Etichette per i punti chiave sull'asse x
  \foreach \x/\xtext in {0/0, 1.57/\(\frac{\pi}{2}\), 3.14/\(\pi\)} {
    \draw[shift={(\x,0)}] (0pt,2pt) -- (0pt,-2pt);}
  
  % Etichetta della funzione tan(x)
  \node[green] at (3.0,2.5) {\(\tan(x)\)};
\end{tikzpicture}
\end{center}

\paragraph{Applicazione in un Triangolo Rettangolo.}
Consideriamo un triangolo rettangolo in cui l'ipotenusa ha lunghezza \(h\) e uno degli angoli acuti è \(\theta\). Per definizione:
\[
\sin\theta=\frac{\text{cateto opposto}}{h},\quad \cos\theta=\frac{\text{cateto adiacente}}{h}.
\]
Ad esempio, se \(h=10\) e \(\theta=30^\circ\), si ha:
\[
\text{cateto opposto}=10\cdot\sin30^\circ=10\cdot\frac{1}{2}=5,\quad \text{cateto adiacente}=10\cdot\cos30^\circ=10\cdot\frac{\sqrt{3}}{2}=5\sqrt{3}.
\]
La figura seguente illustra un triangolo rettangolo con i cateti etichettati in base alle definizioni di seno e coseno:
\begin{center}
\begin{tikzpicture}[scale=1, every node/.style={font=\small}]
  % Definizione dei punti
  \coordinate (A) at (0,0);
  \coordinate (B) at (4,0);
  \coordinate (C) at (0,3);
  
  % Disegno del triangolo rettangolo
  \draw[thick] (A) -- (B) -- (C) -- cycle;
  
  % Angolo rettangolo in A
  \draw (0.4,0) -- (0.4,0.4) -- (0,0.4);
  
  % Etichette dei vertici
  \node at (A) [below left] {\(A\)};
  \node at (B) [right] {\(B\)};
  \node at (C) [above] {\(C\)};
  
  % Segmento ipotenusa
  \draw[<->] (B) -- (C);
  \node at (2.5,2) {\(h\)};
  
  % Cateti
  \draw[<->] (A) -- (B);
  \node at (2,0) [below] {Adiacente};
  
  \draw[<->] (A) -- (C);
  \node at (0,1.5) [left] {Opposto};
\end{tikzpicture}
\end{center}
\newpage

\subsection*{[21] Identità Goniometriche}
Prima di vedere questa sezione è necessario aver consultato la precedente per avere chiara comprensione delle funzioni goniometriche e del loro funzionamento

\paragraph{Identità Pitagoriche}
Le identità pitagoriche derivano dal teorema di Pitagora applicato al triangolo rettangolo inscritto nella circonferenza goniometrica (unitaria). Esse affermano che:
\[
\sin^2\theta + \cos^2\theta = 1,
\]
\[
1 + \tan^2\theta = \frac{1}{\cos^2\theta},
\]
\[
1 + \cot^2\theta = \frac{1}{\sin^2\theta}.
\]

Per sviluppare un'intuizione sul perché queste identità siano valde, basti considerare il triangolo rettangolo che costruiamo all'interno di questo cerchio. Notiamo che si trattadi un triangolo rettangolo con angolo $\theta$ al centro e che ci permette quindi di applicare il Teorema di Pitagora, vediamo come i due cateti hanno lunghezza rispettivamente $\sin \theta $ e $\cos \theta$ e l'ipotenusa è il raggio del cerchio unitario (e quindi di lunghezza $1$). Da questo deriviamo la prima identità pitagorica, le altre due sono riformulazioni della prima usando la definizione di tangente.

\begin{center}
\begin{tikzpicture}[scale=2, every node/.style={font=\small}]
  % Circonferenza unitaria
  \draw[thick] (0,0) circle (1);
  % Raggio che forma l'angolo theta
  \def\theta{40}
  \draw[red, thick, ->] (0,0) -- ({cos(\theta)}, {sin(\theta)});
  % Proiezione del punto P sull'asse x
  \draw[dashed] ({cos(\theta)}, {sin(\theta)}) -- ({cos(\theta)}, 0);
  % Angolo theta
  \draw (0.2,0) arc (0:\theta:0.2);
  \node at (0.3,0.1) {\(\theta\)};
  % Etichette
  \node[below left] at (0,0) {\(O\)};
  \node[above right] at ({cos(\theta)}, {sin(\theta)}) {\(P(\cos\theta,\sin\theta)\)};
  \node[below] at ({cos(\theta)},0) {\(\cos\theta\)};
\end{tikzpicture}
\end{center}

Per evitare ambiguità specifichiamo anche che:$$\sin^2 \theta = \sin \theta \cdot \sin \theta \not = \sin(\sin(\theta))$$ quenta ambiguità di notazione emerge dal fatto che i numeri naturali all'esponente sono utilizzati sia per indicare la potenza algebraica che per iterare le funzioni. Vediamo ora un esempio in cui applichiamo l'identità pitagorica.

Se \(\sin\theta = \frac{3}{5}\), allora:
\[
\cos^2\theta = 1 - \sin^2\theta = 1 - \left(\frac{3}{5}\right)^2 = 1 - \frac{9}{25} = \frac{16}{25},
\]
quindi \(\cos\theta = \frac{4}{5}\) (scegliendo il segno in base al quadrante in cui \(\theta\) si trova).


\paragraph{Identità di Simmetria.}  
Queste identità permettono di calcolare i valori delle funzioni trigonometriche per angoli supplementari, complementari ed esplementari. Ad esempio:
\[
\sin(\pi-\theta) = \sin\theta,\quad \cos(\pi-\theta) = -\cos\theta,\quad \tan(\pi-\theta) = -\tan\theta,
\]
\[
\sin(-\theta) = -\sin\theta,\quad \cos(-\theta) = \cos\theta,\quad \tan(-\theta) = -\tan\theta,
\]
\[
\tan(\pi+\theta)=\tan\theta.
\]
\textbf{Esempio:} Calcoliamo \(\sin(150^\circ)\). Poiché \(150^\circ = 180^\circ - 30^\circ\), si ha:
\[
\sin(150^\circ)=\sin(30^\circ)=\frac{1}{2}.
\]

\textbf{Disegno esplicativo:}

\begin{center}
\begin{minipage}{0.45\textwidth}
\centering
\(\sin(\pi-\theta) = \sin(\theta)\)
\bigskip

\begin{tikzpicture}[scale=1.2]
  % Disegno degli assi
  \draw[->] (-1.5,0) -- (1.5,0) node[right] {$x$};
  \draw[->] (0,-1.5) -- (0,1.5) node[above] {$y$};
  
  % Disegno della circonferenza unitaria
  \draw[thick] (0,0) circle (1);
  
  % Definizione dell'angolo theta (in gradi)
  \def\theta{30}
  
  % Disegno del raggio per l'angolo theta (primo quadrante)
  \draw[red, thick, ->] (0,0) -- ({cos(\theta)}, {sin(\theta)}) node[midway, above right] {};
  
  % Disegno del raggio per l'angolo supplementare (secondo quadrante)
  \draw[blue, thick, ->] (0,0) -- ({cos(180-\theta)}, {sin(180-\theta)}) node[midway, above left] {};
  
  % Proiezioni verticali dei punti su ciascun raggio
  \draw[dashed] ({cos(\theta)}, {sin(\theta)}) -- ({cos(\theta)},0);
  \draw[dashed] ({cos(180-\theta)}, {sin(180-\theta)}) -- ({cos(180-\theta)},0);
  
  % Etichettatura dei punti sulla circonferenza
  \node at ({cos(\theta)}, {sin(\theta)}) [above right] {};
  \node at ({cos(180-\theta)}, {sin(180-\theta)}) [above left] {};

\end{tikzpicture}
\end{minipage}\hfill
\begin{minipage}{0.45\textwidth}
\centering
 \(\cos(-\theta) = \cos(\theta)\)
\bigskip

\begin{tikzpicture}[scale=1.2]
  % Disegno degli assi
  \draw[->] (-1.2,0) -- (1.2,0) node[right] {$x$};
  \draw[->] (0,-1.2) -- (0,1.2) node[above] {$y$};
  % Circonferenza unitaria
  \draw[thick] (0,0) circle (1);
  % Definizione dell'angolo theta positivo
  \def\theta{40}
  \draw[red, thick, ->] (0,0) -- ({cos(\theta)}, {sin(\theta)}) node[midway, above right] {};
  % Proiezione verticale del punto corrispondente a theta
  \draw[dashed] ({cos(\theta)}, {sin(\theta)}) -- ({cos(\theta)},0);
  % Disegno dell'angolo negativo -theta
  \draw[blue, thick, ->] (0,0) -- ({cos(\theta)}, {-sin(\theta)}) node[midway, below right] {};
  % Proiezione verticale del punto corrispondente a -theta
  \draw[dashed] ({cos(\theta)}, {-sin(\theta)}) -- ({cos(\theta)},0);
  % Evidenziazione della stessa coordinata x per entrambi i punti
  \node at ({cos(\theta)}, -0.3) {};
  % Annotazione finale
  \node at (0, -1.5) {};
\end{tikzpicture}
\end{minipage}
\end{center}

Nel primo diagramma sono tracciati due raggi: uno che forma l'angolo \(\theta\) nel primo quadrante e l'altro che forma l'angolo supplementare \(\pi-\theta\) nel secondo quadrante. Per ciascun raggio si costruisce un triangolo rettangolo tramite la proiezione perpendicolare del punto di intersezione della circonferenza con l'asse \(x\). In questi triangoli il lato opposto all'angolo (che rappresenta il valore del seno) ha la stessa lunghezza, mentre il lato adiacente (la proiezione sull'asse \(x\)) assume segni opposti. Ciò dimostra che
\[
\sin(\pi-\theta)=\sin\theta \text{ e che } \cos(\pi - \theta) = - \cos \theta
\]

Nel secondo diagramma sono rappresentati due raggi corrispondenti agli angoli \(\theta\) e \(-\theta\). Anche qui si formano dei triangoli rettangoli grazie alla proiezione dei punti di intersezione con l'asse \(x\). Le basi di questi triangoli, che corrispondono ai valori del coseno, risultano identiche, evidenziando che
\[
\cos(-\theta)=\cos\theta \text{ e che } \sin(-\theta) = - \sin \theta
\]

Questa interpretazione, basata sulla costruzione di triangoli rettangoli e dei rettangoli formati dalle proiezioni sugli assi nella circonferenza unitaria, offre una dimostrazione visiva e intuitiva delle identità trigonometriche.

\paragraph{Identità di Addizione e Sottrazione.}  
Queste identità permettono di calcolare i valori di seno, coseno e tangente per somme e differenze di angoli:
\[
\sin(A+B)=\sin A\cos B+\cos A\sin B,
\]
\[
\cos(A+B)=\cos A\cos B-\sin A\sin B,
\]
\[
\tan(A+B)=\frac{\tan A+\tan B}{1-\tan A\,\tan B}.
\]

Per fare un esempio un po' piu complesso che coinvolga più tipi di identità goniometriche, consideriamo l'espressione
\[
E = \frac{\sin(90^\circ-\theta) + \sin(\theta+30^\circ) - \sin(\theta-30^\circ)}{1-\cos^2\theta}.
\]

\noindent Innanzitutto, applicando l'identità di simmetria, abbiamo:
\[
\sin(90^\circ-\theta)=\cos\theta.
\]
Pertanto, il numeratore diventa:
\[
\cos\theta + \sin(\theta+30^\circ) - \sin(\theta-30^\circ).
\]
Utilizziamo ora la formula di addizione e sottrazione per il seno:
\[
\sin(\theta+30^\circ) - \sin(\theta-30^\circ)=2\cos\theta\,\sin30^\circ.
\]
Sapendo che \(\sin30^\circ=\frac{1}{2}\), si ottiene:
\[
\sin(\theta+30^\circ) - \sin(\theta-30^\circ)=2\cos\theta\cdot\frac{1}{2}=\cos\theta.
\]
Quindi il numeratore si semplifica in:
\[
\cos\theta + \cos\theta = 2\cos\theta.
\]

Nel denominatore, applichiamo l'identità pitagorica:
\[
1-\cos^2\theta=\sin^2\theta.
\]

Pertanto, l'espressione diventa:
\[
E = \frac{2\cos\theta}{\sin^2\theta}.
\]
Questa è la forma semplificata, ottenuta combinando le identità di simmetria, di addizione e sottrazione e quella pitagorica.
\newpage

\subsectionstar{[19] Funzioni Trigonometriche di Coppie di Angoli Semplici}
In questa sezione presentiamo casi che sono notevolmente più semplici rispetto a quelli esaminati nella sezione precedente. Le identità e gli esempi relativi agli angoli complementari, supplementari ed explementari sono applicazioni dirette e intuitive delle identità trigonometriche più complesse viste in precedenza. Pertanto, se si è compreso appieno quanto esposto nella sezione precedente, questi casi risulteranno facilmente comprensibili. Di seguito vediamo una tabella che riassume i termini fonamentali della sezione.

\begin{center}
\begin{tabular}{|l|p{10cm}|}
\hline
\textbf{Tipo di angolo} & \textbf{Definizione} \\
\hline
Acuto & Un angolo minore di \(90^\circ\). \\
\hline
Ottuso & Un angolo maggiore di \(90^\circ\) e minore di \(180^\circ\). \\
\hline
Retto & Un angolo esattamente di \(90^\circ\). \\
\hline
Piatto & Un angolo esattamente di \(180^\circ\). \\
\hline
Giro & Un angolo esattamente di \(360^\circ\). \\
\hline
Complementari & Due angoli sono complementari se la loro somma è \(90^\circ\). \\
\hline
Supplementari & Due angoli sono supplementari se la loro somma è \(180^\circ\). \\
\hline
Esplementari & Due angoli sono esplementari se la loro somma è \(360^\circ\). \\
\hline
\end{tabular}
\end{center}

\paragraph{Funzioni Trigonometriche di Coppie di Angoli Semplici}
Ripassando ancora questi termini, vediamo come i risultati della scorsa sezione si applicano ad angoli complementari, supplementari ed esplementari:% Angoli Complementari
Due angoli sono complementari se la loro somma è \(90^\circ\) oppure, in radianti, \(\frac{\pi}{2}\).

\textbf{Proprietà delle Funzioni Trigonometriche degli Angoli Complementari:}
\[
\sin\Bigl(90^\circ-\theta\Bigr)=\cos\theta,\qquad \cos\Bigl(90^\circ-\theta\Bigr)=\sin\theta,
\]
\[
\tan\Bigl(90^\circ-\theta\Bigr)=\cot\theta,\qquad \cot\Bigl(90^\circ-\theta\Bigr)=\tan\theta,
\]
\[
\sec\Bigl(90^\circ-\theta\Bigr)=\csc\theta,\qquad \csc\Bigl(90^\circ-\theta\Bigr)=\sec\theta.
\]

\textbf{Esempio:} Se \(\theta=30^\circ\), allora:
\[
\sin(60^\circ)=\cos(30^\circ),\qquad \cos(60^\circ)=\sin(30^\circ),\qquad \tan(60^\circ)=\cot(30^\circ).
\]

\bigskip

% Angoli Supplementari
Due angoli sono supplementari se la loro somma è \(180^\circ\) oppure, in radianti, \(\pi\).

\textbf{Proprietà delle Funzioni Trigonometriche degli Angoli Supplementari:}
\[
\sin\Bigl(180^\circ-\theta\Bigr)=\sin\theta,\qquad \cos\Bigl(180^\circ-\theta\Bigr)=-\cos\theta,
\]
\[
\tan\Bigl(180^\circ-\theta\Bigr)=-\tan\theta,\qquad \cot\Bigl(180^\circ-\theta\Bigr)=-\cot\theta,
\]
\[
\sec\Bigl(180^\circ-\theta\Bigr)=-\sec\theta,\qquad \csc\Bigl(180^\circ-\theta\Bigr)=\csc\theta.
\]

\textbf{Esempio:} Se \(\theta=45^\circ\), allora:
\[
\sin(135^\circ)=\sin(45^\circ),\qquad \cos(135^\circ)=-\cos(45^\circ),\qquad \tan(135^\circ)=-\tan(45^\circ).
\]

\bigskip

% Angoli Esplementari
Due angoli sono esplementari se la loro somma è \(360^\circ\) oppure, in radianti, \(2\pi\).

\textbf{Proprietà delle Funzioni Trigonometriche degli Angoli Esplementari:}
\[
\sin\Bigl(360^\circ-\theta\Bigr)=-\sin\theta,\qquad \cos\Bigl(360^\circ-\theta\Bigr)=\cos\theta,
\]
\[
\tan\Bigl(360^\circ-\theta\Bigr)=-\tan\theta,\qquad \cot\Bigl(360^\circ-\theta\Bigr)=-\cot\theta,
\]
\[
\sec\Bigl(360^\circ-\theta\Bigr)=\sec\theta,\qquad \csc\Bigl(360^\circ-\theta\Bigr)=-\csc\theta.
\]

\textbf{Esempio:} Se \(\theta=60^\circ\), allora:
\[
\sin(300^\circ)=-\sin(60^\circ),\qquad \cos(300^\circ)=\cos(60^\circ),\qquad \tan(300^\circ)=-\tan(60^\circ).
\]

Vediamo ora un esempio in cui mettiamo in pratica diverse di queste nozioni assieme.
\vspace{1em}

% Figura del parallelogramma
\begin{center}
\begin{tikzpicture}[scale=1.0]
  % Disegno del parallelogramma
  \coordinate (A) at (0,0);
  \coordinate (B) at (4,0);
  \coordinate (C) at (5,3);
  \coordinate (D) at (1,3);
  
  \draw[thick] (A) -- (B) -- (C) -- (D) -- cycle;
\end{tikzpicture}
\end{center}

\vspace{1em}

% Spiegazione e dimostrazione
In un parallelogramma, per definizione, i lati opposti sono paralleli. Tale proprietà implica che gli angoli interni opposti siano congruenti, ovvero, se indichiamo con \(A\), \(B\), \(C\) e \(D\) gli angoli interni, si ha:
\[
A = C \quad \text{e} \quad B = D.
\]
Poiché la somma degli angoli interni di ogni quadrilatero è \(360^\circ\), si ottiene:
\[
A + B + C + D = 360^\circ.
\]
Sostituendo \(C = A\) e \(D = B\) la relazione diventa:
\[
2A + 2B = 360^\circ \quad \Longrightarrow \quad A + B = 180^\circ.
\]
Pertanto, gli angoli adiacenti in un parallelogramma sono supplementari.

Questa proprietà ci permette di applicare le identità trigonometriche per angoli supplementari. Ad esempio, si sa che:
\[
\sin(180^\circ - \theta) = \sin\theta \quad \text{e} \quad \cos(180^\circ - \theta) = -\cos\theta.
\]
Supponiamo di voler esprimere il seno e il coseno di un angolo \(A\) sapendo che il suo supplementare è \(180^\circ - A\). Dalla relazione appena vista, si ottiene:
\[
\sin(180^\circ - A) = \sin A,\qquad \cos(180^\circ - A) = -\cos A.
\]
Queste formule possono risultare utili, ad esempio, nel calcolo di aree o nella risoluzione di problemi geometrici che coinvolgono parallelogrammi.

In sintesi, il parallelogramma, grazie alle proprietà dei triangoli che si formano dividendolo con una diagonale, dimostra che gli angoli interni sono tali che due a due sono uguali (angoli opposti) e, inoltre, ogni coppia di angoli adiacenti è supplementare (somma \(180^\circ\)). Le identità trigonometriche per angoli supplementari forniscono un ulteriore strumento per l'analisi e la risoluzione di problemi in geometria.


\newpage

\subsectionstar{[16] Formule di Prostaferesi}
\paragraph{Definizione delle Formule di Prostaferesi}  
Le formule di prostaferesi permettono di trasformare somme e differenze di funzioni trigonometriche in prodotti. Esse derivano direttamente dalle formule di somma e differenza degli angoli e sono le seguenti:

\medskip

\textbf{Per il seno:}
\[
\sin A + \sin B = 2 \sin\frac{A+B}{2}\cos\frac{A-B}{2},
\]
\[
\sin A - \sin B = 2 \cos\frac{A+B}{2}\sin\frac{A-B}{2}.
\]

\textbf{Per il coseno:}
\[
\cos A + \cos B = 2 \cos\frac{A+B}{2}\cos\frac{A-B}{2},
\]
\[
\cos A - \cos B = -2 \sin\frac{A+B}{2}\sin\frac{A-B}{2}.
\]

\bigskip

Per capire al meglio le formule di prostaferesi, piuttosto che vedere la loro dimostrazione, può aiutare al meglio vederle in pratica:

\noindent \textbf{Esempio 1:}  
Si consideri l'espressione
\[
\sin 75^\circ + \sin 15^\circ.
\]
Utilizzando la formula di prostaferesi per la somma dei seni,
\[
\sin A + \sin B = 2\sin\frac{A+B}{2}\cos\frac{A-B}{2},
\]
con \(A=75^\circ\) e \(B=15^\circ\) si ha:
\[
\frac{A+B}{2} = \frac{75^\circ+15^\circ}{2} = 45^\circ,\quad \frac{A-B}{2} = \frac{75^\circ-15^\circ}{2} = 30^\circ.
\]
Pertanto:
\[
\sin 75^\circ + \sin 15^\circ = 2\sin 45^\circ\,\cos 30^\circ.
\]
Sapendo che \(\sin 45^\circ = \frac{\sqrt{2}}{2}\) e \(\cos 30^\circ = \frac{\sqrt{3}}{2}\), si ottiene:
\[
\sin 75^\circ + \sin 15^\circ = 2\left(\frac{\sqrt{2}}{2}\right)\left(\frac{\sqrt{3}}{2}\right)=\frac{\sqrt{6}}{2}.
\]

\bigskip

\noindent \textbf{Esempio 2:}  
Si consideri l'espressione
\[
\cos 80^\circ - \cos 20^\circ.
\]
Utilizzando la formula di prostaferesi per la differenza dei coseni,
\[
\cos A - \cos B = -2\sin\frac{A+B}{2}\sin\frac{A-B}{2},
\]
con \(A=80^\circ\) e \(B=20^\circ\) si ha:
\[
\frac{A+B}{2} = \frac{80^\circ+20^\circ}{2} = 50^\circ,\quad \frac{A-B}{2} = \frac{80^\circ-20^\circ}{2} = 30^\circ.
\]
Pertanto:
\[
\cos 80^\circ - \cos 20^\circ = -2\sin 50^\circ\,\sin 30^\circ.
\]
Sapendo che \(\sin 30^\circ = \frac{1}{2}\), si ottiene:
\[
\cos 80^\circ - \cos 20^\circ = -2\sin 50^\circ\cdot\frac{1}{2} = -\sin 50^\circ.
\]

\bigskip
Per evdere un esempio un po' più complesso e che coinvolga diverse formule, consideriamo l'espressione
\[
E = \frac{\sin(3\theta) - \sin\theta}{\cos(3\theta) + \cos\theta}.
\]
Utilizziamo le formule di prostaferesi per trasformare somme e differenze in prodotti. In particolare, abbiamo:
\[
\sin(3\theta) - \sin\theta = 2\,\cos\frac{3\theta+\theta}{2}\,\sin\frac{3\theta-\theta}{2} = 2\cos(2\theta)\sin\theta,
\]
\[
\cos(3\theta) + \cos\theta = 2\,\cos\frac{3\theta+\theta}{2}\,\cos\frac{3\theta-\theta}{2} = 2\cos(2\theta)\cos\theta.
\]
Pertanto,
\[
E = \frac{2\cos(2\theta)\sin\theta}{2\cos(2\theta)\cos\theta} = \tan\theta.
\]
\newpage

\subsectionstar{[37] Teorema dei Seni e delle Proiezioni}
\paragraph{Teorema dei Seni}  
In ogni triangolo, i lati sono proporzionali ai seni degli angoli opposti, ossia:
\[
\frac{a}{\sin\alpha}=\frac{b}{\sin\beta}=\frac{c}{\sin\gamma},
\]
dove \(a\), \(b\) e \(c\) sono i lati del triangolo e \(\alpha\), \(\beta\) e \(\gamma\) sono gli angoli opposti.

\medskip

\begin{center}
\begin{tikzpicture}[scale=1.2]
  % Definizione dei vertici
  \coordinate (A) at (0,0);
  \coordinate (B) at (5,0);
  \coordinate (C) at (3,3);
  
  % Disegno del triangolo
  \draw[thick] (A) -- (B) -- (C) -- cycle;
  
  % Etichette dei vertici
  \node[below left] at (A) {\(A\)};
  \node[below right] at (B) {\(B\)};
  \node[above] at (C) {\(C\)};
  
  % Etichette dei lati
  \node at ($(B)!0.5!(C)+(0.4,0)$) {\(a\)};
  \node at ($(A)!0.5!(C)+(-0.4,0)$) {\(b\)};
  \node at ($(A)!0.5!(B)+(0,-0.4)$) {\(c\)};
  
  % Rappresentazione degli angoli con etichette (senza archi elaborati)
  \node at ($(A)+(0.6,0.2)$) {\(\alpha\)};
  \node at ($(B)+(-0.6,0.2)$) {\(\beta\)};
  \node at ($(C)+(0,-0.6)$) {\(\gamma\)};
\end{tikzpicture}
\end{center}

In altre parole, questo teorema stabilisce una relazione di proporzionalità tra ciascun lato e il seno dell'angolo opposto, permettendoci di comprendere in modo intuitivo come le lunghezze dei lati siano legate alle grandezze degli angoli. Tale proporzionalità ci fornisce uno strumento prezioso per risolvere triangoli, in quanto conoscendo alcuni elementi è possibile calcolare quelli mancanti, mantenendo costante il rapporto tra lati e seni degli angoli.

\noindent\textbf{Esempio:}  
Si consideri un triangolo in cui \(a=5\), \(\alpha=30^\circ\) e \(\beta=45^\circ\). Poiché, per il teorema dei seni,
\[
\frac{5}{\sin 30^\circ}=\frac{b}{\sin 45^\circ},
\]
e sapendo che \(\sin 30^\circ=\frac{1}{2}\) e \(\sin 45^\circ=\frac{\sqrt{2}}{2}\), si ottiene:
\[
\frac{5}{\frac{1}{2}}=\frac{b}{\frac{\sqrt{2}}{2}}\quad\Longrightarrow\quad 10=\frac{b}{\frac{\sqrt{2}}{2}},
\]
da cui:
\[
b=10\cdot\frac{\sqrt{2}}{2}=5\sqrt{2}.
\]
L'angolo \(\gamma\) si calcola come:
\[
\gamma=180^\circ-(30^\circ+45^\circ)=105^\circ.
\]

\begin{center}
\begin{tikzpicture}[scale=1.0]
  % Definizione dei vertici (le coordinate non sono esatte ma servono a scopo illustrativo)
  \coordinate (A) at (0,0);
  \coordinate (B) at (4,0);
  \coordinate (C) at (1.5,2.5);
  
  % Disegno del triangolo
  \draw[thick] (A) -- (B) -- (C) -- cycle;
  
  % Etichette dei vertici
  \node[below left] at (A) {\(A\)};
  \node[below right] at (B) {\(B\)};
  \node[above] at (C) {\(C\)};
  
  % Etichette degli angoli
  \node at ($(A)+(0.5,0.3)$) {\(30^\circ\)};
  \node at ($(B)+(-0.5,0.3)$) {\(45^\circ\)};
  \node at ($(C)+(0.1,-0.5)$) {\(\gamma\)};
  
  % Etichette dei lati (indicando solo i valori noti)
  % Il lato opposto ad A (BC) è etichettato come "a=5"
  \node at ($(B)!0.5!(C)+(0.4,0)$) {\(5\)};
  % Il lato opposto a B (AC) è etichettato come "b=5√2"
  \node at ($(A)!0.5!(C)+(-0.5,0)$) {\(5\sqrt{2}\)};
  % Lato c non è stato calcolato
  \node at ($(A)!0.5!(B)+(0,-0.3)$) {\(c\)};
\end{tikzpicture}
\end{center}

\subsectionstar{[38] Teorema di Carnot e delle Tangenti}
\paragraph{Teorema dei Coseni (di Carnot)}  
Il teorema dei coseni, spesso chiamato anche teorema dei coseni di Carnot, generalizza il teorema di Pitagora a ogni triangolo. Esso afferma che in un triangolo, la lunghezza di un lato elevato al quadrato è data dalla somma dei quadrati degli altri due lati, meno il doppio prodotto di questi ultimi per il coseno dell'angolo compreso tra di essi. In formula:
\[
a^2 = b^2 + c^2 - 2\,b\,c\,\cos\alpha,
\]
dove \(a\) è il lato opposto all'angolo \(\alpha\). Le formule analoghe valgono ciclicamente per gli altri lati. Quando \(\alpha=90^\circ\) si ha \(\cos 90^\circ=0\), e la formula si riduce al teorema di Pitagora:
\[
a^2 = b^2 + c^2.
\]

\medskip

\begin{center}
\begin{tikzpicture}[scale=1.2]
  % Definizione dei vertici (coordinate indicative)
  \coordinate (A) at (0,0);
  \coordinate (B) at (5,0);
  \coordinate (C) at (2,3);
  
  % Disegno del triangolo
  \draw[thick] (A) -- (B) -- (C) -- cycle;
  
  % Etichette dei vertici
  \node[below left] at (A) {\(A\)};
  \node[below right] at (B) {\(B\)};
  \node[above] at (C) {\(C\)};
  
  % Lati etichettati
  \node at ($(B)!0.5!(C)$) [right] {\(a\)};
  \node at ($(A)!0.5!(C)$) [left] {\(b\)};
  \node at ($(A)!0.5!(B)$) [below] {\(c\)};
  
  % Indicazione dell'angolo \(\alpha\) in A
  \node at ($(A)+(0.6,0.3)$) {\(\alpha\)};
\end{tikzpicture}
\end{center}
 
Il teorema dei coseni (di Carnot) stabilisce una relazione \q{proporzionale} tra i lati di un triangolo e il coseno dell'angolo compreso tra essi. In pratica, esso ci dice come il "bilanciamento" delle lunghezze dei lati dipenda dall'ampiezza dell'angolo. Questa relazione diventa particolarmente evidente quando, per un angolo retto, il termine contenente il coseno scompare, riproducendo così il teorema di Pitagora. Quindi, il teorema dei coseni spiega l'equilibrio geometrico del triangolo anche quando non è presente un angolo retto, ed è fondamentale per risolvere triangoli in situazioni dove i dati a disposizione non sono sufficienti per applicare direttamente il teorema dei seni.

 
\noindent \textbf{Esempio:} Supponiamo di avere un triangolo con \(b=8\), \(c=10\) e l'angolo compreso \(\alpha=60^\circ\). Utilizziamo il teorema dei coseni per determinare \(a\):
\[
a^2 = 8^2 + 10^2 - 2\cdot8\cdot10\cos60^\circ.
\]
Sapendo che \(\cos60^\circ=0.5\), calcoliamo:
\[
a^2 = 64 + 100 - 160\cdot0.5 = 164 - 80 = 84,
\]
quindi:
\[
a = \sqrt{84} \approx 9.17.
\]
Questo esempio mostra come, conoscendo due lati e l'angolo compreso, il teorema dei coseni permetta di determinare il lato rimanente.

\paragraph{Teorema delle Tangenti}  
Il teorema delle tangenti per i triangoli stabilisce una relazione tra la differenza e la somma di due lati e le tangenti delle metà degli angoli opposti a tali lati. In particolare, se \(a\) e \(b\) sono due lati di un triangolo e \(\alpha\) e \(\beta\) sono gli angoli opposti rispettivamente, il teorema afferma che
\[
\frac{a - b}{a + b} = \frac{\tan\frac{1}{2}(\alpha - \beta)}{\tan\frac{1}{2}(\alpha + \beta)}.
\]
Questa relazione è molto utile perché permette di determinare informazioni sugli angoli del triangolo a partire dalle misure dei lati (o viceversa) ed è spesso impiegata insieme al teorema dei seni e al teorema dei coseni nella risoluzione completa del triangolo.

\medskip

Il teorema evidenzia come la variazione tra due lati (\(a-b\)) rispetto alla loro somma (\(a+b\)) sia correlata alle tangenti delle metà della differenza e della somma degli angoli opposti. In altre parole, se conosciamo la differenza tra due lati, possiamo dedurre la differenza tra gli angoli opposti (e viceversa) mediante le funzioni tangente applicate a metà angoli. Questa relazione fornisce una chiave intuitiva per comprendere la proporzionalità interna del triangolo e, in particolare, come le variazioni nei lati siano riflesse nei corrispondenti angoli.

\medskip

\begin{center}
\begin{tikzpicture}[scale=1.0]
  % Definizione dei vertici del triangolo
  \coordinate (A) at (0,0);
  \coordinate (B) at (5,0);
  \coordinate (C) at (2,3);
  
  % Disegno del triangolo
  \draw[thick] (A) -- (B) -- (C) -- cycle;
  
  % Etichette dei vertici
  \node[below left] at (A) {\(A\)};
  \node[below right] at (B) {\(B\)};
  \node[above] at (C) {\(C\)};
  
  % Etichette dei lati: 
  \node at ($(B)!0.5!(C)$) [right] {\(a\)};
  \node at ($(A)!0.5!(C)$) [left] {\(b\)};
  % Il lato opposto al vertice C è indicato come c (non necessario per questo teorema)
  
  % Indicazione degli angoli in A e B (quelli relativi a lati a e b)
  \node at ($(A)+(0.6,0.3)$) {\(\alpha\)};
  \node at ($(B)+(-0.6,0.3)$) {\(\beta\)};
\end{tikzpicture}
\end{center}

\medskip

\noindent\textbf{Esempio:}  
Si consideri un triangolo in cui \(a=8\), \(b=4\), \(\alpha=90^\circ\) e \(\beta=30^\circ\).  
Calcoliamo il rapporto dei lati:
\[
\frac{a-b}{a+b}=\frac{8-4}{8+4}=\frac{4}{12}=\frac{1}{3}.
\]
Calcoliamo ora le tangenti delle metà degli angoli:
\[
\tan\frac{(\alpha-\beta)}{2}=\tan\frac{90^\circ-30^\circ}{2}=\tan 30^\circ=\frac{1}{\sqrt{3}},
\]
\[
\tan\frac{(\alpha+\beta)}{2}=\tan\frac{90^\circ+30^\circ}{2}=\tan 60^\circ=\sqrt{3}.
\]
Pertanto il rapporto delle tangenti risulta:
\[
\frac{\tan 30^\circ}{\tan 60^\circ}=\frac{\frac{1}{\sqrt{3}}}{\sqrt{3}}=\frac{1}{3},
\]
in perfetta corrispondenza con il rapporto calcolato dai lati.

\begin{center}
\begin{tikzpicture}[scale=1.0]
  % Definizione dei vertici:
  % Poniamo il vertice A come angolo retto, B come angolo di 30° e C come angolo di 60°.
  \coordinate (A) at (0,0);
  % Nel triangolo 30-60-90, la relazione è: lato opposto a 30° = 4, ipotenusa = 8, lato opposto a 60° = 4√3.
  \coordinate (B) at (4*1.732,0); % 4√3 ≈ 6.928
  \coordinate (C) at (0,4);
  
  % Disegno del triangolo
  \draw[thick] (A) -- (B) -- (C) -- cycle;
  
  % Etichette dei vertici
  \node[below left] at (A) {\(A\)};
  \node[below right] at (B) {\(B\)};
  \node[above left] at (C) {\(C\)};
  
  % Etichette dei lati
  % Lato opposto ad A (BC) è l'ipotenusa a=8
  \node at ($(B)!0.5!(C)$) [above] {\(8\)};
  % Lato opposto a B (AC) è il lato b=4 (più corto)
  \node at ($(A)!0.5!(C)$) [left] {\(4\)};
  % Lato opposto a C (AB) è il lato c=4√3
  \node at ($(A)!0.5!(B)$) [below] {\(4\sqrt{3}\)};
  
  % Etichette degli angoli
  \node at ($(A)+(0.5,0.3)$) {\(90^\circ\)};
  \node at ($(B)+(-0.8,0.3)$) {\(30^\circ\)};
  \node at ($(C)+(-0.5,-0.3)$) {\(60^\circ\)};
\end{tikzpicture}
\end{center}

\textbf{NB}: Anche il teorema delle tangenti si applica in casi generali, nel caso sopra lo vediamo applicato ad un triangolo rettangolo per far sì che i calcoli tornassero semplici e venissero utilizzati i valori noti della tangente.
\newpage

\subsectionstar{[17] Formule di Addizione degli Archi}  
La lunghezza \(L\) di un arco in un cerchio di raggio \(r\) è data dalla relazione
\[
L=r\theta,
\]
dove \(\theta\) è l'angolo sotteso dall'arco, misurato in radianti. Da questa definizione, se due archi hanno angoli \(\theta_1\) e \(\theta_2\), allora l'arco corrispondente alla somma degli angoli ha lunghezza:
\[
L_{\theta_1+\theta_2}=r(\theta_1+\theta_2)=r\theta_1+r\theta_2=L_{\theta_1}+L_{\theta_2}.
\]
Vediamo ora raffigurato un esempio in cui abbiamo i due angoli $\theta_1 $ e $\theta_2$ ed i rispettivi archi, in questo caso abbiamo presto $\theta_1 = 40^\circ $ e $\theta_2 = 60^\circ$. La formula presentata sopra ci permette quindi di calcolare, dati $\theta_1$ e $\theta_2$, la lunghezza dell'arco compreso da entrambi gli angoli assieme, il che equivale all'arco compreso da $\theta_3 = 100^\circ$. È importante ricordare che, per poter usare la formula, è opportuno misurare gli angoli in radianti, sotto la figura vediamo come procedere.
\medskip

\begin{center}
\begin{tikzpicture}[scale=1.0]
  % Centro e cerchio
  \coordinate (O) at (0,0);
  \draw[thick] (O) circle (2.5);
  \node at (O) [below left] {\(O\)};

  % Raggi dal centro per gli angoli 0°, 40° e 100°
  \draw[->, thick] (O) -- (2.5,0) node[midway, below] {0°};
  \draw[->, thick] (O) -- ({2.5*cos(40)},{2.5*sin(40)}) node[midway, above left] {40°};
  \draw[->, thick] (O) -- ({2.5*cos(100)},{2.5*sin(100)}) node[midway, above left] {100°};

  % Arco 1: da 0° a 40° (in rosso)
  \draw[red, very thick] (2.5,0) arc (0:40:2.5);
  \node at ($(O)+(1.8,0.6)$) {\(\theta_1\)};

  % Arco 2: da 40° a 100° (in blu)
  \draw[blue, very thick] ({2.5*cos(40)},{2.5*sin(40)}) arc (40:100:2.5);
  \node at ($(O)+(1.0,1.8)$) {\(\theta_2\)};
\end{tikzpicture}
\end{center}

\medskip

Quanto ci interessa al fine di questa sezione però, non è tanto l'aspetto geometrico della somma di archi che abbiamo visto qua sopra, ci interessa invece vedere che implicazioni questo ha sulle funzioni goniometriche che abbiamo visto. 

Per determinare le funzioni trigonometriche dell'angolo totale \(\theta_1+\theta_2\), usiamo infatti le seguenti formule di addizione:
\[
\sin(\theta_1+\theta_2)=\sin\theta_1\cos\theta_2+\cos\theta_1\sin\theta_2,
\]
\[
\cos(\theta_1+\theta_2)=\cos\theta_1\cos\theta_2-\sin\theta_1\sin\theta_2,
\]
\[
\tan(\theta_1+\theta_2)=\frac{\tan\theta_1+\tan\theta_2}{1-\tan\theta_1\tan\theta_2}.
\]
Queste relazioni permettono di calcolare direttamente, ad esempio, il seno, il coseno e la tangente dell'angolo ottenuto dalla somma dei due archi, facilitando la risoluzione di problemi che coinvolgono il settore circolare.

\medskip

\paragraph{Esempio}  
Supponiamo di avere due archi in un cerchio di raggio \(r=5\), il che vedremo risultare irrilevante, corrispondenti agli angoli
\[
\theta_1=40^\circ \quad \text{e} \quad \theta_2=60^\circ.
\]
Convertendo in radianti:
\[
\theta_1=\frac{40\pi}{180}=\frac{2\pi}{9},\qquad \theta_2=\frac{60\pi}{180}=\frac{\pi}{3}.
\]
L'angolo totale è
\[
\theta_1+\theta_2 = \frac{2\pi}{9}+\frac{\pi}{3} = \frac{2\pi}{9}+\frac{3\pi}{9}=\frac{5\pi}{9}.
\]
Utilizzando la formula di addizione per il seno, otteniamo:
\[
\sin\left(\frac{5\pi}{9}\right)=\sin\left(\frac{2\pi}{9}+\frac{\pi}{3}\right)
=\sin\frac{2\pi}{9}\cos\frac{\pi}{3}+\cos\frac{2\pi}{9}\sin\frac{\pi}{3}.
\]
Sapendo che \(\cos\frac{\pi}{3}=\frac{1}{2}\) e \(\sin\frac{\pi}{3}=\frac{\sqrt{3}}{2}\), l'espressione ci permette di esprimere \(\sin\left(\frac{5\pi}{9}\right)\) in funzione di \(\sin\frac{2\pi}{9}\) e \(\cos\frac{2\pi}{9}\).  
Analoghe formule valgono per il coseno e la tangente dell'angolo totale.

Queste formule sono fondamentali perché collegano direttamente la somma degli archi (ossia, la somma degli angoli al centro) con le funzioni trigonometriche, facilitando il calcolo delle proprietà geometriche dei settori circolari e la risoluzione di problemi legati ai cerchi.

\iffalse
\noindent\textbf{Esempio}  
Consideriamo un cerchio di raggio \(r=5\). Se si considerano due archi con angoli
\[
\theta_1=40^\circ\quad\text{e}\quad \theta_2=60^\circ,
\]
convertendo in radianti:
\[
\theta_1=\frac{40\pi}{180}=\frac{2\pi}{9},\qquad \theta_2=\frac{60\pi}{180}=\frac{\pi}{3},
\]
allora la lunghezza dell'arco corrispondente a \(\theta_1\) è:
\[
L_1=5\cdot\frac{2\pi}{9}=\frac{10\pi}{9},
\]
quella per \(\theta_2\) è:
\[
L_2=5\cdot\frac{\pi}{3}=\frac{5\pi}{3},
\]
e l'arco risultante dalla somma degli angoli, \(\theta_1+\theta_2=\frac{2\pi}{9}+\frac{\pi}{3}=\frac{2\pi}{9}+\frac{3\pi}{9}=\frac{5\pi}{9}\), ha lunghezza:
\[
L_{\theta_1+\theta_2}=5\cdot\frac{5\pi}{9}=\frac{25\pi}{9}.
\]
Notiamo che:
\[
L_{\theta_1+\theta_2}=L_1+L_2,
\]
il che conferma la linearità della lunghezza dell'arco rispetto all'angolo sotteso.
\fi

\paragraph{Area del Settore Circolare}  
L'area \(A\) di un settore circolare in un cerchio di raggio \(r\) è data dalla formula
\[
A = \frac{1}{2} r^2 \theta,
\]
dove \(\theta\) è l'angolo al centro, misurato in radianti. Questa formula indica che l'area del settore varia linearmente con l'angolo sotteso.

\medskip

\begin{center}
\begin{tikzpicture}[scale=1.0]
  % Centro del cerchio
  \coordinate (O) at (0,0);
  \draw[thick] (O) circle (2.5);
  \node at (O) [below left] {\(O\)};
  
  % Raggi dal centro per gli angoli 0°, 40° e 100°
  \draw[-, thick] (O) -- (2.5,0) node[midway, below] {0°};
  \draw[-, thick] (O) -- ({2.5*cos(40)},{2.5*sin(40)}) node[midway, above left] {40°};
  \draw[-, thick] (O) -- ({2.5*cos(100)},{2.5*sin(100)}) node[midway, above left] {100°};
  
  % Settore 1: da 0° a 40° (riempito in rosso chiaro)
  \fill[red!30] (O) -- (2.5,0) arc (0:40:2.5) -- cycle;
  \node at ($(O)+(1.8,0.6)$) {\(\theta_1\)};
  
  % Settore 2: da 40° a 100° (riempito in blu chiaro)
  \fill[blue!30] (O) -- ({2.5*cos(40)},{2.5*sin(40)}) arc (40:100:2.5) -- cycle;
  \node at ($(O)+(1.0,1.8)$) {\(\theta_2\)};
\end{tikzpicture}
\end{center}

\medskip

\noindent\textbf{Esempio:}  
Consideriamo un cerchio di raggio \(r=5\). Supponiamo di avere due settori con angoli
$\theta_1=40^\circ$ e $\theta_2=60^\circ$. Convertiamo gli angoli in radianti:
\[
\theta_1=\frac{40\pi}{180}=\frac{2\pi}{9},\qquad \theta_2=\frac{60\pi}{180}=\frac{\pi}{3}.
\]
L'area del settore per \(\theta_1\) è:
\[
A_1 = \frac{1}{2} \cdot 5^2 \cdot \frac{2\pi}{9} = \frac{25\pi}{9},
\]
mentre l'area del settore per \(\theta_2\) è:
\[
A_2 = \frac{1}{2} \cdot 25 \cdot \frac{\pi}{3} = \frac{25\pi}{6}.
\]
La somma degli angoli è \(\theta_3=\theta_1+\theta_2\). Convertendo,  
\[
\theta_3 = \frac{2\pi}{9}+\frac{\pi}{3} = \frac{2\pi}{9}+\frac{3\pi}{9}=\frac{5\pi}{9},
\]
e l'area del settore corrispondente è:
\[
A_{\theta_3} = \frac{1}{2} \cdot 25 \cdot \frac{5\pi}{9} = \frac{125\pi}{18}.
\]

\newpage

\subsectionstar{[15] Formule di Duplicazione degli Archi}
\paragraph{Formule di Duplicazione}  
Le formule di duplicazione permettono di esprimere il valore di una funzione trigonometrica per l'angolo doppio in funzione del valore della funzione per l'angolo singolo.

\begin{center}
\begin{tikzpicture}[scale=1.0]
  % Centro del cerchio
  \coordinate (O) at (0,0);
  \draw[thick] (O) circle (2.5);
  \node at (O) [below left] {\(O\)};
  
  % Raggi dal centro per 0°, 60° e 120°
  \draw[->, thick] (O) -- (2.5,0) node[midway, below] {0°};
  \draw[->, thick] (O) -- ({2.5*cos(60)},{2.5*sin(60)}) node[midway, below right] {\(60^\circ\)};
  \draw[->, thick] (O) -- ({2.5*cos(120)},{2.5*sin(120)}) node[midway, above left] {\(120^\circ\)};
  
  % Arco per l'angolo di 60° (in rosso)
  \draw[red, very thick] (2.5,0) arc (0:60:2.5);
  \node at ($(O)+(1.5,1.0)$) {};
  
  % Arco per l'angolo di 120° (in blu)
  \draw[blue, very thick] (2.5,0) arc (0:120:2.5);
  \node at ($(O)+(1.8,1.4)$) {};
\end{tikzpicture}
\end{center}

\subsubsection*{Seno}  
La formula per il seno dell'angolo doppio è
\[
\sin(2\theta)=2\sin\theta\,\cos\theta.
\]

\noindent \textbf{Esempio}  
Calcoliamo \(\sin(2\theta)\) per \(\theta=30^\circ\).  
Convertendo in radianti: \(\theta=\frac{\pi}{6}\). Quindi:
\[
\sin(2\theta)=2\sin\frac{\pi}{6}\,\cos\frac{\pi}{6}=2\left(\frac{1}{2}\right)\left(\frac{\sqrt{3}}{2}\right)=\frac{\sqrt{3}}{2}.
\]

\subsubsection*{Coseno}  
Esistono tre forme equivalenti per il coseno dell'angolo doppio:
\[
\cos(2\theta)=\cos^2\theta-\sin^2\theta,
\]
\[
\cos(2\theta)=2\cos^2\theta-1,
\]
\[
\cos(2\theta)=1-2\sin^2\theta.
\]

\noindent \textbf{Esempio}  
Per \(\theta=30^\circ\) (\(\theta=\frac{\pi}{6}\)), usando la prima formula:
\[
\cos(2\theta)=\cos^2\frac{\pi}{6}-\sin^2\frac{\pi}{6}=\left(\frac{\sqrt{3}}{2}\right)^2-\left(\frac{1}{2}\right)^2=\frac{3}{4}-\frac{1}{4}=\frac{1}{2}.
\]

\subsubsection*{Tangente}  
La formula per la tangente dell'angolo doppio è:
\[
\tan(2\theta)=\frac{2\tan\theta}{1-\tan^2\theta}.
\]

\noindent \textbf{Esempio}  
Per \(\theta=30^\circ\) (con \(\tan 30^\circ=\frac{1}{\sqrt{3}}\)):
\[
\tan(2\theta)=\frac{2\cdot\frac{1}{\sqrt{3}}}{1-\left(\frac{1}{\sqrt{3}}\right)^2}=\frac{\frac{2}{\sqrt{3}}}{1-\frac{1}{3}}=\frac{\frac{2}{\sqrt{3}}}{\frac{2}{3}}=\frac{2}{\sqrt{3}}\cdot\frac{3}{2}=\sqrt{3}.
\]
\newpage

\subsectionstar{[13*] Sistemi di Equazioni Goniometriche} 
Quando si risolvono sistemi di equazioni che coinvolgono funzioni trigonometriche, è fondamentale utilizzare le identità (teorema dei seni, teorema dei coseni, formule di somma e sottrazione, duplicazione, prostaferesi, teorema delle tangenti, ecc.) studiate in precedenza. Poiché le funzioni trigonometriche sono periodiche, ogni soluzione viene espressa in forma generale aggiungendo un termine periodico, ad esempio
\[
x = x_0 + 2\pi n,\quad n\in\mathbb{Z},
\]
che garantisce la completezza del risultato.

Per sviluppare un'intuizione di quale sia la forma che un valore deve avere per poter essere una soluzione di un'equazione goniometrica, prendiamo due esempi e rappresentiamoli sul cerchio unitario.

Consideriamo una equazione trigonometrica il cui insieme delle soluzioni è dato da
\[
x = \frac{\pi}{3} + 2\pi n \quad \text{oppure} \quad x = \left(2+\frac{\pi}{5}\right) + 2\pi n,\quad n\in\mathbb{Z}.
\]

Notiamo ora che rappresentare questi numeri, come saremo abituati in algebra, non è più il metodo più efficiente, o dovremmo rappresentare un'infinità di punti. Vediamo infatti:

\begin{center}
\begin{tikzpicture}[scale=1.0]
  % Disegno della linea numerica da 0 a 10
  \draw[<->, thick] (0,0) -- (10,0) node[right] {\(x\)};
  
  % Ticks e etichette per ogni intero da 0 a 10
  \foreach \x in {0,1,...,10} {
    \draw (\x,0.1) -- (\x,-0.1) node[below] {\(\x\)};
  }
  
  % Soluzione 1: x = π/3 ≈ 1.05 (in rosso)
  \coordinate (P1) at (1.05,0);
  \draw[red, fill=red] (P1) circle (2pt) node[above] {\(\frac{\pi}{3}\)};
  
  % Soluzione 2: x = 2+π/5 ≈ 2.63 (in blu)
  \coordinate (P2) at (2.63,0);
  \draw[blue, fill=blue] (P2) circle (2pt) node[above] {\(2+\frac{\pi}{5}\)};
  
  % Soluzioni ripetute aggiungendo il periodo 2π ≈ 6.28
  \coordinate (P1r) at (1.05+6.28,0); % ~7.33
  \coordinate (P2r) at (2.63+6.28,0); % ~8.91
  \draw[red, fill=red] (P1r) circle (2pt) node[above] {\(\frac{\pi}{3}+2\pi\)};
  \draw[blue, fill=blue] (P2r) circle (2pt) node[above] {\(2+\frac{\pi}{5}+2\pi\)};
\end{tikzpicture}
\end{center}

Come se dovessi rappresentare le ore 10:15, non ci importa notare quante volte questo valore si ripete al ripetersi dei giorni, ma ci interessa invece considerare i giorni come una linea chiusa che unisce le 23:59 del giorno precedente con le 00:00 di quello successivo. Similmente rappersentiamo i valori trigonometrici nel cerchio unitario:

\begin{center}
\begin{tikzpicture}[scale=1.0]
  % Disegno del cerchio unitario
  \draw[thick] (0,0) circle (2.5);
  \coordinate (O) at (0,0);
  \node at (O) [below left] {\(O\)};
  
  % Calcolo delle coordinate per x = π/3 (60°) e x = 2+π/5 (150.6°)
  \coordinate (P1) at ({2.5*cos(60)},{2.5*sin(60)});
  \coordinate (P2) at ({2.5*cos(150.6)},{2.5*sin(150.6)});
  
  % Disegno dei raggi corrispondenti
  \draw[-, thick] (O) -- (P1) node[midway, above right] {};
  \draw[-, thick] (O) -- (P2) node[midway, above left] {};
  
  % Evidenziazione dei punti (soluzioni principali)
  \fill[red] (P1) circle (3pt) node[right] {\(\frac{\pi}{3}\)};
  \fill[blue] (P2) circle (3pt) node[left] {\(2+\frac{\pi}{5}\)};
  
  % Disegno dell'arco completo (dashed) per rappresentare il periodo 2π
  \draw[dashed] (2.5,0) arc (0:360:2.5);
\end{tikzpicture}
\end{center}

Detto questo, l'unica altra componente di teoria necessaria per proter procedere, oltre a tutte le equazioni goniometriche viste fin'ora, è capire cosa significhi mettere delle equazioni a sistema. Quando mettiamo delle equazioni a sistema stiamo cercando quei valori che risolvono \textit{sia} la prima \textit{che} la seconda equazione coinvolta, e similmente per ciasun'altra equazione nel sistema. Questo significa che le soluzioni del sistema saranno l'intersezione delle soluzioni di ciascuna delle equazioni cha abbiamo messo a sistema. Per mettere in pratica questa nozione, vediamo un esempio e la rispettiva figura.

Consideriamo il seguente sistema:
\[
\begin{cases}
\sin x = \frac{1}{2},\\[1mm]
\cos x = \frac{\sqrt{3}}{2}.
\end{cases}
\]
Sappiamo che l'equazione \(\sin x = \frac{1}{2}\) ha soluzioni generali (nell'intervallo \([0, 2\pi)\)):
\[
x = \frac{\pi}{6}\quad\text{oppure}\quad x = \frac{5\pi}{6},
\]
mentre l'equazione \(\cos x = \frac{\sqrt{3}}{2}\) ha soluzioni:
\[
x = \frac{\pi}{6}\quad\text{oppure}\quad x = \frac{11\pi}{6}.
\]
Il sistema, dunque, ammette come soluzione comune \(x=\frac{\pi}{6}\).

\begin{center}
\begin{tikzpicture}[scale=1.2]
  % Disegno del cerchio unitario con raggio 2.5
  \coordinate (O) at (0,0);
  \draw[thick] (O) circle (2.5);
  \node at (O) [below left] {\(O\)};
  
  % Soluzioni per sin x = 1/2 (in rosso)
  \coordinate (P1) at ({2.5*cos(30)},{2.5*sin(30)});
  \coordinate (P2) at ({2.5*cos(150)},{2.5*sin(150)});
  \fill[red] (P1) circle (3pt) node[above right] {\(x=\frac{\pi}{6}\)};
  \fill[red] (P2) circle (3pt) node[above left] {\(x=\frac{5\pi}{6}\)};
  
  % Soluzioni per cos x = √3/2 (in blu)
  \coordinate (P3) at ({2.5*cos(30)},{2.5*sin(30)}); % coincide con P1
  \coordinate (P4) at ({2.5*cos(330)},{2.5*sin(330)});
  \fill[blue] (P3) circle (3pt) node[below right] {\(x=\frac{\pi}{6}\)};
  \fill[blue] (P4) circle (3pt) node[below left] {\(x=\frac{11\pi}{6}\)};
  \fill[purple] (P3) circle (3pt) node[below right] {};
\end{tikzpicture}
\end{center}

Vediamo quindi nella figura che l'unico valore che andremo a prendere è proprio quello che risolve entrambe le equazioni, ossia quello segnato in viola. Sistemi di equazioni goniometriche veri e propri possono richiedere per la soluzione ognuna dei risultati goniometrici che abbiamo visto in questa sezione, è quindi necessario avere confidenza con la tabella menzionata sopra per poterli risolvere. Consideriamo il sistema di disequazioni
\[
\begin{cases}
\sin 2x \le -\frac{1}{2}, \\
\cos x \ge \frac{1}{2}.
\end{cases}
\]
L'equazione \(\sin 2x = -\frac{1}{2}\) ha soluzioni \(2x=\frac{7\pi}{6}+2\pi k\) e \(2x=\frac{11\pi}{6}+2\pi k\) (con \(k\in\mathbb{Z}\)); poiché la funzione \(\sin 2x\) è monotona nel tratto \(\left[\frac{7\pi}{6},\,\frac{11\pi}{6}\right]\), la disequazione \(\sin 2x \le -\frac{1}{2}\) è verificata per 
\[
2x\in\left[\frac{7\pi}{6},\,\frac{11\pi}{6}\right]+2\pi k\quad\Longrightarrow\quad x\in\left[\frac{7\pi}{12},\,\frac{11\pi}{12}\right]+\pi k.
\]
La disequazione \(\cos x \ge \frac{1}{2}\) è soddisfatta in \([0,2\pi]\) per
\[
x\in \left[0,\frac{\pi}{3}\right] \cup \left[\frac{5\pi}{3},2\pi\right].
\]
Per \(k=0\) l'intervallo \(x\in\left[\frac{7\pi}{12},\,\frac{11\pi}{12}\right]\) (circa \([1.833,\,2.879]\)) non interseca gli intervalli di \(\cos x \ge \frac{1}{2}\). Per \(k=1\), invece, abbiamo
\[
x\in\left[\frac{7\pi}{12}+\pi,\frac{11\pi}{12}+\pi\right] = \left[\frac{19\pi}{12},\,\frac{23\pi}{12}\right],
\]
che, poiché \(\frac{19\pi}{12}\approx 4.974\) e \(\frac{23\pi}{12}\approx 6.021\), interseca l'intervallo \(\left[\frac{5\pi}{3},2\pi\right]\) (ovvero \([5.236,6.283]\)). L'intersezione esatta è
\[
x\in\left[\frac{5\pi}{3},\,\frac{23\pi}{12}\right].
\]
Pertanto, la soluzione generale del sistema è:
\[
x \in \left[\frac{5\pi}{3}+2\pi n,\frac{23\pi}{12}+2\pi n\right],\quad n\in\mathbb{Z}.
\]
\newpage

\subsectionstar{[17*] Formule di Briggs}
Sia \(ABC\) un triangolo con lati \(a,b,c\) e semiperimetro \(p=\frac{a+b+c}{2}\). Indichiamo con \(\alpha\) l'angolo opposto al lato \(a\), con \(\beta\) l'angolo opposto al lato \(b\) e con \(\gamma\) l'angolo opposto al lato \(c\); vedi la figura in basso. Le Formule di Briggs permettono di calcolare i valori di \(\sin\frac{\alpha}{2}\), \(\cos\frac{\alpha}{2}\), \(\tan\frac{\alpha}{2}\) (e analogamente per \(\beta\) e \(\gamma\)) unicamente a partire dalle misure dei lati \(a,b,c\).

\medskip

\begin{center}
\begin{tabular}{|c|c|c|c|}
\hline
\textbf{Angolo} & \(\sin\frac{\theta}{2}\) & \(\cos\frac{\theta}{2}\) & \(\tan\frac{\theta}{2}\) \\
\hline
\(\alpha\) 
& \(\displaystyle \sqrt{\frac{(p-b)(p-c)}{b\,c}}\) 
& \(\displaystyle \sqrt{\frac{p\,(p-a)}{b\,c}}\) 
& \(\displaystyle \sqrt{\frac{(p-b)(p-c)}{p\,(p-a)}}\) \\
\hline
\(\beta\) 
& \(\displaystyle \sqrt{\frac{(p-a)(p-c)}{a\,c}}\) 
& \(\displaystyle \sqrt{\frac{p\,(p-b)}{a\,c}}\) 
& \(\displaystyle \sqrt{\frac{(p-a)(p-c)}{p\,(p-b)}}\) \\
\hline
\(\gamma\) 
& \(\displaystyle \sqrt{\frac{(p-a)(p-b)}{a\,b}}\) 
& \(\displaystyle \sqrt{\frac{p\,(p-c)}{a\,b}}\) 
& \(\displaystyle \sqrt{\frac{(p-a)(p-b)}{p\,(p-c)}}\) \\
\hline
\end{tabular}
\end{center}

\begin{center}
\begin{tikzpicture}[scale=1.0]
  % Definizione dei vertici del triangolo
  \coordinate (A) at (0,0);
  \coordinate (B) at (5,0);
  \coordinate (C) at (3,3);

  % Disegno del triangolo
  \draw[thick] (A) -- (B) -- (C) -- cycle;
  
  % Etichette dei vertici
  \node[below left] at (A) {\(A\)};
  \node[below right] at (B) {\(B\)};
  \node[above] at (C) {\(C\)};
  
  % Etichette dei lati
  % Lato BC = a
  \node at ($(B)!0.5!(C) + (0.4,0)$) {\(a\)};
  % Lato AC = b
  \node at ($(A)!0.5!(C) + (-0.4,0)$) {\(b\)};
  % Lato AB = c
  \node at ($(A)!0.5!(B) + (0,-0.3)$) {\(c\)};
  
  % Etichette degli angoli (senza archi)
  % L'angolo opposto al lato a (in C) = alpha
  \node at ($(C)+(-0.0,-0.5)$) {\(\alpha\)};
  % L'angolo opposto al lato b (in B) = beta
  \node at ($(B)+(-0.5,0.2)$) {\(\beta\)};
  % L'angolo opposto al lato c (in A) = gamma
  \node at ($(A)+(0.6,0.2)$) {\(\gamma\)};
\end{tikzpicture}
\end{center}

Dal punto di vista mnemonico, inoltre, \(\sin\frac{\alpha}{2}\), \(\cos\frac{\alpha}{2}\) e \(\tan\frac{\alpha}{2}\) presentano strutture simili, differendo sostanzialmente per la disposizione dei fattori \((p-a)\), \((p-b)\) e \((p-c)\) a numeratore e denominatore, e per la presenza di \(p\) o di \(bc\) (e analoghi per \(\beta\) e \(\gamma\)). È dunque sufficiente concentrarsi sulle tre formule iniziali per \(\alpha\) — rispettivamente per \(\sin\frac{\alpha}{2}\), \(\cos\frac{\alpha}{2}\), \(\tan\frac{\alpha}{2}\) — per poi \textit{adattarle} a \(\beta\) e \(\gamma\). Questo approccio riduce drasticamente la quantità di formule da tenere a mente. 

Notiamo inoltre che, per come le abbiamo scritte, le formule di Briggs non ci portano ancora a calcolare il valore di $\sin \theta$ per un qualche angolo interno del triangolo, ma ci portano soo a calcolare il valore di $\sin \theta$, lo stesso vale anche per $\cos$ e $\tan$. Infatti notiamo che un secondo passaggio è necessario per poter giungere al valore desiderato, ossia l'applicazione delle formule di duplicazione. Utilizzieremo infatti le formule:   
\[
    \sin\alpha = 2\,\sin\frac{\alpha}{2}\,\cos\frac{\alpha}{2},\quad
    \cos\alpha = \cos^2\frac{\alpha}{2} - \sin^2\frac{\alpha}{2},\quad
    \tan\alpha = \frac{2\,\tan\frac{\alpha}{2}}{1 - \tan^2\frac{\alpha}{2}}.
\]
Notiamo che grazie alle formule di Briggs possiamo calcolare, partendosolo dalla lunghezza dei lati, tutto quello che sta alla destra dell'uguale, ed a questo modo riusciremo a calcolare $\sin \theta$, $\cos \theta$ e $\tan \theta$ per ognuno degli angoli interni. È però importante notare che per poter calcolare, ad esempio, $\sin \alpha$ sarà necessario eseguire non solo la formula di Briggs per il seno, ma anche quella per il coseno. Vediamo qualche esempio per mettere in pratica queste nozioni.

\bigskip

\noindent \textbf{Esempio}
Si consideri un triangolo con lati \(a=5\), \(b=3\) e \(c=4\), in cui \(a\) è la lunghezza della diagonale (ipotenusa), \(b\) e \(c\) i cateti. Siano \(\alpha\) l’angolo opposto ad \(a\), \(\beta\) quello opposto a \(b\) e \(\gamma\) quello opposto a \(c\). Il semiperimetro risulta \(p=\tfrac{a+b+c}{2}=6\). Nel disegno seguente, il punto \(A\) è \((0,0)\), il punto \(B\) è \((4,0)\) e il punto \(C\) è \((4,3)\). In questo modo, il lato \(AB\) misura \(4\), il lato \(BC\) misura \(3\) e il lato \(AC\) misura \(5\). Questo triangolo in particolare dovrebbe apparire familiare allo studente, o cosǐ sarà in futuro, dato che si tratta di un triangolo determinato da una così detta \hro{\textit{terna pitagorica}}{https://it.wikipedia.org/wiki/Terna_pitagorica}, questi sono triangoli rettangoli le quali misure dei lati sono determinate da numeri interi. Verifichiamo infatti che abbiamo $3^2 + 4^2 = 9 + 16 = 25 = 5^2$ e perciò il triangolo risultante sarà equilatero. Altri esempi di terna pitagorica sono $(5, 12, 13)$ e $(7, 24, 25)$.

\[
\begin{tikzpicture}[scale=1.3]
  \coordinate (A) at (0,0);
  \coordinate (B) at (4,0);
  \coordinate (C) at (4,3);
  \draw[thick] (A)--(B)--(C)--cycle;
  \node[below left] at (A) {\(A\)};
  \node[below right] at (B) {\(B\)};
  \node[right] at (C) {\(C\)};
  \node at ($(A)!0.5!(B)+(0,-0.3)$) {\(4\)};
  \node at ($(B)!0.5!(C)+(0.2,0)$) {\(5\)};
  \node at ($(A)!0.5!(C)+(-0.4,0)$) {\(3\)};
  \node at ($(A)+(0.7,0.2)$) {\(\gamma\)};
  \node at ($(B)+(-0.4,0.3)$) {\(\beta\)};
  \node at ($(C)+(-0.2,-0.5)$) {\(\alpha\)};
\end{tikzpicture}
\]

Si vuole calcolare l’ampiezza degli angoli \(\alpha\), \(\beta\), \(\gamma\) utilizzando le formule di Briggs. Per \(\alpha\) si applica la formula relativa a \(\sin\frac{\alpha}{2}\). Dato che \(\alpha\) è opposto ad \(a\), la tabella fornisce
\[
\sin\frac{\alpha}{2} = \sqrt{\frac{(p-b)(p-c)}{b\,c}}
= \sqrt{\frac{(6-3)\,(6-4)}{3\cdot4}}
= \sqrt{\frac{3\cdot2}{12}}
= \sqrt{\frac{6}{12}}
= \sqrt{\tfrac12}
= \frac{\sqrt{2}}{2}.
\]
Di conseguenza, \(\tfrac{\alpha}{2}=\arcsin\bigl(\tfrac{\sqrt2}{2}\bigr)=45^\circ\), dunque \(\alpha=90^\circ\).

Per \(\beta\), opposto al lato \(b=3\), si utilizza la formula di Briggs per \(\cos\frac{\beta}{2}\). Dalla tabella, risulta
\[
\cos\frac{\beta}{2} = \sqrt{\frac{p\,(p-b)}{a\,c}}
= \sqrt{\frac{6\,(6-3)}{5\cdot4}}
= \sqrt{\frac{6\cdot3}{20}}
= \sqrt{\frac{18}{20}}
= \sqrt{\frac{9}{10}}
= \frac{3}{\sqrt{10}}.
\]
Da questa relazione si trova \(\tfrac{\beta}{2}=\arccos\bigl(\tfrac{3}{\sqrt{10}}\bigr)\). Il valore numerico di \(\frac{3}{\sqrt{10}}\) è poco meno di $1$, la cui arcocoseno è circa \(18^\circ\), quindi \(\beta\approx36^\circ\). Tuttavia, si sa che il triangolo è rettangolo in \(\alpha\), quindi \(\beta\) e \(\gamma\) devono essere gli altri due angoli acuti la cui somma è \(90^\circ\). Pertanto \(\beta\) risulta circa \(36\circ\).

Infine, per \(\gamma\), opposto a \(c=4\), si sfrutta la formula di Briggs per \(\tan\frac{\gamma}{2}\). La tabella riporta
\[
\tan\frac{\gamma}{2} = \sqrt{\frac{(p-a)(p-b)}{p\,(p-c)}}
= \sqrt{\frac{(6-5)\,(6-3)}{6\,(6-4)}}
= \sqrt{\frac{1\cdot3}{6\cdot2}}
= \sqrt{\frac{3}{12}}
= \sqrt{\tfrac14}
= \tfrac12.
\]
Allora \(\tfrac{\gamma}{2}=\arctan\bigl(\tfrac12\bigr)\approx26^\circ\) e \(\gamma\approx53^\circ\). Anche qui, la somma \(\beta+\gamma=36^\circ+53^\circ \approx 90^\circ\), coerente con il fatto che \(\alpha=90^\circ\).

La conclusione è che \(\alpha=90^\circ\), \(\beta\approx36^\circ\) e \(\gamma\approx53^\circ\). I piccoli scostamenti dagli angoli esatti di un triangolo 3-4-5 sono dovuti ad arrotondamenti numerici nelle funzioni inverse. L’uso delle formule di Briggs consente di calcolare in modo diretto \(\sin\frac{\alpha}{2}\), \(\cos\frac{\beta}{2}\) e \(\tan\frac{\gamma}{2}\) partendo unicamente dalle misure \(a,b,c\) del triangolo.

Notiamo anche che per poter avere un risultato numerico da espression di questo tipo è spesso necessario sapere i valori noti di seno e coseno che ci permettono di derivare facilmente i valori noti delle altre funzioni goniometriche, come le inverse secante e cosecante o similmente per la tangente.
\newpage
\subsectionstar{[38*] Sezione Aurea \& Lato di un Decagono}
\noindent
La \textit{sezione aurea} di un segmento si ottiene dividendo un segmento di lunghezza \(a\) in due parti, maggiore (\(x\)) e minore \((a-x)\), in modo che
\[
\frac{a}{x} = \frac{x}{a - x}.
\]
Risolvendo questa proporzione, si trova
\[
x = \frac{a(\sqrt{5}-1)}{2},
\quad
\text{e il rapporto } \phi = \frac{a}{x} = \frac{\sqrt{5}+1}{2} \approx 1.618 \dots
\]
viene chiamato \textit{numero aureo} o \textit{rapporto aureo}.

\smallskip
\noindent
\textbf{Costruzione geometrica della sezione aurea.}
Un metodo pratico per individuare il punto \(C\) su un segmento \(AB\) (lunghezza \(a\)) che realizza la sezione aurea prevede:
\begin{enumerate}
\item Tracciare, da \(A\), una perpendicolare di lunghezza pari a \(\tfrac12\,AB\).
\item Unire l’estremo di tale perpendicolare con \(B\), ottenendo un’ipotenusa.
\item Sottraendo dalla suddetta ipotenusa la misura della perpendicolare e riportando il “resto” sul segmento \(AB\), si ottiene la parte \(AC\) di lunghezza \(\frac{a(\sqrt{5}-1)}{2}\).
\end{enumerate}
Il \textit{teorema di Pitagora} e il trasferimento di segmenti con il compasso rendono possibile questa costruzione.

\smallskip
\noindent
\textbf{Decagono regolare e sezione aurea.}
Un’applicazione notevole riguarda il \textit{decagono regolare} inscritto in una circonferenza di raggio \(r\). Se \(l\) è il lato del decagono, si ha la proporzione
\[
r : l = l : (r - l),
\]
cioè \(l\) è la sezione aurea di \(r\). Questa relazione si ricava esaminando il triangolo isoscele con angolo al centro \(36^\circ\) e bisettrici che mostrano come \(l\) sia medio proporzionale tra \(r\) e \((r-l)\). In particolare,
\[
l = \frac{r(\sqrt{5}-1)}{2}.
\]

\begin{center}
\begin{tikzpicture}[scale=1.0, line join=round, line cap=round]
  % Circonferenza di raggio r
  \coordinate (O) at (0,0);
  \def\r{2.2}
  \draw[thick] (O) circle(\r);

  % Creazione approssimativa di un decagono
  \foreach \i in {0,...,9}{
    \coordinate (P\i) at (\i*36:\r);
  }
  \foreach \i in {0,...,8}{
    \pgfmathtruncatemacro{\next}{\i+1}
    \draw[thick] (P\i)--(P\next);
  }
  \draw[thick] (P9)--(P0);

  % Raggio e un lato
  \draw[dashed] (O)--(P0) node[midway,below left] {\small $r$};
  \node at ($(P0)!0.5!(P1)$) [above right] {\small $l$};

  \node at (0,2.7) {\small Decagono regolare inscritto in circonferenza di raggio $r$};
\end{tikzpicture}
\end{center}

\noindent
\textbf{Angoli di 18°, 36°, 54°, 72° e sezione aurea.}
\smallskip

Uno dei modi più eleganti per mostrare il legame tra \textit{sezione aurea} e \textit{trigonometria} è considerare gli angoli caratteristici del \textit{decagono regolare}. In particolare, quando si inscrive un decagono in una circonferenza di raggio 1, l’angolo al centro che sottende un lato è di \(36^\circ\). Dall’analisi geometrica del decagono (e dei triangoli isosceli con angoli di \(36^\circ\) e \(72^\circ\)), si ricavano valori notevoli per funzioni trigonometriche come \(\sin 18^\circ\) e \(\cos 36^\circ\).

\smallskip
\noindent
\textbf{Deduciamo $\sin 18^\circ$.}
\begin{itemize}
  \item Si consideri un triangolo isoscele con \textit{vertice al centro} e \textit{angolo al vertice} di \(36^\circ\). I due lati uguali sono raggi della circonferenza (lunghezza 1) e la base è il lato del decagono. 
  \item Tracciando bisettrici e segmenti, si mostra che la metà di tale base (ovvero la “semicorda” dell’angolo di \(18^\circ\)) risulta collegata al rapporto aureo.
  \item In termini più diretti, la lunghezza della corda che sottende \(36^\circ\) è la sezione aurea di 1, ossia \(\frac{\sqrt{5}-1}{2}\). La “semicorda” (corrispondente a \(\sin 18^\circ\)) è la metà di tale valore, per cui
\[
\sin 18^\circ = \frac12 \times \frac{\sqrt{5}-1}{2} = \frac{\sqrt{5}-1}{4}.
\]
\end{itemize}

\noindent
\textbf{Deduciamo $\cos 36^\circ$.}
\begin{itemize}
  \item Sapendo che \(\sin 18^\circ = \frac{\sqrt{5}-1}{4}\), si sfrutta la relazione \(\cos 36^\circ = \sin(90^\circ - 36^\circ) = \sin 54^\circ\). 
  \item Inoltre, esiste un rapporto diretto fra \(\sin 18^\circ\) e \(\cos 36^\circ\) grazie alle identità trigonometriche, oppure si procede per via geometrica osservando i triangoli isosceli con lati 1, 1, e base corrispondente al lato del decagono.
  \item Il risultato è 
\[
\cos 36^\circ = \frac{\sqrt{5}+1}{4},
\]
che è complementare a \(\sin 54^\circ\) e coinvolge la “parte positiva” del rapporto aureo (con \(\sqrt{5}+1\) anziché \(\sqrt{5}-1\)).
\end{itemize}

\smallskip
\noindent
\textbf{Ulteriori valori.}
Una volta noti \(\sin 18^\circ\) e \(\cos 36^\circ\), si possono dedurre in modo analogo \(\sin 36^\circ\), \(\cos 18^\circ\), \(\sin 54^\circ\) e \(\sin 72^\circ\), usando formule di \textit{addizione} e \textit{differenza} degli angoli (o formule di duplicazione e complementari). Ne emergono tutte espressioni in cui \(\sqrt{5}\) e i termini \(\pm 1\) compaiono, a conferma che i poligoni regolari (in particolare pentagono e decagono) sono intimamente connessi con il \textit{numero aureo}. La seguente tabella riporta tutti i valori di questo tipo.

\noindent
Nella seguente tabella sono riportati i valori di \(\sin\), \(\cos\) e \(\tan\) per gli angoli di \(18^\circ\), \(36^\circ\), \(54^\circ\) e \(72^\circ\). Si evidenziano sia le \textbf{espressioni in forma radicale} (in cui compare la \textit{sezione aurea}) sia i valori \textbf{approssimati}:

\begin{center}
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{c|c|c|c}
\hline
\textbf{Angolo} & \(\sin\) & \(\cos\) & \(\tan\) \\
\hline
\(18^\circ\) 
& 
\(\displaystyle \frac{\sqrt{5}-1}{4} \approx 0.3090\) 
& 
\(\displaystyle \frac{\sqrt{10+2\sqrt{5}}}{4} \approx 0.9511\) 
& 
\(\approx 0.3249\) \\
\hline
\(36^\circ\) 
& 
\(\displaystyle \frac{\sqrt{10-2\sqrt{5}}}{4} \approx 0.5878\) 
& 
\(\displaystyle \frac{\sqrt{5}+1}{4} \approx 0.8090\) 
& 
\(\approx 0.7265\) \\
\hline
\(54^\circ\) 
& 
\(\displaystyle \frac{\sqrt{5}+1}{4} \approx 0.8090\) 
& 
\(\displaystyle \frac{\sqrt{10-2\sqrt{5}}}{4} \approx 0.5878\) 
& 
\(\approx 1.3764\) \\
\hline
\(72^\circ\) 
& 
\(\displaystyle \frac{\sqrt{10+2\sqrt{5}}}{4} \approx 0.9511\) 
& 
\(\displaystyle \frac{\sqrt{5}-1}{4} \approx 0.3090\) 
& 
\(\approx 3.0777\) \\
\hline
\end{tabular}
\end{center}

\noindent
Si nota che gli angoli \(18^\circ\) e \(36^\circ\) (e i loro complementari \(72^\circ\) e \(54^\circ\)) risultano \textit{intimamente legati} alla \textit{sezione aurea}. In particolare:
\[
\sin 18^\circ = \frac{\sqrt{5}-1}{4}, 
\quad
\cos 36^\circ = \frac{\sqrt{5}+1}{4},
\]
sono espressioni emblematiche che derivano dalla costruzione del \textit{decagono regolare} e dalle relazioni tra i segmenti in esso contenuti, i quali introducono naturalmente il \textit{numero aureo} \(\phi\).
\newpage

\section*{Note sul Documento}

\begin{center}
\begin{tabular}{|l|c|}
\hline
\textbf{Parametro} & \textbf{Valore} \\
\hline
Argomenti del primo concorso & 41 \\
\hline
Argomenti del secondo concorso & 46 \\
\hline
Argomenti del secondo concorso non presenti nel primo & 14\\
\hline
Numero totale di argomenti distinti & 55 \\
\hline
Numero di pagine introduttive & 7 \\
\hline
Media di pagine per argomento & 2,07 \\
\hline
Numero di argomenti raggruppati & 2 \\
\hline
Numero totale di pagine & 113.9 \\
\hline
\end{tabular}
\end{center}

Quanto si vede riassunto sopra fa riferimento alla tabella riassuntiva in cui ho riportato tutti i dati di questo documento, la si può trovare al link:\[\text{\hro{https://docs.google.com/spreadsheets/d/1RlrBk0Y4nBUo-FvXwBSUeQsYiN3-3fdeCY3Ao2ZHMfU/edit}{https://docs.google.com/spreadsheets/d/1RlrBk0Y4nBUo-FvXwBSUeQsYiN3-3fdeCY3Ao2ZHMfU/edit}}\]

\textbf{NB}: 
\begin{itemize}
    \item Ho aggiunto delle note nella parte delle progressioni che avevo precedentemente abbozzato per le lezioni che faccio di logica numerica, quelle non fanno strettamente parte del programma e possono quindi essere eliminate e/o non menzionate nel conteggio delle pagine rilevanti per il pagamento. Di questo infatti non tengo conto nella \hro{tabella}{https://docs.google.com/spreadsheets/d/1RlrBk0Y4nBUo-FvXwBSUeQsYiN3-3fdeCY3Ao2ZHMfU/edit}.
    \item Nella media delle pagine per argomento ho anche tenuto conto di quelle 7 pagine introduttive alle sezioni. La media, non contando quelle, sarebbe quindi di poco inferiore a 2.
\end{itemize}

\end{document}
````
### Invoice
````LaTeX
\section*{Invoice}

\begin{tabular}{l l}
    \textbf{Invoice No.:} & 5\\
    \textbf{Invoice Date:} & 13.03.2025\\
\end{tabular}

\vspace{1em}

\noindent\textbf{Seller:} \\
\begin{tabular}{l l}
    Name: & \textbf{Simone Testino} \\
    Legal Address: & \textbf{Plantage Muidergracht 76, 1018 TV,}\\
    & \textbf{Amsterdam, Netherlands} \\
    VAT Identification Number (BSN): & \textbf{641105824} \\

&\\

Company Name: & \textbf{Futura S.p.A.} \\
Address: & Via Giuseppe Ripamonti 44, 20141 Milano (MI) \\
VAT Number: & \textbf{P.IVA 04322010713} \\

&\\

\noindent\textbf{Description of Supplied Goods or Services:} \\
    Entity of Service: & Handout in Highschool Mathematics ,\\
    Delivery Date: & \textbf{05.03.2025 - 16.03.2025}\\
    Quantity of Services: & \textbf{114 pages} \\
    Payment per Page: & \textbf{10€} \\
    Total Amount (including VAT): & \textbf{1140€}\\


&\\

\noindent\textbf{Bank Information:} \\
    Account Holder: & \textbf{Simone Testino} \\
    IBAN: & \textbf{IT94I0338501601100080084122} \\
    BIC/SWIFT: & \textbf{ISYBITMM} \\
    Bank Name: & \textbf{Isybank by Intesa San Paolo, Italy} \\
\end{tabular}
```