# Syntax-analyzer-parser
The project was created for credit in the course Mathematical Linguistics in college.
LL(1) syntactic analyzer that implements a generative dissection algorithm with a one symbol in advance for following grammar:

𝑆 ∷= 𝑊 ; 𝑆

𝑊 ∷= 𝑃𝑊’

𝑊’ ∷= 𝑂𝑊 | 𝜀

𝑃 ∷= 𝑅 | (𝑊)

𝑅 ∷= 𝐿𝑅’

𝑅′ ∷= . 𝐿 | 𝜀

𝐿 ∷= 𝐶𝐿’

𝐿′ ∷= 𝐿 | 𝜀

𝐶 ∷= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

𝑂 ∷= ∗ | ∶ | + | − | ˆ

Based on the above grammar, a reduced syntax diagram for the three main productions S, W and L was designed.

![S_grammar_schema](https://user-images.githubusercontent.com/75490317/189102847-92bae67a-55e2-4bcb-80bb-a6a6a4f76d28.png)
![W_grammar_schema](https://user-images.githubusercontent.com/75490317/189102867-d50db454-e970-414d-8ec9-d2012832ff73.png)
![L_grammar_schema](https://user-images.githubusercontent.com/75490317/189102887-3bd4b8ab-970c-4f44-b3cf-1282e3476476.png)

Examples of program execution:

![Error_message](https://user-images.githubusercontent.com/75490317/189174663-14b35b98-a275-44d3-9ed9-a65054856fa2.png)
![Good_message](https://user-images.githubusercontent.com/75490317/189174677-eea09509-1b79-4596-b021-10ca7e7b6410.png)

Author: Cezary Bujak
