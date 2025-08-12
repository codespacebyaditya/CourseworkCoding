# Methods in Bioinformatics Coursework Repository

**Course:** BINF 6308 & BINF 6309 - Methods in Bioinformatics  
**Institution:** Northeastern University (NEU)  
**Repository:** This repository contains all coursework, assignments, and projects completed during the Methods in Bioinformatics course sequence.

## Overview

This repository houses comprehensive coursework covering fundamental bioinformatics methods, tools, and pipeline development. The course sequence (BINF 6308 & BINF 6309) provides hands-on experience with essential bioinformatics workflows, from basic sequence analysis to advanced genomic data processing.

## Repository Structure

### Core Bioinformatics Scripts
- **Sequence Analysis**: `sliding_window.py`, `sliding_window_fasta.py`, `hamming.py`
- **File Processing**: `parse_file.py`, `open_file.py`, `write_file.py`, `headers_to_file.py`
- **Sequence Manipulation**: `transcribe.py`, `translate.py`, `translate_APOE.py`, `interleave.py`
- **Data Processing**: `concatenate.py`, `count_aip_kmer.py`, `create_seq.py`

### Bioinformatics Pipelines & Workflows
- **Genome Assembly**: `quast.sh`, `spades.sh`, `alignSpades.sh`
- **Sequence Alignment**: `alignAll.sh`, `alignReads.sh`, `alignPredicted.sh`
- **Read Processing**: `getReads.sh`, `indexReads.sh`, `trim.sh`
- **Genome Analysis**: `getGenome.sh`, `indexGenome.sh`, `buildIndex.sh`
- **Protein Analysis**: `blastPep.sh`, `predictProteins.sh`, `pfamScan.sh`

### R-based Analysis
- **Statistical Analysis**: `markov_chains.R`, `de.R`, `mergeAll.R`, `mergeKo.R`
- **Data Visualization**: `markov_plots.pdf`
- **R Markdown Reports**: `methodResults.Rmd`, `citeExample.Rmd`, `MethodsVariantCalling.Rmd`

### Testing & Validation
- **Unit Tests**: `test_basic_functions.py`, `test_fibonacci.py`, `test_hamming.py`
- **Test Scripts**: Various `.sh` test files for automated testing
- **Test Outputs**: Sample output files for validation

### Data Files
- **Sequence Data**: `newfasta`, `apoe_aa.fasta`, `APOE_refseq_transcript.fasta`
- **Annotation Data**: `tx2gene.csv`, `deAnnotated.csv`, `dfAll.csv`
- **Reference Data**: `ko`, `markov`, `gms.out`

### Documentation & Reports
- **HTML Reports**: `MethodsVariantCalling.html`, `citeExample.html`
- **Bibliography**: `bibliography.ris`, various PMC reference files

## Key Learning Objectives

### BINF 6308 - Foundation Methods
- Basic Python programming for bioinformatics
- Sequence analysis algorithms and implementations
- File parsing and data manipulation
- Introduction to bioinformatics pipelines

### BINF 6309 - Advanced Applications
- Advanced sequence analysis and alignment
- Statistical analysis using R
- Pipeline development and automation
- Genomic data processing workflows
- Variant calling and analysis

## Technologies & Tools Covered

- **Programming Languages**: Python, R, Bash
- **Bioinformatics Tools**: BLAST, SPAdes, QUAST, Pfam
- **Data Formats**: FASTA, CSV, RIS, HTML
- **Analysis Platforms**: R Markdown, Jupyter notebooks
- **Version Control**: Git

## Getting Started

### Prerequisites
- Python 3.x
- R with bioinformatics packages
- Common bioinformatics tools (BLAST, SPAdes, etc.)
- Bash shell environment

### Running Scripts
Most Python scripts can be run directly:
```bash
python script_name.py
```

Shell scripts require execution permissions:
```bash
chmod +x script_name.sh
./script_name.sh
```

R scripts can be run in R or RStudio:
```r
source("script_name.R")
```

## Course Structure

The coursework is organized to build progressively from basic concepts to advanced applications:

1. **Basic Programming** - Python fundamentals, file I/O, data structures
2. **Sequence Analysis** - Algorithms for DNA/RNA/protein analysis
3. **Pipeline Development** - Shell scripting and workflow automation
4. **Statistical Analysis** - R-based data analysis and visualization
5. **Advanced Applications** - Real-world bioinformatics problems

## Contributing

This is a personal coursework repository. All code and materials are original work completed as part of the BINF 6308/6309 course sequence at Northeastern University.

## License

This repository contains educational materials and coursework. Please respect academic integrity and do not copy or redistribute without proper attribution.

## Contact

For questions about the coursework content, please refer to the course materials or contact the course instructor at Northeastern University.

---

*Last updated: [Current Date]*  
*Course: BINF 6308 & BINF 6309 - Methods in Bioinformatics*  
*Institution: Northeastern University*
