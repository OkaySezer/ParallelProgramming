custom_power = lambda x=0, / , e=1: x ** e #custom_power is a lambda function that takes two parameters: x and e. x is the base and e is the exponent. The function returns x raised to the power of e. The default value for x is 0 and the default value for e is 1. The / symbol indicates that x is a positional-only parameter, meaning it cannot be passed as a keyword argument.

def custom_equation(x:int = 0, y:int = 0 , / , a:int = 1 , b:int = 1 , * , c:int = 1 ) -> float:
    
    """
    This function solves the equation (x**a + y**b) / c.

    :param x: The value of x in the equation. Default is 0.
    :param y: The value of y in the equation. Default is 0.
    :param a: The coefficient of x in the equation. Default is 1.
    :param b: The coefficient of y in the equation. Default is 1.
    :param c: The constant term in the equation. Default is 1.
    :return: The result of the equation.
    """
    
    return (x**a + y**b) / c  


def fn_w_counter() -> tuple[int, dict[str, int]]:
    if not hasattr(fn_w_counter, "total_calls"):
        fn_w_counter.total_calls = 0
        fn_w_counter.callers_dict = {}

    fn_w_counter.total_calls += 1
    caller = __name__

    if caller in fn_w_counter.callers_dict:
        fn_w_counter.callers_dict[caller] += 1
    else:
        fn_w_counter.callers_dict[caller] = 1

    return fn_w_counter.total_calls, fn_w_counter.callers_dict

