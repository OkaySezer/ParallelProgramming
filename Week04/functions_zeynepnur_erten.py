
custom_power = lambda x=0,/, e=1 : x ** e


def custom_equation(int x, int y, /, int a, int b,*, int c) -> float :
  """
   This function returns the result of an operation based on the specified base and exponent values.

   :param x: First base value
   :param y: Second base value
   :param a: First exponent value
   :param b: Second exponent value
   :param c: Divisor value
   :return: (x*a + y*b)/c
  """
  return (x**a + y**b)/c


calls = 0
def fn_w_counter()->(int, dict[str, int]):
    global calls,
    calls += 1
    return calls, {__name__: calls }

  

  
