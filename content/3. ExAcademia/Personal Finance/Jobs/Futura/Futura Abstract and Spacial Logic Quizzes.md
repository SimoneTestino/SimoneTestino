---
draft: false
date: 2025-04-02
---
Following the [[Futura Logic Quizzes]], I outline here the main components needed to develop the code that generates the figures. I will use the [Manim Community](https://docs.manim.community/en/stable/index.html) library.

The first step consists in building the general framework, which I implemented in [[Manim Code for Futura Abstract and Spacial Logic Quizzes#Grid]]. This provides the basic structure into which the various figures will be inserted. In this framework, cells can be obscured, and one cell can be marked as the _asked cell_—that is, the missing element that the student must replace by selecting from among the _option cells_. To complete this part, I also implemented a function capable of drawing figures in any cell of the grid or in any of the option cells.

The second part of the programme, detailed in [[Manim Code for Futura Abstract and Spacial Logic Quizzes#Automation of Concepts]], focuses on automating quiz generation. This component requires the concepts defined in [[Futura Abstract and Spacial Logic Quizzes#Concepts]], and aims to automatically produce quizzes that adhere to the logic of those concepts. The result of each run is saved locally in a folder. Concretely, this process consists of a simple `for` loop that iterates over all variables left free by each concept, generating a large collection of distinct quizzes.
## Concepts
To take some inspiration I first consult some similar examples given by manual of IQ tests that I previously collected. In particular I made the [[Manim Code for Futura Abstract and Spacial Logic Quizzes#Gird]] taking inspiration from the [[LogicQuizExample.jpeg]]. From a similar pattern I draw the first example.