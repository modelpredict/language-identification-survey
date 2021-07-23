# language-identification-survey
Live survey of off-the-shelf language identification tools for python

## Reproducing benchmark

### 1. Run the language inference for benchmarks

Available benchmarks:
- fasttext
- fasttext-compressed
- gcld3
- langdetect
- langid
- pycld2

On the host machine.
```bash
python run.py <benchmark_name>
```

In docker:
```bash
docker build -t bench .
docker run -v `pwd`:/src -t -i python /src/run.py <benchmark_name>
```

### 2. Generate results markdown files
```bash
python benchmark_analysis.py
```
