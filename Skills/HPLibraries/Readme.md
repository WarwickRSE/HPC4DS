# What are these files?

These files accompany the "High performance Libraries" Skills Module. We
revist some of the material from other modules a little, as well as new things. 


## Why Is there Fortran Code?

For this part, we have to move away from Python briefly. This is because there is
no flexible, system independent way to control the use of BLAS from numpy, wheras
Fortran makes it easy for us to use either the built in, or an external, BLAS
implementation. This can really matter when going for the last bit of performance
because often the built-in version of functions like this have a lot of scope
for optimisation that a library like BLAS can do wonders with.


As we say in the sheet, you can compile this using either
`gfortran -O3 01_BLAS.f90 -omatrix_timer`
to use built-in functions
`gfortran -O3 01_BLAS.f90 -omatrix_timer -fexternal-blas - lopenblas`
to use openblas, as long as you have this installed

If you are familiar with Fortran, and prefer a different compiler, there
are analogs of this for many - consult compiler docs for details

