# Dataset acquisition and validation plan

## 1. Scope gate before downloading

Before acquiring geospatial files, confirm:
- pilot region polygon or farm coordinates;
- analysis period (recommended initial historical window: at least 5-10 years where product coverage allows);
- intended temporal aggregation (daily, dekadal, monthly, seasonal);
- whether the workflow uses NASA Earthdata, Google Earth Engine, AppEEARS or direct APIs;
- storage budget and whether large data will live in object storage / Git LFS rather than normal Git.

No region-specific downloads are made until this scope is confirmed.

## 2. Acquisition order

### Tier 1 — core environmental time series
1. NASA POWER daily point time series: temperature, precipitation, humidity and solar radiation variables after checking the API parameter dictionary and units.
2. GPM IMERG V07B Final daily/monthly precipitation for spatial precipitation patterns and cross-checking POWER.
3. SMAP SPL3SMP_E V006 surface soil-moisture product with quality flags.
4. MODIS MOD13Q1 (and optionally MYD13Q1) NDVI/EVI with quality filtering.

### Tier 2 — targeted supplementary products
5. ECOSTRESS evapotranspiration / land-surface temperature, only where usable scenes overlap the pilot and dates.
6. SoilGrids regional soil properties, documenting depth and uncertainty.
7. Field soil tests, crop calendars, local crop statistics and farmer constraints.

## 3. Recommended derived features (not raw model labels)

- rainfall totals by crop-relevant season;
- number/duration of dry spells using a documented rainfall threshold;
- temperature maxima and heat-day counts using crop-specific thresholds from agronomic sources;
- SMAP surface-soil-moisture seasonal median/anomaly;
- MODIS NDVI/EVI seasonal median, peak and anomaly;
- ECOSTRESS ET where sampling supports the analysis;
- soil texture, pH and organic-carbon context from SoilGrids or field tests.

Thresholds must be sourced and crop/region-specific. Do not invent universal drought or heat thresholds.

## 4. Validation checks

For every downloaded product:
- verify product ID, collection/version and temporal coverage;
- inspect CRS, transform, dimensions, units and scale/offset;
- retain QA/quality masks;
- check missing-data fraction and spatial coverage over the pilot;
- compare overlapping precipitation/temperature products where appropriate;
- compare gridded soil properties against field tests if available;
- record processing code version and checksums.

## 5. Storage policy

- `raw/`: original immutable source files; gitignored.
- `processed/`: reproducible derivatives; gitignored unless small and intentionally curated.
- `samples/`: tiny sample files with source, date, licence and checksum documented.
- Commit scripts, metadata, schemas, documentation and tests—not multi-gigabyte raw archives.
- For large curated artifacts, evaluate Git LFS or an object store and document access credentials separately. Never commit Earthdata passwords, tokens or API keys.

## 6. Modeling gate

NASA datasets are predictors, not automatically labels. Before ML:
- define the target (e.g., independently observed crop stress / yield anomaly / validated vegetation stress proxy);
- establish independent labels and their provenance;
- check spatial and temporal alignment;
- use time-blocked and geographic holdouts;
- compare simple baselines before Random Forest/XGBoost;
- report calibration, error, uncertainty and applicability limits.

## 7. Official source references

- NASA POWER Daily API: https://power.larc.nasa.gov/docs/services/api/temporal/daily/
- GPM IMERG data directory: https://gpm.nasa.gov/data/directory
- SMAP SPL3SMP_E V006: https://nsidc.org/data/spl3smp_e/versions/6
- MODIS vegetation indices: https://modis.gsfc.nasa.gov/data/dataprod/mod13.php
- ECOSTRESS data: https://ecostress.jpl.nasa.gov/data
- SoilGrids: https://soilgrids.org/
- FAOSTAT: https://www.fao.org/faostat/

## Current status

Catalog and plan only. Pilot boundary, date range and access workflow are pending confirmation.
