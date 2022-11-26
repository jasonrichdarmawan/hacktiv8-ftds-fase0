- `FunctionTransformer(func=imp1, feature_names_out=imp1_out)`

  when you do `joblib.dump(value=pipe, filename=file_1)`, the `imp1()` and `imp1_out()` will not be dumped. Therefore, we need a way to dump it as well.

  Do not write the custom function in the `.ipynb` file because the `pipe.pkl` will look for that custom function inside `__main__`.

  Current solution:
  1. Create a custom `.py` file to store the custom function
  2. `from utils import imp` in the `.ipynb` file
  3. `FunctionTransformer(func=imp.imp1, feature_names_out=imp.imp1_out)` in the `.ipynb` file
  4. Copy the `utils` folder to the deployment folder.

  Do not edit the DataFrame args `imp1(df)`. It will edit the original data.

  Use `importlib.reload(imp)` to reload the package everytime there is a change.