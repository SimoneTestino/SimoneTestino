---
draft: true
date: 2025-04-03
---
During the work for the [[Futura Abstract and Spacial Logic Quizzes]] (i.e. the writing of the code in [[Manim Code for Futura Abstract and Spacial Logic Quizzes]]), I realised that writing in Python using these packages is very accessible—especially with the very accurate guide from [Manim Community](https://docs.manim.community/en/stable/index.html). This quickly led me to conclude that I could use it to produce video material for Futura’s recorded mathematics lectures.

This approach could clearly apply not only for the [[ADT Forze Armate]] (i.e. [[Futura Military]]), for which I currently work, but also for other branches of Futura, such as the team developing material for the medicine entry exam (despite the fact that I suppose this branch might encounter some difficulties with the reform of the medicine examination).

I initially sketched the idea in a chat with Martina, for whom I am writing the [[Futura Abstract and Spacial Logic Quizzes]], but the proposal was ignored. Another option would be to text Giulia instead, for whom I wrote the [[Futura Math Didactic Document]], since, as far as I remember, they will be producing some video material based on the documents I created. It might be interesting to make a draft video on one particularly appealing topic and send it as a test to her, and potentially to Stefano too, who is directing the entire [[ADT Forze Armate]] part of the company.


What follows are some attempts in producing this first sample to be sent to Giulia and, eventually, Stefano.

---
### Algebraic System
```Python
class ExampleFunctionGraph(Scene):

def construct(self):

# Creiamo il piano cartesiano.

axes = Axes(

x_range=[-5, 5, 1],

y_range=[-5, 5, 1],

x_length=10,

y_length=10

)

self.add(axes)

  

# Creiamo i ValueTracker per il coefficiente angolare (m) e l'intercetta (q) della retta rossa.

m_tracker = ValueTracker(2)

q_tracker = ValueTracker(1)

  

# Disegniamo la retta rossa che si aggiorna dinamicamente in base a m e q.

retta_rossa = always_redraw(lambda: FunctionGraph(

lambda t: m_tracker.get_value() * t + q_tracker.get_value(),

x_range=[-5, 5],

color=RED,

))

self.add(retta_rossa)

  

# Creiamo la formula della retta rossa, che si aggiorna dinamicamente,

# con un colore tendente al rosso (più chiaro).

eq_rossa = always_redraw(lambda: MathTex(

f"y = {m_tracker.get_value():.1f}x + {q_tracker.get_value():.1f}",

font_size=48,

color="#FF9999"

).to_corner(UL))

self.add(eq_rossa)

  

# Animiamo la variazione di m e successivamente quella di q per la retta rossa.

self.play(m_tracker.animate.set_value(-2), run_time=3)

self.wait(1)

self.play(q_tracker.animate.set_value(-1), run_time=3)

self.wait(1)

  

# Fino a qui abbiamo realizzato la parte per una singola retta rossa.

# Ora passiamo ad aggiungere una seconda retta blu.

  

# Disegniamo la retta blu (con coefficiente angolare 1 e intercetta 0)

# facendola apparire elegantemente tramite FadeIn.

retta_blu = FunctionGraph(

lambda t: 1 * t + 0, x_range=[-5, 5],

color=BLUE,

)

self.play(FadeIn(retta_blu), run_time=2)

  

# Creiamo l'equazione della retta blu, con un colore tendente al blu (più chiaro),

# posizionandola sotto l'equazione della retta rossa.

eq_blu = MathTex("y = 1x + 0", font_size=48, color="#9999FF")

eq_blu.next_to(eq_rossa, DOWN, aligned_edge=LEFT, buff=0.5)

self.play(Write(eq_blu))

self.wait(1)

  

# Ora creiamo un'animazione in più in cui mettiamo a sistema le due equazioni.

# La scritta del sistema rimarrà a sinistra per tutte le scene successive.

sistema = MathTex(

r"\begin{cases}"

r"y = -2x - 1 \\"

r"y = x"

r"\end{cases}",

font_size=48,

color=WHITE

).to_corner(UL)

self.play(Transform(VGroup(eq_rossa, eq_blu), sistema), run_time=2)

self.wait(1)

  

# Calcoliamo il punto di incidenza delle due rette.

# Per la retta rossa: y = -2x - 1 e per la retta blu: y = x.

# Ponendo -2x - 1 = x, otteniamo x = -1/3 e dunque y = -1/3.

punto_incidenza = axes.c2p(-1/3, -1/3)

  

# Disegniamo il punto di incidenza come un dot bianco.

dot_incidenza = Dot(punto_incidenza, color=WHITE)

self.play(FadeIn(dot_incidenza), run_time=2)

self.wait(1)

  

# Aggiungiamo le coordinate del punto, posizionate sotto la scritta del sistema.

coord_label = MathTex("(-\\frac{1}{3},\\,-\\frac{1}{3})", font_size=36, color=YELLOW)

coord_label.next_to(sistema, DOWN, aligned_edge=LEFT, buff=0.5)

self.play(Write(coord_label), run_time=2)

self.wait(2)

  

%manim -qm -v WARNING ExampleFunctionGraph
```