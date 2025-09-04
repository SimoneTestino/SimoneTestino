---
draft: true
date: 2025-03-19
---
I paste here the relevant code for the second document described in [[Futura Math Didactic Document]]. The source code is available in the project [Overleaf: Documento 03.25](https://www.overleaf.com/read/njtwzjnxvgpb#c86992).

The `name`package refers to [[LaTeX Commands]] on date 13.03.2025.
### Main
```LaTeX
\include{system/name}
\title{Prova Orale per i Concorrenti per il Corpo Sanitario e per il Corpo di Commissariato}

\begin{document}
\maketitle

\tableofcontents

\include{mains/Esercito/Algebra}

\include{mains/Esercito/Geometria}

\include{mains/Esercito/Trigonometria}

\newpage
Riporto i dati relativi a questo documento nella \hro{tabella}{https://docs.google.com/spreadsheets/d/1RlrBk0Y4nBUo-FvXwBSUeQsYiN3-3fdeCY3Ao2ZHMfU/edit}, nel foglio chiamato \q{Esercito}.



\end{document}
```

### Algebra
```LaTeX
\section{Algebra}
\subsectionstar{Gli Insiemi Numerici Semplici [1]}

In questi appunti affronteremo la definizione dei vari insiemi numerici, partendo dai numeri naturali e proseguendo con quelli interi, razionali, irrazionali e così via. L'obiettivo è quello di fornire una base rigorosa e formale per comprendere la struttura e la gerarchia dei numeri, a partire dal concetto elementare di numero come risultato di un'iterazione della funzione successore.

\subsubsection*{I Numeri Naturali}
I numeri naturali costituiscono l'insieme fondamentale impiegato nel conteggio. Essi vengono definiti partendo da un elemento iniziale, convenzionalmente indicato con \(1\), e dalla funzione successore \(s\), che associa ad ogni numero naturale il suo immediato successore. 

In particolare, il numero \(2\) è definito come il successore di \(1\), ovvero:
\[
2 = s(1),
\]
mentre il numero \(3\) corrisponde al successore del successore di \(1\):
\[
3 = s(s(1)).
\]
Analogamente, \(4\) si ottiene come:
\[
4 = s(s(s(1))),
\]
e così via. Così, l'insieme dei numeri naturali può essere formalmente rappresentato come:
\[
\mathbb{N} = \{1, s(1), s(s(1)), s(s(s(1))), \dots\}.
\]

La seguente rappresentazione grafica illustra il meccanismo di successione:
\[
\begin{tikzpicture}[node distance=2cm, auto]
\node (A) {1};
\node (B) [right of=A] {2};
\node (C) [right of=B] {3};
\node (D) [right of=C] {$\cdots$};
\draw[->] (A) -- node {s} (B);
\draw[->] (B) -- node {s} (C);
\draw[->] (C) -- node {s} (D);
\end{tikzpicture}
\]
\subsubsection*{Operazioni sui Numeri Naturali}
I numeri naturali sono chiusi rispetto all'addizione e alla moltiplicazione: per ogni \(a, b \in \mathbb{N}\) si ha
\[
a + b \in \mathbb{N} \quad \text{e} \quad a \cdot b \in \mathbb{N}.
\]
Tuttavia, la sottrazione non è sempre definita in \(\mathbb{N}\); ad esempio, le seguenti operazioni non sono ammesse:
\[
3 - 5 \quad \text{e} \quad 2 - 4,
\]
poiché i loro risultati,
\[
-2,
\]
non appartengono a \(\mathbb{N}\). Analogamente, la divisione dà luogo a un numero naturale solo se il divisore divide esattamente il dividendo: ad esempio,
\[
\frac{6}{3} = 2,
\]
è definita in \(\mathbb{N}\), mentre
\[
\frac{3}{2} \quad \text{e} \quad \frac{5}{4},
\]
non lo sono.

\subsubsection*{I Numeri Interi}
I numeri interi sono definiti estendendo l'insieme dei numeri naturali con l'aggiunta degli opposti, in modo da garantire che ogni operazione di sottrazione sia sempre definita. In particolare, l'insieme degli interi è rappresentato da
\[
\mathbb{Z} = \{\dots, -3, -2, -1, 0, 1, 2, 3, \dots\}.
\]
Così, per ogni \(a, b \in \mathbb{Z}\), l'operazione \(a - b\) produce un risultato che appartiene a \(\mathbb{Z}\); ad esempio,
\[
3 - 5 = -2 \quad \text{e} \quad 2 - 4 = -2.
\]
Tuttavia, la divisione rimane parzialmente definita: il quoziente \(\frac{a}{b}\) è un numero intero solo se \(b\) divide esattamente \(a\); per esempio,
\[
\frac{6}{3} = 2,
\]
mentre
\[
\frac{3}{2} \quad \text{e} \quad \frac{5}{4},
\]
non appartengono a \(\mathbb{Z}\).

\subsubsection*{I Numeri Razionali}
I numeri razionali sono definiti come l'insieme delle frazioni \(\frac{a}{b}\), dove \(a \in \mathbb{Z}\) e \(b \in \mathbb{Z} \setminus \{0\}\). In altre parole,
\[
\mathbb{Q} = \left\{ \frac{a}{b} \,\middle|\, a \in \mathbb{Z},\; b \in \mathbb{Z} \setminus \{0\} \right\}.
\]
Questo insieme amplia quello degli interi, risolvendo il problema della divisione: ogni operazione di divisione, in cui il divisore è diverso da zero, trova una rappresentazione in \(\mathbb{Q}\). Ad esempio, l'operazione
\[
\frac{3}{2}
\]
è definita in \(\mathbb{Q}\), mentre la divisione per zero resta indefinita.

Le regole per la moltiplicazione e la divisione tra frazioni sono le seguenti. Considerando due numeri razionali \(\frac{a}{b}\) e \(\frac{c}{d}\), con \(b, d \neq 0\), si ha:
\[
\frac{a}{b} \cdot \frac{c}{d} = \frac{a \cdot c}{b \cdot d},
\]
e
\[
\frac{\frac{a}{b}}{\frac{c}{d}} = \frac{a}{b} \cdot \frac{d}{c} = \frac{a \cdot d}{b \cdot c},
\]
con la condizione che \(c \neq 0\). Queste regole evidenziano che la divisione per una frazione equivale alla moltiplicazione per il suo reciproco, dove il reciproco di \(\frac{c}{d}\) è \(\frac{d}{c}\).

È fondamentale verificare che i denominatori siano sempre diversi da zero e, ove possibile, semplificare le frazioni per ottenere una rappresentazione ridotta.

\subsec{I Numeri Reali e la Retta dei Numeri [1]}
I numeri reali rappresentano un'ulteriore estensione dell'insieme dei numeri razionali \(\mathbb{Q}\). Essi permettono di includere anche i limiti di successioni di numeri razionali, le misurazioni e le grandezze continue. La loro definizione richiede passaggi aggiuntivi, quali il completamento di \(\mathbb{Q}\) o l'impiego di successioni di Cauchy, ma per il momento è sufficiente accennare che essi costituiscono l'insieme \(\mathbb{R}\).

\subsubsection*{La Retta dei Numeri}
La retta dei numeri è una rappresentazione geometrica che visualizza l'ordine e la posizione dei numeri. In primo luogo, osserviamo la retta dei numeri naturali:
\[
\begin{tikzpicture}[x=1cm, y=0.5cm]
  \draw[->] (0,0) -- (5,0);
  \foreach \x in {1,2,3,4,5} {
    \draw (\x,0.1) -- (\x,-0.1) node[below] {\(\x\)};
  }
\end{tikzpicture}
\]
Sulla retta dei numeri naturali si evidenzia la posizione dei numeri a partire da \(1\), disposti in ordine crescente.

Passando agli interi, la retta si estende includendo anche i numeri negativi e lo zero:
\[
\begin{tikzpicture}[x=1cm, y=0.5cm]
  \draw[->] (-4,0) -- (4,0);
  \foreach \x in {-3,-2,-1,0,1,2,3} {
    \draw (\x,0.1) -- (\x,-0.1) node[below] {\(\x\)};
  }
\end{tikzpicture}
\]
La retta degli interi è simmetrica rispetto a \(0\) e include tutti i numeri negativi e positivi.

Infine, la retta dei numeri razionali, pur potendo essere rappresentata in modo simile, evidenzia la proprietà di densità: tra ogni coppia di numeri razionali esiste sempre un altro numero razionale.
\[
\begin{tikzpicture}[x=1cm, y=0.5cm]
  \draw[->] (0,0) -- (5,0);
  \foreach \x in {0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5} {
    \draw (\x,0.1) -- (\x,-0.1);
  }
  \node[below] at (0, -0.1) {\(0\)};
  \node[below] at (1, -0.1) {\(1\)};
  \node[below] at (2, -0.1) {\(2\)};
  \node[below] at (3, -0.1) {\(3\)};
  \node[below] at (4, -0.1) {\(4\)};
  \node[below] at (5, -0.1) {\(5\)};
\end{tikzpicture}
\]
Questa rappresentazione evidenzia come, a differenza delle rette dei numeri naturali e degli interi, la retta dei numeri razionali sia "piena" di punti, riflettendo la loro densità.

\subsubsection*{Retta Densa e Dimostrazione della Densità di \(\mathbb{Q}\)}
Un insieme \(S\) di numeri è detto \textit{denso} nella retta se, dati due numeri \(a\) e \(b\) con \(a < b\), esiste almeno un elemento \(c \in S\) tale che
\[
a < c < b.
\]
Per dimostrare che l'insieme dei numeri razionali \(\mathbb{Q}\) è denso, si consideri \(a, b \in \mathbb{Q}\) con \(a < b\). Definiamo:
\[
c = \frac{a+b}{2}.
\]
Poiché \(a\) e \(b\) sono razionali, anche \(c\) risulta razionale. Inoltre, si ha:
\[
a < \frac{a+b}{2} < b,
\]
il che prova che tra \(a\) e \(b\) esiste un numero razionale. Pertanto, \(\mathbb{Q}\) è denso nella retta.

\subsubsection*{I Numeri Reali}
I numeri reali, essendo un'estensione dell'insieme dei numeri razionali, permettono di definire operazioni che non sono sempre possibili in \(\mathbb{Q}\). Un esempio emblematico riguarda l'estrazione della radice: infatti, si dimostrerà che \(\sqrt{2}\) non appartiene a \(\mathbb{Q}\).

\begin{Theorem}[Irrazionalità di \(\sqrt{2}\)]
\(\sqrt{2}\) non è un numero razionale.
\end{Theorem}
\begin{proof}[Dimostrazione]
Supponiamo per assurdo che \(\sqrt{2}\) sia razionale, cioè esistano interi \(a\) e \(b\) (con \(b \neq 0\) e \(\gcd(a,b)=1\)) tali che
\[
\sqrt{2} = \frac{a}{b}.
\]
Elevando al quadrato entrambi i membri si ottiene
\[
2 = \frac{a^2}{b^2} \quad \Longrightarrow \quad a^2 = 2b^2.
\]
Pertanto, \(a^2\) è pari, il che implica che \(a\) è pari. Sia \(a = 2k\) per qualche intero \(k\); sostituendo si ha
\[
(2k)^2 = 2b^2 \quad \Longrightarrow \quad 4k^2 = 2b^2 \quad \Longrightarrow \quad b^2 = 2k^2.
\]
Da cui \(b^2\) è pari e dunque \(b\) è pari. Ciò implica che \(a\) e \(b\) hanno entrambi un fattore comune \(2\), contraddicendo l'ipotesi che la frazione \(\frac{a}{b}\) sia espressa in forma ridotta. Quindi, \(\sqrt{2}\) non può essere razionale.
\end{proof}

Questo risultato evidenzia che esistono operazioni, come l'estrazione della radice, che producono numeri al di fuori di \(\mathbb{Q}\). Tale constatazione ci induce a intuire che l'insieme dei numeri reali debba includere anche altri numeri, i numeri irrazionali, per completare la retta numerica.

I numeri reali rappresentano l'insieme che completa la retta numerica, includendo anche quei punti verso i quali alcune successioni di numeri razionali si avvicinano senza mai "fermarsi" all'interno di \(\mathbb{Q}\). In modo informale, una sequenza si dice convergente se i suoi termini si avvicinano sempre di più a un certo valore, nel senso che, dopo un certo stadio, tutti i termini risultano molto prossimi tra loro e a quel valore "limite".

Consideriamo, ad esempio, la successione ottenuta dagli sviluppi decimali di \(\pi\):
\[
3,\quad 3.1,\quad 3.14,\quad 3.141,\quad 3.1415,\quad \dots
\]
Questa successione mostra come i termini si avvicinino progressivamente a \(\pi\). Tuttavia, se ci limitassimo ai numeri razionali, non riusciremmo a trovare il punto preciso verso cui questa successione converge, poiché \(\pi\) non è un numero razionale. In altre parole, il "punto di arrivo" della successione non appartiene all'insieme \(\mathbb{Q}\), il che evidenzia la necessità di introdurre i numeri reali per completare la retta numerica.

La seguente rappresentazione grafica illustra il concetto: immaginiamo una retta numerica in cui i punti corrispondenti ai termini della successione si spostano progressivamente verso un punto che non è rappresentabile nei numeri razionali.
\[
\begin{tikzpicture}[xscale=40]
  % Disegno della retta numerica
  \draw[<->, thick] (3,0) -- (3.3,0);
  \foreach \x in {3,3.05,3.1,3.15,3.2,3.25,3.3} {
    \draw (\x,0.15) -- (\x,-0.15) node[below] {\(\x\)};
  }
  % Sequenza di punti (linee verticali blu) che si avvicinano a π
  \draw[blue, very thick] (3, -0.2) -- (3, 0.2);
  \draw[blue, very thick] (3.1, -0.2) -- (3.1, 0.2);
  \draw[blue, very thick] (3.14, -0.2) -- (3.14, 0.2);
  \draw[blue, very thick] (3.141, -0.2) -- (3.141, 0.2);
  \draw[blue, very thick] (3.1415, -0.2) -- (3.1415, 0.2);
  \draw[blue, very thick] (3.14159, -0.2) -- (3.14159, 0.2);
  % Punto di convergenza (π) evidenziato con una linea rossa
  \draw[red, very thick] (3.1416, -0.2) -- (3.1416, 0.2);
  \node[red, above] at (3.1416,0.25) {\(\pi\)};
\end{tikzpicture}
\]

Concludiamo quindi con questa definizione dei numeri reali: 

\begin{Definition}[Numeri Reali tramite Sequenze]
I numeri reali sono quei numeri che completano la retta numerica, ottenuti come \q{valore finale} di successioni di numeri razionali che si avvicinano sempre di più a un certo numero.
\end{Definition}



\subsec{Radicali e Potenze [1, 4]}
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




\subsec{Introduzione ai Polinomi [1, 2, 3, 4]}
I monomi sono espressioni algebriche costituite da un solo termine, solitamente scritte nella forma
\[
a x^n,
\]
dove \(a\) è un coefficiente e \(n\) è un numero intero non negativo, cioè \(n \in \mathbb{N}\). Questa condizione sull'esponente garantisce che il monomio sia ben definito nell'ambito dell'aritmetica polinomiale.

Un polinomio è una somma finita di monomi. In maniera più formale, un polinomio nella variabile \(x\) si esprime come
\[
P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0,
\]
dove \(n \in \mathbb{N}\) e ogni coefficiente \(a_i\) è un numero (solitamente reale). È fondamentale che tutti gli esponenti, ossia \(n, n-1, \dots, 1, 0\), appartengano all'insieme dei numeri naturali, per garantire la corretta definizione del polinomio.

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

\subsec{Prodotti Notevoli [1, 2, 3, 4]}
I prodotti notevoli sono identità algebriche fondamentali che semplificano il calcolo e la manipolazione delle espressioni polinomiali. Essi derivano dalla proprietà distributiva della moltiplicazione e permettono di esprimere in forma compatta, ad esempio, il quadrato di una somma o di una differenza, il prodotto della somma per la differenza, nonché la somma e la differenza dei cubi. Queste formule sono strumenti essenziali per riconoscere e scomporre espressioni complesse, facilitando la risoluzione di equazioni e il ragionamento algebrico.

\begin{center}
\begin{tabular}{|c|c|}
\hline
\textbf{Prodotto Notevole} & \textbf{Formula Espansa} \\
\hline
\((a+b)^2\) & \(a^2 + 2ab + b^2\) \\
\hline
\((a-b)^2\) & \(a^2 - 2ab + b^2\) \\
\hline
\((a+b)(a-b)\) & \(a^2 - b^2\) \\
\hline
\((a+b)^3\) & \(a^3 + 3a^2b + 3ab^2 + b^3\) \\
\hline
\((a-b)^3\) & \(a^3 - 3a^2b + 3ab^2 - b^3\) \\
\hline
\(a^3+b^3\) & \((a+b)(a^2 - ab + b^2)\) \\
\hline
\(a^3-b^3\) & \((a-b)(a^2 + ab + b^2)\) \\
\hline
\end{tabular}
\end{center}

\bigskip

% Dimostrazioni dei Prodotti Notevoli

\begin{lemma}[(\(a+b\))\textsuperscript{2}]
Per ogni \(a, b \in \mathbb{R}\), vale
\[
(a+b)^2 = a^2 + 2ab + b^2.
\]
\end{lemma}
\begin{proof}[Dimostrazione]
Si ha, per definizione:
\[
(a+b)^2 = (a+b)(a+b).
\]
Applicando la proprietà distributiva:
\[
(a+b)(a+b) = a\cdot a + a\cdot b + b\cdot a + b\cdot b = a^2 + ab + ab + b^2.
\]
Raggruppando i termini simili, si ottiene:
\[
(a+b)^2 = a^2 + 2ab + b^2.
\]
\end{proof}

\begin{lemma}[(\(a-b\))\textsuperscript{2}]
Per ogni \(a, b \in \mathbb{R}\), vale
\[
(a-b)^2 = a^2 - 2ab + b^2.
\]
\end{lemma}
\begin{proof}[Dimostrazione]
Si parte da:
\[
(a-b)^2 = (a-b)(a-b).
\]
Applicando la proprietà distributiva:
\[
(a-b)(a-b) = a\cdot a - a\cdot b - b\cdot a + b\cdot b = a^2 - ab - ab + b^2.
\]
Raggruppando i termini:
\[
(a-b)^2 = a^2 - 2ab + b^2.
\]
\end{proof}

\begin{lemma}[\((a+b)(a-b)\)]
Per ogni \(a, b \in \mathbb{R}\), vale
\[
(a+b)(a-b) = a^2 - b^2.
\]
\end{lemma}
\begin{proof}[Dimostrazione]
Si scrive:
\[
(a+b)(a-b) = a(a-b) + b(a-b).
\]
Applicando la proprietà distributiva:
\[
= a^2 - ab + ab - b^2.
\]
Notando che i termini \(-ab\) e \(ab\) si annullano, si ha:
\[
(a+b)(a-b) = a^2 - b^2.
\]
\end{proof}

\begin{lemma}[(\(a+b\))\textsuperscript{3}]
Per ogni \(a, b \in \mathbb{R}\), vale
\[
(a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3.
\]
\end{lemma}
\begin{proof}[Dimostrazione]
Si ha:
\[
(a+b)^3 = (a+b)(a+b)(a+b).
\]
Utilizzando il risultato per \((a+b)^2\), scriviamo:
\[
(a+b)^3 = (a^2 + 2ab + b^2)(a+b).
\]
Applicando la proprietà distributiva:
\[
= a^2\cdot a + a^2\cdot b + 2ab\cdot a + 2ab\cdot b + b^2\cdot a + b^2\cdot b,
\]
cioè:
\[
= a^3 + a^2b + 2a^2b + 2ab^2 + ab^2 + b^3.
\]
Raggruppando i termini simili:
\[
(a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3.
\]
\end{proof}

\begin{lemma}[(\(a-b\))\textsuperscript{3}]
Per ogni \(a, b \in \mathbb{R}\), vale
\[
(a-b)^3 = a^3 - 3a^2b + 3ab^2 - b^3.
\]
\end{lemma}
\begin{proof}[Dimostrazione]
Si ha:
\[
(a-b)^3 = (a-b)(a-b)(a-b).
\]
Utilizzando il risultato per \((a-b)^2\), otteniamo:
\[
(a-b)^3 = (a^2 - 2ab + b^2)(a-b).
\]
Applicando la proprietà distributiva:
\[
= a^2\cdot a - a^2\cdot b - 2ab\cdot a + 2ab\cdot b + b^2\cdot a - b^2\cdot b,
\]
cioè:
\[
= a^3 - a^2b - 2a^2b + 2ab^2 + ab^2 - b^3.
\]
Raggruppando i termini simili:
\[
(a-b)^3 = a^3 - 3a^2b + 3ab^2 - b^3.
\]
\end{proof}

\begin{lemma}[Somma dei Cubi]
Per ogni \(a, b \in \mathbb{R}\), vale
\[
a^3 + b^3 = (a+b)(a^2 - ab + b^2).
\]
\end{lemma}
\begin{proof}[Dimostrazione]
Si ha:
\[
(a+b)(a^2 - ab + b^2) = a(a^2 - ab + b^2) + b(a^2 - ab + b^2).
\]
Svolgendo i calcoli:
\[
= a^3 - a^2b + ab^2 + a^2b - ab^2 + b^3.
\]
I termini \(-a^2b\) e \(a^2b\), così come \(ab^2\) e \(-ab^2\), si annullano, per cui:
\[
(a+b)(a^2 - ab + b^2) = a^3 + b^3.
\]
\end{proof}

\begin{lemma}[Differenza dei Cubi]
Per ogni \(a, b \in \mathbb{R}\), vale
\[
a^3 - b^3 = (a-b)(a^2 + ab + b^2).
\]
\end{lemma}
\begin{proof}[Dimostrazione]
Si ha:
\[
(a-b)(a^2 + ab + b^2) = a(a^2 + ab + b^2) - b(a^2 + ab + b^2).
\]
Svolgendo:
\[
= a^3 + a^2b + ab^2 - a^2b - ab^2 - b^3.
\]
Osserviamo che i termini \(a^2b\) e \(-a^2b\) si annullano, così come \(ab^2\) e \(-ab^2\), dunque:
\[
(a-b)(a^2 + ab + b^2) = a^3 - b^3.
\]
\end{proof}
\subsubsection*{Esempi Applicativi}
Consideriamo l'equazione
\[
(x+1)^3 - (x-1)^3 = 16.
\]
Utilizziamo il prodotto notevole per la differenza dei cubi, che afferma
\[
a^3 - b^3 = (a-b)(a^2 + ab + b^2),
\]
con
\[
a = x+1 \quad \text{e} \quad b = x-1.
\]
Calcoliamo innanzitutto:
\[
a - b = (x+1) - (x-1) = 2.
\]
Poi, osserviamo che
\[
a^2 + ab + b^2 = (x+1)^2 + (x+1)(x-1) + (x-1)^2.
\]
Svolgiamo i singoli termini:
\[
(x+1)^2 = x^2 + 2x + 1,
\]
\[
(x-1)^2 = x^2 - 2x + 1,
\]
\[
(x+1)(x-1) = x^2 - 1.
\]
Pertanto,
\[
a^2 + ab + b^2 = \bigl(x^2 + 2x + 1\bigr) + \bigl(x^2 - 1\bigr) + \bigl(x^2 - 2x + 1\bigr) = 3x^2 + 1.
\]
Così, l'equazione diventa:
\[
(x+1)^3 - (x-1)^3 = 2(3x^2+1) = 6x^2 + 2.
\]
Sostituendo nell'equazione originale:
\[
6x^2 + 2 = 16.
\]
Sottraendo 2 da entrambi i membri si ottiene:
\[
6x^2 = 14,
\]
da cui
\[
x^2 = \frac{14}{6} = \frac{7}{3}.
\]
Infine, estraendo la radice:
\[
x = \pm \sqrt{\frac{7}{3}}.
\]

\subsec{Scoposizione di Polinomi \& Ruffini [1]}
\subsubsection*{Scomposizione dei Polinomi}
La scomposizione di un polinomio consiste nel scriverlo come prodotto di polinomi di grado inferiore, detta fattorizzazione. Questo procedimento può avvenire tramite diversi metodi:
\begin{itemize}
    \item \textbf{Fattorizzazione per Fattore Comune}: si estrae il massimo comune divisore di tutti i termini.
    \item \textbf{Scomposizione per Gruppi}: si raggruppano i termini in insiemi che presentano un fattore comune.
    \item \textbf{Utilizzo dei Prodotti Notevoli}: si impiegano formule come \((a+b)^2 = a^2+2ab+b^2\), \((a+b)(a-b)=a^2-b^2\), ecc.
    \item \textbf{Scomposizione tramite Equazioni}: in alcuni casi si cerca lo zero del polinomio, così da poterlo scrivere come prodotto di fattori lineari e, eventualmente, polinomi di grado maggiore.
\end{itemize}

\textbf{Esempi:}

\begin{itemize}
    \item Scomponiamo il polinomio 
    \[
    x^2 - 5x + 6.
    \]
    Cerchiamo due numeri la cui somma sia \(-5\) e il cui prodotto sia \(6\). Poiché \(-2\) e \(-3\) soddisfano queste condizioni, si ha:
    \[
    x^2 - 5x + 6 = (x-2)(x-3).
    \]
    
    \item Consideriamo il polinomio 
    \[
    x^3 - 3x^2 + 3x - 1.
    \]
    Osserviamo che questo è il cubo di \((x-1)\), infatti:
    \[
    (x-1)^3 = x^3 - 3x^2 + 3x - 1.
    \]
    
    \item Un esempio di scomposizione per gruppi: 
    \[
    x^3 + 2x^2 + x + 2.
    \]
    Raggruppiamo come \((x^3+2x^2) + (x+2)\) e fattorizziamo:
    \[
    x^2(x+2) + 1(x+2) = (x+2)(x^2+1).
    \]
\end{itemize}
\subsubsection*{Divisione tra Polinomi}
La divisione tra polinomi permette di dividere un polinomio (dividendo) per un altro polinomio (divisore), ottenendo un quoziente e un resto. Si usa l'algoritmo di divisione polinomiale, analogo a quello della divisione tra numeri interi.

\textbf{Esempio:} Dividiamo il polinomio
\[
P(x)=x^3 - 6x^2 + 11x - 6
\]
per il binomio
\[
d(x)=x-1.
\]
Notiamo che \(x=1\) è una radice di \(P(x)\), quindi \(x-1\) è un fattore. Procedendo con la divisione, si ottiene:
\[
x^3 - 6x^2 + 11x - 6 = (x-1)(x^2 - 5x + 6).
\]
Il quoziente \(x^2 - 5x + 6\) si scompone ulteriormente in:
\[
x^2 - 5x + 6 = (x-2)(x-3).
\]

\bigskip

\subsubsection*{Il Metodo di Ruffini}
Il metodo di Ruffini è un procedimento rapido per dividere un polinomio per un binomio lineare della forma \((x-a)\). Si esegue in questo modo:
\begin{enumerate}
    \item Si scrivono i coefficienti del polinomio in ordine decrescente di grado.
    \item Si porta giù il primo coefficiente.
    \item Si moltiplica il coefficiente portato per \(a\) e si somma il risultato al coefficiente successivo.
    \item Si ripete il procedimento per tutti i coefficienti.
\end{enumerate}

\textbf{Esempio:} Dividiamo il polinomio
\[
P(x)=x^3 - 6x^2 + 11x - 6
\]
per \(x-1\) (cioè con \(a=1\)). I coefficienti sono \(1\), \(-6\), \(11\), \(-6\). Disposti in griglia, otteniamo:
\[
\begin{array}{r|rrrr}
1 & 1 & -6 & 11 & -6 \\
  &   & 1  & -5 & 6  \\ \hline
  & 1 & -5 & 6  & 0
\end{array}
\]
\begin{itemize}
    \item Si porta giù il \(1\).
    \item \(1 \times 1 = 1\); sommiamo \(-6+1 = -5\).
    \item \(-5 \times 1 = -5\); sommiamo \(11+(-5)=6\).
    \item \(6 \times 1 = 6\); sommiamo \(-6+6=0\).
\end{itemize}
Il quoziente è \(x^2 - 5x + 6\) e il resto è \(0\). Come visto, \(x^2 - 5x + 6\) si scompone ulteriormente in \((x-2)(x-3)\).

\bigskip

\textbf{Ulteriore Esempio con il Metodo di Ruffini:} Dividiamo
\[
P(x)=2x^3 + 3x^2 - 5x - 6
\]
per \(x+2\) (cioè con \(a=-2\)). I coefficienti sono \(2\), \(3\), \(-5\), \(-6\). La griglia di Ruffini è:
\[
\begin{array}{r|rrrr}
-2 & 2 & 3 & -5 & -6 \\
   &   & -4 & 2 & 6 \\ \hline
   & 2 & -1 & -3 & 0
\end{array}
\]
\begin{itemize}
    \item Portiamo giù \(2\).
    \item \(2 \times (-2) = -4\); sommiamo \(3+(-4)=-1\).
    \item \(-1 \times (-2) = 2\); sommiamo \(-5+2=-3\).
    \item \(-3 \times (-2)=6\); sommiamo \(-6+6=0\).
\end{itemize}
Il quoziente è \(2x^2 - x - 3\) e il resto è \(0\).

\subsec{Risoluzione di un Polinomio [1, 2, 3]}
Risolvere un polinomio significa trovare i valori di \(x\) per cui il polinomio si annulla, ossia determinare l'insieme 
\[
\{x \in \mathbb{R} \mid P(x)=0\}.
\]
Questi valori sono detti \textit{zeri} del polinomio.

\subsubsection*{Polinomi di Primo Grado}
Un polinomio di primo grado ha la forma
\[
P(x)=ax+b \quad (a\neq 0).
\]
Trovare lo zero di \(P(x)\) equivale a risolvere l'equazione
\[
ax+b=0,
\]
da cui si ottiene
\[
x=-\frac{b}{a}.
\]

\textbf{Esempio:} Consideriamo il polinomio
\[
P(x)=2x-4.
\]
Risolvendo \(2x-4=0\) si ha
\[
2x=4 \quad \Longrightarrow \quad x=2.
\]

\medskip

\begin{center}
\begin{tikzpicture}[scale=1]
  % Assi cartesiani (dominio limitato)
  \draw[->] (0,0) -- (4,0) node[right] {\(x\)};
  \draw[->] (0,-2) -- (0,2) node[above] {\(y\)};
  % Grafico della retta: y = 2x - 4, dominio limitato a [1,3]
  \draw[domain=0.3:3, smooth, variable=\x, blue, very thick] plot ({\x}, {2*\x-4});
  % Evidenziamo l'intersezione con l'asse x (x=2, y=0)
  \draw[dashed] (2,0) -- (2,0.5);
  \node at (2,-0.3) {\(2\)};
  \node[blue] at (2,0.7) {\(\bullet\)};
\end{tikzpicture}
\end{center}

\bigskip

\subsubsection*{Polinomi di Secondo Grado}
Un polinomio di secondo grado ha la forma
\[
P(x)=ax^2+bx+c \quad (a\neq 0).
\]
Per trovare gli zeri si risolve l'equazione
\[
ax^2+bx+c=0
\]
utilizzando la formula
\[
x=\frac{-b\pm \sqrt{b^2-4ac}}{2a}.
\]
Il termine \(b^2-4ac\) è detto \textit{discriminante} e ne determina il numero e la natura delle soluzioni.

\textbf{Esempio:} Consideriamo il polinomio
\[
P(x)=x^2-5x+6.
\]
Qui \(a=1\), \(b=-5\) e \(c=6\). Calcoliamo il discriminante:
\[
\Delta=(-5)^2-4\cdot1\cdot6=25-24=1.
\]
Essendo \(\Delta>0\) esistono due soluzioni reali distinte:
\[
x=\frac{-(-5)\pm \sqrt{1}}{2\cdot1}=\frac{5\pm 1}{2},
\]
cioè
\[
x=3 \quad \text{e} \quad x=2.
\]
Il polinomio si scompone dunque in:
\[
x^2-5x+6=(x-2)(x-3).
\]

\medskip

\begin{center}
\begin{tikzpicture}[scale=0.8]
  % Assi cartesiani
  \draw[->] (-1,0) -- (5,0) node[right] {\(x\)};
  \draw[->] (0,-2) -- (0,4) node[above] {\(y\)};
  % Grafico della parabola: y = x^2 - 5x + 6
  \draw[domain=0.0:5, smooth, variable=\x, red, very thick] plot ({\x}, {(\x)^2-5*(\x)+6});
  % Intersezioni con l'asse x (zeri)
  \draw[dashed] (2,0) -- (2,2);
  \draw[dashed] (3,0) -- (3,2);
  \node at (2,-0.3) {\(2\)};
  \node at (3,-0.3) {\(3\)};
  \node[red] at (2,1.8) {\(\bullet\)};
  \node[red] at (3,1.8) {\(\bullet\)};
\end{tikzpicture}
\end{center}

Questi esempi evidenziano come, partendo dalla definizione di polinomio, risolvere l'equazione \(P(x)=0\) significhi trovare i punti in cui il grafico del polinomio interseca l'asse \(x\), detti zeri del polinomio.

\subsec{Equazioni Fratte [1, 2, 3]}
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


\subsec{Disequazioni di Primo e Secondo Grado [1, 2, 3, 4]}
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

\subsec{Razionalizzazione del Denominatore [1]}

Avere il denominatore razionale in una frazione è importante per ottenere una forma \q{semplice} e standardizzata dell'espressione. Un denominatore razionale facilita il confronto tra frazioni, semplifica ulteriori operazioni algebriche (come somma, sottrazione o confronto) e rende la notazione più chiara ed elegante. In altre parole, esprimere una frazione senza radicali o numeri irrazionali nel denominatore permette una manipolazione più agevole e una migliore interpretazione dei risultati.

\bigskip

\textbf{Metodi per Razionalizzare il Denominatore:}

\begin{enumerate}
  \item \textbf{Monomio Irrazionale:} Se il denominatore è un singolo termine contenente un radicale, per esempio \(\sqrt{a}\), si moltiplica numeratore e denominatore per \(\sqrt{a}\) in modo da ottenere:
    \[
    \frac{1}{\sqrt{a}} = \frac{\sqrt{a}}{a}.
    \]
  \item \textbf{Binomio con Radicali:} Se il denominatore è un binomio contenente un termine irrazionale, ad esempio \(a+\sqrt{b}\), si moltiplica numeratore e denominatore per il coniugato \(a-\sqrt{b}\). Questo sfrutta l'identità:
    \[
    (a+\sqrt{b})(a-\sqrt{b}) = a^2 - b.
    \]
  \item \textbf{Denomini Più Complessi:} Per espressioni con più termini o radicali di ordine superiore, si applicano metodi analoghi, cercando di eliminare i radicali mediante opportuni prodotti con espressioni coniugate o simili.
\end{enumerate}

\bigskip

\textbf{Esempi Pratici:}

\medskip

\textbf{Esempio 1:} Razionalizzare il denominatore di 
\[
\frac{1}{\sqrt{2}}.
\]
Moltiplichiamo numeratore e denominatore per \(\sqrt{2}\):
\[
\frac{1}{\sqrt{2}} = \frac{1 \cdot \sqrt{2}}{\sqrt{2} \cdot \sqrt{2}} = \frac{\sqrt{2}}{2}.
\]

\medskip

\textbf{Esempio 2:} Razionalizzare il denominatore di
\[
\frac{3}{2+\sqrt{3}}.
\]
Moltiplichiamo numeratore e denominatore per il coniugato \(2-\sqrt{3}\):
\[
\frac{3}{2+\sqrt{3}} = \frac{3(2-\sqrt{3})}{(2+\sqrt{3})(2-\sqrt{3})} = \frac{3(2-\sqrt{3})}{4-3} = 3(2-\sqrt{3}).
\]

\medskip

\textbf{Esempio 3:} Razionalizzare il denominatore di
\[
\frac{5}{\sqrt{5} - 2}.
\]
Moltiplichiamo numeratore e denominatore per il coniugato \(\sqrt{5}+2\):
\[
\frac{5}{\sqrt{5} - 2} = \frac{5(\sqrt{5}+2)}{(\sqrt{5}-2)(\sqrt{5}+2)} = \frac{5(\sqrt{5}+2)}{5-4} = 5(\sqrt{5}+2).
\]

Questi esempi mostrano come, applicando il metodo del coniugato o moltiplicando per il radicale opportuno, si ottenga una frazione con denominatore razionale, semplificando così l'espressione e rendendola più agevole per ulteriori manipolazioni.

\subsec{Geometria Analitica [3]}%molto più sintetico che su Unione
\begin{Definition}[Varietà Algebrica]
Sia \(f(x,y)\in \mathbb{R}[x,y]\) un polinomio in due variabili. La \textit{varietà algebrica} associata a \(f\) è definita come l'insieme
\[
\mathcal{V}(f)=\{(x,y)\in \mathbb{R}^2 \mid f(x,y)=0\}.
\]
\end{Definition}

Questo significa che ogni polinomio in due variabili può essere rappresentato graficamente come il luogo dei punti del piano cartesiano che soddisfano l'equazione \(f(x,y)=0\).

Un insieme che si presenta come varietà algebrica è costituito da coppie ordinate di numeri reali \((x,y)\) appartenenti a \(\mathbb{R}^2\). Ogni coppia \((x,y)\) può essere rappresentata come un punto nel piano cartesiano: partendo dall'origine, ci si sposta \(x\) unità verso destra (o verso sinistra se \(x\) è negativo) e \(y\) unità verso l'alto (o verso il basso se \(y\) è negativo), ottenendo così la posizione esatta del punto. In questo modo, le varietà algebriche, costituite dall'insieme delle soluzioni di equazioni polinomiali in due variabili, possono essere visualizzate geometricamente nel piano.

\bigskip

\textbf{Esempi:}

\begin{itemize}
  \item \textbf{Circonferenza:} Il polinomio
  \[
  f(x,y)=x^2+y^2-1
  \]
  definisce la circonferenza unitaria:
  \[
  \mathcal{V}(f)=\{(x,y)\in \mathbb{R}^2 \mid x^2+y^2=1\}.
  \]
  \begin{center}
  \begin{tikzpicture}[scale=1]
    % Assi cartesiani
    \draw[->] (-1.5,0) -- (1.5,0) node[right] {\(x\)};
    \draw[->] (0,-1.5) -- (0,1.5) node[above] {\(y\)};
    % Circonferenza unitaria
    \draw[blue, thick] (0,0) circle (1);
  \end{tikzpicture}
  \end{center}

  \item \textbf{Parabola:} Il polinomio
  \[
  f(x,y)=y-x^2
  \]
  rappresenta la parabola:
  \[
  \mathcal{V}(f)=\{(x,y)\in \mathbb{R}^2 \mid y=x^2\}.
  \]
  \begin{center}
  \begin{tikzpicture}[scale=1]
    % Assi cartesiani
    \draw[->] (-2,0) -- (2,0) node[right] {\(x\)};
    \draw[->] (0,-0.5) -- (0,4) node[above] {\(y\)};
    % Grafico della parabola: y = x^2
    \draw[domain=-1.5:1.5, smooth, variable=\x, blue, thick] plot ({\x}, {\x*\x});
  \end{tikzpicture}
  \end{center}

  \item \textbf{Iperbole:} Il polinomio
  \[
  f(x,y)=xy-1
  \]
  definisce l'iperbole:
  \[
  \mathcal{V}(f)=\{(x,y)\in \mathbb{R}^2 \mid xy=1\}.
  \]
  \begin{center}
  \begin{tikzpicture}[scale=1]
    % Assi cartesiani
    \draw[->] (-2,0) -- (2,0) node[right] {\(x\)};
    \draw[->] (0,-2) -- (0,2) node[above] {\(y\)};
    % Primo ramo: per x>0, y = 1/x
    \draw[domain=0.5:2, smooth, variable=\x, blue, thick] plot ({\x}, {1/\x});
    % Secondo ramo: per x<0, y = 1/x
    \draw[domain=-2:-0.5, smooth, variable=\x, blue, thick] plot ({\x}, {1/\x});
  \end{tikzpicture}
  \end{center}

  \item \textbf{Curva con Cuspide:} Il polinomio
  \[
  f(x,y)=y^2-x^3-x^2
  \]
  definisce una curva algebrica con cuspide, che mostra comportamenti particolari nei punti singolari. La curva soddisfa
  \[
  y^2=x^3+x^2.
  \]
  \begin{center}
  \begin{tikzpicture}[scale=0.8]
    % Assi cartesiani
    \draw[->] (-2,0) -- (2,0) node[right] {\(x\)};
    \draw[->] (0,-1.5) -- (0,1.5) node[above] {\(y\)};
    % Grafico approssimato della curva con cuspide
    \draw[domain=-1.5:0, smooth, variable=\x, blue, thick] plot ({\x}, {sqrt(max(0, \x*\x*(1+\x)))});
    \draw[domain=-1.5:0, smooth, variable=\x, blue, thick] plot ({\x}, {-sqrt(max(0, \x*\x*(1+\x)))});
    \draw[domain=0:1.5, smooth, variable=\x, blue, thick] plot ({\x}, {sqrt(\x*\x*(1+\x))});
    \draw[domain=0:1.5, smooth, variable=\x, blue, thick] plot ({\x}, {-sqrt(\x*\x*(1+\x))});
  \end{tikzpicture}
  \end{center}
\end{itemize}

\bigskip

\subsubsection*{Vantaggi della Geometria Analitica}
La geometria analitica permette di tradurre problemi geometrici in problemi algebrici, utilizzando i polinomi come strumenti espressivi per descrivere curve e superfici. Tra i principali vantaggi troviamo:
\begin{itemize}
  \item \textbf{Calcolo Esplicito:} Le proprietà geometriche, come intersezioni, tangenti, aree, ecc., possono essere determinate tramite operazioni algebriche.
  \item \textbf{Formalità e Rigorosità:} La rappresentazione di una varietà algebrica tramite equazioni polinomiali offre un approccio formale e sistematico, facilitando la dimostrazione di teoremi e la classificazione delle curve.
  \item \textbf{Strumenti Computazionali:} Le tecniche di algebra computazionale permettono di risolvere sistemi di equazioni e di studiare la struttura delle varietà, anche in casi complessi.
  \item \textbf{Unificazione di Teorie:} La geometria analitica funge da ponte tra l'algebra e la geometria, rendendo possibile l'applicazione di metodi algebrici per risolvere problemi geometrici e viceversa.
\end{itemize}

Grazie a questi vantaggi, la geometria analitica rappresenta un potente strumento per affrontare problemi in vari ambiti della matematica, dalla risoluzione delle equazioni alle applicazioni in fisica e ingegneria, offrendo un linguaggio unificato e ricco per lo studio della forma e della struttura.


\subsec{Regola di Cartesio [2]}
% Introduzione alla Regola di Cartesio

Per comprendere il significato della Regola di Cartesio, è fondamentale conoscere alcuni concetti relativi ai polinomi e alle loro radici. Una \emph{radice} di un polinomio \(P(x)\) è un numero reale \(r\) tale che
\[
P(r)=0.
\]
In termini geometrici, \(r\) rappresenta l'intersezione del grafico di \(P(x)\) con l'asse \(x\).

La \emph{molteplicità} di una radice \(r\) indica il numero di volte che il fattore \((x-r)\) compare nella fattorizzazione del polinomio. Ad esempio, se un polinomio si scrive come
\[
P(x)=(x-r)^k Q(x),
\]
con \(Q(r)\neq 0\), si dice che \(r\) è una radice di molteplicità \(k\). Quando si conta il numero di radici positive (o negative) di un polinomio, tali radici vengono considerate in base alla loro molteplicità.

La Regola di Cartesio stabilisce, infatti, un limite superiore al numero di radici positive reali (contate con la loro molteplicità) di un polinomio, in relazione alle variazioni di segno che si osservano nella sequenza dei suoi coefficienti, ordinati in modo decrescente per grado. Con questa premessa, possiamo enunciare il teorema.

\begin{Theorem}[Regola di Cartesio]
Sia 
\[
P(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_0,\quad a_n\neq 0,
\]
un polinomio a coefficienti reali, ordinato in modo decrescente per il grado. Allora il numero di radici positive reali di \(P(x)\) (contate con la loro molteplicità) è al più pari al numero di variazioni di segno nella sequenza dei coefficienti \(\{a_n, a_{n-1},\dots,a_0\}\). Inoltre, la differenza tra il numero di variazioni di segno e il numero di radici positive è un numero pari.
\end{Theorem}

Partendo dalla Regola di Cartesio, che fornisce un limite superiore sul numero di radici positive di un polinomio in relazione alle variazioni di segno nei suoi coefficienti, possiamo dedurre un risultato fondamentale sull'insieme delle radici reali di un polinomio. In particolare, questo corollario afferma che un polinomio non costante di grado \(n\) non può avere più di \(n\) radici reali, contate con la loro molteplicità. Tale affermazione è in accordo con il Teorema Fondamentale dell'Algebra, il quale garantisce che un polinomio di grado \(n\) abbia esattamente \(n\) radici nel campo dei numeri complessi (contando la molteplicità), quindi le radici reali costituiscono un sottoinsieme di esse.

\begin{Corollary}
Sia \(P(x)\) un polinomio non costante di grado \(n\) a coefficienti reali. Allora il numero totale di radici reali di \(P(x)\) (contate con la loro molteplicità) non supera \(n\).
\end{Corollary}

\begin{proof}[Dimostrazione]
Applichiamo la regola di Cartesio al polinomio \(P(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_0\). Essa garantisce che il numero di radici positive non superi il numero di variazioni di segno nella sequenza dei coefficienti, e analogamente, sostituendo \(x\) con \(-x\), il numero di radici negative non superi il numero di variazioni di segno nella sequenza dei coefficienti di \(P(-x)\).

Poiché le radici reali totali sono la somma delle radici positive e negative, il loro numero complessivo è limitato dalla somma dei due limiti superiori, i quali non possono eccedere il grado \(n\) del polinomio. In effetti, se \(P(x)\) avesse più di \(n\) radici reali, ciò contraddirebbe il fatto che un polinomio di grado \(n\) non può avere più di \(n\) radici (contate con la molteplicità), in accordo con il Teorema Fondamentale dell'Algebra.

Pertanto, il numero di radici reali di \(P(x)\) non supera \(n\), il che rappresenta un risultato fondamentale dell'algebra e si collega direttamente al Teorema Fondamentale dell'Algebra.
\end{proof}

\begin{esempio}
Consideriamo il polinomio 
\[
P(x)=x^3-6x^2+11x-6.
\]
I coefficienti sono \(1,\ -6,\ 11,\ -6\). Analizzando i segni, notiamo le seguenti variazioni:
\[
1\to -6,\quad -6\to 11,\quad 11\to -6.
\]
Ci sono quindi 3 variazioni di segno, il che implica, secondo la Regola di Cartesio, che il numero di radici positive reali di \(P(x)\) sia al più 3 oppure 1 (la differenza deve essere pari). In questo caso, infatti, \(P(x)\) ha le radici \(x=1\), \(x=2\) e \(x=3\), in totale 3 radici positive, che rientrano nel limite stabilito.
\end{esempio}

\begin{esempio}
Consideriamo il polinomio
\[
Q(x)=x^4-3x^3+2x^2+4x-8.
\]
La sequenza dei coefficienti è: \(1,\ -3,\ 2,\ 4,\ -8\). Le variazioni di segno sono:
\[
1\to -3\quad (\text{variazione}),\quad -3\to 2\quad (\text{variazione}),
\]
\[
\quad 2\to 4\quad (\text{nessuna variazione}),\quad 4\to -8\quad (\text{variazione}).
\]
Pertanto, abbiamo 3 variazioni di segno. Ciò significa che il numero di radici positive reali di \(Q(x)\) è al più 3 oppure 1. Anche se un'analisi dettagliata o l'uso di strumenti numerici può rivelare il numero esatto di radici positive, la Regola di Cartesio ci fornisce un limite superiore utile.
\end{esempio}

\begin{esempio}
Consideriamo il polinomio
\[
R(x)=2x^3+5x^2-3x-6.
\]
Il grado di \(R(x)\) è 3, dunque, per il corollario, il numero totale di radici reali non può superare 3. Esaminiamo la sequenza dei coefficienti: \(2,\ 5,\ -3,\ -6\).  
Si osserva una variazione di segno tra \(5\) (positivo) e \(-3\) (negativo), mentre gli altri termini non introducono ulteriori variazioni (poiché \(2\) e \(5\) sono entrambi positivi, e \(-3\) e \(-6\) sono entrambi negativi).  
Quindi, la Regola di Cartesio ci indica che \(R(x)\) possiede al massimo 1 radice positiva. Complessivamente, il numero totale di radici reali (positive e negative) è comunque limitato dal grado 3 del polinomio, in accordo con il corollario che afferma che un polinomio di grado \(n\) non può avere più di \(n\) radici reali (contate con la molteplicità).
\end{esempio}



\subsec{Equazioni Parametriche [2]}
Le equazioni parametriche sono un sistema di equazioni in cui le coordinate di un punto sono espresse in funzione di uno o più parametri. Invece di descrivere direttamente la relazione tra le variabili, come avviene in un'equazione esplicita del tipo \(y=f(x)\), le equazioni parametriche rappresentano ogni coordinata (ad esempio \(x\) e \(y\) nel piano, o \(x\), \(y\) e \(z\) nello spazio) in termini di un parametro \(t\) (o di più parametri). Per esempio, una curva nel piano può essere definita dalle equazioni
\[
\begin{cases}
x = g(t),\\[1mm]
y = h(t),
\end{cases}
\]
con \(t\) che varia in un intervallo definito. Questo approccio permette di descrivere in maniera flessibile curve che potrebbero non essere rappresentabili come funzioni esplicite, come ad esempio curve chiuse o traiettorie complesse. Le equazioni parametriche trovano applicazione in molti ambiti della matematica e della fisica, facilitando lo studio di movimenti, traiettorie e proprietà geometriche come la lunghezza e la curvatura delle curve.
\subsubsection*{Equazioni Parametriche di Primo Grado}
Le equazioni parametriche di primo grado descrivono le rette nel piano. In questo caso, le coordinate \(x\) e \(y\) di un punto vengono espresse come funzioni lineari di un parametro \(t\). Ad esempio, consideriamo il sistema:
\[
\begin{cases}
x=1+2t,\\[1mm]
y=3-t,
\end{cases}\quad t\in\mathbb{R}.
\]
Questo sistema descrive una retta nel piano cartesiano. La rappresentazione grafica è la seguente:

\begin{center}
\begin{tikzpicture}[scale=0.8]
  % Assi cartesiani
  \draw[->] (-1,0) -- (5,0) node[right] {\(x\)};
  \draw[->] (0,-1) -- (0,5) node[above] {\(y\)};
  % Grafico della retta parametrica
  \draw[blue, very thick, domain=-2:2, variable=\t] plot ({1+2*\t}, {3-\t});
\end{tikzpicture}
\end{center}

\subsubsection*{Equazioni Parametriche di Secondo Grado e Superiore}
Quando le funzioni che descrivono \(x\) e \(y\) sono polinomiali di grado superiore a uno, si ottengono curve come parabole, cubiche, o altre curve algebriche. Ad esempio:

\textbf{Esempio 1 (Parabola):}
\[
\begin{cases}
x=t,\\[1mm]
y=t^2,
\end{cases}\quad t\in[-2,2].
\]
La rappresentazione grafica di questa parabola è:

\begin{center}
\begin{tikzpicture}[scale=0.8]
  % Assi cartesiani
  \draw[->] (-3,0) -- (3,0) node[right] {\(x\)};
  \draw[->] (0,-1) -- (0,5) node[above] {\(y\)};
  % Grafico della parabola: y = t^2
  \draw[red, very thick, domain=-2:2, variable=\t] plot ({\t}, {\t*\t});
\end{tikzpicture}
\end{center}

\textbf{Esempio 2 (Curva Cubica):}
\[
\begin{cases}
x=t,\\[1mm]
y=t^3,
\end{cases}\quad t\in[-2,2].
\]
La rappresentazione grafica della curva cubica è:

\begin{center}
\begin{tikzpicture}[scale=0.8]
  % Assi cartesiani
  \draw[->] (-3,0) -- (3,0) node[right] {\(x\)};
  \draw[->] (0,-3) -- (0,3) node[above] {\(y\)};
  % Grafico della curva cubica: y = t^3
  \draw[green, very thick, domain=-1.5:1.5, variable=\t] plot ({\t}, {\t*\t*\t});
\end{tikzpicture}
\end{center}

\subsubsection*{Equazioni Parametriche Goniometriche}
Le equazioni parametriche goniometriche utilizzano funzioni trigonometriche per esprimere le coordinate, risultando particolarmente utili nelle applicazioni che richiedono una descrizione periodica o rotazionale. Sebbene in questa fase non abbiamo ancora approfondito le funzioni goniometriche, queste equazioni faranno parte del programma della terza sezione. Si consiglia di rivedere questa parte successivamente per una comprensione più completa.

\textbf{Esempio 1 (Circonferenza):}
\[
\begin{cases}
x=\cos(t),\\[1mm]
y=\sin(t),
\end{cases}\quad t\in[0,2\pi].
\]
La rappresentazione grafica della circonferenza unitaria è:

\begin{center}
\begin{tikzpicture}[scale=2]
  % Assi cartesiani
  \draw[->] (-1.5,0) -- (1.5,0) node[right] {\(x\)};
  \draw[->] (0,-1.5) -- (0,1.5) node[above] {\(y\)};
  % Grafico della circonferenza
  \draw[blue, very thick, domain=0:360, variable=\t] plot ({cos(\t)}, {sin(\t)});
\end{tikzpicture}
\end{center}

\textbf{Esempio 2 (Curva di Lissajous):}
\[
\begin{cases}
x=\cos(3t),\\[1mm]
y=\sin(2t),
\end{cases}\quad t\in[0,2\pi].
\]
La rappresentazione grafica della curva di Lissajous è:

\begin{center}
\begin{tikzpicture}[scale=2]
  % Assi cartesiani
  \draw[->] (-1.5,0) -- (1.5,0) node[right] {\(x\)};
  \draw[->] (0,-1.5) -- (0,1.5) node[above] {\(y\)};
  % Grafico della curva di Lissajous
  \draw[red, very thick, domain=0:360, variable=\t] plot ({cos(3*\t)}, {sin(2*\t)});
\end{tikzpicture}
\end{center}

In conclusione, le equazioni parametriche rappresentano uno strumento essenziale per descrivere in modo flessibile e dettagliato curve e traiettorie, sia in ambito algebrico che geometrico. Esse permettono di esprimere le coordinate dei punti in funzione di uno o più parametri, facilitando la rappresentazione di curve complesse che non possono essere descritte con un'unica equazione esplicita. Questa modalità di rappresentazione evidenzia il profondo legame tra algebra e geometria e costituisce una base fondamentale per lo studio avanzato delle proprietà delle curve, con applicazioni in numerosi campi della matematica e della fisica.

\subsec{I Logaritmi [1] }
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

\subsec{Esponenti Reali [1]}
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

\subsec{Esponenziali e Logaritmiche sul Grafico [4]}
\subsubsection*{Grafico di Funzioni Esponenziali}
Una funzione esponenziale ha la forma
\[
f(x)=a\cdot b^x,
\]
dove \(a\) è il coefficiente iniziale e \(b>0\) è la base. Le regole principali per disegnare il grafico sono:
\begin{itemize}
  \item \textbf{Dominio e Immagine:} Il dominio è \(\mathbb{R}\); se \(a>0\) l'immagine è \((0,+\infty)\), mentre se \(a<0\) l'immagine è \((-\infty,0)\).
  \item \textbf{Asintoto:} L'asse \(y=0\) è un asintoto orizzontale.
  \item \textbf{Comportamento:} Se \(b>1\) la funzione è crescente; se \(0<b<1\) la funzione è decrescente.
  \item \textbf{Intercetta:} L'intercetta con l'asse \(y\) è \(f(0)=a\).
\end{itemize}

\textbf{Esempio:} Consideriamo la funzione esponenziale
\[
f(x)=2\cdot 3^x.
\]
Qui il dominio è \(\mathbb{R}\), l'immagine è \((0,+\infty)\) (poiché \(a=2>0\)), l'asintoto orizzontale è \(y=0\) e \(f(0)=2\).

\begin{center}
\begin{tikzpicture}[scale=0.6]
  % Assi cartesiani
  \draw[->] (-2,0) -- (2,0) node[right] {\(x\)};
  \draw[->] (0,-1) -- (0,10) node[above] {\(y\)};
  % Asintoto orizzontale
  \draw[dashed] (-2,0) -- (2,0);
  % Grafico della funzione: f(x)=2*3^x
  \draw[domain=-2.0:1.5, smooth, variable=\x, blue, very thick] plot ({\x}, {2*3^\x});
\end{tikzpicture}
\end{center}

\bigskip

\subsubsection*{Grafico di Funzioni Logaritmiche}
Una funzione logaritmica ha la forma
\[
g(x)=a+\log_b(x),
\]
con \(b>0\) e \(b\neq 1\). Le regole principali per disegnare il grafico sono:
\begin{itemize}
  \item \textbf{Dominio e Immagine:} Il dominio è \((0,+\infty)\) e l'immagine è \(\mathbb{R}\).
  \item \textbf{Asintoto:} L'asse \(x=0\) è un asintoto verticale.
  \item \textbf{Comportamento:} Se \(b>1\) la funzione è crescente; se \(0<b<1\) la funzione è decrescente.
  \item \textbf{Intercetta:} Poiché \(\log_b(1)=0\), \(g(1)=a\) è l'intercetta con l'asse \(y\).
\end{itemize}

\textbf{Esempio:} Consideriamo la funzione logaritmica
\[
g(x)=1+\log_2(x).
\]
Qui il dominio è \((0,+\infty)\), l'asintoto verticale è \(x=0\) e \(g(1)=1\).

\begin{center}
\begin{tikzpicture}[scale=0.8]
  % Assi cartesiani
  \draw[->] (0, -1) -- (5, -1) node[right] {\(x\)};
  \draw[->] (0, -1) -- (0, 3) node[above] {\(y\)};
  % Asintoto verticale
  \draw[dashed] (0, -1) -- (0, 3);
  % Grafico della funzione: g(x)=1+log_2(x)
  \draw[domain=0.2:4, smooth, variable=\x, red, very thick] plot ({\x}, {1+ln(\x)/ln(2)});
\end{tikzpicture}
\end{center}

\bigskip

\begin{esempio}
Consideriamo la funzione esponenziale trasformata
\[
f(x) = -3\cdot 2^{x-2} + 4.
\]
Per costruire il grafico, osserviamo che:
\begin{itemize}
  \item \textbf{Dominio:} \(x\in \mathbb{R}\).
  \item \textbf{Intercetta:} \(f(2)= -3\cdot 2^{0}+4 = 1\).
  \item \textbf{Asintoto orizzontale:} Poiché per \(x\to -\infty\) \(2^{x-2}\to 0\), la funzione tende a \(4\).
  \item \textbf{Comportamento:} Per \(x\to +\infty\) \(2^{x-2}\to +\infty\) e, moltiplicato per \(-3\), \(f(x)\) tende a \(-\infty\).
\end{itemize}
Il grafico seguente, realizzato per \(x\) compreso tra \(-2\) e \(5\), mostra l'andamento di \(f(x)\):
\begin{center}
\begin{tikzpicture}[scale=0.6]
  % Assi cartesiani
  \draw[->] (-2,0) -- (4,0) node[right] {\(x\)};
  \draw[->] (0,-7) -- (0,5) node[above] {\(y\)};
  % Asintoto orizzontale: y=4
  \draw[dashed] (-2,4) -- (6,4);
  \node[above right] at (6,4) {\(y=4\)};
  % Grafico della funzione f(x)= -3*2^(x-2)+4
  \draw[domain=-2:3.7, smooth, variable=\x, blue, very thick] plot ({\x}, {-3*2^(\x-2)+4});
\end{tikzpicture}
\end{center}
\end{esempio}

\begin{esempio}
Consideriamo la funzione logaritmica trasformata
\[
g(x) = 2 + \log_{1/2}(x-1).
\]
Ricordiamo che \(\log_{1/2}(x-1)=\frac{\ln(x-1)}{\ln(1/2)}\). Per il grafico:
\begin{itemize}
  \item \textbf{Dominio:} \(x>1\).
  \item \textbf{Asintoto verticale:} \(x=1\).
  \item \textbf{Intercetta:} Quando \(x=2\), si ha \(g(2)=2+\log_{1/2}(1)=2\).
  \item \textbf{Comportamento:} Essendo la base \(1/2\) minore di 1, la funzione è decrescente.
\end{itemize}
Il grafico seguente, disegnato per \(x\) compreso tra \(1.1\) e \(5\), illustra l'andamento di \(g(x)\):
\begin{center}
\begin{tikzpicture}[scale=0.8]
  % Assi cartesiani
  \draw[->] (0,0) -- (5,0) node[right] {\(x\)};
  \draw[->] (0,-2) -- (0,4) node[above] {\(y\)};
  % Asintoto verticale: x=1
  \draw[dashed] (1,-2) -- (1,4);
  \node[below left] at (1,0) {\(x=1\)};
  % Grafico della funzione g(x)= 2+log_(1/2)(x-1)
  \draw[domain=1.1:5, smooth, variable=\x, red, very thick] plot ({\x}, {2+ln(\x-1)/ln(0.5)});
\end{tikzpicture}
\end{center}
\end{esempio}

\subsec{Metodo della Variabile Ausiliaria [1]}
% Introduzione al Metodo della Variabile Ausiliaria per Equazioni Esponenziali e Logaritmiche
Il metodo della variabile ausiliaria consiste nel sostituire un'espressione ripetuta o complessa con una nuova variabile, al fine di trasformare un'equazione difficile in una forma più semplice, spesso polinomiale. Questo approccio è particolarmente utile per equazioni esponenziali e logaritmiche. Ad esempio, in un'equazione esponenziale si può porre \(u=b^x\) in modo da ridurla ad un'equazione in \(u\); analogamente, per un'equazione logaritmica, è possibile porre \(u=\log_b(x)\) (o una funzione simile) per semplificarne la struttura. Dopo aver risolto l'equazione in \(u\), si torna alla variabile originale mediante la sostituzione inversa.

\begin{esempio}
Consideriamo l'equazione esponenziale
\[
2^{2x} - 3\cdot 2^x + 2 = 0.
\]
Poniamo \(u = 2^x\). L'equazione diventa:
\[
u^2 - 3u + 2 = 0.
\]
Questo si fattorizza come:
\[
(u-1)(u-2) = 0,
\]
quindi \(u = 1\) oppure \(u = 2\). Ritornando alla variabile originale:
\[
2^x = 1 \quad \Rightarrow \quad x = 0,
\]
\[
2^x = 2 \quad \Rightarrow \quad x = 1.
\]

\medskip

\textbf{Grafico:} Mostriamo il grafico della funzione 
\[
f(x)=2^{2x}-3\cdot 2^x+2,
\]
insieme alla funzione ausiliaria \(g(x)=2^x\), per evidenziare le radici \(x=0\) e \(x=1\).

\begin{center}
\begin{tikzpicture}[scale=0.8]
  % Assi cartesiani
  \draw[->] (-1,0) -- (3,0) node[right] {\(x\)};
  \draw[->] (0,-1) -- (0,3) node[above] {\(y\)};
  % Grafico di g(x)=2^x (in verde)
  \draw[domain=-1:2, smooth, variable=\x, green, very thick] plot ({\x}, {2^\x});
  % Grafico di f(x)=2^(2x)-3*2^x+2 (in blu)
  \draw[domain=-1:2, smooth, variable=\x, blue, very thick] plot ({\x}, {2^(2*\x)-3*2^\x+2});
  % Evidenziamo le radici: x=0 e x=1 per f(x)
  \filldraw[red] (0,0) circle (2pt);
  \filldraw[red] (1,0) circle (2pt);
\end{tikzpicture}
\end{center}
\end{esempio}

\begin{esempio}
Consideriamo l'equazione logaritmica
\[
\sqrt{\log_2(x)} + \log_2(x) - 6 = 0.
\]
Poniamo \(u = \log_2(x)\), così che l'equazione diventa:
\[
\sqrt{u} + u - 6 = 0.
\]
Per semplificarla ulteriormente, poniamo \(v = \sqrt{u}\), dunque \(u = v^2\). L'equazione si trasforma in:
\[
v + v^2 - 6 = 0 \quad \Longrightarrow \quad v^2 + v - 6 = 0.
\]
Il discriminante è \(1+24=25\), e le soluzioni sono:
\[
v = \frac{-1 \pm 5}{2}.
\]
Poiché \(v\) rappresenta una radice quadrata, deve essere non negativo; dunque accettiamo solo \(v = 2\). Quindi \(u = v^2 = 4\) e, infine, \(x = 2^u = 2^4 = 16\).

\medskip

\textbf{Grafico:} Di seguito il grafico della funzione
\[
h(x)=\sqrt{\log_2(x)} + \log_2(x) - 6,
\]
che mostra chiaramente che \(x=16\) è la radice dell'equazione.

\begin{center}
\begin{tikzpicture}[scale=0.4]
  % Assi cartesiani
  \draw[->] (0, -3) -- (0, 3) node[above] {\(y\)};
  \draw[->] (0, 0) -- (30, 0) node[right] {\(x\)};
  % Grafico della funzione h(x) = sqrt(log_2(x)) + log_2(x) - 6
  \draw[domain=2:32, smooth, variable=\x, blue, very thick] plot ({\x}, {sqrt(ln(\x)/ln(2)) + ln(\x)/ln(2) - 6});
  % Evidenziamo la radice x=16
  \filldraw[red] (16,0) circle (4pt);
  \node[above] at (16,0) {\(16\)};
\end{tikzpicture}
\end{center}
\end{esempio}

\subsec{Disequazioni e Logaritmiche sul Grafico [4]}
Le disequazioni esponenziali e logaritmiche si risolvono sfruttando le proprietà di monotonia delle funzioni esponenziali e logaritmiche. In generale:

\begin{itemize}
  \item Se \(b>1\), la funzione esponenziale \(f(x)=b^x\) è crescente, mentre se \(0<b<1\) essa è decrescente. Questo implica che, per un'inequazione del tipo 
    \[
    b^x > k,
    \]
    se \(b>1\) si può applicare il logaritmo (a base \(b\)) mantenendo il verso dell'inequazione, ottenendo \(x>\log_b(k)\). Se invece \(0<b<1\), l'inequazione diventa \(x<\log_b(k)\).
    
  \item Analogamente, la funzione logaritmica \(g(x)=\log_b(x)\) è crescente se \(b>1\) e decrescente se \(0<b<1\). Quindi, per un'inequazione
    \[
    \log_b(x) > c,
    \]
    se \(b>1\) si ha \(x>b^c\) e se \(0<b<1\) l'ordine inverte.
    
  \item È importante ricordare che il dominio di una funzione logaritmica è \((0,+\infty)\), pertanto, prima di risolvere una disequazione logaritmica, bisogna sempre considerare le condizioni sul dominio.
\end{itemize}

Di seguito, presentiamo alcuni esempi pratici con i relativi grafici.

\begin{esempio}
Consideriamo la disequazione esponenziale
\[
2^{\,x-1} > 8.
\]
Osserviamo che \(8=2^3\), dunque l'inequazione diventa
\[
2^{\,x-1} > 2^3.
\]
Poiché la funzione \(2^x\) è crescente, si ha
\[
x-1 > 3 \quad \Longrightarrow \quad x>4.
\]

\medskip

\textbf{Grafico:} Nel grafico seguente si rappresenta la funzione \(f(x)=2^{\,x-1}\) (in blu) e la retta orizzontale \(y=8\) (in rosso). L'area in cui \(f(x)>8\) corrisponde a \(x>4\).

\begin{center}
\begin{tikzpicture}[scale=0.8]
  % Assi cartesiani
  \draw[->] (0,0) -- (7,0) node[right] {\(x\)};
  \draw[->] (0,-1) -- (0,9) node[above] {\(y\)};
  % Grafico della funzione f(x)=2^(x-1)
  \draw[domain=0:4.2, smooth, variable=\x, blue, very thick] plot ({\x}, {2^(\x-1)});
  % Linea orizzontale y=8
  \draw[dashed, red, very thick] (0,8) -- (7,8);
  % Evidenziazione del punto di intersezione
  \filldraw[red] (4,8) circle (2pt);
  \node[red, above right] at (4,8) {\(x=4\)};
\end{tikzpicture}
\end{center}
\end{esempio}

\begin{esempio}
Consideriamo ora una disequazione logaritmica
\[
\log_3(x+1) < 2.
\]
Per risolverla, notiamo che, essendo la funzione logaritmica a base \(3>1\) crescente, l'inequazione è equivalente a
\[
x+1 < 3^2,
\]
cioè
\[
x+1 < 9 \quad \Longrightarrow \quad x < 8.
\]
Ricordiamo che il dominio della funzione \(\log_3(x+1)\) è \(x>-1\). Quindi la soluzione completa è:
\[
-1 < x < 8.
\]

\medskip

\textbf{Grafico:} Nel grafico seguente si rappresenta la funzione \(g(x)=\log_3(x+1)\) (in verde) e la retta orizzontale \(y=2\) (in rosso). L'area in cui \(g(x)<2\) è evidenziata per \(x<8\) (considerando anche il dominio \(x>-1\)).

\begin{center}
\begin{tikzpicture}[scale=0.7]
  % Assi cartesiani
  \draw[->] (-2.5,0) -- (10,0) node[right] {\(x\)};
  \draw[->] (0,-3) -- (0,4) node[above] {\(y\)};
  % Asintoto verticale x = -1 (linea tratteggiata)
  \draw[dashed] (-1, -1) -- (-1, 4);
  \node[above left] at (-1,0) {\(x=-1\)};
  % Grafico della funzione g(x)=log_3(x+1)
  \draw[domain=-0.9:10, smooth, variable=\x, green, very thick] plot ({\x}, {ln(\x+1)/ln(3)});
  % Linea orizzontale y = 2
  \draw[dashed, red, very thick] (0,2) -- (10,2);

  % Punto di intersezione per x=8 (calcolato: log_3(9)=2)
  \filldraw[red] (8,2) circle (2pt);

\end{tikzpicture}
\end{center}
\end{esempio}

Questi esempi illustrano come, applicando le proprietà di monotonia delle funzioni esponenziali e logaritmiche e utilizzando le trasformazioni logaritmiche, sia possibile ridurre la risoluzione di disequazioni complesse a semplici confronti algebrici, facilitando l'individuazione dell'intervallo soluzione.


\subsec{Sistemi di Equazioni di Primo e Secondo Grado [2, 3]}
Un modo per comprendere (e talvolta risolvere) i sistemi di equazioni consiste nel \textit{rappresentarne i grafici} in un piano (se il numero di variabili è 2) o nello spazio (se il numero di variabili è 3). In particolare:

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
\subsec{Sistemi a più Incognite [2]}
\subsubsection*{Polinomi in Più Variabili e Varietà Algebrica in Spazi Superiori}
Un polinomio in più variabili è un’espressione algebrica in cui compaiono due o più incognite, ad esempio \(x\), \(y\) e \(z\). La \emph{varietà algebrica} associata a un tale polinomio è l'insieme delle soluzioni dell'equazione ottenuta ponendo il polinomio uguale a zero, e vive in uno spazio di dimensione pari al numero delle variabili. Per esempio, il polinomio 
\[
f(x,y,z)=x^2+y^2+z^2-1
\]
definisce l'insieme
\[
\mathcal{V}(f)=\{(x,y,z)\in \mathbb{R}^3 \mid x^2+y^2+z^2=1\},
\]
che rappresenta la sfera unitaria nello spazio tridimensionale. In questo caso ogni punto della varietà corrisponde a una tripla \((x,y,z)\) e la rappresentazione grafica (in una proiezione) evidenzia la forma sferica.

\medskip

\tdplotsetmaincoords{70}{110}
\begin{center}
\begin{tikzpicture}[tdplot_main_coords, scale=1.2]
  % Disegno degli assi cartesiani 3D
  \draw[->, thick] (0,0,0) -- (3,0,0) node[anchor=north east] {\(x\)};
  \draw[->, thick] (0,0,0) -- (0,3,0) node[anchor=north west] {\(y\)};
  \draw[->, thick] (0,0,0) -- (0,0,3) node[anchor=south] {\(z\)};
  
  % Disegno della sfera unitaria (con raggio 2)
  \shade[ball color=blue!20, opacity=0.4] (0,0,0) circle (2cm);
  
  % Disegno di una curva (circonferenza inclinata) sulla sfera
  % Parametrizzazione: 
  %    x = 2*cos(t)
  %    y = 2*sin(t)*cos(30°)
  %    z = 2*sin(t)*sin(30°)
  \draw[red, very thick, domain=0:360, samples=100] 
    plot ({2*cos(\x)}, {2*sin(\x)*cos(30)}, {2*sin(\x)*sin(30)});
\end{tikzpicture}
\end{center}

\bigskip

Nei sistemi di equazioni in due variabili, come nel caso dei sistemi lineari, il luogo delle soluzioni è rappresentato da rette nel piano. Tali rette possono essere incidenti, parallele o coincidenti. Tuttavia, passando allo spazio tridimensionale, le equazioni di primo grado in tre variabili rappresentano dei piani. L'intersezione di due piani può essere una retta, ma a differenza del piano, in \(\mathbb{R}^3\) due rette non devono necessariamente essere o incidenti o parallele: esse possono essere \emph{sghembe}, ovvero non intersecarsi e non essere parallele. Questo fenomeno evidenzia la maggiore complessità geometrica quando si aumenta il numero di dimensioni.

\medskip

Ad esempio, nel piano le rette \(L_1\) e \(L_2\) devono necessariamente intersecare se non sono parallele, mentre in \(\mathbb{R}^3\) due rette possono essere disposte in modo tale da non avere alcun punto in comune (sono sghembe). Tale possibilità rende lo studio dei sistemi di equazioni in spazi superiori particolarmente interessante dal punto di vista geometrico.

\bigskip

\subsubsection*{Metodi Risolutivi per Sistemi a Più Variabili}
I metodi di risoluzione dei sistemi (come sostituzione, riduzione, eliminazione, e l'uso di matrici) si estendono anche a sistemi con più incognite. Di seguito presentiamo due esempi: uno in tre variabili e uno in quattro variabili.

\begin{esempio}
Consideriamo il sistema in tre variabili
\[
\begin{cases}
x + y + z = 3,\\[1mm]
x - y + z = 2,\\[1mm]
x + 2y - z = 1.
\end{cases}
\]
Per risolvere il sistema, possiamo esprimere \(z\) dalla prima equazione:
\[
z = 3 - x - y,
\]
e sostituirlo nelle altre due:
\[
x - y + (3 - x - y)= 2 \quad \Longrightarrow \quad 3 - 2y = 2 \quad \Longrightarrow \quad y=\frac{1}{2},
\]
\[
x + 2y - (3 - x - y) = 1 \quad \Longrightarrow \quad x + 2y -3 + x + y = 1 \quad \Longrightarrow \quad 2x+3y = 4.
\]
Sostituendo \(y=\frac{1}{2}\):
\[
2x + \frac{3}{2} = 4 \quad \Longrightarrow \quad 2x = \frac{5}{2} \quad \Longrightarrow \quad x = \frac{5}{4}.
\]
Infine, \(z=3-\frac{5}{4}-\frac{1}{2}=\frac{12}{4}-\frac{5}{4}-\frac{2}{4}=\frac{5}{4}\).

La soluzione del sistema è dunque
\[
\left(\frac{5}{4},\,\frac{1}{2},\,\frac{5}{4}\right).
\]

\tdplotsetmaincoords{70}{110}
\begin{center}
\begin{tikzpicture}[tdplot_main_coords, scale=1.2]
  % Assi cartesiani 3D
  \draw[->, thick] (-1,0,0) -- (4,0,0) node[anchor=north east] {\(x\)};
  \draw[->, thick] (0,-1,0) -- (0,4,0) node[anchor=north west] {\(y\)};
  \draw[->, thick] (0,0,-1) -- (0,0,4) node[anchor=south] {\(z\)};
  
  % Piano 1: x+y+z = 3, rappresentato in blu
  \filldraw[blue, opacity=0.15] 
    (3,0,0) --
    (0,3,0) --
    (0,0,3) --
    cycle;
    
  % Piano 2: x - y + z = 2, rappresentato in verde
  % Punti scelti: (0,0,2), (2,0,0) e (0,2,4)
  \filldraw[green, opacity=0.3] 
    (0,0,2) --
    (2,0,0) --
    (0,2,4) --
    cycle;
    
 % Piano 3: x + 2y - z = 1, rappresentato in rosso
% Punti scelti: (0,0,-1), (2,0,1) e (0,2,3)
\filldraw[red, opacity=0.2] 
  (0,0,-1) --
  (2,0,1) --
  (0,2,3) --
  cycle;
    
  % Punto di intersezione dei tre piani: (5/4, 1/2, 5/4)
  \filldraw[black] (1.25,0.5,1.25) circle (2pt);
  \node[above right] at (1.25,0.5,1.25) {\(\left(\frac{5}{4},\,\frac{1}{2},\,\frac{5}{4}\right)\)};
\end{tikzpicture}
\end{center}
\end{esempio}

\begin{esempio}
Consideriamo il sistema in quattro variabili
\[
\begin{cases}
x + y + z + w = 10,\\[1mm]
x - y + z - w = 2,\\[1mm]
2x + y - z + 3w = 14,\\[1mm]
x + 2y + 3z + w = 12.
\end{cases}
\]

Utilizzando il \textbf{metodo di riduzione} in pochi passaggi, procediamo come segue:

\medskip

1. Sommiamo e sottraiamo le prime due equazioni per eliminare alcune variabili. In particolare, dalla somma e differenza di
\[
E_1: \; x+y+z+w=10 \quad \text{e} \quad E_2: \; x-y+z-w=2,
\]
otteniamo:
\[
E_1+E_2:\quad 2x+2z=12 \quad \Longrightarrow \quad x+z=6,
\]
\[
E_1-E_2:\quad 2y+2w=8 \quad \Longrightarrow \quad y+w=4.
\]
Questo permette di esprimere:
\[
z=6-x \quad \text{e} \quad w=4-y.
\]

\medskip

2. Sostituendo \(z=6-x\) e \(w=4-y\) nelle equazioni \(E_3\) ed \(E_4\) si riduce il sistema a due equazioni in \(x\) e \(y\). Ad esempio, si ottengono equazioni del tipo:
\[
3x-2y=8 \quad \text{e} \quad 2x-y=10.
\]

\medskip

3. Dal sistema ridotto, risolvendo la seconda equazione, troviamo facilmente \(x\) (ad esempio, isolando \(y=2x-10\) e sostituendo nell'altra equazione). Una volta determinato \(x\), si procede in modo analogo per trovare \(y\) e successivamente si calcolano \(z\) e \(w\) dalle relazioni \(z=6-x\) e \(w=4-y\).

\medskip

Questa procedura dimostra come il metodo di riduzione consenta di "abbassare" il numero di incognite, partendo dal sistema a quattro variabili e arrivando a un sistema in due variabili. Una volta risolta quest'ultima parte, il procedimento si applica analogamente per determinare gli altri valori.       
\end{esempio}


\subsec{Sistemi di Disequazioni [3]}


I sistemi di disequazioni presentano analogie sostanziali con i sistemi di equazioni, poiché in entrambi i casi si cerca di individuare l'insieme dei valori che soddisfano simultaneamente più condizioni. Tuttavia, mentre i sistemi di equazioni conducono tipicamente a soluzioni isolate (punti), i sistemi di disequazioni determinano delle aree (o regioni) nel piano o nello spazio. Questa differenza nasce dal fatto che le disequazioni, introducendo relazioni di ordine (come \(<\), \(\leq\), \(>\) o \(\geq\)), definiscono dei confini che, una volta tracciati, suddividono il dominio in intervalli o regioni in cui le condizioni sono verificate.

Per risolvere un sistema di disequazioni, il procedimento è analogo a quello adottato per i sistemi di equazioni: si determina innanzitutto la curva o la retta di confine (cioè l'insieme delle soluzioni dell'equazione associata), si individuano i punti critici e si effettua un'analisi del segno nelle varie regioni del dominio. Quest'analisi permette di stabilire in quali di queste regioni la disequazione (o il sistema di disequazioni) è soddisfatta. Pur essendo i metodi di risoluzione simili – ad esempio, attraverso il confronto, l'intersezione delle regioni di soluzione e la verifica dei segni – la natura delle soluzioni (regioni anziché punti) rende l'interpretazione e la rappresentazione grafica di tali sistemi leggermente più complesse.

Inoltre, inizialmente esaminiamo i sistemi di disequazioni in due variabili, partendo da quelli lineari (di grado uno) e successivamente passando a sistemi di grado maggiore; in seguito, estendiamo l'analisi anche a sistemi che coinvolgono più variabili.
\subsubsection*{Sistemi di Disequazioni in Due Variabili  di Primo Grado}

Consideriamo il seguente sistema lineare di disequazioni:
\[
\begin{cases}
x+y \le 4,\\[1mm]
x-y \ge 1.
\end{cases}
\]
La soluzione del sistema è data dall'intersezione dei due semipiani definiti dalle rispettive disequazioni. In particolare, la prima disequazione \(x+y\le4\) rappresenta il semipiano al di sotto (o sulla) retta \(x+y=4\), mentre la seconda \(x-y\ge1\) rappresenta il semipiano al di sopra (o sulla) retta \(x-y=1\).

\medskip

\begin{center}
\begin{tikzpicture}[scale=0.8]
  % Axes
  \draw[->] (-1,0) -- (6,0) node[right] {\(x\)};
  \draw[->] (0,-1) -- (0,6) node[above] {\(y\)};

  % Blue line: x+y=4 extended into the negative region and its fill (region: x+y ≤ 4)
  \draw[blue, thick] (-1,5) -- (5,-1);
  \fill[blue, opacity=0.2] (0,0) -- (0, 4) -- (4,0) -- cycle;

  % Red line: x-y=1 extended into the negative region and its fill (region: x-y ≥ 1)
  \draw[red, thick] (-1,-2) -- (6,5);
  \fill[red, opacity=0.2] (0,-1) -- (6,5) -- (6,6) -- (0,6) -- cycle;

  % Green intersection of the blue and red regions
  \begin{scope}
    \clip (-1,-1) rectangle (6,6);
    \clip (-1,-1) -- (-1,5) -- (5,-1) -- cycle;
    \clip (0,-1) -- (6,5) -- (6,6) -- (0,6) -- cycle;
    \fill[green, opacity=0.4] (-1,-1) rectangle (6,6);
  \end{scope}
\end{tikzpicture}
\end{center}

La zona verde rappresenta l'insieme delle soluzioni del sistema. Nel disengo, per semplicità segnamo solo i valori con $x \ge 0$, ovviamente però l'area verde si estende anche per $x < 0$.

\bigskip

\subsubsection*{Sistemi di Disequazioni in Due Variabili (Grado Maggiore)}

Consideriamo ora un sistema di disequazioni non lineari:
\[
\begin{cases}
y \ge x^2,\\[1mm]
y \le 2-x^2.
\end{cases}
\]
La prima disequazione \(y\ge x^2\) rappresenta il semipiano sopra (o sulla) la parabola \(y=x^2\), mentre la seconda \(y\le2-x^2\) rappresenta il semipiano sotto (o sulla) la parabola ribaltata \(y=2-x^2\). La soluzione del sistema è l'intersezione delle due regioni, ovvero l'insieme dei punti compresi tra le due parabole.

\medskip

\textbf{Grafico:}
\begin{center}
\begin{tikzpicture}[scale=1.3]
  % Assi cartesiani
  \draw[->] (-2,0) -- (2,0) node[right] {\(x\)};
  \draw[->] (0,-1) -- (0,3) node[above] {\(y\)};
  
  % Disegno della parabola y = x^2 (in blu)
  \draw[blue, thick, domain=-1.4:1.4, smooth, variable=\x] plot ({\x}, {\x*\x});
  
  % Disegno della parabola y = 2 - x^2 (in rosso)
  \draw[red, thick, domain=-1.4:1.4, smooth, variable=\x] plot ({\x}, {2-\x*\x});
  
  % Riempimento dell'intersezione (area verde) tra le due parabole per x in [-1,1]
  \fill[green, opacity=0.4] 
    plot[domain=-1:1, smooth, variable=\x] ({\x}, {2-\x*\x}) --
    plot[domain=1:-1, smooth, variable=\x] ({\x}, {\x*\x}) -- cycle;
\end{tikzpicture}
\end{center}

L'area verde rappresenta l'insieme delle soluzioni, ovvero i punti che soddisfano entrambe le disequazioni.

\bigskip

\subsubsection*{Sistemi di Disequazioni in Più Variabili}

Consideriamo un sistema in tre variabili:
\[
\begin{cases}
x+y+z \le 3,\\[1mm]
x\ge0,\\[1mm] y\ge0,\\[1mm] z\ge0.
\end{cases}
\]
Questo sistema definisce la regione dello spazio in cui la somma delle coordinate è al massimo 3, e tutte le coordinate sono non negative. Geometricamente, la soluzione è un tetraedro (o piramide) nel primo ottante.

\medskip

\begin{center}
\begin{tikzpicture}[tdplot_main_coords, scale=1]
  % Assi 3D
  \draw[->, thick] (0,0,0) -- (4,0,0) node[anchor=north east] {\(x\)};
  \draw[->, thick] (0,0,0) -- (0,4,0) node[anchor=north west] {\(y\)};
  \draw[->, thick] (0,0,0) -- (0,0,4) node[anchor=south] {\(z\)};
  
  % Vertici del tetraedro
  \coordinate (A) at (0,0,0);
  \coordinate (B) at (3,0,0);
  \coordinate (C) at (0,3,0);
  \coordinate (D) at (0,0,3);
  
  % Disegno degli spigoli del tetraedro
  \draw[blue, very thick] (A) -- (B) -- (C) -- cycle;
  \draw[blue, very thick] (A) -- (D);
  \draw[blue, very thick] (B) -- (D);
  \draw[blue, very thick] (C) -- (D);
  
  % Riempimento del tetraedro con opacità
  \fill[green, opacity=0.3] (A) -- (B) -- (D) -- cycle;
  \fill[green, opacity=0.3] (A) -- (C) -- (D) -- cycle;
  \fill[green, opacity=0.3] (A) -- (B) -- (C) -- cycle;
  
  % Etichettatura dei vertici
  \node[below right] at (B) {\( (3,0,0) \)};
  \node[above right] at (C) {\( (0,3,0) \)};
  \node[right] at (D) {\( (0,0,3) \)};
\end{tikzpicture}
\end{center}

La regione evidenziata (di colore verde) rappresenta l'insieme dei punti \((x,y,z)\) che soddisfano il sistema.

\bigskip

I metodi risolutivi algebrici (sostituzione, eliminazione, metodo di Gauss) si estendono naturalmente anche a sistemi di disequazioni in più variabili. La rappresentazione grafica in spazi di dimensione superiore (come \(\mathbb{R}^3\)) offre un'importante intuizione geometrica, evidenziando le regioni di soluzione come l'intersezione di ipersuperfici (piani, paraboloidi, ecc.) e mostrando come le relazioni tra le variabili possano dare origine a regioni complesse e articolate.

Vediamo ora quindi un approcccio più algebraico a questo materiale con un esempio.

\subsubsection*{Esempio di Risoluzione Algebraica}

Consideriamo la sfera
\[
S:\quad x^2+y^2+z^2\leq4,
\]
che rappresenta una disequazione in tre variabili (la condizione per rimanere all'interno di una sfera di raggio 2), e la retta
\[
L:\quad 
\begin{cases}
x=1+t,\\[1mm]
y=t,\\[1mm]
z=t,
\end{cases}\quad t\in\mathbb{R},
\]
data in forma parametrica (ossia, un'equazione che esprime le coordinate in funzione di un parametro \(t\)). Il sistema formato da \(S\) e \(L\) è un sistema unico, e la sua soluzione determina il segmento della retta \(L\) che giace all'interno della sfera.

Sostituendo le coordinate parametriche della retta nell'espressione della sfera otteniamo:
\[
(1+t)^2+t^2+t^2\leq4.
\]
Espandendo e semplificando:
\[
1+2t+t^2+2t^2\leq4\quad\Longrightarrow\quad 3t^2+2t+1\leq4,
\]
\[
3t^2+2t-3\leq0.
\]
Per determinare l'intervallo di \(t\) in cui la disequazione è verificata, risolviamo l'equazione associata:
\[
3t^2+2t-3=0.
\]
Calcoliamo il discriminante:
\[
\Delta=2^2-4\cdot3\cdot(-3)=4+36=40.
\]
Le soluzioni sono dunque:
\[
t=\frac{-2\pm\sqrt{40}}{6}=\frac{-2\pm2\sqrt{10}}{6}=\frac{-1\pm\sqrt{10}}{3}.
\]
Pertanto, il segmento di \(L\) contenuto in \(S\) corrisponde all'intervallo
\[
t\in\left[\frac{-1-\sqrt{10}}{3},\,\frac{-1+\sqrt{10}}{3}\right].
\]

\medskip

\textbf{Rappresentazione grafica:}  
Nel disegno seguente rappresentiamo, in proiezione, la sfera come un cerchio (con centro \((0,0)\) e raggio \(2\)) e la retta in forma proiettata. Il segmento evidenziato in verde corrisponde all'intersezione, cioè ai punti della retta per cui il parametro \(t\) appartiene all'intervallo sopra determinato.

\begin{center}
\begin{tikzpicture}[scale=1.0]
  % Disegno del piano cartesiano
  \draw[->] (-4,0) -- (4,0) node[right] {\(x\)};
  \draw[->] (0,-5) -- (0,3) node[above] {\(y\)};
  
  % Cerchio che rappresenta la sfera (proiezione in 2D)
  \draw[thick] (0,0) circle (2);
  
  % Disegno della retta proiettata (equazione: y = x - 1)
  \draw[red, thick] (-3,-4) -- (3,2);
  
  % Calcolo delle intersezioni della retta y = x - 1 con il cerchio x^2+y^2 = 4
  \coordinate (A) at ({(1 - sqrt(7))/2}, {(1 - sqrt(7))/2 - 1});
  \coordinate (B) at ({(1 + sqrt(7))/2}, {(1 + sqrt(7))/2 - 1});
  
  % Evidenziamo il segmento interno (in verde)
  \draw[green, very thick] (A) -- (B);
\end{tikzpicture}
\end{center}
```
### Geometry
```LaTeX
\section{Geometria}
\subsectionstar{Cordinate Cartesiane [1, 2, 3, 4]}
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
Un singolo punto \((x, y)\) è soltanto l’inizio: allo stesso modo, possiamo \textit{marcare interi insiemi di punti} su un piano cartesiano, e descriverli tramite \textit{equazioni}. Ogni equazione in due variabili \(x\) e \(y\) individua, infatti, un insieme di coppie \((x, y)\) che ne soddisfano la relazione, e la loro rappresentazione grafica è una \textit{figura geometrica} (una retta, una curva, o una regione del piano). Questo modo di collegare \textit{algebra} e \textit{geometria} lo abbiamo approfondito nella parte di \textbf{geometria analitica} (ultima sezione di Algebra), dove abbiamo visto come studiare in dettaglio le forme, le posizioni e le proprietà di tali insiemi di punti. 


\subsec{Distanza [1, 2, 3, 4]}
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

\subsubsection*{Esempio: Distanza tra Punto e Retta}
% Esempio: Distanza da un punto a una retta e calcolo del segmento perpendicolare

Consideriamo la retta 
\[
r:\quad y=2x+1,
\]
La distanza \(d\) da un punto \(P(x_0,y_0)\) alla retta \(Ax+By+C=0\) è data da
\[
d=\frac{|Ax_0+By_0+C|}{\sqrt{A^2+B^2}}.
\]
Prendiamo, ad esempio, il punto 
\[
P(3,0).
\]
Con \(A=2\), \(B=-1\) e \(C=1\) otteniamo:
\[
d=\frac{|2\cdot3+(-1)\cdot0+1|}{\sqrt{2^2+(-1)^2}}=\frac{|6+1|}{\sqrt{4+1}}=\frac{7}{\sqrt{5}}.
\]

Un passaggio ulteriore sarebbe calcolare il segmento perpendicolare alla retta, il che è dato dal vettore normale
\[
\mathbf{n}=(2,-1),
\]
la cui versione unitaria è
\[
\mathbf{\hat{n}}=\frac{(2,-1)}{\sqrt{5}}.
\]
Il piede della perpendicolare, \(Q\), si ottiene sottraendo a \(P\) il vettore \(d\,\mathbf{\hat{n}}\):
\[
Q=P-d\,\mathbf{\hat{n}}=\Bigl(3,0\Bigr)-\frac{7}{\sqrt{5}}\cdot\frac{(2,-1)}{\sqrt{5}}=\Bigl(3,0\Bigr)-\frac{7}{5}(2,-1).
\]
Calcolando le coordinate:
\[
Q=\Bigl(3-\frac{14}{5},\,0+\frac{7}{5}\Bigr)=\Bigl(\frac{1}{5},\,\frac{7}{5}\Bigr).
\]
Verifichiamo che \(Q\) appartenga a \(r\): sostituendo \(x=\frac{1}{5}\) in \(y=2x+1\) si ha
\[
y=2\cdot\frac{1}{5}+1=\frac{2}{5}+1=\frac{7}{5}.
\]

\vspace{1em}
\[
\begin{tikzpicture}[scale=1.0]
  % Disegno del piano cartesiano
  \draw[->] (-1,0) -- (5,0) node[right] {\(x\)};
  \draw[->] (0,-1) -- (0,4) node[above] {\(y\)};
  
  % Disegno della retta r: y = 2x+1
  \draw[blue, thick, domain=-1:2, smooth, variable=\x] 
       plot ({\x}, {2*\x+1}) node[right, pos=0.95] {};
  
  % Punto P(3,0)
  \coordinate (P) at (3,0);
  \filldraw[red] (P) circle (2pt) node[below right] {\(P(3,0)\)};
  
  % Punto Q, calcolato come Q=(1/5, 7/5)
  \coordinate (Q) at ({1/5},{7/5});
  \filldraw[black] (Q) circle (2pt) node[above left] {\(Q\)};
  
  % Disegno del segmento perpendicolare da P a Q (tratteggiato)
  \draw[dashed, thick] (P) -- (Q);
  
  % Etichetta per la distanza
  \node[below, blue] at ($(P)!0.5!(Q)$) {};
  
  % Vettore normale (opzionale)
  \draw[->, gray, thick] (Q) -- ++({2/sqrt(5)},{-1/sqrt(5)}) 
      node[right, black] {\(\mathbf{n}\)};
\end{tikzpicture}
\]

\subsubsection*{Esempio in un Triangolo}

Per vedere l'esempio, partiamo prima dalla definizione di triangolo che usa la scorsa definizione di mediana. Vogliamo calcolare infatti la distanza tra un punto interno al triangolo, il baricentro, ed il triangolo stesso. Per misurarla dovremo misurare la distanza tra il baricentro e ciascuno dei suoi lati e selezionare la distanza minima tra queste.

\begin{definition}[Baricentro]
  Il \emph{baricentro} di un triangolo è il punto di intersezione delle mediane ed è dato dalla media aritmetica delle coordinate dei vertici:
  \[
  G=\left(\frac{x_A+x_B+x_C}{3},\,\frac{y_A+y_B+y_C}{3}\right).
  \]
\end{definition}

Consideriamo il triangolo \(ABC\) con vertici
\[
A(0,0),\quad B(6,2),\quad C(3,7).
\]
I punti medi dei lati sono:
\[
M_A=\text{midpoint of } BC=\left(\frac{6+3}{2},\,\frac{2+7}{2}\right)=(4.5,4.5),
\]
\[
M_B=\text{midpoint of } AC=\left(\frac{0+3}{2},\,\frac{0+7}{2}\right)=(1.5,3.5),
\]
\[
M_C=\text{midpoint of } AB=\left(\frac{0+6}{2},\,\frac{0+2}{2}\right)=(3,1).
\]
Il baricentro \(G\) risulta quindi:
\[
G=\left(\frac{0+6+3}{3},\,\frac{0+2+7}{3}\right)=(3,3).
\]

Le mediane sono i segmenti \(AM_A\), \(BM_B\) e \(CM_C\).  
La distanza del baricentro dal triangolo viene definita come il minimo tra le distanze di \(G\) dai tre lati.  
Calcoliamo tali distanze utilizzando la formula della distanza di un punto da una retta.

\begin{itemize}
  \item \textbf{Lato \(AB\):}  
  I punti \(A(0,0)\) e \(B(6,2)\) definiscono la retta con pendenza \(m=\frac{2-0}{6-0}=\frac{1}{3}\).  
  La sua equazione in forma implicita è
  \[
  x-3y=0.
  \]
  La distanza da \(G(3,3)\) è:
  \[
  d_{AB}=\frac{|3-3\cdot3|}{\sqrt{1^2+(-3)^2}}=\frac{|3-9|}{\sqrt{10}}=\frac{6}{\sqrt{10}}.
  \]

  \item \textbf{Lato \(BC\):}  
  I punti \(B(6,2)\) e \(C(3,7)\) definiscono la retta. Utilizzando il punto \(B\) e la pendenza
  \[
  m=\frac{7-2}{3-6}=-\frac{5}{3},
  \]
  la forma punto-pendenza è \(y-2=-\frac{5}{3}(x-6)\), che, in forma implicita, diventa:
  \[
  5x+3y-36=0.
  \]
  La distanza da \(G(3,3)\) è:
  \[
  d_{BC}=\frac{|5\cdot3+3\cdot3-36|}{\sqrt{5^2+3^2}}=\frac{|15+9-36|}{\sqrt{34}}=\frac{12}{\sqrt{34}}.
  \]

  \item \textbf{Lato \(CA\):}  
  I punti \(C(3,7)\) e \(A(0,0)\) definiscono la retta con pendenza \(m=\frac{7}{3}\), ovvero
  \[
  y=\frac{7}{3}x,
  \]
  o, in forma implicita,
  \[
  7x-3y=0.
  \]
  La distanza da \(G(3,3)\) è:
  \[
  d_{CA}=\frac{|7\cdot3-3\cdot3|}{\sqrt{7^2+(-3)^2}}=\frac{|21-9|}{\sqrt{58}}=\frac{12}{\sqrt{58}}.
  \]
\end{itemize}

Confrontando i valori (approssimativamente, \(\frac{6}{\sqrt{10}}\approx1.90\), \(\frac{12}{\sqrt{34}}\approx2.06\) e \(\frac{12}{\sqrt{58}}\approx1.57\)), la distanza minima è
\[
d_{\min}=\frac{12}{\sqrt{58}},
\]
che corrisponde alla distanza dal lato \(CA\).


\begin{center}
\begin{tikzpicture}[scale=0.8]
  % Disegno degli assi cartesiani
  \draw[->] (-1,0) -- (8,0) node[right] {\(x\)};
  \draw[->] (0,-1) -- (0,8) node[above] {\(y\)};
  
  % Definizione dei vertici del triangolo
  \coordinate (A) at (0,0);
  \coordinate (B) at (6,2);
  \coordinate (C) at (3,7);
  
  % Disegno del triangolo ABC
  \draw[thick] (A) -- (B) -- (C) -- cycle;
  
  % Punti medi
  \coordinate (M_A) at (4.5,4.5); % Midpoint of BC
  \coordinate (M_B) at (1.5,3.5); % Midpoint of AC
  \coordinate (M_C) at (3,1);     % Midpoint of AB
  
  % Disegno delle mediane (tratteggiate)
  \draw[dashed, blue] (A) -- (M_A);
  \draw[dashed, blue] (B) -- (M_B);
  \draw[dashed, blue] (C) -- (M_C);
  
  % Baricentro G (media dei vertici)
  \coordinate (G) at (3,3);
  \filldraw[red] (G) circle (2pt) node[below right] {\(G(3,3)\)};
  
  % Etichette dei vertici
  \filldraw[black] (A) circle (2pt) node[below left] {\(A(0,0)\)};
  \filldraw[black] (B) circle (2pt) node[below right] {\(B(6,2)\)};
  \filldraw[black] (C) circle (2pt) node[above] {\(C(3,7)\)};
  
  % Etichette dei punti medi
  \filldraw[black] (M_A) circle (2pt) node[above right] {\(M_A\)};
  \filldraw[black] (M_B) circle (2pt) node[below left] {\(M_B\)};
  \filldraw[black] (M_C) circle (2pt) node[below] {\(M_C\)};
  
  % Calcolo del piede della perpendicolare dal baricentro al lato CA.
  % Lato CA passa per A(0,0) e C(3,7); la sua equazione è y = (7/3)x.
  % Il piede della perpendicolare da G(3,3) si calcola come:
  % Q = \Bigl(\frac{x_G+m y_G}{1+m^2}, \frac{m(x_G+m y_G)}{1+m^2}\Bigr), con m=7/3.
  % Calcoliamo: x_G+m y_G = 3 + (7/3)*3 = 3+7 = 10, e 1+m^2 = 1+49/9 = 58/9.
  % Quindi, Q = \Bigl(10/(58/9), (7/3*10)/(58/9)\Bigr) = (90/58,70/58) = (45/29,35/29).
  \coordinate (Q) at ({45/29},{35/29});
  
  % Disegno della perpendicolare (in violetto) dal baricentro a CA
  \draw[dotted, very thick, violet] (G) -- (M_B) node[midway, above] {\(\frac{12}{\sqrt{58}}\)};
  
  % Disegno del lato CA (in grigio, per evidenziare la base della perpendicolare)
  \draw[gray, thin, dashed] (A) -- (C);
\end{tikzpicture}
\end{center}

\noindent
In questo esempio abbiamo tracciato tutte le mediane del triangolo scaleno \(ABC\), definito il baricentro \(G\) come intersezione delle mediane, e calcolato la distanza minima dal baricentro a uno dei lati del triangolo (in questo caso il lato \(CA\)), che risulta essere
\[
d_{\min}=\frac{12}{\sqrt{58}}.
\]



\subsec{Punto Medio di un Segmento [1, 2, 3, 4]}
Il \emph{punto medio} di un segmento è il punto che divide il segmento in due parti congruenti, ossia, è equidistante dai due estremi. In altre parole, dato un segmento \( \overline{AB} \) con estremi 
\[
A(x_A, y_A) \quad \text{e} \quad B(x_B, y_B),
\]
il punto medio \( M \) si calcola come:
\[
M = \left(\frac{x_A+x_B}{2},\,\frac{y_A+y_B}{2}\right).
\]

\medskip

\textbf{Definizione Algebrica di un Segmento:}

Un segmento può essere definito in due modi:
\begin{enumerate}
  \item \textbf{Con due punti:} Si specificano gli estremi \( A(x_A, y_A) \) e \( B(x_B, y_B) \). Il segmento \( \overline{AB} \) è l'insieme dei punti che stanno tra \( A \) e \( B \).
  \item \textbf{In forma parametrica:} Se la retta contenente \( \overline{AB} \) è data dalla parametrizzazione
  \[
  \begin{cases}
  x = x_A + t(x_B-x_A),\\[1mm]
  y = y_A + t(x_B-x_A),
  \end{cases}\quad t\in\mathbb{R},
  \]
  allora il segmento \( \overline{AB} \) corrisponde all'intervallo dei valori di \( t \) compreso tra 0 e 1, cioè \( t\in[0,1] \).
\end{enumerate}

\medskip

\textbf{Disegno sul Piano Cartesiano:}

\begin{center}
\begin{tikzpicture}[scale=1.0]
  % Disegno degli assi cartesiani
  \draw[->] (-1,0) -- (6,0) node[right] {\(x\)};
  \draw[->] (0,-1) -- (0,6) node[above] {\(y\)};
  
  % Definizione dei punti estremi A e B
  \coordinate (A) at (1,2);
  \coordinate (B) at (5,4);
  
  % Disegno del segmento AB
  \draw[thick, blue] (A) -- (B);
  
  % Marcatura degli estremi
  \filldraw[black] (A) circle (2pt) node[below right] {\(A(1,2)\)};
  \filldraw[black] (B) circle (2pt) node[above right] {\(B(5,4)\)};
  
  % Calcolo e marcatura del punto medio M
  \coordinate (M) at ($(A)!0.5!(B)$);
  \filldraw[red] (M) circle (2pt) node[below right] {\(M\)};
\end{tikzpicture}
\end{center}

\medskip

\textbf{Formula per il Punto Medio:}

Data una coppia di punti \( A(x_A, y_A) \) e \( B(x_B, y_B) \), il punto medio \( M \) si calcola con la formula:
\[
M = \left(\frac{x_A+x_B}{2},\,\frac{y_A+y_B}{2}\right).
\]

Questa formula si ottiene semplicemente calcolando la media aritmetica delle coordinate corrispondenti degli estremi, garantendo così che \( M \) sia equidistante da \( A \) e \( B \).

\medskip

In sintesi, il punto medio rappresenta il "centro" del segmento ed è definito sia geometricamente che algebricamente, utilizzando la media delle coordinate degli estremi o la parametrizzazione della retta contenente il segmento.

\subsubsection*{Esempi Comuni sui Triangoli}

\begin{definition}[Mediana]
  In un triangolo, la \emph{mediana} relativa a un vertice è il segmento che congiunge quel vertice con il punto medio del lato opposto.
\end{definition}

Consideriamo un triangolo \(ABC\) con vertici
\[
A(x_A, y_A),\quad B(x_B, y_B),\quad C(x_C, y_C).
\]
Per determinare la mediana che parte dal vertice \(A\), calcoliamo innanzitutto il punto medio \(M\) del lato \(BC\) utilizzando la formula:
\[
M = \left(\frac{x_B+x_C}{2},\, \frac{y_B+y_C}{2}\right).
\]
Il segmento della mediana è quindi il tratto \(\overline{AM}\), che rappresenta la parte della retta (definita in forma parametrica o tramite gli estremi) compresa tra \(A\) e \(M\).

\medskip

Supponiamo di avere il triangolo con vertici
\[
A(1,2),\quad B(4,6),\quad C(8,2).
\]
Calcoliamo il punto medio del lato \(BC\):
\[
M = \left(\frac{4+8}{2},\, \frac{6+2}{2}\right) = \left(6,\, 4\right).
\]
Pertanto, la mediana che parte da \(A\) è il segmento \(\overline{AM}\) che unisce \(A(1,2)\) a \(M(6,4)\).

La lunghezza del segmento della mediana può essere determinata mediante la formula della distanza tra due punti:
\[
|\overline{AM}| = \sqrt{(6-1)^2 + (4-2)^2} = \sqrt{5^2 + 2^2} = \sqrt{25+4} = \sqrt{29}.
\]

\begin{center}
\begin{tikzpicture}[scale=1.0]
  % Definizione dei vertici del triangolo
  \coordinate (A) at (1,2);
  \coordinate (B) at (4,6);
  \coordinate (C) at (8,2);
  
  % Disegno del triangolo ABC
  \draw[thick] (A) -- (B) -- (C) -- cycle;
  
  % Marcatura dei vertici
  \filldraw[black] (A) circle (2pt) node[below left] {\(A(1,2)\)};
  \filldraw[black] (B) circle (2pt) node[above] {\(B(4,6)\)};
  \filldraw[black] (C) circle (2pt) node[below right] {\(C(8,2)\)};
  
  % Calcolo e marcatura del punto medio M del lato BC
  \coordinate (M) at (6,4);
  \filldraw[red] (M) circle (2pt) node[above right] {\(M(6,4)\)};
  
  % Disegno della mediana che parte da A e arriva a M
  \draw[green, very thick, dashed] (A) -- (M);
  
  % Etichetta per la mediana
  \node[green!70!black, right] at ($(A)!0.5!(M)$) {};
\end{tikzpicture}
\end{center}

In questo esempio abbiamo definito la mediana di un triangolo sia geometricamente (come il segmento che unisce un vertice al punto medio del lato opposto) sia algebricamente, calcolando il punto medio tramite la media aritmetica delle coordinate degli estremi.

\subsec{Le Relazioni [1]}
\subsection*{Introduzione alle Relazioni e alle Funzioni}

Per introdurre in modo formale il concetto di relazione all'interno della teoria degli insiemi, è opportuno partire dall'analisi delle \emph{proprietà} che gli elementi possono possedere. Le proprietà rappresentano predicati o condizioni che determinano se un elemento soddisfa una determinata caratteristica; ad esempio, dire che un numero è pari o primo esprime una sua proprietà intrinseca.

Una volta comprese le proprietà, possiamo definire le \emph{funzioni} come relazioni particolari che rispettano regole specifiche. In effetti, una funzione è una relazione che associa ad ogni elemento del dominio un unico elemento del codominio.

Questo approccio ci consente di studiare le relazioni in modo strutturato, analizzando prima le proprietà che caratterizzano gli elementi e poi osservando come queste proprietà si combinano attraverso relazioni più complesse, come le funzioni.
\subsubsection*{Le Proprietà e gli Insiemi}
Una \emph{proprietà} è una caratteristica che un elemento di un insieme può possedere. Per esempio, consideriamo l'insieme dei numeri naturali \(\mathbb{N}\). Dire che un numero \(n\in\mathbb{N}\) è \emph{pari} significa che esiste un intero \(k\) tale che
\[
n=2k.
\]
Analogamente, dire che un numero \(p\in\mathbb{N}\) (con \(p\ge2\)) è \emph{primo} significa che \(p\) ha esattamente due divisori distinti, \(1\) e \(p\).

Definiamo formalmente l'insieme dei numeri primi, denotato con \(\mathbb{P}\), come:
\[
\mathbb{P} = \{p\in \mathbb{N} \mid p\ge 2 \text{ e } \forall d\in\mathbb{N},\ (d\mid p \implies (d=1 \text{ o } d=p))\}.
\]
Dove $d \mid p$ significa che $d$ è un divisore di $p$. In parole quindi tutti gli elementi dell'insieme $\mathbb{P}$ sono quelli che soddisfano questa proprietà, ossia che sono almeno due e che per ogni loro divisore è o uguale ad $1$ o uguale al numero primo stesso. Vediamo che ad esempio questa proprietà è soddisfatta da questi elementi:
\[
\mathbb{P} = \{2,\,3,\,5,\,7,\,11,\,13,\,\dots\}.
\]
Abbiamo a questo modo definito un insieme grazie ad una proprietà. Questo ci servirà per capire a fondo le relazioni, vediamo ora come generalizzare questa nozione grazie al prodotto cartesiano.

\subsubsection*{Prodotto Cartesiano}
Dato un insieme \(A\), il \emph{prodotto cartesiano} \(A\times A\) è definito come l'insieme di tutte le coppie ordinate
\[
A\times A=\{(a,b) \mid a\in A,\; b\in A\}.
\]
Più in generale, per un intero \(n\geq 1\) si definisce il prodotto cartesiano \(A^n\) come l'insieme di tutte le \(n\)-uple ordinate di elementi di \(A\). Una \emph{relazione} di arità \(n\) su \(A\) è un sottoinsieme di \(A^n\); in altre parole, una relazione non si applica solo a un singolo oggetto, ma a più oggetti contemporaneamente. Vediamo ora alcuni esempi di relazioni per chiarire la nozione.

\subsubsection*{Relazioni in Teoria degli Insiemi: Esempi}
Vediamo un paio di esempi semplici con i quali abbiamo gia familiarità"
\begin{itemize}
  \item La relazione d'ordine \(\le\) su \(\mathbb{N}\) è definita come
    \[
    R_{\le} = \{(a,b) \in \mathbb{N} \times \mathbb{N} \mid a \le b\}.
    \]
    Ad esempio, alcuni elementi di \(R_{\le}\) sono: \((0,0),\,(0,1),\,(0,2),\,(1,1),\,(1,2),\,(2,2),\dots\).

  \item La relazione di uguaglianza su un insieme \(A\) è definita come
    \[
    R_{=} = \{(a,a) \mid a \in A\}.
    \]
    Ad esempio, se \(A = \{0,1,2,3,\dots\}\), allora
    \[
    R_{=} = \{(0,0),\,(1,1),\,(2,2),\,(3,3),\dots\}.
    \]
\end{itemize}
Queste relazioni sono formalmente definite come sottoinsiemi di prodotti cartesiani e consentono di esprimere proprietà che riguardano coppie o insiemi di elementi.



\subsec{Gli Insiemi Ordinati e la Linea Numerica [1]}
\subsubsection*{Proprietà delle Relazioni}

Per studiare formalmente come gli elementi di un insieme interagiscano, è utile partire dalla definizione di \emph{proprietà} degli elementi, e successivamente definire le proprietà delle relazioni. 

Questi sono alcuni esempi di proprietà importanti che le relazioni possono avere:
\begin{itemize}
  \item \textbf{Riflessiva:} Una relazione \(R\) su \(A\) è riflessiva se, per ogni \(a\in A\), si ha \(aRa\). Ad esempio, \(R_{=}\) è riflessiva.
  \item \textbf{Simmetrica:} \(R\) è simmetrica se, per ogni \(a,b\in A\), \(aRb\) implica \(bRa\).
  \item \textbf{Transitiva:} \(R\) è transitiva se, per ogni \(a,b,c\in A\), se \(aRb\) e \(bRc\) allora \(aRc\).
  \item \textbf{Antisimmetrica:} \(R\) è antisimmetrica se, per ogni \(a,b\in A\), se \(aRb\) e \(bRa\) allora \(a=b\).
  \item \textbf{Densa:} Una relazione d'ordine \(<\) su un insieme \(A\) è detta densa se, per ogni \(a,b\in A\) tali che \(a<b\), esiste almeno un elemento \(c\in A\) con \(a<c<b\). Ad esempio, la relazione \(<\) sui numeri reali \(\mathbb{R}\) è densa (tra ogni due numeri reali esiste un altro numero reale), mentre su \(\mathbb{N}\) tale proprietà non vale.
\end{itemize}

Queste proprietà non solo descrivono come la relazione agisce sui singoli elementi, ma permettono anche di caratterizzare relazioni più complesse come quelle d'ordine o di inclusione (\(\subseteq\)). Ad esempio, la relazione \(\le\) su \(\mathbb{N}\) è definita come il sottoinsieme di \(\mathbb{N}\times \mathbb{N}\) contenente coppie come \((0,0),\,(0,1),\,(0,2),\,(1,1),\,(1,2),\,(2,2),\dots\), mentre la relazione di uguaglianza è definita dall'insieme \(\{(a,a) \mid a \in A\}\).

\subsubsection*{Ordini: Ordine Parziale, Lineare e Denso}

Un ordine parziale su un insieme \(A\) è una relazione binaria \(\preceq\) che soddisfa le seguenti proprietà:
\begin{itemize}
  \item \textbf{Riflessività:} per ogni \(a\in A\), \(a \preceq a\);
  \item \textbf{Antisimmetria:} per ogni \(a,b\in A\), se \(a\preceq b\) e \(b\preceq a\) allora \(a=b\);
  \item \textbf{Transitività:} per ogni \(a,b,c\in A\), se \(a\preceq b\) e \(b\preceq c\) allora \(a\preceq c\).
\end{itemize}
Un classico esempio di ordine parziale è la relazione di inclusione \(\subseteq\) sull'insieme delle parti di un insieme \(X\). Ad esempio, se poniamo
\[
X = \{a,b\},
\]
allora la potenza di \(X\) è
\[
\mathcal{P}(X)=\{\varnothing,\{a\},\{b\},\{a,b\}\},
\]
e l'ordine definito da \(\subseteq\) è
\[
\{a,b\} \supseteq \{a\},\quad \{a,b\} \supseteq \{b\},\quad \{a\} \supseteq \varnothing,\quad \{b\} \supseteq \varnothing.
\]
Il seguente diagramma (Hasse diagram) mostra graficamente questo ordine:
\begin{center}
\begin{tikzpicture}[node distance=1.5cm, auto]
  \node (top) {\(\{a,b\}\)};
  \node (left) [below left of=top] {\(\{a\}\)};
  \node (right) [below right of=top] {\(\{b\}\)};
  \node (bottom) [below of=left, xshift=0.75cm] {\(\varnothing\)};
  \draw (bottom) -- (left);
  \draw (bottom) -- (right);
  \draw (left) -- (top);
  \draw (right) -- (top);
\end{tikzpicture}
\end{center}

Un \emph{ordine lineare} (o totale) è un ordine parziale in cui ogni coppia di elementi è comparabile: per ogni \(a,b\in A\) vale o \(a\preceq b\) o \(b\preceq a\). Un esempio classico è l'ordine usuale sui numeri naturali:

\begin{center}
\begin{tikzpicture}[scale=1.0]
  \foreach \x in {0,1,2,3,4} {
    \filldraw[black] (\x,0) circle (2pt) node[below] {\(\x\)};
  }
\end{tikzpicture}
\end{center}

In questo caso, ogni coppia di numeri è confrontabile.



Infine, un \emph{ordine denso} è un ordine lineare in cui, per ogni coppia di elementi distinti \(a,b\) con \(a < b\), esiste almeno un elemento \(c\) tale che \(a < c < b\). Un esempio tipico è l'insieme dei numeri razionali (o dei numeri reali) con l'ordine usuale:
\[
\text{Per ogni } a,b\in\mathbb{Q} \text{ (con } a < b\text{), esiste } c\in\mathbb{Q} \text{ tale che } a < c < b.
\]

Vediamo ad esempio la linea dei numeri razionali:

\begin{center}
\begin{tikzpicture}[scale=1.0]
  % Disegno del piano cartesiano
  \draw[->] (-1,0) -- (5,0) node[right] {\(x\)};
  % Punti discreti che rappresentano un ordine non denso (es. i numeri naturali)
  \foreach \x in {0,1,2,3,4} {
    \filldraw[black] (\x,0) circle (1pt) node[below] {\(\x\)};
  }
\end{tikzpicture}
\end{center}

Queste distinzioni ci permettono di comprendere come le relazioni possano organizzare gli insiemi e le loro proprietà, e ci forniscono una base per definire concetti più complessi come le funzioni, le quali sono relazioni particolari che ad ogni elemento del dominio associano un unico elemento del codominio.


\subsec{Le Funzioni [1]}
Una \emph{funzione} \(f\) da un insieme \(A\) ad un insieme \(B\) è definita come un sottoinsieme del prodotto cartesiano \(A\times B\) che soddisfa le seguenti due condizioni fondamentali:

\begin{enumerate}
  \item \textbf{Condizione di esistenza:} Per ogni elemento \(a \in A\) esiste almeno un elemento \(b \in B\) tale che \((a, b) \in f\). In altre parole, il dominio di \(f\) è proprio \(A\).
  
  \item \textbf{Condizione di unicità:} Per ogni elemento \(a \in A\) esiste al massimo un elemento \(b \in B\) tale che \((a, b) \in f\). Questo garantisce che a ciascun \(a\) corrisponda un unico \(b\), che denotiamo con \(f(a)\).
\end{enumerate}

In simboli, possiamo dire che \(f\) è una funzione se
\[
f \subseteq A\times B,\quad\text{e per ogni } a\in A,\quad \exists!\, b\in B \text{ tale che } (a,b)\in f.
\]

\textbf{Esempio di Funzione:}  
Consideriamo la funzione \(f\colon \mathbb{R}\to\mathbb{R}\) definita da
\[
f(x)=2x+1.
\]
Il grafico di \(f\) è l'insieme
\[
\{(x,2x+1) \mid x\in\mathbb{R}\}\subseteq \mathbb{R}\times\mathbb{R}.
\]
Qui, per ogni \(x\in\mathbb{R}\) esiste esattamente un \(y\) (dato da \(2x+1\)) che soddisfa la relazione, dunque \(f\) rispetta sia la condizione di esistenza che quella di unicità.

\textbf{Esempio di Relazione che Non è una Funzione:}  
Consideriamo la relazione \(R\) definita su \(\mathbb{R}\) da
\[
R=\{(x,y)\in\mathbb{R}\times\mathbb{R} \mid y^2=x\}.
\]
Per \(x=4\) ad esempio, esistono due possibili valori di \(y\), ossia \(y=2\) e \(y=-2\).  
Quindi, per \(x=4\) la relazione \(R\) associa due valori differenti, violando la condizione di unicità. Di conseguenza, \(R\) non è una funzione.

\begin{center}
\begin{tikzpicture}[scale=0.8]
  % Disegno degli assi cartesiani
  \draw[->] (-1,0) -- (8,0) node[right] {\(x\)};
  \draw[->] (0,-4) -- (0,4) node[above] {\(y\)};
  
  % Disegno della relazione R: y^2 = x
  % Rappresentiamo le due branche: y = sqrt(x) e y = -sqrt(x)
  \draw[blue, thick, domain=0:7, samples=100, smooth] plot (\x, {sqrt(\x)});
  \draw[blue, thick, domain=0:7, samples=100, smooth] plot (\x, {-sqrt(\x)});
  
  % Etichette per le branche (opzionali)
  \node[blue, right] at (7, {sqrt(7)}) {\(y=\sqrt{x}\)};
  \node[blue, right] at (7, {-sqrt(7)}) {\(y=-\sqrt{x}\)};
  
  % Disegno di una linea verticale tratteggiata a x = 4
  \draw[dashed, red] (4,-2.5) -- (4,2.5);
  
  % Marcatura dei punti di intersezione della linea x=4 con le due branche
  \filldraw[red] (4,2) circle (2pt) node[above left] {\((4,2)\)};
  \filldraw[red] (4,-2) circle (2pt) node[below left] {\((4,-2)\)};

\end{tikzpicture}
\end{center}

Quando definiamo la funzione radice quadrata, indicata con \(\sqrt{x}\), convenzionalmente essa restituisce l'unico numero non negativo \(y\) tale che \(y^2=x\) per ogni \(x\geq 0\). È importante notare che, sebbene l'equazione \(y^2=x\) ammetta due soluzioni (una positiva e una negativa) per \(x>0\), si sceglie di considerare soltanto la soluzione non negativa. Questa scelta, detta anche \emph{scelta del ramo principale}, non è dovuta a una limitazione matematica intrinseca, bensì ad una convenienza pratica: definendo \(\sqrt{x}\) in questo modo si garantisce che essa sia una funzione, ossia che a ogni \(x\geq0\) corrisponda un unico valore.

Questa convenzione elimina ambiguità e semplifica notevolmente i calcoli in vari contesti matematici, permettendo di utilizzare la radice quadrata in maniera univoca e coerente.

\subsubsection*{Relazioni Generate da Equazioni e Funzioni}

Un'equazione, ad esempio
\[
x^2+y^2=1,
\]
genera una relazione tra \(x\) e \(y\) costituita da tutte le coppie \((x,y)\) tali che la condizione è soddisfatta. In questo caso, l'insieme delle soluzioni coincide con la circonferenza unitaria, ovvero
\[
\{(x,y)\in \mathbb{R}^2 \mid x^2+y^2-1=0\}.
\]

Analogamente, un sistema di equazioni genera una relazione tra tutte le variabili coinvolte, stabilendo quali \(n\)-uple (dove \(n\) è il numero delle variabili) soddisfano simultaneamente il sistema. Ad esempio, il sistema
\[
\begin{cases}
x^2+y^2=1,\\[1mm]
x-y=0,
\end{cases}
\]
definisce l'insieme di tutte le coppie \((x,y)\) tali che \(x^2+y^2-1=0\) e \(x-y=0\).

Inoltre, una funzione \(f\colon A\to B\) genera una relazione, detta \emph{grafo} di \(f\), definita come
\[
\{(a,f(a)) \mid a\in A\}\subseteq A\times B.
\]
Nel caso in cui \(f\) sia data da espressioni polinomiali, il grafo di \(f\) è un esempio di varietà algebrica.

\medskip

\textbf{Definizione di Varietà Algebrica.}  
In geometria algebrica, una varietà algebrica \(\mathcal{V}\) è definita come l'insieme dei punti di \(\mathbb{R}^n\) che annullano un polinomio.

La varietà algebrica associata è definita come
\[
\mathcal{V}(f) = \{ (a_1, a_2, \dots, a_n) \in \mathbb{R}^n \mid f(a_1, a_2, \dots, a_n)=0 \}.
\]
Per esempio, la circonferenza unitaria può essere vista come la varietà algebrica
\[
\mathcal{V}(x^2+y^2-1) = \{ (x,y) \in \mathbb{R}^2 \mid x^2+y^2-1=0 \}.
\]

Questa visione unificata ci permette di studiare le relazioni non solo come insiemi di soluzioni, ma anche come oggetti geometrici dotati di una struttura algebrica fondamentale.

\subsec{Funzione Lineare e Quadratica [1]}

Le funzioni sono strumenti fondamentali in matematica per descrivere relazioni tra variabili. In particolare, le funzioni lineari e quadratiche rappresentano casi base di studio: la funzione lineare, espressa dalla formula 
\[
f(x)=ax+b,
\]
descrive una relazione costante con un grafico che è una retta, mentre la funzione quadratica, data da
\[
f(x)=ax^2+bx+c \quad (a\neq0),
\]
introduce una curvatura che si manifesta nel grafico come una parabola. Nei seguenti appunti verranno presentati esempi, proprietà e rappresentazioni grafiche per ciascun tipo di funzione.

\subsubsection*{Funzioni Lineari}

Una funzione lineare è una funzione del tipo
\[
f(x)=ax+b,
\]
con \(a,b\in\mathbb{R}\). Qui \(a\) rappresenta il coefficiente angolare (o pendenza) della retta e \(b\) l'intercetta con l'asse \(y\). Le funzioni lineari hanno dominio e codominio \(\mathbb{R}\) e il loro grafico è una retta.  
 
\textbf{Esempio:}  
Consideriamo la funzione \(f\colon\mathbb{R}\to\mathbb{R}\) definita da
\[
f(x)=2x+1.
\]
Per ogni \(x\in\mathbb{R}\), \(f(x)\) calcola un valore che varia linearmente. Il grafico di \(f\) è una retta con pendenza \(2\) e intercetta \(1\) sull'asse \(y\).

\vspace{1em}
\textbf{Rappresentazione grafica:}
\begin{center}
\begin{tikzpicture}[scale=0.8]
  % Disegno degli assi
  \draw[->] (-3,0) -- (3,0) node[right] {\(x\)};
  \draw[->] (0,-1) -- (0,5) node[above] {\(y\)};
  
  % Grafico della funzione f(x)=2x+1
  \draw[blue, thick, domain=-1.5:1.5, smooth, variable=\x] plot ({\x},{2*\x+1});
  
  % Etichette per alcuni punti
  \filldraw[black] (-1, -1) circle (2pt) node[left] {\((-1,-1)\)};
  \filldraw[black] (0, 1) circle (2pt) node[above left] {\((0,1)\)};
  \filldraw[black] (1, 3) circle (2pt) node[right] {\((1,3)\)};
\end{tikzpicture}
\end{center}

\bigskip

\subsubsection*{Funzioni Quadratiche}

Una funzione quadratica è una funzione del tipo
\[
f(x)=ax^2+bx+c,
\]
dove \(a,b,c\in\mathbb{R}\) e \(a\neq 0\). Il grafico di una funzione quadratica è una parabola. Le proprietà fondamentali di una funzione quadratica includono:
\begin{itemize}
  \item \textbf{Vertice:} il punto di massimo o minimo della parabola, che può essere calcolato come
  \[
  \left(-\frac{b}{2a},\, f\left(-\frac{b}{2a}\right)\right).
  \]
  \item \textbf{Asse di simmetria:} la retta verticale \(x=-\frac{b}{2a}\) che divide la parabola in due metà speculari.
  \item \textbf{Intersezioni con l'asse \(x\):} ottenute risolvendo l'equazione \(ax^2+bx+c=0\) mediante la formula risolutiva
  \[
  x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}.
  \]
\end{itemize}

\textbf{Esempio:}  
Consideriamo la funzione \(f\colon\mathbb{R}\to\mathbb{R}\) definita da
\[
f(x)=x^2-4x+3.
\]
Calcoliamo il vertice:
\[
x_V=-\frac{-4}{2\cdot1}=\frac{4}{2}=2,\quad f(2)=2^2-4\cdot2+3=4-8+3=-1.
\]
Pertanto, il vertice è \(V(2,-1)\).  
Le radici dell'equazione \(x^2-4x+3=0\) si ottengono risolvendo:
\[
x=\frac{4\pm\sqrt{(-4)^2-4\cdot1\cdot3}}{2}=\frac{4\pm\sqrt{16-12}}{2}=\frac{4\pm2}{2}.
\]
Quindi, \(x=1\) oppure \(x=3\); questi sono i punti in cui la parabola interseca l'asse \(x\).

\vspace{1em}
\begin{center}
\begin{tikzpicture}[scale=0.8]
  % Disegno degli assi
  \draw[->] (-1,0) -- (5,0) node[right] {\(x\)};
  \draw[->] (0,-3) -- (0,4) node[above] {\(y\)};
  
  % Grafico della funzione f(x)=x^2-4x+3
  \draw[red, thick, domain=0:4, smooth, variable=\x] plot ({\x},{\x*\x-4*\x+3});
  
  % Etichette per il vertice e le radici
  \filldraw[black] (2,-1) circle (2pt) node[below right] {\(V(2,-1)\)};
  \filldraw[black] (1,0) circle (2pt) node[below left] {\((1,0)\)};
  \filldraw[black] (3,0) circle (2pt) node[below right] {\((3,0)\)};
\end{tikzpicture}
\end{center}

\medskip

Questi appunti mostrano gli esempi di funzioni lineari e quadratiche, evidenziando le loro caratteristiche, il modo in cui si definiscono e le proprietà che ne derivano, sia dal punto di vista algebrico che grafico.

\subsec{Rette e Fasci di Rette [1]}
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

\subsec{Equazione Segmentaria della Retta [1]}
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

\subsec{Retta Passante per un Punto con Coefficiente Angolare Noto [1]}
Se in un piano cartesiano vogliamo definire la retta che \emph{passa per} un punto \((x_0, y_0)\) e ha \emph{coefficiente angolare} \(m\) (o \emph{pendenza} \(m\)), possiamo usare la \emph{forma punto-pendenza} dell’equazione di una retta:
\[
y - y_0 = m\,(x - x_0).
\]
Questa formula racchiude in modo immediato l’idea che la retta, partendo da \((x_0, y_0)\), \emph{cresce} (o decresce) secondo la pendenza \(m\). 

\begin{center}
\begin{tikzpicture}[scale=0.9, line cap=round, line join=round]
  % Assi
  \draw[->] (-1,0) -- (6,0) node[right] {$x$};
  \draw[->] (0,-1) -- (0,4) node[above] {$y$};

  % Punto (x0,y0)= (2,1)
  \coordinate (P) at (2,1);
  \fill (P) circle(2pt) node[above left] {$(x_0,y_0)$};

  % Disegno di una retta con slope= 0.75, passante per (2,1)
  % Per tracciare: x in [-0.5,5], eqn y-1=0.75(x-2)
  % => y=0.75x -1.5+1=0.75x -0.5
  \draw[thick] plot[domain=-0.5:5,smooth] 
    ({\x},{0.75*\x -0.5});
\end{tikzpicture}
\end{center}

\noindent
\textbf{Osservazione:}  
\begin{itemize}
\item Se \(m>0\), la retta è \emph{crescente}; se \(m<0\), è \emph{decrescente}; se \(m=0\), è \emph{orizzontale}.  
\item Se si volesse la \emph{forma esplicita}, basta svolgere i calcoli: \(y=y_0 + m(x-x_0)=m\,x+(y_0 -m\,x_0)\).  
\item Se \(m\) è infinito (cioè la retta è \emph{verticale}), la forma punto-pendenza non funziona: la retta si descrive con \(x=x_0\).
\end{itemize}

\medskip

\noindent
\textbf{Esempi di Utilizzo}

\begin{esempio}
\textit{Dati un punto \(P(3,2)\) e \(m=-\tfrac12\). Trovare l’equazione della retta.}

\begin{enumerate}
\item Usiamo la formula: \(y-y_0=m(x-x_0)\). Qui \((x_0,y_0)=(3,2)\) e \(m=-\tfrac12\). Quindi
  \[
    y-2 
    = -\tfrac12\,(x-3).
  \]
\item Svolgiamo: \(y-2=-\tfrac12\,x+\tfrac32\). Ossia \(y=-\tfrac12\,x+\tfrac72\). In forma \emph{esplicita}: 
  \[
    \boxed{y=-\tfrac12\,x+\tfrac72}.
  \]
\end{enumerate}
\end{esempio}

\begin{esempio}
\textit{Costruire la retta passante per \(A(1,3)\) con coefficiente angolare \(2\). Determinare dove interseca l’asse \(y\).}

\begin{enumerate}
\item \textbf{Equazione} con la formula punto-pendenza:
  \[
    y-3 
    = 2\,(x-1)
    \quad\Longrightarrow\quad
    y=2x-2+3
    = 2x+1.
  \]
\item \textbf{Intersezione con l’asse \(y\)}: poniamo \(x=0\). Da \(y=2(0)+1=1\). Quindi la retta interseca l’asse \(y\) nel punto \((0,1)\).
\end{enumerate}
\end{esempio}

\begin{esempio}
\textit{Verificare se il punto \(Q(2,0)\) appartiene alla retta passante per \((x_0,y_0)=(4,3)\) con slope \(m=\tfrac34\).}

\begin{enumerate}
\item \textbf{Equazione} della retta: 
  \[
    y-3
    = \tfrac34\,(x-4).
  \]
\item \textbf{Verifica}: sostituiamo \((x,y)=(2,0)\). Lato sinistro: \(0-3=-3\). Lato destro: \(\tfrac34\,(2-4)=\tfrac34\times(-2)=-\tfrac32\). Poiché \(-3\neq -\tfrac32\), il punto \((2,0)\) \emph{non} soddisfa l’equazione. Quindi \(Q\) non appartiene alla retta.
\end{enumerate}
\end{esempio}

\smallskip

\noindent
\textbf{Conclusione:}  
La \emph{forma punto-pendenza} \(y-y_0=m(x-x_0)\) è la più diretta quando conosciamo \emph{un punto} e \emph{il coefficiente angolare} \(m\). In geometria analitica, si adopera spesso questa formula per passare da \emph{condizioni geometriche} (posizione di un punto, pendenza data) all’equazione \emph{algebrica} della retta. 

\subsec{Rette Parallele e Perpendicolari [1]}
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

\subsec{Equazione delle Parabola: Vertice e Fuoco [1]}
La parabola è la rappresentazione grafica della varietà algebrica di un polinomio di secondo grado. Tuttavia, ci sono alcuni punti notevoli – come il vertice, il fuoco e la direttrice – che ci interessa poter calcolare con facilità. Per questo motivo, spesso riscriviamo l'equazione della parabola in una forma detta \emph{canonica}.

Un modo più semplice per determinare questi punti, dato il vertice \(V(h,k)\) e il fuoco \(F(h,k+p)\) (con \(p>0\) se la parabola apre verso l'alto e \(p<0\) se apre verso il basso), è usare le seguenti due formule fondamentali:

\[
y-k=\frac{1}{4p}(x-h)^2
\]
che esprime la parabola in forma canonica, e

\[
F(h,k+p) \quad\text{e}\quad \text{Direttrice: } y=k-p.
\]

Queste formule derivano dalla definizione geometrica della parabola come il luogo dei punti equidistanti da un punto fisso (il fuoco) e da una retta fissa (la direttrice). In particolare, la condizione che per ogni punto \((x,y)\) della parabola la distanza da \(F\) sia uguale alla distanza dalla direttrice porta, attraverso i calcoli algebrici, alla forma canonica sopra esposta.

\subsubsection*{La Forma Canonica della Parabola}

Un modo quindi per definire una parabola è usando la formula canonica. Dato un disengo infatti, basta misurare il vertice \(V(h,k)\) della parabola e la distanza focale \(p\) (cioè la distanza tra il vertice e il fuoco), l'equazione della parabola in forma canonica è:
\[
y-k=\frac{1}{4p}(x-h)^2.
\]

\medskip
\textbf{Passaggio da un polinomio di secondo grado alla forma canonica:}  
Consideriamo un polinomio di secondo grado generico uguale a \(y\):
\[
y = ax^2 + bx + c,\quad a\neq0.
\]
Per trasformarlo nella forma canonica, eseguiamo i seguenti passaggi:

\medskip
\textbf{1. Dividere per \(a\) (se \(a\neq1\)):}
\[
y = a\left(x^2 + \frac{b}{a}x\right) + c.
\]

\medskip
\textbf{2. Completare il quadrato:}  
Aggiungiamo e sottraiamo il termine \(\left(\frac{b}{2a}\right)^2\) all'interno della parentesi:
\[
x^2+\frac{b}{a}x = \left(x^2+\frac{b}{a}x+\left(\frac{b}{2a}\right)^2\right)-\left(\frac{b}{2a}\right)^2,
\]
quindi l'equazione diventa:
\[
y = a\left[\left(x+\frac{b}{2a}\right)^2-\left(\frac{b}{2a}\right)^2\right] + c.
\]
Espandendo:
\[
y = a\left(x+\frac{b}{2a}\right)^2 + \left(c - \frac{b^2}{4a}\right).
\]

\medskip
\textbf{3. Identificare il vertice e riscrivere la formula:}  
Confrontando con la forma canonica \(y-k=\frac{1}{4p}(x-h)^2\) possiamo identificare:
\[
h=-\frac{b}{2a},\qquad k = c-\frac{b^2}{4a}.
\]
Quindi il vertice è \(V\left(-\frac{b}{2a},\, c-\frac{b^2}{4a}\right)\).

\medskip
\textbf{4. Determinare il parametro focale \(p\):}  
L'equazione riscritta è
\[
y-k = a\left(x-h\right)^2.
\]
Confrontandola con
\[
y-k=\frac{1}{4p}(x-h)^2,
\]
si ottiene
\[
a=\frac{1}{4p}\quad\Longrightarrow\quad p=\frac{1}{4a}.
\]
Questa relazione stabilisce la distanza focale in funzione del coefficiente \(a\) (vale per il caso in cui \(a>0\); se \(a<0\) la parabola apre verso il basso, ma il procedimento è analogo).

\medskip
\textbf{Esempio:}  
Consideriamo l'equazione
\[
y = 2x^2 - 8x + 5.
\]
\emph{Passo 1:} Dividiamo per \(2\):
\[
y = 2\left(x^2 - 4x\right) + 5.
\]
\emph{Passo 2:} Completamento del quadrato per \(x^2-4x\):
\[
x^2 - 4x = (x^2-4x+4) - 4 = (x-2)^2 - 4.
\]
Pertanto:
\[
y = 2\left[(x-2)^2 - 4\right] + 5 = 2(x-2)^2 - 8 + 5 = 2(x-2)^2 - 3.
\]
Riscriviamo l'equazione come:
\[
y + 3 = 2(x-2)^2.
\]
\emph{Passo 3:} Confrontando con la forma canonica \(y-k=\frac{1}{4p}(x-h)^2\), abbiamo:
\[
h=2,\quad k=-3,\quad \frac{1}{4p}=2 \quad\Longrightarrow\quad p=\frac{1}{8}.
\]
Quindi il vertice della parabola è \(V(2,-3)\). Poiché la parabola apre verso l'alto (dato \(a=2>0\)), il fuoco è \(F(2,-3+p) = \left(2,-3+\frac{1}{8}\right) = \left(2,-\frac{23}{8}\right)\) e la direttrice è la retta
\[
y=k-p=-3-\frac{1}{8}=-\frac{25}{8}.
\]

\medskip
Questa procedura mostra come ogni polinomio di secondo grado nella forma
\[
y=ax^2+bx+c,
\]
possa essere trasformato, mediante il completamento del quadrato, nella forma canonica
\[
y-k=\frac{1}{4p}(x-h)^2,
\]
che esprime la parabola in termini del suo vertice \(V(h,k)\) e della distanza focale \(p\).  

\medskip

\textbf{Esempio:} Consideriamo una parabola con vertice \(V(2,3)\) e fuoco \(F(2,5)\).  
In questo caso la distanza focale è
\[
p=5-3=2.
\]
L'equazione della parabola diventa:
\[
y-3=\frac{1}{4\cdot2}(x-2)^2=\frac{1}{8}(x-2)^2,
\]
ovvero
\[
y=\frac{1}{8}(x-2)^2+3.
\]
Il fuoco è \(F(2,3+2)=(2,5)\) e la direttrice è la retta \(y=3-2=1\). Per ogni punto \(P(x,y)\) della parabola, la distanza da \(P\) al fuoco risulta uguale alla distanza da \(P\) alla direttrice.

\medskip

\begin{center}
\begin{tikzpicture}[scale=0.8]
  % Disegno degli assi cartesiani
  \draw[->] (-5,0) -- (7,0) node[right] {\(x\)};
  \draw[->] (0,-1) -- (0,7) node[above] {\(y\)};
  
  % Disegno della parabola y = (1/8)(x-2)^2 + 3
  \draw[red, thick, domain=-3:8, samples=100, smooth] plot ({\x}, {1/8*(\x-2)^2+3});
  
  % Marcatura del vertice V(2,3)
  \filldraw[black] (2,3) circle (2pt) node[below left] {\(V(2,3)\)};
  
  % Marcatura del fuoco F(2,5)
  \filldraw[blue] (2,5) circle (2pt) node[above left] {\(F(2,5)\)};
  
  % Disegno della direttrice y = 1 (linea tratteggiata)
  \draw[dashed, gray] (-5,1) -- (7,1) node[right] {\(\text{Direttrice } y=1\)};

  
  % Frecce che indicano la distanza focale
  \draw[->, blue] (2,3) -- (2,5);
  \node[blue] at (2.3,4) {\(2\)};
\end{tikzpicture}
\end{center}

\subsec{Determinare una Parabola da Tre Punti [1]}

Per determinare una parabola si possono considerare diversi casi in base al numero di punti dati:
\begin{enumerate}
  \item \textbf{Un solo punto:}  
  Dato un punto \(P\), esiste un intero \emph{fascio} di parabole che passano per \(P\). In altre parole, una singola condizione non è sufficiente a determinare in modo univoco l'equazione di una parabola, poiché possiamo variare liberamente il parametro che controlla la curvatura e spostare il vertice.
  
  \medskip
  \textbf{Esempio grafico:}  
Consideriamo il punto \(P(2,3)\). Il disegno seguente mostra diverse parabole che passano per \(P\) ma non hanno \(P\) come vertice.

\begin{center}
\begin{tikzpicture}[scale=0.8]
  % Assi cartesiani
  \draw[->] (-1,0) -- (6,0) node[right] {\(x\)};
  \draw[->] (0,-1) -- (0,6) node[above] {\(y\)};
  
  % Punto P
  \filldraw[black] (2,3) circle (2pt) node[above right] {\(P(2,3)\)};
  
  % Parabola 1: Vertice V1(1,1), equazione: y = 2(x-1)^2 + 1 (in blu)
  \draw[blue, thick, domain=-0.6:2.6, samples=100, smooth] plot (\x, {2*(\x-1)^2+1});
  
  % Parabola 2: Vertice V2(3,1), equazione: y = 2(x-3)^2 + 1 (in rosso)
  \draw[red, thick, domain=1.4:4.6, samples=100, smooth] plot (\x, {2*(\x-3)^2+1});
  
  % Parabola 3: Vertice V3(1,4), equazione: y = -1*(\x-1)^2 + 4 (in verde)
  \draw[green, thick, domain=-1.2:3.2, samples=100, smooth] plot (\x, {-1*(\x-1)^2+4});
\end{tikzpicture}
\end{center}
  
  \item \textbf{Due punti:}  
  Se vengono dati due punti distinti, ad esempio \(P(2,3)\) e \(Q(4,5)\), allora esiste un \emph{fascio uniparametrico} di parabole che li contengono. Infatti, due condizioni fissano una relazione tra i coefficienti ma rimane ancora un grado di libertà.
  
  \medskip
\textbf{Esempio grafico:}  
Il disegno seguente mostra diverse parabole che passano per i punti \(P(2,3)\) e \(Q(4,5)\). Queste parabole appartengono a un fascio uniparametrico, poiché due condizioni (passare per \(P\) e \(Q\)) non fissano univocamente la parabola: il vertice può variare. Di seguito riportiamo tre esempi, ottenuti scegliendo diversi valori per il vertice e calcolando di conseguenza il coefficiente della forma canonica \(y-k=a(x-h)^2\).

\begin{center}
\begin{tikzpicture}[scale=0.8]
  % Assi cartesiani
  \draw[->] (-1,0) -- (6,0) node[right] {\(x\)};
  \draw[->] (0,-1) -- (0,6) node[above] {\(y\)};
  
  % Punti fissi P e Q
  \filldraw[black] (2,3) circle (2pt) node[below left] {\(P(2,3)\)};
  \filldraw[black] (4,5) circle (2pt) node[right] {\(Q(4,5)\)};
  
  % Disegno della Parabola 1: y = (x-2.5)^2 + 2.75 (in blu)
  \draw[blue, thick, domain=0.5:4.5, samples=100, smooth] plot (\x, {(\x-2.5)^2+2.75});
  
  % Disegno della Parabola 2: y = -(x-3.5)^2 + 5.25 (in rosso)
  \draw[red, thick, domain=1:6, samples=100, smooth] plot (\x, {-(\x-3.5)^2+5.25});
  
  % Disegno della Parabola 3: y = (1/3)(x-1.5)^2 + 35/12 (in verde)
  \draw[green, thick, domain=-1:5, samples=100, smooth] plot (\x, {1/3*(\x-1.5)^2+35/12});
\end{tikzpicture}
\end{center}
  
  \item \textbf{Tre punti:}  
  Se vengono dati tre punti distinti, non allineati, ad esempio \(P(1,2)\), \(Q(3,4)\) e \(R(5,3)\), allora esiste \emph{una sola} parabola che li passa, poiché le tre condizioni determinano in modo univoco i tre coefficienti dell'equazione quadratica.
  
  \medskip
\textbf{Esempio grafico:}  
Il seguente disegno mostra il triangolo formato dai tre punti \(P(1,2)\), \(Q(3,4)\) e \(R(5,3)\) e la parabola unica che li contiene.

\begin{center}
\begin{tikzpicture}[scale=0.8]
  % Assi cartesiani
  \draw[->] (0,0) -- (7,0) node[right] {\(x\)};
  \draw[->] (0,0) -- (0,6) node[above] {\(y\)};
  
  % Punti P, Q, R
  \filldraw[black] (1,2) circle (2pt) node[left] {\(P(1,2)\)};
  \filldraw[black] (3,4) circle (2pt) node[above] {\(Q(3,4)\)};
  \filldraw[black] (5,3) circle (2pt) node[right] {\(R(5,3)\)};
  
  % Disegno del triangolo formato dai punti
  \draw[dotted] (1,2) -- (3,4) -- (5,3) -- cycle;
  
  % Disegno della parabola unica che passa per i tre punti:
  % y = -0.375x^2 + 2.5x - 0.125
  \draw[red, thick, domain=0:7, samples=100, smooth] plot (\x, {-0.375*(\x)^2 + 2.5*(\x) - 0.125});

\end{tikzpicture}
\end{center}
\end{enumerate}
Dato che un triangolo è determinato in modo univoco da tre punti non collineari e, analogamente, una parabola è univocamente determinata da tre punti distinti (non facenti parte di una retta) appartenenti ad essa, possiamo stabilire una corrispondenza interessante tra queste due strutture. In altre parole:

\begin{itemize}
  \item Per ogni insieme di tre punti non collineari, esiste una e una sola parabola che li contiene.
  \item Viceversa, dato che una parabola è definita da tre punti distinti, si possono sempre scegliere tre punti sulla parabola per formare un triangolo.
\end{itemize}

Questa osservazione implica che, in un certo senso, ogni triangolo (inteso come insieme di tre punti nel piano) può essere associato a una parabola unica che li contiene, e ogni parabola può essere vista come generatrice di un triangolo scelto tra i suoi punti. Tale associazione offre un'interessante prospettiva per studiare le proprietà geometriche e algebriche sia dei triangoli sia delle parabole, evidenziando la relazione profonda tra la determinazione dei punti e la forma delle curve nel piano.

\bigskip
\subsubsection*{Procedimento Algebraico}

Supponiamo di voler determinare l'equazione della parabola nella forma generale
\[
y=ax^2+bx+c,
\]
che deve passare per tre punti distinti \(P(x_1,y_1)\), \(Q(x_2,y_2)\) e \(R(x_3,y_3)\). Sostituendo ciascun punto nell'equazione otteniamo il seguente sistema lineare:
\[
\begin{cases}
ax_1^2+bx_1+c=y_1,\\[1mm]
ax_2^2+bx_2+c=y_2,\\[1mm]
ax_3^2+bx_3+c=y_3.
\end{cases}
\]
Questo sistema può essere risolto con metodi algebrici (ad esempio, sostituzione, eliminazione o matrice inversa) per determinare i coefficienti \(a\), \(b\) e \(c\).

\medskip
\textbf{Esempio:}  
Determiniamo la parabola che passa per i punti \(P(1,2)\), \(Q(3,4)\) e \(R(5,3)\). Sostituendo questi valori nella forma generale:
\[
\begin{cases}
a\cdot 1^2+b\cdot1+c=2,\\[1mm]
a\cdot 3^2+b\cdot3+c=4,\\[1mm]
a\cdot 5^2+b\cdot5+c=3,
\end{cases}
\]
ossia
\[
\begin{cases}
a+b+c=2,\\[1mm]
9a+3b+c=4,\\[1mm]
25a+5b+c=3.
\end{cases}
\]
Sottraendo la prima equazione dalla seconda e dalla terza per eliminare \(c\):
\[
\begin{aligned}
(9a+3b+c)-(a+b+c)&=8a+2b=4-2=2,\\[1mm]
(25a+5b+c)-(a+b+c)&=24a+4b=3-2=1.
\end{aligned}
\]
Da cui:
\[
8a+2b=2 \quad\Longrightarrow\quad 4a+b=1,\quad (1)
\]
\[
24a+4b=1 \quad\Longrightarrow\quad 6a+b=\frac{1}{4},\quad (2)
\]
Sottraendo (2) da (1):
\[
(4a+b) - (6a+b) = 1-\frac{1}{4} \quad\Longrightarrow\quad -2a=\frac{3}{4}\quad\Longrightarrow\quad a=-\frac{3}{8}.
\]
Sostituendo \(a=-\frac{3}{8}\) in (1):
\[
4\left(-\frac{3}{8}\right)+b=1\quad\Longrightarrow\quad -\frac{3}{2}+b=1\quad\Longrightarrow\quad b=1+\frac{3}{2}=\frac{5}{2}.
\]
Infine, sostituendo \(a\) e \(b\) nella prima equazione:
\[
-\frac{3}{8}+\frac{5}{2}+c=2\quad\Longrightarrow\quad c=2+\frac{3}{8}-\frac{5}{2}.
\]
Calcolando:
\[
\frac{5}{2}=\frac{20}{8},\quad 2=\frac{16}{8},\quad c=\frac{16+3-20}{8}=\frac{-1}{8}.
\]
Quindi, l'equazione della parabola è:
\[
y=-\frac{3}{8}x^2+\frac{5}{2}x-\frac{1}{8}.
\]
Questo esempio mostra come, partendo da tre punti, il sistema determinante per \(a\), \(b\) e \(c\) abbia una soluzione unica, definendo in modo univoco la parabola passante per quei punti.

\subsec{Determinare una Parabola da il Vertice ed un Punto [1]}
Consideriamo le seguenti situazioni:

\begin{enumerate}
  \item \textbf{Fissato il vertice:}  
  Se fissiamo il vertice \(V(2,3)\) di una parabola, allora le parabole aventi quel vertice hanno equazione della forma
  \[
  y-3=a(x-2)^2,\quad a\in\mathbb{R}\setminus\{0\}.
  \]
  In questo caso, per valori diversi di \(a\) otteniamo un intero \emph{fascio} di parabole, che non coincidono tra loro (il vertice è comune, ma la curvatura varia).  
  \medskip
  
  \textbf{Disegno:}
  \begin{center}
  \begin{tikzpicture}[scale=0.8]
    % Assi cartesiani
    \draw[->] (-1,0) -- (6,0) node[right] {\(x\)};
    \draw[->] (0,-1) -- (0,6) node[above] {\(y\)};
    
    % Vertice fisso V(2,3)
    \filldraw[black] (2,3) circle (2pt) node[above right] {\(V(2,3)\)};

\draw[blue, thick, domain=-0.83:4.83, samples=100, smooth] plot (\x, {0.5*(\x-2)^2+3});

\draw[red, thick, domain=0:4, samples=100, smooth] plot (\x, {1*(\x-2)^2+3});
 
\draw[green, thick, domain=0.59:3.41, samples=100, smooth] plot (\x, {2*(\x-2)^2+3});


\draw[purple, thick, domain=0:4, samples=100, smooth] plot (\x, {-1*(\x-2)^2+3});
    
  \end{tikzpicture}
  \end{center}
  
  \item \textbf{Fissato il vertice e un altro punto:}  
  Se, oltre al vertice \(V(2,3)\), fissiamo anche un altro punto, ad esempio \(P(4,5)\), la condizione che la parabola passi per entrambi determina in maniera univoca il parametro \(a\).  
  Imponendo \(P(4,5)\) nella forma \(y-3=a(x-2)^2\) otteniamo:
  \[
  5-3=a(4-2)^2\quad\Longrightarrow\quad 2=a\cdot4\quad\Longrightarrow\quad a=\frac{1}{2}.
  \]
  La parabola unica che passa per \(V(2,3)\) e \(P(4,5)\) è dunque:
  \[
  y-3=\frac{1}{2}(x-2)^2.
  \]
  
  \begin{center}
  \begin{tikzpicture}[scale=0.8]
    % Assi cartesiani
    \draw[->] (-1,0) -- (6,0) node[right] {\(x\)};
    \draw[->] (0,-1) -- (0,6) node[above] {\(y\)};
    
    % Vertice V(2,3) e punto P(4,5)
    \filldraw[black] (2,3) circle (2pt) node[below] {\(V(2,3)\)};
    \filldraw[black] (4,5) circle (2pt) node[right] {\(P(4,5)\)};
    
    % Disegno della parabola unica: y-3 = 0.5(x-2)^2
    \draw[red, thick, domain=-1:5, samples=100, smooth] plot (\x, {0.5*(\x-2)^2+3});

  \end{tikzpicture}
  \end{center}
\end{enumerate}

\subsubsection*{Procedimento Algebraico}

Sia \(V(h,k)\) il vertice di una parabola con asse verticale. L'equazione della parabola in forma canonica si esprime come
\[
y-k = a(x-h)^2.
\]
Se, inoltre, conosciamo un punto \(P(x_1,y_1)\) che appartiene alla parabola, possiamo determinare il coefficiente \(a\) imponendo che il punto soddisfi l'equazione:
\[
y_1 - k = a (x_1 - h)^2.
\]
Da cui si ricava:
\[
a = \frac{y_1-k}{(x_1-h)^2}.
\]
Questo valore di \(a\) definisce univocamente la parabola che ha vertice \(V(h,k)\) e passa per \(P(x_1,y_1)\).

\medskip
\textbf{Esempio:}  
Supponiamo che il vertice della parabola sia \(V(2,3)\) e che la parabola passi per il punto \(P(4,5)\).  
Calcoliamo \(a\):
\[
a = \frac{5-3}{(4-2)^2} = \frac{2}{4} = \frac{1}{2}.
\]
Pertanto, l'equazione della parabola diventa:
\[
y-3 = \frac{1}{2}(x-2)^2,\quad \text{cioè}\quad y = \frac{1}{2}(x-2)^2+3.
\]

\medskip

\begin{center}
\begin{tikzpicture}[scale=0.8]
  % Disegno degli assi cartesiani
  \draw[->] (-1,0) -- (6,0) node[right] {\(x\)};
  \draw[->] (0,-1) -- (0,7) node[above] {\(y\)};
  
  % Vertice V(2,3)
  \filldraw[black] (2,3) circle (2pt) node[above left] {\(V(2,3)\)};
  
  % Punto P(4,5)
  \filldraw[black] (4,5) circle (2pt) node[above right] {\(P(4,5)\)};
  
  % Disegno della parabola: y - 3 = 1/2(x-2)^2
  \draw[red, thick, domain=-1:5.2, samples=100, smooth] plot (\x, {0.5*(\x-2)^2+3});
\end{tikzpicture}
\end{center}

\subsec{Determinare una Parabola dal Vertice ed il Fuoco [1]}

Consideriamo la seguente procedura, che illustra come, fissato il vertice e il fuoco, si determini univocamente la parabola:

\begin{enumerate}
  \item \textbf{Fissato il vertice:}  
  Se fissiamo il vertice \(V(2,3)\) di una parabola, allora le parabole aventi quel vertice hanno equazione della forma
  \[
  y-3=a(x-2)^2,\quad a\in\mathbb{R}\setminus\{0\}.
  \]
  In questo caso, per valori diversi di \(a\) otteniamo un intero \emph{fascio} di parabole, che non coincidono tra loro (il vertice è comune, ma la curvatura varia).  

  \begin{center}
  \begin{tikzpicture}[scale=0.8]
    % Assi cartesiani
    \draw[->] (-1,0) -- (6,0) node[right] {\(x\)};
    \draw[->] (0,-1) -- (0,6) node[above] {\(y\)};
    
    % Vertice fisso V(2,3)
    \filldraw[black] (2,3) circle (2pt) node[above right] {\(V(2,3)\)};

\draw[blue, thick, domain=-0.83:4.83, samples=100, smooth] plot (\x, {0.5*(\x-2)^2+3});

\draw[red, thick, domain=0:4, samples=100, smooth] plot (\x, {1*(\x-2)^2+3});
 
\draw[green, thick, domain=0.59:3.41, samples=100, smooth] plot (\x, {2*(\x-2)^2+3});


\draw[purple, thick, domain=0:4, samples=100, smooth] plot (\x, {-1*(\x-2)^2+3});
    
  \end{tikzpicture}
  \end{center}

\item \textbf{Fissiamo il fuoco:}  
Supponiamo di voler fissare, oltre al vertice, anche il fuoco \(F\) della parabola. Quando il vertice \(V(h,k)\) e il fuoco \(F(h,k+p)\) sono entrambi fissati, la distanza focale \(p\) è determinata e, di conseguenza, la parabola è univocamente definita dalla forma canonica
\[
y-k=\frac{1}{4p}(x-h)^2.
\]

\begin{center}
\begin{tikzpicture}[scale=0.8]
  % Assi cartesiani
  \draw[->] (-1,0) -- (7,0) node[right] {\(x\)};
  \draw[->] (0,-1) -- (0,8) node[above] {\(y\)};
  
  % Disegno della parabola: y-3 = (1/6)(x-2)^2
  \draw[red, thick, domain=-1:7, samples=100, smooth] plot (\x, {1/6*(\x-2)^2+3});
  
  % Vertice V(2,3)
  \filldraw[black] (2,3) circle (2pt) node[below left] {\(V(2,3)\)};
  
  % Fuoco F(2,4.5)
  \filldraw[blue] (2,4.5) circle (2pt) node[above left] {\(F(2,4.5)\)};
  
  % Direttrice: y = k-p = 3-1.5 = 1.5 (linea tratteggiata)
  \draw[dashed, gray] (-1,1.5) -- (7,1.5) node[right] {\(\text{Direttrice } y=1.5\)};
  
  % Freccia che indica la distanza focale p=1.5
  \draw[-, blue, dashed, thick] (2,3) -- (2,4.5) node[midway, right] {\(1.5\)};
\end{tikzpicture}
\end{center}
\end{enumerate}

\subsubsection*{Procedimento Algebraico}

Per determinare l'equazione di una parabola a partire dal vertice e dal fuoco, si procede con le seguenti operazioni generali:

\begin{enumerate}
  \item \textbf{Identificare il vertice:}  
  Sia il vertice \(V(h,k)\) della parabola.

  \item \textbf{Determinare il fuoco e la distanza focale:}  
  Supponiamo che il fuoco sia \(F(h,k+p)\). La distanza focale è data da \(p=|k_F-k|\). 

  \item \textbf{Utilizzare la forma canonica:}  
  Con l'asse della parabola verticale, la forma canonica è
  \[
  y-k=\frac{1}{4p}(x-h)^2.
  \]
  Questa equazione deriva dalla condizione geometrica che ogni punto della parabola ha la stessa distanza dal fuoco e dalla direttrice \(y=k-p\).

  \item \textbf{Sostituire i valori noti:}  
  Inserendo \(h\), \(k\) e \(p\) nella formula, si ottiene l'equazione esplicita della parabola.
\end{enumerate}

\medskip
\textbf{Esempio:}  
Supponiamo di avere il vertice \(V(-3,6)\) e il fuoco \(F(-3,4.5)\).  
La distanza focale è
\[
p=6-4.5=1.5.
\]
Sostituendo nella forma canonica per una parabola con asse verticale che apre verso il basso (in questo caso, il fuoco si trova sotto il vertice e la direttrice è data da \(y=k+p\)):
\[
y-6=-\frac{1}{4\cdot1.5}(x+3)^2=-\frac{1}{6}(x+3)^2.
\]
Pertanto, l'equazione della parabola è
\[
y=-\frac{1}{6}(x+3)^2+6.
\]

\medskip

\textbf{Disegno Rappresentativo:}

\begin{center}
\begin{tikzpicture}[scale=0.9]
  % Disegno degli assi cartesiani
  \draw[->] (-7,0) -- (1,0) node[right] {\(x\)};
  \draw[->] (0,-1) -- (0,8) node[above] {\(y\)};
  
  % Disegno della parabola: y-6 = -(1/6)(x+3)^2
  \draw[red, thick, domain=-7:1, samples=100, smooth] plot (\x, {-1/6*(\x+3)^2+6});
  
  % Marcatura del vertice V(-3,6)
  \filldraw[black] (-3,6) circle (2pt) node[above right] {\(V(-3,6)\)};
  
  % Marcatura del fuoco F(-3,4.5)
  \filldraw[blue] (-3,4.5) circle (2pt) node[below right] {\(F(-3,4.5)\)};
  
  % Disegno della direttrice: per una parabola che apre verso il basso, la direttrice è data da y = k+p
  \draw[dashed, gray] (-7,7.5) -- (1,7.5) node[right] {\(\text{Direttrice } y=7.5\)};
  
  % Freccia che indica la distanza focale p=1.5 (dal vertice al fuoco)
  \draw[-, blue, dashed, thick] (-3,6) -- (-3,4.5) node[midway, right] {\(1.5\)};

\end{tikzpicture}
\end{center}

\subsec{La Retta Tangente e la Derivata [1]} 


La retta tangente a una curva in un punto è, in termini semplici, la linea che \q{tocca} la curva in quel punto e ne segue la direzione locale. Immaginate di avere una strada tortuosa e di voler approssimare la sua forma in un tratto molto breve con una linea retta: quella linea, che si adatta perfettamente al percorso in quel punto, è la tangente. In altre parole, la tangente fornisce una buona approssimazione lineare della curva intorno al punto di contatto, catturandone la pendenza esatta in quel momento.

\begin{center}
\begin{tikzpicture}[scale=1.0]
  % Disegno del cerchio con centro (0,0) e raggio 2
  \draw[thick] (0,0) circle (2);
  
  % Disegno della retta tangente al cerchio nel punto (2,0)
  \draw[red, thick] (2,-2.5) -- (2,2.5);
  
  % Marcatura del punto di tangenza
  \filldraw[black] (2,0) circle (2pt) node[right] {\(T\)};
\end{tikzpicture}
\end{center}

\subsubsection*{Derivata di Polinomi di Secondo Grado}

La derivazione è un'operazione fondamentale che permette di determinare il tasso di variazione di una funzione. Ad esempio, se consideriamo una funzione costante \(f(x)=c\), dove \(c\) è una costante reale, notiamo che il valore della funzione non varia al variare di \(x\); per questo motivo la sua derivata è zero, ovvero \(\frac{d}{dx}(c)=0\).

\begin{center}
\begin{tikzpicture}[scale=0.7]
  % Disegno degli assi cartesiani
  \draw[->] (-1,0) -- (5,0) node[right] {\(x\)};
  \draw[->] (0,-1) -- (0,5) node[above] {\(y\)};
  
  % Disegno della funzione costante f(x)=c, ad esempio c=3
  \draw[red, thick, domain=-1:5] plot (\x, {3});
  \node[red, right] at (5,3) {\(f(x)=3\)};
  
  % Marcatura di un punto della funzione
  \filldraw[black] (2,3) circle (2pt) node[above left] {\(P(2,3)\)};
  
  % Disegno della tangente in P (che coincide con la funzione costante)
  \draw[->, blue, thick] (2,3) -- (4,3) node[midway, above] {\(m=0\)};
  
  % Annotazione esplicativa
  \node at (2,1) {\(\frac{d}{dx}(c)=0\)};
\end{tikzpicture}
\end{center}

Per una funzione lineare della forma \(f(x)=ax+b\), il termine \(ax\) varia in modo costante, mentre il termine \(b\) essendo costante non contribuisce alla variazione. Notiamo infatti che la pendenza della curva, ossia della retta, rimane costante e quindi la sua derivata è infatti la funzione costante, si ottiene che la derivata di \(ax\) è \(a\) e quella di \(b\) è zero, per cui \(\frac{d}{dx}(ax+b)=a\).

\begin{center}
\begin{tikzpicture}[scale=0.7]
  % Disegno degli assi cartesiani
  \draw[->] (-1,0) -- (5,0) node[right] {\(x\)};
  \draw[->] (0,-1) -- (0,10) node[above] {\(y\)};
  
  % Grafico della funzione lineare f(x)=2x+1 (in rosso)
  \draw[red, thick, domain=-1:4] plot (\x, {2*\x+1});
  \node[red, right] at (4.5,10) {\(f(x)=2x+1\)};
  
  % Punto P(2,5) sulla funzione
  \filldraw[black] (2,5) circle (2pt) node[above left] {\(P(2,5)\)};
  
  % Grafico della derivata, che è una retta costante f'(x)=2 (in blu)
  \draw[blue, thick, domain=-1:5] plot (\x, {2});
  \node[blue, above] at (4,2) {\(f'(x)=2\)};
  
  % Annotazione per evidenziare che la derivata è costante
  \node at (2,0.5) {\(\frac{d}{dx}(2x+1)=2\)};
\end{tikzpicture}
\end{center}

Nel caso di un polinomio di secondo grado, ad esempio \(f(x)=ax^2+bx+c\), il termine \(ax^2\) ha derivata \(2ax\), mentre \(bx\) deriva in \(b\) e la costante \(c\) deriva in 0. Di conseguenza, la derivata di \(f(x)\) risulta essere
\[
\frac{d}{dx}(ax^2+bx+c)=2ax+b.
\]

\begin{center}
\begin{tikzpicture}[scale=0.7]
  % Assi cartesiani
  \draw[->] (-1,0) -- (5,0) node[right] {\(x\)};
  \draw[->] (0,-2) -- (0,6) node[above] {\(y\)};
  
  % Grafico della funzione quadratica: f(x)= x^2 - 4x + 3
  \draw[red, thick, domain=-0.5:4.5, samples=100, smooth] plot (\x, {(\x)^2 - 4*\x + 3});
  \node[red] at (8, {((4.5)^2 - 4*4.5 + 3)+0.5}) {\(f(x)=x^2-4x+3\)};
  
  % Grafico della derivata: f'(x)= 2x - 4
  \draw[blue, thick, domain=0.2:5, samples=100, smooth] plot (\x, {2*\x - 4});
  \node[blue] at (8, {2*4-4+0.5}) {\(f'(x)=2x-4\)};
  
  % Punto di esempio sulla funzione
  \filldraw[black] (2, {2*2-4*2+3}) circle (2pt) node[above right] {\(P(2,-1)\)};
\end{tikzpicture}
\end{center}

Notiamo infatti che quando la pendenza della parabola passa dall'essere negativa (star scendendo) ad essere positiva (star sapendo), ossia nel punto di vertice, anche la retta stessa cambia di segno toccando lo zero nella stessa coordinata $x$ del vertice della parabola di cui è la derivata.

\subsubsection*{Derivata di Polinomi}

Per capire meglio la ragione dietro alle formule che abbiamo visto sopra, vediamo come funziona in generale la derivata di un polinomio. Per capirla a fondo, basta avere confidenza con due nozioni: la derivata di un monomio e la linearità della derivata.

È importante evidenziare che la derivazione è un'operazione lineare: la derivata della somma di due funzioni è pari alla somma delle loro derivate, ovvero
\[
\frac{d}{dx}[f(x)+g(x)] = f'(x)+g'(x),
\]
e la derivata di una costante moltiplicata per una funzione è la costante moltiplicata per la derivata della funzione, cioè
\[
\frac{d}{dx}[cf(x)] = c\,f'(x).
\]

Queste regole consentono di calcolare in modo rapido la derivata di qualsiasi polinomio, ottenendo così il coefficiente angolare della retta tangente alla curva in un dato punto.

La derivazione di un polinomio si effettua applicando la regola della potenza a ciascun termine. In generale, se consideriamo un termine della forma
\[
a x^n,
\]
dove \(a\) è una costante e \(n\) un intero non negativo, la sua derivata è
\[
\frac{d}{dx}(a x^n)=a n x^{n-1}.
\]
Poiché la derivazione è un'operazione lineare, la derivata di un polinomio, che è una somma di termini, si ottiene derivando ogni termine e sommando i risultati. Ad esempio, per il polinomio
\[
f(x)=ax^2+bx+c,
\]
la derivata risulta essere
\[
f'(x)=2ax+b,
\]
poiché la derivata della costante \(c\) è zero.

\noindent\textbf{Esempio}
\noindent
Consideriamo il polinomio
\[
f(x)=3x^8-2x^5+x^3+7.
\]
Applicando la regola della potenza a ciascun termine, otteniamo:
\[
\frac{d}{dx}(3x^8)=3\cdot8\,x^{7}=24x^7,
\]
\[
\frac{d}{dx}(-2x^5)=-2\cdot5\,x^{4}=-10x^4,
\]
\[
\frac{d}{dx}(x^3)=3x^2,
\]
\[
\frac{d}{dx}(7)=0.
\]
Pertanto, la derivata del polinomio è:
\[
f'(x)=24x^7-10x^4+3x^2.
\]

\subsec{La Retta Tangente della Parabola [1]} 
Per un polinomio \(f(x)\), la retta tangente al punto \(P(x_0,f(x_0))\) è data dall'equazione
\[
y-f(x_0)=f'(x_0)(x-x_0).
\]
Questo procedimento è particolarmente utile per funzioni semplici, come le parabole, in cui la derivata si calcola facilmente. Nel caso di una parabola, che è un polinomio di secondo grado, la derivata viene ottenuta applicando la regola della potenza ad ogni termine, e il valore ottenuto in un punto di interesse ci permette di determinare in modo univoco la retta tangente.

\begin{esempio}
Consideriamo la parabola definita da
\[
f(x)=\frac{1}{2}(x-2)^2+3.
\]
Il vertice di questa parabola è \(V(2,3)\). Calcoliamo la derivata:
\[
f'(x)=x-2.
\]
Scegliamo il punto di tangenza \(P\) con \(x_0=4\). Allora
\[
f(4)=\frac{1}{2}(4-2)^2+3=\frac{1}{2}\cdot4+3=2+3=5,
\]
e
\[
f'(4)=4-2=2.
\]
La retta tangente in \(P(4,5)\) ha quindi equazione
\[
y-5=2(x-4),
\]
ossia
\[
y=2x-3.
\]
\begin{center}
\begin{tikzpicture}[scale=0.8]
  % Assi cartesiani
  \draw[->] (-1,0) -- (7,0) node[right] {\(x\)};
  \draw[->] (0,-1) -- (0,8) node[above] {\(y\)};
  
  % Funzione: f(x)=0.5*(x-2)^2+3 in rosso
  \draw[red, thick, domain=-1:5.5, samples=100, smooth] plot (\x, {0.5*(\x-2)^2+3});
  
  % Derivata: f'(x)=x-2 in blu
  \draw[blue, thick, domain=0:7, samples=100, smooth] plot (\x, {\x-2});
  
  % Retta tangente: y=2x-3 in verde (tangente al punto P(4,5))
  \draw[green, thick, domain=0:5.5, samples=100, smooth] plot (\x, {2*\x-3});
  
  % Punto di tangenza P(4,5)
  \filldraw[black] (4,5) circle (2pt) node[above right] {\(P(4,5)\)};

\end{tikzpicture}
\end{center}

Nel disegno, la curva rossa rappresenta la funzione 
\[
f(x)=\frac{1}{2}(x-2)^2+3,
\]
la quale definisce una parabola. La linea blu mostra la derivata di \(f(x)\), ovvero 
\[
f'(x)=x-2,
\]
che indica il tasso di variazione della funzione in ogni punto ed è utile per determinare la pendenza locale. Infine, la retta verde rappresenta la tangente alla curva nel punto \(P(4,5)\); essa è la retta che, passando per \(P\), ha la stessa pendenza della funzione in quel punto.
\end{esempio}

\subsubsection*{Rette Reciproche ad una Parabola}

Due rette si dicono \emph{reciproche} se sono perpendicolari, ovvero se il prodotto dei loro coefficienti angolari è \(-1\). Nel contesto di una parabola, ad ogni punto della curva è associata una retta tangente. La retta reciproca, detta anche \emph{normale}, è la retta perpendicolare alla tangente in quel punto.

\medskip
Sia data una parabola definita da una funzione \(f(x)\). La retta tangente alla parabola in un punto \(P(x_0, f(x_0))\) ha coefficiente angolare
\[
m_t = f'(x_0).
\]
La retta normale (o retta reciproca) in \(P\) ha invece coefficiente angolare
\[
m_n = -\frac{1}{f'(x_0)},
\]
poiché \(m_t \cdot m_n = -1\). Questa proprietà permette di verificare che due rette siano reciproche: basta controllare che il loro prodotto sia \(-1\).

\medskip
\textbf{Esempio:}  
Consideriamo la parabola
\[
y=\frac{1}{2}(x-2)^2+3.
\]
Il suo derivato è
\[
f'(x)=x-2.
\]
Scegliamo il punto \(P(4, f(4))\). Calcoliamo:
\[
f(4)=\frac{1}{2}(4-2)^2+3=\frac{1}{2}\cdot4+3=2+3=5,
\]
e
\[
m_t=f'(4)=4-2=2.
\]
Il coefficiente angolare della retta normale in \(P\) è quindi
\[
m_n=-\frac{1}{2}.
\]

Consideriamo il punto \(P(4,5)\) e il coefficiente angolare \(m_n=-\frac{1}{2}\). Utilizzando la formula punto-pendenza, abbiamo
\[
y-5=-\frac{1}{2}(x-4).
\]
Risolvendo:
\[
y-5=-\frac{1}{2}x+2 \quad\Longrightarrow\quad y=-\frac{1}{2}x+7.
\]


\medskip

\begin{center}
\begin{tikzpicture}[scale=0.8]
  % Disegno degli assi
  \draw[->] (-1,0) -- (7,0) node[right] {\(x\)};
  \draw[->] (0,-1) -- (0,8) node[above] {\(y\)};
  
  % Disegno della parabola y = 0.5*(x-2)^2 + 3
  \draw[red, thick, domain=-1:5.5, samples=100, smooth] plot (\x, {0.5*(\x-2)^2+3});
  
  % Punto P(4,5)
  \filldraw[black] (4,5) circle (2pt) node[right] {\(P(4,5)\)};
  
  % Tangente in P con coefficiente m_t = 2
  % Equazione della tangente: y-5 = 2(x-4)
  \draw[blue, thick, domain=2:6, samples=100, smooth] 
    plot (\x, {2*(\x-4)+5}) node[right] {};
  
  % Normale in P con coefficiente m_n = -1/2
  % Equazione della normale: y-5 = -0.5(x-4)
  \draw[green, thick, domain=-1:6, samples=100, smooth] 
    plot (\x, {-0.5*(\x-4)+5}) node[right] {};

\end{tikzpicture}
\end{center}

\noindent
Nel disegno, il colore rosso indica la parabola definita da 
\[
y=0.5(x-2)^2+3,
\]
il colore blu rappresenta la retta tangente alla parabola nel punto \(P(4,5)\) (con pendenza \(m_t=2\)), mentre il colore verde indica la retta normale (o retta reciproca) a quella parabola in \(P(4,5)\) (con pendenza \(m_n=-\frac{1}{2}\)).


\subsec{Dimostrazione dei Criteri di Similitudine [2, 3]} %con dimostrazione!!
I triangoli simili sono figure geometriche che, pur potendo avere dimensioni diverse, presentano la stessa forma. Ciò significa che essi hanno gli angoli corrispondenti congruenti e le lunghezze dei lati corrispondenti sono proporzionali.

\begin{definition}[Triangoli Simili]
Siano \(\triangle ABC\) e \(\triangle A'B'C'\) due triangoli. Essi sono detti \emph{simili} (si scrive \(\triangle ABC \sim \triangle A'B'C'\)) se e solo se:
\[
\angle A = \angle A',\quad \angle B = \angle B',\quad \angle C = \angle C',
\]
e se esiste una costante \(k>0\) tale che:
\[
\frac{AB}{A'B'} = \frac{BC}{B'C'} = \frac{CA}{C'A'} = k.
\]
\end{definition}

Vediamo un esempio di due triangoli simili, notiamo che hanno dimensioni diverse e che occupano regioni dello spazio diverse, nonostante questo sono comunque triangoli simili.

\begin{center}
\begin{tikzpicture}[scale=0.8]


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

Ora vogliamo trovare e \textit{dimostrare} dei criteri che ci permettono di concludere che dei triangoli siano simili. Significa quindi che faremo delle assunzioni su coppie di triangoli e vorremo dimostrare che partendo da solo quelle assunzioni i triangoli sono simili.

Questo argomento, coinvolgendo dimostrazioni formali, è più complesso di quelli che abbiamo visto fin'ora e coinvolge parti di trigonometria. È quindi consigliabile per lo studente rivedere questo argomento dopo aver visto la sezione di trigonometria.

\subsubsection*{Criterio Lato-Lato-Lato}

\begin{theorem}[Criterio LLL di Similitudine]
Siano \(\triangle ABC\) e \(\triangle A'B'C'\) due triangoli. Se esiste una costante \(k>0\) tale che
\[
\frac{AB}{A'B'}=\frac{BC}{B'C'}=\frac{CA}{C'A'}=k,
\]
allora i triangoli sono simili, cioè \(\triangle ABC \sim \triangle A'B'C'\).
\end{theorem}

\begin{proof}[dimostrazione]
Dimostriamo che, se i lati corrispondenti sono in proporzione, allora anche gli angoli corrispondenti sono congruenti.

Sia
\[
\frac{AB}{A'B'}=\frac{BC}{B'C'}=\frac{CA}{C'A'}=k.
\]
Consideriamo l'angolo \(A\) in \(\triangle ABC\) e l'angolo \(A'\) in \(\triangle A'B'C'\). Applicando la legge dei coseni, abbiamo:
\[
\cos A = \frac{AB^2 + AC^2 - BC^2}{2\,AB\,AC},
\]
\[
\cos A' = \frac{(A'B')^2 + (A'C')^2 - (B'C')^2}{2\,A'B'\,A'C'}.
\]
Poiché i lati di \(\triangle A'B'C'\) sono tali che \(A'B'=\frac{1}{k}AB\), \(A'C'=\frac{1}{k}AC\) e \(B'C'=\frac{1}{k}BC\), sostituendo nelle formule otteniamo:
\[
\cos A' = \frac{\frac{1}{k^2}\left(AB^2+AC^2-BC^2\right)}{2\,\frac{1}{k^2}(AB\,AC)}
=\frac{AB^2+AC^2-BC^2}{2\,AB\,AC}=\cos A.
\]
Essendo la funzione coseno invertibile (su \([0,\pi]\)), si deduce che \(A = A'\). Applicando lo stesso ragionamento agli altri angoli, si ottiene che
\[
\angle A = \angle A',\quad \angle B = \angle B',\quad \angle C = \angle C'.
\]
Pertanto, per definizione, i triangoli sono simili, cioè \(\triangle ABC \sim \triangle A'B'C'\).
\end{proof}

\subsubsection*{Criterio LAL}

\begin{theorem}[Criterio LAL]
Siano \(\triangle ABC\) e \(\triangle A'B'C'\) due triangoli. Se i lati corrispondenti che formano l'angolo compreso sono in proporzione, cioè
\[
\frac{AB}{A'B'}=\frac{AC}{A'C'}=k \quad (k>0),
\]
e se l'angolo compreso \(\angle A\) è congruente all'angolo compreso \(\angle A'\), allora
\[
\triangle ABC \sim \triangle A'B'C'.
\]
\end{theorem}

\begin{proof}[dimostrazione]
Consideriamo la legge dei coseni nel triangolo \(ABC\):
\[
BC^2 = AB^2 + AC^2 - 2\,AB\,AC\cos\angle A.
\]
Analogamente, per il triangolo \(A'B'C'\) si ha:
\[
(B'C')^2 = (A'B')^2 + (A'C')^2 - 2\,A'B'\,A'C'\cos\angle A'.
\]
Dato che \(\angle A=\angle A'\) e che \(A'B'=\frac{1}{k}AB\) e \(A'C'=\frac{1}{k}AC\), sostituendo nella seconda equazione troviamo:
\[
(B'C')^2 = \frac{1}{k^2}\Bigl(AB^2+AC^2-2\,AB\,AC\cos\angle A\Bigr)
=\frac{1}{k^2}\,BC^2.
\]
Da cui
\[
\frac{BC}{B'C'}=k.
\]
Quindi, i tre lati sono in proporzione e, per il criterio LLL di similitudine, i triangoli sono simili.
\end{proof}

\subsubsection*{Criterio AA}

\begin{theorem}[Criterio AA]
Siano \(\triangle ABC\) e \(\triangle A'B'C'\) tali che
\[
\angle A=\angle A'\quad\text{e}\quad\angle B=\angle B'.
\]
Allora, poiché la somma degli angoli interni di ciascun triangolo è \(\pi\), si ha
\[
\angle C=\pi-(\angle A+\angle B)=\pi-(\angle A'+\angle B')=\angle C'.
\]
Quindi, i triangoli sono simili.
\end{theorem}

\begin{proof}[dimostrazione (AA)]
Dato che \(\angle A+\angle B+\angle C=\pi\) e \(\angle A'+\angle B'+\angle C'=\pi\), l'uguaglianza di \(\angle A\) con \(\angle A'\) e di \(\angle B\) con \(\angle B'\) implica immediatamente che
\[
\angle C=\pi-(\angle A+\angle B)=\pi-(\angle A'+\angle B')=\angle C'.
\]
Pertanto, per definizione, i triangoli sono simili.
\end{proof}

\begin{theorem}[Criterio LLL]
Siano \(\triangle ABC\) e \(\triangle A'B'C'\) tali che
\[
\frac{AB}{A'B'}=\frac{BC}{B'C'}=\frac{CA}{C'A'}=k,\quad k>0.
\]
Allora i triangoli sono simili.
\end{theorem}

\begin{proof}[dimostrazione (SSS)]
Consideriamo la legge dei coseni nel triangolo \(ABC\):
\[
\cos A=\frac{AB^2+AC^2-BC^2}{2\,AB\,AC}.
\]
Nel triangolo \(A'B'C'\) i lati sono proporzionali a quelli di \(ABC\); in particolare, \(A'B'=\frac{1}{k}AB\), \(A'C'=\frac{1}{k}AC\) e \(B'C'=\frac{1}{k}BC\). Quindi,
\[
\cos A'=\frac{(A'B')^2+(A'C')^2-(B'C')^2}{2\,A'B'\,A'C'} 
=\frac{\frac{1}{k^2}\left(AB^2+AC^2-BC^2\right)}{2\,\frac{1}{k^2}(AB\,AC)}
=\frac{AB^2+AC^2-BC^2}{2\,AB\,AC}=\cos A.
\]
Essendo il coseno iniettivo su \([0,\pi]\), si deduce che \(\angle A=\angle A'\). Applicando lo stesso ragionamento agli altri angoli, risulta che tutti gli angoli corrispondenti sono congruenti. Pertanto, per definizione, i triangoli sono simili.
\end{proof}
\subsec{Punti Notevoli del Triangolo [2]}
In un triangolo esistono tre segmenti notevoli che assumono un ruolo fondamentale: la \textbf{mediana}, la \textbf{bisettrice} e l’\textbf{altezza}. Ognuno di questi elementi presenta caratteristiche geometriche peculiari e contribuisce allo studio delle proprietà del triangolo. In alcune circostanze speciali, come nel triangolo equilatero, tali segmenti possono persino coincidere. Vedremo anche come, dal punto di vista delle coordinate, il \textbf{baricentro} (o \textit{centro di gravità}) del triangolo si ottenga come intersezione delle mediane e possa essere calcolato facilmente. In questa sezione vediamo le seguenti nozioni in modo informale mentre nella seguente vedremo i relativi teoremi e dimostrazioni formali necessarie per completare il programma.

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

\subsec{Teoremi dei Punti Notevoli [2]}

Ognuno dei quattro principali \emph{punti notevoli} (incentro, baricentro, circocentro, ortocentro) è definito come il punto di concorrenza di un particolare insieme di linee “speciali” (bisettrici, mediane, assi perpendicolari, altezze). Qui forniamo quattro enunciati, uno per ciascuna famiglia di linee, accompagnati dalle dimostrazioni fondamentali.

\medskip

\begin{theorem}[Concorrenza delle Bisettrici — L’Incentro]
In un triangolo, le tre bisettrici degli angoli interni si incontrano in un unico punto, detto \emph{incentro}, che è il centro della circonferenza \emph{inscritta}.
\end{theorem}

\begin{proof}[dimostrazione]
Le bisettrici sono i segmenti che dividono ciascun angolo in due parti uguali, partendo dal vertice e giungendo al lato opposto. Si considerino le bisettrici degli angoli \(\widehat{A}\) e \(\widehat{B}\), che si incontrano in un punto \(I\). Occorre mostrare che anche la bisettrice dell’angolo \(\widehat{C}\) passa per \(I\). 

\textbf{Obiettivo:} Mostrare che in un triangolo \(ABC\), le tre \emph{bisettrici} degli angoli interni concorrono in un unico punto \(I\), detto \emph{incentro}, e che \(I\) è il centro della circonferenza tangente a tutti i lati (\emph{incirconferenza}).

\begin{enumerate}
\item \textbf{Definizione e Prime Due Bisettrici}

  \begin{enumerate}
  \item \emph{Bisettrice dall’angolo \(A\).}  
  Nel triangolo \(ABC\), la bisettrice dell’angolo \(\widehat{A}\) è il segmento che, partendo da \(A\), divide \(\angle A\) in due angoli uguali, fino a incontrare il lato \(\overline{BC}\) in un punto \(D\).

  \item \emph{Bisettrice dall’angolo \(B\).}  
  Analogamente, la bisettrice di \(\widehat{B}\) è il segmento da \(B\) che separa \(\angle B\) in due parti congruenti, fino a un punto \(E\) su \(\overline{AC}\).

  \item \emph{Intersezione delle prime due bisettrici.}  
  Le bisettrici da \(A\) e \(B\) definiscono un punto \(I\). Occorre provare che anche la bisettrice di \(\widehat{C}\) passa per \(I\).
  \end{enumerate}

\item \textbf{Equidistanza dell’Incentro dai Lati}

  \begin{enumerate}
  \item \emph{Definizione di circonferenza tangente ai lati.}  
  Se un punto \(I\) è equidistante dai lati \(\overline{AB}\), \(\overline{BC}\), \(\overline{CA}\), esiste una circonferenza con centro \(I\) che tocca ciascun lato in un solo punto (tangente). Questa è l’\emph{incirconferenza} del triangolo.

  \item \emph{Bisettrici e tangenti.}  
  Dal punto \(I\), tracciamo i segmenti perpendicolari ai lati. Se \(I\) si trova sull’angolo \(\widehat{A}\) bisecato, allora i segmenti \(\overline{IA}\) risulteranno equidistanti dai lati adiacenti a \(A\). Similmente, la bisettrice di \(\widehat{B}\) rende \(\overline{IB}\) equidistante dai lati attigui a \(B\).

  \item \emph{Contraddizione se la bisettrice di \(\widehat{C}\) non passasse per \(I\).}  
  Se il terzo angolo \(\widehat{C}\) non avesse la sua bisettrice concorrente in \(I\), non sarebbe possibile mantenere la condizione di \emph{unica} circonferenza tangente a tutti e tre i lati, poiché i segmenti perpendicolari dai lati a \(I\) non sarebbero tutti uguali.
  \end{enumerate}

\item \textbf{Concorrenza della Bisettrice di \(\widehat{C}\)}

  \begin{enumerate}
  \item \emph{Geometria elementare.}  
  Si osserva che la bisettrice di \(\widehat{C}\) “eredita” la stessa proprietà di equidistanza: se \(I\) è già a ugual distanza da due lati, e \(I\) rimane interno al triangolo, l’unico modo per avere una tangente comune anche al terzo lato è che la bisettrice di \(\widehat{C}\) debba passare per \(I\).

  \item \emph{Conclusione:}  
  Tutte e tre le bisettrici si incontrano in \(I\). Questo punto \(I\) è l’\emph{incentro}, il centro dell’incirconferenza. 
  \end{enumerate}

\item \textbf{Formula dell’Incentro (coefficienti angolari o lato-lato)}

  In coordinate, se si desidera la posizione esplicita di \(I\), si possono usare le relazioni di \emph{proporzionalità} sulle bisettrici:
  \[
    \frac{BD}{DC} = \frac{AB}{AC}, 
    \quad
    \frac{AE}{EC} = \frac{BA}{BC},
    \quad
    \dots
  \]
  Risolvendo per i punti d’intersezione e trovando l’incrocio di due bisettrici, si ottiene la coppia \((x_I,y_I)\).  
  Un metodo alternativo si basa sulla \emph{formula a pesi}, secondo cui:
  \[
    I 
    = \frac{a\,A + b\,B + c\,C}{\,a+b+c\,},
  \]
  dove \(a,b,c\) sono le lunghezze opposte ai vertici \(A,B,C\). In altre parole, l’incentro è una \emph{media pesata} dei vertici, con pesi proporzionali ai lati opposti.
\end{enumerate}
\end{proof}

\begin{center}
\begin{tikzpicture}[scale=1.0, line cap=round, line join=round]

\coordinate (A) at (0,0);
\coordinate (B) at (5,0);
\coordinate (C) at (2,3);

\draw[thick] (A) -- (B) -- (C) -- cycle;

\pgfmathsetmacro{\xBD}{(15*sqrt(2)) / (sqrt(13)+5)}
\coordinate (D) at ($(B) ! {\xBD/(3*sqrt(2))} ! (C)$);

\pgfmathsetmacro{\yAE}{(5*sqrt(13)) / (3*sqrt(2)+5)}
\coordinate (E) at ($(A) ! {\yAE/sqrt(13)} ! (C)$);

\pgfmathsetmacro{\zAF}{(5*sqrt(13)) / ((3*sqrt(2)) + sqrt(13))}
\coordinate (F) at (\zAF, 0);

\draw[dashed] (A)--(D);
\draw[dashed] (B)--(E);
\draw[dashed] (C)--(F);

\path[name path=AD] (A) -- (D);
\path[name path=BE] (B) -- (E);
\path[name path=CF] (C) -- (F);

\path[name intersections={of=AD and BE,by=I}];

\fill (I) circle(1.2pt) node[above left] {I};

\draw[thick] (I) circle(1.145);

\node[below left]  at (A) {$A$};
\node[below right] at (B) {$B$};
\node[above]       at (C) {$C$};

\end{tikzpicture}
\end{center}

\begin{esempio}
Dato il triangolo \(ABC\) con vertici 
\[
A(0,0),\quad B(4,0),\quad C(2,3)
\]
nel piano cartesiano, determinare l’equazione della \emph{circonferenza incisa} (incirconferenza), ossia la circonferenza tangente ai lati \(\overline{AB}\), \(\overline{BC}\) e \(\overline{CA}\).

\begin{enumerate}
\item \textbf{Calcolo delle lunghezze dei lati.}

\[
AB = \sqrt{(4-0)^2 + (0-0)^2} = 4,
\quad
BC = \sqrt{(2-4)^2 + (3-0)^2} = \sqrt{4 + 9} = \sqrt{13},
\]
\[
CA = \sqrt{(2-0)^2 + (3-0)^2} = \sqrt{4 + 9} = \sqrt{13}.
\]

\item \textbf{Formula dell’incentro (coordinate).}

L’incentro \(I\) si può esprimere come 
\[
I = \frac{a\,A + b\,B + c\,C}{\,a + b + c\,},
\]
dove \(a=BC\), \(b=CA\), \(c=AB\). Nel nostro caso:
\[
a = \sqrt{13}, 
\quad 
b = \sqrt{13}, 
\quad 
c = 4.
\]
Calcoliamo:
\[
I 
= \frac{\sqrt{13}\,(0,0) + \sqrt{13}\,(4,0) + 4\,(2,3)}
  {\sqrt{13} + \sqrt{13} + 4}
= \frac{ \bigl(\,4\sqrt{13},\,0\bigr) + \bigl(8,12\bigr) }
  { 2\sqrt{13} + 4 }.
\]
Sommando i vettori:
\[
\bigl(4\sqrt{13} + 8,\; 0 + 12\bigr),
\]
e dividendo per \(2\sqrt{13} + 4\), otteniamo
\[
I 
= \Bigl(\,
  \frac{4\sqrt{13} + 8}{\,2\sqrt{13} + 4\,},\,
  \frac{12}{\,2\sqrt{13} + 4\,}
\Bigr).
\]

\item \textbf{Calcolo del raggio (inradius).}

Il raggio dell’incirconferenza è \(\displaystyle r = \frac{2\,\Delta}{P}\), dove \(\Delta\) è l’area del triangolo e \(P\) è il perimetro.  
\begin{enumerate}
\item \emph{Perimetro:} 
\[
P = a + b + c = \sqrt{13} + \sqrt{13} + 4 = 2\sqrt{13} + 4.
\]
\item \emph{Area:}  
Usiamo la formula del determinante (o base \(\times\) altezza):
\[
\Delta 
= \frac12\,\Bigl|\,
x_A(y_B - y_C) + x_B(y_C - y_A) + x_C(y_A - y_B)
\Bigr|.
\]
Sostituendo \(A(0,0)\), \(B(4,0)\), \(C(2,3)\):
\[
\Delta 
= \frac12 \bigl|\,
0 \cdot (0-3) + 4\cdot(3-0) + 2\cdot(0-0)
\bigr|
= \frac12 \times |\,0 + 12 + 0\,|
= 6.
\]
\item \emph{Raggio inraggio:}  
\[
r 
= \frac{2\,\Delta}{P}
= \frac{2 \times 6}{2\sqrt{13} + 4}
= \frac{12}{\,2\sqrt{13} + 4\,}.
\]
\end{enumerate}

\item \textbf{Equazione dell’incirconferenza.}

Se il centro è \(I(x_I,y_I)\) e il raggio è \(r\), l’equazione standard è
\[
(x - x_I)^2 + (y - y_I)^2 = r^2.
\]
Abbiamo
\[
x_I = \frac{4\sqrt{13} + 8}{\,2\sqrt{13} + 4\,},
\quad
y_I = \frac{12}{\,2\sqrt{13} + 4\,},
\quad
r = \frac{12}{\,2\sqrt{13} + 4\,}.
\]
Per semplicità, si può lasciare in forma frazionaria. L’equazione finale risulta
\[
\boxed{
\Bigl(x - x_I\Bigr)^2 + \Bigl(y - y_I\Bigr)^2 = 
\Bigl(\frac{12}{\,2\sqrt{13} + 4\,}\Bigr)^2
}.
\]

\end{enumerate}

\textit{Conclusione:} L’incentro \(\bigl(x_I,y_I\bigr)\) si ottiene come media pesata dei vertici, e l’inraggio \(r\) come \(\tfrac{2\,\Delta}{P}\). Da questi si ricava l’equazione dell’incirconferenza. 
\end{esempio}

\begin{theorem}[Concorrenza delle Mediane — Il Baricentro]
In un triangolo, le tre mediane (segmenti che congiungono un vertice al punto medio del lato opposto) si incontrano in un unico punto, detto \emph{baricentro}.
\end{theorem}

\begin{proof}[dimostrazione]
Siano \(M_a\), \(M_b\), \(M_c\) i punti medi dei lati opposti ai vertici \(A\), \(B\), \(C\). Consideriamo le mediane \(\overline{AM_a}\) e \(\overline{BM_b}\). Queste due linee definiscono un punto \(G\). Si mostra che anche la terza mediana \(\overline{CM_c}\) passa per \(G\).  

\noindent
\textbf{Obiettivo:} Mostrare che in un triangolo \(ABC\) con coordinate 
\[
A(x_A,y_A),\quad B(x_B,y_B),\quad C(x_C,y_C),
\]
le tre \emph{mediane} (segmenti che congiungono ciascun vertice con il punto medio del lato opposto) si incontrano in un unico punto, detto \emph{baricentro}. Infine, fornire la formula esplicita per il calcolo di tale punto notevole.

\begin{enumerate}
\item \textbf{Definizione delle Mediane}

  \begin{enumerate}
  \item \emph{Mediana da \(A\).}  
  Sia \(M_{BC}\) il punto medio del lato \(\overline{BC}\). In coordinate:
  \[
    M_{BC}\Bigl(\,\tfrac{x_B + x_C}{2},\;\tfrac{y_B + y_C}{2}\Bigr).
  \]
  La mediana da \(A\) è la retta che unisce \(A(x_A,y_A)\) e \(M_{BC}\). 

  \item \emph{Mediana da \(B\).}  
  Sia \(M_{AC}\) il punto medio di \(\overline{AC}\):
  \[
    M_{AC}\Bigl(\,\tfrac{x_A + x_C}{2},\;\tfrac{y_A + y_C}{2}\Bigr).
  \]
  La mediana da \(B\) è la retta che unisce \(B(x_B,y_B)\) e \(M_{AC}\).

  \item \emph{Mediana da \(C\).}  
  Sia \(M_{AB}\) il punto medio di \(\overline{AB}\):
  \[
    M_{AB}\Bigl(\,\tfrac{x_A + x_B}{2},\;\tfrac{y_A + y_B}{2}\Bigr).
  \]
  La mediana da \(C\) è la retta che unisce \(C(x_C,y_C)\) e \(M_{AB}\).
  \end{enumerate}

\item \textbf{Intersezione delle Prime Due Mediane}

  Consideriamo le mediane da \(A\) e da \(B\). Otteniamo un sistema di due equazioni lineari: 
  \[
    \begin{cases}
      \text{retta } A\!-\!M_{BC},\\[4pt]
      \text{retta } B\!-\!M_{AC}.
    \end{cases}
  \]
  Ciascuna è descritta in forma implicita o esplicita, e la loro intersezione fornisce un unico punto \((x_G,y_G)\). Questo punto \(G\) è l’intersezione di due mediane.

\item \textbf{Verifica con la Terza Mediana}

  Per mostrare che la mediana da \(C\) passa anch’essa per \((x_G,y_G)\), si controlla che \((x_G,y_G)\) soddisfa l’equazione della retta \(\overline{C M_{AB}}\). In modo analitico, si sostituiscono le coordinate \((x_G,y_G)\) nella terza equazione; se la coppia è soluzione, significa che \(\overline{C M_{AB}}\) include \((x_G,y_G)\), provando la \emph{concorrenza} di tutte e tre.

\item \textbf{Formula del Baricentro}

  Se risolviamo direttamente le coordinate di \((x_G,y_G)\) oppure usiamo un argomento vettoriale (o di \emph{geometria analitica}), scopriamo che il \emph{baricentro} \(G\) ha coordinate
  \[
    \boxed{
    G\Bigl(\,\tfrac{x_A + x_B + x_C}{3},\;\tfrac{y_A + y_B + y_C}{3}\Bigr).
    }
  \]
  Questa formula mostra che il baricentro è la \emph{media aritmetica} delle coordinate dei tre vertici.
\end{enumerate}
\end{proof}

\begin{center}
\begin{tikzpicture}[scale=1.0, line cap=round, line join=round]

  % Triangolo ABC
  \coordinate (A) at (0,0);
  \coordinate (B) at (5,0);
  \coordinate (C) at (2,3);
  \draw[thick] (A) -- (B) -- (C) -- cycle;

  % Mediane come esempio
  \coordinate (M_BC) at ($(B)!0.5!(C)$);
  \coordinate (M_AC) at ($(A)!0.5!(C)$);
  \coordinate (M_AB) at ($(A)!0.5!(B)$);

  \draw[dashed] (A) -- (M_BC);
  \draw[dashed] (B) -- (M_AC);
  \draw[dashed] (C) -- (M_AB);

  \node[below left]  at (A) {$A$};
  \node[below right] at (B) {$B$};
  \node[above]       at (C) {$C$};
\end{tikzpicture}
\end{center}

\begin{theorem}[Concorrenza degli Assi Perpendicolari — Il Circocentro]
In un triangolo, i tre assi perpendicolari dei lati si incontrano in un unico punto, detto \emph{circocentro}, che è il centro della \emph{circonferenza circoscritta}.
\end{theorem}

\begin{proof}[dimostrazione]
Un asse perpendicolare di un lato è la retta perpendicolare al lato che passa per il suo punto medio. Consideriamo gli assi perpendicolari dei lati \(\overline{AB}\) e \(\overline{BC}\), che si intersecano in un punto \(O\). Si dimostra che l’asse del terzo lato \(\overline{CA}\) passa per \(O\).  

Il motivo è che \(O\) risulta equidistante dai vertici \(A\), \(B\), \(C\). Infatti, se \(O\) è sull’asse di \(\overline{AB}\), allora \(OA=OB\). Se è sull’asse di \(\overline{BC}\), allora \(OB=OC\). Dunque \(OA=OB=OC\). Per il terzo lato, la stessa equidistanza costringe il suo asse a concorrere in \(O\). Questo \(O\) è il \emph{circocentro}, centro della circonferenza passante per \(A, B, C\).  
\end{proof}

\begin{center}
\begin{tikzpicture}[scale=1.0, line cap=round, line join=round]

% Vertici del triangolo
\coordinate (A) at (0,0);
\coordinate (B) at (5,0);
\coordinate (C) at (2,3);

% Disegno del triangolo ABC
\draw[thick] (A) -- (B) -- (C) -- cycle;

% Punti medi dei lati
\coordinate (M_AB) at (2.5,0);   % midpoint di AB
\coordinate (M_BC) at (3.5,1.5); % midpoint di BC
\coordinate (M_AC) at (1,1.5);   % midpoint di AC

% 1) Asse perpendicolare di AB
% AB e' orizzontale => slope(AB)=0 => asse = x costante
\draw[dashed] (2.5,-1) -- (2.5,4);

% 2) Asse perpendicolare di BC
% slope(BC)= -1 => slope perpendicolare= +1 => eq: y = x + k
% B(5,0), C(2,3) => M_BC(3.5,1.5) => 1.5=3.5 +k => k= -2 => eq: y=x-2
\draw[dashed] plot[domain=-1:6] ({\x},{\x-2});

% 3) Asse perpendicolare di AC
% slope(AC)= (3-0)/(2-0)=3/2 => slope perpendicolare= -2/3 => eq: y= -2/3 x + k
% Passa per M_AC(1,1.5) => 1.5= -2/3(1)+k => k=1.5+2/3= 13/6
% eq => y= -2/3 x + 13/6
\draw[dashed] plot[domain=-1:6] ({\x},{-2/3*\x + 13/6});

% Intersezione: i primi due assi => x=2.5 e y=x-2 => x=2.5 => y=0.5 => O=(2.5,0.5)
% Verifichiamo che O stia anche sul terzo asse => y= -2/3(2.5)+13/6 => 0.5 => OK
\coordinate (O) at (2.5,0.5);

% Disegno del circocentro e della circonferenza circoscritta
% Raggio= distanza OA
\pgfmathsetmacro{\r}{sqrt((2.5-0)^2 + (0.5-0)^2)}

\fill (O) circle(1.5pt) node[above left] {Circocentro};
\draw[thick] (O) circle(\r);

% Etichette dei vertici
\node[below left]  at (A) {$A$};
\node[below right] at (B) {$B$};
\node[above]       at (C) {$C$};

\end{tikzpicture}
\end{center}

\begin{esempio}
Dati i punti \(A(0,0)\), \(B(5,0)\), \(C(2,3)\) sul piano cartesiano, determinare l’equazione della circonferenza che circoscrive il triangolo \(ABC\).

\begin{enumerate}
\item \textbf{Calcolo del circocentro.}  
  \begin{enumerate}
  \item \emph{Asse perpendicolare del lato \(\overline{AB}\).}  
  I punti \(A(0,0)\) e \(B(5,0)\) danno un segmento orizzontale di lunghezza \(5\).  
  Il punto medio è \(\bigl(\tfrac{0+5}{2},\,\tfrac{0+0}{2}\bigr)=(2.5,0)\).  
  Poiché \(\overline{AB}\) è orizzontale, l’asse è la retta verticale \(x=2.5\).

  \item \emph{Asse perpendicolare del lato \(\overline{BC}\).}  
  I punti \(B(5,0)\) e \(C(2,3)\) definiscono un segmento di pendenza \(-1\).  
  Il punto medio è \(\bigl(\tfrac{5+2}{2},\,\tfrac{0+3}{2}\bigr)=(3.5,1.5)\).  
  Un asse perpendicolare a \(\overline{BC}\) avrà pendenza \(+1\). L’equazione della retta passante per \((3.5,1.5)\) e pendenza \(+1\) è
  \[
    y - 1.5 \;=\; 1\,(x - 3.5)
    \quad\Longrightarrow\quad
    y \;=\; x - 2.
  \]

  \item \emph{Intersezione degli assi.}  
  Il sistema
  \[
    \begin{cases}
      x = 2.5, \\
      y = x - 2
    \end{cases}
  \]
  fornisce \(x=2.5\) e \(y=0.5\). Quindi il \emph{circocentro} è \(O(2.5,\,0.5)\).
  \end{enumerate}

\item \textbf{Calcolo del raggio.}  
Scegliendo uno qualsiasi dei vertici, ad esempio \(A(0,0)\), il raggio \(R\) è la distanza \(\overline{OA}\). Con \(O(2.5,0.5)\) e \(A(0,0)\):
\[
R \;=\;\sqrt{(2.5 - 0)^2 + (0.5 - 0)^2}
\;=\;\sqrt{6.25 + 0.25}
\;=\;\sqrt{6.5}.
\]

\item \textbf{Equazione della circonferenza.}  
Se il centro è \((h,k)\) e il raggio è \(R\), l’equazione standard della circonferenza è
\[
(x - h)^2 + (y - k)^2 \;=\; R^2.
\]
Nel nostro caso, \(h=2.5\), \(k=0.5\) e \(R^2=6.5\). Pertanto:
\[
\boxed{(x - 2.5)^2 + (y - 0.5)^2 = 6.5}.
\]
\end{enumerate}
\end{esempio}



\begin{theorem}[Concorrenza delle Altezze — L’Ortocentro]
In un triangolo, le tre altezze (segmenti condotti da un vertice e perpendicolari al lato opposto) si incontrano in un unico punto, detto \emph{ortocentro}.
\end{theorem}

\begin{proof}[dimostrazione]
Siano \(\overline{AD_a}\), \(\overline{BE_b}\), \(\overline{CF_c}\) le tre altezze, con \(D_a\), \(E_b\), \(F_c\) punti sui lati corrispondenti. Basta dimostrare che \(\overline{AD_a}\) e \(\overline{BE_b}\) definiscono un punto \(H\), e che la terza altezza \(\overline{CF_c}\) passa per \(H\).  

\textbf{Obiettivo:} Mostrare che in un triangolo \(ABC\) con coordinate 
\[
A(x_A,\,y_A), 
\quad 
B(x_B,\,y_B), 
\quad 
C(x_C,\,y_C),
\]
le tre altezze si incontrano in un unico punto (ortocentro) risolvendo i sistemi lineari delle loro equazioni.

\begin{enumerate}
\item \textbf{Equazioni delle Altezze.}

  \begin{enumerate}
  \item \emph{Altezza da \(A\).}  
  Il lato \(\overline{BC}\) ha pendenza 
  \[
    m_{BC} = \frac{y_C - y_B}{x_C - x_B}.
  \]
  L’altezza da \(A\) è perpendicolare a \(\overline{BC}\), dunque la sua pendenza è
  \[
    m_A = -\,\frac{1}{m_{BC}} 
    = \frac{x_B - x_C}{\,y_C - y_B\,}.
  \]
  La retta passante per \(A(x_A, y_A)\) con pendenza \(m_A\) ha equazione
  \[
    y - y_A 
    = m_A \,\bigl(x - x_A\bigr).
  \]

  \item \emph{Altezza da \(B\).}  
  Il lato \(\overline{AC}\) ha pendenza 
  \[
    m_{AC} = \frac{y_C - y_A}{x_C - x_A}.
  \]
  L’altezza da \(B\) è perpendicolare a \(\overline{AC}\), con pendenza
  \[
    m_B = -\,\frac{1}{m_{AC}} 
    = \frac{x_A - x_C}{\,y_C - y_A\,}.
  \]
  L’equazione per \(B(x_B,\,y_B)\) risulta
  \[
    y - y_B 
    = m_B \,\bigl(x - x_B\bigr).
  \]

  \item \emph{Altezza da \(C\).}  
  Il lato \(\overline{AB}\) ha pendenza 
  \[
    m_{AB} = \frac{y_B - y_A}{x_B - x_A}.
  \]
  L’altezza da \(C\) è perpendicolare a \(\overline{AB}\), quindi la sua pendenza è
  \[
    m_C = -\,\frac{1}{m_{AB}} 
    = \frac{x_A - x_B}{\,y_B - y_A\,}.
  \]
  La retta per \(C(x_C,\,y_C)\) con pendenza \(m_C\) ha equazione
  \[
    y - y_C 
    = m_C \,\bigl(x - x_C\bigr).
  \]
  \end{enumerate}

\item \textbf{Intersezione delle Prime Due Altezze.}

  Consideriamo le rette delle altezze da \(A\) e da \(B\). Otteniamo il sistema
  \[
    \begin{cases}
      y - y_A = m_A\,\bigl(x - x_A\bigr), \\
      y - y_B = m_B\,\bigl(x - x_B\bigr).
    \end{cases}
  \]
  Sviluppando e semplificando, si ricava un’unica soluzione \((x_H,\,y_H)\). Questo punto \(H\) è l’intersezione delle due altezze.

\item \textbf{Verifica con la Terza Altezza.}

  Per mostrare che anche l’altezza da \(C\) passa per \(H\), sostituiamo \((x_H,\,y_H)\) nell’equazione
  \[
    y - y_C 
    = m_C\,(x - x_C).
  \]
  Se la coppia \((x_H,\,y_H)\) soddisfa questa retta, allora \(H\) appartiene anche alla terza altezza, provando la \emph{concorrenza} di tutte e tre.
\end{enumerate}  
\end{proof}

\begin{center}
\begin{tikzpicture}[scale=1.0, line cap=round, line join=round]

  % Triangolo ABC
  \coordinate (A) at (0,0);
  \coordinate (B) at (5,0);
  \coordinate (C) at (2,3);
  \draw[thick] (A) -- (B) -- (C) -- cycle;

  % Piedi delle altezze:
  % H_A è la proiezione di A sul lato BC
  % H_B è la proiezione di B sul lato AC
  % H_C è la proiezione di C sul lato AB
  \coordinate (H_A) at ($(B)!(A)!(C)$);
  \coordinate (H_B) at ($(A)!(B)!(C)$);
  \coordinate (H_C) at ($(A)!(C)!(B)$);

  % Altezze (linee tratteggiate)
  \draw[dashed] (A) -- (H_A);
  \draw[dashed] (B) -- (H_B);
  \draw[dashed] (C) -- (H_C);

  % Etichette dei vertici
  \node[below left]  at (A) {$A$};
  \node[below right] at (B) {$B$};
  \node[above]       at (C) {$C$};

\end{tikzpicture}
\end{center}


\subsec{Equivalenze tra Figure Piane [2, 3]}
Le relazioni di equivalenza sono relazioni binarie che permettono di raggruppare gli elementi di un insieme in classi in cui gli elementi sono considerati "equivalenti" rispetto a una certa proprietà. In generale, una relazione \(R\) definita su un insieme \(A\) è una relazione di equivalenza se soddisfa i seguenti criteri:

\begin{itemize}
  \item \textbf{Riflessività:} Per ogni \(a\in A\), \(a\, R\, a\).
  \item \textbf{Simmetria:} Per ogni \(a,b\in A\), se \(a\, R\, b\) allora \(b\, R\, a\).
  \item \textbf{Transitività:} Per ogni \(a,b,c\in A\), se \(a\, R\, b\) e \(b\, R\, c\) allora \(a\, R\, c\).
\end{itemize}

Quando questi criteri sono soddisfatti, la relazione \(R\) divide l'insieme \(A\) in classi di equivalenza, dove ogni classe contiene tutti gli elementi che sono equivalenti tra loro secondo \(R\).

Esistono alcune relazioni di equivalenza con un significato geometrico particolarmente chiaro e utili in vari contesti. Vediamo ora tre di queste relazioni.

\begin{definition}[Congruenza]
Due figure piane \(F\) e \(G\) sono \emph{congruenti} se esiste una trasformazione rigida (rotazione, traslazione e/o riflessione) che trasforma \(F\) in \(G\). In altre parole, \(F\) e \(G\) hanno la stessa forma e le stesse dimensioni.
\end{definition}

\begin{center}
\begin{tikzpicture}[scale=1]
  % Disegno del primo rettangolo F
  \draw[thick] (0,0) rectangle (3,2);
  \node at (1.5,1) {\(F\)};
  
\draw[thick, rotate around={30:(5.5,1)}] (4,0) rectangle (7,2);
\node at (5.5,1) {\(G\)};
  
  % Freccia che indica la trasformazione rigida
  \draw[->, dashed, thick] (3.2,1) -- (3.8,1) node[midway, above] {};
\end{tikzpicture}
\end{center}



% Similitudine
\begin{definition}[Similitudine]
Due figure piane \(F\) e \(G\) sono \emph{simili} se esiste una trasformazione composta da una dilatazione e un movimento rigido che trasforma \(F\) in \(G\). Ciò implica che gli angoli corrispondenti sono congruenti e le lunghezze dei lati sono in proporzione.
\end{definition}

\begin{center}
\begin{tikzpicture}[scale=1]
  % Disegno di un piccolo rettangolo F
  \draw[thick] (0,0) rectangle (2,1);
  \node at (1,0.5) {\(F\)};
  
  % Disegno di un rettangolo G, ottenuto con una dilatazione (scala 1.5) di F
  \draw[thick] (3,0) rectangle (6,1.5);
  \node at (4.5,0.75) {\(G\)};
  
  % Freccia che indica la dilatazione
  \draw[->, dashed, thick] (2.2,0.5) -- (2.8,0.5) node[midway, above] {};
\end{tikzpicture}
\end{center}

% Equivalenza per Area
\begin{definition}[Equivalenza per Area]
Due figure piane \(F\) e \(G\) sono dette \emph{equivalenti per area} se hanno la stessa misura d'area, indipendentemente dalla loro forma o dalle loro dimensioni.
\end{definition}

\begin{center}
\begin{tikzpicture}[scale=0.8]
  % Disegno di un rettangolo F con area 8 (4 x 2)
  \draw[thick] (0,0) rectangle (4,2);
  \node at (2,1) {\(F\)};
  
  % Disegno di un triangolo G con base 4 e altezza 4 (area 1/2*4*4 = 8)
  \draw[thick] (6,0) -- (10,0) -- (8,4) -- cycle;
  \node at (8,1.5) {\(G\)};
  
  % Freccia che indica l'equivalenza d'area
  \draw[->, dashed, thick] (4.2,1) -- (5.8,1) node[midway, above] {};
\end{tikzpicture}
\end{center}

\begin{esempio}
Consideriamo i seguenti quadrilateri, definiti dai loro vertici:
\[
Q:\quad A(0,0),\; B(4,0),\; C(4,2),\; D(0,2),
\]
\[
Q':\quad A'(0,0),\; B'(4,0),\; C'(5,2),\; D'(1,2).
\]
Il quadrilatero \(Q\) è un rettangolo (con tutti gli angoli retti), mentre \(Q'\) è un parallelogramma inclinato (non tutti gli angoli sono \(90^\circ\)).

\vspace{0.5em}
\textbf{Non Congruenza e Non Similitudine:}  
Dimostriamo ora che i due quadrilateri non sono congruenti né simili.

Per \(Q\) abbiamo:
\[
AB=4,\quad BC=2,\quad CD=4,\quad DA=2.
\]
Quindi i rapporti tra i lati sono:
\[
AB:BC:CD:DA=4:2:4:2=2:1:2:1.
\]

Per \(Q'\) calcoliamo:
\[
A'B'=4,
\]
\[
B'C'=\sqrt{(5-4)^2+(2-0)^2}=\sqrt{1+4}=\sqrt{5},
\]
\[
C'D'=\sqrt{(5-1)^2+(2-2)^2}=\sqrt{16+0}=4,
\]
\[
D'A'=\sqrt{(1-0)^2+(2-0)^2}=\sqrt{1+4}=\sqrt{5}.
\]
Pertanto, i rapporti tra i lati di \(Q'\) sono:
\[
A'B':B'C':C'D':D'A'=4:\sqrt{5}:4:\sqrt{5}.
\]
Dividendo ogni termine per \(\sqrt{5}\), otteniamo:
\[
\frac{4}{\sqrt{5}}:1:\frac{4}{\sqrt{5}}:1,
\]
con \(\frac{4}{\sqrt{5}}\approx 1.78885\), che non corrisponde al rapporto \(2:1\) dei lati di \(Q\).

Pertanto, i lati corrispondenti dei due quadrilateri non sono proporzionali, e dunque \(Q\) e \(Q'\) non sono congruenti (poiché la congruenza richiede l'esatta corrispondenza delle lunghezze) né simili (dato che per la similitudine è necessaria una proporzionalità costante tra i lati corrispondenti).

\vspace{0.5em}
\textbf{Equivalenza per Area:}  
Calcolando l'area di \(Q\) otteniamo:
\[
\text{Area}(Q)=4\times2=8.
\]
Per \(Q'\), l'area di un parallelogramma si calcola come prodotto della base per l'altezza. Consideriamo il parallelogramma \(Q'\) definito dai vertici 
\[
A'(0,0),\quad B'(4,0),\quad C'(5,2),\quad D'(1,2).
\]
La base del parallelogramma è data dal lato \(A'B'\), la cui lunghezza è \(4\).

Per calcolare l'altezza, proiettiamo il punto \(C'(5,2)\) sulla retta che contiene \(A'B'\) (cioè la retta \(y=0\)). La proiezione di \(C'\) è il punto \(C''(5,0)\). La distanza tra \(C'\) e \(C''\) si ottiene applicando il teorema di Pitagora:
\[
h=\sqrt{(5-5)^2+(2-0)^2}=\sqrt{0+4}=2.
\]
Pertanto, l'area del parallelogramma \(Q'\) è data da:
\[
\text{Area}(Q')=\text{base}\times h=4\times 2=8.
\]

\medskip

\begin{center}
\begin{tikzpicture}[scale=0.8]
  % Quadrilatero Q (rettangolo)
  \draw[thick] (0,0) rectangle (4,2);
  \node at (2,1) {\(Q\)};
  
  % Quadrilatero Q' (parallelogramma), spostato a destra
  \draw[thick] (5,0) -- (9,0) -- (10,2) -- (6,2) -- cycle;
  \node at (7.5,1) {\(Q'\)};
\end{tikzpicture}
\end{center}
\end{esempio}

\subsubsection*{Implicazioni tra le Equivalenze: Dimostrazioni e Controesempi}

\begin{statement}
Se due figure piane sono congruenti, allora sono simili.
\end{statement}

\begin{proof}[dimostrazione]
Se due figure \(F\) e \(G\) sono congruenti, esiste una trasformazione rigida (traslazione, rotazione e/o riflessione) che trasforma \(F\) in \(G\). Le trasformazioni rigide preservano gli angoli e mantengono i rapporti di lunghezza invariati (scala 1). Pertanto, gli angoli corrispondenti di \(F\) e \(G\) sono congruenti e i lati corrispondenti sono in proporzione con rapporto costante \(k=1\). Così, per definizione, \(F\) e \(G\) sono simili.
\end{proof}

\begin{statement}
Se due figure piane sono congruenti, allora hanno la stessa area.
\end{statement}

\begin{proof}[dimostrazione]
Le trasformazioni rigide, come rotazioni, traslazioni e riflessioni, preservano le misure (compresa l'area). Se \(F\) e \(G\) sono congruenti, esiste una trasformazione rigida che mappa \(F\) su \(G\); pertanto, l'area di \(F\) è esattamente uguale all'area di \(G\).
\end{proof}

\subsubsection*{Controesempi alle Implicazioni Inverse}

\textbf{Controesempio 1: Similitudine non implica equivalenza per area.}  
Consideriamo due quadrati simili ma di dimensioni differenti. Ad esempio, il quadrato \(Q_1\) ha lato 2 e il quadrato \(Q_2\) ha lato 4. Pur essendo simili (poiché tutti gli angoli sono retti e i lati sono in proporzione 1:2), le loro aree risultano rispettivamente \(2^2=4\) e \(4^2=16\).

\begin{center}
\begin{tikzpicture}[scale=0.8]
  % Quadrato Q1 con lato 2
  \draw[thick] (0,0) rectangle (2,2);
  \node at (1,1) {\(Q_1\)};
  
  % Quadrato Q2 con lato 4, spostato a destra
  \draw[thick] (3,0) rectangle (7,4);
  \node at (5,2) {\(Q_2\)};
  
  % Freccia che evidenzia la trasformazione di scala
  \draw[->, dashed] (2.2,1) -- (2.8,1) node[midway, above] {};
\end{tikzpicture}
\end{center}

\textbf{Controesempio 2: Equivalenza per area non implica similitudine.}  
Consideriamo un rettangolo \(R\) e un parallelogramma \(P\) che hanno la stessa area, ma forme differenti. Ad esempio, il rettangolo \(R\) ha base 4 e altezza 2 (area \(4\times2=8\)), mentre il parallelogramma \(P\) ha base 5 e altezza \(1.6\) (area \(5\times1.6=8\)); tuttavia, \(R\) ha angoli retti, mentre \(P\) ha angoli non retti, quindi le due figure non sono simili.

\begin{center}
\begin{tikzpicture}[scale=0.8]
  % Rettangolo R
  \draw[thick] (0,0) rectangle (4,2);
  \node at (2,1) {\(R\)};
  
% Parallelogramma P, spostato ulteriormente a destra
\draw[thick] (7,0) -- (12,0) -- (11,1.6) -- (6,1.6) -- cycle;
\node at (9,0.8) {\(P\)};
  
  % Freccia per evidenziare l'equivalenza per area
  \draw[->, dashed] (4.2,1) -- (5.8,1) node[midway, above] {};
\end{tikzpicture}
\end{center}

\subsec{Teoremi di Pitagora e Dimostrazione [2]}%[39] problemi a 1 o 2 incognite.

\textbf{Intuizione Geometrica:}  
Il disegno seguente illustra una delle classiche costruzioni geometriche che conducono al Teorema di Pitagora.

\begin{center}
\begin{tikzpicture}[scale=0.6, line cap=round, line join=round]
  % Definiamo i punti del triangolo rettangolo (3-4-5)
  \coordinate (A) at (0,0);
  \coordinate (B) at (3,0);      % lunghezza AB = 3 (lato a)
  \coordinate (C) at (3,4);      % lunghezza BC = 4 (lato b), AC = 5 (ipotenusa c)

  % Disegno del triangolo rettangolo
  \draw[thick] (A) -- (B) -- (C) -- cycle;

  % Quadrato sul lato a (AB)
  % Costruiamo il quadrato verso il basso
  \path[draw=red, fill=red!15, thick]
    (A) -- (B) -- ++(0,-3) -- ++(-3,0) -- cycle;

  % Quadrato sul lato b (BC)
  % Costruiamo il quadrato verso destra
  \path[draw=blue, fill=blue!15, thick]
    (B) -- (C) -- ++(4,0) -- ++(0,-4) -- cycle;

  % Quadrato sul lato c (AC)
  % Il vettore AC è (3,4); ruotiamo di 90° in senso antiorario per ottenere (-4,3)
  \path[draw=purple, fill=purple!15, thick]
    (A) -- (C) -- ++(-4,3) -- ++(-3,-4) -- cycle;

  % Etichette per i lati
  \node at ($(A)!0.5!(B)-(0,0.2)$) {\(a\)};
  \node at ($(B)!0.5!(C)+(0.2,0)$) {\(b\)};
  \node at ($(A)!0.5!(C)+(-0.3,0.2)$) {\(c\)};

\end{tikzpicture}
\end{center}

Notiamo che l'area segnata in blu sommata all'area segnata in rosso ha la stessa misura dell'area segnata in viola.

\subsubsection*{Teorema di Pitagora}

\begin{theorem}[Teorema di Pitagora]
Sia un triangolo rettangolo con cateti di lunghezza \(a\) e \(b\) e ipotenusa di lunghezza \(c\). Allora
\[
a^2 + b^2 = c^2.
\]
\end{theorem}

\begin{proof}[dimostrazione]
In un triangolo rettangolo \(ABC\) con angolo retto in \(C\), consideriamo i cateti di lunghezza \(a\) e \(b\), e l'ipotenusa di lunghezza \(c\). Costruiamo un quadrato esterno di lato \((a+b)\) e disponiamo all'interno quattro copie congruenti del triangolo rettangolo lungo i suoi bordi, in modo tale che le loro ipotenuse racchiudano un quadrato centrale di lato \(c\). L'area del quadrato esterno, \((a+b)^2\), coincide quindi con la somma delle aree dei quattro triangoli \(\bigl(4 \times \tfrac{1}{2}ab = 2ab\bigr)\) e del quadrato interno \(\bigl(c^2\bigr)\). Confrontando le due espressioni, si ottiene:
\[
(a+b)^2 = 2ab + c^2,
\]
da cui, espandendo \((a+b)^2\) e semplificando, risulta:
\[
a^2 + b^2 = c^2.
\]
Questa costruzione evidenzia che l'area del quadrato sull'ipotenusa è esattamente pari alla somma delle aree dei quadrati sui cateti, come enunciato dal Teorema di Pitagora.

\begin{center}
\begin{tikzpicture}[scale=1, line cap=round, line join=round]

  % Parametri del triangolo rettangolo
  \def\a{2}            % cateto a
  \def\b{3}            % cateto b
  \pgfmathsetmacro{\c}{sqrt(\a*\a + \b*\b)} % ipotenusa c = sqrt(a^2 + b^2)
  % Lato del quadrato esterno = a + b
  \def\S{\a+\b}

  % Idea: disponiamo i 4 triangoli lungo i bordi di un quadrato di lato (a+b),
  % in modo che l'ipotenusa di ciascuno faccia da lato al quadrato centrale di lato c.

  % 1) Partiamo dal triangolo in basso a sinistra.
  %    - Un cateto lungo l'asse x (lungo a)
  %    - Un cateto lungo l'asse y (lungo b)
  %    - Vertici: (0,0), (a,0), (0,b)

  \coordinate (A1) at (0,0);
  \coordinate (B1) at (\a,0);
  \coordinate (C1) at (0,\b);

  % 2) Per gli altri triangoli, sfruttiamo rotazioni di 90° attorno ai vertici
  %    del quadrato esterno di lato S = a + b.
  %    In tal modo, tutti i cateti si "appoggiano" sui lati del quadrato esterno
  %    e le ipotenuse si toccano a formare il quadrato centrale.

  % Vertice in alto a sinistra del quadrato grande: (0,S)
  % Rotazione del triangolo T1 di -90° intorno a (0,S) per ottenere T2

  \begin{scope}[shift={(0,\S)}, rotate=-90]
    \coordinate (A2) at (0,0);
    \coordinate (B2) at (\a,0);
    \coordinate (C2) at (0,\b);
    % Ora questi punti, visti dall'esterno, si trovano correttamente in alto a sinistra.
    % Li disegneremo dopo aver terminato la rotazione.
    \draw[thick, fill=blue!20, draw=blue]
      (A2) -- (B2) -- (C2) -- cycle;
  \end{scope}

  % Vertice in alto a destra del quadrato grande: (S,S)
  % Rotazione del triangolo T1 di 180° intorno a (S,S) per ottenere T3

  \begin{scope}[shift={(\S,\S)}, rotate=180]
    \coordinate (A3) at (0,0);
    \coordinate (B3) at (\a,0);
    \coordinate (C3) at (0,\b);
    \draw[thick, fill=green!20, draw=green]
      (A3) -- (B3) -- (C3) -- cycle;
  \end{scope}

  % Vertice in basso a destra del quadrato grande: (S,0)
  % Rotazione del triangolo T1 di 90° intorno a (S,0) per ottenere T4

  \begin{scope}[shift={(\S,0)}, rotate=90]
    \coordinate (A4) at (0,0);
    \coordinate (B4) at (\a,0);
    \coordinate (C4) at (0,\b);
    \draw[thick, fill=violet!20, draw=violet]
      (A4) -- (B4) -- (C4) -- cycle;
  \end{scope}

  % Disegno del primo triangolo (quello in basso a sinistra) dopo aver disegnato i 3 ruotati
  \draw[thick, fill=red!20, draw=red] (A1) -- (B1) -- (C1) -- cycle;

  % Disegno del quadrato esterno di lato (a+b)
  \draw[thick] (0,0) rectangle (\S,\S);

  % Ora disegniamo il "quadrato" interno di lato c. In questa costruzione
  % le ipotenuse dei 4 triangoli coincidono proprio con i lati di questo quadrato.
  % Il modo più semplice per vederlo è notare che le ipotenuse si incontrano
  % in un quadrilatero al centro, i cui lati sono c.
  % Tuttavia, le coordinate di tale quadrato si ottengono dall'intersezione delle linee
  % che passano per le ipotenuse di ogni triangolo.
  % Per brevità, possiamo tracciare le ipotenuse e lasciare che si incrocino.

  % Ipotenusa del triangolo T1
  \draw[thick, dashed] (B1) -- (C1);

  % Ipotenusa del triangolo T2 (bisogna ripetere la stessa trasformazione)
  % SHIFT=(0,S), rotate=-90 => applichiamo la rotazione e lo shift a B1 e C1
  \begin{scope}[shift={(0,\S)}, rotate=-90]
    \draw[thick, dashed] (\a,0) -- (0,\b);
  \end{scope}

  % Ipotenusa del triangolo T3
  \begin{scope}[shift={(\S,\S)}, rotate=180]
    \draw[thick, dashed] (\a,0) -- (0,\b);
  \end{scope}

  % Ipotenusa del triangolo T4
  \begin{scope}[shift={(\S,0)}, rotate=90]
    \draw[thick, dashed] (\a,0) -- (0,\b);
  \end{scope}

  % Etichette
  \node at (1,0) [below] {\(a\)};
  \node at (0,1.5) [left] {\(b\)};

\end{tikzpicture}
\end{center}

\smallskip
\textit{Descrizione:} I quattro triangoli colorati in rosso, blu, verde e viola sono copie congruenti del triangolo rettangolo iniziale, disposti lungo i lati del quadrato di lato \((a+b)\). Le loro ipotenuse, collegate fra loro, formano al centro un quadrato di lato \(c\). Questa configurazione geometrica mostra come l'area del quadrato esterno si possa scomporre in quattro triangoli uguali e in un quadrato interno, fornendo la base per la dimostrazione del Teorema di Pitagora.
\end{proof}

\subsubsection*{Esempi di applicazione del Teorema di Pitagora}

\begin{esempio}[Problema aritmetico]
Un triangolo rettangolo ha i due cateti di lunghezza \(6\) m e \(8\) m. Calcolare la lunghezza dell'ipotenusa.
\[
c = \sqrt{6^2 + 8^2}
= \sqrt{36 + 64}
= \sqrt{100}
= 10 \text{ m.}
\]
\end{esempio}

\begin{esempio}[Problema algebrico di I grado]
Un triangolo rettangolo ha l’ipotenusa di lunghezza \(13\) cm, e la differenza tra i cateti è \(7\) cm. Determinare la lunghezza dei cateti.

Siano \(a\) e \(b\) le lunghezze dei due cateti, con \(a > b\). Abbiamo il sistema:
\[
\begin{cases}
a - b = 7, \\
a^2 + b^2 = 13^2 = 169.
\end{cases}
\]
Dal primo si ricava \(a = b + 7\). Sostituiamo nella seconda equazione:
\[
(b + 7)^2 + b^2 = 169 
\quad \Longrightarrow \quad b^2 + 14b + 49 + b^2 = 169,
\]
\[
2b^2 + 14b + 49 = 169 
\quad \Longrightarrow \quad 2b^2 + 14b - 120 = 0.
\]
Dividiamo per 2:
\[
b^2 + 7b - 60 = 0.
\]
La soluzione di questa equazione di secondo grado è
\[
b = \frac{-7 \pm \sqrt{7^2 + 4 \cdot 60}}{2}
= \frac{-7 \pm \sqrt{49 + 240}}{2}
= \frac{-7 \pm \sqrt{289}}{2}
= \frac{-7 \pm 17}{2}.
\]
Scartando la soluzione negativa, otteniamo \(b = 5\). Di conseguenza, \(a = b + 7 = 12\). I cateti misurano dunque \(12\) cm e \(5\) cm.
\end{esempio}

\begin{esempio}[Problema algebrico di II grado con sistema a due variabili]
Si consideri un triangolo rettangolo i cui cateti misurano \(x\) e \(y\), con \(x > y\). Si sa che il perimetro del triangolo è \(36\) e che la differenza tra i cateti è \(6\). Determinare la lunghezza di \(x\) e \(y\), nonché dell'ipotenusa.

\textit{Impostazione del problema:}  
Il triangolo è rettangolo, quindi l'ipotenusa \(c\) soddisfa
\[
c = \sqrt{x^2 + y^2}.
\]
Sappiamo inoltre che:
\[
x + y + c = 36, 
\quad 
x - y = 6.
\]

\textit{Formulazione del sistema:}
\[
\begin{cases}
x + y + \sqrt{x^2 + y^2} = 36,\\
x - y = 6.
\end{cases}
\]

\textit{Risoluzione:}  
Dal secondo vincolo \(x - y = 6\) si ricava
\[
x = y + 6.
\]
Sostituiamo questa espressione nella prima equazione:
\[
(y + 6) + y + \sqrt{(y + 6)^2 + y^2} = 36.
\]
Si semplifica:
\[
2y + 6 + \sqrt{(y + 6)^2 + y^2} = 36
\quad \Longrightarrow \quad
2y + \sqrt{y^2 + 12y + 36 + y^2} = 30,
\]
\[
\sqrt{2y^2 + 12y + 36} = 30 - 2y.
\]
Per avere un valore reale, è necessario che \(30 - 2y \ge 0\), ossia \(y \le 15\). Elevando al quadrato entrambi i membri,
\[
2y^2 + 12y + 36 = (30 - 2y)^2
\quad \Longrightarrow \quad
2y^2 + 12y + 36 = 900 - 120y + 4y^2.
\]
Riuniamo i termini:
\[
0 = 900 - 120y + 4y^2 - (2y^2 + 12y + 36)
\quad \Longrightarrow \quad
0 = 900 - 120y + 4y^2 - 2y^2 - 12y - 36,
\]
\[
0 = 864 - 132y + 2y^2
\quad \Longrightarrow \quad
2y^2 - 132y + 864 = 0.
\]
Dividendo per 2:
\[
y^2 - 66y + 432 = 0.
\]
Il discriminante risulta:
\[
\Delta = 66^2 - 4 \cdot 432 = 4356 - 1728 = 2628.
\]
Non è un quadrato perfetto, ma
\[
\sqrt{2628} = 6\sqrt{73}.
\]
Le soluzioni dell’equazione in \(y\) sono:
\[
y = \frac{66 \pm 6\sqrt{73}}{2} 
= 33 \pm 3\sqrt{73}.
\]
Affinché \(30 - 2y \ge 0\), occorre \(y \le 15\).  
Osserviamo che \(33 + 3\sqrt{73}\) è molto maggiore di \(15\), quindi \(\;y = 33 + 3\sqrt{73}\) non è accettabile nel contesto geometrico. L’unica soluzione ammissibile è
\[
y = 33 - 3\sqrt{73}.
\]
Di conseguenza,
\[
x = y + 6 = (33 - 3\sqrt{73}) + 6 
= 39 - 3\sqrt{73}.
\]
Infine l’ipotenusa è
\[
c = \sqrt{x^2 + y^2}.
\]
Sostituendo i valori di \(x\) e \(y\) si ottiene un’espressione radicale che, numericamente, risulta coerente con la condizione \(x + y + c = 36\).
\end{esempio}




\subsec{Teoremi di Euclide e Dimostrazione [2]}

Le costruzioni evidenziate mostrano come, tracciando l’altezza dal vertice retto di un triangolo rettangolo, si ottengono due nuovi triangoli che, insieme al triangolo originale, risultano a coppie simili fra loro. Questa rete di similitudini costituisce il fondamento delle dimostrazioni dei Teoremi di Euclide, in quanto rende possibili relazioni precise fra i lati del triangolo e i segmenti in cui l’altezza suddivide l’ipotenusa.

\begin{center}
\begin{tikzpicture}[scale=1.0, line cap=round, line join=round]

  % Vertici del triangolo ABC (rettangolo in C)
  \coordinate (A) at (0,0);
  \coordinate (B) at (5,0);
  \coordinate (C) at (2,3);

  % Piede dell'altezza da C su AB
  \coordinate (H) at ($(A)!(C)!(B)$);

  % Riempimento dei due "piccoli" triangoli
  \fill[red!20]   (A) -- (H) -- (C) -- cycle;   % Triangolo AHC
  \fill[green!20] (B) -- (H) -- (C) -- cycle;   % Triangolo BHC

  % Disegno del triangolo principale e dell'altezza
  \draw[thick] (A) -- (B) -- (C) -- cycle;
  \draw[thick, dashed] (C) -- (H);

  % Etichette dei vertici
  \node[below left]  at (A) {\(A\)};
  \node[below right] at (B) {\(B\)};
  \node[above]       at (C) {\(C\)};
  \node[below]       at (H) {\(H\)};

  % Etichette dei segmenti p, q, h (opzionali)
  \draw[decorate, decoration={brace, amplitude=4pt, mirror}] (A) -- (H)
    node[midway, below] {\(p\)};
  \draw[decorate, decoration={brace, amplitude=4pt, mirror}] (H) -- (B)
    node[midway, below] {\(q\)};
  \node at ($(C)!0.5!(H)+(0.3,0)$) {\(h\)};

\end{tikzpicture}
\end{center}

\subsubsection*{Teoremi di Euclide}

\begin{Theorem}[Primo Teorema di Euclide]
In un triangolo rettangolo \(ABC\) con angolo retto in \(C\), si consideri l’altezza \(CH\) condotta sull’ipotenusa \(AB\). Se indichiamo con \(p = AH\) e \(q = BH\) i due segmenti in cui l’ipotenusa è suddivisa dal piede dell’altezza, e con \(h = CH\) la lunghezza dell’altezza, allora
\[
h^2 = p \cdot q.
\]
In altre parole, l’altezza relativa all’ipotenusa è media geometrica dei due segmenti in cui divide l’ipotenusa.
\end{Theorem}

Vediamo ora una rappresentazione grafica:

\begin{center}
\begin{tikzpicture}[scale=1.0, line cap=round, line join=round]

  % Triangolo rettangolo ABC, con angolo retto in C
  \coordinate (A) at (0,0);
  \coordinate (B) at (5,0);
  \coordinate (C) at (2,3);

  % Proiezione di C su AB (piede dell'altezza H)
  \coordinate (H) at ($(A)!(C)!(B)$);

  % Disegno del triangolo principale (lati in nero)
  \draw[thick] (A) -- (B) -- (C) -- cycle;
  
  % Segmento CH tratteggiato in nero (prima di evidenziarlo a colori)
  \draw[thick, dashed] (C) -- (H);

  % ----------------------------------------------------------------
  % Evidenziazione dei segmenti p, q, h con colori diversi
  % p = AH (rosso)
  \draw[line width=1pt, red!60!black] (A) -- (H);
  % q = BH (verde)
  \draw[line width=1pt, green!60!black] (B) -- (H);
  % h = CH (blu, tratteggiato)
  \draw[line width=1pt, blue, dashed] (C) -- (H);
  % ----------------------------------------------------------------

  % Etichette dei vertici
  \node[below left]  at (A) {\(A\)};
  \node[below right] at (B) {\(B\)};
  \node[above]       at (C) {\(C\)};
  \node[below]       at (H) {\(H\)};

  % Etichette dei segmenti p, q, h (con parentesi graffe)
  \draw[decorate, decoration={brace, amplitude=5pt, mirror}] (A) -- (H)
    node[midway, below] {\(p\)};
  \draw[decorate, decoration={brace, amplitude=5pt, mirror}] (H) -- (B)
    node[midway, below] {\(q\)};
  \node at ($(C)!0.5!(H) + (0.3,0)$) {\(h\)};

  % Etichette dei cateti a, b, ipotenusa c
  \node at ($(A)!0.5!(C)$) [left]  {\(b\)};
  \node at ($(B)!0.5!(C)$) [right] {\(a\)};
  \node at ($(A)!0.5!(B)$) [below] {\(c\)};

\end{tikzpicture}
\end{center}

In questo disegno, i segmenti \(\overline{AH}\) (\(p\)) e \(\overline{BH}\) (\(q\)) sono evidenziati rispettivamente in rosso e verde, mentre l’altezza \(\overline{CH}\) (\(h\)) è evidenziata in blu tratteggiato. Tutti gli altri lati del triangolo rettangolo \(ABC\) sono disegnati con linee nere standard. In questo modo, si mette in risalto la scomposizione dell’ipotenusa \(AB\) nei segmenti \(p\) e \(q\), e la misura dell’altezza \(h\).

\begin{proof}[dimostrazione]
Sia \(ABC\) un triangolo rettangolo con \(\angle C = 90^\circ\). Tracciamo l’altezza \(CH\) sull’ipotenusa \(AB\), e indichiamo con \(H\) il piede dell’altezza. Denotiamo inoltre \(AH = p\) e \(BH = q\), e l’altezza \(CH = h\).

Osserviamo i due triangoli rettangoli \(AHC\) e \(BHC\). Essi sono simili al triangolo \(ABC\) (perché condividono gli angoli acuti e hanno in comune l’angolo retto). In particolare,
\[
\triangle AHC \sim \triangle CBA
\quad \text{e} \quad
\triangle BHC \sim \triangle CAB.
\]
Dalla similitudine \(\triangle AHC \sim \triangle CBA\) otteniamo il rapporto fra i lati corrispondenti:
\[
\frac{h}{b} = \frac{p}{c}
\quad \Longrightarrow \quad
h = \frac{bp}{c}.
\]
Analogamente, dalla similitudine \(\triangle BHC \sim \triangle CAB\):
\[
\frac{h}{a} = \frac{q}{c}
\quad \Longrightarrow \quad
h = \frac{aq}{c}.
\]
Essendo \(c = AB = p + q\), e sapendo inoltre che \(a^2 + b^2 = c^2\) (Teorema di Pitagora), si dimostra (anche attraverso altri passaggi di similitudine) che la relazione più sintetica è:
\[
h^2 = p \, q.
\]
In questo modo, l’altezza \(h\) è media geometrica dei segmenti \(p\) e \(q\). 
\end{proof}


\begin{Theorem}[Secondo Teorema di Euclide]
Nello stesso triangolo rettangolo \(ABC\) con altezza \(CH\) sull’ipotenusa \(AB\), ciascun cateto è media geometrica fra l’intera ipotenusa e il segmento dell’ipotenusa adiacente a quel cateto. In simboli:
\[
AC^2 = p \cdot AB,
\quad
BC^2 = q \cdot AB,
\]
dove \(AC = b\), \(BC = a\), \(AB = c\), \(AH = p\) e \(BH = q\).
\end{Theorem}

\begin{proof}[dimostrazione]
Consideriamo di nuovo il triangolo rettangolo \(ABC\), con \(\angle C = 90^\circ\). Poniamo \(AC = b\), \(BC = a\), \(AB = c\), e i segmenti \(AH = p\), \(BH = q\).  

Dal rapporto di similitudine \(\triangle AHC \sim \triangle CBA\), abbiamo:
\[
\frac{AC}{AB} = \frac{AH}{AC}
\quad \Longrightarrow \quad
\frac{b}{c} = \frac{p}{b}
\quad \Longrightarrow \quad
b^2 = p \, c.
\]
Allo stesso modo, dalla similitudine \(\triangle BHC \sim \triangle CAB\):
\[
\frac{BC}{AB} = \frac{BH}{BC}
\quad \Longrightarrow \quad
\frac{a}{c} = \frac{q}{a}
\quad \Longrightarrow \quad
a^2 = q \, c.
\]
Da cui le due relazioni finali:
\[
b^2 = p \, c, 
\quad
a^2 = q \, c.
\]
Ovvero ciascun cateto è media geometrica fra la lunghezza dell’ipotenusa e il segmento di ipotenusa a esso adiacente.
\end{proof}

\begin{center}
\begin{tikzpicture}[scale=1.0, line cap=round, line join=round]

  % Triangolo rettangolo ABC, con angolo retto in C
  \coordinate (A) at (0,0);
  \coordinate (B) at (5,0);
  \coordinate (C) at (2,3);

  % Proiezione di C su AB (piede dell'altezza H)
  \coordinate (H) at ($(A)!(C)!(B)$);

  % Disegno del triangolo principale (lati in nero)
  \draw[thick] (A) -- (B) -- (C) -- cycle;
  
  % Altezza CH tratteggiata in nero
  \draw[thick, dashed] (C) -- (H);

  % -------------------------------------------------------------
  % Evidenziazione dei segmenti rilevanti per il Secondo Teorema:
  %  - AC e AH (in rosso)
  %  - BC e BH (in verde)
  %  - AB (ipotenusa) rimane in nero
  % -------------------------------------------------------------
  
  % AC (rosso)
  \draw[line width=1pt, red!60!black] (A) -- (C);
  % AH (rosso)
  \draw[line width=1pt, red!60!black] (A) -- (H);

  % BC (verde)
  \draw[line width=1pt, green!60!black] (B) -- (C);
  % BH (verde)
  \draw[line width=1pt, green!60!black] (B) -- (H);

  % Etichette dei vertici
  \node[below left]  at (A) {\(A\)};
  \node[below right] at (B) {\(B\)};
  \node[above]       at (C) {\(C\)};
  \node[below]       at (H) {\(H\)};

  % Etichette dei segmenti p, q, h (con parentesi graffe)
  \draw[decorate, decoration={brace, amplitude=5pt, mirror}] (A) -- (H)
    node[midway, below] {\(p\)};
  \draw[decorate, decoration={brace, amplitude=5pt, mirror}] (H) -- (B)
    node[midway, below] {\(q\)};
  \node at ($(C)!0.5!(H) + (0.3,0)$) {\(h\)};

  % Etichette dei cateti a, b, ipotenusa c
  \node at ($(A)!0.5!(C)$) [left]  {\(b\)};
  \node at ($(B)!0.5!(C)$) [right] {\(a\)};
  \node at ($(A)!0.5!(B)$) [below] {\(c\)};

\end{tikzpicture}
\end{center}

\begin{esempio}[Problema aritmetico]
In un triangolo rettangolo \(ABC\) con ipotenusa \(AB = 13\) e cateti \(AC = b\), \(BC = a\), sia \(CH\) l’altezza condotta sull’ipotenusa. Sapendo che \(AC = 5\) e \(BC = 12\), calcolare i segmenti \(AH\) e \(BH\).

L’ipotenusa \(AB\) misura \(13\). Per il Primo Teorema di Euclide, \(CH^2 = AH \cdot BH\). Inoltre, poiché \(AC^2 = AH \cdot AB\) (Secondo Teorema di Euclide), abbiamo:
\[
5^2 = AH \cdot 13 
\quad \Longrightarrow \quad AH = \frac{25}{13}.
\]
Analogamente,
\[
12^2 = BH \cdot 13
\quad \Longrightarrow \quad BH = \frac{144}{13}.
\]
Verifichiamo che \(AH + BH = 13\). Infatti, \(\tfrac{25}{13} + \tfrac{144}{13} = \tfrac{169}{13} = 13\). Quindi \(AH = \tfrac{25}{13}\) e \(BH = \tfrac{144}{13}\).
\end{esempio}

\medskip

\begin{esempio}[Problema algebrico di I grado]
In un triangolo rettangolo \(ABC\) con \(\angle C = 90^\circ\), si indica con \(AB = c\) l’ipotenusa, e con \(AC = b\), \(BC = a\) i cateti. L’altezza dall’angolo retto \(CH\) divide l’ipotenusa in \(AH = p\) e \(BH = q\). Sapendo che \(b = 8\), \(p - q = 2\) e che \(c = p + q\), determinare \(p\), \(q\) e \(c\).

Dal Secondo Teorema di Euclide, \(b^2 = p \cdot c\). Sostituiamo \(b = 8\) e \(c = p + q\):
\[
8^2 = p(p + q) = p^2 + pq.
\]
Sappiamo anche che \(p - q = 2\). Riscriviamo \(q = p - 2\). Allora
\[
64 = p^2 + p(p - 2) = p^2 + p^2 - 2p = 2p^2 - 2p.
\]
Otteniamo \(2p^2 - 2p - 64 = 0\), cioè \(p^2 - p - 32 = 0\). Le soluzioni dell’equazione sono
\[
p = \frac{1 \pm \sqrt{1 + 128}}{2} = \frac{1 \pm \sqrt{129}}{2}.
\]
Se vogliamo \(p > q\) e \(p - q = 2\), scegliamo la soluzione che risulta coerente con i dati (solitamente si scarta quella negativa o troppo piccola). Ponendo
\[
p = \frac{1 + \sqrt{129}}{2},
\]
allora \(q = p - 2\). L’ipotenusa vale \(c = p + q = 2p - 2\). Numericamente, si verifica che i valori soddisfano le relazioni richieste.
\end{esempio}

\medskip

\begin{esempio}[Problema algebrico di II grado]
Un triangolo rettangolo \(ABC\) ha \(\angle C = 90^\circ\), con ipotenusa \(AB = c\). L’altezza \(CH\) sull’ipotenusa divide \(AB\) in \(AH = p\) e \(BH = q\). Siano \(a = BC\) e \(b = AC\). Si sa che il perimetro \(a + b + c\) è \(30\) e che \(p + q = c\). Usando i Teoremi di Euclide e di Pitagora, risolviamo il sistema:

\[
\begin{cases}
a + b + c = 30,\\
a^2 + b^2 = c^2,\\
a^2 = c\,q,\quad b^2 = c\,p,\\
p + q = c.
\end{cases}
\]

La relazione \(a^2 + b^2 = c^2\) discende dal Teorema di Pitagora, mentre \(a^2 = c\,q\) e \(b^2 = c\,p\) derivano dal Secondo Teorema di Euclide. In più, \(p + q = c\). Dobbiamo trovare valori di \(a, b, c, p, q\) tali che il perimetro \(a + b + c\) risulti \(30\). 

Se non imponiamo ulteriori vincoli, esistono \emph{diverse} soluzioni reali possibili; presentiamo qui una soluzione “simmetrica” ponendo \(a = b\). Questo corrisponde a un triangolo rettangolo isoscele in cui i cateti sono uguali.
\begin{enumerate}
\item Poniamo \(a = b\). Dal Teorema di Pitagora segue
\[
c = \sqrt{a^2 + b^2} = \sqrt{2\,a^2} = a\sqrt{2}.
\]
\item Dalla condizione \(a + b + c = 30\) otteniamo
\[
a + a + a\sqrt{2} = 30 
\quad\Longrightarrow\quad
2\,a + a\sqrt{2} = 30
\quad\Longrightarrow\quad
a\,(2 + \sqrt{2}) = 30.
\]
\item Calcoliamo
\[
a = \frac{30}{2 + \sqrt{2}}
\quad\Longrightarrow\quad
a = \frac{30}{2 + \sqrt{2}} \cdot \frac{2 - \sqrt{2}}{2 - \sqrt{2}}
= \frac{30\,(2 - \sqrt{2})}{4 - 2}
= 15\,(2 - \sqrt{2}).
\]
Numericamente, \(2 - \sqrt{2} \approx 0.586\), quindi \(a \approx 15 \times 0.586 \approx 8.79\). Analogamente, \(b = a \approx 8.79\).
\item L’ipotenusa risulta
\[
c = a\sqrt{2} \approx 8.79 \times 1.414 \approx 12.43.
\]
\item Verifichiamo il perimetro: \(a + b + c \approx 8.79 + 8.79 + 12.43 \approx 30\).
\end{enumerate}
\medskip

Dal Secondo Teorema di Euclide, 
\[
a^2 = c\,q \quad\text{e}\quad b^2 = c\,p.
\]
Con \(a = b\), abbiamo \(a^2 = b^2\), quindi \(q = p\). Poiché \(p + q = c\), si ottiene \(2p = c\), dunque \(p = q = \tfrac{c}{2}\). Numericamente, 
\[
p = q = \frac{12.43}{2} \approx 6.215.
\]
Controlliamo che 
\[
a^2 = c\,q \quad\Longrightarrow\quad 8.79^2 \approx 77.3 \quad\text{e}\quad c \, q \approx 12.43 \times 6.215 \approx 77.3,
\]
coerente entro gli arrotondamenti. 
\end{esempio}
\subsec{Teorema di Talete e Dimostrazione [3]}
Il \emph{Teorema di Talete} stabilisce che, se due rette parallele intersecano i lati di un angolo (o i loro prolungamenti), i segmenti che ne derivano sono in \emph{proporzione}. Questo concetto è fondamentale per molte dimostrazioni geometriche (come quelle riguardanti figure simili) e per la risoluzione di problemi pratici in cui occorrono rapporti tra segmenti.

\begin{theorem}[Teorema di Talete]
Siano \(r\) e \(s\) due rette parallele che intersecano due semirette (od angoli) con vertice \(M\). Indicando con \(A\) e \(A'\) i punti di intersezione su \(r\) e con \(B\) e \(B'\) i punti di intersezione su \(s\), come in figura, allora i segmenti \(\overline{AM}\), \(\overline{A'M}\), \(\overline{BM}\) e \(\overline{B'M}\) risultano in proporzione, cioè:
\[
\frac{AM}{A'M} \;=\; \frac{BM}{B'M}.
\]
\end{theorem}

\begin{proof}[dimostrazione]
  Consideriamo due rette parallele \(r\) e \(s\). Sulla retta \(r\) prendiamo due punti \(A\) e \(A'\), mentre sulla retta \(s\) prendiamo due punti \(B\) e \(B'\). Siano \(M\) il vertice di un angolo, e le \emph{semirette} che escono da \(M\) intersechino \(r\) in \(A\) e \(A'\) e \(s\) in \(B\) e \(B'\).  
  Il disegno risultante ha questa forma:


\begin{center}
\begin{tikzpicture}[scale=0.9]

% Due linee orizzontali (rette parallele) "r" e "s"
\draw[thick] (-1,0)--(5,0) node[right]{$r$};
\draw[thick] (-1,-2)--(5,-2) node[right]{$s$};

% Semirette che si incontrano in M (in basso)
\draw[thick] (0,1)--(2,-3);
\draw[thick] (4,1)--(2,-3);

% Intersezioni con r e s
\coordinate (A) at (0.5, 0);
\coordinate (B) at (1.5, -2);
\coordinate (A') at (3.5, 0);
\coordinate (B') at (2.5, -2);

\coordinate (M) at (2, -3);

\fill (A) circle(1.2pt) node[above right]{$A$};
\fill (B) circle(1.2pt) node[below left]{$B$};
\fill (A') circle(1.2pt) node[above left]{$A'$};
\fill (B') circle(1.2pt) node[below right]{$B'$};
\fill (M) circle(1.2pt) node[below]{$M$};

\end{tikzpicture}
\end{center}
\begin{enumerate}
\item \textbf{Triangoli considerati.}  
  Osserviamo i due triangoli \(\triangle MAB\) e \(\triangle MA'B'\). Nel primo triangolo, i vertici sono \(M, A, B\). Nel secondo, i vertici sono \(M, A', B'\). 

\item \textbf{Parallelismo e angoli corrispondenti.}  
  Dato che \(r\parallel s\), si formano coppie di \emph{angoli alterni interni} e \emph{angoli corrispondenti} congruenti. In particolare:
  \begin{itemize}
    \item L’angolo \(\angle AMB\) è comune a entrambi i triangoli (si trova in vertice \(M\)).
    \item L’angolo \(\angle MAB\) e l’angolo \(\angle MA'B'\) risultano \emph{congruenti} perché la retta \(AB\) e la retta \(A'B'\) “catturano” angoli alterni interni con \(r\parallel s\).
    \item Analogamente, l’angolo \(\angle MBA\) e l’angolo \(\angle MB'A'\) sono congruenti per lo stesso motivo.
  \end{itemize}

\item \textbf{Similitudine per angoli.}  
  Nei triangoli \(\triangle MAB\) e \(\triangle MA'B'\), abbiamo dunque \emph{tre coppie di angoli} rispettivamente congruenti:
  \[
    \angle AMB = \angle A'MB',\quad
    \angle MAB = \angle MA'B',\quad
    \angle MBA = \angle MB'A'.
  \]
  Pertanto, i due triangoli sono \emph{simili} (criterio di similitudine “angolo–angolo–angolo”).

\item \textbf{Conclusione: Proporzione dei lati.}  
  Dalla \emph{similitudine} dei triangoli \(\triangle MAB\) e \(\triangle MA'B'\), segue la proporzione dei lati corrispondenti. In particolare, osservando i lati che partono dal vertice \(M\):
  \[
    \frac{AM}{A'M}
    \;=\;
    \frac{BM}{B'M}.
  \]
  Questa è l’esatta \emph{relazione di Talete} che volevamo dimostrare.
\end{enumerate}

\end{proof}

\begin{corollary}
Se i segmenti \(\overline{AM}\) e \(\overline{A'M}\) (o \(\overline{BM}\) e \(\overline{B'M}\)) rappresentano \emph{misure} di grandezze, allora la proporzione \(\tfrac{AM}{A'M}=\tfrac{BM}{B'M}\) permette di \emph{trasferire} o \emph{riprodurre} rapporti tra segmenti su piani differenti. In particolare, se uno dei segmenti è incognito, e gli altri sono noti, si può determinare la misura incognita tramite il \emph{prodotto incrociato}.
\end{corollary}

\noindent
\textbf{Esempi Applicativi.}

\begin{esempio}
Nella figura di Talete, se sappiamo \(AM=3\) cm, \(A'M=2\) cm, e \(BM=4\) cm, possiamo calcolare \(B'M\) incognito:  
\[
\frac{AM}{A'M}
= 
\frac{BM}{B'M}
\quad\Longrightarrow\quad
\frac{3}{2}
= 
\frac{4}{B'M}
\quad\Longrightarrow\quad
3\,B'M
= 
8
\quad\Longrightarrow\quad
B'M
= 
\frac{8}{3}\text{ cm}.
\]
\end{esempio}

\bigskip

\textbf{Conclusione.}  
Il \emph{Teorema di Talete} e i suoi corollari costituiscono uno strumento essenziale per affrontare problemi di \emph{proporzioni} in geometria. La semplicità del risultato (\(\tfrac{AM}{A'M}=\tfrac{BM}{B'M}\)) si traduce in un potente \emph{metodo costruttivo} per riprodurre o verificare rapporti tra segmenti, e in una tecnica \emph{algebrica} (tramite il prodotto incrociato) per calcolare misure incognite a partire da misure note.



\subsubsection*{Tabella Riassuntiva} 
La seguente tabella riassume le principali formule per il calcolo dell’area di figure piane classiche. Per ciascuna figura, sono riportate le relazioni fondamentali che esprimono l’area in termini di misure note come lati, altezze o diagonali. Queste formule trovano applicazione sia in contesti di risoluzione aritmetica diretta sia in contesti algebrici, dove spesso si presentano incognite da determinare prima di applicare la formula.

\begin{center}
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{l|l}
\hline

\textbf{Figura} & \textbf{Formula dell'area} \\
\hline
Triangolo: base \& altezza & \(A = \tfrac12 \, (\text{base}) \times (\text{altezza})\) \\
Triangolo: tre lati \(a, b, c\) (formula di Erone) & \(A = \sqrt{s(s-a)(s-b)(s-c)}, \; s = \tfrac{a+b+c}{2}\) \\
Triangolo equilatero di lato \(a\) & \(A = \tfrac{\sqrt{3}}{4} \, a^2\) \\
Rettangolo & \(A = (\text{base}) \times (\text{altezza})\) \\
Quadrato di lato \(l\) & \(A = l^2\) \\
Parallelogramma & \(A = (\text{base}) \times (\text{altezza})\) \\
Rombo (diagonali \(d_1, d_2\)) & \(A = \tfrac{d_1 \, d_2}{2}\) \\
Trapezio (basi \(B\) e \(b\), altezza \(h\)) & \(A = \tfrac{(B + b)}{2} \times h\) \\
Cerchio di raggio \(r\) & \(A = \pi r^2\) \\
Settore circolare (angolo \(\theta\) in radianti) & \(A = \tfrac{\theta}{2} \, r^2\) \\
Poligono regolare con \(n\) lati di lunghezza \(l\) & \(A = \tfrac{n \, l^2}{4 \,\tan\!\bigl(\frac{\pi}{n}\bigr)}\) \\
\hline
\end{tabular}
\end{center}
\renewcommand{\arraystretch}{1.0}

\begin{esempio}
 
Si consideri un cerchio di raggio \(r\) al cui interno è inscritto un pentagono regolare. Ogni lato del pentagono, indicato con \(s\), sottende al centro un angolo di \(72^\circ\). Il segmento che unisce il centro del cerchio a due vertici consecutivi del pentagono individua un \emph{settore circolare} di ampiezza \(72^\circ\) e un \emph{triangolo isoscele} (con lati \(r, r, s\)). Si sa che la differenza di area fra il settore circolare e tale triangolo è pari a 5. Trovare \(r\) e \(s\).

\begin{center}
\begin{tikzpicture}[scale=2.0, line cap=round, line join=round]

  % Centro del cerchio
  \coordinate (O) at (0,0);

  % Raggio del cerchio (per disegno schematico poniamo r=1)
  \def\r{1}

  % Disegno del cerchio
  \draw[thick] (O) circle (\r);

  % Definiamo i 5 vertici di un pentagono regolare, con un vertice in alto
  \foreach \i in {0,...,4}{
    \coordinate (A\i) at (90 + 72*\i:\r);
  }

  % Disegno del pentagono regolare (collegando i 5 punti)
  \draw[thick] (A0) -- (A1) -- (A2) -- (A3) -- (A4) -- cycle;

  % Settore circolare relativo a uno spicchio di 72° (fra A0 e A1)
  % Riempito in blu tenue
  \begin{scope}
    \clip (O) -- (A0) arc[start angle=90, delta angle=72, radius=\r] -- cycle;
    \fill[blue!20] (O) circle(\r);
  \end{scope}

  % Triangolo O-A0-A1 riempito in rosso tenue
  \fill[red!20] (O) -- (A0) -- (A1) -- cycle;

  % Etichette dei vertici
  \node[above]       at (A0) {\(A_0\)};
  \node[left]       at (A1) {\(A_1\)};
  \node[below left] at (A2) {\(A_2\)};
  \node[below right]  at (A3) {\(A_3\)};
  \node[right]        at (A4) {\(A_4\)};
  \node[below right]  at (O)  {\(O\)};

  % Frecce o archi per indicare l'angolo al centro (72°)
  \draw[-] (O)+(90:0.3) arc[start angle=90, delta angle=72, radius=0.3];
  \node at ($(O)+(90+36:0.5)$) {\(72^\circ\)};

  % Se desiderato, si può etichettare la differenza di area (settore - triangolo)
  % con un nodo, ma qui lasciamo il disegno pulito.
\end{tikzpicture}
\end{center}

\textit{Nuova impostazione con l’area del pentagono regolare:}  
Un pentagono regolare inscritto in un cerchio di raggio \(r\) può essere suddiviso in 5 triangoli isosceli con lati \(r, r, s\), dove \(s\) è il lato del pentagono. L’area di ciascun triangolo è \(\tfrac12\,r^2\,\sin(72^\circ)\). Di conseguenza, l’area \(\mathcal{A}_{\text{pent}}\) dell’intero pentagono risulta
\[
\mathcal{A}_{\text{pent}} = 5 \times \bigl(\tfrac12\,r^2\,\sin(72^\circ)\bigr) 
= \tfrac{5}{2}\,r^2\,\sin(72^\circ).
\]
Il singolo triangolo (uno dei cinque) ha area 
\[
\mathcal{A}_{\text{triang}} = \tfrac12\,r^2\,\sin(72^\circ).
\]

\textit{Settore circolare da \(72^\circ\):}  
Poiché il lato \(s\) sottende un angolo al centro di \(72^\circ\), l’area del settore circolare corrispondente è
\[
\mathcal{A}_{\text{settore}} = \frac{72}{360}\,\pi\,r^2 = 0.2\,\pi\,r^2.
\]

\textit{Condizione sul lato del pentagono:}  
Il lato \(s\) è la corda che insiste su un angolo al centro di \(72^\circ\). Ne segue la relazione
\[
s = 2\,r\,\sin\bigl(36^\circ\bigr).
\]

\textit{Differenza di area pari a 5:}  
Si richiede che la differenza tra l’area del settore \(\mathcal{A}_{\text{settore}}\) e l’area del triangolo isoscele \(\mathcal{A}_{\text{triang}}\) sia 5. Matematicamente:
\[
\mathcal{A}_{\text{settore}} \;-\; \mathcal{A}_{\text{triang}} 
= 0.2\,\pi\,r^2 \;-\; \Bigl(\tfrac12\,r^2\,\sin(72^\circ)\Bigr)
= 5.
\]

\textit{Sistema finale:}  
\[
\begin{cases}
s \;=\; 2\,r\,\sin(36^\circ),\\[6pt]
0.2\,\pi\,r^2 \;-\;\tfrac12\,r^2\,\sin(72^\circ) \;=\; 5.
\end{cases}
\]

\textit{Soluzione:}  
Dalla seconda equazione si isola \(r\). Si ha
\[
0.2\,\pi\,r^2 - 0.5\,r^2\,\sin(72^\circ) = 5
\quad\Longrightarrow\quad
r^2 \,\bigl(0.2\,\pi - 0.5\,\sin(72^\circ)\bigr) = 5.
\]
Allora
\[
r^2 = \frac{5}{\,0.2\,\pi - 0.5\,\sin(72^\circ)\!}
\quad\Longrightarrow\quad
r = \sqrt{\frac{5}{\,0.2\,\pi - 0.5\,\sin(72^\circ)\!}}.
\]
Una volta trovato \(r\), si ricava \(s\) dalla prima equazione:
\[
s = 2\,r\,\sin(36^\circ).
\]

I valori di questi angoli si possono trovare con metodi trigonometrici (vedi il metodo della sezione aurea):
\[
\sin(36^\circ) \approx 0.5878, 
\quad
\sin(72^\circ) \approx 0.9511,
\quad
0.2\,\pi \approx 0.6283,
\quad
0.5\,\sin(72^\circ) \approx 0.4755.
\]
\[
0.2\,\pi - 0.5\,\sin(72^\circ) \approx 0.6283 - 0.4755 = 0.1528,
\quad
r^2 \approx \frac{5}{0.1528} \approx 32.72,
\quad
r \approx 5.72.
\]
\[
s = 2 \times 5.72 \times 0.5878 \;\approx\; 6.73.
\]


\end{esempio}

\subsec{Il Cerchio [2]}
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

\subsec{Diedri, Triedri ed Angoloidi [4]}
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

\paragraph{Triedro}
Un triedro è la parte di spazio delimitata da tre piani che si incontrano in un solo punto, detto vertice del triedro. Possiamo pensarlo come un “angolo solido” con tre “cerniere”, ciascuna lungo l’intersezione di due piani. Per misurarne le ampiezze, si considera l’angolo diedro formato da ogni coppia di piani e, in particolare, si può osservare come tali piani intersecano un opportuno piano ausiliario o si ricorre ai vettori normali dei piani stessi. In generale, un triedro genera tre diedri, uno per ogni coppia di piani.

\begin{center}
\begin{tikzpicture}[scale=1.2, line cap=round, line join=round]

  % Assi 3D
  \draw[->] (0,0,0) -- (4,0,0) node[anchor=north east] {$x$};
  \draw[->] (0,0,0) -- (0,4,0) node[anchor=north west] {$y$};
  \draw[->] (0,0,0) -- (0,0,4) node[anchor=south] {$z$};

  % Tre piani che si intersecano nell'origine (0,0,0):
  % Piano 1: x=0 (yz-plane)
  \fill[blue!20,opacity=0.5]
    (0,3,3) -- (0,3,-1) -- (0,-1,-1) -- (0,-1,3) -- cycle;

  % Piano 2: y=0 (xz-plane)
  \fill[green!20,opacity=0.5]
    (3,0,3) -- (3,0,-1) -- (-1,0,-1) -- (-1,0,3) -- cycle;

  % Piano 3: z=0 (xy-plane)
  \fill[red!20,opacity=0.5]
    (4,4,0) -- (4,0,0) -- (0,0,0) -- (0,4,0) -- cycle;

  % Origine
  \node[below left] at (0,0,0) {$O$};

\end{tikzpicture}
\end{center}

\noindent
Nella figura, i tre piani \(x=0\), \(y=0\) e \(z=0\) si incontrano tutti nell’origine \(O\). Ciascuna coppia di piani forma un diedro, e l’insieme dei tre diedri (con le relative linee di intersezione) costituisce il triedro. Se vogliamo misurare gli angoli tra questi piani, ci riconduciamo alla misura dei diedri corrispondenti. Ad esempio, l’angolo tra i piani \(x=0\) e \(y=0\) è il diedro individuato dalla retta d’intersezione \(z\)-asse e può essere calcolato esaminando un piano perpendicolare all’asse \(z\). Analoghi ragionamenti valgono per le altre due coppie di piani, producendo così tre angoli diedri che caratterizzano il triedro.

\subparagraph{Proiezioni del triedro su due piani diversi}

Nel triedro formato dai piani \(x=0\), \(y=0\), \(z=0\), è spesso utile considerare le sue \emph{proiezioni} su piani coordinate, per visualizzare in due dimensioni come si distribuiscono le linee di intersezione. Di seguito, mostriamo due proiezioni: la prima sul piano \(y\)-\(z\) (ignorando la coordinata \(x\)) e la seconda sul piano \(x\)-\(z\) (ignorando la coordinata \(y\)). Questo ci permette di vedere come un 

\begin{center}
\begin{minipage}{0.45\textwidth}
\begin{tikzpicture}[scale=1.2, line cap=round, line join=round]

  % Assi del piano yz
  \draw[->] (0,0) -- (4,0) node[right] {$y$};
  \draw[->] (0,0) -- (0,3) node[above] {$z$};

  % retta y=0 (verde, corrisponde al piano y=0 in 3D)
  \draw[thick, green] (0,0) -- (0,2.5) node[midway,left] {\(y=0\)};

  % retta z=0 (rosso, corrisponde al piano z=0 in 3D)
  \draw[thick, red] (0,0) -- (3.5,0) node[midway,below] {\(z=0\)};

  % Etichetta dell'origine
  \node[below left] at (0,0) {$O$};

\end{tikzpicture}
\end{minipage}
\hfill
\begin{minipage}{0.45\textwidth}
\begin{tikzpicture}[scale=1.2, line cap=round, line join=round]

  % Assi del piano xz
  \draw[->] (0,0) -- (4,0) node[right] {$x$};
  \draw[->] (0,0) -- (0,3) node[above] {$z$};

  % retta x=0 (blu, corrisponde al piano x=0 in 3D)
  \draw[thick, blue] (0,0) -- (0,2.5) node[midway,left] {\(x=0\)};

  % retta z=0 (rosso, corrisponde al piano z=0 in 3D)
  \draw[thick, red] (0,0) -- (3.5,0) node[midway,below] {\(z=0\)};

  % Etichetta dell'origine
  \node[below left] at (0,0) {$O$};

\end{tikzpicture}
\end{minipage}
\end{center}

Notiamo quindi come il triedro possa essere definito da due angoli (diedri) che possiamo misurare il gradi. Il caso che abbiamo preso qua è particolarmente semplice, dato che coinvolge due triangoli retti, possiamo pero facilmente immaginare come ogni altro triedro possa essere generato variando ciascuno di questi due angoli.

\paragraph{Angoloide}
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

\subparagraph{Misurare un Angoloide}
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


\subsec{Rette e Piani Perpendicolari e Paralleli [4]}
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


\subsec{Calcolo del Volume [4]}
Il calcolo del volume di un solido consiste nel misurare la porzione di spazio racchiusa dalla sua superficie. Analogamente a quanto avviene per le aree in due dimensioni, possiamo affrontare il calcolo dei volumi sia con metodi aritmetici (quando si dispone di formule dirette e dati sufficienti) sia con procedure algebriche, in cui la determinazione di misure mancanti (altezze, raggi, spigoli, ecc.) può richiedere la risoluzione di equazioni di primo o di secondo grado.

\paragraph{Prismi e parallelepipedi}
Un prisma è un solido con due basi poligonali congruenti e parallele, unite da facce laterali rettangolari. Se la base è un rettangolo (o quadrato), si ottiene un parallelepipedo. La formula generale per il volume è
\[
V = \bigl(\text{area della base}\bigr)\times \bigl(\text{altezza}\bigr).
\]
Per un parallelepipedo rettangolo con spigoli \(a, b, c\), il volume diventa
\[
V = a \, b \, c.
\]
Il \emph{cubo} è un parallelepipedo rettangolo con spigoli tutti uguali \((a)\), per cui
\[
V = a^3.
\]

\paragraph{Cilindro}
Un cilindro è un solido con due basi circolari congruenti e parallele, unite da una superficie laterale rettangolare avvolta su se stessa. La sua formula del volume è analoga a quella del prisma, con la base = cerchio di raggio \(r\):
\[
V = \pi r^2 \times h.
\]
Se in un problema l’altezza \(h\) o il raggio \(r\) non è noto, si possono impostare equazioni per determinarli, ad esempio risolvendo un sistema di primo o secondo grado che coinvolge dati relativi a superfici, perimetri o altre misure.

\paragraph{Piramide}
Una piramide è un solido con una base poligonale e un vertice (detto \emph{apice}) non complanare con la base. Le facce laterali sono triangoli. Il volume di una piramide è
\[
V = \frac{1}{3}\,\bigl(\text{area della base}\bigr)\times \bigl(\text{altezza}\bigr).
\]
Quando la base è un rettangolo (piramide a base rettangolare) o un quadrato (piramide quadrata), e l’altezza non è immediatamente data, si può ricorrere a teoremi di Pitagora o ad altri vincoli geometrici, dando origine a sistemi di equazioni.

\paragraph{Cono}
Il cono è analogo alla piramide ma con base circolare. Il suo volume si ottiene dalla formula
\[
V = \frac{1}{3}\,\pi r^2 \,h,
\]
dove \(r\) è il raggio della base e \(h\) l’altezza. Problemi conici possono diventare algebrici quando occorre determinare \(r\) o \(h\) da condizioni su superfici laterali, perimetri, inclinazioni, ecc.

\paragraph{Tronco di piramide e tronco di cono}
Un tronco di piramide si ottiene tagliando una piramide con un piano parallelo alla base; analogamente, un tronco di cono è un cono a cui è stata rimossa la parte vicina all’apice tramite un piano parallelo alla base circolare. Le formule dei volumi corrispondono a differenze di piramidi o coni interi, ma sono spesso riassunte come:
\[
V_{\text{tronco di piramide}} = \frac{h}{3}\,\bigl(A_1 + A_2 + \sqrt{A_1\,A_2}\bigr),
\]
dove \(A_1\) e \(A_2\) sono le aree delle due basi, e \(h\) la distanza fra le basi;  
\[
V_{\text{tronco di cono}} = \frac{\pi h}{3}\,\bigl(r_1^2 + r_2^2 + r_1\,r_2\bigr),
\]
dove \(r_1\) e \(r_2\) sono i raggi delle basi circolari e \(h\) l’altezza del tronco. Anche in questi casi, se uno dei raggi o la distanza fra le basi non è noto, si imposta un’equazione per determinare le incognite.

\paragraph{Sfera e parti di sfera}
La sfera di raggio \(r\) ha volume
\[
V = \frac{4}{3}\,\pi r^3.
\]
Se occorre calcolare \emph{parti} di sfera, come calotte sferiche o sfere sezionate da piani, ci si può riferire a formule specifiche. Ad esempio, la \emph{calotta sferica} di altezza \(h\) su una sfera di raggio \(r\) ha volume
\[
V_{\text{calotta}} = \frac{\pi h^2\,(3r - h)}{3}.
\]
Problemi più complessi (ad esempio una calotta sferica con vincoli su circonferenze, aree, o la combinazione con un cilindro inscritto) possono richiedere la risoluzione di equazioni di primo o secondo grado per trovare \(r\) o \(h\).


\begin{center}
% -- Disegno 2D: Sezione della sfera e calotta --
\begin{tikzpicture}[scale=1.2, line cap=round, line join=round]

  % Raggio della sfera (sezione in 2D)
  \def\r{2}

  % Centro O(0,0)
  \coordinate (O) at (0,0);

  % Disegno della sezione circolare
  \draw[thick] (O) circle(\r);

  % Piano orizzontale in 2D: y = 0.8
  \def\planeY{0.8}
  \def\capHeight{\r - \planeY} % h = r - planeY

  % Segmento orizzontale che rappresenta il piano
  \draw[dashed] (-2.5,\planeY) -- (2.5,\planeY) node[right] {piano};

  % Riempimento della calotta
  \begin{scope}
    \clip (O) circle(\r);
    \fill[blue!20] (-2.5,\planeY) rectangle (2.5,2.5);
  \end{scope}

  % Etichette
  \node[below left] at (O) {$O$};
  \draw[decorate, decoration={brace, amplitude=4pt, mirror}] (0,0) -- (2,0)
    node[midway, below=5pt] {$r$};
  \draw[<->, thick] (2.3,\planeY) -- (2.3,\r) 
    node[midway, right] {$h$};

\end{tikzpicture}
\end{center}

Un piano orizzontale, definito da \(z = \text{costante}\), interseca la sfera e produce una \emph{calotta} sopra di esso (riempita in blu). Nella figura è vista come un arco di circonferenza con un piano orizzontale in coordinate \((x,y)\). L’altezza della calotta è \(h = r - (\text{distanza del piano dal centro})\).

\subsubsection*{Settore sferico definito da un triedro}
Un triedro formato da tre piani passanti per il centro di una sfera di raggio \(r\) individua una porzione di sfera analoga al \emph{settore circolare} in due dimensioni, ma esteso in 3D. Se l’angolo solido racchiuso dal triedro è \(\Omega\) (misurato in steradi), il volume della porzione sferica (detta anche \emph{settore sferico}) risulta:
\[
V = \frac{\Omega\,r^3}{3}.
\]
In pratica, i tre piani racchiudono un “cono” di spazio con vertice al centro della sfera, e la parte di sfera compresa in questo cono è il settore sferico corrispondente.

\begin{center}
% -- Disegno 2D: Sezione o proiezione del triedro e del settore sferico --
\begin{tikzpicture}[scale=1.0, line cap=round, line join=round]

  % Disegniamo un cerchio come sezione della sfera
  \def\rr{2}
  \draw[thick] (0,0) circle(\rr);

  % Angolo in 2D (due semirette e la sfera in sezione)
  \draw[blue, thick] (0,0) -- (140:\rr*1.3);
  \draw[red, thick] (0,0) -- (30:\rr*1.3);

  % Riempimento dell'angolo
  \fill[gray!30, opacity=0.5] (0,0) -- (30:\rr) arc[start angle=30, end angle=140, radius=\rr] -- cycle;


  % Cerchio etichette
  \node[below left] at (0,0) {$O$};

\end{tikzpicture}
\end{center}

\medskip

\noindent
Questi piani formano un triedro di angolo solido \(\Omega\), e la porzione di sfera compresa fra i piani è il settore sferico di volume \(\tfrac{\Omega\,r^3}{3}\). Nel disegno una proiezione in due dimensioni illustra l’analogia con il settore circolare, ma esteso a uno spazio tridimensionale. In tale proiezione, l’angolo \(\theta\) rappresenta una sezione bidimensionale di uno dei piani rispetto a un piano di riferimento. Nella realtà 3D, l’angolo solido \(\Omega\) descrive la porzione spaziale effettiva racchiusa dal triedro. 

\subsubsection*{Tabella riassuntiva dei volumi principali}
\renewcommand{\arraystretch}{1.4}
\begin{center}
\begin{tabular}{l|l}
\hline
\textbf{Solido} & \textbf{Formula del volume} \\
\hline
Prisma & $V = \bigl(\text{area base}\bigr)\,\times\,h$ \\
Parallelepipedo rettangolo & $V = a\,b\,c$ \\
Cubo (lato $a$) & $V = a^3$ \\
Cilindro (raggio $r$, altezza $h$) & $V = \pi r^2\,h$ \\
Piramide & $V = \frac13\,\bigl(\text{area base}\bigr)\times h$ \\
Cono & $V = \frac13\,\pi r^2\,h$ \\
Tronco di piramide & $V = \frac{h}{3}\,\bigl(A_1 + A_2 + \sqrt{A_1\,A_2}\bigr)$ \\
Tronco di cono & $V = \frac{\pi h}{3}\,\bigl(r_1^2 + r_2^2 + r_1\,r_2\bigr)$ \\
Sfera (raggio $r$) & $V = \frac{4}{3}\,\pi r^3$ \\
Calotta sferica (altezza $h$ su sfera di raggio $r$) & $V = \frac{\pi h^2\,(3r - h)}{3}$ \\
\hline
\end{tabular}
\end{center}
\renewcommand{\arraystretch}{1.0}

\begin{esempio}
Un cilindro di altezza $H$ e raggio di base $R$ contiene al suo interno un cono invertito, che tocca la base superiore del cilindro con il suo vertice. Sapendo che il volume complessivo (cilindro meno cono) è pari a $300\pi$, e che $H = 3R$, determinare $H$ e $R$.

\textit{Soluzione:}  
Il volume del cilindro è $\pi R^2\,H$. Il cono ha la stessa base del cilindro (raggio $R$) ma un’altezza coincidente con $H$, quindi il suo volume è $\frac13\,\pi R^2\,H$. La differenza fra i due volumi è
\[
\pi R^2\,H \;-\; \frac13\,\pi R^2\,H \;=\; \frac23\,\pi R^2\,H.
\]
Dati $H = 3R$ e volume finale $300\pi$, otteniamo:
\[
\frac23\,\pi R^2 \,\bigl(3R\bigr) = 300\pi 
\quad\Longrightarrow\quad
\frac23 \times 3 \,\pi R^3 = 300\pi
\quad\Longrightarrow\quad
2\,\pi R^3 = 300\pi
\quad\Longrightarrow\quad
R^3 = 150
\quad\Longrightarrow\quad
R = \sqrt[3]{150}.
\]
Allora $H = 3R = 3\,\sqrt[3]{150}$. Numericamente, $R\approx 5.31$ e $H\approx 15.93$.

\end{esempio}

\begin{esempio}[Problema di II grado]
Si consideri un tronco di cono con altezza $h=10$ e basi di raggi $r_1$ e $r_2$ (con $r_2>r_1$). Il volume è $V = \frac{\pi h}{3}(r_1^2 + r_2^2 + r_1r_2)$. Se si sa che $r_2 - r_1 = 2$ e che $V=2000\pi$, determinare $r_1$ e $r_2$.

\textit{Soluzione:}  
Poniamo $r_2 = r_1 + 2$. Sostituiamo nella formula del volume:
\[
2000\pi = \frac{\pi \cdot 10}{3}\,\bigl(r_1^2 + (r_1+2)^2 + r_1(r_1+2)\bigr).
\]
\[
2000 = \frac{10}{3}\,\bigl(r_1^2 + r_1^2 + 4r_1 + 4 + r_1^2 + 2r_1\bigr)
= \frac{10}{3}\,\bigl(3r_1^2 + 6r_1 + 4\bigr).
\]
\[
2000 = \frac{10}{3}\,(3r_1^2 + 6r_1 + 4)
\quad\Longrightarrow\quad
2000 \times \frac{3}{10} = 3r_1^2 + 6r_1 + 4.
\]
\[
600 = 3r_1^2 + 6r_1 + 4
\quad\Longrightarrow\quad
3r_1^2 + 6r_1 + 4 - 600 = 0
\quad\Longrightarrow\quad
3r_1^2 + 6r_1 - 596 = 0.
\]
Risolvendo l’equazione di secondo grado, si ottiene:
\[
r_1 = \frac{-6 \pm \sqrt{36 + 4 \cdot 3 \cdot 596}}{2 \cdot 3}.
\]
Selezionando la soluzione positiva e coerente con il contesto geometrico, si trova $r_1$ e da lì $r_2 = r_1 + 2$. Questo fornisce i raggi richiesti.  
\end{esempio}

\noindent
In conclusione, i metodi di calcolo del volume possono essere diretti (quando si conoscono le formule e tutte le misure necessarie) oppure algebrici (quando bisogna determinare alcune misure incognite risolvendo equazioni di primo o di secondo grado). I solidi elementari (prisma, parallelepipedo, cilindro, piramide, cono, tronchi e sfera) offrono una vasta gamma di esempi per esercitare sia le competenze geometriche sia le tecniche algebriche.  
```
### Trigonometry
```LaTeX
\section{Trigonometria}

\subsectionstar{Misurare gli Angoli [2]}

La misura di un \emph{angolo} si può esprimere in \textbf{gradi} (°) o in \textbf{radianti}. Inoltre, i gradi possono essere \emph{suddivisi} in \emph{primi} (') e \emph{secondi} (''). In questa sezione illustriamo le principali \emph{unità di misura}, le \emph{conversioni} tra loro e alcune \emph{operazioni} comuni.

\medskip

\noindent
\textbf{1. Gradi e Suddivisioni in Primi e Secondi}

\begin{itemize}
\item L’angolo giro (tutto l’angolo di \(360^\circ\)) si suddivide in \(\,360\) \emph{gradi}.  
\item Ciascun grado (\(^\circ\)) si può dividere in \(\,60\) \emph{primi} (\('\)). Dunque \(1^\circ = 60'\).  
\item Ciascun primo (\('\)) si può dividere in \(\,60\) \emph{secondi} (\(''\)). Quindi \(1' = 60''\).  
\end{itemize}

\noindent
\textbf{Esempi di notazione:}
\begin{itemize}
\item \(25^\circ\,30'\) significa \(25\) gradi e \(30\) primi.  
\item \(17^\circ\,45'\,10''\) indica \(17\) gradi, \(45\) primi, \(10\) secondi.  
\end{itemize}

\noindent
\textbf{Operazioni con gradi, primi, secondi:}  
\begin{enumerate}
\item \emph{Somma}: Ad esempio, per sommare \(13^\circ\,20'\,50''\) e \(2^\circ\,40'\,30''\), si sommano separatamente i gradi, i primi e i secondi, facendo \emph{attenzione} ai riporti (60' = 1° e 60'' = 1'):  
  \[
    (13^\circ + 2^\circ) = 15^\circ,\quad 
    (20' + 40') = 60' = 1^\circ,\quad 
    (50'' + 30'') = 80'' = 1' + 20''.
  \]
  Alla fine si riorganizza tutto, ottenendo \(15^\circ +1^\circ +1' \implies 16^\circ\,1'\,20''.\)
\item \emph{Conversione in gradi decimali}: \(25^\circ\,30' = 25^\circ + \tfrac{30}{60}^\circ=25.5^\circ\).  
\end{enumerate}

\medskip

\noindent
\subsubsection*{I Radianti}

\begin{itemize}
\item Un \emph{angolo giro} in radianti misura \(2\pi\). Di conseguenza, \(180^\circ\) corrisponde a \(\pi\) radianti.  
\item Il \emph{raggiodi} 1 (sul \emph{cerchio goniometrico}) consente di definire il radiante: un \emph{angolo} si dice di \(x\) radianti se \emph{l’arco} sotteso su un cerchio di raggio \(1\) ha lunghezza \(x\).  
\end{itemize}

\noindent
\textbf{Formule di Conversione tra Gradi e Radianti:}
\begin{enumerate}
\item \emph{Da gradi a radianti}: un angolo \(\alpha\) in gradi si trasforma in \(\alpha_{\text{rad}}\) (in radianti) tramite
  \[
    \alpha_{\text{rad}} 
    = \alpha^\circ \times \frac{\pi}{180^\circ}.
  \]
  Esempio: \(30^\circ = 30 \times \frac{\pi}{180} = \frac{\pi}{6}.\)

\item \emph{Da radianti a gradi}: un angolo \(\theta\) in radianti corrisponde a
  \[
    \theta_{\text{deg}}
    = \theta \times \frac{180^\circ}{\pi}.
  \]
  Esempio: \(\tfrac{\pi}{4}\approx 0.7854 \implies 0.7854 \times \tfrac{180}{\pi}\approx 45^\circ.\)
\end{enumerate}


\noindent
\textbf{Quando usare i Gradi e quando i Radianti}

Nella \emph{pratica matematica} e nelle applicazioni, la scelta fra gradi e radianti dipende principalmente dal \emph{contesto}:

\begin{itemize}
\item \textbf{Gradi}: 
  \begin{itemize}
  \item Sono più \emph{intuitivi} nell’uso quotidiano e scolastico, perché suddividono l’angolo giro in \(360^\circ\). Un angolo retto risulta \(90^\circ\), un angolo piatto \(180^\circ\), e così via.
  \item Sono usati spesso in \emph{topografia} tradizionale, in \emph{cartografia}, o quando si descrivono angoli in modo descrittivo (ad esempio, l’angolo di inclinazione di una rampa, l’angolo di un poligono, ecc.).
  \item Offrono un \emph{linguaggio comune} in ambito non strettamente scientifico (ingegneria civile, istruzioni pratiche, ecc.).
  \end{itemize}

\item \textbf{Radianti}: 
  \begin{itemize}
  \item Sono la \emph{scelta privilegiata} in \emph{analisi matematica}, \emph{calcolo infinitesimale}, e in generale quando si trattano \emph{funzioni trigonometriche} e le loro serie, derivate e integrali.  
  \item Rendono le formule più \emph{semplici} e naturali: ad esempio, la derivata di \(\sin x\) è \(\cos x\) solo se \(x\) è misurato in radianti.  
  \item Facilitano l’uso di \emph{identità} come \(\mathrm{e}^{i\theta}=\cos\theta + i\sin\theta\), e permettono di interpretare angoli come \(\theta\) in un’ottica di \emph{misura di archi} (lunghezza dell’arco su cerchio unitario).
  \item Sono \emph{standard} nella fisica avanzata, dove velocità angolari, oscillazioni, e gran parte della trigonometria applicata si esprime in radianti.
  \end{itemize}
\end{itemize}


\subsubsection*{Esempi}
\begin{esempio}

\noindent
\textbf{Problema:} Siano \(\alpha\) e \(\beta\) due angoli (in gradi) tali che
\[
\alpha + \beta = 120^\circ,
\quad
\alpha - \beta = 30^\circ.
\]
Determinare i valori di \(\alpha\) e \(\beta\).

\smallskip
\textbf{Soluzione:}
\begin{enumerate}
\item Impostiamo il sistema:
  \[
    \begin{cases}
    \alpha + \beta = 120^\circ,\\
    \alpha - \beta = 30^\circ.
    \end{cases}
  \]
\item Sommiamo le due equazioni: \((\alpha + \beta)+(\alpha - \beta)=120^\circ + 30^\circ\). Otteniamo
  \(\,2\alpha=150^\circ\implies \alpha=75^\circ.\)
\item Sostituiamo \(\alpha=75^\circ\) in \(\alpha + \beta=120^\circ\). Quindi
  \[
    75^\circ + \beta = 120^\circ
    \quad\Longrightarrow\quad
    \beta=45^\circ.
  \]
\item \textbf{Conclusione:} \(\alpha=75^\circ\), \(\beta=45^\circ\).  
\end{enumerate}
\end{esempio}

\bigskip

\begin{esempio}

\noindent
\textbf{Problema:} Siano \(\alpha\) e \(\beta\) due angoli (in gradi) tali che
\[
\begin{cases}
\alpha + 2\beta = 210^\circ,\\
\alpha - \beta = 30^\circ,\\
\alpha, \beta > 0.
\end{cases}
\]
Determinare i valori di \(\alpha\) e \(\beta\).

\smallskip
\textbf{Soluzione:}
\begin{enumerate}
\item Dalle due equazioni, costruiamo il sistema:
  \[
    \begin{cases}
    \alpha + 2\beta = 210^\circ,\\
    \alpha - \beta = 30^\circ.
    \end{cases}
  \]
\item Dalla seconda, \(\alpha= \beta + 30^\circ\). Sostituiamo nella prima:
  \[
    (\beta + 30^\circ) + 2\beta = 210^\circ
    \quad\Longrightarrow\quad
    3\beta + 30^\circ = 210^\circ
    \quad\Longrightarrow\quad
    3\beta=180^\circ
    \quad\Longrightarrow\quad
    \beta=60^\circ.
  \]
\item Quindi \(\alpha= \beta + 30^\circ=60^\circ + 30^\circ=90^\circ\).
\item Verifichiamo \(\alpha,\beta>0\). Sono \(\alpha=90^\circ\) e \(\beta=60^\circ\), entrambe positive.  
\item \textbf{Conclusione:} \(\alpha=90^\circ\), \(\beta=60^\circ\).  
\end{enumerate}
\end{esempio}

\bigskip

\begin{esempio}

\noindent
\textbf{Problema:} Siano \(\theta\) un angolo in \emph{radianti} e \(\gamma\) un angolo in \emph{gradi}. Si sa che
\[
\theta + \gamma 
= \frac{5\pi}{6}
\quad(\text{radianti}),
\quad
\theta - \gamma 
= \frac{\pi}{6}
\quad(\text{radianti}),
\]
e inoltre \(\gamma\) è convertibile in radianti con la formula 
\(\gamma^\text{(rad)} = \dfrac{\pi}{180^\circ}\,\gamma^\text{(deg)}\). Trovare i valori numerici di \(\theta\) (in radianti) e \(\gamma\) (in gradi).

\smallskip
\textbf{Soluzione:}
\begin{enumerate}
\item Poiché \(\gamma\) è in gradi, definiamo \(\gamma^\text{(rad)}=\dfrac{\pi}{180}\,\gamma\). Le equazioni
  \[
    \theta + \gamma^\text{(rad)} = \frac{5\pi}{6},
    \quad
    \theta - \gamma^\text{(rad)} = \frac{\pi}{6}
  \]
  sono \emph{entrambe} in radianti.  
\item Poniamo \(x=\theta\) (in radianti) e \(y=\gamma^\text{(rad)}\). Il sistema diventa
  \[
    \begin{cases}
    x + y = \tfrac{5\pi}{6},\\
    x - y = \tfrac{\pi}{6}.
    \end{cases}
  \]
\item Sommiamo le due equazioni: \((x+y)+(x-y)= \tfrac{5\pi}{6} + \tfrac{\pi}{6}\). Dunque \(2x= \tfrac{6\pi}{6}= \pi\). Quindi \(x= \tfrac{\pi}{2}\).  
\item Sostituiamo \(x= \tfrac{\pi}{2}\) in \(x+y= \tfrac{5\pi}{6}\). Otteniamo \( \tfrac{\pi}{2}+ y= \tfrac{5\pi}{6}\implies y= \tfrac{5\pi}{6}- \tfrac{\pi}{2}= \tfrac{5\pi}{6}- \tfrac{3\pi}{6}= \tfrac{2\pi}{6}= \tfrac{\pi}{3}.\)
\item Ricordiamo \(y= \gamma^\text{(rad)}= \dfrac{\pi}{180}\,\gamma\). Quindi 
  \[
    \dfrac{\pi}{180}\,\gamma= \tfrac{\pi}{3}
    \quad\Longrightarrow\quad
    \gamma= \tfrac{\pi/3}{\,\pi/180\,}
    = \tfrac{\pi/3}{1}\times \tfrac{180}{\pi}
    = \tfrac{180}{3}
    = 60^\circ.
  \]
\item \textbf{Conclusione}: \(\theta= x= \tfrac{\pi}{2}\) (cioè \(90^\circ\)) e \(\gamma=60^\circ\).  
\end{enumerate}
\end{esempio}



\subsec{Funzioni Goniometriche [1, 2, 3]} %Radianti

Le equazioni goniometriche sono fondamentali per descrivere i rapporti tra gli angoli e le lunghezze in un triangolo rettangolo. In un triangolo rettangolo, il \textit{seno} di un angolo \(\theta\) è definito come il rapporto tra la lunghezza del cateto opposto a \(\theta\) e l'ipotenusa, mentre il \textit{coseno} è il rapporto tra la lunghezza del cateto adiacente a \(\theta\) e l'ipotenusa. Queste definizioni permettono di estendere il concetto di seno e coseno ad angoli di qualsiasi misura. Da queste definizioni derivano anche le altre funzioni goniometriche:
\[
\tan\theta=\frac{\sin\theta}{\cos\theta},\quad \sec\theta=\frac{1}{\cos\theta},\quad \csc\theta=\frac{1}{\sin\theta}.
\]

\paragraph{Grafici di \(\sin(x)\) e \(\cos(x)\)}
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

\subsubsection*{Esagono Trigonometrico}

Il diagramma seguente rappresenta un esagono trigonometrico, uno strumento mnemonico per mostrare le relazioni fondamentali tra le sei funzioni trigonometriche: \(\sin\), \(\cos\), \(\tan\), \(\cot\), \(\sec\) e \(\csc\). Al centro dell’esagono è presente il valore \(1\). Ogni vertice corrisponde a una delle funzioni, mentre le connessioni indicano importanti identità, come quelle di reciprocità e di quoziente.

\begin{center}
\begin{tikzpicture}[>=latex,scale=2,line cap=round,line join=round]
    % Coordinate dei vertici di un esagono regolare
    \coordinate (A) at (60:1);   % sin
    \coordinate (B) at (0:1);    % cos
    \coordinate (C) at (300:1);  % cot
    \coordinate (D) at (240:1);  % csc
    \coordinate (E) at (180:1);  % sec
    \coordinate (F) at (120:1);  % tan

    % Disegno dell'esagono esterno
    \draw (A) -- (B) -- (C) -- (D) -- (E) -- (F) -- cycle;

    % Centro
    \coordinate (O) at (0,0);

    % Collegamenti dal centro ai vertici
    \draw (A) -- (O) -- (B);
    \draw (C) -- (O) -- (D);
    \draw (E) -- (O) -- (F);

    % Etichette dei vertici
    \node at ($(A)+(0,0.2)$) {\(\sin\)};
    \node at ($(B)+(0.2,0)$) {\(\cos\)};
    \node at ($(C)+(0.2,-0.2)$) {\(\cot\)};
    \node at ($(D)+(-0.2,-0.2)$) {\(\csc\)};
    \node at ($(E)+(-0.2,0)$) {\(\sec\)};
    \node at ($(F)+(0,0.2)$) {\(\tan\)};

\end{tikzpicture}
\end{center}

\subsubsection*{Spiegazione delle Caratteristiche Principali}

\begin{enumerate}
    \item I vertici opposti corrispondono a funzioni reciproche:
    \[
    \sin(x) = \frac{1}{\csc(x)}, 
    \quad \cos(x) = \frac{1}{\sec(x)}, 
    \quad \tan(x) = \frac{1}{\cot(x)}.
    \]
    
    \item I vertici adiacenti suggeriscono identità di quoziente, ad esempio:
    \[
    \tan(x) = \frac{\sin(x)}{\cos(x)}, 
    \quad \cot(x) = \frac{\cos(x)}{\sin(x)}.
    \]
    
    \item Il valore \(1\) al centro simboleggia la stretta relazione tra le funzioni e i loro reciproci o quozienti. Questo fornisce una rappresentazione sintetica delle identità trigonometriche di base.
\end{enumerate}
\subsec{Prima Relazione Fondametale \& Dimostrazione [1]}

\begin{theorem}
Per ogni angolo \(\alpha\), vale la relazione
\[
\sin^2(\alpha) + \cos^2(\alpha) = 1.
\]
\end{theorem}

\begin{proof}[dimostrazione]
Consideriamo il \emph{cerchio goniometrico} di raggio \(1\), centrato nell’origine \(O\) del piano cartesiano. Sia \(P\) il punto di intersezione di un raggio \(\overline{OP}\) con la circonferenza, e sia \(\alpha\) l’angolo che \(\overline{OP}\) forma con l’asse \(x\) positivo. Per definizione, le coordinate di \(P\) sono
\[
\bigl(\cos \alpha,\; \sin \alpha\bigr).
\]
Poiché il raggio \(\overline{OP}\) ha lunghezza 1, la distanza dall’origine è:
\[
OP^2 = \cos^2(\alpha) + \sin^2(\alpha) = 1.
\]
Questo conclude la dimostrazione della prima relazione fondamentale. In alternativa, si può considerare un triangolo rettangolo di ipotenusa unitaria, con cateti \(\cos\alpha\) e \(\sin\alpha\); il Teorema di Pitagora fornisce la stessa identica relazione.
\end{proof}

\begin{center}
\begin{tikzpicture}[scale=1.5, line cap=round, line join=round]
  % Cerchio goniometrico (raggio=1)
  \draw[thick] (0,0) circle(1);

  % Assi x e y
  \draw[->] (-1.2,0) -- (1.2,0) node[right] {$x$};
  \draw[->] (0,-1.2) -- (0,1.2) node[above] {$y$};

  % Angolo alpha (in gradi)
  \def\alpha{40}

  % Punto P sul cerchio (cos alpha, sin alpha)
  \coordinate (P) at ({cos(\alpha)},{sin(\alpha)});

  % Raggio OP
  \draw[thick, blue] (0,0) -- (P);

  % Proiezioni su x e y (linee tratteggiate)
  \draw[dashed] (P) -- ({cos(\alpha)},0) coordinate (X);
  \draw[dashed] (X) -- (0,0);

  % Angolo in O
  \draw (0.4,0) arc (0:\alpha:0.4);

  % Punti e testo
  \fill (0,0) circle(0.015) node[below left] {$O$};
  \fill (P) circle(0.015)   node[right] {$P$};
\end{tikzpicture}
\end{center}

\begin{esempio}[]
Consideriamo un triangolo rettangolo \(ABC\) con angolo retto in \(C\). Siano \(AC = 3\), \(BC = 4\) e \(AB = 5\). L’ipotenusa \(AB\) misura dunque 5, mentre i due cateti sono di lunghezze 3 e 4. Se indichiamo con \(\alpha\) l’angolo \(\widehat{CAB}\), si ha:

\[
\sin(\alpha) 
= \frac{\text{cateto opposto}}{\text{ipotenusa}} 
= \frac{AC}{AB}
= \frac{3}{5},
\quad
\cos(\alpha) 
= \frac{\text{cateto adiacente}}{\text{ipotenusa}}
= \frac{BC}{AB}
= \frac{4}{5}.
\]

Per verificare la \emph{prima relazione fondamentale} \(\sin^2\alpha + \cos^2\alpha = 1\), calcoliamo:

\[
\sin^2(\alpha) + \cos^2(\alpha)
= \left(\frac{3}{5}\right)^2 + \left(\frac{4}{5}\right)^2
= \frac{9}{25} + \frac{16}{25}
= \frac{25}{25}
= 1.
\]

Questo esempio concreto mostra come, in un tipico triangolo rettangolo con lati \(3\), \(4\) e \(5\), i valori di \(\sin\alpha\) e \(\cos\alpha\) soddisfino perfettamente la formula \(\sin^2\alpha + \cos^2\alpha = 1\). L’osservazione si basa sulla definizione di seno e coseno come rapporti fra i lati di un triangolo rettangolo.
\end{esempio}

\subsec{Funzioni Trigonometriche di Angoli Noti [1]}
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

\subsec{Dimostrazione di Angoli Noti [1]}

In trigonometria, molti problemi richiedono di conoscere i valori di \(\sin\theta\), \(\cos\theta\) e \(\tan\theta\) per alcuni \emph{angoli notevoli}, come \(0^\circ\), \(30^\circ\), \(45^\circ\), \(60^\circ\), \(90^\circ\), ecc. Questi valori si ricavano in modo geometrico, spesso sfruttando \emph{triangoli speciali} (equilatero, isoscele) o il \emph{cerchio goniometrico}. A partire da \(\sin\theta\) e \(\cos\theta\), si ottengono per estensione anche i valori di \(\tan\theta\), \(\sec\theta\), \(\csc\theta\), \(\cot\theta\), grazie alle relazioni fondamentali della trigonometria (ad esempio \(\tan\theta = \frac{\sin\theta}{\cos\theta}\)).  

Nel seguito, dimostreremo in particolare i valori di \(\sin(60^\circ)\), \(\cos(45^\circ)\), \(\sin(30^\circ)\) e così via, fornendo poi una piccola tabella riassuntiva e spiegando come tali valori costituiscano i mattoni fondamentali per calcoli più complessi.  
\subsubsection*{Valore di \(\sin(30^\circ)\)}

\begin{theorem}
\(\sin(30^\circ) = \tfrac12.\) e $\sin(60^\circ) = $
\end{theorem}

\begin{proof}[dimostrazione]
Consideriamo un triangolo equilatero \(ABC\) di lato \(2\). Tracciamo l’altezza \(CH\), che incontra il lato \(AB\) nel punto \(H\). Poiché il triangolo è equilatero, \(AH = HB = 1\). Il segmento \(CH\) è altezza, mediana e bisettrice dell’angolo \(\widehat{CAB}\), quindi \(\angle CAB = 60^\circ\). Nel triangolo rettangolo \(ACH\), l’ipotenusa \(AC\) è \(2\), il cateto \(AH\) misura \(1\). Per il Teorema di Pitagora si ha:
\[
CH = \sqrt{AC^2 - AH^2} 
= \sqrt{2^2 - 1^2} 
= \sqrt{4 - 1} 
= \sqrt{3}.
\]
Nel \(\triangle ACH\), l’angolo \(\widehat{CAH}\) è \(30^\circ\) (in quanto il triangolo equilatero è stato diviso in due triangoli rettangoli, e \(\angle CAB = 60^\circ\) viene dimezzato). Pertanto,
\[
\sin(30^\circ) = \frac{\text{cateto opposto}}{\text{ipotenusa}}
= \frac{AH}{AC}
= \frac{1}{2}.
\]
\end{proof}

\begin{center}
\begin{tikzpicture}[scale=1.5, line cap=round, line join=round]

  % Triangolo equilatero ABC di lato 2
  \coordinate (A) at (0,0);
  \coordinate (B) at (2,0);
  % C in alto (x=1, y = sqrt(3))
  \coordinate (C) at (1,{sqrt(3)});

  % Disegno ABC
  \draw[thick] (A) -- (B) -- (C) -- cycle;

  % Altezza CH (H e' la proiezione di C su AB)
  \coordinate (H) at (1,0);
  \draw[dashed] (C) -- (H);

  % Etichette vertici
  \node[below left]  at (A) {$A$};
  \node[below right] at (B) {$B$};
  \node[above]       at (C) {$C$};
  \node[below]       at (H) {$H$};


\end{tikzpicture}
\end{center}

\noindent
\textbf{Osservazione:} Abbiamo scelto il lato 2 per ottenere ipotenusa 2 e cateto 1 nel triangolo rettangolo. Ciò rende immediato il calcolo di \(\sin(60^\circ) = \frac{\sqrt{3}}{2}\).

\bigskip

\textbf{Corollari}

\textbf{Derivazione per \(\theta = 30^\circ\) e \(\theta = 60^\circ\):}  
Per un \textit{triangolo equilatero} di lato \(2\), tracciando l’altezza si formano due triangoli rettangoli con cateto \(1\), ipotenusa \(2\) e l’altro cateto \(\sqrt{3}\). L’angolo alla base di ciascun triangolo rettangolo è \(30^\circ\) e l’angolo all’apice è \(60^\circ\). Ne segue:

\[
\sin(30^\circ) = \frac{\text{cateto opposto}}{\text{ipotenusa}} = \frac{1}{2}, 
\quad
\cos(30^\circ) = \frac{\sqrt{3}}{2},
\]
\[
\sin(60^\circ) = \frac{\sqrt{3}}{2}, 
\quad
\cos(60^\circ) = \frac{1}{2}.
\]
Da tali valori, si ottengono anche le funzioni \(\tan\), \(\sec\), \(\csc\), \(\cot\) mediante:
\[
\tan(\theta) = \frac{\sin(\theta)}{\cos(\theta)}, 
\quad
\sec(\theta) = \frac{1}{\cos(\theta)}, 
\quad
\csc(\theta) = \frac{1}{\sin(\theta)},
\quad
\cot(\theta) = \frac{\cos(\theta)}{\sin(\theta)}.
\]

\medskip

\begin{theorem}
\(\sin(90^\circ) = 1\) e \(\cos(90^\circ) = 0.\)
\end{theorem}

\begin{proof}[dimostrazione (cerchio goniometrico)]
Consideriamo il cerchio goniometrico di raggio \(1\) centrato nell’origine \(O\). L’angolo \(90^\circ\) corrisponde a un raggio \(\overline{OP}\) \emph{perpendicolare} all’asse \(x\). Sul piano cartesiano, il punto \(P\) associato all’angolo \(90^\circ\) ha coordinate \((x,y)\) con \(x=0\) e \(y=1\). Questo perché il raggio, essendo diretto verso l’alto, non si sposta orizzontalmente (quindi \(x=0\)), ma raggiunge il margine superiore del cerchio (dove \(y=1\)).

Di conseguenza,
\[
\cos(90^\circ) = x = 0,
\quad
\sin(90^\circ) = y = 1.
\]
\end{proof}

\begin{center}
\begin{tikzpicture}[scale=1.5, line cap=round, line join=round]

  % Cerchio goniometrico
  \draw[thick] (0,0) circle(1);

  % Assi x e y
  \draw[->] (-1.2,0) -- (1.2,0) node[right] {$x$};
  \draw[->] (0,-1.2) -- (0,1.2) node[above] {$y$};

  % Punto P su cerchio per alpha = 90°
  \coordinate (P) at (0,1.2);

  % Raggio OP
  \draw[thick, blue] (0,0) -- (P);

  % Punti e coordinate
  \fill (0,0) circle(0.015) node[below left] {$O$};
  \fill (P) circle(0.015)   node[left] {$P$};


  % Angolo di 90°, disegnato come un arco a sinistra
  \draw (0.3,0) arc (0:90:0.3);
  \node at (45:0.50) {$90^\circ$};

\end{tikzpicture}
\end{center}

\noindent
\textbf{Osservazione:}  
L’angolo \(90^\circ\) (o \(\tfrac{\pi}{2}\) in radianti) sposta il punto sul cerchio goniometrico esattamente in alto, dove la coordinata \(x\) si annulla e la coordinata \(y\) vale 1. Da qui si deduce \(\cos(90^\circ)=0\) e \(\sin(90^\circ)=1\). 

\subsubsection*{Determinazione di \(\sin(18^\circ)\) con il decagono e la sezione aurea}

\begin{theorem}
\(\displaystyle \sin(18^\circ) \;=\; \frac{\sqrt{5} - 1}{4}.\)
\end{theorem}

\begin{proof}[dimostrazione]
Si consideri un \emph{decagono regolare} di lato 1, inscritto in una circonferenza di centro \(O\). L’angolo al centro sotteso da ogni lato è \(36^\circ\). Se \(A\) e \(B\) sono due vertici consecutivi del decagono, il segmento \(\overline{AB}\) ha lunghezza 1. se \(C\) è il vertice successivo a \(B\), l’angolo \(\widehat{AOB}\) vale \(36^\circ\), mentre \(\widehat{AOC}\) vale \(72^\circ\). 

Se suddividiamo l’intera circonferenza (che misura \(360^\circ\)) in 10 archi uguali, ciascun arco corrispondente a un lato del decagono sottende al centro un angolo di
\[
\frac{360^\circ}{10} = 36^\circ.
\]
Se \(A\) e \(B\) sono due vertici consecutivi del decagono, il segmento \(\overline{AB}\) è uno di questi lati; di conseguenza, l’angolo \(\widehat{AOB}\) formato dai raggi \(\overline{OA}\) e \(\overline{OB}\) è esattamente \(36^\circ\). Se \(C\) è il vertice immediatamente successivo a \(B\), allora la sequenza \(A \to B \to C\) percorre due lati consecutivi, cioè due archi da \(36^\circ\) ciascuno. Perciò l’angolo \(\widehat{AOC}\) risulta
\[
36^\circ + 36^\circ = 72^\circ.
\]

\begin{center}
\begin{tikzpicture}[scale=1.5, line cap=round, line join=round]

% Raggio R in modo che il lato del decagono regolare inscritto sia 1
% Per un decagono, il lato = 2*R*sin(π/10).
% Se vogliamo lato=1, allora R = 1/(2 sin(18°)).
\pgfmathsetmacro{\R}{1/(2*sin(18))}  % sin(18) in radianti => 18*pi/180 = pi/10

% Centro O
\coordinate (O) at (0,0);

% Disegno del cerchio di centro O e raggio R
\draw[thick] (O) circle (\R);

% DEFINIZIONE MANUALE DEI VERTICI DEL DECAGONO
% Angolo al centro = 36° (π/5), 
% Partiamo dall'alto (90°) e scendiamo a incrementi di 36°.
% In un disegno "a mano" li scriviamo uno a uno.
\coordinate (P0) at ({\R*cos(90)} , {\R*sin(90)});
\coordinate (P1) at ({\R*cos(54)} , {\R*sin(54)});
\coordinate (P2) at ({\R*cos(18)} , {\R*sin(18)});
\coordinate (P3) at ({\R*cos(-18)}, {\R*sin(-18)});
\coordinate (P4) at ({\R*cos(-54)}, {\R*sin(-54)});
\coordinate (P5) at ({\R*cos(-90)}, {\R*sin(-90)});
\coordinate (P6) at ({\R*cos(-126)}, {\R*sin(-126)});
\coordinate (P7) at ({\R*cos(-162)}, {\R*sin(-162)});
\coordinate (P8) at ({\R*cos(  162)}, {\R*sin( 162)});
\coordinate (P9) at ({\R*cos(  126)}, {\R*sin( 126)});

% COLLEGHIAMO I VERTICI CON SEGMENTI PER FORMARE IL DECAGONO
\draw[thick] (P0) -- (P1) -- (P2) -- (P3) -- (P4) -- (P5) -- (P6) -- (P7) -- (P8) -- (P9) -- cycle;

% NOMINIAMO TRE VERTICI CONSECUTIVI: A=P0, B=P1, C=P2
\node[above]       at (P0) {$A$};
\node[right]       at (P1) {$B$};
\node[below right] at (P2) {$C$};

\draw[thick, dashed] (O) -- (P0);
\draw[thick, dashed] (O) -- (P1);
\draw[thick, dashed] (O) -- (P2);

% ETICHETTA IL CENTRO
\fill (O) circle(0.01) node[below left] {$O$};

% Disegno di segmenti speciali: AB e BC (lati consecutivi), AC (prossimo vertice)
% (Abbiamo già disegnato tutti i lati con la "cycle", ma li evidenziamo se vogliamo)
% \draw[line width=1pt,blue] (P0)--(P1)--(P2);

% Mostriamo l'angolo AOB = 36° e l'angolo AOC = 72°:
% Disegno di due archi in O

\draw[->] (0.4,0) arc[start angle=0, delta angle=72, radius=0.4];
\node at (36:0.55) {\small $72^\circ$};

\end{tikzpicture}
\end{center}

Tracciando la diagonale \(\overline{AC}\) che “salta” un vertice del decagono (ciò corrisponde a un arco di \(72^\circ\) anziché \(36^\circ\)), si confronta la sua lunghezza con quella del lato \(\overline{AB}\). Il lato, in quanto corda sottesa da \(36^\circ\), misura \(2R \sin(18^\circ)\), mentre la diagonale, come corda sottesa da \(72^\circ\), misura \(2R \sin(36^\circ)\). Dividendo la lunghezza della diagonale per quella del lato, si ottiene
\[
\frac{2R \,\sin(36^\circ)}{2R \,\sin(18^\circ)} \;=\; \frac{\sin(36^\circ)}{\sin(18^\circ)}.
\]
Dopo aver stabilito che il lato di un decagono regolare (di raggio \(R\)) misura \(2R \,\sin(18^\circ)\) e la diagonale “che salta un vertice” misura \(2R \,\sin(36^\circ)\), il rapporto fra diagonale e lato è
\[
\frac{2R \,\sin(36^\circ)}{2R \,\sin(18^\circ)} 
\;=\; \frac{\sin(36^\circ)}{\sin(18^\circ)}.
\]
Usando le identità trigonometriche relative agli angoli \(36^\circ\) e \(72^\circ\), si verifica che
\[
\frac{\sin(36^\circ)}{\sin(18^\circ)} 
= \frac{1 + \sqrt{5}}{2}
= \varphi.
\]
In questo modo, si dimostra che la diagonale \(\overline{AC}\) e il lato \(\overline{AB}\) di un decagono regolare sono in \emph{rapporto aureo}. 

In particolare, in uno di questi triangoli isosceli con base 1 e lati (diagonali) congruenti, l’angolo al centro corrispondente è \(36^\circ\), mentre la bisettrice interna di tale angolo crea un angolo di \(18^\circ\). 

\begin{center}
\begin{tikzpicture}[scale=1.5, line cap=round, line join=round]

% Raggio R in modo che il lato del decagono regolare inscritto sia 1
% Per un decagono, il lato = 2*R*sin(π/10).
% Se vogliamo lato=1, allora R = 1/(2 sin(18°)).
\pgfmathsetmacro{\R}{1/(2*sin(18))}  % sin(18) in radianti => 18*pi/180 = pi/10

% Centro O
\coordinate (O) at (0,0);

% Disegno del cerchio di centro O e raggio R
\draw[thick] (O) circle (\R);

% DEFINIZIONE MANUALE DEI VERTICI DEL DECAGONO
% Angolo al centro = 36° (π/5), 
% Partiamo dall'alto (90°) e scendiamo a incrementi di 36°.
% In un disegno "a mano" li scriviamo uno a uno.
\coordinate (P0) at ({\R*cos(90)} , {\R*sin(90)});
\coordinate (P1) at ({\R*cos(54)} , {\R*sin(54)});
\coordinate (P2) at ({\R*cos(18)} , {\R*sin(18)});
\coordinate (P3) at ({\R*cos(-18)}, {\R*sin(-18)});
\coordinate (P4) at ({\R*cos(-54)}, {\R*sin(-54)});
\coordinate (P5) at ({\R*cos(-90)}, {\R*sin(-90)});
\coordinate (P6) at ({\R*cos(-126)}, {\R*sin(-126)});
\coordinate (P7) at ({\R*cos(-162)}, {\R*sin(-162)});
\coordinate (P8) at ({\R*cos(  162)}, {\R*sin( 162)});
\coordinate (P9) at ({\R*cos(  126)}, {\R*sin( 126)});

% COLLEGHIAMO I VERTICI CON SEGMENTI PER FORMARE IL DECAGONO
\draw[thick] (P0) -- (P1) -- (P2) -- (P3) -- (P4) -- (P5) -- (P6) -- (P7) -- (P8) -- (P9) -- cycle;

% NOMINIAMO TRE VERTICI CONSECUTIVI: A=P0, B=P1, C=P2
\node[above]       at (P0) {$A$};
\node[right]       at (P1) {$B$};
\node[below right] at (P2) {$C$};

% Prima, riempiamo il triangolo in blu trasparente
\fill[blue!20] (O) -- (P0) -- (P2) -- cycle;

% Poi disegniamo i segmenti desiderati
\draw[thick] (O) -- (P0);
\draw[thick, dashed, red] (O) -- (P1);
\draw[thick] (O) -- (P2);
\draw[thick] (P0) -- (P2);

% ETICHETTA IL CENTRO
\fill (O) circle(0.01) node[below left] {$O$};

% Disegno di segmenti speciali: AB e BC (lati consecutivi), AC (prossimo vertice)
% (Abbiamo già disegnato tutti i lati con la "cycle", ma li evidenziamo se vogliamo)
% \draw[line width=1pt,blue] (P0)--(P1)--(P2);

% Mostriamo l'angolo AOB = 36° e l'angolo AOC = 72°:
% Disegno di due archi in O

\draw[->] (0.4,0) arc[start angle=0, delta angle=72, radius=0.4];
\node at (36:0.55) {\small $72^\circ$};

\end{tikzpicture}
\end{center}

Da questa configurazione scaturisce un’equazione trigonometrica che coinvolge \(\cos(36^\circ)\) e \(\sin(18^\circ)\). Usando le note relazioni di \emph{similitudine} e il fatto che \(\cos(36^\circ)\) si esprime in termini di \(\varphi\), si giunge a
\[
\sin(18^\circ) = \frac{\sqrt{5}-1}{4}.
\]
L’aspetto cruciale è che il decagono regolare, con la sua ricca geometria, fornisce un legame fra la lunghezza del lato, le diagonali, e la costante \(\varphi\), rendendo esplicito come l’angolo di \(18^\circ\) compaia naturalmente associato alla \emph{sezione aurea}.
\end{proof}

\noindent
\textbf{Conclusione:}  
Il valore \(\sin(18^\circ) = \tfrac{\sqrt{5}-1}{4}\) si ottiene dall’analisi geometrica del decagono regolare o, equivalentemente, da un triangolo isoscele con vertice di \(36^\circ\) e bisettrice che crea l’angolo \(18^\circ\). Questa costruzione lega la trigonometria alla \emph{sezione aurea}, una costante geometrica notevole.

\subsubsection*{Tabella Riassuntiva}


\renewcommand{\arraystretch}{1.8}
\begin{center}
\begin{tabular}{c|cccccc}
\hline
\(\theta\) 
& \(\sin\theta\) 
& \(\cos\theta\) 
& \(\tan\theta\) 
& \(\sec\theta\) 
& \(\csc\theta\) 
& \(\cot\theta\) \\
\hline
\(0^\circ\)
& \(0\)
& \(1\)
& \(0\)
& \(1\)
& \(\text{non definita}\)
& \(\text{non definita}\) \\
\hline
\(18^\circ\)
& \(\displaystyle \frac{\sqrt{5}-1}{4}\)
& \(\displaystyle \frac{\sqrt{10+2\sqrt{5}}}{4}\)
& \(\displaystyle \frac{\sqrt{5}-1}{\sqrt{10+2\sqrt{5}}}\)
& \(\displaystyle \frac{4}{\sqrt{10+2\sqrt{5}}}\)
& \(\displaystyle \frac{4}{\sqrt{5}-1}\)
& \(\displaystyle \frac{\sqrt{10+2\sqrt{5}}}{\sqrt{5}-1}\) \\
\hline
\(30^\circ\)
& \(\displaystyle \frac12\)
& \(\displaystyle \frac{\sqrt{3}}{2}\)
& \(\displaystyle \frac{1}{\sqrt{3}}\)
& \(\displaystyle \frac{2}{\sqrt{3}}\)
& \(\displaystyle 2\)
& \(\displaystyle \sqrt{3}\) \\
\hline
\(36^\circ\)
& \(\displaystyle \frac{\sqrt{10 - 2\sqrt{5}}}{4}\)
& \(\displaystyle \frac{\sqrt{5}+1}{4}\)
& \(\displaystyle \frac{\sqrt{10 - 2\sqrt{5}}}{\sqrt{5}+1}\)
& \(\displaystyle \frac{4}{\sqrt{5}+1}\)
& \(\displaystyle \frac{4}{\sqrt{10 - 2\sqrt{5}}}\)
& \(\displaystyle \frac{\sqrt{5}+1}{\sqrt{10 - 2\sqrt{5}}}\) \\
\hline
\(45^\circ\)
& \(\displaystyle \frac{\sqrt{2}}{2}\)
& \(\displaystyle \frac{\sqrt{2}}{2}\)
& \(1\)
& \(\displaystyle \sqrt{2}\)
& \(\displaystyle \sqrt{2}\)
& \(1\) \\
\hline
\(60^\circ\)
& \(\displaystyle \frac{\sqrt{3}}{2}\)
& \(\displaystyle \frac12\)
& \(\displaystyle \sqrt{3}\)
& \(\displaystyle 2\)
& \(\displaystyle \frac{2}{\sqrt{3}}\)
& \(\displaystyle \frac{1}{\sqrt{3}}\) \\
\hline
\(90^\circ\)
& \(1\)
& \(0\)
& \(\text{non definita}\)
& \(\text{non definita}\)
& \(1\)
& \(0\) \\
\hline
\(180^\circ\)
& \(0\)
& \(-1\)
& \(0\)
& \(-1\)
& \(\text{non definita}\)
& \(\text{non definita}\) \\
\hline
\(270^\circ\)
& \(-1\)
& \(0\)
& \(\text{non definita}\)
& \(\text{non definita}\)
& \(-1\)
& \(0\) \\
\hline
\end{tabular}
\end{center}
\renewcommand{\arraystretch}{1.0}

\noindent
\textbf{Osservazione:} Questi valori costituiscono i \emph{mattoni fondamentali} per la trigonometria degli angoli più comuni. Altri angoli notevoli (ad esempio \(120^\circ, 135^\circ, 150^\circ\), ecc.) si ricavano sfruttando le \emph{simmetrie} (angoli supplementari e complementari) e le \emph{formule di addizione} (\(\sin(\theta \pm \phi)\), \(\cos(\theta \pm \phi)\)). I valori di \(\tan, \sec, \csc, \cot\) seguono dalle definizioni e dalle identità fondamentali come \(\sin^2\theta + \cos^2\theta = 1\). 

\subsubsection*{Esempi di calcolo con gli angoli noti}

\begin{esempio}[Calcolo di \(\cos(18^\circ)\)]
Abbiamo stabilito che \(\sin(18^\circ) = \tfrac{\sqrt{5}-1}{4}\). Dalla \emph{prima relazione fondamentale} \(\sin^2\theta + \cos^2\theta = 1\), segue
\[
\cos^2(18^\circ) = 1 - \sin^2(18^\circ)
= 1 - \Bigl(\tfrac{\sqrt{5}-1}{4}\Bigr)^2
= 1 - \frac{(\sqrt{5}-1)^2}{16}
\]
\[
= 1 - \frac{5 - 2\sqrt{5} + 1}{16}
= 1 - \frac{6 - 2\sqrt{5}}{16}
= 1 - \frac{3 - \sqrt{5}}{8}.
\]
Semplificando, si trova
\[
\cos^2(18^\circ) 
= \frac{8 - (3 - \sqrt{5})}{8}
= \frac{5 + \sqrt{5}}{8}.
\]
Poiché \(18^\circ\) è un angolo acuto, \(\cos(18^\circ)\) è positivo, dunque
\[
\cos(18^\circ) 
= \sqrt{\frac{5 + \sqrt{5}}{8}}
= \frac{\sqrt{10 + 2\sqrt{5}}}{4}.
\]
\end{esempio}

\begin{esempio}[Calcolo di \(\tan(36^\circ)\)]
L’angolo \(36^\circ\) compare naturalmente nel decagono regolare e si collega a \(\sin(36^\circ)\) e \(\cos(36^\circ)\). In particolare, \(\sin(36^\circ) = \tfrac{\sqrt{10 - 2\sqrt{5}}}{4}\) e \(\cos(36^\circ) = \tfrac{\sqrt{5}+1}{4}\). La tangente è definita come
\[
\tan(36^\circ) 
= \frac{\sin(36^\circ)}{\cos(36^\circ)}
= \frac{\tfrac{\sqrt{10 - 2\sqrt{5}}}{4}}{\tfrac{\sqrt{5}+1}{4}}
= \frac{\sqrt{10 - 2\sqrt{5}}}{\sqrt{5}+1}.
\]
Semplificando (ad esempio, moltiplicando numeratore e denominatore per \(\sqrt{5}-1\)), si può ottenere un’espressione più “radicale” senza somma nel denominatore. Tuttavia, già questa forma evidenzia la stretta relazione con la sezione aurea.
\end{esempio}

\begin{esempio}[Calcolo di \(\cot(180^\circ)\)]
La cotangente di un angolo \(\theta\) è definita come
\[
\cot(\theta) = \frac{\cos(\theta)}{\sin(\theta)}
= \frac{1}{\tan(\theta)}.
\]
Nel caso \(\theta = 180^\circ\), abbiamo \(\sin(180^\circ) = 0\) e \(\cos(180^\circ) = -1\). Poiché \(\sin(180^\circ) = 0\), il denominatore in \(\tfrac{\cos(\theta)}{\sin(\theta)}\) diventa zero, rendendo \(\cot(180^\circ)\) \emph{non definita}. In pratica, non esiste un valore finito per la cotangente di un angolo in cui \(\sin\theta = 0\).
\end{esempio}

\begin{esempio}[Calcolo di \(\sin(15^\circ)\) come esempio più complesso]
Per determinare \(\sin(15^\circ)\) possiamo usare la \emph{formula di differenza} degli angoli:
\[
15^\circ = 45^\circ \;-\; 30^\circ.
\]
Ricordiamo che
\[
\sin(\alpha - \beta)
= \sin\alpha \cos\beta - \cos\alpha \sin\beta.
\]
Ponendo \(\alpha = 45^\circ\) e \(\beta = 30^\circ\), otteniamo
\[
\sin(15^\circ)
= \sin(45^\circ)\cos(30^\circ) \;-\;\cos(45^\circ)\sin(30^\circ).
\]
Sostituiamo i valori noti:
\[
\sin(45^\circ) = \frac{\sqrt{2}}{2}, 
\quad
\cos(45^\circ) = \frac{\sqrt{2}}{2}, 
\quad
\cos(30^\circ) = \frac{\sqrt{3}}{2}, 
\quad
\sin(30^\circ) = \frac12.
\]
Calcolando,
\[
\sin(15^\circ)
= \Bigl(\tfrac{\sqrt{2}}{2}\Bigr)\Bigl(\tfrac{\sqrt{3}}{2}\Bigr)
-\Bigl(\tfrac{\sqrt{2}}{2}\Bigr)\Bigl(\tfrac12\Bigr)
= \frac{\sqrt{6}}{4} - \frac{\sqrt{2}}{4}
= \frac{\sqrt{6} - \sqrt{2}}{4}.
\]
Questo valore è più complesso rispetto a quelli degli angoli \(30^\circ\), \(45^\circ\), \(60^\circ\), ma si ricava comunque dalle \emph{identità di somma e differenza} e dai valori noti delle funzioni trigonometriche.
\end{esempio}

\subsec{Formule di Addizione e Duplicazione [2]} %piu approfondito di 15 - 17

\subsubsection*{Calcolo della lunghezza di un arco dato un angolo al centro}

\textbf{Introduzione:}  
In un cerchio di raggio \(R\), la lunghezza di un arco dipende dall’angolo al centro che lo sottende. Se l’angolo al centro è misurato in \emph{radianti}, la formula più diretta è
\[
\text{lunghezza dell’arco} 
= R \cdot \theta,
\]
dove \(\theta\) è l’angolo in radianti. Se invece \(\theta\) è espresso in \emph{gradi}, la formula diventa
\[
\text{lunghezza dell’arco} 
= \frac{\theta}{360^\circ} \times 2\pi R.
\]
Spieghiamo perché, usando un ragionamento di proporzioni.

\begin{theorem}
Se un arco di cerchio corrisponde a un angolo al centro \(\theta\), la sua lunghezza è 
\[
\text{arco} = \frac{\theta}{360^\circ} \times (2\pi R),
\]
quando \(\theta\) è in gradi, e 
\(\text{arco} = R \,\theta\) quando \(\theta\) è in radianti.
\end{theorem}

\begin{proof}[dimostrazione con le proporzioni]
Consideriamo un cerchio di raggio \(R\). L’intera circonferenza misura \(2\pi R\). Un angolo al centro di \(360^\circ\) (cioè un giro completo) sottende tutta la circonferenza, perciò \(360^\circ \leftrightarrow 2\pi R\). Se un angolo al centro è \(\theta\) (in gradi), esso è una frazione \(\tfrac{\theta}{360^\circ}\) dell’angolo giro, e di conseguenza sottende la stessa frazione della circonferenza. In simboli:
\[
\frac{\text{arco}}{2\pi R}
= \frac{\theta}{360^\circ}
\quad\Longrightarrow\quad
\text{arco} 
= \frac{\theta}{360^\circ}\,\times 2\pi R.
\]
Se invece \(\theta\) è espresso in radianti, ricordiamo che \(2\pi\) radianti corrispondono all’intera circonferenza. Un angolo al centro di \(\theta\) radianti rappresenta la frazione \(\tfrac{\theta}{2\pi}\) della circonferenza, quindi
\[
\frac{\text{arco}}{2\pi R}
= \frac{\theta}{2\pi}
\quad\Longrightarrow\quad
\text{arco} 
= R \,\theta.
\]
Questo conclude la dimostrazione, evidenziando che la lunghezza dell’arco si ottiene per proporzione rispetto all’angolo giro (in gradi o in radianti).
\end{proof}

\begin{center}
\begin{tikzpicture}[scale=1.2, line cap=round, line join=round]

  % Raggio R
  \def\R{2}

  % Angolo in gradi
  \def\ang{60} % Esempio di 60°

  % Cerchio di centro O
  \coordinate (O) at (0,0);
  \draw[thick] (O) circle(\R);

  % Punto A in direzione 0°, B in direzione \ang
  \coordinate (A) at (\R,0);
  \coordinate (B) at ({\R*cos(\ang)},{\R*sin(\ang)});

  % Disegno dei raggi OA e OB
  \draw[thick] (O) -- (A) node[midway, below] {};
  \draw[thick] (O) -- (B) node[midway, sloped, above] {};

  % Arco AB
  \draw[blue, thick] 
    let \p1 = (A), \p2=(B) in 
    plot[domain=0:\ang] 
    ({\R*cos(\x)},{\R*sin(\x)});

  % Angolo al centro
  \draw (0.4,0) arc[start angle=0, delta angle=\ang, radius=0.4];
  \node at (\ang/2:0.6) {};

\end{tikzpicture}
\end{center}

\noindent
\textbf{Osservazione:} Se l’angolo al centro è di \(\theta\) gradi, la \emph{frazione} di giro completo è \(\tfrac{\theta}{360^\circ}\). Applicando la stessa frazione alla circonferenza \(2\pi R\), si ottiene la formula \(\tfrac{\theta}{360^\circ}\times 2\pi R\). Quando \(\theta\) è in radianti, l’intero giro è \(2\pi\) radianti, e la porzione \(\tfrac{\theta}{2\pi}\) della circonferenza fornisce la formula \(R\,\theta\). 

\subsubsection*{Formule di addizione degli archi}

\begin{theorem}
Per ogni coppia di angoli \(\alpha\) e \(\beta\), valgono le seguenti identità:
\[
\sin(\alpha + \beta) 
= \sin\alpha \,\cos\beta + \cos\alpha \,\sin\beta,
\quad
\cos(\alpha + \beta) 
= \cos\alpha \,\cos\beta - \sin\alpha \,\sin\beta.
\]
\end{theorem}

\begin{proof}[dimostrazione]
Consideriamo il \emph{cerchio goniometrico} di raggio 1 centrato nell’origine \(O\). Siano \(\alpha\) e \(\beta\) due angoli misurati in senso antiorario rispetto all’asse \(x\). Definiamo tre punti:
\[
P(\cos\alpha,\;\sin\alpha), \quad
Q(\cos\beta,\;\sin\beta), \quad
R(\cos(\alpha+\beta),\;\sin(\alpha+\beta)).
\]
Tali punti appartengono alla circonferenza e corrispondono rispettivamente agli angoli \(\alpha\), \(\beta\) e \(\alpha+\beta\). Tracciamo i segmenti \(\overline{OP}\), \(\overline{OQ}\), \(\overline{OR}\), che hanno tutti lunghezza 1.  

Dal punto di vista geometrico, \(\overline{OP}\) e \(\overline{OQ}\) formano i vettori di estremi \(P\) e \(Q\), e la \emph{composizione} di questi vettori (tramite il \emph{parallelogramma} costruito su \(\overline{OP}\) e \(\overline{OQ}\)) conduce al punto \(R\). Scomponendo i lati orizzontali e verticali in coordinate, si ottengono i termini \(\sin\alpha \,\cos\beta\), \(\cos\alpha \,\sin\beta\), ecc. con segni adeguati.  

La proiezione sui due assi cartesiani (asse \(x\) e asse \(y\)) fa sì che la coordinata orizzontale di \(R\) risulti \(\cos(\alpha + \beta) = \cos\alpha \,\cos\beta - \sin\alpha \,\sin\beta\), mentre la coordinata verticale risulti \(\sin(\alpha + \beta) = \sin\alpha \,\cos\beta + \cos\alpha \,\sin\beta\). In tal modo si ottengono le formule di addizione per seno e coseno.
\end{proof}

\noindent
\begin{minipage}{0.47\textwidth}
\begin{tikzpicture}[scale=1.2, line cap=round, line join=round]

  % Raggio e angoli
  \def\R{2}
  \def\angA{60}  % Primo arco
  \def\angB{30}  % Secondo arco = metà del primo

  % Centro O
  \coordinate (O) at (0,0);

  % Cerchio
  \draw[thick] (O) circle(\R);

  % Punti P (0->angA) e Q (angA->angB)
  \coordinate (P) at (\R,0); 
  \coordinate (Q) at ({\R*cos(\angA)},{\R*sin(\angA)});
  \coordinate (R) at ({\R*cos(\angA+\angB)},{\R*sin(\angA+\angB)});

  % Raggi OP, OQ, OR
  \draw[thick] (O) -- (P);
  \draw[thick] (O) -- (Q);
  \draw[thick, dashed, purple] (O) -- (R);

  % Primo arco (P->Q) in blu
  \draw[blue, thick] plot[domain=0:\angA] 
    ({\R*cos(\x)},{\R*sin(\x)});

  % Secondo arco (Q->R) in red
  \draw[red, thick] plot[domain=\angA:\angA+\angB] 
    ({\R*cos(\x)},{\R*sin(\x)});

\end{tikzpicture}
\end{minipage}
\hfill
\begin{minipage}{0.47\textwidth}
\begin{tikzpicture}[scale=1.9, line cap=round, line join=round]

  % Raggio e angolo
  \def\R{1.3}
  \def\ang{30}

  % Centro O
  \coordinate (O) at (0,0);

  % Cerchio
  \draw[thick] (O) circle(\R);

  % Punti P (angolo 0°) e Q (angolo \ang)
  \coordinate (P) at (\R,0);
  \coordinate (Q) at ({\R*cos(\ang)},{\R*sin(\ang)});

  % Segmenti OP (orizzontale) e OQ (angolo \ang in rosso)
  \draw[thick] (O) -- (P);
  \draw[thick] (O) -- (Q);

  % Arco (0->\ang) in rosso
  \draw[thick, red] (\R,0) arc[start angle=0, delta angle=\ang, radius=\R];

  % Segmento viola che mostra un "seno" (dashed)
  \coordinate (Qx) at ({\R*cos(\ang)},0);
  \draw[violet, thick, dashed] (Q) -- (Qx);

  % Segmento supplementare per la "somma dei seni" (dashed)
  % (Esempio: prolungamento in y di Qx)
  \coordinate (S) at (\R,{ \R*sin(\ang) + 0.5});

\end{tikzpicture}
\end{minipage}

\noindent
\textbf{Osservazione:}  
Nel disegno, i vettori \(\overline{OP}\) e \(\overline{OQ}\) sono lunghi 1 (raggio del cerchio goniometrico). La loro “somma” (costruendo il parallelogramma tratteggiato) conduce al punto \(R\) che rappresenta \(\overline{OR}\). La proiezione orizzontale e verticale fornisce le formule di addizione: \(\sin(\alpha+\beta)\) e \(\cos(\alpha+\beta)\).

\subsubsection*{Formule di duplicazione degli archi}

\begin{theorem}
Per ogni angolo \(\alpha\), valgono le seguenti identità di \emph{duplicazione}:
\[
\sin(2\alpha) = 2\,\sin(\alpha)\cos(\alpha),
\quad
\cos(2\alpha) = \cos^2(\alpha) - \sin^2(\alpha).
\]
\end{theorem}

\begin{proof}[dimostrazione]
Per dimostrare \(\sin(2\alpha) = 2\,\sin(\alpha)\cos(\alpha)\) si può ricorrere alla \emph{formula di addizione} degli archi, applicata a \(\sin(\alpha + \alpha)\). In particolare, poiché
\[
\sin(\alpha + \alpha)
= \sin(\alpha)\cos(\alpha) + \cos(\alpha)\sin(\alpha),
\]
sommando i termini otteniamo
\[
\sin(2\alpha) 
= 2\,\sin(\alpha)\cos(\alpha).
\]
Per dimostrare \(\cos(2\alpha) = \cos^2(\alpha) - \sin^2(\alpha)\), si osserva che dalla formula di addizione
\[
\cos(\alpha + \alpha)
= \cos(\alpha)\cos(\alpha) - \sin(\alpha)\sin(\alpha)
= \cos^2(\alpha) - \sin^2(\alpha).
\]
Così risulta \(\cos(2\alpha) = \cos^2(\alpha) - \sin^2(\alpha)\). In alternativa, si può anche usare la \emph{prima relazione fondamentale} \(\sin^2\theta + \cos^2\theta = 1\) per esprimere una di queste funzioni in termini dell’altra. Ma la derivazione più diretta rimane l’uso delle formule di addizione per \(\sin(\alpha+\beta)\) e \(\cos(\alpha+\beta)\).
\end{proof}

\begin{center}
\begin{tikzpicture}[scale=1.4, line cap=round, line join=round]

  % Disegno per illustrare la duplicazione di un angolo
  % Raggio e definizione
  \def\R{1.3}
  \def\alpha{30} % in gradi, per illustrare

  % Centro O
  \coordinate (O) at (0,0);

  % Cerchio
  \draw[thick] (O) circle(\R);

  % Punti: P corrisponde a alpha, Q a 2alpha
  \coordinate (P) at ({\R*cos(\alpha)},{\R*sin(\alpha)});
  \coordinate (Q) at ({\R*cos(2*\alpha)},{\R*sin(2*\alpha)});

  % Raggi
  \draw[thick] (O) -- (P);
  \draw[thick] (O) -- (Q);
  \draw[thick] (O) -- (\R, 0);

  % Arco da 0 a alpha (blu)
  \draw[blue, thick] plot[domain=0:\alpha] 
    ({\R*cos(\x)},{\R*sin(\x)});
  % Arco da alpha a 2alpha (rosso)
  \draw[red, thick] plot[domain=\alpha:2*\alpha] 
    ({\R*cos(\x)},{\R*sin(\x)});

  % Etichette
  \fill (O) circle(0.015) node[below left] {$O$};
  \fill (P) circle(0.015) node[right] {$P$};
  \fill (Q) circle(0.015) node[above] {$Q$};

  % Archi per alpha e 2alpha
  \draw (0.3,0) arc[start angle=0, delta angle=\alpha, radius=0.3];

  % Arco piu' grande (disegno offset in radius)
  \draw (0.5,0) arc[start angle=0, delta angle=2*\alpha, radius=0.5];

\end{tikzpicture}
\end{center}

\noindent
\textbf{Osservazione:} Nella figura, l’angolo \(\alpha\) corrisponde al raggio \(\overline{OP}\), mentre \(\overline{OQ}\) rappresenta \(2\alpha\). L’arco \(\widehat{OP}\) in blu è \(\alpha\), e l’arco \(\widehat{PQ}\) in rosso mostra il secondo “pezzo” di angolo fino a \(2\alpha\). Le \emph{formule di duplicazione} permettono di calcolare rapidamente \(\sin(2\alpha)\) e \(\cos(2\alpha)\) se si conoscono \(\sin(\alpha)\) e \(\cos(\alpha)\). 

\subsec{Teoremi sul Triangolo \& Dimostrazioni [3]}
Oltre ai Teoremi di Pitagora ed Euclide (che verranno discussi separatamente), esistono altri risultati fondamentali riguardanti i triangoli, i quali ci forniranno un quadro più completo della geometria di queste figure. Di seguito, presentiamo alcuni di tali risultati.

\begin{theorem}
In ogni triangolo, la somma dei tre angoli interni è \(180^\circ\).
\end{theorem}

\begin{proof}[dimostrazione]
Consideriamo un triangolo \(ABC\). Sia \(\ell\) la retta passante per \(C\) e parallela al lato \(\overline{AB}\). Tracciamo \(\ell\) in modo che \(C\) sia compreso fra le sue semirette.

\begin{center}
\begin{tikzpicture}[scale=1.0, line cap=round, line join=round]

  % Vertici del triangolo
  \coordinate (A) at (0,0);
  \coordinate (B) at (4,0);
  \coordinate (C) at (2,2);

  % Disegno del triangolo ABC
  \draw[thick] (A) -- (B) -- (C) -- cycle;

  % Retta l parallela ad AB, passante per C
  % AB e' orizzontale, quindi l e' orizzontale
  \draw[dashed] (C)++(-3,0) -- ++(6,0) node[right] {$\ell$};

  % Etichette vertici
  \node[below left]  at (A) {$A$};
  \node[below right] at (B) {$B$};
  \node[above]       at (C) {$C$};

\end{tikzpicture}
\end{center}

Poiché \(\ell\) è parallela a \(\overline{AB}\), gli angoli \(\widehat{CAB}\) e \(\widehat{BCH}\) (dove \(H\) è un punto su \(\ell\)) sono \emph{alterni interni} e quindi congruenti; analogamente, gli angoli \(\widehat{CBA}\) e \(\widehat{ACH}\) sono congruenti. L’angolo \(\widehat{ACB}\) rimane invariato. Osservando che sulla retta \(\ell\) la somma degli angoli adiacenti in \(C\) è \(180^\circ\), otteniamo
\[
\angle CAB \;+\; \angle ACB \;+\; \angle CBA 
= 180^\circ.
\]
Questo conclude la dimostrazione.
\end{proof}

\begin{theorem}
L’area di un triangolo è data dalla formula
\[
\text{Area} = \frac{1}{2}\; (\text{base}) \;\times\; (\text{altezza}).
\]
\end{theorem}

\begin{proof}[dimostrazione]
Consideriamo un triangolo \(ABC\) e scegliamo come base il lato \(\overline{AB}\). Tracciamo l’altezza \(CH\), perpendicolare a \(\overline{AB}\), dove \(H\) è il piede dell’altezza su \(AB\).

\begin{center}
\begin{tikzpicture}[scale=1.0, line cap=round, line join=round]

  \coordinate (A) at (0,0);
  \coordinate (B) at (4,0);
  \coordinate (C) at (2,2);

  % Disegno del triangolo ABC
  \draw[thick] (A) -- (B) -- (C) -- cycle;

  % Proiezione di C su AB
  \coordinate (H) at ($(A)!(C)!(B)$);

  % Altezza CH
  \draw[dashed] (C) -- (H);

  % Etichette
  \node[below left]  at (A) {$A$};
  \node[below right] at (B) {$B$};
  \node[above]       at (C) {$C$};
  \node[below]       at (H) {$H$};

\end{tikzpicture}
\end{center}

La lunghezza \(\overline{AB}\) è la \emph{base}, e \(\overline{CH}\) è l’\emph{altezza} del triangolo rispetto a quella base. Completiamo il triangolo a un \emph{parallelogramma} raddoppiando la figura con una copia speculare: risulta che l’area del parallelogramma è \((\text{base}) \times (\text{altezza})\), e il nostro triangolo ne è esattamente la metà. Quindi
\[
\text{Area} 
= \frac{1}{2} \times (\text{base}) \times (\text{altezza}).
\]
\end{proof}

\subsubsection*{Tabella Riassuntiva dei Principali Teoremi sui Triangoli}

\noindent
\textbf{Teoremi validi per tutti i triangoli:}

\renewcommand{\arraystretch}{1.2}
\begin{center}
\begin{tabular}{p{0.32\textwidth} p{0.62\textwidth}}
\hline
Teorema & Formula \\
\hline

Somma degli Angoli Interni 
& 
\(\angle A + \angle B + \angle C = 180^\circ\). \\

Angolo Esterno
& 
L’angolo esterno in un vertice (es.\ \(\widehat{ABX}\) prolungando \(BC\)) è la somma dei due angoli interni opposti: \(\widehat{ABX} = \angle A + \angle C\). \\

Teorema dei Seni 
& 
\(\displaystyle \frac{AB}{\sin C} 
= \frac{BC}{\sin A}
= \frac{CA}{\sin B}
= 2R\), con \(R\) raggio della circonferenza circoscritta. \\

Teorema del Coseno 
& 
\(\displaystyle AB^2 = AC^2 + CB^2 - 2\,(AC)\,(CB)\,\cos A\). (Formule analoghe scambiando i vertici.) \\

Teorema dell’Area (generale)
& 
\(\displaystyle \text{Area} = \frac12\,(\text{base})\,(\text{altezza})
= \frac12\,AB\,CH
= \frac12\,BC\,AH
= \frac12\,CA\,BH.\)  
Altre formule: \(\text{Area} = \tfrac12\,ab\,\sin \gamma\), o \(\sqrt{s(s-a)(s-b)(s-c)}\). \\

Teorema dei Punti Notevoli
& 
\(\begin{cases}
\text{Mediane} \to \text{Baricentro }G =\bigl(\tfrac{x_A+x_B+x_C}{3},\tfrac{y_A+y_B+y_C}{3}\bigr).\\[3pt]
\text{Bisettrici} \to \text{Incentro }I =\tfrac{aA + bB + cC}{\,a+b+c\,}.\\[3pt]
\text{Assi perpendicolari} \to \text{Circocentro }O\ (\text{equidistante da }A,B,C).\\[3pt]
\text{Altezze} \to \text{Ortocentro }H.
\end{cases}\) \\

\hline
\end{tabular}
\end{center}

\medskip

\noindent
\textbf{Teoremi validi solo per i triangoli rettangoli (angolo retto in \(C\)):}

\renewcommand{\arraystretch}{1.2}
\begin{center}
\begin{tabular}{p{0.35\textwidth} p{0.57\textwidth}}
\hline
Teorema & Formula \\
\hline

Teorema di Pitagora
& 
\(AC^2 + BC^2 = AB^2\). (Se \(\angle C\) è retto, \(AB\) è l’ipotenusa.) \\

Primo Teorema di Euclide
& 
\(CH^2 = AH\,BH\). (\(CH\) altezza sull’ipotenusa, \(AH\) e \(BH\) i segmenti in cui l’ipotenusa è divisa.) \\

Secondo Teorema di Euclide
& 
\(\displaystyle \overline{AC}^2 = \overline{AH}\,\overline{AB}, 
\quad
\overline{BC}^2 = \overline{BH}\,\overline{AB}.\)\\

\hline
\end{tabular}
\end{center}


\subsec{Teorema di Carnot \& Dimostrazione [3]}

\begin{theorem}
In un triangolo \(ABC\) di lati \(a = BC\), \(b = AC\), \(c = AB\) opposti rispettivamente agli angoli \(\angle A\), \(\angle B\), \(\angle C\), vale la relazione
\[
c^2 = a^2 + b^2 - 2\,a\,b\,\cos C.
\]
Analoghe formule si ottengono scambiando i vertici (per \(\angle A\) si usa \(b^2 + c^2 - 2bc\,\cos A\), e così via).
\end{theorem}

\begin{proof}[dimostrazione]
\noindent
\textbf{Idea geometrica:} Il teorema di Carnot, o \emph{Legge del Coseno}, generalizza il Teorema di Pitagora a triangoli non rettangoli. Se l’angolo \(\widehat{C}\) fosse \(90^\circ\), allora \(\cos C = 0\) e la formula si ridurrebbe a \(c^2 = a^2 + b^2\). In caso generale, occorre sottrarre il termine \(2ab\,\cos C\).

\medskip

\begin{enumerate}
\item Sia \(ABC\) un triangolo con \(\angle C\) compreso tra i lati \(\overline{AC}\) e \(\overline{BC}\). Vogliamo dimostrare \(c^2 = a^2 + b^2 - 2ab\,\cos C\). 

\item Su \(AC\) prolunghiamo un segmento \(\overline{CD}\) tale che \(\overline{CD}\) sia \emph{parallelo} a \(\overline{AB}\). In questo modo, il quadrilatero \(ABDC\) ha un angolo retto e ci permette di costruire proiezioni utili.

\item Indichiamo con \(H\) il piede della proiezione ortogonale di \(B\) sulla retta \(AC\). Allora \(\overline{BH}\) è un segmento perpendicolare a \(\overline{AC}\). 

\item Nel triangolo \(ABC\), la lunghezza \(\overline{BH}\) è data da \(b \sin C\). Infatti, \(\angle C\) è anche l’angolo fra i lati \(\overline{BC}=a\) e \(\overline{AC}=b\). Allo stesso modo, la distanza \(\overline{AH}\) è \(b \cos C\). 

\item Il lato \(\overline{AB}\) può quindi essere visto come la somma \(\overline{AH} + \overline{HB}\) proiettata orizzontalmente e verticalmente, portando a:
\[
c^2 = (AH + \dots)^2 + (BH)^2 
\]
(oppure si usano scomposizioni di vettori).

\item In modo analitico (o con scomposizione trigonometrica), si ottiene
\[
c^2 = a^2 + b^2 - 2ab\,\cos C,
\]
che è la forma del Teorema del Coseno. 
\end{enumerate}
\end{proof}

\begin{center}
\begin{tikzpicture}[scale=0.9, line cap=round, line join=round]

% Vertici principali del triangolo
\coordinate (A) at (0,0);
\coordinate (C) at (6,0);
\coordinate (B) at (3,2.5);

% Prolunghiamo AC fino a D, tale che CD sia parallelo ad AB
% La pendenza di AB è (2.5-0)/(3-0) = 2.5/3
% Partendo da C(6,0), se aggiungiamo 6 in x, otteniamo x=12,
% y = 0 + (2.5/3)*6 = 5 => D(12,5)
\coordinate (D) at (12,5);

% Punto H = piede della proiezione ortogonale di B su AC (l'asse x):
% Quindi H ha la stessa x di B e y=0
\coordinate (H) at (3,0);

% Disegno del triangolo e segmenti aggiuntivi
\draw[thick] (A) -- (B) -- (C) -- cycle;  % Triangolo ABC
\draw[dashed] (C) -- (D);                 % CD parallelo a AB
\draw[dashed] (B) -- (H);                 % BH perpendicolare ad AC

% Etichette dei punti
\node[below left]  at (A) {$A$};
\node[below]       at (C) {$C$};
\node[above]       at (B) {$B$};
\node[above right] at (D) {$D$};
\node[below]       at (H) {$H$};

\draw[thick, dashed, red] (A) -- (B) -- (D) -- (C) -- cycle;

\end{tikzpicture}
\end{center}

\begin{esempio}
\textit{Testo:} Sia \(ABC\) un triangolo con \(AB=7\), \(BC=5\), e l’angolo \(\widehat{B}=60^\circ\). Calcolare la lunghezza \(AC\).

\begin{enumerate}
\item Poniamo \(AC=x\). Dal Teorema di Carnot, considerando \(\angle B=60^\circ\), abbiamo
\[
AC^2 
= AB^2 + BC^2 - 2\,AB\,BC\,\cos 60^\circ
= 7^2 + 5^2 - 2\,(7)\,(5)\,\frac12.
\]
\item Sostituendo i valori, otteniamo
\[
x^2
= 49 + 25 - 35
= 39.
\]
\item Quindi \(AC = x = \sqrt{39}\approx 6.24.\)
\end{enumerate}
\noindent
\textit{Conclusione:} Grazie al Teorema di Carnot, abbiamo ricavato \(AC = \sqrt{39}\) in modo diretto usando la misura di \(\angle B\). 
\end{esempio}
\subsec{Teorema dei Seni \& Dimostrazione [3]}

\begin{theorem}
In ogni triangolo \(ABC\), siano \(a = BC\), \(b = AC\), \(c = AB\) i lati opposti rispettivamente agli angoli \(\angle A\), \(\angle B\), \(\angle C\). Allora vale la relazione
\[
\frac{a}{\sin A} 
= \frac{b}{\sin B} 
= \frac{c}{\sin C} 
= 2R,
\]
dove \(R\) è il raggio della circonferenza circoscritta al triangolo.
\end{theorem}

\begin{proof}[dimostrazione]
Dividiamo la dimostrazione in steps:
\begin{enumerate}
\item \textbf{Circonferenza circoscritta.}  
Si consideri il \emph{circocentro} \(O\) del triangolo \(ABC\), cioè il centro della circonferenza passante per i tre vertici. Sia \(R\) il raggio di questa circonferenza.

\item \textbf{Costruzione di un triangolo rettangolo.}  
Tracciamo la retta dal centro \(O\) a un vertice, ad esempio \(A\). Poiché \(OA = R\), se consideriamo l’angolo \(\angle B\) al vertice \(B\), possiamo costruire un triangolo rettangolo in cui un lato (la proiezione) è \(\overline{OB}\), anche di lunghezza \(R\), e l’angolo al centro \(\widehat{AOB}\) è il doppio di \(\angle C\). Si sfrutta il fatto che l’arco \(\widehat{AB}\) opposto a \(\angle C\) sottende al centro un angolo \(2C\).

\item \textbf{Relazione fra lato e seno dell’angolo.}  
Nel \(\triangle AOB\), se si lascia cadere un’altezza sull’asse \(\overline{AB}\), si ottiene una relazione fra \(\overline{AB}\) e \(\sin\angle C\). Precisamente, si mostra che
\[
\frac{a}{\sin A} = 2R
\]
(oppure analoghe espressioni scambiando i vertici).

\item \textbf{Ripetizione per gli altri lati.}  
Analoghi ragionamenti si applicano a \(\angle A\) e \(\angle B\). Si conclude che
\[
\frac{a}{\sin A} 
= \frac{b}{\sin B} 
= \frac{c}{\sin C} 
= 2R.
\]
\end{enumerate}
\end{proof}

\begin{center}
\begin{tikzpicture}[scale=1.0, line cap=round, line join=round]

% Vertici del triangolo
\coordinate (A) at (0,0);
\coordinate (B) at (5,0);
\coordinate (C) at (2,3);

% Disegno del triangolo ABC
\draw[thick] (A) -- (B) -- (C) -- cycle;

% Punti medi dei lati
\coordinate (M_AB) at (2.5,0);   % midpoint di AB
\coordinate (M_BC) at (3.5,1.5); % midpoint di BC
\coordinate (M_AC) at (1,1.5);   % midpoint di AC

% Intersezione: i primi due assi => x=2.5 e y=x-2 => x=2.5 => y=0.5 => O=(2.5,0.5)
% Verifichiamo che O stia anche sul terzo asse => y= -2/3(2.5)+13/6 => 0.5 => OK
\coordinate (O) at (2.5,0.5);

% Disegno del circocentro e della circonferenza circoscritta
% Raggio= distanza OA
\pgfmathsetmacro{\r}{sqrt((2.5-0)^2 + (0.5-0)^2)}

\fill (O) circle(1.5pt) node[above left] {};
\draw[thick] (O) circle(\r);

% Etichette dei vertici
\node[below left]  at (A) {$A$};
\node[below right] at (B) {$B$};
\node[above]       at (C) {$C$};

\end{tikzpicture}
\end{center}

\begin{esempio}
\textit{Testo:} In un triangolo \(ABC\), siano \(\angle A = 30^\circ\), \(\angle B = 50^\circ\), e il lato \(a = BC = 10\). Determinare \(\angle C\) e gli altri lati \(b=AC\) e \(c=AB\).

\begin{enumerate}
\item \textbf{Determinazione di \(\angle C\).}  
Poiché la somma degli angoli interni è \(180^\circ\), si ha
\[
\angle C 
= 180^\circ - (30^\circ + 50^\circ)
= 100^\circ.
\]

\item \textbf{Teorema dei Seni.}  
Poniamo \(b=AC\) e \(c=AB\). Dal Teorema dei Seni:
\[
\frac{a}{\sin A}
= \frac{b}{\sin B}
= \frac{c}{\sin C}.
\]
Con \(a=10\) e \(\angle A=30^\circ\), \(\sin A= \tfrac12\). Otteniamo
\[
\frac{10}{\tfrac12}
= 20 
= 2R.
\]
Dunque \(R=10\).

\item \textbf{Calcolo di \(b\).}  
\(\sin B = \sin(50^\circ)\approx 0.7660\). Dal Teorema dei Seni,
\[
\frac{b}{\sin B} 
= 2R 
= 20
\quad\Longrightarrow\quad
b 
= 20 \,\sin(50^\circ)
\approx 20 \times 0.7660
= 15.32.
\]

\item \textbf{Calcolo di \(c\).}  
\(\sin C = \sin(100^\circ)\approx 0.9848\). Quindi,
\[
\frac{c}{\sin(100^\circ)}
= 20
\quad\Longrightarrow\quad
c
= 20 \times 0.9848
= 19.70 \approx 19.7.
\]

\item \textbf{Conclusione.}  
Si ottiene \(\angle C=100^\circ\), \(b\approx 15.32\) e \(c\approx 19.70\). Tutti i valori derivano in modo diretto dal Teorema dei Seni, una volta noti due angoli e un lato.
\end{enumerate}
\end{esempio}




\subsec{Teorema della Corda \& Dimostrazione [3]}

\begin{theorem}
In un cerchio di raggio \(R\), la \emph{lunghezza} di una corda che sottende un angolo al centro \(2\alpha\) è
\[
\text{corda} = 2\,R\,\sin(\alpha).
\]
\end{theorem}

\begin{proof}[dimostrazione]
Vediamo i passaggi della dimostrazione:
\begin{enumerate}
\item \textbf{Cerchio e angolo al centro.}  
Consideriamo un cerchio di centro \(O\) e raggio \(R\). Sia \(AB\) una corda che sottende al centro un angolo \(\widehat{AOB} = 2\alpha\).  
\item \textbf{Triangolo isoscele.}  
I segmenti \(\overline{OA}\) e \(\overline{OB}\) sono due raggi del cerchio, quindi \(OA=OB=R\). Il triangolo \(AOB\) è isoscele con base \(\overline{AB}\).  
\item \textbf{Bisettrice e triangolo rettangolo.}  
Tracciamo la bisettrice dall’angolo al vertice \(O\) fino al punto \(M\) sulla corda \(\overline{AB}\). L’angolo \(\angle AOM\) risulta \(\alpha\). Inoltre, \(\triangle AOM\) è rettangolo se \(\overline{OM}\) è l’altezza sulla base \(AB\).  
\item \textbf{Calcolo della corda.}  
Poiché \(AM\) è la metà della corda \(\overline{AB}\), si ottiene \(AM = \tfrac12\,AB\). Nel \(\triangle AOM\), l’ipotenusa è \(OA=R\) e l’angolo \(\angle AOM=\alpha\). Il cateto opposto a \(\alpha\) è \(AM\), quindi
\[
AM = OA \,\sin(\alpha) 
= R\,\sin(\alpha).
\]
Pertanto,
\[
AB = 2\,AM 
= 2\,R\,\sin(\alpha).
\]
\end{enumerate}
\end{proof}

\begin{center}
\begin{tikzpicture}[scale=1.2, line cap=round, line join=round]

% Centro del cerchio e raggio
\coordinate (O) at (0,0);
\def\R{2.5}

% Disegno del cerchio
\draw[thick] (O) circle(\R);

% Angolo al centro = 2 alpha, costruiamo 2 alpha= 60° per esempio
\def\twoalpha{60} % quindi alpha=30
\coordinate (A) at (\R,0);
\coordinate (B) at ({\R*cos(\twoalpha)},{\R*sin(\twoalpha)});

% Segmenti OA e OB
\draw[thick] (O)--(A);
\draw[thick] (O)--(B);

% Corda AB
\draw[thick, blue] (A)--(B);

% Bisettrice: punto M a meta' di AB
\coordinate (M) at ($(A)!0.5!(B)$);
\draw[dashed] (O)--(M);

% Etichette
\node[right]  at (A) {$A$};
\node[above]  at (B) {$B$};
\node[left]   at (O) {$O$};
\node[blue]   at ($(A)!0.5!(B)+(0,0.2)$) {};
\node at ($(O)!0.5!(A)$) [below left] {};
\node at ($(O)!0.5!(B)$) [above left] {};

% Angolo 2 alpha in O
\draw (0.8,0) arc[start angle=0, delta angle=\twoalpha, radius=0.8];
\node at (\twoalpha/2+10:1.15) {$2\alpha$};

\end{tikzpicture}
\end{center}

\begin{esempio}
\textit{Testo:} In un cerchio di raggio \(R=10\), consideriamo una corda che sottende al centro un angolo di \(100^\circ\). Determinare la lunghezza della corda.

\begin{enumerate}
\item \textbf{Angolo al centro e metà angolo.}  
Se l’angolo al centro \(\widehat{AOB}\) è \(2\alpha=100^\circ\), allora \(\alpha=50^\circ\).

\item \textbf{Teorema della Corda.}  
La lunghezza della corda \(\overline{AB}\) è
\[
AB 
= 2\,R\,\sin(\alpha) 
= 2\times 10\times \sin(50^\circ).
\]
\item \textbf{Calcolo numerico.}  
\(\sin(50^\circ)\approx 0.7660\), dunque
\[
AB 
\approx 20 \times 0.7660
= 15.32.
\]

\item \textbf{Conclusione.}  
La corda misura circa \(15.32\).  
\end{enumerate}
\end{esempio}

\subsec{Equazioni Goniometriche di Primo e Secondo Grado [2]}

Le \emph{equazioni goniometriche} sono quelle in cui l’incognita compare all’interno di funzioni trigonometriche (seno, coseno, tangente, ecc.). Risolvere un’equazione goniometrica significa trovare tutti gli angoli (in gradi o radianti) che soddisfano la relazione data. Spesso queste equazioni sono \emph{periodiche}, per cui la soluzione generale si esprime aggiungendo i periodi appropriati. 

In particolare, se compare \(\sin x\) o \(\cos x\), la periodicità è \(2\pi\); se compare \(\tan x\) o \(\cot x\), la periodicità è \(\pi\). Quando si risolve \(\sin x = A\) o \(\cos x = A\), occorre:
\begin{itemize}
\item Identificare gli angoli di \emph{riferimento} in un periodo (ad esempio \([0, 2\pi)\)).
\item Espandere la soluzione a tutti i possibili angoli usando la periodicità.
\item Verificare che i valori trovati siano validi (per esempio, se \(A\notin[-1,1]\), non ci sono soluzioni).
\end{itemize}

\subsubsection*{Rappresentazione delle Soluzioni su Piano Cartesiano e su Cerchio Goniometrico}

Nelle \emph{equazioni goniometriche} (ad esempio \(\sin x = \tfrac12\), \(\cos x = A\), \(\tan x = B\)), la variabile \(x\) è un \emph{angolo}, che possiamo interpretare:

\begin{itemize}
\item \textbf{Su un piano cartesiano} \((x,y)\), dove \(x\) è la variabile indipendente (l’angolo, in ascissa) e \(y\) è il valore della funzione trigonometrica (in ordinata). Le soluzioni di \(\sin x = \tfrac12\) corrispondono a tutti i punti \((x,y)\) sul grafico di \(\sin x\) in cui \(y=\tfrac12\). Graficamente, ciò appare come \emph{infinite intersezioni} di una retta orizzontale \(y=\tfrac12\) con la sinusoide \(y=\sin x\).  
\item \textbf{Sul cerchio goniometrico}, dove un unico giro \([0,2\pi)\) (o \([- \pi,\pi)\), ecc.) racchiude i possibili valori di \(x\) in un solo “ciclo”. Qui la soluzione si manifesta come \emph{punti} sul cerchio (angoli di riferimento) e poi si estende a tutti i giri possibili ripetendo la periodicità.
\end{itemize}

% --- Prima figura: il grafico di sin(x) in [0,2pi] ---
\begin{center}
\begin{tikzpicture}[scale=1.0, line cap=round, line join=round]

% Assi
\draw[->] (-0.5,0) -- (19,0) node[right] {$x$};
\draw[->] (0,-1.5) -- (0,1.5) node[above] {$y$};

% Curva sin(x) in nero tratteggiato, dominio [0,6 pi] ~ [0,18.849...]
\draw[domain=0:19, smooth, variable=\t, dashed] 
  plot ({\t},{sin(\t r)});

% Retta orizzontale y=0.5
\draw[dashed] (-0.5,0.5) -- (19,0.5);

% Calcoliamo i punti di intersezione sin x=0.5 in [0,6 pi]
% x = pi/6 + 2k pi  or x= 5pi/6 + 2k pi, con k=0,1,2
% pi/6 ~ 0.5236, 5pi/6 ~ 2.618
% Aggiungiamo 2 pi ~ 6.283 per k=1 e k=2

\def\xa{0.5236}   % pi/6
\def\xb{2.618}    % 5pi/6
\def\xc{6.807}    % pi/6 + 2pi
\def\xd{8.901}    % 5pi/6 + 2pi
\def\xe{13.09}    % pi/6 + 4pi
\def\xf{15.18}    % 5pi/6 + 4pi

% Disegno in blu dei punti di soluzione
\fill[blue] (\xa,0.5) circle(2pt);
\fill[blue] (\xb,0.5) circle(2pt);
\fill[blue] (\xc,0.5) circle(2pt);
\fill[blue] (\xd,0.5) circle(2pt);
\fill[blue] (\xe,0.5) circle(2pt);
\fill[blue] (\xf,0.5) circle(2pt);

\end{tikzpicture}
\end{center}

Nel \emph{piano cartesiano}, l’equazione \(\sin x=\tfrac12\) si vede come l’intersezione fra la sinusoide e la retta orizzontale \(y=\tfrac12\). Tali intersezioni si ripetono \emph{infinitamente} a intervalli di \(2\pi\).


% --- Seconda figura: il cerchio goniometrico ---
\begin{center}
\begin{tikzpicture}[scale=1.6, line cap=round, line join=round]

% Assi e cerchio
\draw[->] (-1.2,0) -- (1.2,0) node[right] {$x$};
\draw[->] (0,-1.2) -- (0,1.2) node[above] {$y$};
\draw[thick] (0,0) circle(1);

% Definizione degli angoli (in gradi) per sin x=1/2
\def\alpha{30}   % pi/6
\def\beta{150}   % 5pi/6

% Raggi in nero tratteggiato
\draw[dashed] (0,0) -- ({cos(\alpha)},{sin(\alpha)});
\draw[dashed] (0,0) -- ({cos(\beta)},{sin(\beta)});

% Punti di soluzione in blu
\fill[blue] ({cos(\alpha)},{sin(\alpha)}) circle(1.8pt);
\fill[blue] ({cos(\beta)},{sin(\beta)}) circle(1.8pt);

% Etichetta dell'origine
\node at (0,0) [below left] {$O$};

\end{tikzpicture}
\end{center}

 Sul \emph{cerchio goniometrico}, ci basta considerare il \emph{primo giro} \([0,2\pi)\) per trovare i due punti di riferimento (\(\tfrac{\pi}{6}\) e \(\tfrac{5\pi}{6}\)), poi aggiungere \(\pm 2k\pi\) per tutte le soluzioni. 

\begin{esempio}
\(\sin x = \tfrac12.\)  
Bisogna trovare tutti gli \(x\) per cui il seno vale \(\tfrac12\). L’angolo di riferimento è \(\tfrac{\pi}{6}\), ma poiché \(\sin x\) è positivo anche nel secondo quadrante, l’altro angolo base è \(\tfrac{5\pi}{6}\). Quindi:
\[
\sin x = \frac12 
\;\;\Longrightarrow\;\;
x = \frac{\pi}{6} + 2k\pi 
\quad \text{oppure}\quad 
x = \frac{5\pi}{6} + 2k\pi,\quad k\in \mathbb{Z}.
\]
\end{esempio}

\begin{esempio}
\(\cos x = \sqrt{\tfrac12}.\)  
Qui \(\cos x = \cos \bigl(\tfrac{\pi}{4}\bigr)\). Dato che \(\cos x\) è positiva nel primo e nel quarto quadrante, gli angoli di riferimento sono \(\pm \tfrac{\pi}{4}\). Pertanto:
\[
x = \pm \frac{\pi}{4} + 2k\pi,\quad k\in \mathbb{Z}.
\]
\end{esempio}

\begin{esempio}
\(\tan x = 1.\)  
Poiché \(\tan \tfrac{\pi}{4} = 1\), la periodicità di \(\tan x\) è \(\pi\). Dunque:
\[
x = \frac{\pi}{4} + k\pi,\quad k\in \mathbb{Z}.
\]
\end{esempio}

\subsubsection*{Equazioni Goniometriche di Secondo Grado}

Si chiamano \emph{equazioni goniometriche di secondo grado} quelle in cui compaiono, ad esempio, \(\sin^2 x\) o \(\cos^2 x\) o espressioni equivalenti, e dove si può fare un’analogia con le classiche equazioni quadratiche.

\noindent
\textbf{Strategie di Risoluzione:}
\begin{enumerate}
\item \textbf{Sostituzione:} Si introduce una variabile ausiliaria, per esempio \(u = \sin x\) oppure \(u = \cos x\). Così l’equazione diventa \emph{quadratica} in \(u\).  
  Una volta trovati i valori di \(u\), si risolve \(\sin x = u\) o \(\cos x = u\).

\item \textbf{Uso delle Identità Pitagoriche:} Se compaiono \(\sin^2 x\) e \(\cos^2 x\) nella stessa equazione, può essere utile sostituire \(\cos^2 x = 1 - \sin^2 x\) (o viceversa) per ridurre il numero di funzioni diverse.

\item \textbf{Riduzione di Termine Misto:} Se compare \(\sin x \cos x\), a volte conviene sfruttare la formula \(\sin(2x)=2\sin x\cos x\) oppure \(\cos(2x)=\cos^2 x - \sin^2 x\) per semplificare.

\item \textbf{Controllo di Dominio e Soluzioni Multiple:} Al termine, bisogna ricordare che \(\sin x\) e \(\cos x\) non possono superare 1 o -1. Se l’equazione “quadratica” in \(u\) ha soluzioni \(u_1\) o \(u_2\) fuori dall’intervallo \([-1,1]\), quelle non sono accettabili per \(\sin x\) o \(\cos x\).
\end{enumerate}

\begin{esempio}
\(\sin^2 x \;-\;\sqrt{2}\,\sin x \;+\;\tfrac12 \;=\;0.\)

\noindent
\textbf{Soluzione:} Introduciamo \(u=\sin x\). L’equazione diventa
\[
u^2 \;-\;\sqrt{2}\,u \;+\;\tfrac12 \;=\;0.
\]
Il discriminante è
\[
\Delta = (\!-\!\sqrt{2})^2 - 4\cdot 1\cdot \tfrac12 = 2 - 2 = 0,
\]
quindi c’è un’unica radice reale
\[
u \;=\;\frac{\sqrt{2}}{2}.
\]
Essendo \(u=\sin x\), si ha
\[
\sin x = \frac{\sqrt{2}}{2}.
\]
Gli angoli di riferimento in \([0, 2\pi)\) sono \(x=\tfrac{\pi}{4}\) e \(x=\tfrac{3\pi}{4}\). Aggiungendo la periodicità \(2\pi\), le soluzioni generali sono
\[
x \;=\; \frac{\pi}{4} + 2k\pi 
\quad \text{oppure}\quad
x \;=\; \frac{3\pi}{4} + 2k\pi,\quad k\in\mathbb{Z}.
\]
\end{esempio}

\begin{esempio}
\(\sin^2 x \;+\;\sin x\,\cos x \;-\;\cos^2 x \;=\;0.\)

\noindent
\textbf{Soluzione:} Riscriviamo \(\sin^2 x - \cos^2 x = -\sin x\,\cos x\). Ricordiamo che 
\(\sin^2 x - \cos^2 x = -\cos(2x)\) e \(\sin x\,\cos x = \tfrac12\,\sin(2x)\). L’equazione diventa
\[
-\cos(2x) \;=\; -\,\tfrac12\,\sin(2x),
\]
cioè
\[
\cos(2x) \;=\;\frac12\,\sin(2x).
\]
Dividendo per \(\sin(2x)\) (supponendo \(\sin(2x)\neq 0\), poi verifichiamo a parte \(\sin(2x)=0\)), si ottiene
\[
\cot(2x) \;=\;\frac12 
\quad\Longrightarrow\quad
\tan(2x) \;=\;2.
\]
Le soluzioni di \(\tan(2x)=2\) sono
\[
2x \;=\;\arctan(2)\;+\;k\pi,
\quad k\in\mathbb{Z}.
\]
Quindi
\[
x \;=\;\frac12\,\arctan(2)\;+\;\frac{k\pi}{2}.
\]
Se \(\sin(2x)=0\), allora \(2x=n\pi\). Ma sostituendo in \(\cos(2x)=\tfrac12\,\sin(2x)\), si ottiene \(\cos(n\pi)=0\) che non è possibile per \(n\) intero (poiché \(\cos(n\pi)\) è \(\pm1\)). Dunque nessuna soluzione in quel caso.  
\end{esempio}

\begin{esempio}
\(\sin^2 x \;+\;\cos^2 x \;-\;\sqrt{3}\,\sin x\,\cos x \;=\;0.\)

\noindent
\textbf{Soluzione:} Poiché \(\sin^2 x + \cos^2 x = 1\), l’equazione diventa
\[
1 \;-\;\sqrt{3}\,\sin x\,\cos x \;=\;0 
\quad\Longrightarrow\quad
\sin x\,\cos x 
\;=\;\frac{1}{\sqrt{3}}.
\]
Ricordiamo \(\sin(2x) = 2\,\sin x\,\cos x\). Quindi
\[
\sin(2x) 
= 2\,\bigl(\tfrac{1}{\sqrt{3}}\bigr)
= \frac{2}{\sqrt{3}}
= \frac{2\sqrt{3}}{3}.
\]
Per \(\sin(2x)=\tfrac{2\sqrt{3}}{3}\), notiamo che \(\tfrac{2\sqrt{3}}{3}=\sin(\tfrac{\pi}{3})\times 2= \sin(\tfrac{2\pi}{3})\dots\) ma è più diretto considerare \(\tfrac{2\sqrt{3}}{3}\approx 1.1547\), in realtà \(\frac{2\sqrt{3}}{3}\approx 1.1547>1\). 

\emph{Attenzione}: \(\tfrac{2\sqrt{3}}{3} \approx 1.1547\), che supera \(1\). Ciò significa che non esiste un angolo reale con \(\sin(2x)\) uguale a un valore maggiore di \(1\). Quindi \emph{nessuna} soluzione reale.  

Se fosse stato un valore \(\le1\), avremmo scritto \(2x=\sin^{-1}(\tfrac{2\sqrt{3}}{3})+\dots\). Ma qui \(\tfrac{2\sqrt{3}}{3}>1\), per cui non ci sono soluzioni. 
\end{esempio}

\newpage
\textbf{Tabella delle Identità Trigonometriche e Altre Formule Utili:}

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
\textbf{Complementari:} \(\sin(90^\circ-\theta)=\cos\theta,\;\cos(90^\circ-\theta)=\sin\theta\) \\[2mm]
& \textbf{Supplementari:} \(\sin(180^\circ-\theta)=\sin\theta,\;\cos(180^\circ-\theta)=-\cos\theta\) \\[2mm]
& \textbf{Esplementari:} \(\sin(360^\circ-\theta)=-\sin\theta,\;\cos(360^\circ-\theta)=\cos\theta\) \\
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
\(\displaystyle \alpha = \sqrt{\frac{(p-b)(p-c)}{b\,c}}\), \(\sqrt{\frac{p\,(p-a)}{b\,c}}\), \(\sqrt{\frac{(p-b)(p-c)}{p\,(p-a)}}\) \\
\hline
Formule di Briggs per \(\beta\) & 
\(\displaystyle \beta = \sqrt{\frac{(p-a)(p-c)}{a\,c}}\), \(\sqrt{\frac{p\,(p-b)}{a\,c}}\), \(\sqrt{\frac{(p-a)(p-c)}{p\,(p-b)}}\) \\
\hline
Formule di Briggs per \(\gamma\) & 
\(\displaystyle \gamma = \sqrt{\frac{(p-a)(p-b)}{a\,b}}\), \(\sqrt{\frac{p\,(p-c)}{a\,b}}\), \(\sqrt{\frac{(p-a)(p-b)}{p\,(p-c)}}\) \\
\hline
\end{tabular}
\end{center}

\noindent
\textbf{Osservazione:} Queste identità e formule sono essenziali per manipolare e risolvere \emph{equazioni goniometriche} di vario tipo (lineari, quadratiche, con somma e sottrazione, ecc.). Nelle equazioni di secondo grado, in particolare, la strategia è ridurre \(\sin^2 x\) o \(\cos^2 x\) in termini di \(\sin(2x)\) o \(\cos(2x)\), o introdurre sostituzioni del tipo \(u=\sin x\) o \(u=\cos x\). 

\subsec{Disequazioni Goniometriche [2]}

Le \emph{disequazioni goniometriche} sono \emph{inequazioni} (del tipo \(>\), \(\ge\), \(<\), \(\le\)) in cui compaiono funzioni trigonometriche di un’incognita angolare. Risolvere una disequazione goniometrica significa individuare tutti gli \emph{angoli} che rendono vera l’inequazione. Come per le equazioni goniometriche, occorre tenere conto della \emph{periodicità} e della \emph{natura} (intervalli, quadranti) delle funzioni trigonometriche coinvolte.

\begin{itemize}
\item \textbf{Strategie comuni:}
  \begin{enumerate}
    \item \emph{Trasformare la disequazione} in una forma standard, ad esempio \(\sin x > A\), \(\cos x \le B\), \(\tan x < C\), ecc.
    \item \emph{Individuare gli angoli di riferimento} in un periodo (ad es.\ \([0, 2\pi)\) se la funzione è \(\sin x\) o \(\cos x\), oppure \([0,\pi)\) se è \(\tan x\) o \(\cot x\)).
    \item \emph{Disegnare} la funzione sul cerchio goniometrico o sul grafico cartesiano, per capire in quali intervalli (o archi) la disequazione risulta vera.
    \item \emph{Espandere la soluzione} a tutti i periodi, sommando multipli di \(2\pi\) (o \(\pi\)) a seconda della funzione.
  \end{enumerate}
\end{itemize}

\begin{esempio}
\(\sin x > \tfrac12.\)

Vogliamo trovare gli angoli \(x\) per cui \(\sin x\) supera \(\tfrac12\). Sappiamo che \(\sin x = \tfrac12\) agli angoli di riferimento \(\tfrac{\pi}{6}\) e \(\tfrac{5\pi}{6}\). Il grafico di \(\sin x\) (oppure il cerchio goniometrico) mostra che \(\sin x\) è maggiore di \(\tfrac12\) quando \(x\) si trova \emph{tra} questi due angoli, ossia:
\[
\frac{\pi}{6} < x < \frac{5\pi}{6}
\quad (\text{mod }2\pi).
\]
Più precisamente, la soluzione generale è
\[
x \in \bigcup_{k\in\mathbb{Z}} 
\Bigl(\,\frac{\pi}{6} + 2k\pi,\; \frac{5\pi}{6} + 2k\pi\Bigr).
\]
\end{esempio}

Come per le equazioni, abbiamo due modi di rappresentare le soluzioni, possiamo rappresentarle come al solito sul piano cartesiano o usare il più efficiente cerchio goniometrico. Vediamo entrambe le rappresentazioni:

\begin{center}
\begin{tikzpicture}[scale=1.1, line cap=round, line join=round]

% Assi
\draw[->] (-0.5,0) -- (19,0) node[right] {$x$};
\draw[->] (0,-1.5) -- (0,1.5) node[above] {$y$};

% Seno in nero tratteggiato su [0, 6pi]
\draw[domain=0:19, smooth, variable=\t, dashed] 
  plot ({\t},{sin(\t r)});

% Retta orizzontale y=0.5 (disegno in dashed)
\draw[dashed] (-0.5,0.5) -- (19,0.5);

% Intervalli di x in cui sin x > 0.5 su [0,6 pi]:
%   [pi/6 + 2k pi, 5pi/6 + 2k pi], k=0,1,2
% Valori approssimati:
%  k=0 => [0.5236, 2.618]
%  k=1 => [6.807, 8.901]
%  k=2 => [13.09, 15.18]

% Disegno in blu (piu' spesso) delle parti di sin x che superano 0.5
\draw[blue, line width=1.4pt, domain=0.5236:2.618, smooth, variable=\t] 
  plot ({\t},{sin(\t r)});
\draw[blue, line width=1.4pt, domain=6.807:8.901, smooth, variable=\t] 
  plot ({\t},{sin(\t r)});
\draw[blue, line width=1.4pt, domain=13.09:15.18, smooth, variable=\t] 
  plot ({\t},{sin(\t r)});

\end{tikzpicture}
\end{center}

\begin{center}
\begin{tikzpicture}[scale=1.9, line cap=round, line join=round]

% Cerchio goniometrico di raggio 1
\draw[thick] (0,0) circle(1);

% Assi
\draw[->] (-1.2,0) -- (1.2,0) node[right] {$x$};
\draw[->] (0,-1.2) -- (0,1.2) node[above] {$y$};

% Angoli pi/6 e 5pi/6
\def\startAng{30}    % in degrees => pi/6
\def\endAng{150}     % => 5pi/6

% Arco in blu, thick line, dall'angolo 30° a 150°
\draw[blue, thick, domain=\startAng:\endAng]
  plot ({cos(\x)}, {sin(\x)});

% Raggi a pi/6 e 5pi/6 (dashed)
\draw[dashed] (0,0) -- ({cos(\startAng)},{sin(\startAng)});
\draw[dashed] (0,0) -- ({cos(\endAng)},{sin(\endAng)});

% Punti sul cerchio
\fill ({cos(\startAng)},{sin(\startAng)}) circle(0.02)
  node[right] {$\tfrac{\pi}{6}$};
\fill ({cos(\endAng)},{sin(\endAng)})   circle(0.02)
  node[left]  {$\tfrac{5\pi}{6}$};

% Etichetta dell'origine
\node at (0,0) [below left] {$O$};

\end{tikzpicture}
\end{center}

\noindent
Nel disegno, l’arco \(\bigl(\tfrac{\pi}{6},\,\tfrac{5\pi}{6}\bigr)\) sul \emph{cerchio goniometrico} rappresenta gli angoli del primo giro \([0,2\pi)\) in cui \(\sin x\) è maggiore di \(\tfrac12\). Aggiungendo i multipli di \(2\pi\), si ottiene la soluzione generale.

\subsubsection*{Esempi di Disequazioni Goniometriche di Secondo Grado}

In questa sezione presentiamo alcuni \emph{esempi più articolati} di disequazioni goniometriche, in cui occorrono \emph{restrizioni} di dominio (ad esempio denominatori non nulli o tangenti non definite) e/o equazioni di secondo grado in funzioni trigonometriche.

\bigskip

%---------------------------------------------------------------------------------
% ESEMPIO 1: tan(2x)-3>0 con restrizioni
%---------------------------------------------------------------------------------
\begin{esempio}
\(\tan(2x) - 3 > 0.\)

\noindent
\textbf{Strategia:} Risolvere \(\tan(2x) > 3\). Ricordiamo che \(\tan\theta\) è indefinita dove \(\cos\theta=0\). Qui, \(\theta = 2x\). Quindi:

\begin{enumerate}
\item \textbf{Dominio:} \(\cos(2x)\neq 0 \implies 2x \neq \tfrac{\pi}{2} + k\pi,\; k\in\mathbb{Z}.\)  
   Dunque \(x\neq \tfrac{\pi}{4} + \tfrac{k\pi}{2}\). In quei punti \(\tan(2x)\) non è definita, quindi non possono far parte della soluzione.

\item \textbf{Soluzione di base:} \(\tan(2x) > 3.\)  
   Impostiamo \(\tan(2x) - 3 > 0\). Facciamo riferimento all’angolo \(\alpha=\arctan(3)\) (circa \(71.565^\circ\) in gradi, oppure \(\approx 1.249\) in radianti). La funzione \(\tan\theta\) è \emph{crescente} in ogni intervallo di ampiezza \(\pi\). Quindi:
   \[
   2x \in \bigl(\alpha + k\pi,\; \tfrac{\pi}{2} + k\pi\bigr)
   \cup
   \bigl(\tfrac{3\pi}{2} + k\pi,\; \alpha + (k+1)\pi\bigr),
   \]
   ma dobbiamo descriverlo in modo più lineare. In sostanza, \(\tan\theta > 3\) negli intervalli dove \(\theta\) supera \(\arctan(3)\) ma è ancora prima della vertical asymptote.

\item \textbf{Traduzione in \(x\):} poiché \(\theta=2x\), dividiamo tutto per 2. Quindi
\[
x \in \bigl(\tfrac{\alpha}{2} + \tfrac{k\pi}{2},\;\tfrac{\pi}{4} + \tfrac{k\pi}{2}\bigr)
\;\cup\;
\bigl(\tfrac{3\pi}{4} + \tfrac{k\pi}{2},\;\tfrac{\alpha}{2} + \tfrac{(k+1)\pi}{2}\bigr).
\]
\item \textbf{Eliminazione dei punti vietati:} Ricordiamo che \(x\neq \tfrac{\pi}{4} + \tfrac{k\pi}{2}\). Tali valori corrispondono agli \emph{estremi} degli intervalli, quindi rimangono \emph{esclusi}.  
\end{enumerate}

\noindent
\textbf{Conclusione:} La disequazione \(\tan(2x)>3\) ammette soluzione in quegli intervalli di \(\theta=2x\) dove \(\theta\) supera \(\arctan(3)\) ma non raggiunge il successivo asintoto, tenendo conto della periodicità \(\pi\). La traduzione in \(x\) \emph{dimezza} tali intervalli e \emph{esclude} i punti in cui \(\cos(2x)=0\).
\end{esempio}

\noindent
L’idea è di interpretare \(\theta = 2x\) come angolo sul \emph{cerchio goniometrico} e mostrare in \textcolor{red}{rosso} i punti da \emph{escludere} (dove \(\cos\theta=0\), cioè \(\tan\theta\) è indefinita), e in \textcolor{blue}{blu} gli \emph{archi} in cui \(\tan\theta > 3\). Questo è un disegno puramente \emph{dimostrativo}, senza valori numerici precisi, ma utile a visualizzare la struttura delle soluzioni.


\begin{center}
\begin{tikzpicture}[scale=1.6, line cap=round, line join=round]

% Cerchio goniometrico di raggio 1
\draw[thick] (0,0) circle(1);

% Assi
\draw[->] (-1.2,0) -- (1.2,0) node[right] {$x$};
\draw[->] (0,-1.2) -- (0,1.2) node[above] {$y$};

% Angolo alpha = arctan(3) ~ 71.565° (1.249 rad)
% Per indicare i punti in cui tan theta=3
\def\alphaDeg{71.565}
\def\alphaRad{1.249}  % approssimato

% Punti dove cos(theta)=0 => theta= pi/2 (90°) e 3pi/2 (270°)
% Li segniamo in rosso come "esclusi"
\foreach \ang in {90,270}{
  \fill[red] ({cos(\ang)},{sin(\ang)}) circle(0.05);
}

% Disegniamo un paio di archi "blu" dove tan theta>3
% Ad esempio: 
% 1) un arco immediatamente dopo theta=alphaDeg fino a pi/2
% 2) un arco in (alphaDeg+180°, 270°)
% 3) e cosi' via, periodico ogni 180° (pi rad)

% Arco 1: da alphaDeg=71.565° a 90°
\draw[blue, very thick, domain=\alphaDeg:90] 
  plot({cos(\x)},{sin(\x)});

% Arco 2: da alphaDeg+180=251.565° a 270°
\pgfmathsetmacro{\alphaDegTwo}{\alphaDeg+180}
\draw[blue, very thick, domain=\alphaDegTwo:270]
  plot({cos(\x)},{sin(\x)});

% Punti di transizione (dove tan theta=3)
\fill[blue] ({cos(\alphaDeg)},{sin(\alphaDeg)}) circle(0.02)
  node[right] {};
\fill[blue] ({cos(\alphaDegTwo)},{sin(\alphaDegTwo)}) circle(0.02)
  node[left] {};

% Etichetta dell'origine
\node at (0,0) [below left] {$O$};

% Piccola legenda
\node[red] at (0.7,1.1) {};
\node[blue] at (0.7,0.9) {};

\end{tikzpicture}
\end{center}



%---------------------------------------------------------------------------------
% ESEMPIO 2: Disequazione di II grado con denominatore
%---------------------------------------------------------------------------------
\begin{esempio}
\[
\frac{\sin^2 x - 1}{\,1 - 2\,\cos^2 x\,} \;\ge\; 0.
\]

\noindent
\textbf{Strategia:} Individuiamo anzitutto \emph{dove è definita} l’espressione, poi studiamo il segno del numeratore e del denominatore. 

\begin{enumerate}
\item \textbf{Dominio:} Il denominatore non deve essere zero:
\[
1 - 2\,\cos^2 x \;\neq\; 0
\;\;\Longrightarrow\;\;
\cos^2 x \;\neq\;\tfrac12
\;\;\Longrightarrow\;\;
\cos x \;\neq\;\pm \tfrac{1}{\sqrt2}.
\]
Quindi \(\cos x\neq \pm \frac{\sqrt2}{2}\). Gli angoli esclusi sono
\[
x \;=\;\pm \tfrac{\pi}{4} + k\pi 
\quad\text{oppure}\quad
x \;=\;\pm \tfrac{3\pi}{4} + k\pi,\quad k\in\mathbb{Z}.
\]

\item \textbf{Numeratore:} \(\sin^2 x -1 = -\cos^2 x.\)  
   Quindi il numeratore è \(-\cos^2 x\). Il suo segno è sempre \(\le 0\), ed è zero solo se \(\cos x=0\). 

\item \textbf{Denominatore:} \(1 - 2\cos^2 x\).  
\begin{itemize}
   \item Se \(\cos^2 x < \tfrac12\), allora \(1-2\cos^2 x>0\).  
   \item Se \(\cos^2 x > \tfrac12\), allora \(1-2\cos^2 x<0\).  
\end{itemize}
\item \textbf{Segno complessivo:}  
   \[
   \frac{\sin^2 x -1}{\,1 - 2\,\cos^2 x\,}
   = \frac{-\cos^2 x}{\,1 - 2\cos^2 x\,}.
   \]
   \begin{itemize}
   \item Se \(\cos^2 x=0\implies \cos x=0\implies x=\tfrac{\pi}{2}+k\pi\), allora il numeratore è \(0\). Soluzione parziale se non annulla pure il denominatore. In quel caso, \(\cos^2 x=0<\tfrac12\), denominatore \(>0\). Quindi il valore dell’espressione è \(0\) e soddisfa \(\ge 0\).  
   \item Se \(\cos^2 x<\tfrac12\implies 1-2\cos^2 x>0\), il numeratore è \(\le 0\). Dunque il rapporto è \(\le 0\). Per \(\ge 0\) serve che sia esattamente \(0\). Quindi \(\cos x=0\).  
   \item Se \(\cos^2 x>\tfrac12\implies 1-2\cos^2 x<0\), il numeratore \(\le 0\). Un numero \(\le 0\) diviso per un \(\!<0\) dà \(\ge 0\). In particolare, \(\cos^2 x>\tfrac12\implies |\cos x|>\tfrac{1}{\sqrt2}\).  
   \end{itemize}
\end{enumerate}

\noindent
\textbf{Soluzione finale:}  
\[
\begin{aligned}
&\text{(i) } x = \frac{\pi}{2}+k\pi \quad(\cos x=0)\quad\text{sono soluzioni,}\\
&\text{(ii) } |\cos x|>\tfrac{1}{\sqrt2}\quad\Longrightarrow\quad \cos^2 x>\tfrac12 \quad\text{(con }x\neq \pm\tfrac{\pi}{4}+k\pi\text{, etc.)}
\end{aligned}
\]
Unendo i vari vincoli (escludendo i punti dove il denominatore si annulla) si ottiene l’insieme degli \(x\) che soddisfano la disequazione.  
\end{esempio}

\bigskip


Spesso conviene illustrare la soluzione anche su un \emph{grafico cartesiano} (per esempio, tracciando la funzione 
\(\displaystyle f(x)=\frac{\sin^2 x -1}{\,1 - 2\,\cos^2 x\,}\) 
e individuando le zone in cui \(f(x)\ge 0\)), e \emph{su un cerchio goniometrico}, evidenziando i quadranti o gli archi \emph{non ammissibili} (in \textcolor{red}{rosso}) o \emph{soluzione} (in \textcolor{blue}{blu}).

\begin{center}
\begin{tikzpicture}[scale=1.6, line cap=round, line join=round]

% Cerchio goniometrico di raggio 1
\draw[thick] (0,0) circle(1);

% Assi
\draw[->] (-1.2,0) -- (1.2,0) node[right] {$x$};
\draw[->] (0,-1.2) -- (0,1.2) node[above] {$y$};

% Esempio: coloriamo in rosso i punti "vietati"
% (ad es. cos x=±1/sqrt2) => x=±pi/4, ±3pi/4,... 
% Mettiamo alcuni di questi come segni rossi
\foreach \k in {0,...,3}{%
  \pgfmathsetmacro{\ang}{45+90*\k}
  \fill[red] ({cos(\ang)},{sin(\ang)}) circle(0.05);
}

% Esempio: coloriamo in blu un arco che rappresenta la parte di soluzione
% (ad es. |cos x|>1/sqrt2 => x in zone vicine all'asse x)
% Diciamo che "soluzione" e' intorno a 0°, 180°, etc.
\draw[blue, very thick, domain=-25:25] plot({cos(\x)}, {sin(\x)});
\draw[blue, very thick, domain=155:205] plot({cos(\x)}, {sin(\x)});
\draw[blue, very thick, domain=335:385] plot({cos(\x)}, {sin(\x)});

% Etichetta dell'origine
\node at (0,0) [below left] {$O$};

\end{tikzpicture}
\end{center}

\noindent
Nell’esempio sopra, i \textcolor{red}{punti rossi} rappresentano \emph{valori esclusi} (dove \(\cos x= \pm \frac{1}{\sqrt2}\)), mentre gli \textcolor{blue}{archi blu} indicano intervalli di \emph{soluzione} (qui mostrati in modo schematizzato). Naturalmente, occorre poi ripetere o traslare tali archi in tutti i giri possibili. 

\subsec{Sistemi di Equazioni e Disequazioni Goniometriche [2]}

Oltre a singole equazioni (o disequazioni) goniometriche, possiamo trovarci di fronte a \emph{sistemi} in cui compaiono funzioni trigonometriche (\(\sin x\), \(\cos x\), \(\tan x\), ecc.) in più di una condizione simultanea. Risolvere un sistema goniometrico significa determinare \emph{tutti gli angoli} che \emph{soddisfano insieme} le varie equazioni/disequazioni presenti. 

\medskip

\noindent
\textbf{Considerazioni generali:}
\begin{itemize}
\item \emph{Uso delle identità}: spesso i sistemi coinvolgono somme e prodotti di \(\sin x\), \(\cos x\), \(\tan x\). Ricordare identità come 
  \(\sin^2 x + \cos^2 x=1\), 
  \(\sin(2x)=2\sin x\,\cos x\), 
  \(\cos(2x)=\cos^2 x - \sin^2 x\), 
  e le \emph{formule di addizione/sottrazione} (\(\sin(\alpha\pm\beta)\), \(\cos(\alpha\pm\beta)\)) può permettere di trasformare o semplificare le espressioni.
\item \emph{Domini e periodi}: ogni funzione trigonometrica ha punti di discontinuità o zone non definite (\(\tan x\) e \(\sec x\) non definite quando \(\cos x=0\), ecc.). È fondamentale \emph{escludere} tali valori dall’insieme delle soluzioni e \emph{ripetere} la ricerca su tutti i periodi appropriati (\(2\pi\) per \(\sin x\) e \(\cos x\), \(\pi\) per \(\tan x\), \(\cot x\), ecc.).
\end{itemize}

\medskip

\noindent
\textbf{Metodi generali di risoluzione di sistemi goniometrici}:

\paragraph{1. Metodo della Sostituzione}
In vari sistemi, una prima equazione può fornire un’espressione per \(\sin x\) o \(\cos x\) (o altre funzioni) che possiamo \emph{sostituire} nella seconda (o nelle successive) equazioni. Ad esempio, se dal primo vincolo \(\sin x + \cos x=1\) deduciamo \(\sin x=1-\cos x\), potremo sostituire \(\sin x\) con \(1-\cos x\) in un’altra condizione, magari \(\sin x\,\cos x>0\). Questa tecnica:
\begin{itemize}
\item \emph{trasforma} il problema goniometrico in uno di \emph{equazioni algebriche} (spesso polinomiali) in \(\cos x\) o \(\sin x\);
\item \emph{riduce} la dimensionalità del sistema, passando da due o più funzioni a una singola incognita trigonometrica.
\end{itemize}
Dopo aver trovato i possibili valori di \(\cos x\) o \(\sin x\), si ricostruiscono gli angoli corrispondenti \emph{e} si verifica che le soluzioni rispettino \emph{tutte} le condizioni del sistema.

\paragraph{2. Metodo della Riduzione}
Quando compaiono funzioni come \(\sin(2x)\), \(\cos(3x)\), \(\tan(5x)\), o combinazioni di \(\sin x\) e \(\cos x\) in diverse equazioni, può essere vantaggioso \emph{ridurre} il problema definendo una nuova variabile, per esempio \(\theta = 2x\) o \(\theta=3x\). Così, \(\sin(2x)\) diventa \(\sin\theta\) e \(\cos(3x)\) diventa \(\cos(\tfrac{3}{2}\theta)\), ecc. A volte, si applica la riduzione per \(\theta=2x\) a un’intera disequazione, ricavando poi la soluzione in \(\theta\) e \emph{dividendo} successivamente per 2 (o 3, 5, \ldots) per tornare alla variabile \(x\). Questa strategia:
\begin{itemize}
\item \emph{semplifica} l’analisi dei periodi (ad esempio \(\tan(2x)\) ha periodo \(\tfrac{\pi}{2}\) in \(x\), ma se poniamo \(\theta=2x\), allora \(\tan\theta\) ha periodo \(\pi\) in \(\theta\));
\item \emph{permette} di disegnare un cerchio goniometrico in termini di \(\theta\) invece che di \(x\).
\end{itemize}
Attenzione però che \(\theta=2x\) implica \(\theta\in\mathbb{R}\) se \(x\in\mathbb{R}\), e le soluzioni vanno poi \emph{riscandite} per ottenere la forma generale in \(x\).

\medskip

Per alcuni sistemi, specialmente quelli che coinvolgono \(\sin x\) e \(\cos x\) separatamente, è comodo rappresentare \((\cos x, \sin x)\) come punto sul cerchio, e \emph{colorare} regioni o curve che soddisfano i vincoli. Invece, se compaiono \(\sin(2x)\) o \(\cos(3x)\), l’interpretazione diretta sul cerchio risulta meno immediata, ma si può ridurre a un \(\theta\)-substituzione (\(\theta=2x\) o \(\theta=3x\)) e procedere come nei casi di singole equazioni/disequazioni.

\begin{center}
\begin{tikzpicture}[scale=1.4, line cap=round, line join=round]

% Cerchio goniometrico di raggio 1
\draw[thick] (0,0) circle(1);

% Assi
\draw[->] (-1.2,0) -- (1.2,0) node[right] {$x$};


% Esempio di regioni: sin x < 0 => parte bassa del cerchio
\begin{scope}
  \clip (0,0) circle(1);
  \fill[blue!15] plot[domain=180:360] ({cos(\x)},{sin(\x)}) -- cycle;
\end{scope}

% Etichetta dell'origine
\node at (0,0) [below left] {$O$};
\draw[->] (0,-1.2) -- (0,1.2) node[above] {$y$};
\end{tikzpicture}
\end{center}

\noindent
Nell’immagine sopra, la \emph{semicirconferenza} inferiore (in blu) indica \(\sin x<0\). Eventualmente, si possono sovrapporre altre curve o linee per rappresentare \(\cos(2x)\ge \tfrac12\), anche se in questo caso conviene ridurre a \(\theta=2x\) e disegnare un cerchio \emph{di} \(\theta\). 

\bigskip

\begin{esempio}
\[
\begin{cases}
\sin x + \cos x = 1,\\[4pt]
\sin x \,\cos x \;\ge\; 0.
\end{cases}
\]
\textbf{Soluzione:}
\begin{enumerate}
\item \emph{Prima equazione:} \(\sin x + \cos x = 1.\)  
  Usiamo la formula \((\sin x + \cos x)^2 = \sin^2 x + 2\sin x \cos x + \cos^2 x = 1 + 2\sin x \cos x.\) Quindi
  \[
    (1)^2 = 1 + 2\,\sin x \cos x
    \quad\Longrightarrow\quad
    1 = 1 + 2\,\sin x \cos x
    \quad\Longrightarrow\quad
    \sin x \cos x = 0.
  \]
  Dalla \(\sin x + \cos x = 1\) e \(\sin x \cos x = 0\) deduciamo che \(\sin x=0\) o \(\cos x=0\). Ma \(\sin x + \cos x=1\) esclude alcuni casi:
  \begin{itemize}
    \item Se \(\sin x=0\), allora \(\cos x=1\). Quindi \(x=2k\pi\).  
    \item Se \(\cos x=0\), allora \(\sin x=1\). Quindi \(x=\tfrac{\pi}{2}+2k\pi\).
  \end{itemize}

\item \emph{Seconda equazione (disequazione):} \(\sin x \,\cos x \ge 0.\)  
  Ciò significa che \(\sin x\) e \(\cos x\) hanno lo \emph{stesso segno} (entrambe \(\ge 0\) o \(\le 0\)).

\item \emph{Verifica con le soluzioni precedenti:}  
  \begin{itemize}
    \item \(x=2k\pi\): Qui \(\sin(2k\pi)=0\), \(\cos(2k\pi)=1\). Il prodotto \(\sin x\,\cos x=0\ge 0\). E \(\sin x + \cos x=1\). \emph{Accettabile}.  
    \item \(x=\tfrac{\pi}{2}+2k\pi\): Qui \(\sin(\tfrac{\pi}{2}+2k\pi)=1\), \(\cos(\tfrac{\pi}{2}+2k\pi)=0\). Il prodotto \(\sin x\,\cos x=0\ge 0\). E \(\sin x + \cos x=1\). \emph{Accettabile} anche questa.  
  \end{itemize}

\item \emph{Conclusione:} Le soluzioni del sistema sono
\[
x=2k\pi
\quad\text{oppure}\quad
x=\frac{\pi}{2}+2k\pi,
\quad k\in\mathbb{Z}.
\]
\end{enumerate}
\end{esempio}

\bigskip

\begin{esempio}
\[
\begin{cases}
\sin^2 x - \cos^2 x = 0,\\[4pt]
\tan x > 0.
\end{cases}
\]
\textbf{Soluzione:}
\begin{enumerate}
\item \(\sin^2 x - \cos^2 x=0\) implica \(\sin^2 x=\cos^2 x\). Dunque \(\sin^2 x/\cos^2 x=1\) \(\Rightarrow \tan^2 x=1\) \(\Rightarrow \tan x=\pm1\). Quindi
  \[
    \tan x=1
    \quad\text{o}\quad
    \tan x=-1.
  \]
\item \(\tan x>0\) significa che \(\sin x\) e \(\cos x\) hanno lo stesso segno (primo e terzo quadrante). Con \(\tan x=\pm1\), otteniamo:
  \begin{itemize}
    \item \(\tan x=1\) con \(\tan x>0\). Dà \(x=\tfrac{\pi}{4}+k\pi\). Occorre \(\sin x\) e \(\cos x\) dello stesso segno. In \(\tfrac{\pi}{4}+k\pi\), \(\tan x=1\) è sempre \emph{positivo}, dunque \emph{valido per ogni \(k\in\mathbb{Z}\)}.
    \item \(\tan x=-1\) non soddisfa \(\tan x>0\). Quindi \(\tan x=-1\) è esclusa.
  \end{itemize}

\item \emph{Conclusione:} Le soluzioni sono
\[
x=\frac{\pi}{4}+k\pi,\quad k\in\mathbb{Z}.
\]
\end{enumerate}
\end{esempio}

\bigskip

\begin{esempio}
\[
\begin{cases}
\cos(2x)\ge \tfrac12,\\[4pt]
\sin x < 0.
\end{cases}
\]
\textbf{Soluzione:}
\begin{enumerate}
\item \(\cos(2x)\ge \tfrac12\). Sappiamo che \(\cos \theta \ge \tfrac12\) implica \(\theta\in [-\tfrac{\pi}{3}+2k\pi,\tfrac{\pi}{3}+2k\pi]\) oppure \(\theta\in [\dots]\) a seconda dei periodi. In particolare,
  \[
    2x \in \bigcup_{k\in\mathbb{Z}} 
    \Bigl[-\tfrac{\pi}{3}+2k\pi,\;\tfrac{\pi}{3}+2k\pi\Bigr].
  \]
  Dividendo per 2,
  \[
    x \in \bigcup_{k\in\mathbb{Z}}
    \Bigl[-\tfrac{\pi}{6}+k\pi,\;\tfrac{\pi}{6}+k\pi\Bigr].
  \]

\item \(\sin x<0\). La funzione \(\sin x\) è negativa nei quarti 3 e 4, ossia \((\pi,2\pi)\) in un giro. In generale,
  \[
    x \in \bigcup_{k\in\mathbb{Z}}
    (\pi + 2k\pi,\;2\pi + 2k\pi).
  \]

\item \emph{Intersezione di questi due insiemi}: Bisogna sovrapporre i segmenti \(\bigl[-\tfrac{\pi}{6}+k\pi,\tfrac{\pi}{6}+k\pi\bigr]\) con i \((\pi+2k\pi,2\pi+2k\pi)\). Spesso conviene \emph{disegnare} un asse orizzontale e marcare tali intervalli, scoprendo in quali sottointervalli \(\sin x<0\) e \(\cos(2x)\ge\tfrac12\) valgono \emph{insieme}.

\item \emph{Conclusione (schematica)}: L’intersezione fornisce dei piccoli archi in cui \(x\) sta \emph{nella parte finale} di \([k\pi-\tfrac{\pi}{6},\,k\pi+\tfrac{\pi}{6}]\) e \(\sin x<0\) (quindi \(x> \pi +2m\pi\)). La descrizione finale si esprime con unione di segmenti come
  \[
    x \in \bigcup_{m\in\mathbb{Z}} 
    \Bigl[
      \pi + 2m\pi,\; 
      \tfrac{7\pi}{6} + 2m\pi
    \Bigr].
  \]
  (Verifica con un grafico o un diagramma su linea per un riscontro.)
\end{enumerate}
\end{esempio}

\subsec{Applicazioni alla Topografia [3]}
Le \emph{tecniche goniometriche} trovano ampio impiego in topografia, dove occorre misurare altezze (di torri, montagne, edifici) e distanze (tra punti non facilmente accessibili) \emph{senza} dover ricorrere direttamente a strumenti di misura che raggiungano fisicamente quei luoghi. Di seguito, illustriamo alcuni esempi di come i sistemi di equazioni/disequazioni goniometriche possano modellare queste situazioni.

\begin{itemize}
\item \textbf{Misura dell’altezza di una torre.}  
  Immaginiamo di voler determinare l’altezza di un campanile, visibile da due punti differenti sul terreno (ad esempio \(P\) e \(Q\)), noti e orizzontalmente distanti fra loro. Se in entrambi i punti misuriamo \emph{l’angolo di elevazione} \(\alpha\) e \(\beta\) verso la sommità del campanile, possiamo impostare un \emph{sistema} goniometrico:
  \[
    \tan\alpha 
    = \frac{h}{\,d\,}, 
    \quad
    \tan\beta 
    = \frac{h}{\,d - \Delta\,}.
  \]
  Qui \(h\) è l’altezza incognita del campanile, \(d\) e \(d-\Delta\) sono le distanze orizzontali (con \(\Delta\) la differenza tra le posizioni di \(P\) e \(Q\)). Risolvendo tale sistema (spesso per \(\alpha,\beta\) e \(\Delta\) noti), otteniamo \(h\).

\item \textbf{Misura di una montagna.}  
  Analogamente, se dobbiamo calcolare l’altezza di una montagna da due punti a diversa elevazione, potremmo avere un sistema più complesso, comprendente \(\sin\) e \(\cos\) di angoli (ad esempio, se la linea di vista forma un’angolazione obliqua rispetto al terreno). Ancora una volta, le \emph{relazioni trigonometriche} forniscono equazioni (o disequazioni) che vincolano i parametri: la \emph{differenza di quota}, gli \emph{angoli di elevazione}, e le \emph{distanze orizzontali}.

\item \textbf{Misura di distanze non accessibili.}  
  In topografia è frequente dover stimare la distanza fra due punti \(A\) e \(B\) separati da ostacoli (fiumi, vallate). Effettuando misure di \emph{angoli} da un terzo punto \(C\) o da più punti noti, si costruiscono \emph{sistemi di triangoli} in cui compaiono equazioni come
  \[
    \frac{AB}{\sin\angle C}
    = \frac{BC}{\sin\angle A}
    = \frac{AC}{\sin\angle B}
  \]
  (Teorema dei Seni), oppure formule di proiezione e prodotti (Teorema del Coseno). Il sistema risultante è \emph{goniometrico} e ci permette di ricavare \(\overline{AB}\) (la distanza incognita) una volta note le misure di angoli e gli altri lati.
\end{itemize}

\paragraph{Sistemi Goniometrici in Topografia}
Quando ci troviamo di fronte a \emph{due o più} condizioni — per esempio, \(\tan\alpha_1=h/(d_1)\) e \(\tan\alpha_2=h/(d_2)\), oppure \(\angle A+\angle B+\angle C=180^\circ\) in un \emph{triangolo di posizionamento} — si crea un \emph{sistema} di equazioni/disequazioni goniometriche. Le \emph{strategie di risoluzione} restano le stesse:
\begin{enumerate}
\item \textbf{Sostituzione}: Se la prima relazione dà \(h=d\tan\alpha\), possiamo sostituirla in un’altra. Oppure, se una relazione fornisce \(\sin\theta\), la si immette in una formula con \(\cos\theta\).  
\item \textbf{Riduzione}: Se compaiono funzioni come \(\sin(2\theta)\) o \(\tan(3\theta)\), possiamo definire \(\phi=2\theta\) (o \(\phi=3\theta\)) e riscrivere l’intero sistema in termini di \(\phi\).
\end{enumerate}

\noindent
Spesso, \emph{l’interpretazione geometrica} aiuta: i punti su un \emph{cerchio goniometrico} corrispondono a determinati angoli di elevazione, e la soluzione del sistema diventa la \emph{collezione} di archi o regioni che \emph{contemporaneamente} soddisfano tutte le condizioni. In topografia, si riflette questo passaggio “angolo \(\leftrightarrow\) posizione” nelle costruzioni di triangoli e poligoni di rilevamento.

\medskip

\noindent
\textbf{Esempio schematico:}  
Supponiamo di avere un \emph{punto} \(P\) da cui osserviamo la cima di una torre \(T\). La distanza orizzontale \(PT\) non è direttamente misurabile, ma possiamo misurare \(\alpha=\angle TPH\) (angolo di elevazione rispetto all’orizzontale) e sappiamo la nostra altezza strumentale \(PH\). Se \(\overline{TH}=h\) (incognita) e \(\overline{PT}=d\), otteniamo il sistema:
\[
\begin{cases}
\tan\alpha = \dfrac{h}{\,d\,},\\
h + H_0 = \text{altezza totale della torre},\\
\text{(altri vincoli se misuriamo da un secondo punto, ecc.)}
\end{cases}
\]
Risolvendo e verificando i valori, si ottiene l’altezza incognita della torre. Rappresentare \(\alpha\) e \(\beta\) su un cerchio goniometrico permette di \emph{visualizzare} le possibili soluzioni e gli \emph{intervalli} di validità (ad esempio, se l’angolo di elevazione supera i \(90^\circ\), la configurazione fisica cambia).

\smallskip

\noindent
\textbf{Conclusione:} Le \emph{applicazioni topografiche} dei sistemi goniometrici si basano sulle stesse idee di \emph{sostituzione} e \emph{riduzione} illustrate in precedenza, arricchite dalla \emph{geometria} del problema (angoli di elevazione, distanze orizzontali, triangoli di rilevamento). La rappresentazione sul \emph{cerchio goniometrico} resta uno strumento concettuale per comprendere gli angoli e i vincoli, mentre la risoluzione formale si concretizza in equazioni e disequazioni trigonometriche. 

```
### Invoice
```LaTeX
\section*{Invoice}

\begin{tabular}{l l}
    \textbf{Invoice No.:} & 6. \\
    \textbf{Invoice Date:} & 19.03.2025\\
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
    Delivery Date: & \textbf{14.03.2025 - 19.03.2025}\\
    Quantity of Services: & \textbf{122 pages} \\
    Payment per Page: & \textbf{10€} \\
    Total Amount (including VAT): & \textbf{1220€}\\


&\\

\noindent\textbf{Bank Information:} \\
    Account Holder: & \textbf{Simone Testino} \\
    IBAN: & \textbf{IT94I0338501601100080084122} \\
    BIC/SWIFT: & \textbf{ISYBITMM} \\
    Bank Name: & \textbf{Isybank by Intesa San Paolo, Italy} \\
\end{tabular}
```