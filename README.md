# LAAPSI Processing

Repo for processing LAAPSI. For official content, see [colingorrie/laapsi](https://github.com/colingorrie/laapsi).

## Contributors

- Seumas Macdonald
- James Tauber
- Colin Gorrie

## Directory Layout

So far, the only data directories being manually modified are:

- `orig` (the original files from Colin)
- `manual-data` (data needed for processing, e.g. lemma overrides from Colin)

The main output directories are:

- `text` (the processed text in GLTP format)
- `analysis` (further analysis of the text in GLTP format)

Other directories are:

- `cache` (for storing the Morpheus cache)
- `config` (for storing configuration like for text-validation)
- `scripts` (where all the code lives)

## Scripts

The scripts are run in this order (after dependencies in the Pipfile are installed):

- `./scripts/orig-to-para.py` converts from `orig` files to `para` files under `text`
- `./scripts/para-to-sent.py` converts those `para` files to sentence-based `sent` files
- `./scripts/add-norm.py` produces the `norm` files in `analysis` from the `sent` files
- `./scripts/lemmatise.py` produces the `lemma` files in `analysis` from the `norm` files using Morpheus and `manual-data/lemma_overrides.yaml`

The folowing are modules not called from the command-line:

- `morpheus.py` (Morphology API client)
- `utils.py` (common functions shared between scripts)

Other scripts include:

- `sort-yaml.py <filename>` sorts the given yaml file with top-level keys in alphabetical order

## License

The content is CC-BY-SA and the code is MIT.
