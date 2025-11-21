---
draft: true
date: 2025-03-19
---
I have been asked whether I would like to work on quizzes in the area of _spatial and abstract logic_, which refers to those IQ questions where figures are presented in a sequence, and we are asked to choose the missing one. This opportunity was offered to me immediately after my work on [[Futura Math Didactic Document]], but I find it significantly less convenient. Below, I outline some of the main difficulties:

- The payment is €2 per question, which includes creating both the question and all possible answer drawings, as well as providing an explanation. This is significantly lower than the €10 per page I received for the last document.  
- I am required to work directly on the Futura website, meaning I must upload images there rather than generating a PDF, which I could easily produce in $\LaTeX$. This entails a lengthy process of uploading multiple images, which is time-consuming.  
- The use of AI has been prohibited due to the poor quality of AI-generated outcomes. This is the same reason they asked me to work on the [[Futura Math Didactic Document]], with the key difference that, in that document, I was still allowed to use AI. Here, however, its use appears to be categorically forbidden. Even if I were permitted to use it, generating complex enough images for these quizzes would be challenging and would take far too long relative to the payment.  
- The total compensation for the 300 required questions amounts to €600, which is not particularly substantial.  

That said, a major advantage is that there is no strict deadline, unlike my last document, so I could take more time to complete the work. Given the current pay rate and my past work experience and opportunities, this job seems unreasonable. The only remaining consideration is at what price point I would find it acceptable. I consider the payment for [[Futura Math Didactic Document]] to have been particularly high, given the context and the possibility of using AI, so it does not serve as a good comparison.  

If I were to use it as a reference, I would estimate that each quiz question would require _at least_ as much work as a page of the document. In reality, it would likely demand much more effort, as the most time-consuming pages were those containing complex images—precisely the type of content required for the quizzes.  

In conclusion, I would be on the verge of accepting the job if I were paid €8 per quiz. For anything less, I would likely decline. Since this represents a _fourfold_ increase over the offered rate, it is not a reasonable negotiation point, and I will therefore not request a higher rate but simply reject the job.  

---
I should consider some of [these](https://www.matematiranje.in.rs/Logical%20problems%20and%20I.Q.%20Test/Intelligence%20test.pdf) PDFs which are made available, the material is substantially the same that is required. Formatting is though the main point. [This](https://cambomaths.wordpress.com/wp-content/uploads/2009/10/test_your_iq_-_400_questions_r.pdf) one is a longer source with a lot of tests. The legal aspect, I am afraid, is going to be certainly a problem.

---
I had a call with Martina about this, and we agreed that the best approach is for me to take some time to try creating a few—around 5 to 10—to see how long it takes. Based on that, I can calculate my hourly rate of approximately €30 and determine the total amount I will be paid. My estimate, as mentioned earlier, is that I will earn around €8–10 per question, but I will first give it a try and see how it goes.  

A final point concerns the tools for creating the images. One option is to use $\LaTeX$ with the `tikz` package, but this would be highly inefficient without AI assistance. Given my experience while working on [[Futura Math Didactic Document]], the current o3-mini-high model is not particularly effective at generating such images. Alternatively, I could use an iPad with an Apple Pencil to draw the figures, allowing the software to refine them into more *geometric* shapes. This workflow on the iPad would certainly be an interesting approach to explore.

---
\[27.03.2025\] I am now thinking on how to make the questions and I suppose that writing a python code would be the most optimal way to proceed. In the first place it would be quite educational for me, as I would be learning again how to program decently in python and on the other hand it would allow me, once the framework is written, to produce a very large amount of quizzes starting from very simple ideas. Furthermore, it would also be easy to implement AI in the workflow. Estimating an appropriate amount of hours becomes then quite difficult though, as it would require me a lot of time to build the infrastructure but then it would be simple to generate all the output. I asked a price of 8eur per quiz, claiming to need an hour to make three quizzes, it seems an appropriate esteem (despite it clearly is very difficult to predict how long it will take me to draw them with Python).

---
\[02.04.2025\] We agreed on 200 quizzes for 7eur each. I currently plan using [Manim Community](https://docs.manim.community/en/stable/index.html) to produce all images. I begin the work on this in [[Futura Logic Quizzes]] and write the code in [[Manim Code for Futura Abstract and Spacial Logic Quizzes]].