# JRC-PPDB-OPEN

This is an edited version of the JRC Open Power Plants Database (JRC-PPDB-OPEN) based on v. 1.0.

The datapackage (both data and metadata) has been modified and is now valid.

The original version can be found here:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3574566.svg)](https://doi.org/10.5281/zenodo.3574566)

Authors: Kanellopoulos K.; De Felice M.; Hidalgo Gonzalez I.; Bocin A.

License: [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/legalcode)

## Main modifications

- Regex pattern constraints related to IDs and names have been removed when these prevented validation

- Enums have been made consistent in capitalization

- Constraints on `ramp_down`changed from [0,1] to [-1,0]

- Removed data for fields `co2emitted`, `cf`, `Generation` when not meeting the constraints

- Removed extra fields `water_withdrawal`,`water_consumption` not present in the metadata

See the diff to check the changes on the `datapackage.json` and the script `mod.py` for those on the data.
