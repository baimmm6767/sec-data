sec-data is an open-source Python engine that extracts detailed, modelling-ready financial statements directly from SEC filings and exports them to local CSV or Excel files.

The primary supported workflow is quarterly financial extraction for U.S. domestic filers using 10-Q and 10-K filings. The engine combines XBRL facts, presentation and calculation linkbases, dynamic custom-tag handling, cross-filing reconciliation, HTML fallback extraction, accounting-identity repairs, Q4 derivation, segment and geographic disclosure extraction, filing-aware row ordering, parallel processing, and persistent caching.

Unlike financial-data websites that limit exports or require paid API access, sec-data runs entirely on the user’s machine. The resulting datasets remain local, editable, and ready for financial modelling, valuation work, screening tools, research applications, or integration into other open-source platforms.

Current capabilities include:

* Detailed quarterly income statements, balance sheets, and cash-flow statements for U.S. filers
* Business-segment and geographic-revenue breakdowns
* Company-specific and custom XBRL line-item support
* Cross-filing historical reconciliation
* Automated Q4 reconstruction from annual and year-to-date values
* Accounting identity, cash-flow, debt, equity, and segment reconciliation
* Filing-like statement organization and human-readable row ordering
* CSV export and multi-sheet Excel workbooks
* Parallel SEC filing retrieval, rate limiting, retries, and persistent local caching
* Optional Arelle-assisted custom-tag enrichment

Experimental and work-in-progress features include:

* Native annual-only extraction through the `--annual` option
* Foreign private issuer annual extraction from 20-F and 40-F filings
* IFRS and non-U.S. taxonomy handling
* Complex industry-specific statement structures
* Unusually tagged or historically inconsistent filings

Foreign quarterly reporting, broad international exchange coverage, analyst estimates, market prices, transcripts, and operating metrics are not currently part of the stable core.

The project is intended to serve both individual investors who want unrestricted local financial data and developers building open-source research platforms, Excel tools, APIs, dashboards, screeners, valuation systems, and financial applications.

The stable product focus is detailed U.S. quarterly financial statements. Annual and foreign-filer support should currently be treated as experimental.

All generated outputs should be reviewed before being used the outputs from this script is not in any way shape or form financial advice.
