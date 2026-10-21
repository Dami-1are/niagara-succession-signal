# Week 6 - Succession Benchmark Table and Proxy Register

## Purpose and scope

This layer keeps Ontario Statistics Canada succession survey estimates and Canadian Federation of Independent Business (CFIB) national survey evidence separate from Niagara-specific observations. Ontario and Canada values are benchmarks, not measured Niagara rates.

## Reproducibility

Run `python src/build_succession_benchmarks.py`. The script reads the four cleaned Ontario StatCan tables, the structured 13-row CFIB table and the sector crosswalk. It does not edit `data/raw/`.

## Ontario StatCan benchmark

All 3,332 source rows are retained (476 + 476 + 1,360 + 1,020). Survey values remain percentages and reference year 2026 is preserved.

- `STATUS == F`: `value_status=suppressed`; value remains missing because the estimate is too unreliable to publish.
- `STATUS == ..`: `value_status=not_available`; value remains missing because it is unavailable for the reference period.
- Original status codes are retained in `quality_flag`.
- `E` rows are flagged with `caution_flag=True`; `D` rows are not flagged unless the project lead confirms otherwise.
- Suppressed or unavailable values are never imputed or replaced with zero.
- Source size bins are retained in the measure label and are not forced into incompatible standard size bands.

## CFIB benchmark

All 13 CFIB rows are retained, including population, source page and notes. The evidence is from Canada in 2022, not Niagara or Ontario. Where the source permits multiple responses, categories must not be treated as mutually exclusive.

## Proxy register

The register documents the ten proxies in the Week 6 specification. It distinguishes indirect proxies from demographic context and provincial/national benchmarks. Self-employment is not described as a direct business-owner count; population age is not owner age; business exits are not automatically succession-related closures.

## Limitations and decisions to confirm

1. There is no direct Niagara succession variable or Niagara business-owner age in this layer.
2. NEI inventory turnover is an indirect inventory-change signal, not a closure rate or succession measure.
3. Ontario survey results and national CFIB evidence must not be presented as Niagara rates.
4. The `D` and `E` caution treatment is provisional and requires confirmation.
5. NEI licensing and redistribution permission remain unresolved; do not redistribute NEI source records until licensing is confirmed.
6. Small-cell modelling rules remain open in the draft specification.

## Validation

The builder checks expected row counts for each StatCan input, the combined 3,332-row total, the 13-row CFIB total, and that F/.. values remain missing. Outputs are written under `data/processed/layer/`.
