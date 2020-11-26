# Code Examples for Checkpointing

These are the code examples demonstrating some of the basic concerns with using
checkpointing (saving state so a code can restart). The code calculates an
approximate value for pi (3.14159...). A description of how this works
and what all the files are, are in the sections below

## The files
All of these files should be run using e.g. `python3 <filename>` where you replace
<filename> with the one you want

* 01\_no\_restart.py This is the basic file that doesn't have any checkpointing
* 02\_broken\_writer.py and 03\_broken\_reader.py These are a *BROKEN* implementation
of a checkpoint - while the second can restart from the data written by the first, it
does it wrong.
* 04\_writer.py and 05\_reader.py These are a basic working checkpointed code using
pickle. The first part runs halfway and writes some state data which the second part
uses to restart from.
* 06\_statistical\_reader.py This code uses the result written by 02\_broken\_writer.py
to do an approximate restart - we get the right answer again, but not exactly the
same as we do from the original code

## The algorithm

If you're wondering how this code works, it uses the formula for the area of a 
circle, Area = pi * radius^2
We have a square, with sides of length 2, and a circle drawn inside this as big as
possible, so it touches all the edges.
The radius of this circle is 1, so its area is pi. The square has area 4.
Now we imagine throwing darts at the square such that every dart hits. And we count how
many are inside the circle, and how many we have thrown. Once we throw enough, the ratio
of these tends towards the value of pi/4.

To simulate throwing the darts, we pick  two random numbers, one for the position across (x)
and one for the position up-and-down. 
All the points inside a circle are less than a distance of *radius* from its centre, and
that's how we identify them using x^2 + y^2 < 1

Run this enough times, and we can get a very good approxmation to pi!




