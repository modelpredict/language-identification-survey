# language-identification-survey
Live survey of off-the-shelf language identification tools for python

## Running
```bash
docker build -t bench .
docker run -v `pwd`:/src -t -i python /src/run.py fasttext-compressed
```
