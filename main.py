import streamlit as st
import requests
import pandas as pd
import json
import time

if __name__ == '__main__':
    st.subheader('Azure function - Cassandra data to Azure blob')
    query_text = st.text_area('Query text:','SELECT * FROM thingsboard.ts_kv_cf LIMIT 5')
    blob_store = st.selectbox("Want to store data in azure blob?", ("True", "False"))
    if st.button('Start'):
        tStart = time.time()
        st.write("Query text: {}".format(query_text))
        st.write("Blob storage: {}".format(blob_store))
        payload = {'query_text': query_text, 'blob_store': blob_store}
        answer = json.loads(requests.get('http://192.168.33.10:8080/api/service', params=payload).text)
        tEnd = time.time()

        if blob_store == "True":
            st.write("Finish store the data into azure blob.")
        st.dataframe(pd.DataFrame(json.loads(answer['data'])))

        st.write("Download Link: {}".format(answer['url']))
        st.write("Spend time: {} seconds.".format(tEnd-tStart))
        # st.dataframe(pd.DataFrame.from_dict(answer, orient='columns'))