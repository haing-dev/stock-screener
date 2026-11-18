"""eq_scorecard (runs on WRDS Cloud): the investor scorecard of the equity plan (step E0.4 phase B), as registered in
docs/research/equity/STAGE0_REGISTRATION.md sections 2-9. One of the two seal-exempt jobs (plan v0.3 section 5.4):
it reads US 13F holdings, CRSP stock returns and CRSP fund returns from 2010-06 to the seal end (2025-12) and prints
only the output of registration section 8: statistics and rank shares per library investor, the tier lists, the
best-scored filers and funds the library holds no document for (name and rank shares), persistence tables and counts.
It prints no holding, no stock name, no return series and no average by style, sector or factor.

Build note (functions, the reading taken where the registration left room, run time):
docs/research/equity/SCORECARD_BUILD_NOTE.md. The investor table is the frozen file of phase A2, embedded below by
tools/equity/make_scorecard_job.py; it is the only investor input.

Two job names, both registered in tools/equity/seal_exempt.json (template steps only):
eq_sc_pull_v1 (re-run as eq_sc_pull_v1b, v1c, ... until pull_status prints ALL PULLS COMPLETE); every pull is
resumable, one data set per year, written under a temporary name and renamed:
  pull_base(sql, save, out, DATA)              manager names, CUSIP map, factors, book-to-market, fund headers, styles
  pull_crsp(sql, save, out, DATA)              crsp.msf_v2 2009-06..2025-12
  pull_agg(sql, save, out, DATA)               per filer and quarter: matched positions and value (SQL aggregate)
  pull_hold(sql, load, save, out, DATA)        holdings rows of filers that can be in a rank group + library filers
  pull_funds(sql, load, save, out, DATA)       CRSP fund monthly returns and assets (whole class groups)
  pull_status(load, out, DATA)                 ALL PULLS COMPLETE, or what is missing
eq_sc_cleanup_v1 (once the result is accepted):
  cleanup(out, DATA)                           deletes every eq_sc_ data set except eq_sc_report
eq_scorecard_v1 (build and report only):
  build(load, save, out, DATA)                 refuses to start unless every pull is complete and made for this input;
                                               keeps the report lines as data set eq_sc_report; returns nothing
  report(load, out, part, parts)               prints one part of the report (each python step under 60,000 chars)
"""
import hashlib
import json
import os
import random
import re
import time
import traceback
import warnings

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

VERSION = "eq_scorecard-1.1.0"

# >>> FROZEN INPUT (written by tools/equity/make_scorecard_job.py; the only part that may change between runs) >>>
INV = json.loads(r"""[{"end_ym": null, "explicit_max": 2.0, "explicit_mean": 0.11, "fundnos": [], "grade": "A", "id": "I001", "known_fundnos": [], "known_mgrnos": [13112], "mgrnos": [13112], "name": "Brad Gerstner", "own_docs": 27, "primary_style": "growth", "ran_money": "yes", "record_kind": "13f", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 0.12, "fundnos": [], "grade": "N", "id": "I002", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Bill Gurley", "own_docs": 26, "primary_style": "growth", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 1.79, "fundnos": [], "grade": "N", "id": "I003", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Stig Brodersen", "own_docs": 19, "primary_style": "deep_value", "ran_money": "unclear", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [95344], "grade": "F", "id": "I004", "known_fundnos": [62577, 95344], "known_mgrnos": [], "mgrnos": [], "name": "Tobias Carlisle", "own_docs": 16, "primary_style": "deep_value", "ran_money": "yes", "record_kind": "fund", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 1.71, "fundnos": [], "grade": "N", "id": "I005", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Kyle Grieve", "own_docs": 7, "primary_style": "quality_compounders", "ran_money": "unclear", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I006", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Hari Ramachandra", "own_docs": 12, "primary_style": "deep_value", "ran_money": "unclear", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 1.6, "fundnos": [], "grade": "N", "id": "I007", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Clay Finck", "own_docs": 5, "primary_style": "quality_compounders", "ran_money": "unclear", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 1.11, "fundnos": [7317, 8750, 28357], "grade": "F", "id": "I008", "known_fundnos": [7317, 8750, 28357], "known_mgrnos": [78320], "mgrnos": [], "name": "Chris Davis", "own_docs": 9, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "fund", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 0.89, "fundnos": [], "grade": "C", "id": "I009", "known_fundnos": [], "known_mgrnos": [66138], "mgrnos": [66138], "name": "Howard Marks", "own_docs": 9, "primary_style": "credit_distressed", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 3.0, "explicit_mean": 1.89, "fundnos": [56165, 58470, 59064], "grade": "F", "id": "I010", "known_fundnos": [56165, 58470, 59064], "known_mgrnos": [12775], "mgrnos": [], "name": "Joel Greenblatt", "own_docs": 9, "primary_style": "deep_value", "ran_money": "yes", "record_kind": "fund", "region": "us", "role": "investor", "shares_with": null, "start_ym": 201201}, {"end_ym": null, "explicit_max": 3.0, "explicit_mean": 1.22, "fundnos": [], "grade": "A", "id": "I011", "known_fundnos": [], "known_mgrnos": [26263], "mgrnos": [26263], "name": "Robert Vinall", "own_docs": 9, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 3.0, "explicit_mean": 2.14, "fundnos": [], "grade": "N", "id": "I012", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Ian Cassel", "own_docs": 7, "primary_style": "small_micro_cap", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 1.14, "fundnos": [], "grade": "C", "id": "I013", "known_fundnos": [101704, 105026], "known_mgrnos": [10558], "mgrnos": [10558], "name": "Mohnish Pabrai", "own_docs": 7, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 1.67, "fundnos": [], "grade": "A", "id": "I014", "known_fundnos": [], "known_mgrnos": [11757], "mgrnos": [11757], "name": "Chris Bloomstran", "own_docs": 6, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "13f", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 3.0, "explicit_mean": 2.17, "fundnos": [], "grade": "A", "id": "I015", "known_fundnos": [], "known_mgrnos": [14460], "mgrnos": [14460], "name": "Dev Kantesaria", "own_docs": 6, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "13f", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 3.0, "explicit_mean": 2.0, "fundnos": [], "grade": "A", "id": "I016", "known_fundnos": [], "known_mgrnos": [14144], "mgrnos": [14144], "name": "Fran\u00e7ois Rochon", "own_docs": 5, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "13f", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 1.8, "fundnos": [], "grade": "A", "id": "I017", "known_fundnos": [], "known_mgrnos": [53990], "mgrnos": [53990], "name": "Tom Gayner", "own_docs": 5, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "13f", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 1.0, "fundnos": [], "grade": "A", "id": "I018", "known_fundnos": [], "known_mgrnos": [9118, 14885], "mgrnos": [9118, 14885], "name": "Guy Spier", "own_docs": 4, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 0.75, "fundnos": [], "grade": "C", "id": "I019", "known_fundnos": [], "known_mgrnos": [41500], "mgrnos": [41500], "name": "Jeremy Grantham", "own_docs": 4, "primary_style": "macro_multi_asset", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 3.0, "explicit_mean": 2.33, "fundnos": [], "grade": "A", "id": "I020", "known_fundnos": [], "known_mgrnos": [8805], "mgrnos": [8805], "name": "Andrew Brenton", "own_docs": 3, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "A", "id": "I021", "known_fundnos": [], "known_mgrnos": [11194], "mgrnos": [11194], "name": "Chris Hohn", "own_docs": 3, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "A", "id": "I022", "known_fundnos": [], "known_mgrnos": [13616], "mgrnos": [13616], "name": "Christopher Begg", "own_docs": 3, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "13f", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 3.0, "explicit_mean": 2.33, "fundnos": [], "grade": "C", "id": "I023", "known_fundnos": [], "known_mgrnos": [9843], "mgrnos": [9843], "name": "Connor Haley", "own_docs": 3, "primary_style": "small_micro_cap", "ran_money": "yes", "record_kind": "13f", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 1.33, "fundnos": [], "grade": "B", "id": "I024", "known_fundnos": [], "known_mgrnos": [26407], "mgrnos": [26407], "name": "Dan Sundheim", "own_docs": 3, "primary_style": "long_short", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 1.0, "fundnos": [], "grade": "B", "id": "I025", "known_fundnos": [], "known_mgrnos": [42315], "mgrnos": [42315], "name": "David Einhorn", "own_docs": 3, "primary_style": "deep_value", "ran_money": "yes", "record_kind": "13f", "region": "europe", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I026", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "David Gardner", "own_docs": 3, "primary_style": "growth", "ran_money": "unclear", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "C", "id": "I027", "known_fundnos": [], "known_mgrnos": [7808], "mgrnos": [7808], "name": "Dmitry Balyasny", "own_docs": 3, "primary_style": "long_short", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [86781], "grade": "F", "id": "I028", "known_fundnos": [86781, 103829], "known_mgrnos": [], "mgrnos": [], "name": "Joseph Shaposhnik", "own_docs": 3, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "fund", "region": "us", "role": "investor", "shares_with": null, "start_ym": 201601}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 1.33, "fundnos": [17878], "grade": "F", "id": "I029", "known_fundnos": [17878, 103745], "known_mgrnos": [44850], "mgrnos": [], "name": "Murray Stahl", "own_docs": 3, "primary_style": "deep_value", "ran_money": "yes", "record_kind": "fund", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 1.67, "fundnos": [], "grade": "N", "id": "I030", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Shawn O'Malley", "own_docs": 3, "primary_style": "quality_compounders", "ran_money": "unclear", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "A", "id": "I031", "known_fundnos": [], "known_mgrnos": [8350], "mgrnos": [8350], "name": "Warren Buffett", "own_docs": 3, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I032", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Alex", "own_docs": 2, "primary_style": "growth", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "C", "id": "I033", "known_fundnos": [98968], "known_mgrnos": [14367], "mgrnos": [14367], "name": "Anthony Scaramucci", "own_docs": 2, "primary_style": "growth", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "allocator", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 0.5, "fundnos": [6867], "grade": "F", "id": "I034", "known_fundnos": [6867], "known_mgrnos": [15095], "mgrnos": [], "name": "Arnold Van Den Berg", "own_docs": 2, "primary_style": "deep_value", "ran_money": "yes", "record_kind": "fund", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 0.5, "fundnos": [], "grade": "N", "id": "I035", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Bill Miller", "own_docs": 2, "primary_style": "none", "ran_money": "unclear", "record_kind": "none", "region": "unclear", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 3.0, "explicit_mean": 2.5, "fundnos": [14612, 14617], "grade": "F", "id": "I036", "known_fundnos": [14612, 14617], "known_mgrnos": [], "mgrnos": [], "name": "Bill Nygren", "own_docs": 2, "primary_style": "deep_value", "ran_money": "yes", "record_kind": "fund", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 3.0, "explicit_mean": 2.5, "fundnos": [], "grade": "N", "id": "I037", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Brian Feroldi", "own_docs": 2, "primary_style": "growth", "ran_money": "unclear", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I038", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Chris Mayer", "own_docs": 2, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I039", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Daniel Mahncke", "own_docs": 2, "primary_style": "quality_compounders", "ran_money": "unclear", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 3.0, "explicit_mean": 1.5, "fundnos": [], "grade": "N", "id": "I040", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "David Fagan", "own_docs": 2, "primary_style": "index_allocation", "ran_money": "unclear", "record_kind": "none", "region": "other", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "C", "id": "I041", "known_fundnos": [], "known_mgrnos": [13265], "mgrnos": [13265], "name": "David Rubenstein", "own_docs": 2, "primary_style": "private_venture", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 3.0, "explicit_mean": 2.5, "fundnos": [6972], "grade": "F", "id": "I042", "known_fundnos": [6972, 58270], "known_mgrnos": [8799], "mgrnos": [], "name": "Derek Pilecki", "own_docs": 2, "primary_style": "long_short", "ran_money": "yes", "record_kind": "fund", "region": "us", "role": "investor", "shares_with": null, "start_ym": 201701}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [88558], "grade": "F", "id": "I043", "known_fundnos": [88558], "known_mgrnos": [], "mgrnos": [], "name": "Eddy Elfenbein", "own_docs": 2, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "fund", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I044", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Ernie Chan", "own_docs": 2, "primary_style": "quant_systematic", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I045", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Gautam Baid", "own_docs": 2, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "none", "region": "emerging", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 0.5, "fundnos": [], "grade": "A", "id": "I046", "known_fundnos": [], "known_mgrnos": [28301], "mgrnos": [28301], "name": "Gavin Baker", "own_docs": 2, "primary_style": "growth", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I047", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "James Ferguson", "own_docs": 2, "primary_style": "none", "ran_money": "unclear", "record_kind": "none", "region": "global", "role": "allocator", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I048", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Jim Mellon", "own_docs": 2, "primary_style": "macro_multi_asset", "ran_money": "unclear", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I049", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "John Huber", "own_docs": 1, "primary_style": "quality_compounders", "ran_money": "unclear", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I050", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "John Spears", "own_docs": 2, "primary_style": "deep_value", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 1.5, "fundnos": [], "grade": "A", "id": "I051", "known_fundnos": [], "known_mgrnos": [14546], "mgrnos": [14546], "name": "Li Lu", "own_docs": 2, "primary_style": "deep_value", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I052", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Marc Rowan", "own_docs": 2, "primary_style": "credit_distressed", "ran_money": "unclear", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [12560], "grade": "F", "id": "I053", "known_fundnos": [12546, 12550, 12560], "known_mgrnos": [], "mgrnos": [], "name": "Matthew McLennan", "own_docs": 2, "primary_style": "deep_value", "ran_money": "yes", "record_kind": "fund", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I054", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Nima Shayegh", "own_docs": 2, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "A", "id": "I055", "known_fundnos": [], "known_mgrnos": [14201], "mgrnos": [14201], "name": "Pat Dorsey", "own_docs": 2, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "A", "id": "I056", "known_fundnos": [], "known_mgrnos": [11450], "mgrnos": [11450], "name": "Philippe Laffont", "own_docs": 2, "primary_style": "growth", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 0.5, "fundnos": [], "grade": "C", "id": "I057", "known_fundnos": [], "known_mgrnos": [11218], "mgrnos": [11218], "name": "Ray Dalio", "own_docs": 2, "primary_style": "macro_multi_asset", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 1.5, "fundnos": [], "grade": "N", "id": "I058", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Robert Hagstrom", "own_docs": 2, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [17996], "grade": "F", "id": "I059", "known_fundnos": [17996], "known_mgrnos": [8520], "mgrnos": [], "name": "Samantha McLemore", "own_docs": 2, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "fund", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 0.5, "fundnos": [], "grade": "C", "id": "I060", "known_fundnos": [], "known_mgrnos": [11912], "mgrnos": [11912], "name": "Sander Gerber", "own_docs": 2, "primary_style": "long_short", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 1.5, "fundnos": [], "grade": "A", "id": "I061", "known_fundnos": [], "known_mgrnos": [8200], "mgrnos": [8200], "name": "Seth Klarman", "own_docs": 2, "primary_style": "deep_value", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "A", "id": "I062", "known_fundnos": [104640], "known_mgrnos": [13408], "mgrnos": [13408], "name": "Terry Smith", "own_docs": 2, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 1.5, "fundnos": [], "grade": "A", "id": "I063", "known_fundnos": [], "known_mgrnos": [39925], "mgrnos": [39925], "name": "Thomas Russo", "own_docs": 2, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I064", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Vinod Khosla", "own_docs": 2, "primary_style": "private_venture", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I065", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Abby Zimmerman", "own_docs": 1, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I066", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Adam Shapiro", "own_docs": 1, "primary_style": "none", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "allocator", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I067", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Adam Wilk", "own_docs": 1, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "C", "id": "I068", "known_fundnos": [], "known_mgrnos": [9956], "mgrnos": [9956], "name": "Alan Patricof", "own_docs": 1, "primary_style": "private_venture", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [14617], "grade": "F", "id": "I069", "known_fundnos": [14617], "known_mgrnos": [], "mgrnos": [], "name": "Alex Fitch", "own_docs": 1, "primary_style": "deep_value", "ran_money": "yes", "record_kind": "fund", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I070", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Alex Morris", "own_docs": 1, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "A", "id": "I071", "known_fundnos": [], "known_mgrnos": [11405], "mgrnos": [11405], "name": "Alex Sacerdote", "own_docs": 1, "primary_style": "growth", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I072", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Alfonso Peccatiello", "own_docs": 1, "primary_style": "macro_multi_asset", "ran_money": "unclear", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I073", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Andrew Ballou", "own_docs": 1, "primary_style": "deep_value", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I074", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Andrew Fox", "own_docs": 1, "primary_style": "growth", "ran_money": "unclear", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I075", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Andrew Martin", "own_docs": 1, "primary_style": "deep_value", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I076", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Andrew Wilkinson", "own_docs": 1, "primary_style": "quality_compounders", "ran_money": "unclear", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I077", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Anthony Bolton", "own_docs": 1, "primary_style": "deep_value", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I078", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Anthony Kingsley", "own_docs": 1, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "C", "id": "I079", "known_fundnos": [], "known_mgrnos": [9698], "mgrnos": [9698], "name": "Antonio Gracias", "own_docs": 1, "primary_style": "growth", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I080", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Arif Karim", "own_docs": 1, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I081", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Asher Edelman", "own_docs": 1, "primary_style": "special_situations", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 3.0, "explicit_mean": 3.0, "fundnos": [], "grade": "N", "id": "I082", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Aswath Damodaran", "own_docs": 1, "primary_style": "deep_value", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I083", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Barry Ritholtz", "own_docs": 1, "primary_style": "none", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "C", "id": "I084", "known_fundnos": [], "known_mgrnos": [54860], "mgrnos": [54860], "name": "Ben Silver", "own_docs": 1, "primary_style": "growth", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I085", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Bill Gebhardt", "own_docs": 1, "primary_style": "quant_systematic", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I086", "known_fundnos": [60469, 102128, 102211], "known_mgrnos": [], "mgrnos": [], "name": "Bill Miller IV", "own_docs": 1, "primary_style": "deep_value", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I087", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Bill Priest", "own_docs": 1, "primary_style": "quant_systematic", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I088", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Bob Mylod", "own_docs": 1, "primary_style": "growth", "ran_money": "unclear", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "A", "id": "I089", "known_fundnos": [], "known_mgrnos": [10247], "mgrnos": [10247], "name": "Bob Robotti", "own_docs": 1, "primary_style": "deep_value", "ran_money": "yes", "record_kind": "13f", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I090", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Brent Johnson", "own_docs": 1, "primary_style": "small_micro_cap", "ran_money": "unclear", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I091", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Brian Gaines", "own_docs": 1, "primary_style": "deep_value", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "A", "id": "I092", "known_fundnos": [10972], "known_mgrnos": [26630], "mgrnos": [26630], "name": "Bruce Berkowitz", "own_docs": 1, "primary_style": "deep_value", "ran_money": "yes", "record_kind": "13f", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "C", "id": "I093", "known_fundnos": [], "known_mgrnos": [14445], "mgrnos": [14445], "name": "Bryan Lawrence", "own_docs": 1, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "13f", "region": "unclear", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I094", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Carson Block", "own_docs": 1, "primary_style": "long_short", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [62312, 62589, 62590], "grade": "F", "id": "I095", "known_fundnos": [62312, 62589, 62590], "known_mgrnos": [14305], "mgrnos": [], "name": "Cathie Wood", "own_docs": 1, "primary_style": "growth", "ran_money": "yes", "record_kind": "fund", "region": "us", "role": "investor", "shares_with": null, "start_ym": 201401}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I096", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Charlie Munger", "own_docs": 1, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I097", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Chris", "own_docs": 1, "primary_style": "long_short", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I098", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Christian Angermayer", "own_docs": 1, "primary_style": "private_venture", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I099", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Christian Billinger", "own_docs": 1, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "none", "region": "europe", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I100", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Clark Tang", "own_docs": 1, "primary_style": "growth", "ran_money": "unclear", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I101", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Clay Fink", "own_docs": 1, "primary_style": "quality_compounders", "ran_money": "unclear", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I102", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Collin Roche", "own_docs": 1, "primary_style": "private_venture", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I103", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Cory Paddock", "own_docs": 1, "primary_style": "sector_specialist", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "C", "id": "I104", "known_fundnos": [], "known_mgrnos": [16135], "mgrnos": [16135], "name": "Cristiano Souza", "own_docs": 1, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": 202403}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "A", "id": "I105", "known_fundnos": [], "known_mgrnos": [83400], "mgrnos": [83400], "name": "Dan Loeb", "own_docs": 1, "primary_style": "special_situations", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I106", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Dan Rasmussen", "own_docs": 1, "primary_style": "small_micro_cap", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": null, "explicit_mean": null, "fundnos": [], "grade": "N", "id": "I107", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Daniel Pronk", "own_docs": 0, "primary_style": "none", "ran_money": "unclear", "record_kind": "none", "region": "unclear", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "C", "id": "I108", "known_fundnos": [], "known_mgrnos": [23000], "mgrnos": [23000], "name": "David Booth", "own_docs": 1, "primary_style": "quant_systematic", "ran_money": "yes", "record_kind": "13f", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "C", "id": "I109", "known_fundnos": [103366], "known_mgrnos": [17392], "mgrnos": [17392], "name": "David Orr", "own_docs": 1, "primary_style": "long_short", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "A", "id": "I110", "known_fundnos": [], "known_mgrnos": [14088, 22705], "mgrnos": [14088, 22705], "name": "David Rosen", "own_docs": 1, "primary_style": "deep_value", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I111", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "David Stein", "own_docs": 1, "primary_style": "macro_multi_asset", "ran_money": "unclear", "record_kind": "none", "region": "global", "role": "allocator", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "A", "id": "I112", "known_fundnos": [], "known_mgrnos": [4423], "mgrnos": [4423], "name": "David Tepper", "own_docs": 1, "primary_style": "none", "ran_money": "yes", "record_kind": "13f", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "C", "id": "I113", "known_fundnos": [], "known_mgrnos": [54860], "mgrnos": [54860], "name": "David Tykoczynski", "own_docs": 1, "primary_style": "growth", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": "I084", "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I114", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Dede Eyesan", "own_docs": 1, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I115", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Dilhan Pillay Sandrasegara", "own_docs": 1, "primary_style": "none", "ran_money": "unclear", "record_kind": "none", "region": "global", "role": "allocator", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I116", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Django Davidson", "own_docs": 1, "primary_style": "deep_value", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I117", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Dwayne Louie", "own_docs": 1, "primary_style": "special_situations", "ran_money": "unclear", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I118", "known_fundnos": [12883, 12951, 101504], "known_mgrnos": [], "mgrnos": [], "name": "Ed Perks", "own_docs": 1, "primary_style": "none", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I119", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Eduardo Marques", "own_docs": 1, "primary_style": "deep_value", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I120", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Edwin Lugo", "own_docs": 1, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I121", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Fabrice Grinda", "own_docs": 1, "primary_style": "private_venture", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 3.0, "explicit_mean": 3.0, "fundnos": [], "grade": "A", "id": "I122", "known_fundnos": [], "known_mgrnos": [23050], "mgrnos": [23050], "name": "Fred Martin", "own_docs": 1, "primary_style": "growth", "ran_money": "yes", "record_kind": "13f", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I123", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Freddie Lait", "own_docs": 1, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I124", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Garrett Finn", "own_docs": 1, "primary_style": "small_micro_cap", "ran_money": "unclear", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I125", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "George Noble", "own_docs": 1, "primary_style": "long_short", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I126", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Gil Scrollback", "own_docs": 1, "primary_style": "none", "ran_money": "unclear", "record_kind": "none", "region": "global", "role": "allocator", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I127", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Glenn Dubin", "own_docs": 1, "primary_style": "long_short", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "allocator", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I128", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Glenn Kacher", "own_docs": 1, "primary_style": "growth", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I129", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Graeme Forster", "own_docs": 1, "primary_style": "deep_value", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I130", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Hamilton Helmer", "own_docs": 1, "primary_style": "quality_compounders", "ran_money": "unclear", "record_kind": "none", "region": "unclear", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I131", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Hari Rama", "own_docs": 1, "primary_style": "quality_compounders", "ran_money": "unclear", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 3.0, "explicit_mean": 3.0, "fundnos": [], "grade": "C", "id": "I132", "known_fundnos": [], "known_mgrnos": [15389], "mgrnos": [15389], "name": "Harris Kupperman", "own_docs": 1, "primary_style": "deep_value", "ran_money": "yes", "record_kind": "13f", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I133", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Helena Morrissey", "own_docs": 1, "primary_style": "macro_multi_asset", "ran_money": "yes", "record_kind": "none", "region": "europe", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "A", "id": "I134", "known_fundnos": [], "known_mgrnos": [9442], "mgrnos": [9442], "name": "Henry Ellenbogen", "own_docs": 1, "primary_style": "growth", "ran_money": "yes", "record_kind": "13f", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I135", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Host of We Study Billionaires", "own_docs": 1, "primary_style": "quality_compounders", "ran_money": "unclear", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I136", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Howard Lindzon", "own_docs": 1, "primary_style": "private_venture", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": null, "explicit_mean": null, "fundnos": [], "grade": "N", "id": "I137", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Jack Raines", "own_docs": 0, "primary_style": "none", "ran_money": "unclear", "record_kind": "none", "region": "unclear", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I138", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "James Anderson", "own_docs": 1, "primary_style": "growth", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I139", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "James Zimmerman", "own_docs": 1, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I140", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Jamin Ball", "own_docs": 1, "primary_style": "private_venture", "ran_money": "unclear", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "C", "id": "I141", "known_fundnos": [], "known_mgrnos": [17446], "mgrnos": [17446], "name": "Jared Kushner", "own_docs": 1, "primary_style": "private_venture", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 3.0, "explicit_mean": 3.0, "fundnos": [], "grade": "N", "id": "I142", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Jason Donville", "own_docs": 1, "primary_style": "growth", "ran_money": "yes", "record_kind": "none", "region": "other", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "C", "id": "I143", "known_fundnos": [], "known_mgrnos": [13787], "mgrnos": [13787], "name": "Jason Karp", "own_docs": 1, "primary_style": "none", "ran_money": "yes", "record_kind": "13f", "region": "unclear", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I144", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Jay Bowen", "own_docs": 1, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "C", "id": "I145", "known_fundnos": [], "known_mgrnos": [11615], "mgrnos": [11615], "name": "Jeff Horing", "own_docs": 1, "primary_style": "private_venture", "ran_money": "yes", "record_kind": "13f", "region": "unclear", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I146", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Jeff Yass", "own_docs": 1, "primary_style": "quant_systematic", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I147", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Jens", "own_docs": 1, "primary_style": "none", "ran_money": "unclear", "record_kind": "none", "region": "global", "role": "allocator", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 3.0, "explicit_mean": 3.0, "fundnos": [], "grade": "N", "id": "I148", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Jesse Gamble", "own_docs": 1, "primary_style": "growth", "ran_money": "yes", "record_kind": "none", "region": "other", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "B", "id": "I149", "known_fundnos": [], "known_mgrnos": [12867], "mgrnos": [12867], "name": "Jim Chanos", "own_docs": 1, "primary_style": "long_short", "ran_money": "yes", "record_kind": "13f", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I150", "known_fundnos": [90773], "known_mgrnos": [], "mgrnos": [], "name": "Joel Tillinghast", "own_docs": 1, "primary_style": "deep_value", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "A", "id": "I151", "known_fundnos": [], "known_mgrnos": [24580], "mgrnos": [24580], "name": "John Armitage", "own_docs": 1, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I152", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "John Graham", "own_docs": 1, "primary_style": "macro_multi_asset", "ran_money": "unclear", "record_kind": "none", "region": "global", "role": "allocator", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I153", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "John Jennings", "own_docs": 1, "primary_style": "index_allocation", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "allocator", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "A", "id": "I154", "known_fundnos": [], "known_mgrnos": [9090], "mgrnos": [9090], "name": "John Lennon", "own_docs": 1, "primary_style": "deep_value", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I155", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Jon Cukierwar", "own_docs": 1, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I156", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Jon Gray", "own_docs": 1, "primary_style": "private_venture", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I157", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Jonathan Boyar", "own_docs": 1, "primary_style": "small_micro_cap", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I158", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Josh Resnick", "own_docs": 1, "primary_style": "long_short", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I159", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Josh Wolfe", "own_docs": 1, "primary_style": "private_venture", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I160", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Josh Young", "own_docs": 1, "primary_style": "small_micro_cap", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I161", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Jurrien Timmer", "own_docs": 1, "primary_style": "macro_multi_asset", "ran_money": "unclear", "record_kind": "none", "region": "global", "role": "allocator", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I162", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Keith Rabois", "own_docs": 1, "primary_style": "private_venture", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "A", "id": "I163", "known_fundnos": [], "known_mgrnos": [53255], "mgrnos": [53255], "name": "Kelly Granat", "own_docs": 1, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "C", "id": "I164", "known_fundnos": [], "known_mgrnos": [38240], "mgrnos": [38240], "name": "Ken Fisher", "own_docs": 1, "primary_style": "macro_multi_asset", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "C", "id": "I165", "known_fundnos": [], "known_mgrnos": [16210], "mgrnos": [16210], "name": "Ken Griffin", "own_docs": 1, "primary_style": "long_short", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I166", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Kevin Hartz", "own_docs": 1, "primary_style": "private_venture", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I167", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Kris Sidial", "own_docs": 1, "primary_style": "none", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I168", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Kristof Gleich", "own_docs": 1, "primary_style": "macro_multi_asset", "ran_money": "unclear", "record_kind": "none", "region": "us", "role": "allocator", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I169", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Larry Connor", "own_docs": 1, "primary_style": "none", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I170", "known_fundnos": [91261, 91263], "known_mgrnos": [], "mgrnos": [], "name": "Laura Geritz", "own_docs": 1, "primary_style": "deep_value", "ran_money": "yes", "record_kind": "none", "region": "emerging", "role": "investor", "shares_with": null, "start_ym": 201701}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "C", "id": "I171", "known_fundnos": [], "known_mgrnos": [14968], "mgrnos": [14968], "name": "Lauren Templeton", "own_docs": 1, "primary_style": "deep_value", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I172", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Leah", "own_docs": 1, "primary_style": "growth", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I173", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Leon", "own_docs": 1, "primary_style": "growth", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "A", "id": "I174", "known_fundnos": [], "known_mgrnos": [21430], "mgrnos": [21430], "name": "Leon Cooperman", "own_docs": 1, "primary_style": "none", "ran_money": "yes", "record_kind": "13f", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I175", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Leon Shaulov", "own_docs": 1, "primary_style": "long_short", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "C", "id": "I176", "known_fundnos": [], "known_mgrnos": [15774], "mgrnos": [15774], "name": "Mala Gaonkar", "own_docs": 1, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I177", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Marcus Wallenberg", "own_docs": 1, "primary_style": "quality_compounders", "ran_money": "unclear", "record_kind": "none", "region": "europe", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I178", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Maria Vassalou", "own_docs": 1, "primary_style": "macro_multi_asset", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I179", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Matt Cherwin", "own_docs": 1, "primary_style": "macro_multi_asset", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "A", "id": "I180", "known_fundnos": [], "known_mgrnos": [10779], "mgrnos": [10779], "name": "Matt Mark", "own_docs": 1, "primary_style": "special_situations", "ran_money": "yes", "record_kind": "13f", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I181", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Michael Anders", "own_docs": 1, "primary_style": "none", "ran_money": "unclear", "record_kind": "none", "region": "unclear", "role": "allocator", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I182", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Michael Buckley", "own_docs": 1, "primary_style": "growth", "ran_money": "unclear", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I183", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Michael Chu", "own_docs": 1, "primary_style": "private_venture", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I184", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Michael Moritz", "own_docs": 1, "primary_style": "private_venture", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "C", "id": "I185", "known_fundnos": [], "known_mgrnos": [8401], "mgrnos": [8401], "name": "Michael Rees", "own_docs": 1, "primary_style": "private_venture", "ran_money": "yes", "record_kind": "13f", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I186", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Mike Paulus", "own_docs": 1, "primary_style": "index_allocation", "ran_money": "unclear", "record_kind": "none", "region": "us", "role": "allocator", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I187", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Muhammad Andreala", "own_docs": 1, "primary_style": "growth", "ran_money": "unclear", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I188", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Nate Chesley", "own_docs": 1, "primary_style": "none", "ran_money": "unclear", "record_kind": "none", "region": "global", "role": "allocator", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I189", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Nick Shallik", "own_docs": 1, "primary_style": "growth", "ran_money": "unclear", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I190", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Nick Sleep", "own_docs": 1, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I191", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Nishant Gargnani", "own_docs": 1, "primary_style": "special_situations", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I192", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Noah Yechiely", "own_docs": 1, "primary_style": "macro_multi_asset", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I193", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Omar Aguilar", "own_docs": 1, "primary_style": "index_allocation", "ran_money": "unclear", "record_kind": "none", "region": "us", "role": "allocator", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "C", "id": "I194", "known_fundnos": [], "known_mgrnos": [9474], "mgrnos": [9474], "name": "Orlando Bravo", "own_docs": 1, "primary_style": "private_venture", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 3.0, "explicit_mean": 3.0, "fundnos": [], "grade": "N", "id": "I195", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Paul Andreola", "own_docs": 1, "primary_style": "small_micro_cap", "ran_money": "yes", "record_kind": "none", "region": "other", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "C", "id": "I196", "known_fundnos": [], "known_mgrnos": [93315], "mgrnos": [93315], "name": "Paul Black", "own_docs": 1, "primary_style": "growth", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I197", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Paul Enright", "own_docs": 1, "primary_style": "long_short", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "C", "id": "I198", "known_fundnos": [], "known_mgrnos": [85625], "mgrnos": [85625], "name": "Paul Tudor Jones", "own_docs": 1, "primary_style": "macro_multi_asset", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "C", "id": "I199", "known_fundnos": [], "known_mgrnos": [10643], "mgrnos": [10643], "name": "Paul Marshall", "own_docs": 1, "primary_style": "long_short", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "A", "id": "I200", "known_fundnos": [], "known_mgrnos": [78988], "mgrnos": [78988], "name": "Paul Singer", "own_docs": 1, "primary_style": "special_situations", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I201", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Paul Zummo", "own_docs": 1, "primary_style": "long_short", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "allocator", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "C", "id": "I202", "known_fundnos": [], "known_mgrnos": [13574], "mgrnos": [13574], "name": "Pete Muller", "own_docs": 1, "primary_style": "quant_systematic", "ran_money": "yes", "record_kind": "13f", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "A", "id": "I203", "known_fundnos": [], "known_mgrnos": [5300], "mgrnos": [5300], "name": "Peter Keefe", "own_docs": 1, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "13f", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I204", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Peter Thiel", "own_docs": 1, "primary_style": "private_venture", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I205", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Pierre-Olivier Langevin", "own_docs": 1, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "A", "id": "I206", "known_fundnos": [], "known_mgrnos": [11659], "mgrnos": [11659], "name": "Prem Watsa", "own_docs": 1, "primary_style": "deep_value", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I207", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Preston Pysh", "own_docs": 1, "primary_style": "macro_multi_asset", "ran_money": "unclear", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I208", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Reid Hoffman", "own_docs": 1, "primary_style": "growth", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I209", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Richard Lawrence", "own_docs": 1, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "none", "region": "asia", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I210", "known_fundnos": [6418, 37118], "known_mgrnos": [], "mgrnos": [], "name": "Rick Rieder", "own_docs": 1, "primary_style": "none", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "B", "id": "I211", "known_fundnos": [], "known_mgrnos": [25190], "mgrnos": [25190], "name": "Ricky Sandler", "own_docs": 1, "primary_style": "long_short", "ran_money": "yes", "record_kind": "13f", "region": "unclear", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 3.0, "explicit_mean": 3.0, "fundnos": [], "grade": "N", "id": "I212", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Rob Goldstein", "own_docs": 1, "primary_style": "deep_value", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I213", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Robert Carver", "own_docs": 1, "primary_style": "macro_multi_asset", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "C", "id": "I214", "known_fundnos": [], "known_mgrnos": [11535], "mgrnos": [11535], "name": "Robert Wallace", "own_docs": 1, "primary_style": "private_venture", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "allocator", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I215", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Roger Fan", "own_docs": 1, "primary_style": "special_situations", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I216", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Ryan Tolkin", "own_docs": 1, "primary_style": "long_short", "ran_money": "unclear", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I217", "known_fundnos": [3618], "known_mgrnos": [], "mgrnos": [], "name": "Scott Barbee", "own_docs": 1, "primary_style": "deep_value", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "C", "id": "I218", "known_fundnos": [], "known_mgrnos": [14968], "mgrnos": [14968], "name": "Scott Phillips", "own_docs": 1, "primary_style": "deep_value", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": "I171", "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I219", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Shirley", "own_docs": 1, "primary_style": "none", "ran_money": "unclear", "record_kind": "none", "region": "global", "role": "allocator", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I220", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Shree Viswanathan", "own_docs": 1, "primary_style": "quality_compounders", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I221", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Sinan Xin", "own_docs": 1, "primary_style": "long_short", "ran_money": "yes", "record_kind": "none", "region": "emerging", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "A", "id": "I222", "known_fundnos": [], "known_mgrnos": [7272], "mgrnos": [7272], "name": "Soo Chuen Tan", "own_docs": 1, "primary_style": "deep_value", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "C", "id": "I223", "known_fundnos": [], "known_mgrnos": [13021], "mgrnos": [13021], "name": "Stan Druckenmiller", "own_docs": 1, "primary_style": "macro_multi_asset", "ran_money": "yes", "record_kind": "13f", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I224", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Stephanie Link", "own_docs": 1, "primary_style": "growth", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "C", "id": "I225", "known_fundnos": [], "known_mgrnos": [75106], "mgrnos": [75106], "name": "Steve Cohen", "own_docs": 1, "primary_style": "long_short", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I226", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Steve Eisman", "own_docs": 1, "primary_style": "long_short", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I227", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Steven Bregman", "own_docs": 1, "primary_style": "deep_value", "ran_money": "unclear", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I228", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Thomas Kaplan", "own_docs": 1, "primary_style": "sector_specialist", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "A", "id": "I229", "known_fundnos": [], "known_mgrnos": [11450], "mgrnos": [11450], "name": "Thomas Laffont", "own_docs": 1, "primary_style": "growth", "ran_money": "yes", "record_kind": "13f", "region": "global", "role": "investor", "shares_with": "I056", "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I230", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Thomas Mueller-Borja", "own_docs": 1, "primary_style": "none", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I231", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Tim Draper", "own_docs": 1, "primary_style": "private_venture", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I232", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Tom", "own_docs": 1, "primary_style": "long_short", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I233", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Tom Morgan", "own_docs": 1, "primary_style": "growth", "ran_money": "unclear", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "C", "id": "I234", "known_fundnos": [], "known_mgrnos": [13391], "mgrnos": [13391], "name": "Tully Friedman", "own_docs": 1, "primary_style": "private_venture", "ran_money": "yes", "record_kind": "13f", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I235", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Unnamed fund-of-managers allocator", "own_docs": 1, "primary_style": "none", "ran_money": "unclear", "record_kind": "none", "region": "global", "role": "allocator", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I236", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Unnamed head of Liberty Mutual Investments", "own_docs": 1, "primary_style": "private_venture", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "allocator", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 2.0, "explicit_mean": 2.0, "fundnos": [], "grade": "N", "id": "I237", "known_fundnos": [103438], "known_mgrnos": [], "mgrnos": [], "name": "Victor Haghani", "own_docs": 1, "primary_style": "quant_systematic", "ran_money": "yes", "record_kind": "none", "region": "global", "role": "investor", "shares_with": null, "start_ym": 202501}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "C", "id": "I238", "known_fundnos": [], "known_mgrnos": [12188], "mgrnos": [12188], "name": "Vitaliy Katsenelson", "own_docs": 1, "primary_style": "none", "ran_money": "yes", "record_kind": "13f", "region": "unclear", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 1.0, "explicit_mean": 1.0, "fundnos": [], "grade": "N", "id": "I239", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Wilson Cheung", "own_docs": 1, "primary_style": "sector_specialist", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I240", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Ying", "own_docs": 1, "primary_style": "long_short", "ran_money": "yes", "record_kind": "none", "region": "unclear", "role": "investor", "shares_with": null, "start_ym": null}, {"end_ym": null, "explicit_max": 0.0, "explicit_mean": 0.0, "fundnos": [], "grade": "N", "id": "I241", "known_fundnos": [], "known_mgrnos": [], "mgrnos": [], "name": "Zach", "own_docs": 1, "primary_style": "long_short", "ran_money": "yes", "record_kind": "none", "region": "us", "role": "investor", "shares_with": null, "start_ym": null}]""")
DOCS = json.loads(r"""[[1, 2, 2, 12253], [2, 2, 3, 17689], [3, 2, 1, 15032], [4, 0, 0, 7077], [5, 0, 0, 9179], [6, 2, 1, 14625], [7, 2, 3, 8019], [8, 2, 2, 16051], [9, 2, 2, 11324], [10, 2, 3, 21200], [11, 0, 0, 2644], [12, 1, 0, 7590], [13, 2, 1, 11327], [14, 0, 0, 11403], [15, 2, 2, 11326], [16, 2, 2, 20998], [17, 1, 0, 10931], [18, 2, 2, 23626], [19, 2, 3, 23129], [20, 2, 3, 10352], [21, 2, 1, 13239], [22, 0, 0, 2041], [23, 2, 4, 18900], [24, 2, 2, 20322], [25, 3, 2, 22598], [26, 2, 2, 9442], [27, 0, 0, 11150], [28, 0, 0, 18294], [29, 1, 0, 13596], [30, 0, 0, 6802], [31, 0, 0, 9765], [32, 0, 0, 8398], [33, 0, 0, 13004], [34, 2, 2, 11209], [35, 0, 0, 7173], [36, 3, 3, 8471], [37, 0, 0, 14209], [38, 1, 0, 7454], [39, 2, 3, 10045], [40, 0, 0, 6653], [41, 0, 0, 5792], [42, 2, 2, 7686], [43, 2, 3, 5976], [44, 0, 0, 15079], [45, 0, 0, 10243], [46, 0, 0, 21186], [47, 2, 3, 9662], [48, 2, 2, 13937], [49, 0, 0, 3002], [50, 1, 1, 15524], [51, 0, 0, 12439], [52, 2, 1, 16746], [53, 1, 0, 8953], [54, 3, 5, 12088], [55, 2, 2, 16981], [56, 2, 2, 14477], [57, 1, 1, 12219], [58, 1, 0, 17396], [59, 1, 0, 16439], [60, 2, 1, 14405], [61, 2, 3, 14024], [62, 1, 0, 4125], [63, 0, 0, 8181], [64, 2, 2, 11287], [65, 2, 3, 10364], [66, 2, 2, 11961], [67, 1, 0, 15746], [68, 0, 0, 9740], [69, 1, 0, 16053], [70, 0, 0, 1645], [71, 1, 0, 9160], [72, 2, 3, 28975], [73, 2, 3, 10290], [74, 2, 4, 13178], [75, 0, 0, 7233], [76, 0, 0, 7559], [77, 1, 0, 24840], [78, 1, 0, 18517], [79, 2, 1, 9744], [80, 0, 0, 12655], [81, 0, 0, 11742], [82, 1, 0, 11141], [83, 0, 0, 11856], [84, 0, 0, 7709], [85, 0, 0, 9837], [86, 1, 0, 11277], [87, 0, 0, 4406], [88, 0, 0, 11455], [89, 2, 3, 13076], [90, 2, 2, 16961], [91, 2, 3, 15294], [92, 2, 3, 10423], [93, 2, 1, 17393], [94, 2, 3, 13315], [95, 2, 2, 19376], [96, 1, 0, 12355], [97, 1, 0, 15885], [98, 2, 4, 17627], [99, 0, 0, 8930], [100, 0, 0, 13225], [101, 2, 2, 9403], [102, 2, 1, 3550], [103, 0, 0, 8675], [104, 0, 0, 5770], [105, 2, 3, 12760], [106, 2, 2, 6475], [107, 0, 0, 10892], [108, 2, 2, 15933], [109, 0, 0, 7802], [110, 0, 0, 7198], [111, 0, 0, 20559], [112, 0, 0, 10423], [113, 0, 0, 11512], [114, 1, 0, 10126], [115, 0, 0, 13747], [116, 0, 0, 11846], [117, 0, 0, 13940], [118, 0, 0, 10206], [119, 0, 0, 11960], [120, 0, 0, 10984], [121, 0, 0, 11465], [122, 2, 1, 15047], [123, 1, 0, 11956], [124, 1, 0, 13841], [125, 0, 0, 12313], [126, 1, 0, 10873], [127, 0, 0, 6402], [128, 1, 0, 6804], [129, 1, 0, 5342], [130, 1, 0, 9207], [131, 2, 2, 6147], [132, 0, 0, 5847], [133, 0, 0, 4914], [134, 0, 0, 7816], [135, 1, 0, 5884], [136, 1, 0, 7621], [137, 0, 0, 6385], [138, 2, 2, 11184], [139, 1, 0, 7430], [140, 3, 4, 7404], [141, 0, 0, 8946], [142, 1, 0, 4499], [143, 1, 1, 6526], [144, 1, 0, 8442], [145, 1, 0, 9164], [146, 0, 0, 7429], [147, 0, 0, 5958], [148, 0, 0, 9877], [149, 1, 0, 4855], [150, 1, 0, 4479], [151, 1, 0, 4706], [152, 2, 2, 9308], [153, 1, 0, 8195], [154, 1, 0, 7912], [155, 0, 0, 8212], [156, 1, 1, 7551], [157, 1, 0, 7236], [158, 2, 2, 10038], [159, 1, 0, 8638], [160, 2, 2, 7345], [161, 1, 1, 8830], [162, 0, 0, 10173], [163, 1, 1, 12777], [164, 1, 0, 4536], [165, 1, 0, 5737], [166, 2, 2, 9393], [167, 0, 0, 7185], [168, 1, 1, 16223], [169, 2, 2, 13532], [170, 1, 1, 13405], [171, 1, 0, 9673], [172, 2, 1, 9046], [173, 2, 1, 11871], [174, 2, 1, 7914], [175, 1, 0, 8662], [176, 1, 0, 13333], [177, 1, 0, 12573], [178, 2, 2, 11212], [179, 2, 4, 16159], [180, 3, 4, 14372], [181, 2, 3, 19124], [182, 1, 2, 9482], [183, 3, 1, 9168], [184, 3, 5, 11878], [185, 2, 1, 10953], [186, 1, 0, 6283], [187, 0, 0, 9656], [188, 2, 1, 13369], [189, 2, 3, 5199], [190, 1, 0, 12774], [191, 0, 0, 9747], [192, 3, 1, 9942], [193, 1, 0, 11977], [194, 2, 2, 31316], [195, 0, 0, 1623], [196, 0, 0, 2009], [197, 1, 1, 1456], [198, 0, 0, 10387], [199, 0, 0, 27620], [200, 1, 0, 10423], [201, 3, 1, 9269], [202, 2, 3, 11211], [203, 2, 2, 17286], [204, 0, 0, 10331], [205, 2, 2, 12374], [206, 1, 0, 14339], [207, 1, 1, 12693], [208, 1, 0, 915], [209, 0, 0, 7633], [210, 1, 0, 12774], [211, 2, 1, 12602], [212, 1, 0, 11174], [213, 2, 2, 12848], [214, 2, 1, 9316], [215, 1, 2, 12155], [216, 2, 5, 13527], [217, 3, 3, 12801], [218, 2, 1, 14267], [219, 0, 0, 13522], [220, 1, 0, 15220], [221, 2, 1, 15186], [222, 2, 1, 7870], [223, 2, 2, 15138], [224, 3, 3, 13672], [225, 1, 1, 8080], [226, 1, 0, 8406], [227, 1, 0, 12233], [228, 2, 2, 13482], [229, 2, 1, 9290], [230, 2, 1, 22711], [231, 2, 2, 32416], [232, 2, 3, 14667], [233, 1, 0, 14349], [234, 1, 0, 9925], [235, 1, 1, 13715], [236, 2, 3, 13204], [237, 3, 3, 12002], [238, 2, 3, 20653], [239, 2, 2, 18172], [240, 0, 0, 20276], [241, 2, 2, 8495], [242, 3, 4, 11457], [243, 2, 2, 14978], [244, 0, 0, 23593], [245, 2, 2, 9187], [246, 2, 1, 10863], [247, 2, 1, 7888], [248, 0, 0, 9613], [249, 3, 4, 8463], [250, 3, 3, 12156], [251, 0, 0, 7513], [252, 2, 2, 11501], [253, 0, 0, 15027], [254, 2, 2, 15029], [255, 2, 2, 24412], [256, 0, 0, 16353], [257, 3, 2, 15198], [258, 2, 1, 4508], [259, 2, 1, 6466], [260, 1, 0, 6694], [261, 2, 3, 18716], [262, 0, 0, 9154], [263, 2, 2, 9310], [264, 0, 0, 11735], [265, 3, 1, 7285], [266, 2, 1, 10030], [267, 2, 2, 6008], [268, 2, 2, 12694], [269, 1, 0, 16201], [270, 2, 1, 10953], [271, 2, 1, 9070], [272, 2, 1, 1483], [273, 2, 2, 11015], [274, 1, 0, 29519], [275, 1, 0, 4293], [276, 2, 2, 11620], [277, 1, 0, 10822], [278, 3, 2, 9359], [279, 2, 1, 5912], [280, 2, 3, 19827], [281, 2, 2, 14470], [282, 3, 4, 12147], [283, 2, 2, 10826], [284, 2, 4, 23126], [285, 1, 0, 13195], [286, 1, 0, 3416], [287, 2, 1, 13742], [288, 2, 3, 9555], [289, 1, 0, 11204], [290, 2, 2, 10978], [291, 2, 2, 10981], [292, 2, 1, 12033], [293, 2, 3, 11198], [294, 2, 3, 20389], [295, 2, 1, 18443], [296, 2, 2, 15688], [297, 0, 0, 9083], [298, 0, 0, 13259], [299, 1, 0, 37368], [300, 0, 0, 8981], [301, 1, 0, 4910], [302, 0, 0, 8694], [303, 1, 1, 8031], [304, 0, 0, 1902], [305, 0, 0, 6138], [306, 2, 3, 8268], [307, 3, 4, 12928], [308, 3, 4, 23242], [309, 3, 2, 24657], [310, 3, 3, 27866], [311, 3, 3, 18568], [312, 0, 0, 7818], [313, 2, 4, 8915], [314, 0, 0, 6219], [315, 2, 1, 7307], [316, 3, 3, 11763], [317, 0, 0, 8776], [318, 1, 0, 9063], [319, 1, 0, 3229], [320, 1, 0, 14539], [321, 2, 2, 18308], [322, 1, 0, 7285], [323, 2, 1, 11751], [324, 1, 0, 7425], [325, 0, 0, 7229], [326, 0, 0, 7313], [327, 2, 1, 10689], [328, 1, 0, 12427], [329, 1, 1, 12127], [330, 1, 0, 11463], [331, 2, 2, 12495], [332, 1, 0, 8975], [333, 3, 3, 15904], [334, 1, 1, 14918], [335, 0, 0, 13710], [336, 1, 0, 4976], [337, 0, 0, 13580], [338, 0, 0, 14283], [339, 0, 0, 14416], [340, 0, 0, 8004], [341, 3, 2, 14246], [342, 2, 2, 8792], [343, 0, 0, 8702], [344, 1, 1, 9547], [345, 0, 0, 6436], [346, 2, 2, 5077], [347, 1, 0, 14299], [348, 1, 0, 15173], [349, 3, 3, 10986], [350, 2, 2, 10735], [351, 3, 2, 10292], [352, 2, 2, 16305], [353, 2, 2, 23425], [354, 2, 2, 14449], [355, 2, 2, 19864], [356, 2, 2, 16043], [357, 2, 1, 15508], [358, 2, 2, 15310], [359, 2, 2, 17354], [360, 2, 1, 15045], [361, 2, 3, 10264], [362, 2, 2, 21820], [363, 2, 2, 13156], [364, 1, 0, 4290], [365, 0, 0, 13293], [366, 2, 1, 18399], [367, 2, 2, 22606], [368, 3, 2, 13164], [369, 1, 0, 7633], [370, 1, 1, 14027], [371, 2, 1, 9695], [372, 2, 1, 11760], [373, 0, 0, 5814], [374, 0, 0, 7381], [375, 0, 0, 13275], [376, 0, 0, 8419], [377, 0, 0, 5333], [378, 1, 0, 6046], [379, 2, 1, 11754], [380, 2, 2, 10369], [381, 1, 0, 11119], [382, 3, 2, 11079], [383, 2, 2, 13380], [384, 1, 1, 8243], [385, 1, 1, 14949], [386, 2, 2, 12954], [387, 2, 2, 10211], [388, 2, 1, 11569], [389, 2, 3, 11184], [390, 0, 0, 10208], [391, 3, 3, 13147], [392, 0, 0, 24911], [393, 0, 0, 14874], [394, 0, 0, 18410], [395, 2, 1, 10764], [396, 2, 2, 14791], [397, 2, 2, 17477], [398, 2, 2, 10609], [399, 2, 2, 8055], [400, 0, 0, 6433], [401, 1, 0, 15922], [402, 0, 0, 23215], [403, 3, 3, 13064], [404, 2, 2, 12058], [405, 2, 1, 8376], [406, 0, 0, 12025], [407, 2, 2, 10099], [408, 3, 5, 14394], [409, 3, 3, 4005], [410, 2, 1, 10593], [411, 3, 5, 13653], [412, 0, 0, 7469], [413, 2, 3, 9491], [414, 1, 0, 9260], [415, 3, 2, 13061], [416, 2, 2, 18199], [417, 1, 1, 7090], [418, 2, 3, 10048], [419, 2, 1, 24757], [420, 0, 0, 8726], [421, 2, 2, 16900], [422, 1, 0, 1731], [423, 2, 2, 13255], [424, 2, 2, 12241], [425, 0, 0, 11342], [426, 3, 2, 10351], [427, 0, 0, 11878], [428, 1, 0, 7434], [429, 2, 1, 16517], [430, 2, 1, 8030], [431, 1, 0, 17568], [432, 0, 0, 7179], [433, 2, 4, 14689], [434, 0, 0, 1855], [435, 1, 0, 10386], [436, 0, 0, 8999], [437, 2, 3, 14312], [438, 0, 0, 23550], [439, 0, 0, 28717], [440, 0, 0, 23637], [441, 0, 0, 21026], [442, 0, 0, 25411], [443, 2, 1, 19143], [444, 0, 0, 16341], [445, 0, 0, 23148], [446, 1, 0, 25255], [447, 0, 0, 25741], [448, 3, 3, 11426], [449, 1, 0, 10457], [450, 2, 1, 8744], [451, 0, 0, 8757], [452, 2, 2, 14669], [453, 1, 0, 7046], [454, 0, 0, 8181], [455, 2, 2, 11930], [456, 2, 2, 8470], [457, 0, 0, 14619], [458, 0, 0, 6767], [459, 3, 1, 13975], [460, 1, 0, 11584], [461, 2, 3, 16944], [462, 0, 0, 9705], [463, 0, 0, 2009], [464, 2, 2, 4842], [465, 1, 0, 9881], [466, 2, 4, 10765], [467, 0, 0, 10909], [468, 2, 2, 11836], [469, 1, 0, 15365], [470, 0, 0, 5638], [471, 2, 2, 7206], [472, 1, 0, 3044], [473, 0, 0, 9185], [474, 0, 0, 13007], [475, 1, 0, 16315], [476, 2, 2, 17082], [477, 2, 2, 19045], [478, 2, 1, 17770], [479, 1, 0, 11242], [480, 3, 2, 13211], [481, 2, 1, 10052], [482, 2, 2, 8907], [483, 2, 2, 9781], [484, 1, 1, 12471], [485, 1, 0, 25075], [486, 0, 0, 6251], [487, 0, 0, 17558], [488, 2, 1, 6765], [489, 2, 1, 3870], [490, 1, 0, 11647], [491, 0, 0, 15037], [492, 2, 3, 15554], [493, 3, 4, 14239], [494, 3, 2, 12004], [495, 0, 0, 20769], [496, 2, 3, 10156], [497, 2, 1, 15600], [498, 0, 0, 2756], [499, 2, 2, 9081], [500, 2, 1, 13001], [501, 2, 2, 12357], [502, 3, 4, 12188], [503, 3, 4, 8686], [504, 2, 1, 9019], [505, 3, 1, 8988], [506, 2, 2, 11327], [507, 2, 3, 10627], [508, 2, 2, 22887], [509, 2, 2, 8413], [510, 2, 2, 16316], [511, 2, 2, 14708], [512, 2, 3, 6744], [513, 0, 0, 10568], [514, 0, 0, 12998], [515, 1, 0, 9027], [516, 0, 0, 9541], [517, 2, 1, 9131], [518, 2, 1, 24965], [519, 2, 2, 13367], [520, 2, 2, 21307], [521, 2, 3, 11757], [522, 3, 4, 15916], [523, 2, 1, 16024], [524, 2, 1, 11757], [525, 0, 0, 17874], [526, 0, 0, 19177], [527, 1, 1, 28635], [528, 0, 0, 7499], [529, 2, 2, 11830], [530, 0, 0, 15052], [531, 2, 1, 19202], [532, 2, 3, 19084], [533, 0, 0, 21983], [534, 3, 3, 22234], [535, 2, 3, 13603], [536, 2, 2, 11904], [537, 0, 0, 23371], [538, 2, 1, 9560], [539, 1, 0, 11062], [540, 2, 2, 10406], [541, 1, 0, 11266], [542, 1, 0, 15343], [543, 2, 2, 13226], [544, 1, 0, 15408], [545, 1, 0, 10688], [546, 2, 3, 10655], [547, 2, 3, 28259], [548, 0, 0, 21099], [549, 3, 3, 19726], [550, 0, 0, 10340], [551, 2, 1, 12082], [552, 2, 1, 10247], [553, 2, 2, 10101], [554, 2, 3, 15657], [555, 2, 3, 11663], [556, 0, 0, 7561], [557, 0, 0, 12810], [558, 1, 0, 12331], [559, 2, 2, 11723], [560, 1, 0, 3903], [561, 1, 0, 12656], [562, 2, 3, 9484], [563, 1, 1, 15962], [564, 2, 3, 9298], [565, 2, 2, 11326], [566, 2, 1, 17173], [567, 0, 0, 1895], [568, 1, 0, 8947], [569, 2, 3, 9088], [570, 2, 2, 9519], [571, 3, 4, 10877], [572, 3, 1, 10840], [573, 3, 4, 14154], [574, 2, 2, 10252], [575, 1, 0, 13084], [576, 1, 1, 11829], [577, 3, 1, 8539], [578, 2, 2, 3725], [579, 2, 2, 13318], [580, 2, 2, 11785], [581, 2, 4, 14546], [582, 2, 1, 3885], [583, 1, 0, 6150], [584, 2, 1, 8224], [585, 0, 0, 10400], [586, 2, 3, 10488], [587, 3, 2, 10008], [588, 3, 3, 11279], [589, 0, 0, 12246], [590, 2, 1, 9994], [591, 2, 3, 14756], [592, 1, 0, 12198], [593, 2, 2, 24712], [594, 3, 2, 16005], [595, 0, 0, 15248], [596, 1, 1, 23060], [597, 1, 0, 12591], [598, 1, 0, 12938], [599, 0, 0, 12397], [600, 0, 0, 11336], [601, 2, 2, 20102], [602, 3, 4, 4860], [603, 1, 0, 12582], [604, 1, 1, 5579], [605, 1, 2, 5715], [606, 1, 0, 12297], [607, 1, 0, 12717], [608, 2, 3, 10064], [609, 1, 0, 10184], [610, 1, 1, 11676], [611, 3, 1, 11584], [612, 2, 2, 18434], [613, 0, 0, 11228], [614, 2, 3, 13664], [615, 2, 3, 18017], [616, 2, 2, 29073], [617, 1, 1, 16509], [618, 2, 2, 11898], [619, 1, 0, 12153], [620, 3, 2, 13654], [621, 3, 2, 11555], [622, 1, 0, 10203], [623, 0, 0, 8553], [624, 0, 0, 8691], [625, 0, 0, 9433], [626, 0, 0, 6631], [687, 0, 0, 9696], [688, 2, 1, 5924], [689, 0, 0, 10056], [690, 2, 2, 8576], [691, 0, 0, 6188], [692, 2, 1, 5260], [693, 0, 0, 6909], [694, 2, 2, 9848], [695, 2, 2, 15169]]""")
# <<< FROZEN INPUT <<<

# ------------------------------------------------------------------------------------------- registered settings
H_FROM, H_TO = "2010-06-30", "2025-12-31"          # quarter-ends of 13F holdings read
CRSP_FROM = 200906                                   # first CRSP month (momentum of the June 2010 peer groups)
M_FIRST, M_LAST = 201101, 202512                     # record months computed (seal end 2025-12)
WINDOWS = [("2011-15", 201101, 201512), ("2016-20", 201601, 202012), ("2021-25", 202101, 202512),
           ("2011-25", 201101, 202512)]
BLOCKS = ("2011-15", "2016-20", "2021-25")
MIN_RESULT, MIN_STATS, NW_LAGS = 36, 60, 3
POS_LO, POS_HI, VAL_MIN = 5, 150, 100e6              # rank group of 13F filers (median over the window's filings)
FUND_TNA_MIN = 15.0                                  # $M, mean assets over the window
TIER_RECORD, STYLE_CAP, TIER_EXPLICIT, CONTROL_N, SEED = 30, 8, 10, 10, 20261117
FOUND_N, TOP_FILERS, TOP_FUNDS = 50, 25, 10
ADD_LO, ADD_HI, ADD_N = 1e9, 30e9, 40                # Addendum A (registration section 13): $1-30bn, top 40
FY0, FY1 = 2010, 2025                                # June formation years of the peer groups
PRE_LO, PRE_HI, PRE_VAL, PRE_MONTHS = 3, 200, 75e6, 30   # loose pre-filter of pull_hold (superset of rank groups)
CHUNK = 55000


def _mi(ym):
    return (np.asarray(ym) // 100) * 12 + np.asarray(ym) % 100 - 1


def _ym(mi):
    return (np.asarray(mi) // 12) * 100 + np.asarray(mi) % 12 + 1


MI_FIRST, MI_LAST, MI_CRSP = int(_mi(M_FIRST)), int(_mi(M_LAST)), int(_mi(CRSP_FROM))
WIN = [(w, int(_mi(a)), int(_mi(b))) for w, a, b in WINDOWS]


def _q_of(d):
    d = pd.to_datetime(d)
    return (d.dt.year * 4 + (d.dt.month - 1) // 3).astype("int64").to_numpy()


def _qend_mi(q):
    q = np.asarray(q)
    return (q // 4) * 12 + 3 * (q % 4) + 2


def _entry_mi(q):
    """Month in which the 45-day deadline of quarter q falls (holdings enter at its close)."""
    y, k = divmod(int(q), 4)
    d = pd.Timestamp(y, 3 * k + 3, 1) + pd.offsets.MonthEnd(0) + pd.Timedelta(days=45)
    return d.year * 12 + d.month - 1


def input_sha():
    return hashlib.sha256(json.dumps([INV, DOCS], sort_keys=True).encode()).hexdigest()


PULL_VERSION = "pull-1"     # change whenever a pull query or a pre-filter constant changes: old pulls then go stale


def pull_key():
    """Hash of what the investor-dependent pulls depend on: the pull code version, library 13F filers (always
    pulled) and library funds (all their share classes pulled). A change needs fresh eq_sc_cand, eq_sc_hold_*,
    eq_sc_fret_* and eq_sc_fmeta."""
    return hashlib.sha256(json.dumps([PULL_VERSION, _lib_mgrnos(), _lib_fundnos()]).encode()).hexdigest()


def code_sha():
    """SHA-256 of this module's code with the frozen input block left out (seal_check.code_hash), computed from the
    file that is running."""
    try:
        text = open(__file__, encoding="utf-8").read()
    except (IOError, OSError, NameError):
        return "unknown"
    lines = text.splitlines(True)
    try:
        i = next(k for k, x in enumerate(lines) if x.startswith("# >>> FROZEN INPUT"))
        j = next(k for k, x in enumerate(lines) if x.startswith("# <<< FROZEN INPUT"))
    except StopIteration:
        return "unknown"
    return hashlib.sha256("".join(lines[:i + 1] + lines[j:]).encode("utf-8")).hexdigest()


def _clean(e):
    """Exception text without SQL, id lists or data: class and the first line, before any '[SQL'."""
    s = str(e).split("[SQL")[0].strip().splitlines()
    s = s[0] if s else ""
    return "%s: %s" % (type(e).__name__, re.sub(r"\d[\d,.\s]{20,}", "<numbers>", s)[:200])


# ------------------------------------------------------------------------------------------------------- pulls
def _runner(save, out, data, budget):
    t0 = time.time()
    st = {"left": 0}

    def have(name):
        return bool(data) and os.path.exists(os.path.join(data, name + ".csv.gz"))

    def step(name, fn):
        if have(name):
            return
        if time.time() - t0 > budget:
            st["left"] += 1
            return
        t1 = time.time()
        try:
            df = fn()
        except Exception as e:  # noqa: BLE001
            raise RuntimeError("%s not pulled: %s" % (name, _clean(e))) from None
        if data:                                  # written under a temporary name, then renamed: never half a file
            save(name + "_part", df)
            os.replace(os.path.join(data, name + "_part.csv.gz"), os.path.join(data, name + ".csv.gz"))
        else:
            save(name, df)
        out("  %-18s %9d rows %6.0f s" % (name, len(df), time.time() - t1))
    return have, step, st, t0


def _done(out, what, st, t0):
    out("%s: %s after %.0f s" % (what, ("%d data sets left for the next run" % st["left"]) if st["left"]
                                else "complete", time.time() - t0))


def pull_base(sql, save, out, data, budget=9000):
    have, step, st, t0 = _runner(save, out, data, budget)
    step("eq_sc_names", lambda: sql("/* eqsc names */ select mgrno, mgrname, rdate2 from tfn.s34names"))
    step("eq_sc_cusip", lambda: sql(
        "/* eqsc cusip */ select distinct cusip, permno, namedt, nameenddt from crsp.stocknames_v2 "
        "where cusip is not null"))
    step("eq_sc_ff", lambda: sql(
        "/* eqsc ff */ select date, mktrf, smb, hml, rmw, cma, umd, rf from ff.fivefactors_monthly "
        "where date between '2009-01-01' and '2025-12-31'"))
    step("eq_sc_bm", lambda: sql(
        "/* eqsc bm */ select permno, public_date, bm from wrdsapps_finratio.firm_ratio where permno is not null "
        "and public_date between '%d-01-01' and '%d-06-30' and extract(month from public_date) <= 6"
        % (FY0, FY1)))
    step("eq_sc_fhdr", lambda: sql(
        "/* eqsc fhdr */ select crsp_fundno, crsp_portno, crsp_cl_grp, fund_name, index_fund_flag, et_flag "
        "from crsp.fund_hdr"))
    step("eq_sc_fsty", lambda: sql(
        "/* eqsc fsty */ select crsp_fundno, begdt, enddt, crsp_obj_cd from crsp.fund_style "
        "where enddt >= '2010-12-01' or enddt is null"))
    _done(out, "pull_base", st, t0)


def _crsp_years():
    return list(range(CRSP_FROM // 100, M_LAST // 100 + 1))


def _fund_years():
    return list(range(M_FIRST // 100 - 1, M_LAST // 100 + 1))


def pull_crsp(sql, save, out, data, budget=9000):
    have, step, st, t0 = _runner(save, out, data, budget)
    for y in _crsp_years():
        lo = "%d-%02d-01" % (y, CRSP_FROM % 100) if y == CRSP_FROM // 100 else "%d-01-01" % y
        step("eq_sc_msf_%d" % y, lambda lo=lo, y=y: sql(
            "/* eqsc msf %s %d-12-31 */ select permno, yyyymm, mthret, mthprc, shrout, primaryexch, securitytype, "
            "securitysubtype, sharetype from crsp.msf_v2 where mthcaldt between '%s' and '%d-12-31'"
            % (lo, y, lo, y)))
    _done(out, "pull_crsp", st, t0)


def _hyears():
    return list(range(int(H_FROM[:4]), int(H_TO[:4]) + 1))


def _hrange(y):
    return (H_FROM if y == int(H_FROM[:4]) else "%d-01-01" % y), (H_TO if y == int(H_TO[:4]) else "%d-12-31" % y)


AGG_SQL = """/* eqsc agg %(lo)s %(hi)s */
with h as (
  select mgrno, rdate, cusip, sum(shares)::float8 as sh, sum(shares * coalesce(prc, 0))::float8 as fv
  from tfn.s34
  where fdate = rdate and shares > 0 and rdate between '%(lo)s' and '%(hi)s'
  group by mgrno, rdate, cusip),
n as (
  select distinct cusip, permno, namedt, coalesce(nameenddt, date '2099-12-31') as ne
  from crsp.stocknames_v2 where cusip is not null),
k as (
  select distinct on (h.mgrno, h.rdate, h.cusip) h.mgrno, h.rdate, h.sh, h.fv, n.permno
  from h left join n on n.cusip = h.cusip and h.rdate between n.namedt and n.ne
  order by h.mgrno, h.rdate, h.cusip, n.permno),
p as (
  select permno, yyyymm, abs(mthprc)::float8 as px from crsp.msf_v2
  where mthcaldt between '%(lo)s' and '%(hi)s' and mthprc is not null and mthprc <> 0)
select k.mgrno, k.rdate, sum(k.fv) as fv_all,
  sum(case when p.px is not null then k.fv else 0 end) as fv_used,
  count(distinct case when p.px is not null then k.permno end) as npos,
  sum(case when p.px is not null then k.sh * p.px else 0 end) as val
from k left join p on p.permno = k.permno
  and p.yyyymm = (extract(year from k.rdate) * 100 + extract(month from k.rdate))::int
group by k.mgrno, k.rdate"""


def pull_agg(sql, save, out, data, budget=9000):
    have, step, st, t0 = _runner(save, out, data, budget)
    for y in _hyears():
        lo, hi = _hrange(y)
        step("eq_sc_agg_%d" % y, lambda lo=lo, hi=hi: sql(AGG_SQL % {"lo": lo, "hi": hi}))
    _done(out, "pull_agg", st, t0)


def _lib_mgrnos():
    """Filers of investors ranked on their 13F (their holdings are always pulled)."""
    return sorted({int(m) for p in INV if p.get("record_kind") == "13f" for m in p.get("mgrnos", [])})


def _lib_fundnos():
    return sorted({int(f) for p in INV if p.get("record_kind") == "fund" for f in p.get("fundnos", [])})


def _known_mgrnos():
    """Every filer matched to a library investor, whatever its record kind (left out of the best-scored list)."""
    return {int(m) for p in INV for k in ("mgrnos", "known_mgrnos") for m in p.get(k, [])}


def _known_fundnos():
    return {int(f) for p in INV for k in ("fundnos", "known_fundnos") for f in p.get(k, [])}


def candidates(load):
    """Filers that can be in a rank group of some window (loose pre-filter on the SQL aggregate) + library filers."""
    a = pd.concat([load("eq_sc_agg_%d" % y) for y in _hyears()], ignore_index=True)
    a = a[(a.npos >= 1) & (a.val > 0)]
    f = pd.DataFrame({"bk": a.mgrno.astype("int64").to_numpy(), "q": _q_of(a.rdate),
                      "npos": a.npos.to_numpy(float), "val": a.val.to_numpy(float)})
    f = f.groupby(["bk", "q"], as_index=False).agg(npos=("npos", "max"), val=("val", "max"))
    f = _schedule(f, {})
    keep = set()
    for w, a0, b0 in WIN:
        lo, hi = _win_span(f, a0, b0)
        sub = f[lo <= hi].assign(n=(hi - lo + 1)[lo <= hi])
        g = sub.groupby("bk").agg(npos=("npos", "median"), val=("val", "median"), n=("n", "sum"))
        ok = (g.npos >= PRE_LO) & (g.npos <= PRE_HI) & (g.val >= PRE_VAL) & (g.n >= PRE_MONTHS)
        keep |= set(g.index[ok].tolist())
    return sorted(keep | set(_lib_mgrnos()))


def _stale(load, have, name, out):
    """True (and a message) if a stored data set was made for another investor input."""
    if not have(name):
        return False
    k = load(name).key.astype(str)
    if len(k) and k.iloc[0] == pull_key():
        return False
    out("%s was pulled for another investor input: delete eq_sc_cand, eq_sc_hold_*, eq_sc_fret_*, eq_sc_fmeta "
        "(a delete step in the pull job) and pull again" % name)
    return True


def pull_hold(sql, load, save, out, data, budget=9000):
    have, step, st, t0 = _runner(save, out, data, budget)
    if not all(have("eq_sc_agg_%d" % y) for y in _hyears()):
        out("pull_hold: the per-quarter aggregates are not complete; run pull_agg again")
        return
    if _stale(load, have, "eq_sc_cand", out):
        return
    if not have("eq_sc_cand") and any(have("eq_sc_hold_%d" % y) for y in _hyears()):
        out("pull_hold refused: holdings years exist without eq_sc_cand (orphans): delete eq_sc_hold_* and pull again")
        return
    step("eq_sc_cand", lambda: pd.DataFrame({"mgrno": candidates(load)}).assign(key=pull_key()))
    if not have("eq_sc_cand"):
        out("pull_hold: candidate list not written yet; run again")
        return
    ids = load("eq_sc_cand").mgrno.astype("int64").tolist()
    inl = ",".join(str(i) for i in ids) or "-1"
    out("  candidate filers: %d" % len(ids))
    for y in _hyears():
        lo, hi = _hrange(y)
        step("eq_sc_hold_%d" % y, lambda lo=lo, hi=hi: sql(
            "/* eqsc hold %s %s */ select mgrno, rdate, cusip, shares::float8 as shares, prc::float8 as prc "
            "from tfn.s34 where fdate = rdate and shares > 0 and rdate between '%s' and '%s' and mgrno in (%s)"
            % (lo, hi, lo, hi, inl)))
    _done(out, "pull_hold", st, t0)


FUND_GROUPS = ("crsp_fundno in (select h.crsp_fundno from crsp.fund_hdr h where h.crsp_fundno in (%(s)s) or "
               "h.crsp_cl_grp in (select h2.crsp_cl_grp from crsp.fund_hdr h2 where h2.crsp_fundno in (%(s)s)) or "
               "(h.crsp_cl_grp is null and h.crsp_portno in (select h3.crsp_portno from crsp.fund_hdr h3 where "
               "h3.crsp_cl_grp is null and h3.crsp_fundno in (%(s)s))))")


def pull_funds(sql, load, save, out, data, budget=9000):
    """Every share class of every fund (class group, else portfolio) with a class that ever had an ED code, and of
    every library fund."""
    have, step, st, t0 = _runner(save, out, data, budget)
    if _stale(load, have, "eq_sc_fmeta", out):
        return
    if not have("eq_sc_fmeta") and any(have("eq_sc_fret_%d" % y) for y in _fund_years()):
        out("pull_funds refused: fund years exist without eq_sc_fmeta (orphans): delete eq_sc_fret_* and pull again")
        return
    step("eq_sc_fmeta", lambda: pd.DataFrame({"key": [pull_key()]}))     # written before the fund years
    lib = ",".join(str(f) for f in _lib_fundnos())
    cond = FUND_GROUPS % {"s": "select crsp_fundno from crsp.fund_style where crsp_obj_cd like 'ED%'"}
    if lib:
        cond = "(%s or %s)" % (cond, FUND_GROUPS % {"s": lib})
    for y in _fund_years():
        lo = "%d-12-01" % y if y < M_FIRST // 100 else "%d-01-01" % y
        step("eq_sc_fret_%d" % y, lambda lo=lo, y=y: sql(
            "/* eqsc fret %s %d-12-31 lib=%s */ select crsp_fundno, caldt, mtna::float8 as mtna, mret::float8 as "
            "mret from crsp.monthly_tna_ret_nav where caldt between '%s' and '%d-12-31' and %s"
            % (lo, y, lib or "-", lo, y, cond)))
    _done(out, "pull_funds", st, t0)


def _inputs():
    n = ["eq_sc_names", "eq_sc_cusip", "eq_sc_ff", "eq_sc_bm", "eq_sc_fhdr", "eq_sc_fsty", "eq_sc_cand", "eq_sc_fmeta"]
    n += ["eq_sc_msf_%d" % y for y in _crsp_years()]
    n += ["eq_sc_agg_%d" % y for y in _hyears()]
    n += ["eq_sc_hold_%d" % y for y in _hyears()]
    n += ["eq_sc_fret_%d" % y for y in _fund_years()]
    return n


def _pull_state(load, data):
    miss = [n for n in _inputs() if not os.path.exists(os.path.join(data, n + ".csv.gz"))]
    stale = [n for n in ("eq_sc_cand", "eq_sc_fmeta") if n not in miss
             and str(load(n).key.astype(str).iloc[0]) != pull_key()]
    return miss, stale


def cleanup(out, data):
    """Job eq_sc_cleanup_v<n>, run once the result is accepted: deletes every stored eq_sc_ data set except the
    report (eq_sc_report holds results only)."""
    n = 0
    for f in sorted(os.listdir(data)):
        if f.startswith("eq_sc_") and f.endswith(".csv.gz") and f != "eq_sc_report.csv.gz":
            os.remove(os.path.join(data, f))
            n += 1
    out("cleanup: %d eq_sc_ data sets deleted (eq_sc_report kept)" % n)


def pull_status(load, out, data):
    miss, stale = _pull_state(load, data)
    if not miss and not stale:
        out("ALL PULLS COMPLETE: %d data sets, pull key %s" % (len(_inputs()), pull_key()[:16]))
    else:
        out("PULLS NOT COMPLETE: %d data sets missing (first: %s), %d made for another investor input%s"
            % (len(miss), miss[0] if miss else "-", len(stale), (" (%s)" % ", ".join(stale)) if stale else ""))


# ----------------------------------------------------------------------------------------------- CRSP panel
class Panel(object):
    """CRSP monthly panel as arrays: rows = permno (sorted), columns = months from 2009-06 to 2025-12."""

    def __init__(self, msf):
        msf = msf.copy()
        msf["j"] = _mi(msf.yyyymm.astype("int64").to_numpy()) - MI_CRSP
        msf = msf[(msf.j >= 0) & (msf.j <= MI_LAST - MI_CRSP)]
        msf = msf.drop_duplicates(["permno", "j"], keep="last")
        self.perm = np.sort(msf.permno.astype("int64").unique())
        self.nm = MI_LAST - MI_CRSP + 1
        ri = np.searchsorted(self.perm, msf.permno.astype("int64").to_numpy())
        j = msf.j.to_numpy()
        shape = (len(self.perm), self.nm)
        self.R = np.full(shape, np.nan)
        self.P = np.full(shape, np.nan)
        self.C = np.full(shape, np.nan)
        self.COM = np.zeros(shape, bool)
        self.NY = np.zeros(shape, bool)
        r = np.array(pd.to_numeric(msf.mthret, errors="coerce"), dtype=float)   # includes the delisting return
        r[r < -1] = np.nan                                                 # any missing-value code
        self.R[ri, j] = r
        p = np.abs(pd.to_numeric(msf.mthprc, errors="coerce").to_numpy(float))
        p[p == 0] = np.nan
        self.P[ri, j] = p
        self.C[ri, j] = p * pd.to_numeric(msf.shrout, errors="coerce").to_numpy(float)
        def txt(c):
            return msf[c].fillna("").astype(str).to_numpy()
        ex = txt("primaryexch")
        self.COM[ri, j] = ((txt("securitytype") == "EQTY") & (txt("securitysubtype") == "COM")
                           & (txt("sharetype") == "NS") & np.isin(ex, ["N", "A", "Q"]))
        self.NY[ri, j] = ex == "N"

    def rows(self, permno):
        permno = np.asarray(permno, dtype="int64")
        i = np.searchsorted(self.perm, permno)
        ic = np.minimum(i, len(self.perm) - 1)
        ok = (i < len(self.perm)) & (self.perm[ic] == permno) if len(self.perm) else np.zeros(len(permno), bool)
        return ic, ok

    def at(self, arr, ri, ok, mi):
        mi = np.broadcast_to(np.asarray(mi), ri.shape)
        j = mi - MI_CRSP
        good = ok & (j >= 0) & (j < self.nm)
        v = np.full(ri.shape, np.nan)
        v[good] = arr[ri[good], j[good]]
        return v


BM_AMBIGUOUS = [0]


def _bm_table(bm, panel):
    """Book-to-market per permno and formation year: latest firm_ratio row with public_date on or before June 30."""
    b = bm.copy()
    d = pd.to_datetime(b.public_date)
    b = b[d.dt.month <= 6]
    b["fy"] = d[d.dt.month <= 6].dt.year.to_numpy()
    b["d"] = d[d.dt.month <= 6].to_numpy()
    b["bm"] = pd.to_numeric(b.bm, errors="coerce")
    b = b[np.isfinite(b.bm)]
    last = b.groupby(["permno", "fy"]).d.transform("max")
    b = b[b.d == last]
    nb = b.groupby(["permno", "fy"]).bm.transform("nunique")
    amb = b[nb > 1][["permno", "fy"]].drop_duplicates()
    b = b[nb == 1].drop_duplicates(["permno", "fy"])          # two different values on the latest date: no value
    BM_AMBIGUOUS[0] = len(amb)
    out = np.full((len(panel.perm), FY1 - FY0 + 1), np.nan)
    ri, ok = panel.rows(b.permno.to_numpy())
    col = b.fy.to_numpy() - FY0
    good = ok & (col >= 0) & (col <= FY1 - FY0)
    out[ri[good], col[good]] = b.bm.to_numpy()[good]
    return out


def _fifths(v, ids):
    """Fifths 0..4 of v (ties broken by id): floor(5 * rank / n)."""
    order = np.lexsort((ids, v))
    rk = np.empty(len(v), dtype="int64")
    rk[order] = np.arange(len(v))
    return (5 * rk) // max(len(v), 1)


class Peers(object):
    """DGTW peer groups (125) formed each June, held July to June; value-weighted group returns per month."""

    def __init__(self, panel, bmt):
        self.panel = panel
        self.G = np.full((len(panel.perm), FY1 - FY0 + 1), -1, dtype="int16")
        self.B = np.full((125, panel.nm), np.nan)
        for fy in range(FY0, FY1 + 1):
            self._form(fy, bmt)

    def _j(self, mi):
        return int(mi) - MI_CRSP

    def _form(self, fy, bmt):
        p = self.panel
        js = self._j(fy * 12 + 5)       # size at the end of June of the formation year
        jf = self._j(fy * 12 + 5)       # share type and exchange at the end of June
        jm = self._j(fy * 12 + 5)       # momentum: the twelve months June (fy-1) .. May (fy)
        if jm - 12 < 0 or js >= p.nm:
            return
        cap = p.C[:, js]
        mom = np.prod(1.0 + p.R[:, jm - 12:jm], axis=1) - 1.0
        bmv = bmt[:, fy - FY0]
        u = p.COM[:, jf] & np.isfinite(cap) & (cap > 0) & np.isfinite(bmv) & (bmv > 0) & np.isfinite(mom)
        ny = u & p.NY[:, jf]
        if ny.sum() < 5:
            return
        bps = np.percentile(cap[ny], [20, 40, 60, 80])
        idx = np.where(u)[0]
        s = np.searchsorted(bps, cap[idx], side="left")
        g = np.full(len(idx), -1, dtype="int64")
        ids = p.perm[idx]
        for si in range(5):
            a = np.where(s == si)[0]
            if not len(a):
                continue
            b = _fifths(bmv[idx[a]], ids[a])
            for bi in range(5):
                c = a[b == bi]
                if not len(c):
                    continue
                m = _fifths(mom[idx[c]], ids[c])
                g[c] = si * 25 + bi * 5 + m
        self.G[idx, fy - FY0] = g
        # value-weighted group returns July fy .. June fy+1 (weights: previous month-end market value)
        gg = self.G[:, fy - FY0].astype("int64")
        for mi in range(fy * 12 + 6, fy * 12 + 18):
            j = self._j(mi)
            if j <= 0 or j >= p.nm:
                continue
            r, w = p.R[:, j], p.C[:, j - 1]
            v = (gg >= 0) & np.isfinite(r) & np.isfinite(w) & (w > 0)
            sw = np.bincount(gg[v], weights=w[v], minlength=125)
            swr = np.bincount(gg[v], weights=w[v] * r[v], minlength=125)
            with np.errstate(invalid="ignore", divide="ignore"):
                self.B[:, j] = np.where(sw > 0, swr / sw, np.nan)

    def group(self, ri, ok, mi):
        fy = np.where(np.asarray(mi) % 12 >= 6, np.asarray(mi) // 12, np.asarray(mi) // 12 - 1)
        col = np.broadcast_to(fy - FY0, ri.shape)
        good = ok & (col >= 0) & (col <= FY1 - FY0)
        g = np.full(ri.shape, -1, dtype="int64")
        g[good] = self.G[ri[good], col[good]]
        return g

    def bench(self, g, mi):
        j = int(mi) - MI_CRSP
        b = np.full(g.shape, np.nan)
        if 0 <= j < self.panel.nm:
            v = g >= 0
            b[v] = self.B[g[v], j]
        return b


# ------------------------------------------------------------------------------------------- factors, stats
class Factors(object):
    def __init__(self, ff):
        d = pd.to_datetime(ff["date"])
        mi = (d.dt.year * 12 + d.dt.month - 1).to_numpy()
        n = MI_LAST - MI_CRSP + 1
        self.X = np.full((n, 6), np.nan)
        self.RF = np.full(n, np.nan)
        j = mi - MI_CRSP
        v = (j >= 0) & (j < n)
        cols = ["mktrf", "smb", "hml", "rmw", "cma", "umd"]
        self.X[j[v]] = ff[cols].apply(pd.to_numeric, errors="coerce").to_numpy(float)[v]
        self.RF[j[v]] = pd.to_numeric(ff["rf"], errors="coerce").to_numpy(float)[v]
        self.MKT = self.X[:, 0] + self.RF


def ols_nw(y, X, lags):
    """OLS with an intercept and Newey-West standard errors (Bartlett weights, small-sample factor n/(n-k)), the
    form of qs/btstats.ols_nw. Returns (coefficients, t-values)."""
    y = np.asarray(y, float)
    X = np.column_stack([np.ones(len(y)), np.asarray(X, float)])
    n, k = X.shape
    if n <= k + 1:
        return None, None
    XtX_inv = np.linalg.pinv(X.T @ X)
    b = XtX_inv @ X.T @ y
    u = y - X @ b
    Xu = X * u[:, None]
    S = Xu.T @ Xu
    for lag in range(1, lags + 1):
        G = Xu[lag:].T @ Xu[:-lag]
        S += (1 - lag / (lags + 1.0)) * (G + G.T)
    V = XtX_inv @ S @ XtX_inv * n / max(n - k, 1)
    se = np.sqrt(np.maximum(np.diag(V), 1e-30))
    return b, b / se


def _stats(mi, ret, ff, extra=None):
    """Window statistics of a monthly return series (months mi, sorted)."""
    n = len(mi)
    st = {"n": n}
    if n == 0:
        return st
    j = mi - MI_CRSP
    if n >= MIN_RESULT:
        X, ex = ff.X[j], ret - ff.RF[j]
        ok = np.isfinite(ex) & np.all(np.isfinite(X), axis=1)
        b, t = ols_nw(ex[ok], X[ok], NW_LAGS)
        if b is not None:
            st["a"], st["t"] = 1200.0 * b[0], t[0]
    st["r"] = 100.0 * (np.prod(1.0 + ret) ** (12.0 / n) - 1.0)
    mk = ff.MKT[j]
    if np.all(np.isfinite(mk)):
        st["rm"] = st["r"] - 100.0 * (np.prod(1.0 + mk) ** (12.0 / n) - 1.0)
    w = np.cumprod(1.0 + ret)
    peak = np.maximum.accumulate(np.concatenate([[1.0], w]))[1:]
    st["dd"] = 100.0 * float(np.min(w / peak - 1.0))
    yrs = mi // 12
    beat = full = 0
    for y in np.unique(yrs):
        s = yrs == y
        if s.sum() == 12 and np.all(np.isfinite(mk[s])):
            full += 1
            beat += int(np.prod(1.0 + ret[s]) > np.prod(1.0 + mk[s]))
    if full:
        st["yb"] = beat / float(full)
    for key, arr in (extra or {}).items():
        a = np.asarray(arr, float)
        f = np.isfinite(a)
        if key in ("pa", "p10", "pn"):
            if f.sum():
                st[key] = 1200.0 * float(np.mean(a[f]))
        elif f.sum():
            st[key] = float(np.mean(a[f]))
    return st


# ------------------------------------------------------------------------------------------ 13F copy books
NON_QUARTER_END = [0]


def _positions(h, cus, panel):
    """Matched positions per filer and quarter (first versions; CUSIP valid at the quarter-end; CRSP price at the
    quarter-end) and per filing the filed and used value."""
    h = h[h.cusip.notna() & h.mgrno.notna()].copy()
    h["cusip"] = h.cusip.astype(str)
    h["mgrno"] = h.mgrno.astype("int64")
    h["rdate"] = pd.to_datetime(h.rdate)
    h["q"] = _q_of(h.rdate)
    NON_QUARTER_END[0] += int((h.rdate != h.rdate + pd.offsets.QuarterEnd(0)).sum())
    h = h[h.rdate == h.groupby(["mgrno", "q"]).rdate.transform("max")]     # one filing per manager and quarter
    h["fv"] = h.shares.astype(float) * pd.to_numeric(h.prc, errors="coerce").abs().fillna(0.0).to_numpy()
    g = h.groupby(["mgrno", "q", "cusip"], as_index=False).agg(sh=("shares", "sum"), fv=("fv", "sum"),
                                                              rdate=("rdate", "first"))
    fil = g.groupby(["mgrno", "q"], as_index=False).agg(fv_all=("fv", "sum"))
    c = cus[cus.cusip.notna() & cus.permno.notna()].copy()
    c["cusip"] = c.cusip.astype(str)
    c["namedt"] = pd.to_datetime(c.namedt, errors="coerce").fillna(pd.Timestamp("1900-01-01"))
    c["nameenddt"] = pd.to_datetime(c.nameenddt, errors="coerce").fillna(pd.Timestamp("2099-12-31"))
    m = g.merge(c[["cusip", "permno", "namedt", "nameenddt"]], on="cusip", how="inner")
    m = m[(m.rdate >= m.namedt) & (m.rdate <= m.nameenddt)]
    m = m.sort_values(["mgrno", "q", "cusip", "permno"]).drop_duplicates(["mgrno", "q", "cusip"])
    ri, ok = panel.rows(m.permno.to_numpy())
    px = panel.at(panel.P, ri, ok, _qend_mi(m.q.to_numpy()))
    m = m.assign(px=px)
    m = m[np.isfinite(m.px) & (m.px > 0)]
    m = m.assign(val=m.sh * m.px, permno=m.permno.astype("int64"))
    pos = m.groupby(["mgrno", "q", "permno"], as_index=False).agg(val=("val", "sum"), fv=("fv", "sum"))
    used = pos.groupby(["mgrno", "q"], as_index=False).agg(fv_used=("fv", "sum"))
    fil = fil.merge(used, on=["mgrno", "q"], how="left")
    fil["fv_used"] = fil.fv_used.fillna(0.0)
    return pos[["mgrno", "q", "permno", "val"]], fil


def _schedule(f, cut):
    """Holding months of each filing (registration 3.4-3.5): from the close of the deadline month, three months,
    buy and hold. If the next quarter's filing is missing, the portfolio is held three more months (six in all),
    whether or not the filer files again; if the quarter after is missing too the spell ends there. Decided only
    from what was public. cut: book -> (first, last) record month index."""
    f = f.sort_values(["bk", "q"]).reset_index(drop=True)
    nxt = f.groupby("bk").q.shift(-1)
    f["H"] = np.where((nxt - f.q) == 1, 3, 6).astype("int64")
    em = {q: _entry_mi(q) for q in f.q.unique()}
    f["em"] = f.q.map(em).astype("int64")
    lo = np.full(len(f), MI_FIRST, dtype="int64")
    hi = np.full(len(f), MI_LAST, dtype="int64")
    for bk, (a, b) in cut.items():
        s = (f.bk == bk).to_numpy()
        lo[s], hi[s] = max(a, MI_FIRST), min(b, MI_LAST)
    f["lo_b"], f["hi_b"] = lo, hi
    return f


def _win_span(f, a, b):
    lo = np.maximum.reduce([f.em.to_numpy() + 1, f.lo_b.to_numpy(), np.full(len(f), a)])
    hi = np.minimum.reduce([f.em.to_numpy() + f.H.to_numpy(), f.hi_b.to_numpy(), np.full(len(f), b)])
    return lo, hi


def _hold(pos, em, panel, peers):
    """Buy and hold of one quarter's positions. pos: bk, permno, w (sums to 1 per book), h (months held).
    Returns per book and record month: return, weight share without a return, peer-adjusted return, weight share
    with a peer group."""
    if not len(pos):
        return []
    ri, ok = panel.rows(pos.permno.to_numpy())
    w0, h = pos.w.to_numpy(float), pos.h.to_numpy()
    codes, books = pd.factorize(pos.bk, sort=True)
    cum = np.ones(len(pos))
    res = []
    for k in range(1, int(h.max()) + 1):
        mi = em + k
        if mi > MI_LAST:
            break
        r = panel.at(panel.R, ri, ok, mi)
        miss = ~np.isfinite(r)
        rr = np.where(miss, 0.0, r)
        if mi >= MI_FIRST:
            act = h >= k
            g = peers.group(ri, ok, mi)
            b = peers.bench(g, mi)
            pm = act & ~miss & np.isfinite(b)
            w = w0 * cum
            nb = len(books)
            sw = np.bincount(codes[act], weights=w[act], minlength=nb)
            swr = np.bincount(codes[act], weights=(w * rr)[act], minlength=nb)
            swm = np.bincount(codes[act], weights=(w * miss)[act], minlength=nb)
            swp = np.bincount(codes[pm], weights=w[pm], minlength=nb)
            swd = np.bincount(codes[pm], weights=(w * (rr - np.where(pm, b, 0.0)))[pm], minlength=nb)
            live = np.bincount(codes[act], minlength=nb) > 0
            with np.errstate(invalid="ignore", divide="ignore"):
                res.append(pd.DataFrame({"bk": np.asarray(books)[live], "mi": mi, "ret": (swr / sw)[live],
                                         "miss": (swm / sw)[live],
                                         "pa": np.where(swp > 0, swd / swp, np.nan)[live],
                                         "pash": np.where(sw > 0, swp / sw, np.nan)[live]}))
        cum = cum * (1.0 + rr)
    return res


def _books(pos, fil, panel, peers):
    """All filers (book = mgrno) and library 13F investors (book = -(n+1); several mgrno = one filer, the larger
    filing when two file the same quarter): filing table and monthly record (copy portfolio, peer-adjusted, top-10
    and new-positions variants). Turnover and new positions are computed quarter by quarter to keep memory small."""
    P = [pos.rename(columns={"mgrno": "bk"})]
    F = [fil.rename(columns={"mgrno": "bk"})]
    cut, lib = {}, {}
    for n, p in enumerate(INV):
        if p.get("record_kind") != "13f":
            continue
        bk = -(n + 1)
        mg = sorted({int(m) for m in p.get("mgrnos", [])})
        lib[bk] = (p["id"], mg)
        a = int(_mi(int(p["start_ym"]))) if p.get("start_ym") else MI_FIRST
        b = int(_mi(int(p["end_ym"]))) if p.get("end_ym") else MI_LAST
        cut[bk] = (a, b)
        s = pos[pos.mgrno.isin(mg)]
        v = s.groupby(["q", "mgrno"], as_index=False).val.sum().sort_values(["q", "val", "mgrno"],
                                                                           ascending=[True, False, True])
        pick = v.drop_duplicates("q")[["q", "mgrno"]]   # one filer under several mgrno: the larger filing
        P.append(s.merge(pick, on=["q", "mgrno"])[["q", "permno", "val"]].assign(bk=bk))
        t = fil.merge(pick, on=["q", "mgrno"])
        F.append(t[["q", "fv_all", "fv_used"]].assign(bk=bk))
    P = pd.concat(P, ignore_index=True)[["bk", "q", "permno", "val"]]
    P["w"] = P.val / P.groupby(["bk", "q"]).val.transform("sum")
    P = P.sort_values(["q", "bk", "w", "permno"], ascending=[True, True, False, True]).reset_index(drop=True)
    st = P.groupby(["bk", "q"], as_index=False).agg(npos=("permno", "count"), val=("val", "sum"))
    Fa = pd.concat(F, ignore_index=True).groupby(["bk", "q"], as_index=False)[["fv_all", "fv_used"]].sum()
    st = st.merge(Fa, on=["bk", "q"], how="left")
    with np.errstate(invalid="ignore", divide="ignore"):
        st["fvsh"] = np.where(st.fv_all > 0, st.fv_used / st.fv_all, np.nan)
    st = _schedule(st, cut)
    H = st.set_index(["bk", "q"]).H
    qs = P.q.to_numpy()
    uq = np.unique(qs)
    cuts = {q: (np.searchsorted(qs, q, "left"), np.searchsorted(qs, q, "right")) for q in uq}
    res, r10, rnew, extra = [], [], [], []
    for q in uq:
        a0, b0 = cuts[q]
        cur = P.iloc[a0:b0]
        rk = cur.groupby("bk").cumcount().to_numpy()
        top = cur[rk < 10]
        t10 = top.groupby("bk").w.sum()
        tov = pd.Series(np.nan, index=t10.index)
        new = cur.iloc[0:0]
        if q - 1 in cuts:
            a1, b1 = cuts[q - 1]
            prv = P.iloc[a1:b1]
            both = set(prv.bk) & set(cur.bk)
            c2, p2 = cur[cur.bk.isin(both)], prv[prv.bk.isin(both)]
            mm = c2[["bk", "permno", "w"]].merge(p2[["bk", "permno", "w"]], on=["bk", "permno"], how="outer",
                                                 suffixes=("", "_p")).fillna({"w": 0.0, "w_p": 0.0})
            d = (mm.w - mm.w_p).abs().groupby(mm.bk).sum()
            tov.loc[d.index] = 0.5 * d
            nw = c2.merge(p2[["bk", "permno"]].assign(old=1), on=["bk", "permno"], how="left")
            new = nw[nw.old.isna()].drop(columns=["old"])
            new = new.assign(w=new.val / new.groupby("bk").val.transform("sum"))
        extra.append(pd.DataFrame({"bk": t10.index, "q": q, "top10": t10.to_numpy(), "to": tov.to_numpy()}))
        em = _entry_mi(q)
        if em + 1 > MI_LAST or em + 6 < MI_FIRST:
            continue
        for src, acc in ((cur, res), (top, r10), (new, rnew)):
            if not len(src):
                continue
            s = src.assign(q=q)
            s = s.assign(h=H.reindex(pd.MultiIndex.from_arrays([s.bk, s.q])).to_numpy())
            if src is top:
                s = s.assign(w=s.w / s.groupby("bk").w.transform("sum"))
            acc.extend(_hold(s, em, panel, peers))
    st = st.merge(pd.concat(extra, ignore_index=True), on=["bk", "q"], how="left")
    del P
    M = pd.concat(res, ignore_index=True) if res else pd.DataFrame(columns=["bk", "mi", "ret", "miss", "pa", "pash"])
    for acc, col in ((r10, "p10"), (rnew, "pn")):
        if acc:
            x = pd.concat(acc, ignore_index=True)[["bk", "mi", "pa"]].rename(columns={"pa": col})
            M = M.merge(x, on=["bk", "mi"], how="left")
        else:
            M[col] = np.nan
    lim = st.groupby("bk").agg(lo=("lo_b", "first"), hi=("hi_b", "first"))
    M = M.merge(lim, left_on="bk", right_index=True)
    M = M[(M.mi >= M.lo) & (M.mi <= M.hi) & np.isfinite(M.ret)].drop(columns=["lo", "hi"])
    return st, M.sort_values(["bk", "mi"]).reset_index(drop=True), lib


def _book_windows(st, M, ff):
    """Per book and window: statistics, filing medians, rank-group test (13F)."""
    rows = []
    grp = {bk: g for bk, g in M.groupby("bk")}
    for w, a, b in WIN:
        lo, hi = _win_span(st, a, b)
        sub = st[lo <= hi]
        keys = set(zip(sub.bk, sub.q))
        prev_in = np.array([(bk, q - 1) in keys for bk, q in zip(sub.bk, sub.q)], bool)
        fa = sub.groupby("bk").agg(np_=("npos", "median"), val=("val", "median"), tw=("top10", "median"),
                                   fv=("fvsh", "mean"))
        tov = sub[prev_in & np.isfinite(sub.to)].groupby("bk").to.mean() * 4.0
        for bk in fa.index:
            g = grp.get(bk)
            if g is None:
                s = {"n": 0}
            else:
                g = g[(g.mi >= a) & (g.mi <= b)]
                s = _stats(g.mi.to_numpy(), g.ret.to_numpy(float), ff,
                           {"pa": g.pa, "pv": g.pash, "ms": g.miss, "p10": g.p10, "pn": g.pn})
            s.update({"bk": bk, "w": w, "np": fa.at[bk, "np_"], "valm": fa.at[bk, "val"], "tw": fa.at[bk, "tw"],
                      "fv": fa.at[bk, "fv"], "to": tov.get(bk, np.nan)})
            s["grp"] = bool(bk >= 0 and POS_LO <= s["np"] <= POS_HI and s["valm"] >= VAL_MIN
                            and s["n"] >= MIN_RESULT and "a" in s)
            rows.append(s)
    return pd.DataFrame(rows)


# -------------------------------------------------------------------------------------------------- funds
def _flag(s):
    return s.fillna("").astype(str).str.strip().replace({"nan": "", "None": ""}) != ""


def _fund_classes(hdr):
    h = hdr.drop_duplicates("crsp_fundno")       # one header row per share class
    h = h.assign(crsp_fundno=h.crsp_fundno.astype("int64"))
    cl, pt = h.crsp_cl_grp, h.crsp_portno
    gid = np.where(cl.notna(), "G" + cl.fillna(0).astype("int64").astype(str),
                   np.where(pt.notna(), "P" + pt.fillna(0).astype("int64").astype(str),
                            "C" + h.crsp_fundno.astype(str)))
    return h.assign(gid=gid, idx=_flag(h.index_fund_flag))


def _fund_months(fret, sty):
    """Class-months with return, start-of-month assets (previous month-end TNA) and objective code in force."""
    f = fret.copy()
    f["crsp_fundno"] = f.crsp_fundno.astype("int64")
    f["mtna"] = pd.to_numeric(f.mtna, errors="coerce").where(lambda x: x > 0)      # CRSP -99 = missing
    f["mret"] = pd.to_numeric(f.mret, errors="coerce").where(lambda x: x >= -1)    # any missing-value code
    d = pd.to_datetime(f.caldt)
    f["mi"] = (d.dt.year * 12 + d.dt.month - 1).to_numpy()
    f = f.drop_duplicates(["crsp_fundno", "mi"]).sort_values(["crsp_fundno", "mi"]).reset_index(drop=True)
    pf, pm = f.crsp_fundno.shift(1), f.mi.shift(1)
    f["w"] = np.where((pf == f.crsp_fundno) & (pm == f.mi - 1), f.mtna.shift(1), np.nan)
    f["dt"] = pd.to_datetime(_ym(f.mi).astype(str), format="%Y%m") + pd.offsets.MonthEnd(0)
    s = sty.copy()
    s["crsp_fundno"] = s.crsp_fundno.astype("int64")
    s["begdt"] = pd.to_datetime(s.begdt, errors="coerce")
    s["enddt"] = pd.to_datetime(s.enddt, errors="coerce").fillna(pd.Timestamp("2099-12-31"))
    s = s.dropna(subset=["begdt"]).sort_values("begdt")
    f = pd.merge_asof(f.sort_values("dt"), s[["crsp_fundno", "begdt", "enddt", "crsp_obj_cd"]],
                      left_on="dt", right_on="begdt", by="crsp_fundno", direction="backward")
    code = np.where(f.enddt >= f.dt, f.crsp_obj_cd.fillna("").astype(str), "")
    f["ed"] = pd.Series(code).str.startswith("ED").to_numpy()
    return f.drop(columns=["begdt", "enddt", "crsp_obj_cd"])


def _combine(f, key):
    """Share classes combined by assets at the start of the month."""
    v = np.isfinite(f.mret) & np.isfinite(f.w) & (f.w > 0)
    x = f[v].assign(wr=f.w[v] * f.mret[v])
    g = x.groupby([key, "mi"], as_index=False).agg(sw=("w", "sum"), swr=("wr", "sum"), ed=("ed", "max"))
    g["ret"] = g.swr / g.sw
    t = f[np.isfinite(f.mtna)].groupby([key, "mi"], as_index=False).agg(tna=("mtna", "sum"))
    g = g.merge(t, on=[key, "mi"], how="left")
    return g[(g.mi >= MI_FIRST) & (g.mi <= MI_LAST)].sort_values([key, "mi"])


def _fund_windows(rec, key, ff, idx_ids, cut=None):
    rows = []
    for k, g in rec.groupby(key):
        if cut:
            a0, b0 = cut[k]
            g = g[(g.mi >= a0) & (g.mi <= b0)]
        for w, a, b in WIN:
            x = g[(g.mi >= a) & (g.mi <= b)]
            s = _stats(x.mi.to_numpy(), x.ret.to_numpy(float), ff)
            s.update({"bk": k, "w": w, "tna": float(x.tna.mean()) if len(x) else np.nan,
                      "ed": bool(len(x) and x.ed.all())})
            s["grp"] = bool(k not in idx_ids and s["ed"] and s["tna"] >= FUND_TNA_MIN and s["n"] >= MIN_RESULT
                            and "a" in s)
            rows.append(s)
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------------------------- ranks, tiers
def _share(pool, x, own):
    """Rank share of x in the pool (0 worst .. 1 best, ties average) after taking out the investor's own entries;
    missing unless one of its own entries is in the pool."""
    if x is None or not np.isfinite(x) or not len(pool) or not pool.index.isin(list(own)).any():
        return np.nan
    v = pool[~pool.index.isin(list(own))].to_numpy(float)
    if len(v) == 0:
        return np.nan
    return (np.sum(v < x) + 0.5 * np.sum(v == x)) / float(len(v))


def _member_shares(pool):
    if len(pool) < 2:
        return pd.Series(np.nan, index=pool.index)
    return (pool.rank(method="average") - 1.0) / (len(pool) - 1.0)


def _blockpos(tab):
    """Share of the blocks with a result in which the six-factor alpha is positive."""
    t = tab[tab.w.isin(BLOCKS) & (tab.n >= MIN_RESULT) & tab.a.notna()]
    return t.groupby("bk").a.apply(lambda s: float((s > 0).mean()))


def _pools(tab):
    pool = {w: tab[(tab.w == w) & tab.grp].set_index("bk").a.astype(float) for w, _, _ in WIN}
    ingrp = set(tab[tab.w.isin(BLOCKS) & tab.grp].bk)
    bp = _blockpos(tab)
    bpool = bp[bp.index.isin(ingrp)]
    return pool, bpool


def _spearman(x, y):
    rx, ry = pd.Series(x).rank().to_numpy(), pd.Series(y).rank().to_numpy()
    if len(rx) < 3 or np.std(rx) == 0 or np.std(ry) == 0:
        return np.nan
    return float(np.corrcoef(rx, ry)[0, 1])


def _quint(s):
    r = s.rank(method="average")
    return np.minimum(5, np.floor(5 * (r - 1) / len(s)).astype(int) + 1)


def _persist(tab, b1, b2):
    t1 = tab[(tab.w == b1) & tab.grp].set_index("bk").a
    t2 = tab[(tab.w == b2) & (tab.n >= MIN_RESULT) & tab.a.notna()].set_index("bk").a
    both = t1.index[t1.index.isin(t2.index)]
    out = {"pop": len(t1), "both": len(both), "rho": _spearman(t1[both], t2[both]) if len(both) else np.nan}
    tbl = np.zeros((5, 6), dtype=int)
    if len(t1):
        q1 = _quint(t1)
        q2 = _quint(t2[both]) if len(both) else pd.Series(dtype=float)
        for k in t1.index:
            col = int(q2[k]) - 1 if k in q2.index else 5
            tbl[int(q1[k]) - 1, col] += 1
    out["tbl"] = tbl
    return out


def _tiers(inv):
    """Registration section 7. inv: list of dicts with id, grade, own_docs, months, score, style, explicit_*."""
    def num(x, d):
        return d if x is None or (isinstance(x, float) and not np.isfinite(x)) else x
    join = {p["id"]: p["shares_with"] for p in inv if p.get("shares_with")}   # same record as another investor
    elig = [p for p in inv if p["grade"] in ("A", "B", "F") and p["own_docs"] >= 1 and p["months"] >= MIN_STATS
            and p["id"] not in join]
    sc = sorted([p for p in elig if np.isfinite(p["score"])], key=lambda p: (-p["score"], -p["own_docs"], p["id"]))
    rec, per = [], {}
    for p in sc:
        if len(rec) >= TIER_RECORD:
            break
        if per.get(p["style"], 0) >= STYLE_CAP:
            continue
        rec.append(p["id"])
        per[p["style"]] = per.get(p["style"], 0) + 1
    ex = [p for p in inv if p.get("ran_money") == "yes" and p.get("role", "investor") == "investor"
          and p["id"] not in rec]
    ex = sorted(ex, key=lambda p: (-num(p.get("explicit_max"), -1e9), -num(p.get("explicit_mean"), -1e9),
                                   -p["own_docs"], p["id"]))
    exp = [p["id"] for p in ex[:TIER_EXPLICIT]]
    a = set(rec) | set(exp)
    pool = sorted(p["id"] for p in elig if p["id"] not in a)
    ctrl = sorted(random.Random(SEED).sample(pool, CONTROL_N)) if len(pool) > CONTROL_N else list(pool)
    withs = {}
    for j, t in sorted(join.items()):
        if j in exp:
            continue                       # took an explicit place on its own
        withs[j] = ("record" if t in rec else "explicit" if t in exp else "control" if t in ctrl else "B", t)
    b = sorted(p["id"] for p in inv if p["id"] not in a and p["id"] not in set(ctrl) and p["id"] not in withs)
    return {"record": rec, "explicit": exp, "control": ctrl, "B": b, "eligible": len(elig), "with": withs}


def _foundation():
    d = sorted(DOCS, key=lambda r: (-r[1], -r[2], -r[3], r[0]))
    return [int(r[0]) for r in d[:FOUND_N]]


# --------------------------------------------------------------------------------------------------- build
def _load_years(load, prefix, years, **kw):
    return pd.concat([load("%s_%d" % (prefix, y), **kw) for y in years], ignore_index=True)


LAST = {}      # the last build's internal tables, kept inside the module (never returned or printed)


def _where(e):
    """Name and line of the deepest frame of this module in a traceback (no message: it could hold data)."""
    fr = [f for f in traceback.extract_tb(e.__traceback__) if f.filename == globals().get("__file__")]
    f = fr[-1] if fr else traceback.extract_tb(e.__traceback__)[-1]
    return "%s line %d" % (f.name, f.lineno)


def build(load, save, out, data):
    """The scorecard. Starts only if every pull is complete and was made for this investor input (pull key)."""
    LAST.clear()
    save("eq_sc_report", pd.DataFrame({"line": ["build started but not finished: no scorecard"]}))
    miss, stale = _pull_state(load, data)
    if miss or stale:
        out("build refused: %d input data sets missing (first: %s), %d made for another investor input; run the "
            "pull job (eq_sc_pull_v1, v1b, ...) until it prints ALL PULLS COMPLETE"
            % (len(miss), miss[0] if miss else "-", len(stale)))
        return None
    try:
        res = _build(load, out)
        lines = _report_lines(res)
    except Exception as e:  # noqa: BLE001
        out("build FAILED: %s in %s (message not shown: it could hold data)" % (type(e).__name__, _where(e)))
        return None
    save("eq_sc_report", pd.DataFrame({"line": lines}))
    out("build: report %d lines, %d characters" % (len(lines), sum(len(x) + 1 for x in lines)))
    res["lines"] = lines
    LAST.update(res)
    return None


def _build(load, out):
    t0 = time.time()
    BM_AMBIGUOUS[0] = NON_QUARTER_END[0] = 0

    def tick(what):
        out("build: %-34s %6.0f s" % (what, time.time() - t0))
    panel = Panel(_load_years(load, "eq_sc_msf", _crsp_years()))
    tick("CRSP panel %d x %d" % (len(panel.perm), panel.nm))
    peers = Peers(panel, _bm_table(load("eq_sc_bm"), panel))
    ff = Factors(load("eq_sc_ff"))
    tick("peer groups (bm ambiguous: %d)" % BM_AMBIGUOUS[0])
    cus = load("eq_sc_cusip", dtype={"cusip": str})
    parts = [_positions(load("eq_sc_hold_%d" % y, dtype={"cusip": str}), cus, panel) for y in _hyears()]
    pos = pd.concat([x[0] for x in parts], ignore_index=True)       # one year at a time: memory stays small
    fil = pd.concat([x[1] for x in parts], ignore_index=True)
    del parts
    tick("positions (non-quarter-end rdates: %d)" % NON_QUARTER_END[0])
    st, M, lib = _books(pos, fil, panel, peers)
    tick("copy books (%d filers, %d filings)" % (pos.mgrno.nunique(), len(fil)))
    del pos, fil
    tab = _book_windows(st, M, ff)
    tick("13F windows")
    hdr = _fund_classes(load("eq_sc_fhdr"))
    fm = _fund_months(_load_years(load, "eq_sc_fret", _fund_years()), load("eq_sc_fsty"))
    fm = fm.merge(hdr[["crsp_fundno", "gid"]], on="crsp_fundno", how="inner")
    idx_ids = set(hdr[hdr.idx].gid)
    frec = _combine(fm, "gid")
    ftab = _fund_windows(frec, "gid", ff, idx_ids)
    lrec, lcut, lown = [], {}, {}
    for n, p in enumerate(INV):
        if p.get("record_kind") != "fund":
            continue
        fn = sorted({int(x) for x in p.get("fundnos", [])})
        gids = set(hdr[hdr.crsp_fundno.isin(fn)].gid)      # each listed fundno stands for all its share classes
        lrec.append(fm[fm.gid.isin(gids)].assign(inv=p["id"]))   # several funds: one record, combined by assets
        lcut[p["id"]] = (int(_mi(int(p["start_ym"]))) if p.get("start_ym") else MI_FIRST,
                         int(_mi(int(p["end_ym"]))) if p.get("end_ym") else MI_LAST)
        lown[p["id"]] = gids
    ltab = (_fund_windows(_combine(pd.concat(lrec, ignore_index=True), "inv"), "inv", ff, set(), lcut)
            if lrec else pd.DataFrame(columns=["bk", "w", "n"]))
    tick("funds (%d portfolios)" % frec.gid.nunique())
    res = _results(tab, ftab, ltab, lib, lown, load, hdr, frec)
    tick("ranks, tiers, persistence")
    res.update({"lib": lib, "st": st, "M": M, "tab": tab, "ftab": ftab, "ltab": ltab, "frec": frec, "panel": panel,
                "peers": peers})
    return res


def _results(tab, ftab, ltab, lib, lown, load, hdr, frec):
    pools = {"13f": None, "fund": None}
    pools["13f"], bpf = _pools(tab)
    pools["fund"], bpm = _pools(ftab)
    bpools = {"13f": bpf, "fund": bpm}
    libtab = tab[tab.bk < 0]
    bk_of = {v[0]: k for k, v in lib.items()}
    inv = []
    for n, p in enumerate(INV):
        kind = p.get("record_kind")
        d = {"id": p["id"], "name": p.get("name", ""), "grade": p.get("grade"), "kind": kind,
             "style": p.get("primary_style") or "none", "own_docs": int(p.get("own_docs") or 0),
             "explicit_max": p.get("explicit_max"), "explicit_mean": p.get("explicit_mean"),
             "ran_money": p.get("ran_money"), "role": p.get("role", "investor"), "months": 0, "score": np.nan,
             "shares_with": p.get("shares_with") or None,
             "win": {}}
        if kind == "13f" and p["id"] in bk_of:
            t, own = libtab[libtab.bk == bk_of[p["id"]]], lib[bk_of[p["id"]]][1]
        elif kind == "fund" and len(ltab) and p["id"] in set(ltab.bk):
            t, own = ltab[ltab.bk == p["id"]], lown.get(p["id"], set())
        else:
            inv.append(d)
            continue
        for _, r in t.iterrows():
            w = r["w"]
            s = r.to_dict()
            pool = pools[kind][w]
            s["rk"] = _share(pool, s.get("a"), own) if s.get("n", 0) >= MIN_RESULT else np.nan
            d["win"][w] = s
        d["months"] = int(d["win"].get("2011-25", {}).get("n", 0))
        bt = t[t.w.isin(BLOCKS) & (t.n >= MIN_RESULT) & t.a.notna()] if "a" in t else t.iloc[0:0]
        bpos = float((bt.a > 0).mean()) if len(bt) else np.nan
        d["bshare"] = _share(bpools[kind], bpos, own)
        comp = [d["win"].get("2011-25", {}).get("rk", np.nan), d["win"].get("2021-25", {}).get("rk", np.nan),
                d["bshare"]]
        comp = [c for c in comp if c is not None and np.isfinite(c)]
        d["comp"] = comp
        d["score"] = float(np.mean(comp)) if comp else np.nan
        inv.append(d)
    tiers = _tiers(inv)
    # best-scored filers and funds without a library document
    libm = _known_mgrnos()                                   # every filer matched to a library investor
    libg = set(hdr[hdr.crsp_fundno.isin(list(_known_fundnos()))].gid)   # every fund (whole class group)

    def best(tb, kind, exclude, n):
        own_t = tb[~tb.bk.isin(list(exclude))]
        if not len(own_t):
            return []
        sh = {w: _member_shares(pools[kind][w]) for w in ("2011-25", "2021-25")}
        bsh = _member_shares(bpools[kind])
        months = own_t[own_t.w == "2011-25"].set_index("bk").n
        out_ = []
        for bk, m in months.items():
            if (kind == "13f" and bk < 0) or m < MIN_STATS:
                continue
            c = [sh["2011-25"].get(bk, np.nan), sh["2021-25"].get(bk, np.nan), bsh.get(bk, np.nan)]
            cf = [x for x in c if np.isfinite(x)]
            if cf:
                out_.append((float(np.mean(cf)), bk, c))
        out_.sort(key=lambda x: (-x[0], str(x[1])))
        return out_[:n]
    nm = load("eq_sc_names")
    nm = nm.assign(mgrno=nm.mgrno.astype("int64"), d=pd.to_datetime(nm.rdate2, errors="coerce").fillna(
        pd.Timestamp("1900-01-01")), mgrname=nm.mgrname.fillna("").astype(str))
    nm = nm.sort_values(["mgrno", "d"]).drop_duplicates("mgrno", keep="last").set_index("mgrno").mgrname
    tf = [(s, nm.get(bk, str(bk)), c) for s, bk, c in best(tab, "13f", libm, TOP_FILERS)]
    fn = hdr.assign(fund_name=hdr.fund_name.fillna("").astype(str))
    fn = fn.sort_values(["gid", "crsp_fundno"]).drop_duplicates("gid").set_index("gid").fund_name
    tm = [(s, fn.get(bk, bk), c) for s, bk, c in best(ftab, "fund", libg, TOP_FUNDS)]
    pers = {kind: [(b1, b2, _persist(tb, b1, b2)) for b1, b2 in (("2011-15", "2016-20"), ("2016-20", "2021-25"))]
            for kind, tb in (("13f", tab[tab.bk >= 0]), ("fund", ftab))}
    cnt = []
    for w, _, _ in WIN:
        g = tab[(tab.w == w) & tab.grp]
        cnt.append((w, len(g), int(((ftab.w == w) & ftab.grp).sum()) if len(ftab) else 0, g.fv.median(),
                    g.pv.mean() if "pv" in g else np.nan, g.ms.mean() if "ms" in g else np.nan))
    add = _addendum(tab, pools["13f"], bpools["13f"], nm)
    return {"inv": inv, "tiers": tiers, "found": _foundation(), "top_filers": tf, "top_funds": tm,
            "persist": pers, "counts": cnt, "pools": pools, "addendum": add}


def _addendum(tab, pool, bpool, nm):
    """Registration section 13 (Addendum A): filers in the 2021-25 rank group with median matched 13F value over the
    2021-25 filings of $1-30bn and no filer number in any mgrnos / known_mgrnos of the frozen file. List 1: the
    section 7.2 score, 60 months 2011-25 required. List 2: the 2021-25 alpha rank share, 60 months 2021-25 required.
    Sector share and country are not in the stored pulls (msf_v2 siccd and s34names country were not pulled)."""
    t21 = tab[(tab.w == "2021-25") & tab.grp & (tab.bk >= 0)].set_index("bk")
    t11 = tab[(tab.w == "2011-25") & (tab.bk >= 0)].set_index("bk")
    known = _known_mgrnos()
    popn = [bk for bk in t21.index if ADD_LO <= t21.at[bk, "valm"] <= ADD_HI and int(bk) not in known]
    sh11, sh21 = _member_shares(pool["2011-25"]), _member_shares(pool["2021-25"])
    bsh = _member_shares(bpool)
    rows = {}
    for bk in popn:
        c = [sh11.get(bk, np.nan), sh21.get(bk, np.nan), bsh.get(bk, np.nan)]
        cf = [x for x in c if np.isfinite(x)]
        n11 = int(t11.at[bk, "n"]) if bk in t11.index else 0
        r11 = t11.loc[bk] if bk in t11.index else None
        rows[bk] = {"name": str(nm.get(bk, str(bk))), "score": float(np.mean(cf)) if cf else np.nan, "comp": c,
                    "n11": n11, "n21": int(t21.at[bk, "n"]), "a21": t21.at[bk, "a"], "t21": t21.at[bk, "t"],
                    "a11": r11["a"] if r11 is not None and n11 >= MIN_STATS else np.nan,
                    "t11": r11["t"] if r11 is not None and n11 >= MIN_STATS else np.nan,
                    "val": t21.at[bk, "valm"] / 1e9, "np": t21.at[bk, "np"], "to": t21.at[bk, "to"]}
    l1 = sorted([bk for bk, r in rows.items() if r["n11"] >= MIN_STATS and np.isfinite(r["score"])],
                key=lambda bk: (-rows[bk]["score"], int(bk)))[:ADD_N]
    l2 = sorted([bk for bk, r in rows.items() if r["n21"] >= MIN_STATS and np.isfinite(r["comp"][1])],
                key=lambda bk: (-rows[bk]["comp"][1], int(bk)))[:ADD_N]
    return {"pop": len(popn), "rows": rows, "list1": l1, "list2": l2}


# -------------------------------------------------------------------------------------------------- report
def _f(x, fmt, sign=False):
    if x is None:
        return "."
    try:
        if not np.isfinite(float(x)):
            return "."
    except (TypeError, ValueError):
        return "."
    s = (("%+" + fmt[1:]) if sign else fmt) % float(x)
    return s.replace("0.", ".", 1) if fmt.startswith("%.") and abs(float(x)) < 1 and not sign else s


def _wline(pid, w, s, full):
    head = "  %-6s %-7s n%-3d" % (pid, w, int(s.get("n", 0)))
    if not full:
        return head + " rk %s" % _f(s.get("rk"), "%.3f")
    return head + (" a %s t %s r %s rm %s pa %s pv %s dd %s yb %s np %s tw %s to %s p10 %s pn %s fv %s ms %s rk %s"
                   % (_f(s.get("a"), "%.2f", True), _f(s.get("t"), "%.2f", True), _f(s.get("r"), "%.1f", True),
                      _f(s.get("rm"), "%.1f", True), _f(s.get("pa"), "%.2f", True), _f(s.get("pv"), "%.2f"),
                      _f(s.get("dd"), "%.1f"), _f(s.get("yb"), "%.2f"), _f(s.get("np"), "%.0f"),
                      _f(s.get("tw"), "%.2f"), _f(s.get("to"), "%.2f"), _f(s.get("p10"), "%.2f", True),
                      _f(s.get("pn"), "%.2f", True), _f(s.get("fv"), "%.2f"), _f(s.get("ms"), "%.3f"),
                      _f(s.get("rk"), "%.3f")))


def _report_lines(res):
    L = []
    kinds = [p.get("record_kind") for p in INV]
    L.append("EQ SCORECARD %s | registration STAGE0_REGISTRATION.md s.8" % VERSION)
    L.append("code sha256 %s (computed at run time from the module file) | input sha256 %s | pull key %s"
             % (code_sha(), input_sha(), pull_key()[:16]))
    L.append("peer groups: CRSP common shares (EQTY/COM/NS) on NYSE, NYSE American, Nasdaq; foreign-incorporated "
             "and REIT/trust common shares included (registration reading 8)")
    L.append("investors %d (13f %d, fund %d, none %d) | record months %d-%02d..%d-%02d | seal-exempt run"
             % (len(INV), kinds.count("13f"), kinds.count("fund"), kinds.count("none"), M_FIRST // 100,
                M_FIRST % 100, M_LAST // 100, M_LAST % 100))
    L.append("")
    L.append("COUNTS window | filers in rank group | funds in rank group | filed value used (median) | "
             "value with a peer group (mean) | weight without a return (mean)")
    for w, nf, nm, fv, pv, ms in res["counts"]:
        L.append("  %-7s %6d %6d %s %s %s" % (w, nf, nm, _f(fv, "%.3f"), _f(pv, "%.3f"), _f(ms, "%.4f")))
    L.append("")
    L.append("LIBRARY INVESTORS (matched). Columns: n months | a six-factor alpha %/yr | t | r return %/yr (geometric) "
             "| rm minus CRSP VW market | pa peer-adjusted %/yr | pv value share with a peer group | dd worst fall % "
             "| yb share of calendar years ahead of the market | np median positions | tw median weight of ten "
             "largest | to turnover/yr | p10, pn peer-adjusted top-10 / new-positions variants | fv filed value used "
             "| ms weight share without a return | rk rank share. Statistics only where the window or the record "
             "has 60 months; '.' = none")
    for d in res["inv"]:
        if d["kind"] not in ("13f", "fund"):
            continue
        full_rec = d["months"] >= MIN_STATS
        L.append("INV %-6s %-28s | grade %s | %-4s | months %3d | style %s | score %s | components %s"
                 % (d["id"], d["name"][:28], d["grade"], d["kind"], d["months"], d["style"],
                    _f(d["score"], "%.3f"), " ".join(_f(c, "%.3f") for c in d.get("comp", []))))
        for w, _, _ in WIN:
            s = d["win"].get(w)
            if s is None:
                continue
            L.append(_wline(d["id"], w, s, full_rec or s.get("n", 0) >= MIN_STATS))
    nm = {d["id"]: d for d in res["inv"]}
    T = res["tiers"]
    L.append("")
    L.append("TIERS (section 7) | eligible by record %d" % T["eligible"])
    W_ = T.get("with", {})

    def withs(tier):
        return ["  %-6s %-28s with %s (same record, no place)" % (j, nm[j]["name"][:28], t)
                for j, (tr, t) in sorted(W_.items()) if tr == tier]
    L.append("TIER A by record (%d):" % len(T["record"]))
    for i in T["record"]:
        L.append("  %-6s %-28s %-20s score %s" % (i, nm[i]["name"][:28], nm[i]["style"][:20],
                                                 _f(nm[i]["score"], "%.3f")))
    L.extend(withs("record"))
    L.append("TIER A by explicit criteria (%d):" % len(T["explicit"]))
    for i in T["explicit"]:
        L.append("  %-6s %-28s explicit max %s mean %s docs %d" % (i, nm[i]["name"][:28],
                                                                  _f(nm[i]["explicit_max"], "%.0f"),
                                                                  _f(nm[i]["explicit_mean"], "%.2f"),
                                                                  nm[i]["own_docs"]))
    L.extend(withs("explicit"))
    L.append("CONTROL (seed %d, %d): %s" % (SEED, len(T["control"]), " ".join(T["control"])))
    L.extend(withs("control"))
    for k in range(0, max(len(T["B"]), 1), 20):
        L.append(("TIER B (%d): " % len(T["B"]) if k == 0 else "  ") + " ".join(T["B"][k:k + 20]))
    L.extend(withs("B"))
    for k in range(0, max(len(res["found"]), 1), 25):
        L.append(("FOUNDATION documents (%d): " % len(res["found"]) if k == 0 else "  ")
                 + " ".join(str(x) for x in res["found"][k:k + 25]))
    L.append("")
    L.append("BEST-SCORED FILERS WITHOUT A LIBRARY DOCUMENT (score | rank shares 2011-25, 2021-25, blocks)")
    for n, (s, name, c) in enumerate(res["top_filers"], 1):
        L.append("  %2d %-44s %s | %s" % (n, str(name)[:44], _f(s, "%.3f"), " ".join(_f(x, "%.3f") for x in c)))
    L.append("BEST-SCORED FUNDS WITHOUT A LIBRARY DOCUMENT (score | rank shares 2011-25, 2021-25, blocks)")
    for n, (s, name, c) in enumerate(res["top_funds"], 1):
        L.append("  %2d %-44s %s | %s" % (n, str(name)[:44], _f(s, "%.3f"), " ".join(_f(x, "%.3f") for x in c)))
    L.append("")
    L.append("PERSISTENCE (section 9): rank correlation of the six-factor alpha; rows = first-block fifth (1 worst), "
             "columns = second-block fifth 1..5 and 'stopped filing or under 36 months'")
    for kind, lst in res["persist"].items():
        for b1, b2, p in lst:
            L.append("  %-4s %s -> %s | in rank group %d | with both %d | rho %s" % (kind, b1, b2, p["pop"], p["both"],
                                                                                 _f(p["rho"], "%.3f", True)))
            for i in range(5):
                L.append("     %d: %s" % (i + 1, " ".join("%5d" % v for v in p["tbl"][i])))
    L.extend(_addendum_lines(res["addendum"]))
    L.append("END OF SCORECARD")
    return L


def _addendum_lines(A):
    L = ["", "ADDENDUM A (registration section 13): 13F filers in the 2021-25 rank group, median 13F value over the "
             "2021-25 filings $1-30bn (US-listed long book, not firm assets), no filer of the frozen file | "
             "population %d" % A["pop"],
         "  country and largest SIC-division share: not in the stored pulls (s34names country and msf_v2 siccd were "
         "not pulled); left out",
         "  columns: score | rank shares 2011-25, 2021-25, blocks | a21 t21 = 2021-25 six-factor alpha %/yr and t | "
         "a11 t11 = 2011-25 (60 months) | 13F value $bn (median 2021-25) | median positions | turnover/yr"]
    for title, key in (("LIST 1 (registered score, 60 months after 2010; top %d)" % ADD_N, "list1"),
                       ("LIST 2 (2021-25 six-factor alpha rank share, 60 months in 2021-25; top %d)" % ADD_N,
                        "list2")):
        L.append(title + ": %d" % len(A[key]))
        for n, bk in enumerate(A[key], 1):
            r = A["rows"][bk]
            L.append("  %2d %-40s %s | %s | a21 %s t21 %s | a11 %s t11 %s | $%sbn | np %s | to %s"
                     % (n, r["name"][:40], _f(r["score"], "%.3f"), " ".join(_f(x, "%.3f") for x in r["comp"]),
                        _f(r["a21"], "%.2f", True), _f(r["t21"], "%.2f", True), _f(r["a11"], "%.2f", True),
                        _f(r["t11"], "%.2f", True), _f(r["val"], "%.2f"), _f(r["np"], "%.0f"),
                        _f(r["to"], "%.2f")))
    return L


def report(load, out, part=1, parts=1):
    try:
        lines = load("eq_sc_report", keep_default_na=False).line.astype(str).tolist()
    except Exception as e:  # noqa: BLE001
        out("report: not built (%s)" % type(e).__name__)
        return
    chunks, cur, size = [], [], 0
    for x in lines:
        if size + len(x) + 1 > CHUNK and cur:
            chunks.append(cur)
            cur, size = [], 0
        cur.append(x)
        size += len(x) + 1
    if cur:
        chunks.append(cur)
    if part > len(chunks):
        out("[report part %d of %d: empty]" % (part, len(chunks)))
        return
    out("[report part %d of %d]" % (part, len(chunks)))
    for x in chunks[part - 1]:
        out(x)
    if part == parts and len(chunks) > parts:
        out("[%d more parts not printed: add report steps]" % (len(chunks) - parts))
