# Lab 5: Static Code Analysis — Issue Report

## Tools Used
- Pylint: Code quality and programming practices
- Bandit: Security vulnerabilities
- Flake8: Style and formatting

## Issues Identified and Fixes

| No. | Issue | Type | Original Location | Description | Fix Applied |
|---|---|---|---|---|---|
| 1 | Mutable default argument | Bug | Line 15 | Using `entry_logs=[]` shares a mutable list across function calls. | Changed the default to `None` and initialized a new list inside the function. |
| 2 | Unsafe `eval()` | Security | Line 48 | Evaluating an expression dynamically can execute unintended code. | Replaced dynamic evaluation with numeric surge-multiplier validation and arithmetic. |
| 3 | Bare exception handler | Code quality | Line 32 | A bare `except` can hide unexpected errors. | Removed the broad handler and used explicit handling of invalid slot identifiers. |
| 4 | Shell command execution | Security | Line 64 | `os.system()` executes a shell command unnecessarily. | Removed shell execution and used a formatted Python print statement. |
| 5 | Unsafe file handling | Code quality | Line 61 | The file was opened without a context manager or explicit encoding. | Used `with open(..., encoding="utf-8")` for automatic resource cleanup. |
| 6 | Insecure random PIN generation | Security | Line 57 | Standard pseudo-random generation is not suitable for security-sensitive PINs. | Used `secrets.randbelow()` to generate a four-digit PIN. |
| 7 | Non-standard function names | Style | Multiple lines | CamelCase function names do not follow PEP 8 naming conventions. | Renamed functions to snake_case and updated their calls. |
| 8 | Missing docstrings | Code quality | Multiple lines | Functions lacked documentation. | Added docstrings describing function purposes. |
| 9 | Unused variables/imports | Code quality | Multiple lines | Unused variables and imports reduce readability. | Removed unnecessary declarations and imports. |
| 10 | Input validation | Reliability | Parking and fee functions | Invalid inputs could cause unexpected behavior. | Added validation for slot IDs, plate numbers, booked hours, and surge multipliers. |

## Verification Results

- Initial Pylint score: 4.10/10.
- Updated Pylint score: 9.67/10.
- Final Bandit scan: No issues identified.
- Flake8: Check `flake8_report.txt` for the final result.
- Program execution: Successfully executed during verification.

## Conclusion

Static analysis helped identify code-quality, reliability, style, and security issues. Fixes improved readability and safer handling of user inputs, files, and PIN generation.
