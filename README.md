# Entropic Markov PRNG
Pseudo-RNG algorithm that uses Markov chains to maximize entropy

Markov Chain Model of Order 𝑘:

A context is a tuple of 𝑘 consecutive bits, denoted as 
```math 
s = (x_i-k+1 , ... , x_i)
```


```math
P(b | s) = \frac{N(s, b)}{N(s)}

```
