In this page I present the program I wrote for keeping track of my marks of the [[M.Sc. Logic (UvA)]]; the structure and intent are exposed in [[Storage Information Programs with OOP]] together with other general guidelines.

Before beginning to write the code I make a list of all classes I will need:
#### Required Classes
- `Marks_state`: full description of the current state of marks
	- `Course*`: all there is to say about a course
		- `Tests*`: all there is to say about a test
			- `Taken`: `bool`
			- `Passed`: `bool`
			- `Mark`
				- `value`: `float`
				- `scale`: `{int, int, int}`
			- `Relevance`: `float` $\in [0, 1]$
			- `Date`: `{int, int, int}`
			- `Type`: `str`, can be: `oral`, `written`, `take-home`
			- `Open-book`: `bool` s.t. `type = "take home" -> open-book = True`
		- `Credits`: `int`
		- `Full Name`: `str`
		- `Counting`: `bool`, whether I foresee to let the course count for credits or not
###### `class Date`
```Python
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        self.validate_date()

    def validate_date(self):
        """Validates the date to ensure it is correct."""
        from calendar import monthrange
        if not (1 <= self.month <= 12):
            raise ValueError("Month must be between 1 and 12")
        if not (1 <= self.day <= monthrange(self.year, self.month)[1]):
            raise ValueError("Day is out of range for the given month and year")

    def __str__(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year}"

    def __repr__(self):
        return f"Date(day={self.day}, month={self.month}, year={self.year})"

    def __eq__(self, other):
        if isinstance(other, Date):
            return (self.day == other.day and
                    self.month == other.month and
                    self.year == other.year)
        return False

    def __lt__(self, other):
        if isinstance(other, Date):
            return (self.year, self.month, self.day) < (other.year, other.month, other.day)
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Date):
            return (self.year, self.month, self.day) <= (other.year, other.month, other.day)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Date):
            return (self.year, self.month, self.day) > (other.year, other.month, other.day)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Date):
            return (self.year, self.month, self.day) >= (other.year, other.month, other.day)
        return NotImplemented

```
###### `class Scale`
```Python
class Scale:
    def __init__(self, lowest, sufficient, maximal):
        self.lowest = lowest
        self.sufficient = sufficient
        self.maximal = maximal
        self.validate_scale()

    def validate_scale(self):
        """Validates the scale to ensure the integers are in the correct order."""
        if not ((self.lowest <= self.sufficient <= self.maximal) or self.lowest >= self.sufficient >= self.maximal)):
            raise ValueError("The scale values must be in the order: lowest <= sufficient <= maximal")

    def __str__(self):
        return f"Lowest: {self.lowest}, Sufficient: {self.sufficient}, Maximal: {self.maximal}"

    def __repr__(self):
        return f"Scale(lowest={self.lowest}, sufficient={self.sufficient}, maximal={self.maximal})"

    def is_within_scale(self, value):
        """Checks if a given value is within the scale."""
        return (self.lowest <= value <= self.maximal) or (self.lowest >= value >= self.maximal)

	def is_sufficient(self, value):
	    """Checks if a given value is between the sufficient and maximal marks."""
	    if self.lowest <= self.maximal:
	        return self.sufficient <= value <= self.maximal
	    else:
	        return self.sufficient >= value >= self.maximal

    def is_maximal(self, value):
        """Checks if a given value is at the maximal mark."""
        return value == self.maximal
```
###### `class Mark`
```Python
class Mark:
    def __init__(self, value, scale):
        self.value = value
        self.scale = scale
        self.validate_mark()

    def validate_mark(self):
        """Validates that the value is within the scale."""
        if not self.scale.is_within_scale(self.value):
            raise ValueError("The value is out of the defined scale")

    def __str__(self):
        return f"Value: {self.value}, Scale: ({self.scale})"

    def __repr__(self):
        return f"Mark(value={self.value}, scale={self.scale})"

    def percentage(self):
        """Returns the mark as a percentage of the maximal value in the scale."""
        return (self.value / self.scale.maximal) * 100

    def is_passing(self):
        """Checks if the mark meets or exceeds the sufficient mark in the scale."""
        return self.scale.is_sufficient(self.value)
```
==le, ge, lt, gt, eq==
###### `class Period`
```Python
class Period:
    def __init__(self, semester, period_num):
        self.semester = semester
        self.period_num = period_num
        self.validate_period()

    def validate_period(self):
        """Validates the period attributes."""
        if not isinstance(self.semester, int) or self.semester <= 0:
            raise ValueError("Semester must be a positive integer.")
        if self.period_num not in {1, 2, 3}:
            raise ValueError("Period number must be 1, 2, or 3.")

    def __str__(self):
        return f"Semester {self.semester}, Period {self.period_num}"

    def __repr__(self):
        return f"Period(semester={self.semester}, period_num={self.period_num})"

    def __eq__(self, other):
        if isinstance(other, Period):
            return (self.semester == other.semester and
                    self.period_num == other.period_num)
        return False

    def __lt__(self, other):
        if isinstance(other, Period):
            return (self.semester, self.period_num) < (other.semester, other.period_num)
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Period):
            return (self.semester, self.period_num) <= (other.semester, other.period_num)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Period):
            return (self.semester, self.period_num) > (other.semester, other.period_num)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Period):
            return (self.semester, self.period_num) >= (other.semester, other.period_num)
        return NotImplemented
```
###### `class Test`
```Python
class Test:
    def __init__(self, mark, relevance, date, taken, passed, exam_type, open_book):
        self.mark = mark
        self.relevance = relevance
        self.date = date
        self.taken = taken
        self.passed = passed
        self.exam_type = exam_type
        self.open_book = open_book
        self.validate_test()

    def validate_test(self):
        """Validates the test attributes."""
        if not isinstance(self.mark, Mark):
            raise TypeError("mark must be an instance of Mark")
        if not (0 <= self.relevance <= 1):
            raise ValueError("relevance must be between 0 and 1")
        if not isinstance(self.date, Date):
            raise TypeError("date must be an instance of Date")
        if not isinstance(self.taken, bool):
            raise TypeError("taken must be a boolean")
        if not isinstance(self.passed, bool):
            raise TypeError("passed must be a boolean")
        if self.exam_type not in {'oral', 'written', 'take-home'}:
            raise ValueError("exam_type must be 'oral', 'written', or 'take-home'")
        if self.exam_type == 'take-home' and not self.open_book:
            raise ValueError("take-home exams must be open book")

    def __str__(self):
        return (f"Mark: {self.mark}, Relevance: {self.relevance:.2f}, "
                f"Date: {self.date}, Taken: {self.taken}, "
                f"Passed: {self.passed}, Type: {self.exam_type}, "
                f"Open Book: {self.open_book}")

    def __repr__(self):
        return (f"Test(mark={self.mark}, relevance={self.relevance}, "
                f"date={self.date}, taken={self.taken}, "
                f"passed={self.passed}, exam_type={self.exam_type}, "
                f"open_book={self.open_book})")
```
###### `class Course`
```Python
class Course:
    def __init__(self, full_name, credits, counted, *tests):
        self.full_name = full_name
        self.credits = credits
        self.counted = counted
        self.tests = tests
        self.validate_course()

    def validate_course(self):
        """Validates the course attributes."""
        if not isinstance(self.full_name, str):
            raise TypeError("full_name must be a string")
        if not isinstance(self.credits, int) or self.credits < 0:
            raise ValueError("credits must be a non-negative integer")
        if not isinstance(self.counted, bool):
            raise TypeError("counted must be a boolean")
        if not all(isinstance(test, Test) for test in self.tests):
            raise TypeError("All tests must be instances of Test")

    def __str__(self):
        tests_str = ', '.join(str(test) for test in self.tests)
        return (f"Full Name: {self.full_name}, Credits: {self.credits}, "
                f"Counted: {self.counted}, Tests: [{tests_str}]")

    def __repr__(self):
        return (f"Course(full_name={self.full_name}, credits={self.credits}, "
                f"counted={self.counted}, tests={self.tests})")

    def compute_weighted_average(self):
        """Computes the weighted average of taken tests and the sum of their relevance.

        Returns:
            tuple: (total_relevance, weighted_average) or (0, 0) if no tests have been taken.
        """
        total_value = 0
        total_relevance = 0

        for test in self.tests:
            if test.taken:
                total_value += test.mark.value * test.relevance
                total_relevance += test.relevance

        if total_relevance == 0:
            return 0, 0  # If no tests have been taken, return 0 for both values

        weighted_average = total_value / total_relevance
        return total_relevance, weighted_average
```
###### `class MarksState`
```Python
class MarksState:
    def __init__(self, *courses):
        self.courses = courses
        self.validate_marks_state()

    def validate_marks_state(self):
        """Validates that all courses are instances of the Course class."""
        if not all(isinstance(course, Course) for course in self.courses):
            raise TypeError("All courses must be instances of Course")

    def compute_weighted_average(self, courses):
        """Helper method to compute the weighted average based on relevance (within courses) and credits (between courses)."""
        total_credits = 0
        weighted_sum = 0
        
        for course in courses:
            relevant_tests = [test for test in course.tests if test.taken]
            total_relevance = sum(test.relevance for test in relevant_tests)
            
            if total_relevance > 0:
                course_weighted_sum = 0
                for test in relevant_tests:
                    course_weighted_sum += test.mark.value * test.relevance
                
                course_average = course_weighted_sum / total_relevance
                weighted_sum += course_average * course.credits
                total_credits += course.credits
        
        if total_credits == 0:
            return (0, 0)  # No valid tests to average
        
        weighted_average = weighted_sum / total_credits
        return (total_credits, weighted_average)

    def period_average(self, courses, period_num):
        """Compute the average for a specific period within a set of courses."""
        period_courses = [course for course in courses if course.period.period_num == period_num]
        return self.compute_weighted_average(period_courses)
    
    def semester_average(self, courses, semester_num):
        """Compute the average for all periods within a specific semester."""
        semester_courses = [course for course in courses if course.period.semester == semester_num]
        return self.compute_weighted_average(semester_courses)
    
    def overall_average(self):
        """Compute the overall weighted average across all courses."""
        return self.compute_weighted_average(self.courses)
    
    def generate_report(self):
        """Generates the basic report displaying overall, per semester, and per period averages, along with total credits."""
        report = []
        
        overall_credits, overall_avg = self.overall_average()
        report.append(f"Overall Average: {overall_avg:.2f} (Total Credits: {overall_credits})")
        
        semesters = sorted(set(course.period.semester for course in self.courses))
        
        for semester in semesters:
            semester_credits, semester_avg = self.semester_average(self.courses, semester)
            if semester_credits == 0:
                continue
            
            report.append(f"Semester {semester} Average: {semester_avg:.2f} (Total Credits: {semester_credits})")
            
            for period_num in [1, 2, 3]:
                period_credits, period_avg = self.period_average(self.courses, period_num)
                if period_credits == 0:
                    continue
                
                report.append(f"  Period {period_num} Average: {period_avg:.2f} (Total Credits: {period_credits})")
        
        return "\n".join(report)
    
    # New extended report methods
    def generate_extended_report(self):
        """Generates an extended report with course details for each period, including course name, average, and credits."""
        report = []

        overall_credits, overall_avg = self.overall_average()
        report.append(f"Overall Average: {overall_avg:.2f} (Total Credits: {overall_credits})")

        semesters = sorted(set(course.period.semester for course in self.courses))
        
        for semester in semesters:
            semester_credits, semester_avg = self.semester_average(self.courses, semester)
            if semester_credits == 0:
                continue

            report.append(f"Semester {semester} Average: {semester_avg:.2f} (Total Credits: {semester_credits})")
            
            for period_num in [1, 2, 3]:
                period_credits, period_avg = self.period_average(self.courses, period_num)
                if period_credits == 0:
                    continue

                report.append(f"  Period {period_num} Average: {period_avg:.2f} (Total Credits: {period_credits})")

                # Add courses within the period
                period_courses = [course for course in self.courses if course.period.period_num == period_num]
                for course in period_courses:
                    total_relevance, course_avg = course.compute_weighted_average()
                    report.append(f"    Course: {course.full_name} | Mark: {course_avg:.2f} | Credits: {course.credits}")

        return "\n".join(report)

    def generate_super_extended_report(self):
        """Generates a super extended report with detailed test information for each course."""
        report = []

        overall_credits, overall_avg = self.overall_average()
        report.append(f"Overall Average: {overall_avg:.2f} (Total Credits: {overall_credits})")

        semesters = sorted(set(course.period.semester for course in self.courses))
        
        for semester in semesters:
            semester_credits, semester_avg = self.semester_average(self.courses, semester)
            if semester_credits == 0:
                continue

            report.append(f"Semester {semester} Average: {semester_avg:.2f} (Total Credits: {semester_credits})")
            
            for period_num in [1, 2, 3]:
                period_credits, period_avg = self.period_average(self.courses, period_num)
                if period_credits == 0:
                    continue

                report.append(f"  Period {period_num} Average: {period_avg:.2f} (Total Credits: {period_credits})")

                # Add courses within the period
                period_courses = [course for course in self.courses if course.period.period_num == period_num]
                for course in period_courses:
                    total_relevance, course_avg = course.compute_weighted_average()
                    report.append(f"    Course: {course.full_name} | Mark: {course_avg:.2f} | Credits: {course.credits}")

                    # Add test details for each course
                    for test in course.tests:
                        if test.taken:
                            report.append(f"      Test: {test.exam_type} | Mark: {test.mark.value:.2f} | "
                                          f"Relevance: {test.relevance:.2f} | Passed: {test.passed}")

        return "\n".join(report)
```
