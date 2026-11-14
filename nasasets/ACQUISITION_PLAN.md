# NASA dataset acquisition and validation plan

## 1. Scope gate before downloading

Before acquiring geospatial files, define:
- study boundary (polygon, watershed, administrative area or farm locations);
- analysis period and seasonal windows;
- intended temporal aggregation (daily, 16-day, monthly, seasonal);
- required spatial scale and whether analysis is field, landscape, basin or regional;
- access workflow (NASA Earthdata, LP DAAC AppEEARS, GES DISC, PO.DAAC, USGS or APIs);
- storage budget and whether large data will live in object storage / Git LFS rather than ordinary Git.

No region-specific bulk downloads are made until the study boundary and date range are defined.

## 2. Challenge-listed NASA datasets

### Climate and water
1. **NASA POWER** — daily meteorological/solar parameters. Confirm each parameter's units, provenance and native resolution; not every parameter is a direct satellite observation.
2. **GPM IMERG** — precipitation rate/accumulation. Use Final for retrospective analysis; Early/ Late products are for lower-latency use cases.
3. **GRACE / GRACE-FO** — monthly terrestrial water-storage anomalies for basin/regional long-term water trends. Do not interpret these as field-scale groundwater or soil moisture.

### Soil moisture and thermal stress
4. **SMAP** — surface soil-moisture retrievals with QA. Do not interpret as nutrient content or direct field root-zone moisture.
5. **ECOSTRESS** — evapotranspiration and land-surface temperature/stress products. Sampling is irregular; choose exact products based on the intended variable and coverage.

### Vegetation and land-surface observations
6. **Landsat Collection 2 Level-2** — surface reflectance and surface temperature; useful for field-scale change where cloud-free observations exist. Preserve QA masks.
7. **MODIS vegetation indices** — MOD13Q1/MYD13Q1 NDVI/EVI at 250 m, 16-day composites; useful for seasonal regional monitoring. Preserve quality flags.

### Elevation and terrain
8. **SRTM** — original radar-derived terrain elevation, nominally 1 arc-second (~30 m) for the global product.
9. **NASADEM_HGT V001** — reprocessed SRTM-derived ~30 m DEM; recommended first DEM to test alongside SRTM.
10. **NASADEM_SC V001** — slope/curvature derivatives from NASADEM, useful for terrain and erosion/runoff screening.
11. **ASTER GDEM V3 (ASTGTM.003)** — independent stereo-derived ~30 m DEM for comparison; inspect artifacts.
12. **GEDI L2A / L3** — sampled ground elevation and canopy-height information. GEDI is not a continuous wall-to-wall DEM and should be supplementary.

## 3. What to acquire first

A practical first data stack, once the region is selected:
- NASA POWER daily time series for temperature/rainfall/solar variables.
- GPM IMERG Final daily precipitation.
- SMAP daily surface soil moisture.
- MODIS 16-day NDVI/EVI.
- Landsat Collection 2 Level-2 for finer spatial/thermal analysis where cloud cover allows.
- NASADEM or SRTM for elevation, then derive slope/aspect/terrain attributes.
- ECOSTRESS where useful overpasses/products exist.
- GRACE/GRACE-FO only for basin/region-scale long-term water-storage context.
- ASTER GDEM and GEDI only where they answer a specific terrain/canopy question.

Do not download every product at maximum resolution by default. Select products according to the question, scale, temporal overlap and storage budget.

## 4. Supporting non-satellite inputs from the challenge

Collect separately and label their provenance:
- local soil information (field/laboratory measurements preferred for nutrients and organic matter);
- crop characteristics (water use, rooting depth, duration, heat/frost sensitivity, forage value, nitrogen-fixing potential);
- farmer priorities and constraints (water availability, erosion reduction, organic matter, market suitability, management capacity).

These are contextual inputs, not NASA satellite datasets. Do not infer nitrogen, phosphorus, potassium or organic matter directly from SMAP, GRACE or elevation data.

## 5. Candidate derived features

- rainfall totals, intensity, extreme-rainfall indicators and dry-spell duration;
- heat-day counts and temperature anomalies using crop-specific, sourced thresholds;
- SMAP soil-moisture seasonal medians/anomalies;
- ECOSTRESS evapotranspiration and thermal-stress indicators where sampling supports it;
- Landsat/MODIS vegetation-index seasonal curves and anomalies;
- GRACE/GRACE-FO monthly water-storage anomalies at basin scale;
- DEM elevation, slope, aspect, curvature, topographic wetness/drainage proxies and erosion-screening variables.

Do not treat derived indices as ground truth. Record formulas, units, thresholds, quality filters and spatial/temporal aggregation.

## 6. Validation checks

For every product:
- verify product ID, collection/version, temporal coverage and access date;
- inspect CRS, transform, dimensions, units, scale/offset and vertical datum for DEMs;
- retain QA/quality masks and no-data values;
- check missing-data fraction and spatial coverage;
- compare overlapping products only after matching units, support and time windows;
- inspect DEM voids, water artifacts, slope outliers and source layers;
- record processing code version, provenance and checksums.

## 7. Storage policy

- `raw/`: original immutable source files; gitignored.
- `processed/`: reproducible derivatives; gitignored unless small and intentionally curated.
- `samples/`: tiny sample files with source, product/version, date, licence/citation and checksum.
- Commit scripts, metadata, schemas, documentation and tests—not multi-gigabyte raw archives.
- Use Git LFS or object storage for large curated artifacts where appropriate.
- Never commit Earthdata passwords, tokens or API keys.

## 8. Modeling gate

NASA datasets are predictors/context, not automatically ML labels. Before ML:
- define a defensible target (independent crop-stress observations, yield records, field measurements or a clearly named proxy);
- document target provenance and limitations;
- check spatial and temporal alignment;
- use time-blocked and geographic holdouts;
- compare simple baselines before Random Forest/XGBoost;
- report calibration, errors, uncertainty and applicability limits.

## 9. Official references

- NASA POWER Daily API: https://power.larc.nasa.gov/docs/services/api/temporal/daily/
- GPM data directory: https://gpm.nasa.gov/data/directory
- SMAP SPL3SMP_E V006: https://nsidc.org/data/spl3smp_e/versions/6
- ECOSTRESS: https://ecostress.jpl.nasa.gov/data
- Landsat Collection 2: https://www.usgs.gov/landsat-missions/landsat-collection-2
- MODIS vegetation indices: https://modis.gsfc.nasa.gov/data/dataprod/mod13.php
- GRACE/GRACE-FO data: https://grace.jpl.nasa.gov/data/get-data/
- NASADEM User Guide: https://lpdaac.usgs.gov/documents/2237/NASADEM_User_Guide_V13.pdf
- NASADEM slope/curvature: https://data.nasa.gov/dataset/nasadem-slope-and-curvation-global-1-arc-second-v001
- ASTER/SRTM DEM comparison guide: https://lpdaac.usgs.gov/documents/642/DEM_Comparison_Guide.pdf
- GEDI L2A V002: https://data.nasa.gov/dataset/gedi-l2a-elevation-and-height-metrics-data-global-footprint-level-v002
- GEDI L3 V2: https://data.nasa.gov/dataset/gedi-l3-gridded-land-surface-metrics-version-2

## Current status

The catalogue now follows the NASA dataset families named in the challenge prompt and identifies additional NASA elevation products. No regional data files have been downloaded because no study boundary or date range has been selected.
