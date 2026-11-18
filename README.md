# OLS Diagnostics: Robust and Clustered Standard Errors

## Objective
I tested when a nominal 95% confidence interval for an OLS slope actually covers the true value, and which standard errors fix the problem.

## Methodology
- Simulated 500 samples where the error variance grows with x, and counted how often classical, HC1 and HC3 intervals contained the true slope.
- Simulated 300 panels of 40 firms with 25 employees each, where workers in the same firm share a shock, and compared classical, HC3 and firm-clustered intervals.
- Fit one regression with six types of standard errors (classical, HC0–HC3, clustered) and compared how much clustering changed each coefficient.
- Added three planted rows to the data and used leverage, studentised residuals and Cook's distance to find which one moved the slope.
- Wrote my own prompt asking an AI for a function that builds the standard error table, then checked every number against statsmodels.
- Saved a small module, `src/diagnostics.py`, that recommends HC3 or clustered standard errors based on the design.

## Key Findings
- With heteroskedastic errors, classical intervals covered 92.4% and HC3 covered 94.4%.
- With errors shared within 40 firms, HC3 covered only 50.3%, while clustering by firm covered 93.7%. Robust standard errors do not fix dependence within groups.
- Only one of the three planted rows moved the slope, from 1.4927 to 1.4468, because it had both high leverage and a large residual.
- The common flagging rules also flagged many real rows, so I would use them to check rows, not to delete them.
