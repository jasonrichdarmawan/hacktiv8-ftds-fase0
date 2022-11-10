create model from this [Jupyter Notebook](./P1W1D1PM_20221031_FTDS_016_RMT_Machine_Learning_Problem_Framing.ipynb)

run the Web Apps with:
```
$ streamlit run main.py
```

kesalahan batch sebelumnya:
1. error tapi ga tau kenapa ketika deploy ke huggingface.co
   1. nama file harusnya 'app.py'
   2. missing libraries
      'PIL' -> 'pillow'
      'json' -> tidak perlu di requirements.txt
   3. file not exist.