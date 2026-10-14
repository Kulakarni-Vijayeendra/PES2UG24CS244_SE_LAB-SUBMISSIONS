# Lab 5: Static Code Analysis — Reflection

## 1. What is static code analysis, and why is it useful?

Static code analysis examines source code without executing the program. It helps identify potential bugs, security vulnerabilities, poor programming practices, and style violations early in development.

## 2. What did Pylint, Bandit, and Flake8 contribute?

Pylint identified code-quality problems, including naming conventions, missing docstrings, unused variables, and mutable default arguments. Bandit detected security-sensitive coding patterns. Flake8 checked Python style and formatting rules.

## 3. Which issues were important to fix, and how were they addressed?

The unsafe use of `eval()`, shell-command execution, and insecure PIN generation were important security concerns. The mutable default argument and broad exception handling could also lead to reliability problems. These issues were addressed using explicit validation, safer Python APIs, and improved resource handling.

## 4. How did static analysis improve the program?

The analysis guided systematic fixes rather than relying only on manual inspection. The Pylint score increased from 4.10/10 to 9.67/10, and the final Bandit scan reported no issues. The program was also executed to check its behavior after modification.

## Conclusion

Using multiple static analysis tools provides complementary checks for quality, security, and style. Static analysis does not replace runtime testing, but it makes code easier to maintain and helps detect potential problems before deployment.
