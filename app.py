"""
app.py
"""
import json
import streamlit as st

st.subheader("This tool helps you generate the Plumber action. \n Please state the three categories you want to classify your form to.")

st.info("💡 **Tip**: These categories should ideally be **mutually exclusive** (i.e. can only belong to one category) and **collectively exhaustive** (i.e. all possibly categories are defined).")


col1, col2 = st.columns([0.3, 0.7])

category_1 = col1.text_input("Category 1")
category_2 = col1.text_input("Category 2")
category_3 = col1.text_input("Category 3")


def generate_payload(category_1, category_2, category_3):
    """
    Generate json
    """
    payload = {
  'messages': [
    {
      'role': 'system',
      'content': f'You will receive feedback. If it is related to {category_1}, reply with 1. If it is related to {category_2}, reply with 2. If it is related to {category_3}, reply with 3.'
    },
    {
      'role': 'user',
      'content': 'PLS_REPLACE_THIS'
    }
  ],
  'max_tokens': 1,
  'logit_bias': {
    '15': 100,
    '16': 100,
    '17': 100
  }
}
    return payload


if col1.button('Generate'):
    if (category_1 == "") or (category_2 == "") or (category_3 == ""):
        st.toast('Please fill in the 3 categories.', icon='⚠️')
    else:
        payload = generate_payload(category_1, category_2, category_3)
        payload_str = json.dumps(payload, indent=4)
        col2.code(payload_str, language='json')
