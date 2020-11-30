MODULE support

  USE ISO_FORTRAN_ENV
  IMPLICIT NONE

  CONTAINS

  FUNCTION get_cols() RESULT(cols)

    CHARACTER(LEN=1000) :: str_arg
    INTEGER :: cols, err

    IF (COMMAND_ARGUMENT_COUNT() /= 1) THEN
      CALL GET_COMMAND_ARGUMENT(0,str_arg)
      PRINT *, 'Usage : ',TRIM(str_arg),' <number_of_matrix_elements>'
      STOP
    END IF

    CALL GET_COMMAND_ARGUMENT(1,str_arg)
    READ(str_arg, *, iostat=err) cols

    IF (err /= 0) THEN
      PRINT *, 'Number of matrix elements specified must be an integer!'
      STOP
    END IF
  END FUNCTION get_cols

  SUBROUTINE random_init

    LOGICAL, SAVE :: init_done = .FALSE.
    INTEGER :: n, count
    INTEGER, DIMENSION(:), ALLOCATABLE :: seed
    REAL :: warm(1000)

    IF (init_done) RETURN
    init_done = .TRUE.
    CALL RANDOM_SEED(size=n)
    ALLOCATE(seed(n))
    DO n = 1, SIZE(seed)
      seed(n) = n
    END DO
    CALL RANDOM_SEED(put = seed)

    !Warm up the RNG
    CALL RANDOM_NUMBER(warm)

  END SUBROUTINE random_init

END MODULE support

PROGRAM matrix_timer

  USE support
  IMPLICIT NONE

  REAL(REAL64), DIMENSION(:,:), ALLOCATABLE :: matrix1, matrix2, result
  INTEGER :: cols,t1, t2

  cols = get_cols()

  ALLOCATE(matrix1(cols,cols), matrix2(cols,cols), result(cols, cols))
  CALL random_init
  CALL RANDOM_NUMBER(matrix1)
  CALL RANDOM_NUMBER(matrix2)

  CALL SYSTEM_CLOCK(t1)
  result = MATMUL(matrix1, matrix2)
  CALL SYSTEM_CLOCK(t2)

  PRINT *, 'Time in matrix multiply is ', t2-t1
  PRINT *, "Maximum value of result matrix is ", MAXVAL(result)
  PRINT *, "(This is needed to prevent the compiler optimising the work away)"
 
END PROGRAM matrix_timer
