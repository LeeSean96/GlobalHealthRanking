# US Clinical Trial Registry Analysis Helper

This is a tool that digests the raw public registry data and generates a CSV file that displays interventional trials and information relevant to them. This tool was primarily built for UAEM (http://www.uaem.org/) members to quickly assess compliance of research bodies conducting clinical trials to the Declaration of Helsinki in an effort to promote transparency in medical research.

### Prerequisites

The software requires only Python 3.4 =< to run. This can be obtained at "https://www.python.org/download/releases/3.0/".

It is recommended to also get OpenRefine to aid in reconciliating the data.


### How To

1. To use this tool, clone or fork this repository.

2. Make a folder "data" in the directory where "parser.py" sits.

3. Obtain your dataset from [ClinicalTrialsGov (Download all data)](https://clinicaltrials.gov/ct2/resources/download#DownloadAllData) and unzip it in the "Data" directory.

4. Open up your console or IDLE and type "python3 parser.py" or "python parser.py"

```
user@Desktop:~/GlobalHealthRanking$ python3 parser.py
```

5. A CSV file will appear in the same directory as "parser.py" after an hour. 

6. Filter and study the data as desired using OpenRefine or Excel. (Excel will be noticeably slower, we recommend using OpenRefine to further select and bin your data before processing it with Excel).

## Built With

* [Python3](https://www.python.org/download/releases/3.0/)


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.


## Authors

* **Yi Nian Lee (Sean)** - [LeeSean96](https://github.com/LeeSean96)
* **Till Bruckner**  - [Transparimed](https://www.transparimed.org/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


