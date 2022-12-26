# This is a web-based app to predict the cell type base on single-cell omics data.

## How to use

- Go to [here]() and upload your metrics data. Run the `ML` function and download the trained model.

## Notes

- Currently it supports only mono-omics data (e.g. scRNAseq, scATACseq).
- The app needs `pycaret` but M1 Mac does not support this package.
- I follow a [tutorial](./DidNotWorkInM1/pycaret_installation_guide.md) but it did not work. I then archive the files in [here](./DidNotWorkInM1/).
- In the final, I develop and run the app by [colab notebook](./colab_automl_dev.ipynb) and [ngrok](https://dashboard.ngrok.com/get-started/setup).
- The web-based app is now hosted in [streamlit cloud]().

## Future updates

- Support `prediction` function.
- Support multi-omics data.
