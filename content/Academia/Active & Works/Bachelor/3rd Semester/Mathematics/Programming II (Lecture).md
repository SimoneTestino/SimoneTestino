This course should have been preceded by Programming I, which I will take the next semester. This was necessary in order to finish the BSc Mathematics in 4 semesters considering the transfer from the University of Constance to the LMU Munich. Here is a brief recap of the topics relevant for the exam, I will need to take the course for 3 ECTS only. The course is on Object Oriented Programming in C++.
## Recap
This will mainly be a collection of notes on programs which can most be found on the [course website](https://www.math.lmu.de/~gkleen/teaching/W23/pro2/). Here I only presented the first lecture, since the published material was complete and detailed enough and we were allowed only to bring that material to the exam and not the personal notes.
#### Lecture 1
###### `class`
```C++
using namespace std;

class Complex { 

private:
	double re, im;
public:
	Complex(double=0, double=0); 
	
	double real();
	double imag();
	
	friend Complex conj(Complex);
};

Complex::Complex(double re_, double im_)
	: re(re_), im(im_) {}

double Complex::real() { return re; }
double Complex::imag() { return im; }

Complex conj(Complex z) {
	z.im = -z.im; return z;
}

```
This is a classic example of a class, it is divided in the private and public part, the former contains the informations that constitute a complex number. In the public part there is first the constructor, a function with the same name of the class, its sole job in this program is to set to `0` a non specified component in the class. Then I name two methods `real` and `imag` which are defined after the class thanks to  the `::`, since their output is a familiar type, there is no need to do more. On the other hand, if we want to define a function of the same type, like `conj` giving the complex conjugate, there is the need to add `friend`, it is similarly defined after the class but without the need to add `::`. Recall that the definition of both methods and friend function must follow the definition of the class.
###### `this`
The command `this` is the so-called pointer, one could add inside the class the function:
``` C++
Complex square() {
	double re2 = re*re - im*im,
		im2 = 2*re*im;
    re = re2; im = im2;
	return *this;
	}

int main() {
	Complex z{1.0, 2.0};
	cout << << ”Re z = ” << z.square()
	return 0;
}
```
Writing the function with `z.` in front determines the input and the output will be the same value, in fact there is the need to set `z` to the same values of `z2` in the defined function. Also compare the following two defined functions.
```C++
double real() { return (*this).re; }
double imag() { return this->im; }
```
They show two different syntax for the same semantic. Furthermore consider the following function:
```C++
double abs() {
	return sqrt( (*this).real()*(*this).real() + (this->imag())*(this->imag()) );
	}
```
###### `private`/`public`
The components of the class declared in the `private` section cannot be accessed from the outside of the class, `private` is also the default option of the class. For instance if we write outside of the class the following line, we will get an error:
``` C++
cout << z.re << endl;
```
###### Constructors
It shows how an attribute should be initialised, it must have the same name of the class and you can also construct the attribute of the class even if some of the inputs are missing.
```C++
class Complex {
	Complex (double x, double y)
	    : re(x), im(y) {}
};
```
Another example is the following:
```C++
class Polynom { 
	private:
		vector<double> coeff;
	public:
		Polynom() {}
		Polynom(int n) : coeff(n + 1) { coeff[n] = 1; } Polynom(const vector<double>& v) : coeff(v) {}
```
What needs to be done in the case where less variables than needed are given is expressed within the `()`, for instance consider
```C++
Complex(double re_=0, double im_=0) : re(re_), im(im_) {}
```
The constructors that sets at `0`the missing variables. Constructors are called standard iff no parameters is required.

An interesting example of a constructor is the one of vectors. Those can be initialised by giving its length or with its content
```C++
vector<double> v1(7);
vector<double> v2{1, 2, 3, 4};
```
###### Destructor
The name of the destructor must be of the form `~C`, they are normally built in, though one can make an explicit one by using `delete` operator. An example is the following:
```C++
~Vektor() {
delete[] ap;
}
```
Such destructors are useful only for managing the memory correctly but should have no influence on the theoretical practice of the program. 

