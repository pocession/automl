# This is a web-based app to predict the cell type base on single-cell omics data.

## How to use

- Go to [here](https://pocession-automl-app-streamlit-lunch-2ob4cw.streamlit.app/) and upload your metrics data. Run the `ML` function and download the trained model.

## Notes

### 2022/12/28

- The web-based app is now hosted in [streamlit cloud](https://pocession-automl-app-streamlit-lunch-2ob4cw.streamlit.app/).

### 2022/12/27

- Currently it supports only mono-omics data (e.g. scRNAseq, scATACseq).
- The app needs `pycaret` but M1 Mac does not support this package.
- I follow a [tutorial](./DidNotWorkInM1/pycaret_installation_guide.md) but it did not work. I then archive the files in [here](./DidNotWorkInM1/).
- In the final, I develop and run the app by [colab notebook](./colab_automl_dev.ipynb). I lunch the app in [local](http://172.28.0.12:8501) or [in public link](http://d22e-35-231-228-144.ngrok.io).
- I use [ngrok](https://ngrok.com/) to create a public link and use [localtunnel](https://www.npmjs.com/package/localtunnel) to create a local link.

## Future updates

- Run scRNA-seq data as sample data.
- Support `prediction` function.
- Support multi-omics data.
