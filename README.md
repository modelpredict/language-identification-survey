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

Available datasets:
- tatoeba-sentences-2021-06-05
- tatoeba-sentences-2021-06-05-common-48
- open-subtitles-v2018-100k-per-lang

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

### 4. Get memory usage for different models
```bash
python get_memory_usage.py <benchmark_names>
# e.g. python get_memory_usage.py fasttext
# e.g. python get_memory_usage.py fasttext-compressed
```

It will print memory usage in MB (bytes/1024/1024).
