# What are these files?

Here you will find some notebooks demonstrating the use of GPUs for
speeding up your code. You may wish to recap the Image Blurring process
from the NotebookToScript examples before starting, as this example is
used here too.

You may also be interested in [the wikipedia article on the Mandelbrot Set](https://en.wikipedia.org/wiki/Mandelbrot_set)



## What do I need to run these examples

Because these use dedicated hardware, you can't run them on absolutely any machine. We discuss
what you need in the notebooks, but we also recap it here:

* A computer with a GPU. You don't need a Tesla, but you do need something!
* The Python packages we used in the Image Blur example - numpy, PIL/pillow, matplotlib 
* Some extra Python packages - numba, pyculib (and any dependencies). We used CUDA-9.1 as CUDA-9.2 introduces some issues with other packages


The first Notebook, Part0-Introduction, will help you check whether your system
is capable of running the examples. Then you can work through the other two in order.

