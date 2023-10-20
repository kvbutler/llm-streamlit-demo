ideal_candidate_chain_problem = """
You are a hiring manager at Google.

Given a problem type and level of difficulty below provide an algorithmic computer science problem that would be used to evaluate a potential candidate for a job as a software engineer.

Problem type: {problem_type}
Difficulty: {difficulty}

---

Provide the output in the following format

Problem Description:

Example Inputs and Outputs:

Test Cases:
"""

ideal_candidate_chain_problem_old = """
You are a hiring manager at Google.

Given a problem type and level of difficulty below provide an algorithmic computer science problem that would be used to evaluate a potential candidate for a job as a software engineer.

Problem type: {problem_type}
Difficulty: {difficulty}

---

Example

Problem Description:

Given a string s, find the length of the longest substring without repeating characters.

Example Inputs and Outputs:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Test Cases:

s = "bbbbb"
s = "pwwkew"

---

Provide the output in the following format

Problem Description:

Example Inputs and Outputs:

Test Cases:
"""

ideal_candidate_chain_solution = """
You are a world class programmer on an interview at Google.

Given a problem in the following example format develop a solution in Python with passing test cases. The code should have a single entrypoint `main` respond with only code.

---

{problem}
"""

ideal_candidate_chain_solution_old = """
You are a world class programmer on an interview at Google.

Given a problem in the following example format develop a solution in Python with passing test cases. The code should have a single entrypoint `main` respond with only code.

---

Example

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Test Cases:

s = "bbbbb"
s = "pwwkew"

---

{problem}
"""