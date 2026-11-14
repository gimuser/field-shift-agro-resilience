# NASA datasets and supporting inputs

This directory is the version-controlled **data registry and acquisition workspace** for FIELD SHIFT. The catalogue is restricted to the NASA dataset families named in the challenge brief, plus closely related NASA elevation products that clarify the phrase "SRTM or other NASA elevation products".

> **Important:** This commit records products and acquisition guidance; it does not contain bulk satellite archives. Large raster/time-series files should be fetched for a defined area and date range, stored outside ordinary Git or in Git LFS/object storage, and reproducibly regenerated using documented scripts.

## Collection layout

- `catalog.csv` — machine-readable register of challenge-listed NASA products and elevation candidates.
- `ACQUISITION_PLAN.md` — product selection, access, validation and download plan.
- `raw/` — original downloaded files; ignored by Git.
- `processed/` — clipped/reprojected/aggregated outputs; ignored by Git.
- `samples/` — small, documented examples only; eligible for Git when licensing and size permit.
- `external/` — reserved for local soil information, crop characteristics and farmer-provided priorities. These are supporting inputs, not additional NASA satellite datasets.

## NASA datasets named in the challenge

1. **SMAP** — surface soil-moisture retrievals; useful for regional wetness/dryness context, not soil nutrients or field-scale root-zone moisture.
2. **ECOSTRESS** — evapotranspiration and land-surface temperature products; valuable for plant-water-use/heat context where usable observations exist, but sampling is irregular.
3. **GPM** — precipitation estimates, including IMERG; useful for rainfall totals, intensity and extreme precipitation analysis.
4. **Landsat** — multispectral surface reflectance and thermal observations; useful for vegetation condition, land-surface temperature and field-scale change analysis. Select a specific Landsat collection/product and QA policy before processing.
5. **MODIS** — frequent vegetation and land-surface observations; useful for seasonal vegetation indices and anomalies, with coarser spatial detail than Landsat.
6. **NASA POWER** — meteorological and solar time series. Parameter provenance and native spatial resolution vary; do not describe every parameter as a direct satellite observation.
7. **GRACE and GRACE-FO** — large-scale terrestrial water-storage anomalies; useful for long-term groundwater/water-resource context, not individual-field soil moisture.
8. **SRTM and other NASA elevation products** — elevation, slope, terrain position and drainage/topographic context.

## What "other NASA elevation products" can mean

The strongest candidates to register alongside SRTM are:

- **NASADEM_HGT V001** — NASA's reprocessed SRTM-derived global DEM at 1 arc-second spacing (about 30 m). It uses improved processing and auxiliary control data to reduce voids and improve geolocation. This is the best first alternative to compare with the original SRTM.
- **NASADEM_SC V001** — slope and curvature derivatives at 1 arc-second spacing, derived from NASADEM. Useful for terrain steepness and landform context; these are derivatives, not a separate elevation observation.
- **ASTER GDEM V3 (ASTGTM.003)** — global ~30 m DEM derived from stereo imagery from Terra's ASTER instrument. Useful as an independent comparison/backup, but can contain artifacts and should be quality-checked.
- **GEDI L2A (GEDI02_A)** — lidar footprint measurements including ground elevation and canopy-height metrics, with approximately 25 m footprint size. It is sampled along tracks, not a continuous wall-to-wall DEM.
- **GEDI L3 Gridded Land Surface Metrics** — 1 km grid summaries including mean ground elevation and canopy-height metrics. Useful for broad ecosystem/terrain context, not field-boundary elevation.
- **SRTM** — the original Shuttle Radar Topography Mission elevation product explicitly named in the challenge.

**Recommended choice:** start with SRTM/NASADEM at ~30 m for terrain analysis. Add ASTER GDEM as a comparison where needed. Treat GEDI as a supplementary sampled canopy/ground-height source, not as a replacement DEM. Use NASADEM slope/curvature as derived terrain layers if erosion/runoff context is part of the model.

## Supporting inputs explicitly contemplated by the challenge

- Local soil information (prefer measured field/laboratory data where available).
- Crop characteristics and crop calendars, with source and region recorded.
- Farmer priorities such as water use, forage value, nitrogen-fixing potential, erosion reduction, organic matter improvement and market suitability.

These inputs should be represented transparently and should not be mislabeled as NASA observations. No additional third-party gridded soil or national-statistics datasets are included in this challenge-scoped catalogue at this stage.

## Data integrity rules

- Keep original files unchanged in `raw/`; record source URL, product/version, access date, spatial/temporal coverage, units, CRS, license/citation and checksum.
- Preserve QA/quality flags and no-data values.
- Never silently resample or merge products with different spatial/temporal resolutions.
- Keep observation, retrieval, reanalysis, model-derived estimate and in-situ measurement labels distinct.
- Do not train an ML model until suitable labels/targets, leakage-safe validation and geographic/temporal coverage have been assessed.
- Do not generate crop recommendations from satellite variables alone.

## Download scope

No region-specific raster downloads are included yet. The study boundary and date range are still unconfirmed. The NASA products and candidate elevation datasets are now catalogued independently of any pilot-region choice.
