# language-identification-survey
Live survey of off-the-shelf language identification tools for python

## Reproducing benchmark

### 1. Download the dataset
```bash
./datasets/tatoeba-sentences-2021-06-05/download
```

### 2. Run the language inference for benchmarks

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
docker run -v `pwd`:/src -t -i bench python /src/run.py <benchmark_name>
```

### 3. Run analysis
```bash
python analyze.py --correctness
python analyze.py --timings
```
