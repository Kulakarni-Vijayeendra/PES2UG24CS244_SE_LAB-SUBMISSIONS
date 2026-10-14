# Lab 5: Static Code Analysis — Reflection

> Note: The provided Lab 5 handout asks for reflection answers but does not list specific questions. The answers below address the lab's stated learning outcomes and the work completed.

## 1. What is static code analysis, and why is it useful?

Static code analysis examines source code without executing the program. It helps identify potential bugs, insecure coding patterns, and style or maintainability problems early in development. Finding these issues before deployment can make software safer, easier to understand, and less expensive to maintain.

## 2. What are the differences between Pylint, Bandit, and Flake8?

- **Pylint** checks code quality and programming practices. It can identify issues such as poor naming, unused variables, missing documentation, and potential design problems.
- **Bandit** focuses on security. It scans Python code for common security risks and unsafe coding patterns.
- **Flake8** checks Python style and formatting, including many PEP 8 violations and common code-quality errors.

Using all three provides complementary checks: general code quality, security, and style.

## 3. What issues were identified and how were they fixed?

The original parking lot program contained several problems. The mutable default argument for `entry_logs` was replaced with a `None` default and initialized inside the function. Broad exception handling was narrowed. The use of `eval()` for fee calculation was removed in favor of direct arithmetic and validation. Shell execution through `os.system()` was removed, and file writing was changed to use a context manager with an explicit encoding. Ticket PIN generation was changed to use Python's `secrets` module rather than a general-purpose random number generator. Input validation was also added for values such as parking duration and the surge multiplier.

These changes reduce unintended shared state, avoid unnecessary code execution risks, make file handling more reliable, and reject invalid input.

## 4. How did static analysis improve the code's quality and maintainability?

Static analysis gave specific feedback that could be used to improve the program systematically. After changes, the final reports showed a Pylint score of **9.67/10**, Bandit reported **no issues identified**, and Flake8 produced no reported violations. Pylint still reported a warning related to the use of a global statement, so the score was not perfect. Overall, the tools helped identify problems that could be overlooked during manual review and provided a way to verify the changes after fixing them.
