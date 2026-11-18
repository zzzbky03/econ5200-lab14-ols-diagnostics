"""Regression diagnostics that end in a recommendation (ECON 5200 Lab 14).

The design rule: a diagnostic that reports a statistic and stops leaves the reader to guess, so
recommend_cov gives back the covariance type to use and the reason for it.
"""
import pandas as pd
import statsmodels.api as sm

FEW_CLUSTERS = 40      # below about 40 clusters, cluster-robust tests reject too often (Ch 14)


def recommend_cov(groups=None) -> dict:
    """The covariance type the design calls for, chosen before looking at any residuals."""
    if groups is None:
        return {"cov_type": "HC3", "cov_kwds": {},
                "reason": "rows treated as independent: HC3 by default, whatever a test says"}
    n_groups = pd.Series(groups).nunique()
    reason = f"errors may be shared within each of {n_groups} groups: cluster on them"
    if n_groups < FEW_CLUSTERS:
        reason += f"; only {n_groups} clusters, so check with a wild cluster bootstrap"
    return {"cov_type": "cluster", "cov_kwds": {"groups": groups}, "reason": reason}


def fit_as_recommended(y, X, groups=None):
    """OLS of y on X plus an intercept, with the recommended covariance type, and the advice."""
    advice = recommend_cov(groups)
    fit = sm.OLS(y, sm.add_constant(X)).fit(cov_type=advice["cov_type"],
                                            cov_kwds=advice["cov_kwds"])
    return fit, advice
