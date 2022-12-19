# streamlit_qrcode_scanner

A Qrcode Scanner with back camera as default  
Use https://github.com/mebjas/html5-qrcode


## Example:

import streamlit as st  
from streamlit_qrcode_scanner import qrcode_scanner  

qr_code = qrcode_scanner(key='qrcode_scanner')  

if qr_code:  
  st.write(qr_code)  
