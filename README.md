# language-identification-survey
Live survey of off-the-shelf language identification tools for python

## GCLD3
```bash
cd models/gcld3
./copy_dataset.sh
docker build -t gcld3 .
docker run -v `pwd`:/src -t -i gcld3 python /src/run.py
```

