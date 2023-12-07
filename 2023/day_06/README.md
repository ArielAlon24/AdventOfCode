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
