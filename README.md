# Entropic Markov PRNG
Pseudo-RNG algorithm that uses Markov chains to maximize entropy

Markov Chain Model of Order 𝑘:

A context is a tuple of 𝑘 consecutive bits, denoted as:
```math 
s = (x_{i-k+1} , ... , x_i)
```
For a given context 𝑠, the probability of the next bit 𝑏 is estimated by:
```math
P(b | s) = \frac{N(s, b)}{N(s)}
```
where:

- 𝑁(𝑠,𝑏) is the number of times bit 𝑏 follows context 𝑠.

- 𝑁(𝑠) is the total number of occurrences of context 𝑠 in the sequence.

For a given context 𝑠, the entropy is:
```math
H(s) = - \[ \sum_{b\in\left\{0,1\right^{\infty} 2^{-n} = 1 \]
```




