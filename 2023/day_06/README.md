# Solve Proccess

I'll split the total t time to t1 and t2, t1 is the time the boat
accelerates, and t2 the time after that (t1 + t2 = t).

Every second in t1 the velocity of the boat (v) increases by 1
milimiter per milisecond.

Thus v can be described by the following:
$$v = t1$$

Which means that x (the board total movment) will be:
$$
x = v * t2 \
  = t1 * t2 \
  = t1 * (t - t1) \ 
  = t1 * t - t1 ^ 2
$$

But we now x from the question, so we can solve for t1:
$$
t1 ^ 2 - t * t1 + x = 0

t1_0 = (t - sqrt(t^2 - 4x)) / 2
t1_1 = (t + sqrt(t^2 - 4x)) / 2
$$


And we look for the range of t1 so to solve our problem we can find:
$$
t1_1 - t1_0 + 1 =
  = ceil((t + sqrt(t^2 - 4x)) / 2 - 1)
    - floor((t - sqrt(t^2 - 4x)) / 2 + 1) + 1
$$
=======
# Solving Proccess

I'll split the total time $t$ to $t_1$ and $t_2$, $t_1$ is the acceleration time, and $t_2$ is the moving time ($t1 + t2 = t$).

In every milisecond that passes in $t_1$ the velocity of the boat $v$, increases by $1$ milimiter per milisecond. Thus $v$ can be described by the following formula:
$$v = t_1$$
Which means that $x$, the total distance that the boat made can be expressed as:
$$x = t_2v = t_1t_2 = t_1(t - t_1) = t_1t - t_1 ^ 2$$

But we now the value of $x$, so we can use this equation to solve for $t_1$:
$$t_1 ^ 2 - t1(t) + x = 0$$
Using the quadratic formula:
$$t_{1_0}, t_{1_1} = \frac{t \pm \sqrt{t^2 - 4x}}{2}$$

Lastly, to find $t_1$ inclusive range, we can calculate:
$$\Delta t_1 + 1 =$$
$$= \lceil \frac{t + \sqrt{t^2 - 4x}}{2} - 1 \rceil
    \lfloor \frac{t - \sqrt{t^2 - 4x}}{2} + 1 \rfloor + 1
$$

Now, the same calculation in Python:
```Python
def calculate_range(t: int, x: int) -> int:
    root = math.sqrt(t * t - 4 * x)
    return math.ceil((t + root) / 2 - 1) - math.floor((t - root) / 2 + 1) + 1
```