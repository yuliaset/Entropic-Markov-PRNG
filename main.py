import numpy as np
import math
from collections import defaultdict, Counter

def build_markov_model(sequence, k):
    """
    Build a k-th order Markov chain model from the binary sequence.
    Returns:
        transition_counts: dict mapping context (tuple of k bits) to counts of next bits.
        context_counts: dict mapping context to total occurrences.
    """
    transition_counts = defaultdict(lambda: Counter())
    context_counts = Counter()

    for i in range(len(sequence) - k):
        context = tuple(sequence[i:i+k])
        next_bit = sequence[i+k]
        transition_counts[context][next_bit] += 1
        context_counts[context] += 1
    return transition_counts, context_counts

def calculate_entropy(transition_counts, context_counts):
    """
    Calculate the weighted average entropy for the transition probabilities.
    Returns:
        weighted_avg_entropy: average entropy weighted by context occurrence.
    """
    total_contexts = sum(context_counts.values())
    weighted_entropy_sum = 0.0
    for context, count in context_counts.items():
        counts = transition_counts[context]
        entropy = 0.0
        for next_bit, c in counts.items():
            p = c / count
            entropy -= p * math.log2(p)
        weighted_entropy_sum += (count / total_contexts) * entropy
    return weighted_entropy_sum

def iterative_generate_sequence(N, k):
    """
    Iteratively generate a binary sequence of length N.
    At each step, the program tests adding a 0 vs. a 1 and chooses the bit that
    yields a higher average transition entropy (closer to the ideal 1 bit).

    For the first k bits, we need an initial seed. Here we start with a fixed seed.
    """

    sequence = [0] * k

    while len(sequence) < N:

        candidate0 = sequence + [0]
        candidate1 = sequence + [1]

        if len(candidate0) < k + 1:
            sequence.append(np.random.choice([0,1]))
            continue

        trans0, cnt0 = build_markov_model(candidate0, k)
        trans1, cnt1 = build_markov_model(candidate1, k)

        entropy0 = calculate_entropy(trans0, cnt0)
        entropy1 = calculate_entropy(trans1, cnt1)

        if entropy0 >= entropy1:
            chosen = 0
        else:
            chosen = 1

        sequence.append(chosen)

        if len(sequence) % 50 == 0 or len(sequence) == N:
            print(f"Length {len(sequence)}: entropy0 = {entropy0:.3f}, entropy1 = {entropy1:.3f} -> Chose {chosen}")

    return sequence

if __name__ == "__main__":
    N = 2**10   
    k = 4     

    sequence = iterative_generate_sequence(N, k)
    print("\nFinal sequence:")
    print(sequence)

    trans, cnt = build_markov_model(sequence, k)
    final_entropy = calculate_entropy(trans, cnt)
    print(f"\nFinal weighted average transition entropy (order {k}): {final_entropy} bits")