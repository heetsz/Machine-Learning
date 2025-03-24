import streamlit as st
import pandas as pd
import numpy as np

st.title("hello streamlit")
st.write("simple text")
df = pd.DataFrame({
      'col 1': [1,2,3,4,5],
      'col 2': [12,234,33234, 23, 43]
})

st.write("this is the dataframe")
st.write(df)

chart_data = pd.DataFrame(
      np.random.randn(20, 3), columns = ['a', 'b', 'c']
)
st.line_chart(chart_data)

#streamlit run app.py