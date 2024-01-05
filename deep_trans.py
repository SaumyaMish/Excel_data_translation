import time
import pandas as pd
from deep_translator import GoogleTranslator

start_time = time.time()

# Read the existing file
df = pd.read_excel('order.xls', engine="xlrd")

translated_cols = GoogleTranslator(source='auto', target='en').translate_batch(list(df.columns))
translated_cols

def translate_text(text, target_lang_abbr):
  translated = GoogleTranslator(source='auto', target=target_lang_abbr).translate(text)
  return translated

start = time.time()
rows = []
for index, row in df.iterrows():
  l = []
  for column_name, cell_value in row.items():
    if(type(cell_value) == str):
      translated_cell = translate_text(cell_value, "en")
      # translated_cell = GoogleTranslator(source='auto', target='en').translate(cell_value)
      l.append(translated_cell)
    else:
      l.append(cell_value)
  rows.append(l)
end = time.time()
print(rows[0])
print(f"Time taken for translation {start - end} sec")

translated_df = pd.DataFrame(rows, columns=translated_cols)
print(translated_df.head())

translated_df.to_excel("Order_Export_Translated.xlsx")

# if __name__ == "__main__":
#     file_path = 'order.xls'  # Replace with your file path
#     # translate_excel(file_path)