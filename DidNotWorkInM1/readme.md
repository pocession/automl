### Install of pycaret in M1 mac needs some extra efforts. Check the link below.

### https://pareekshithkatti.medium.com/setting-up-python-for-data-science-on-m1-mac-ced8a0d05911

1. Step1: `pip install --no-dependencies pycaret`
2. Step2: `cat pycaret_requirements.txt | xargs -n 1 conda install`
3. For all the packages that did not get installed, please pip install it.
4. Step3: `brew install cmake libomp`
5. Step4: `pip install xgboost --no-binary xgboost -v`

### However, eventually, it still does not work on my M1 Mac.
