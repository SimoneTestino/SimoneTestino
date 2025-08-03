Here is the code I usually add to all documents created after October 2024 which makes typing in $\LaTeX$ easier and quicker. I also implemented the _gaming cards symbols_ which I find funny to use.

``` LaTeX
\documentclass[12pt]{article}
\date{\today}
\author{Simone Testino}

% Required Packages
\usepackage{amsmath, amssymb, amsfonts, amsthm, mathtools}
\usepackage{geometry}
\usepackage{graphicx}
\usepackage{tikz}
\usepackage{quiver}
\usepackage[dvipsnames]{xcolor}
\usepackage{csquotes}
\usepackage{ulem}
\usepackage{hyperref}
\usepackage{wasysym}
\usepackage{eurosym}
\usepackage{enumerate}

% Page Layout Configuration
\usepackage{geometry}
\geometry{
  left=2cm,
  right=2cm,
  top=2cm,
  bottom=2cm
}

% Mathematical Shortcuts
% Font Styles
\renewcommand{\b}[1]{\mathbb{#1}}
\renewcommand{\c}[1]{\mathcal{#1}}
\newcommand{\f}[1]{\mathfrak{#1}}

% Greek Letters
\newcommand{\vf}{\varphi}
\newcommand{\p}{\psi}

% Quantifiers
\newcommand{\fa}[1]{\forall_{#1}}
\newcommand{\ex}[1]{\exists_{#1}}

% Logical Operators
\renewcommand{\a}{\land}
\renewcommand{\o}{\lor}
\newcommand{\n}{\lnot}

% Categories and Sets
\newcommand{\Cat}{\textbf{Cat}}
\newcommand{\Set}{\textbf{Set}}
\newcommand{\subs}{\subseteq}
\newcommand{\sups}{\supseteq}

% Modal Logic
\newcommand{\sq}{\Box}
\newcommand{\dm}{\lozenge}

% Text Formatting
\newcommand{\q}[1]{\enquote{#1}}
\newcommand{\txr}[1]{\textcolor{red}{#1}}
\newcommand{\txb}[1]{\textcolor{blue}{#1}}

% Logical Symbols
\newcommand{\md}{\models}
\newcommand{\vd}{\vdash}
\newcommand{\forces}{\vDash}
\newcommand{\az}{\aleph_0}

% Proof Phrases
\newcommand{\fca}{for contradiction assume }
\newcommand{\Fca}{For contradiction assume }
\newcommand{\fn}[1]{\footnote{#1}}

% Implications
\newcommand{\To}{\Rightarrow}
\newcommand{\oT}{\Leftarrow}
\newcommand{\ToT}{\Leftrightarrow}
\newcommand{\ot}{\leftarrow}
\newcommand{\tot}{\leftrightarrow}

% Logical Languages
\newcommand{\Prop}{\text{Prop}}
\newcommand{\Atom}{\text{Atom}}
\newcommand{\FV}{\text{FV}}
\newcommand{\FOL}{\mathcal{L}_{FOL}}
\newcommand{\PL}{\mathcal{L}_{PL}}
\newcommand{\Le}{\mathcal{L}_{\epsilon}}
\newcommand{\Lgr}{\mathcal{L}_{gr}}
\newcommand{\K}{\text{K}}
\newcommand{\Kv}{\text{Kv}}
\newcommand{\dom}{\text{dom}}

% Theorem Environments
\theoremstyle{definition}
\newtheorem{Definition}{Definition}[section]
\newtheorem*{definition}{Definition}
\newtheorem{Exercise}[Definition]{Exercise}
\newtheorem*{exercise}{Exercise}
\newtheorem{Question}[Definition]{Question}
\newtheorem*{redquestion}{\textcolor{red}{Question}}
\newtheorem{redQuestion}{\textcolor{red}{Question}}

\theoremstyle{plain}
\newtheorem{Theorem}[Definition]{Theorem}
\newtheorem{Proposition}[Definition]{Proposition}
\newtheorem{Lemma}[Definition]{Lemma}
\newtheorem{Corollary}[Definition]{Corollary}
\newtheorem*{corollary}{Corollary}
\newtheorem*{theorem}{Theorem}
\newtheorem*{proposition}{Proposition}
\newtheorem*{lemma}{Lemma}
\newtheorem*{answer}{Answer}
\newtheorem{Answer}{Answer}
\newtheorem*{statement}{Statement}
\newtheorem{Statement}[Definition]{Statement}

\theoremstyle{remark}
\newtheorem{Remark}[Definition]{Remark}
\newtheorem*{remark}{Remark}
\newtheorem{Hypothesis}[Definition]{Hypothesis}
\newtheorem*{hypothesis}{Hypothesis}
\newtheorem*{example}{Example}
\newtheorem{Example}[Definition]{Example}
\newtheorem*{question}{Question}
\newtheorem{redProblem}{\textcolor{red}{Problem}}
\newtheorem*{redproblem}{\textcolor{red}{Problem}}

% Custom Proof Environments
\newenvironment{happyproof}[1][\proofname]
  {\renewcommand\qedsymbol{\smiley{}}\proof[#1]}
  {\endproof}
 
\newenvironment{argument}[1][Argument]
  {\renewcommand\qedsymbol{}\proof[#1]}
  {\endproof}
 
\newenvironment{proof sketch}[1][\proofname]
  {\renewcommand\qedsymbol{}\proof[#1]}
  {\endproof}

% Hyperlink Setup
\hypersetup{
    colorlinks=true,
    linkcolor=darkgray,
    urlcolor=darkgray,
    citecolor=darkgray,
    pdfborder={0 0 0}
}

% Custom Hyperlink Commands
\newcommand{\hor}[2]{\href{#1}{\dashuline{#2}}}
\newcommand{\horf}[2]{\hor{#1}{#2}\footnote{\hor{#1}{#1}}}
\newcommand{\hro}[2]{\href{#2}{\dashuline{#1}}}
\newcommand{\hrof}[2]{\hro{#1}{#2}\footnote{\hor{#2}{#2}}}

% Package Finalization
\endinput
```