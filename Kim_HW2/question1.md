# question 1 problem solving

**q1-1)**
<br>
_note: table is in index.html_

**q1-2)**

1. **let p(n) be the statement:** 1\^2 + 2^2 + 3^2 + ... (2n - 1)^2 + (2n)^2 = n(2n + 1)(4n + 1) / 3
2. **basis:** first 2n positive integers (verify p(1) is true)
   <br>
   1^2 + 2^2 = 1(2(1) + 1)(4(1) + 1) / 3
   <br>
   5 = 1(3)(5)/3
   <br>
   5 = 5 ✔️
   <br>
3. **inductive step: p(k) → p(k+1)**
   <br>
   **inductive hypothesis:** assume 1\^2 + 2^2 + 3^2 + ... (2k - 1)^2 + (2k)^2 = k(2k + 1)(4k + 1) / 3
   <br>
   <br>
   _what to show:
   <br>
   1\^2 + 2^2 + 3^2 + ... (2(k + 1) - 1)^2 + (2(k + 1))^2 = k(2(k + 1) + 1)(4(k + 1) + 1) / 3
   <br>
   1\^2 + 2^2 + 3^2 + ... (2(k + 1) - 1)^2 + (2(k + 1))^2 = (k + 1)(2k + 3)(4k + 5) / 3
   <br>
   1\^2 + 2^2 + 3^2 + ... (2(k + 1) - 1)^2 + (2(k + 1))^2 = 1/3 [8k^3 + 30k^2 + 37k + 15]_
   <br>
   <br>
   1\^2 + 2^2 + 3^2 + ... (2k - 1)^2 + (2k)^2 **+ (2k + 1)^2 + (2k + 2)^2** = k(2k + 1)(4k + 1) / 3 **+ (2k + 1)^2 + (2k + 2)^2**
   <br>
   _note: expand and then multiply top and bottom of fraction by 3 to combine_
   <br>
   1\^2 + 2^2 + 3^2 + ... (2k - 1)^2 + (2k)^2 **+ (2k + 1)^2 + (2k + 2)^2** = k(2k + 1)(4k + 1) / 3 **+ 3 (8k^2 + 12k + 5) / 3**
   <br>
   1\^2 + 2^2 + 3^2 + ... (2k - 1)^2 + (2k)^2 **+ (2k + 1)^2 + (2k + 2)^2** = 1/3 [k(2k + 1)(4k + 1) + (8k^2 + 12k + 5)]
   <br>
   1\^2 + 2^2 + 3^2 + ... (2k - 1)^2 + (2k)^2 **+ (2k + 1)^2 + (2k + 2)^2** = 1/3 [8k^3 + 30k^2 + 37k + 15]
   <br>
   _matches answer in what to show!_
4. because the basis is true and p(k) → p(k + 1), p(n) is true for all n >= 1 by mathematical induction.
   <br>

**q1-3)**

1. let p(n) be the statement: finding a counterfeit coin among 3^n coins requires exactly n weighings
2. **basis:** prove p(1) is true
   <br>
   we have 3^1 = 3 coins, and one is counterfeit
   <br>
   put coin 1 on the left side of a scale and coin 2 on the right side, leave coin 3 off:
   <br> a. if the scale is balanced → coin 1 and 2 are real, coin 3 is the counterfeit
   <br> b. if the left side is heaver → coin 1 is the counterfeit, assuming counterfeit coins are heavier
   <br> c. if the right side is heaver → coin 2 is the counterfeit
   <br>
   <br>
   all of this used 1 weighing, so p(1) ✔️
3. **inductive step: p(k) → p(k+1)**
   <br>
   inductive hypothesis: assume finding a counterfeit coin among 3^k coins requires exactly k weighings
   <br>
   3^(k + 1) coins, one counterfeit coin
   <br>
   3^(k + 1) = (3 \* 3^k) = (3^k + 3^k + 3^k)
   <br>
   <br>
   divide 3^(k + 1) coins into 3 equal groups of 3^k coins (call them groups: A, B, C)
   <br>
   weigh A vs. B (1 weighing)
   <br>
   a. if balanced, A and B are real, C has the counterfeit
   <br>
   b. if A is heavier, A is the counterfeit
   <br>
   c. if B is heavier, B is the counterfeit
   <br>
   <br>
   in all cases, we identified which group of 3^k is the counterfeit. by our inductive hypothesis, we know it's true that finding a counterfeit among 3^k coins requires k weighings.
   <br>
   so the total weighings is: 1 (to find the group) + k (to find the counterfeit in the group) = k + 1
   <br>
   therefore p(k + 1) is true
   <br>
   p(n) is true for all n >= 1
