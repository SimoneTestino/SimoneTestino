---
draft: true
date: 2025-04-03
---

Following the reasoning outlined in [[Futura Logic Quizzes]], I decided to take on the job and begin working on it. To support this, I developed the following code, which I introduce in [[Futura Abstract and Spacial Logic Quizzes]]. This code is not publicly released, as it serves as a key component in the rapid and efficient production of the quizzes. I wrote it with the assistance of AI to accelerate development, using the Manim Community Library.
#### ShiftUP (2 - 15)
```Python
%%manim -ql BasicGrid

import numpy as np

import random

  

C = list(range(1, 10)) # Cell numbers

  

# Global configuration

config.background_color = WHITE

config.pixel_width = 1920

config.pixel_height = 1080

  

def string_to_color(color_str):

color_str = color_str.lower()

if color_str == "red":

return "#b22222"

elif color_str == "blue":

return "#336699"

elif color_str == "green":

return "#228b22"

elif color_str == "yellow":

return "#b8860b"

else:

return "#000000"

  

def create_diagonal_stripes(center, cell_size=2, num_stripes=8):

lines = VGroup()

center = np.array(center)

v = np.array([1, -1, 0]) / np.linalg.norm([1, -1, 0])

u = np.array([1, 1, 0]) / np.linalg.norm([1, 1, 0])

half = cell_size / 2

max_offset = cell_size / np.sqrt(2)

offsets = np.linspace(-max_offset, max_offset, num_stripes)

for offset in offsets:

t_min = -half * np.sqrt(2) + abs(offset)

t_max = half * np.sqrt(2) - abs(offset)

start = center + offset * u + t_min * v

end = center + offset * u + t_max * v

lines.add(Line(start, end, stroke_color=BLACK, stroke_width=2))

return lines

  

def create_interactive_grid(obscured_cells, asked_cell):

grid_lines = VGroup()

for x in [-3, -1, 1, 3]:

grid_lines.add(Line([x, -3, 0], [x, 3, 0], color=BLACK, stroke_width=2))

for y in [-3, -1, 1, 3]:

grid_lines.add(Line([-3, y, 0], [3, y, 0], color=BLACK, stroke_width=2))

cell_centers = []

for row in range(3):

for col in range(3):

x = -2 + col * 2

y = 2 - row * 2

cell_centers.append(np.array([x, y, 0]))

overlays = VGroup()

for i, center in enumerate(cell_centers):

cell_num = i + 1

if cell_num in obscured_cells:

overlays.add(create_diagonal_stripes(center))

if cell_num == asked_cell:

overlays.add(Text("?", font_size=72, color=BLACK).move_to(center))

return VGroup(grid_lines, overlays)

  

def insert_figures_in_cell(cell_number, figures, cell_size=2):

if cell_number <= 9:

row = (cell_number - 1) // 3

col = (cell_number - 1) % 3

center_x = -1.40 + col * 1.40

center_y = 2.4 - row * 1.40

cell_center = np.array([center_x, center_y, 0])

else:

option_centers = [

np.array([-4.35, -2.45, 0]), # A (10)

np.array([-4.6 + (2.355*1)+0.15, -2.45, 0]), # B (11)

np.array([-4.6 + (2.355*2)+0.1, -2.45, 0]), # C (12)

np.array([-4.6 + (2.355*3)+0.05, -2.45, 0]), # D (13)

np.array([-4.6 + (2.355*4), -2.45, 0]) # E (14)

]

cell_center = option_centers[cell_number - 10]

figures_group = VGroup()

for fig in figures:

if fig[0] == "P":

_, num_sides, side_length, offset_tuple, color_str, rotation_angle = fig

R = side_length / (2 * np.sin(np.pi / num_sides))

poly = RegularPolygon(n=num_sides, radius=R, color=string_to_color(color_str))

poly.rotate(rotation_angle * DEGREES)

poly.move_to(cell_center + np.array(offset_tuple + (0,)))

figures_group.add(poly)

elif fig[0] == "C":

_, _, radius, offset_tuple, color_str, _ = fig

circle = Circle(radius=radius, color=string_to_color(color_str))

circle.move_to(cell_center + np.array(offset_tuple + (0,)))

figures_group.add(circle)

return figures_group

  

# Initialize random cells with updated answer options

ans = [10, 11, 12, 13, 14]

tr = random.choice(ans)

Wr_1 = [element for element in ans if element != tr]

wr_1 = random.choice(Wr_1)

Wr_2 = [element for element in ans if element not in [tr, wr_1]]

wr_2 = random.choice(Wr_2)

Wr_3 = [element for element in ans if element not in [tr, wr_1, wr_2]]

wr_3 = random.choice(Wr_3)

Wr_4 = [element for element in ans if element not in [tr, wr_1, wr_2, wr_3]]

wr_4 = random.choice(Wr_4)

print(wr_4)

  
  

# Random cell selection logic remains the same

o1 = random.choice(C)

o2 = random.choice(C)

a = random.choice(C)

while (o1 == o2 or o1 == a or o2 == a) or \

(((o1 - 1) // 3) == ((o2 - 1) // 3) or ((o1 - 1) // 3) == ((a - 1) // 3) or ((o2 - 1) // 3) == ((a - 1) // 3)) or \

(((o1 - 1) % 3) == ((o2 - 1) % 3) or ((o1 - 1) % 3) == ((a - 1) % 3) or ((o2 - 1) % 3) == ((a - 1) % 3)):

o1 = random.choice(C)

o2 = random.choice(C)

a = random.choice(C)

  

class BasicGrid(Scene):

def construct(self):

interactive_grid = create_interactive_grid(obscured_cells=[o1, o2], asked_cell=a).shift(UP * 1)

# Create answer options including E

option_A = VGroup(

Text("A:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

option_B = VGroup(

Text("B:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

option_C = VGroup(

Text("C:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

option_D = VGroup(

Text("D:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

option_E = VGroup(

Text("E:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

options = VGroup(option_A, option_B, option_C, option_D, option_E).arrange(RIGHT, buff=0.6)

options.next_to(interactive_grid, DOWN, buff=1)

content = VGroup(interactive_grid, options).scale(0.7).center()

  

# Figure generation logic

F1 = ['C', 'P']

F2 = [3, 4, 5, 6]

Co = ['red', 'blue', 'yellow', 'green']

Ang = [0, 45, 90, 120, 150, 180, 270]

Row = [0, 1, 2]

d = random.choice([element for element in C if element not in [a, o1, o2]])

for r in Row:

fa1 = random.choice(F1)

fa2 = random.choice(F2)

coa = random.choice(Co)

anga = random.choice(Ang)

fb1 = random.choice(F1)

fb2 = random.choice(F2)

cob = random.choice(Co)

angb = random.choice(Ang) #[('C', 0.15, (0, 0))]

for c in [3*r + 1, 3*r + 2, 3*r + 3]:

if o1 != c and o2 != c and a != c:

content.add(

insert_figures_in_cell(c, [(fa1, fa2, 0.5, (0, 0), coa, anga)]),

insert_figures_in_cell(c, [(fb1, fb2, 0.15, (0, 0.25*((c+2)%3)), cob, angb)])

)

if c == d:

content.add(

insert_figures_in_cell(wr_3, [(fa1, fa2, 0.5, (0, 0), coa, anga)]),

insert_figures_in_cell(wr_3, [(fb1, fb2, 0.15, (0, 0.25*((c+2)%3)), cob, angb)])

)

elif c == a:

content.add(

insert_figures_in_cell(tr, [(fa1, fa2, 0.5, (0, 0), coa, anga)]),

insert_figures_in_cell(tr, [(fb1, fb2, 0.15, (0, 0.25*((c+2)%3)), cob, angb)])

)

elif c == o1:

content.add(

insert_figures_in_cell(wr_1, [(fa1, fa2, 0.5, (0, 0), coa, anga)]),

insert_figures_in_cell(wr_1, [(fb1, fb2, 0.15, (0, 0.25*((c+2)%3)), cob, angb)])

)

elif c == o2:

content.add(

insert_figures_in_cell(wr_2, [(fa1, fa2, 0.5, (0, 0), coa, anga)]),

insert_figures_in_cell(wr_2, [(fb1, fb2, 0.15, (0, 0.25*((c+2)%3)), cob, angb)])

)

content.add(

insert_figures_in_cell(wr_4, [(fa1, fb2, 0.5, (0, 0), coa, anga+0.2)]),

insert_figures_in_cell(wr_4, [(fb1, fa2, 0.15, (0, 0.25*((c+2)%3)), cob, angb)])

)

  

# Solution mapping

solution_map = {

10: 'A',

11: 'B',

12: 'C',

13: 'D',

14: 'E'

}

soluzione = solution_map.get(tr, 'Nessuna soluzione')

print(f"La soluzione corretta dell'esercizio è la {soluzione} dato che la figura interna più piccola viene spostata verso l'alto ogni volta che si procede a destra")

self.add(content)
```

#### AddSide (126 - 147)
```Python
%%manim -ql BasicGrid

import numpy as np

import random

  

C = list(range(1, 10)) # Cell numbers

  

# Global configuration

config.background_color = WHITE

config.pixel_width = 1920

config.pixel_height = 1080

  

def string_to_color(color_str):

color_str = color_str.lower()

if color_str == "red":

return "#b22222"

elif color_str == "blue":

return "#336699"

elif color_str == "green":

return "#228b22"

elif color_str == "yellow":

return "#b8860b"

else:

return "#000000"

  

def create_diagonal_stripes(center, cell_size=2, num_stripes=8):

lines = VGroup()

center = np.array(center)

v = np.array([1, -1, 0]) / np.linalg.norm([1, -1, 0])

u = np.array([1, 1, 0]) / np.linalg.norm([1, 1, 0])

  

half = cell_size / 2

max_offset = cell_size / np.sqrt(2)

offsets = np.linspace(-max_offset, max_offset, num_stripes)

  

for offset in offsets:

t_min = -half * np.sqrt(2) + abs(offset)

t_max = half * np.sqrt(2) - abs(offset)

start = center + offset * u + t_min * v

end = center + offset * u + t_max * v

lines.add(Line(start, end, stroke_color=BLACK, stroke_width=2))

return lines

  

def create_interactive_grid(obscured_cells, asked_cell):

grid_lines = VGroup()

for x in [-3, -1, 1, 3]:

grid_lines.add(Line([x, -3, 0], [x, 3, 0], color=BLACK, stroke_width=2))

for y in [-3, -1, 1, 3]:

grid_lines.add(Line([-3, y, 0], [3, y, 0], color=BLACK, stroke_width=2))

  

cell_centers = []

for row in range(3):

for col in range(3):

x = -2 + col * 2

y = 2 - row * 2

cell_centers.append(np.array([x, y, 0]))

  

overlays = VGroup()

for i, center in enumerate(cell_centers):

cell_num = i + 1

if cell_num in obscured_cells:

overlays.add(create_diagonal_stripes(center))

if cell_num == asked_cell:

overlays.add(Text("?", font_size=72, color=BLACK).move_to(center))

return VGroup(grid_lines, overlays)

  

def insert_figures_in_cell(cell_number, figures, cell_size=2):

if cell_number <= 9:

row = (cell_number - 1) // 3

col = (cell_number - 1) % 3

center_x = -1.40 + col * 1.40

center_y = 2.4 - row * 1.40

cell_center = np.array([center_x, center_y, 0])

else:

option_centers = [

np.array([-4.35, -2.45, 0]), # A (10)

np.array([-4.6 + (2.355*1)+0.15, -2.45, 0]), # B (11)

np.array([-4.6 + (2.355*2)+0.1, -2.45, 0]), # C (12)

np.array([-4.6 + (2.355*3)+0.05, -2.45, 0]), # D (13)

np.array([-4.6 + (2.355*4), -2.45, 0]) # E (14)

]

cell_center = option_centers[cell_number - 10]

  

figures_group = VGroup()

for fig in figures:

if fig[0] == "P":

_, num_sides, side_length, offset_tuple, color_str, rotation_angle = fig

R = side_length / (2 * np.sin(np.pi / num_sides))

poly = RegularPolygon(n=num_sides, radius=R, color=string_to_color(color_str))

poly.rotate(rotation_angle * DEGREES)

poly.move_to(cell_center + np.array(offset_tuple + (0,)))

figures_group.add(poly)

elif fig[0] == "C":

_, _, radius, offset_tuple, color_str, _ = fig

circle = Circle(radius=radius, color=string_to_color(color_str))

circle.move_to(cell_center + np.array(offset_tuple + (0,)))

figures_group.add(circle)

return figures_group

  

# Initialize random cells with updated answer options

ans = [10, 11, 12, 13, 14]

tr = random.choice(ans)

Wr_1 = [element for element in ans if element != tr]

wr_1 = random.choice(Wr_1)

Wr_2 = [element for element in ans if element not in [tr, wr_1]]

wr_2 = random.choice(Wr_2)

Wr_3 = [element for element in ans if element not in [tr, wr_1, wr_2]]

wr_3 = random.choice(Wr_3)

Wr_4 = [element for element in ans if element not in [tr, wr_1, wr_2, wr_3]]

wr_4 = random.choice(Wr_4)

print('wr_1:'+ str(wr_1))

print('wr_2:'+ str(wr_2))

print('wr_3:'+ str(wr_3))

print('wr_4:'+ str(wr_4))

  
  

# Random cell selection logic remains the same

o1 = random.choice(C)

o2 = random.choice(C)

a = random.choice(C)

while (o1 == o2 or o1 == a or o2 == a) or \

(((o1 - 1) // 3) == ((o2 - 1) // 3) or ((o1 - 1) // 3) == ((a - 1) // 3) or ((o2 - 1) // 3) == ((a - 1) // 3)) or \

(((o1 - 1) % 3) == ((o2 - 1) % 3) or ((o1 - 1) % 3) == ((a - 1) % 3) or ((o2 - 1) % 3) == ((a - 1) % 3)):

o1 = random.choice(C)

o2 = random.choice(C)

a = random.choice(C)

  

class BasicGrid(Scene):

def construct(self):

interactive_grid = create_interactive_grid(obscured_cells=[o1, o2], asked_cell=a).shift(UP * 1)

  

# Create answer options including E

option_A = VGroup(

Text("A:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

  

option_B = VGroup(

Text("B:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

  

option_C = VGroup(

Text("C:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

  

option_D = VGroup(

Text("D:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

  

option_E = VGroup(

Text("E:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

  

options = VGroup(option_A, option_B, option_C, option_D, option_E).arrange(RIGHT, buff=0.6)

options.next_to(interactive_grid, DOWN, buff=1)

  

content = VGroup(interactive_grid, options).scale(0.7).center()

  

# Figure generation logic

  

F1 = ['P']

  

F2 = [3, 4, 5, 6]

  

Co = ['red', 'blue', 'yellow', 'green']

  

Ang = [0, 45, 90, 120, 150, 180, 270]

  

Row = [0, 1, 2]

  

d_1 = random.choice([element for element in C if element not in [a, o1, o2]])

d_2 = random.choice([element for element in C if element not in [a, o1, o2, d_1]])

  
  
  

for r in Row:

  

fa1 = random.choice(F1)

  

fa2 = random.choice(F2)

  

coa = random.choice(Co)

  

anga = random.choice(Ang)

  
  
  

fb1 = random.choice(F1)

  

fb2 = random.choice(F2)

  

cob = random.choice(Co)

  

angb = random.choice(Ang) #[('C', 0.15, (0, 0))]

  
  
  

for c in [3*r + 1, 3*r + 2, 3*r + 3]:

  

if o1 != c and o2 != c and a != c:

  

content.add(

  

insert_figures_in_cell(c, [(fa1, fa2, 0.25, (-0.25, 0), coa, anga)]),

  

insert_figures_in_cell(c, [(fa1, fa2+(c+2)%3, 0.25, (0.25, 0), cob, anga+(c*30))])

  

)

  

if c == d_1:

print('wr_3 cell:'+str(c))

  

content.add(

  

insert_figures_in_cell(wr_3, [(fa1, fa2, 0.25, (-0.25, 0), coa, anga)]),

  

insert_figures_in_cell(wr_3, [(fa1, fa2+(c+2)%3, 0.25, (0.25, 0), cob, anga+(c*30))])

  

)

elif c == d_2:

print('wr_4 cell:'+str(c))

  

content.add(

  

insert_figures_in_cell(wr_4, [(fa1, fa2, 0.25, (-0.25, 0), coa, anga)]),

  

insert_figures_in_cell(wr_4, [(fa1, fa2+(c+2)%3, 0.25, (0.25, 0), cob, anga+(c*30))])

  

)

  

elif c == a:

print('tr cell:'+str(c))

  

content.add(

  

insert_figures_in_cell(tr, [(fa1, fa2, 0.25, (-0.25, 0), coa, anga)]),

  

insert_figures_in_cell(tr, [(fa1, fa2+(c+2)%3, 0.25, (0.25, 0), cob, anga+(c*30))])

  

)

  

elif c == o1:

print('wr_1 cell:'+str(c))

  

content.add(

  

insert_figures_in_cell(wr_1, [(fa1, fa2, 0.25, (-0.25, 0), coa, anga)]),

  

insert_figures_in_cell(wr_1, [(fa1, fa2+(c+2)%3, 0.25, (0.25, 0), cob, anga+(c*30))])

  

)

  

elif c == o2:

print('wr_2 cell:'+str(c))

  

content.add(

  

insert_figures_in_cell(wr_2, [(fa1, fa2, 0.25, (-0.25, 0), coa, anga)]),

  

insert_figures_in_cell(wr_2, [(fa1, fa2+1, 0.25, (0.25, 0), cob, anga+(c*30))])

  

)

  
  
  
  
  

# Solution mapping

  

solution_map = {

  

10: 'A',

  

11: 'B',

  

12: 'C',

  

13: 'D',

  

14: 'E'

  

}

  

soluzione = solution_map.get(tr, 'Nessuna soluzione')

  
  
  

print(f"La soluzione corretta dell'esercizio è la {soluzione}, in ogni riga ci sono due poligoni regolari ed il secondo nella prima colonna ha tanti lati quanti il primo ma poi vanno aumentando mano a mano che ci si sposta nelle colonne a destra. Colori ed angoli possono essere ignorati")

  

self.add(content)
```
#### ColShapeShift (52 -77)
```Python
%%manim -ql BasicGrid

  

import numpy as np

import random

  

C = list(range(1, 10)) # Cell numbers

  

# Global configuration

config.background_color = WHITE

config.pixel_width = 1920

config.pixel_height = 1080

  

def string_to_color(color_str):

color_str = color_str.lower()

if color_str == "red":

return "#b22222"

elif color_str == "blue":

return "#336699"

elif color_str == "green":

return "#228b22"

elif color_str == "yellow":

return "#b8860b"

else:

return "#000000"

  

def create_diagonal_stripes(center, cell_size=2, num_stripes=8):

lines = VGroup()

center = np.array(center)

v = np.array([1, -1, 0]) / np.linalg.norm([1, -1, 0])

u = np.array([1, 1, 0]) / np.linalg.norm([1, 1, 0])

half = cell_size / 2

max_offset = cell_size / np.sqrt(2)

offsets = np.linspace(-max_offset, max_offset, num_stripes)

for offset in offsets:

t_min = -half * np.sqrt(2) + abs(offset)

t_max = half * np.sqrt(2) - abs(offset)

start = center + offset * u + t_min * v

end = center + offset * u + t_max * v

lines.add(Line(start, end, stroke_color=BLACK, stroke_width=2))

return lines

  

def create_interactive_grid(obscured_cells, asked_cell):

grid_lines = VGroup()

for x in [-3, -1, 1, 3]:

grid_lines.add(Line([x, -3, 0], [x, 3, 0], color=BLACK, stroke_width=2))

for y in [-3, -1, 1, 3]:

grid_lines.add(Line([-3, y, 0], [3, y, 0], color=BLACK, stroke_width=2))

cell_centers = []

for row in range(3):

for col in range(3):

x = -2 + col * 2

y = 2 - row * 2

cell_centers.append(np.array([x, y, 0]))

overlays = VGroup()

for i, center in enumerate(cell_centers):

cell_num = i + 1

if cell_num in obscured_cells:

overlays.add(create_diagonal_stripes(center))

if cell_num == asked_cell:

overlays.add(Text("?", font_size=72, color=BLACK).move_to(center))

return VGroup(grid_lines, overlays)

  

def insert_figures_in_cell(cell_number, figures, cell_size=2):

if cell_number <= 9:

row = (cell_number - 1) // 3

col = (cell_number - 1) % 3

center_x = -1.40 + col * 1.40

center_y = 2.4 - row * 1.40

cell_center = np.array([center_x, center_y, 0])

else:

option_centers = [

np.array([-4.35, -2.45, 0]), # A (10)

np.array([-4.6 + (2.355*1)+0.15, -2.45, 0]), # B (11)

np.array([-4.6 + (2.355*2)+0.1, -2.45, 0]), # C (12)

np.array([-4.6 + (2.355*3)+0.05, -2.45, 0]), # D (13)

np.array([-4.6 + (2.355*4), -2.45, 0]) # E (14)

]

cell_center = option_centers[cell_number - 10]

figures_group = VGroup()

for fig in figures:

if fig[0] == "P":

_, num_sides, side_length, offset_tuple, color_str, rotation_angle = fig

R = side_length / (2 * np.sin(np.pi / num_sides))

poly = RegularPolygon(n=num_sides, radius=R, color=string_to_color(color_str))

poly.rotate(rotation_angle * DEGREES)

poly.move_to(cell_center + np.array(offset_tuple + (0,)))

figures_group.add(poly)

elif fig[0] == "C":

_, _, radius, offset_tuple, color_str, _ = fig

circle = Circle(radius=radius, color=string_to_color(color_str))

circle.move_to(cell_center + np.array(offset_tuple + (0,)))

figures_group.add(circle)

return figures_group

  

# Initialize random cells with updated answer options

ans = [10, 11, 12, 13, 14]

tr = random.choice(ans)

Wr_1 = [element for element in ans if element != tr]

wr_1 = random.choice(Wr_1)

Wr_2 = [element for element in ans if element not in [tr, wr_1]]

wr_2 = random.choice(Wr_2)

Wr_3 = [element for element in ans if element not in [tr, wr_1, wr_2]]

wr_3 = random.choice(Wr_3)

Wr_4 = [element for element in ans if element not in [tr, wr_1, wr_2, wr_3]]

wr_4 = random.choice(Wr_4)

print(wr_4) # Corrected from its original slight indent to be top-level

  

# Random cell selection logic remains the same

o1 = random.choice(C)

o2 = random.choice(C)

a = random.choice(C)

while (o1 == o2 or o1 == a or o2 == a) or \

(((o1 - 1) // 3) == ((o2 - 1) // 3) or ((o1 - 1) // 3) == ((a - 1) // 3) or ((o2 - 1) // 3) == ((a - 1) // 3)) or \

(((o1 - 1) % 3) == ((o2 - 1) % 3) or ((o1 - 1) % 3) == ((a - 1) % 3) or ((o2 - 1) % 3) == ((a - 1) % 3)):

o1 = random.choice(C)

o2 = random.choice(C)

a = random.choice(C)

  

class BasicGrid(Scene):

def construct(self):

interactive_grid = create_interactive_grid(obscured_cells=[o1, o2], asked_cell=a).shift(UP * 1)

# Create answer options including E

option_A = VGroup(

Text("A:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

option_B = VGroup(

Text("B:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

option_C = VGroup(

Text("C:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

option_D = VGroup(

Text("D:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

option_E = VGroup(

Text("E:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

options = VGroup(option_A, option_B, option_C, option_D, option_E).arrange(RIGHT, buff=0.6)

options.next_to(interactive_grid, DOWN, buff=1)

content = VGroup(interactive_grid, options).scale(0.7).center()

  

# Figure generation logic

F1 = ['C', 'P']

F2 = [3, 4, 5, 6]

Co = ['red', 'blue', 'yellow', 'green']

Ang = [0, 45, 90, 120, 150, 180, 270]

Row = [0, 1, 2]

d = random.choice([element for element in C if element not in [a, o1, o2]])

cob = [random.choice(Co), random.choice(Co), random.choice(Co)]

for r in Row:

fa1 = random.choice(F1)

fa2 = random.choice(F2)

coa = random.choice(Co)

anga = random.choice(Ang)

fb1 = random.choice(F1)

fb2 = random.choice(F2)

angb = random.choice(Ang)

Lenn = random.choice([-0.1, -0.05, 0.05, 0.1])

def F_1(cell, c):

return insert_figures_in_cell(cell, [('P', fb2, 0.4, (Lenn*((c+2)%3), 0), cob[(c)%3], angb)])

  

def F_2(cell, c):

return insert_figures_in_cell(cell, [('P', 2, 0.1, (Lenn*((c+2)%3), 0), 'black', angb)])

  

for c in [3*r + 1, 3*r + 2, 3*r + 3]:

if o1 != c and o2 != c and a != c:

content.add(

F_1(c, c),

F_2(c, c)

)

if c == d:

content.add(

F_1(wr_3, c),

F_2(wr_3, c)

)

elif c == a:

content.add(

F_1(tr, c),

F_2(tr, c)

)

elif c == o1:

content.add(

F_1(wr_1, c),

F_2(wr_1, c)

)

elif c == o2:

content.add(

F_1(wr_2, c),

F_2(wr_2, c)

)

  
  

content.add(

#insert_figures_in_cell(wr_4, [('P', fb2+1, 0.5, (0, 0), random.choice(Co), anga+0.2)]),

insert_figures_in_cell(wr_4, [('P', fb2+1, 0.25, (0.25*((c+2)%3), 0), cob[(c+2)%3], angb)])

)

# Solution mapping

solution_map = {

10: 'A',

11: 'B',

12: 'C',

13: 'D',

14: 'E'

}

soluzione = solution_map.get(tr, 'Nessuna soluzione')

print(f"La soluzione corretta dell'esercizio è la {soluzione}. Nota che le figure, che siano poligoni regolari o cerchi, rimangono costanti nelle righe mentre i colori di queste figure sono costanti nelle colonne. Inoltre, spostandosi verso destra si nota un progressivo spostamento della figura che si allontana dal centro.")

self.add(content)
```
#### SumUpSides (101 - 125)
```Python
%%manim -ql BasicGrid

  

import numpy as np

import random

  

C = list(range(1, 10)) # Cell numbers

  

# Global configuration

config.background_color = WHITE

config.pixel_width = 1920

config.pixel_height = 1080

  

def string_to_color(color_str):

color_str = color_str.lower()

if color_str == "red":

return "#b22222"

elif color_str == "blue":

return "#336699"

elif color_str == "green":

return "#228b22"

elif color_str == "yellow":

return "#b8860b"

else:

return "#000000"

  

def create_diagonal_stripes(center, cell_size=2, num_stripes=8):

lines = VGroup()

center = np.array(center)

v = np.array([1, -1, 0]) / np.linalg.norm([1, -1, 0])

u = np.array([1, 1, 0]) / np.linalg.norm([1, 1, 0])

half = cell_size / 2

max_offset = cell_size / np.sqrt(2)

offsets = np.linspace(-max_offset, max_offset, num_stripes)

for offset in offsets:

t_min = -half * np.sqrt(2) + abs(offset)

t_max = half * np.sqrt(2) - abs(offset)

start = center + offset * u + t_min * v

end = center + offset * u + t_max * v

lines.add(Line(start, end, stroke_color=BLACK, stroke_width=2))

return lines

  

def create_interactive_grid(obscured_cells, asked_cell):

grid_lines = VGroup()

for x in [-3, -1, 1, 3]:

grid_lines.add(Line([x, -3, 0], [x, 3, 0], color=BLACK, stroke_width=2))

for y in [-3, -1, 1, 3]:

grid_lines.add(Line([-3, y, 0], [3, y, 0], color=BLACK, stroke_width=2))

cell_centers = []

for row in range(3):

for col in range(3):

x = -2 + col * 2

y = 2 - row * 2

cell_centers.append(np.array([x, y, 0]))

overlays = VGroup()

for i, center in enumerate(cell_centers):

cell_num = i + 1

if cell_num in obscured_cells:

overlays.add(create_diagonal_stripes(center))

if cell_num == asked_cell:

overlays.add(Text("?", font_size=72, color=BLACK).move_to(center))

return VGroup(grid_lines, overlays)

  

def insert_figures_in_cell(cell_number, figures, cell_size=2):

if cell_number <= 9:

row = (cell_number - 1) // 3

col = (cell_number - 1) % 3

center_x = -1.40 + col * 1.40

center_y = 2.4 - row * 1.40

cell_center = np.array([center_x, center_y, 0])

else:

option_centers = [

np.array([-4.35, -2.45, 0]), # A (10)

np.array([-4.6 + (2.355*1)+0.15, -2.45, 0]), # B (11)

np.array([-4.6 + (2.355*2)+0.1, -2.45, 0]), # C (12)

np.array([-4.6 + (2.355*3)+0.05, -2.45, 0]), # D (13)

np.array([-4.6 + (2.355*4), -2.45, 0]) # E (14)

]

cell_center = option_centers[cell_number - 10]

figures_group = VGroup()

for fig in figures:

if fig[0] == "P":

_, num_sides, side_length, offset_tuple, color_str, rotation_angle = fig

R = side_length / (2 * np.sin(np.pi / num_sides))

poly = RegularPolygon(n=num_sides, radius=R, color=string_to_color(color_str))

poly.rotate(rotation_angle * DEGREES)

poly.move_to(cell_center + np.array(offset_tuple + (0,)))

figures_group.add(poly)

elif fig[0] == "C":

_, _, radius, offset_tuple, color_str, _ = fig

circle = Circle(radius=radius, color=string_to_color(color_str))

circle.move_to(cell_center + np.array(offset_tuple + (0,)))

figures_group.add(circle)

return figures_group

  

# Initialize random cells with updated answer options

ans = [10, 11, 12, 13, 14]

tr = random.choice(ans)

Wr_1 = [element for element in ans if element != tr]

wr_1 = random.choice(Wr_1)

Wr_2 = [element for element in ans if element not in [tr, wr_1]]

wr_2 = random.choice(Wr_2)

Wr_3 = [element for element in ans if element not in [tr, wr_1, wr_2]]

wr_3 = random.choice(Wr_3)

Wr_4 = [element for element in ans if element not in [tr, wr_1, wr_2, wr_3]]

wr_4 = random.choice(Wr_4)

print(wr_4) # Corrected from its original slight indent to be top-level

  

# Random cell selection logic remains the same

o1 = random.choice(C)

o2 = random.choice(C)

a = random.choice(C)

while (o1 == o2 or o1 == a or o2 == a) or \

(((o1 - 1) // 3) == ((o2 - 1) // 3) or ((o1 - 1) // 3) == ((a - 1) // 3) or ((o2 - 1) // 3) == ((a - 1) // 3)) or \

(((o1 - 1) % 3) == ((o2 - 1) % 3) or ((o1 - 1) % 3) == ((a - 1) % 3) or ((o2 - 1) % 3) == ((a - 1) % 3)):

o1 = random.choice(C)

o2 = random.choice(C)

a = random.choice(C)

  

class BasicGrid(Scene):

def construct(self):

interactive_grid = create_interactive_grid(obscured_cells=[], asked_cell=a).shift(UP * 1)

# Create answer options including E

option_A = VGroup(

Text("A:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

option_B = VGroup(

Text("B:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

option_C = VGroup(

Text("C:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

option_D = VGroup(

Text("D:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

option_E = VGroup(

Text("E:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

options = VGroup(option_A, option_B, option_C, option_D, option_E).arrange(RIGHT, buff=0.6)

options.next_to(interactive_grid, DOWN, buff=1)

content = VGroup(interactive_grid, options).scale(0.7).center()

  

# Figure generation logic

F1 = ['C', 'P']

f2 = [3, 4, 5]

F2 = [3, 4, 5, 6, 7, 8]

Co = ['red', 'blue', 'yellow', 'green']

Ang = [0, 45, 90, 120, 150, 180, 270]

Row = [0, 1, 2]

d = random.choice([element for element in C if element not in [a, o2]])

  

for r in Row:

fa1 = random.choice(F1)

fa2 = random.choice(F2)

coa = random.choice(Co)

anga = random.choice(Ang)

fb1 = random.choice(F1)

fb2 = [random.choice(f2), random.choice(f2)]

cob = [random.choice(Co), random.choice(Co)]

while (fb2[1] - fb2[0] <=1 and fb2[0] - fb2[1]<=1):

fb2 = [random.choice(f2), random.choice(f2)]

cob = [random.choice(Co), random.choice(Co)]

angb = random.choice(Ang)

print(r)

def F_1(cell, c):

if (c+2)%3 < 2:

return insert_figures_in_cell(cell, [('P', fb2[(c+2)%3], 0.4, (0, 0), cob[(c+2)%3], anga)])

elif cob[1] == cob[0]:

return insert_figures_in_cell(cell, [('P', fb2[0]+fb2[1], 0.4, (0, 0), cob[0], anga)])

elif fb2[0] > fb2 [1]:

return insert_figures_in_cell(cell, [('P', fb2[0]-fb2[1], 0.4, (0, 0), cob[0], anga)])

else:

return insert_figures_in_cell(cell, [('P', fb2[1]-fb2[0], 0.4, (0, 0), cob[1], anga)])

  

#def F_2(cell, c):

#return insert_figures_in_cell(cell, [('P', 2, 0.2, (0, 0), 'red', anga)])

  

for c in [3*r + 1, 3*r + 2, 3*r + 3]:

print(c)

if a != c:

content.add(

F_1(c, c),

#F_2(c, c)

)

if c == d:

content.add(

F_1(wr_3, c),

#F_2(wr_3, c)

)

elif c == a:

content.add(

F_1(tr, c),

#F_2(tr, c)

)

elif c == o1:

content.add(

F_1(wr_1, c),

#F_2(wr_1, c)

)

elif c == o2:

content.add(

F_1(wr_2, c),

#F_2(wr_2, c)

)

  
  

content.add(

insert_figures_in_cell(wr_4, [('P', random.choice(f2), 0.5, (0, 0), 'red', anga)])

#insert_figures_in_cell(wr_4, [('P', 2, 0.2, (0, 0), 'red', anga)])

)

# Solution mapping

solution_map = {

10: 'A',

11: 'B',

12: 'C',

13: 'D',

14: 'E'

}

soluzione = solution_map.get(tr, 'Nessuna soluzione')

print(f"La soluzione corretta dell'esercizio è la {soluzione}. Nella stessa riga andiamo ad applicare un'operazione di somma del primo poligono al secondo per ottenere il terzo: contiamo il numero di vertici di un colore e se uguali si sommano, se invece sono di colore diverso si sottraggono lasciando il colore che prevale.")

self.add(content)
```
#### ModuloSide (148 - 176)
```Python
%%manim -ql BasicGrid

  

import numpy as np

import random

  

C = list(range(1, 10)) # Cell numbers

  

# Global configuration

config.background_color = WHITE

config.pixel_width = 1920

config.pixel_height = 1080

  

def string_to_color(color_str):

color_str = color_str.lower()

if color_str == "red":

return "#b22222"

elif color_str == "blue":

return "#336699"

elif color_str == "green":

return "#228b22"

elif color_str == "yellow":

return "#b8860b"

else:

return "#000000"

  

def create_diagonal_stripes(center, cell_size=2, num_stripes=8):

lines = VGroup()

center = np.array(center)

v = np.array([1, -1, 0]) / np.linalg.norm([1, -1, 0])

u = np.array([1, 1, 0]) / np.linalg.norm([1, 1, 0])

half = cell_size / 2

max_offset = cell_size / np.sqrt(2)

offsets = np.linspace(-max_offset, max_offset, num_stripes)

for offset in offsets:

t_min = -half * np.sqrt(2) + abs(offset)

t_max = half * np.sqrt(2) - abs(offset)

start = center + offset * u + t_min * v

end = center + offset * u + t_max * v

lines.add(Line(start, end, stroke_color=BLACK, stroke_width=2))

return lines

  

def create_interactive_grid(obscured_cells, asked_cell):

grid_lines = VGroup()

for x in [-3, -1, 1, 3]:

grid_lines.add(Line([x, -3, 0], [x, 3, 0], color=BLACK, stroke_width=2))

for y in [-3, -1, 1, 3]:

grid_lines.add(Line([-3, y, 0], [3, y, 0], color=BLACK, stroke_width=2))

cell_centers = []

for row in range(3):

for col in range(3):

x = -2 + col * 2

y = 2 - row * 2

cell_centers.append(np.array([x, y, 0]))

overlays = VGroup()

for i, center in enumerate(cell_centers):

cell_num = i + 1

if cell_num in obscured_cells:

overlays.add(create_diagonal_stripes(center))

if cell_num == asked_cell:

overlays.add(Text("?", font_size=72, color=BLACK).move_to(center))

return VGroup(grid_lines, overlays)

  

def insert_figures_in_cell(cell_number, figures, cell_size=2):

if cell_number <= 9:

row = (cell_number - 1) // 3

col = (cell_number - 1) % 3

center_x = -1.40 + col * 1.40

center_y = 2.4 - row * 1.40

cell_center = np.array([center_x, center_y, 0])

else:

option_centers = [

np.array([-4.35, -2.45, 0]), # A (10)

np.array([-4.6 + (2.355*1)+0.15, -2.45, 0]), # B (11)

np.array([-4.6 + (2.355*2)+0.1, -2.45, 0]), # C (12)

np.array([-4.6 + (2.355*3)+0.05, -2.45, 0]), # D (13)

np.array([-4.6 + (2.355*4), -2.45, 0]) # E (14)

]

cell_center = option_centers[cell_number - 10]

figures_group = VGroup()

for fig in figures:

if fig[0] == "P":

_, num_sides, side_length, offset_tuple, color_str, rotation_angle = fig

R = side_length / (2 * np.sin(np.pi / num_sides))

poly = RegularPolygon(n=num_sides, radius=R, color=string_to_color(color_str))

poly.rotate(rotation_angle * DEGREES)

poly.move_to(cell_center + np.array(offset_tuple + (0,)))

figures_group.add(poly)

elif fig[0] == "C":

_, _, radius, offset_tuple, color_str, _ = fig

circle = Circle(radius=radius, color=string_to_color(color_str))

circle.move_to(cell_center + np.array(offset_tuple + (0,)))

figures_group.add(circle)

return figures_group

  

# Initialize random cells with updated answer options

ans = [10, 11, 12, 13, 14]

tr = random.choice(ans)

Wr_1 = [element for element in ans if element != tr]

wr_1 = random.choice(Wr_1)

Wr_2 = [element for element in ans if element not in [tr, wr_1]]

wr_2 = random.choice(Wr_2)

Wr_3 = [element for element in ans if element not in [tr, wr_1, wr_2]]

wr_3 = random.choice(Wr_3)

Wr_4 = [element for element in ans if element not in [tr, wr_1, wr_2, wr_3]]

wr_4 = random.choice(Wr_4)

print(wr_4) # Corrected from its original slight indent to be top-level

  

# Random cell selection logic remains the same

o1 = random.choice(C)

o2 = random.choice(C)

a = random.choice(C)

while (o1 == o2 or o1 == a or o2 == a) or \

(((o1 - 1) // 3) == ((o2 - 1) // 3) or ((o1 - 1) // 3) == ((a - 1) // 3) or ((o2 - 1) // 3) == ((a - 1) // 3)) or \

(((o1 - 1) % 3) == ((o2 - 1) % 3) or ((o1 - 1) % 3) == ((a - 1) % 3) or ((o2 - 1) % 3) == ((a - 1) % 3)):

o1 = random.choice(C)

o2 = random.choice(C)

a = random.choice(C)

  

class BasicGrid(Scene):

def construct(self):

interactive_grid = create_interactive_grid(obscured_cells=[o1], asked_cell=a).shift(UP * 1)

# Create answer options including E

option_A = VGroup(

Text("A:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

option_B = VGroup(

Text("B:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

option_C = VGroup(

Text("C:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

option_D = VGroup(

Text("D:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

option_E = VGroup(

Text("E:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

options = VGroup(option_A, option_B, option_C, option_D, option_E).arrange(RIGHT, buff=0.6)

options.next_to(interactive_grid, DOWN, buff=1)

content = VGroup(interactive_grid, options).scale(0.7).center()

  

# Figure generation logic

F1 = ['C', 'P']

f2 = [3, 4, 5]

F2 = [3, 4, 5, 6, 7, 8]

Co = ['red', 'blue', 'yellow', 'green']

Ang = [0, 45, 90, 120, 150, 180, 270]

Row = [0, 1, 2]

d = random.choice([element for element in C if element not in [a, o2]])

k = random.choice([0, 1, 2])

for r in Row:

fa1 = random.choice(F1)

fa2 = random.choice(F2)

coa = random.choice(Co)

anga = random.choice(Ang)

fb1 = random.choice(F1)

fb2 = random.choice(f2)

cob = random.choice(Co)

fb2 = random.choice(F2)

cob = random.choice(Co)

angb = random.choice(Ang)

def F_1(cell, c):

return insert_figures_in_cell(cell, [('P', fb2-1+(c+k)%3, 0.4, (0, 0), cob, anga)])

  

def F_2(cell, c):

return insert_figures_in_cell(cell, [('P', 2, 0.2, (0, 0), 'red', anga)])

  

for c in [3*r + 1, 3*r + 2, 3*r + 3]:

if a != c and o1 != c:

content.add(

F_1(c, c),

F_2(c, c)

)

if c == d:

content.add(

F_1(wr_3, c),

F_2(wr_3, c)

)

elif c == a:

content.add(

F_1(tr, c),

F_2(tr, c)

)

elif c == o1:

content.add(

F_1(wr_1, c),

F_2(wr_1, c)

)

elif c == o2:

content.add(

F_1(wr_2, c),

F_2(wr_2, c)

)

  
  

content.add(

insert_figures_in_cell(wr_4, [('P', random.choice(f2), 0.5, (0, 0), 'red', anga)]),

insert_figures_in_cell(wr_4, [('P', 2, 0.2, (0, 0), 'red', anga)])

)

# Solution mapping

solution_map = {

10: 'A',

11: 'B',

12: 'C',

13: 'D',

14: 'E'

}

soluzione = solution_map.get(tr, 'Nessuna soluzione')

print(f"La soluzione corretta dell'esercizio è la {soluzione}. Colore e rotazione del poligono rimangono costanti sulla riga e notiamo come ciascuna colonna aggiunga 0, 1 o 2 lati ai poligoni.")

self.add(content)
```
#### SticksUnion (16 - 37)
```Python
%%manim -ql BasicGrid

  

import numpy as np

import random

  

C = list(range(1, 10)) # Cell numbers

  

# Global configuration

config.background_color = WHITE

config.pixel_width = 1920

config.pixel_height = 1080

  

def string_to_color(color_str):

color_str = color_str.lower()

if color_str == "red":

return "#b22222"

elif color_str == "blue":

return "#336699"

elif color_str == "green":

return "#228b22"

elif color_str == "yellow":

return "#b8860b"

else:

return "#000000"

  

def create_diagonal_stripes(center, cell_size=2, num_stripes=8):

lines = VGroup()

center = np.array(center)

v = np.array([1, -1, 0]) / np.linalg.norm([1, -1, 0])

u = np.array([1, 1, 0]) / np.linalg.norm([1, 1, 0])

half = cell_size / 2

max_offset = cell_size / np.sqrt(2)

offsets = np.linspace(-max_offset, max_offset, num_stripes)

for offset in offsets:

t_min = -half * np.sqrt(2) + abs(offset)

t_max = half * np.sqrt(2) - abs(offset)

start = center + offset * u + t_min * v

end = center + offset * u + t_max * v

lines.add(Line(start, end, stroke_color=BLACK, stroke_width=2))

return lines

  

def create_interactive_grid(obscured_cells, asked_cell):

grid_lines = VGroup()

for x in [-3, -1, 1, 3]:

grid_lines.add(Line([x, -3, 0], [x, 3, 0], color=BLACK, stroke_width=2))

for y in [-3, -1, 1, 3]:

grid_lines.add(Line([-3, y, 0], [3, y, 0], color=BLACK, stroke_width=2))

cell_centers = []

for row in range(3):

for col in range(3):

x = -2 + col * 2

y = 2 - row * 2

cell_centers.append(np.array([x, y, 0]))

overlays = VGroup()

for i, center in enumerate(cell_centers):

cell_num = i + 1

if cell_num in obscured_cells:

overlays.add(create_diagonal_stripes(center))

if cell_num == asked_cell:

overlays.add(Text("?", font_size=72, color=BLACK).move_to(center))

return VGroup(grid_lines, overlays)

  

def insert_figures_in_cell(cell_number, figures, cell_size=2):

if cell_number <= 9:

row = (cell_number - 1) // 3

col = (cell_number - 1) % 3

center_x = -1.40 + col * 1.40

center_y = 2.4 - row * 1.40

cell_center = np.array([center_x, center_y, 0])

else:

option_centers = [

np.array([-4.35, -2.45, 0]), # A (10)

np.array([-4.6 + (2.355*1)+0.15, -2.45, 0]), # B (11)

np.array([-4.6 + (2.355*2)+0.1, -2.45, 0]), # C (12)

np.array([-4.6 + (2.355*3)+0.05, -2.45, 0]), # D (13)

np.array([-4.6 + (2.355*4), -2.45, 0]) # E (14)

]

cell_center = option_centers[cell_number - 10]

figures_group = VGroup()

for fig in figures:

if fig[0] == "P":

_, num_sides, side_length, offset_tuple, color_str, rotation_angle = fig

R = side_length / (2 * np.sin(np.pi / num_sides))

poly = RegularPolygon(n=num_sides, radius=R, color=string_to_color(color_str))

poly.rotate(rotation_angle * DEGREES)

poly.move_to(cell_center + np.array(offset_tuple + (0,)))

figures_group.add(poly)

elif fig[0] == "C":

_, _, radius, offset_tuple, color_str, _ = fig

circle = Circle(radius=radius, color=string_to_color(color_str))

circle.move_to(cell_center + np.array(offset_tuple + (0,)))

figures_group.add(circle)

return figures_group

  

# Initialize random cells with updated answer options

ans = [10, 11, 12, 13, 14]

tr = random.choice(ans)

Wr_1 = [element for element in ans if element != tr]

wr_1 = random.choice(Wr_1)

Wr_2 = [element for element in ans if element not in [tr, wr_1]]

wr_2 = random.choice(Wr_2)

Wr_3 = [element for element in ans if element not in [tr, wr_1, wr_2]]

wr_3 = random.choice(Wr_3)

Wr_4 = [element for element in ans if element not in [tr, wr_1, wr_2, wr_3]]

wr_4 = random.choice(Wr_4)

print(wr_4) # Corrected from its original slight indent to be top-level

  

# Random cell selection logic remains the same

o1 = random.choice(C)

o2 = random.choice(C)

a = random.choice(C)

while (o1 == o2 or o1 == a or o2 == a) or \

(((o1 - 1) // 3) == ((o2 - 1) // 3) or ((o1 - 1) // 3) == ((a - 1) // 3) or ((o2 - 1) // 3) == ((a - 1) // 3)) or \

(((o1 - 1) % 3) == ((o2 - 1) % 3) or ((o1 - 1) % 3) == ((a - 1) % 3) or ((o2 - 1) % 3) == ((a - 1) % 3)):

o1 = random.choice(C)

o2 = random.choice(C)

a = random.choice(C)

  

class BasicGrid(Scene):

def construct(self):

interactive_grid = create_interactive_grid(obscured_cells=[], asked_cell=a).shift(UP * 1)

# Create answer options including E

option_A = VGroup(

Text("A:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

option_B = VGroup(

Text("B:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

option_C = VGroup(

Text("C:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

option_D = VGroup(

Text("D:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

option_E = VGroup(

Text("E:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

options = VGroup(option_A, option_B, option_C, option_D, option_E).arrange(RIGHT, buff=0.6)

options.next_to(interactive_grid, DOWN, buff=1)

content = VGroup(interactive_grid, options).scale(0.7).center()

  

# Figure generation logic

F1 = ['C', 'P']

f2 = [3, 4, 5]

F2 = [3, 4, 5, 6, 7, 8]

Co = ['red', 'blue', 'yellow', 'green']

Ang = [0, 45, 90, 120, 150, 180, 270]

Row = [0, 1, 2]

d = random.choice([element for element in C if element not in [a]])

k = random.choice([0, 1, 2])

for r in Row:

fa1 = random.choice(F1)

fa2 = random.choice(F2)

coa = random.choice(Co)

anga = random.choice(Ang)

fb1 = random.choice(F1)

fb2 = random.choice(f2)

cob = random.choice(Co)

fb2 = random.choice(F2)

cob = random.choice(Co)

angb = random.choice(Ang)

V1 = [random.choice([0, 1]), random.choice([0, 1]),]

V2 = [random.choice([0, 1]), random.choice([0, 1]),]

while V1 == [0, 0] or V2== [0, 0]:

V1 = [random.choice([0, 1]), random.choice([0, 1]),]

V2 = [random.choice([0, 1]), random.choice([0, 1]),]

  

def F_1(cell, c):

A = [('P', 2, 0.4, (0, 0), coa, anga)]

B = [('P', 2, 0.4, (0, 0), cob, angb)]

C = [('P', 4, 0.4, (0, 0), cob, angb)]

if (c+2)%3 == 0:

if V1[0] == 0 and V1[1] == 0:

return insert_figures_in_cell(14, A)

elif V1[0] == 1 and V1[1] == 0:

return insert_figures_in_cell(cell, A)

elif V1[0] == 0 and V1[1] == 1:

return insert_figures_in_cell(cell, B)

else: #V1[0] == 1 and V1[1] == 1:

return insert_figures_in_cell(cell, A), insert_figures_in_cell(cell, B)

elif (c+2)%3 == 1:

if V2[0] == 0 and V2[1] == 0:

return insert_figures_in_cell(14, A)

elif V2[0] == 1 and V2[1] == 0:

return insert_figures_in_cell(cell, A)

elif V2[0] == 0 and V2[1] == 1:

return insert_figures_in_cell(cell, B)

else: #V[0] == 1 and V[1] == 1:

return insert_figures_in_cell(cell, A), insert_figures_in_cell(cell, B)

else:

if (V1[0] == 1 or V2[0] == 1) and (V1[1] == 0 and V2[1] == 0):

print(c, 1)

return insert_figures_in_cell(cell, A)

elif (V1[1] == 1 or V2[1] == 1) and (V1[0] == 0 and V2[0] == 0):

print(c, 2)

return insert_figures_in_cell(cell, B)

elif V1[1] == 1 or V2[1] == 1 and (V1[0] == 1 or V2[0] == 1):

print(c, 3)

return insert_figures_in_cell(cell, A), insert_figures_in_cell(cell, B)

else:

return insert_figures_in_cell(cell, C)

  

for c in [3*r + 1, 3*r + 2, 3*r + 3]:

if a != c:

content.add(

F_1(c, c)

)

if c == d:

content.add(

F_1(wr_3, c)

)

elif c == a:

content.add(

F_1(tr, c)

)

elif c == o1:

content.add(

F_1(wr_1, c)

)

elif c == o2:

content.add(

F_1(wr_2, c)

)

  
  

content.add(

insert_figures_in_cell(wr_4, [('P', 2, 0.4, (0, 0), coa, anga)]),

insert_figures_in_cell(wr_4, [('P', 2, 0.4, (0, 0), coa, anga)])

)

# Solution mapping

solution_map = {

10: 'A',

11: 'B',

12: 'C',

13: 'D',

14: 'E'

}

soluzione = solution_map.get(tr, 'Nessuna soluzione')

print(f"La soluzione corretta dell'esercizio è la {soluzione}. Notiamo che per ogni riga il/i segmento/i della prima colonna vengono unito/i a quello/i della seconda per comporre la terza colonna.")

self.add(content)
```
#### ColourSudoku (177 - 201)
```Python
%%manim -ql BasicGrid

  

import numpy as np

import random

  

C = list(range(1, 10)) # Cell numbers

  

# Global configuration

config.background_color = WHITE

config.pixel_width = 1920

config.pixel_height = 1080

  

def string_to_color(color_str):

color_str = color_str.lower()

if color_str == "red":

return "#b22222"

elif color_str == "blue":

return "#336699"

elif color_str == "green":

return "#228b22"

elif color_str == "yellow":

return "#b8860b"

else:

return "#000000"

  

def create_diagonal_stripes(center, cell_size=2, num_stripes=8):

lines = VGroup()

center = np.array(center)

v = np.array([1, -1, 0]) / np.linalg.norm([1, -1, 0])

u = np.array([1, 1, 0]) / np.linalg.norm([1, 1, 0])

half = cell_size / 2

max_offset = cell_size / np.sqrt(2)

offsets = np.linspace(-max_offset, max_offset, num_stripes)

for offset in offsets:

t_min = -half * np.sqrt(2) + abs(offset)

t_max = half * np.sqrt(2) - abs(offset)

start = center + offset * u + t_min * v

end = center + offset * u + t_max * v

lines.add(Line(start, end, stroke_color=BLACK, stroke_width=2))

return lines

  

def create_interactive_grid(obscured_cells, asked_cell):

grid_lines = VGroup()

for x in [-3, -1, 1, 3]:

grid_lines.add(Line([x, -3, 0], [x, 3, 0], color=BLACK, stroke_width=2))

for y in [-3, -1, 1, 3]:

grid_lines.add(Line([-3, y, 0], [3, y, 0], color=BLACK, stroke_width=2))

cell_centers = []

for row in range(3):

for col in range(3):

x = -2 + col * 2

y = 2 - row * 2

cell_centers.append(np.array([x, y, 0]))

overlays = VGroup()

for i, center in enumerate(cell_centers):

cell_num = i + 1

if cell_num in obscured_cells:

overlays.add(create_diagonal_stripes(center))

if cell_num == asked_cell:

overlays.add(Text("?", font_size=72, color=BLACK).move_to(center))

return VGroup(grid_lines, overlays)

  

def insert_figures_in_cell(cell_number, figures, cell_size=2):

if cell_number <= 9:

row = (cell_number - 1) // 3

col = (cell_number - 1) % 3

center_x = -1.40 + col * 1.40

center_y = 2.4 - row * 1.40

cell_center = np.array([center_x, center_y, 0])

else:

option_centers = [

np.array([-4.35, -2.45, 0]), # A (10)

np.array([-4.6 + (2.355*1)+0.15, -2.45, 0]), # B (11)

np.array([-4.6 + (2.355*2)+0.1, -2.45, 0]), # C (12)

np.array([-4.6 + (2.355*3)+0.05, -2.45, 0]), # D (13)

np.array([-4.6 + (2.355*4), -2.45, 0]) # E (14)

]

cell_center = option_centers[cell_number - 10]

figures_group = VGroup()

for fig in figures:

if fig[0] == "P":

_, num_sides, side_length, offset_tuple, color_str, rotation_angle = fig

R = side_length / (2 * np.sin(np.pi / num_sides))

poly = RegularPolygon(n=num_sides, radius=R, color=string_to_color(color_str))

poly.rotate(rotation_angle * DEGREES)

poly.move_to(cell_center + np.array(offset_tuple + (0,)))

figures_group.add(poly)

elif fig[0] == "C":

_, _, radius, offset_tuple, color_str, _ = fig

circle = Circle(radius=radius, color=string_to_color(color_str))

circle.move_to(cell_center + np.array(offset_tuple + (0,)))

figures_group.add(circle)

return figures_group

  

# Initialize random cells with updated answer options

ans = [10, 11, 12, 13, 14]

tr = random.choice(ans)

Wr_1 = [element for element in ans if element != tr]

wr_1 = random.choice(Wr_1)

Wr_2 = [element for element in ans if element not in [tr, wr_1]]

wr_2 = random.choice(Wr_2)

Wr_3 = [element for element in ans if element not in [tr, wr_1, wr_2]]

wr_3 = random.choice(Wr_3)

Wr_4 = [element for element in ans if element not in [tr, wr_1, wr_2, wr_3]]

wr_4 = random.choice(Wr_4)

print(wr_4) # Corrected from its original slight indent to be top-level

  

# Random cell selection logic remains the same

o1 = random.choice(C)

o2 = random.choice(C)

a = random.choice(C)

while (o1 == o2 or o1 == a or o2 == a) or \

(((o1 - 1) // 3) == ((o2 - 1) // 3) or ((o1 - 1) // 3) == ((a - 1) // 3) or ((o2 - 1) // 3) == ((a - 1) // 3)) or \

(((o1 - 1) % 3) == ((o2 - 1) % 3) or ((o1 - 1) % 3) == ((a - 1) % 3) or ((o2 - 1) % 3) == ((a - 1) % 3)):

o1 = random.choice(C)

o2 = random.choice(C)

a = random.choice(C)

  

class BasicGrid(Scene):

def construct(self):

interactive_grid = create_interactive_grid(obscured_cells=[], asked_cell=a).shift(UP * 1)

# Create answer options including E

option_A = VGroup(

Text("A:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

option_B = VGroup(

Text("B:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

option_C = VGroup(

Text("C:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

option_D = VGroup(

Text("D:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

option_E = VGroup(

Text("E:", font_size=36, color=BLACK),

Square(side_length=2, color=BLACK, stroke_width=2)

).arrange(RIGHT, buff=0.2)

options = VGroup(option_A, option_B, option_C, option_D, option_E).arrange(RIGHT, buff=0.6)

options.next_to(interactive_grid, DOWN, buff=1)

content = VGroup(interactive_grid, options).scale(0.7).center()

  

# Figure generation logic

F1 = ['C', 'P']

f2 = [3, 4, 5]

F2 = [3, 4, 5, 6, 7, 8]

Co = ['red', 'blue', 'yellow', 'green']

Ang = [0, 45, 90, 120, 150, 180, 270]

Row = [0, 1, 2]

d = random.choice([element for element in C if element not in [a]])

coa = [random.choice(Co), random.choice(Co), random.choice(Co)]

cob = [random.choice(Co), random.choice(Co), random.choice(Co)]

while coa[0] == coa[1] or coa[1] == coa[2] or coa[2] == coa[0]:

coa = [random.choice(Co), random.choice(Co), random.choice(Co)]

while cob[0] == cob[1] or cob[1] == cob[2] or cob[2] == cob[0]:

cob = [random.choice(Co), random.choice(Co), random.choice(Co)]

for r in Row:

fa1 = random.choice(F1)

fa2 = random.choice(F2)

anga = random.choice(Ang)

fb1 = random.choice(F1)

fb2 = random.choice(f2)

fb2 = random.choice(F2)

angb = random.choice(Ang)

V = [random.choice([0, 1, 2]), random.choice([0, 1, 2]), random.choice([0, 1, 2])]

while V[0] == V[1] or V[1] == V[2] or V[2] == V[0]:

V = [random.choice([0, 1, 2]), random.choice([0, 1, 2]), random.choice([0, 1, 2])]

  

def F_1(cell, c):

A = [('P', 2, 0.3, (0, 0), coa[V[c%3]], anga)]

B = [(random.choice(['P', 'C']), random.choice([3, 4, 5, 6]), 0.5, (0, 0), cob[V[c%3]], anga)]

return insert_figures_in_cell(cell, A), insert_figures_in_cell(cell, B)

  

for c in [3*r + 1, 3*r + 2, 3*r + 3]:

if a != c:

content.add(

F_1(c, c)

)

if c == d:

content.add(

F_1(wr_3, c)

)

elif c == a:

content.add(

F_1(tr, c)

)

elif c == o1:

content.add(

F_1(wr_1, c)

)

elif c == o2:

content.add(

F_1(wr_2, c)

)

  
  

content.add(

insert_figures_in_cell(wr_4, [('P', 2, 0.3, (0, 0), coa[V[c%3]], anga)]), insert_figures_in_cell(wr_4, [(random.choice(['P', 'C']), random.choice([3, 4, 5, 6]), 0.5, (0, 0), cob[V[c%3]], anga)])

)

# Solution mapping

solution_map = {

10: 'A',

11: 'B',

12: 'C',

13: 'D',

14: 'E'

}

soluzione = solution_map.get(tr, 'Nessuna soluzione')

print(f"La soluzione corretta dell'esercizio è la {soluzione}. Notiamo che, similmente ad un sudoku orizzontale, ogni riga contiene una linea di ciascuno dei tre colori delle linee e lo stesso succede con le figure che le comprendono; inoltre la rotazione delle linee rimangono costanti nelle righe")

self.add(content)
```