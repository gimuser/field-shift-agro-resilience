# NASA datasets and supporting geospatial data

This directory is the version-controlled **data registry and acquisition workspace** for FIELD SHIFT.

> **Important:** This commit adds dataset specifications and storage conventions, not bulk satellite archives. Large raster/time-series files should be fetched for a defined pilot area and date range, stored outside Git or in Git LFS/object storage, and reproducibly regenerated using documented scripts.

## Collection layout

- `catalog.csv` — machine-readable source register.
- `ACQUISITION_PLAN.md` — access, validation and download plan.
- `raw/` — original downloaded files; ignored by Git.
- `processed/` — clipped/reprojected/aggregated outputs; ignored by Git.
- `samples/` — small, documented examples only; eligible for Git when licensing and size permit.
- `external/` — non-NASA supporting data, with provenance recorded.

## Priority datasets

1. **NASA POWER Daily** — daily meteorological and solar variables for a point or region. The service documents daily time series from 1981 to near-real-time; parameter source and native resolution vary by variable. Do not describe every POWER variable as a direct satellite observation.
2. **GPM IMERG V07B** — precipitation estimates; NASA lists 0.1-degree / roughly 10-km spatial resolution and coverage beginning January 1998. Choose Final for retrospective research, not Early/ Late unless latency is required.
3. **SMAP SPL3SMP_E V006** — daily enhanced Level-3 radiometer soil-moisture product on a 9-km EASE-Grid. Surface soil moisture is not a field-scale measurement and should not be interpreted as soil nutrient content or crop root-zone moisture.
4. **MODIS MOD13Q1 / MYD13Q1** — 16-day vegetation indices at 250 m, useful for seasonal vegetation-condition analysis. Apply quality flags.
5. **ECOSTRESS** — targeted evapotranspiration and land-surface temperature products; high spatial detail but irregular revisit and cloud/coverage limitations. Use as a supplementary layer, not a continuous daily series.

## Supporting (non-NASA) data

- **ISRIC SoilGrids** — gridded soil properties at multiple depths, useful as regional context, not a substitute for field soil tests.
- **FAOSTAT** — country-level agricultural production context; too coarse for individual-farm recommendations.
- **FAO crop calendars / local agronomic sources** — crop calendars and management context, subject to regional validation.
- **Local soil tests and agricultural statistics** — preferred for field-specific nutrient and management information when available.

## Data integrity rules

- Keep original files unchanged in `raw/`; record source URL, product/version, access date, spatial/temporal coverage, units, CRS, license/citation and checksum.
- Preserve quality flags and no-data values.
- Never silently resample or merge products with different spatial/temporal resolutions.
- Keep observation, retrieval, reanalysis, model-derived estimate and in-situ measurement labels distinct.
- Do not train an ML model until suitable labels/targets, leakage-safe validation and geographic/temporal coverage have been assessed.
- Do not generate crop recommendations from satellite variables alone.

## Pilot scope

The pilot geography and date range have not yet been confirmed. Therefore no region-specific raster downloads are included in this initial commit.
