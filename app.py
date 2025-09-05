import os
import io
import numpy as np
import pandas as pd
import streamlit as st
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Automation & Search Assistant")

st.title("Excel/CSV Automation and Document Search Assistant")

# Tabs for features
excel_tab, doc_tab = st.tabs(["Excel/CSV Assistant", "Document Search"])

with excel_tab:
    st.header("Excel/CSV Automation")
    uploaded_file = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"])
    instruction = st.text_area("Describe the task",
        placeholder="e.g., sort by total sales and keep top 10 rows")
    if st.button("Run", key="excel_run") and uploaded_file and instruction:
        # Load DataFrame
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        prompt = (
            "You are a Python data assistant. Given a pandas DataFrame named df, "
            "write python code using pandas to perform the user's task. "
            "Assign the final DataFrame to a variable named result_df. "
            "Return only the code." )
        try:
            resp = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system", "content": prompt},
                          {"role": "user", "content": instruction}]
            )
            code = resp.choices[0].message["content"]
            st.subheader("Generated code")
            st.code(code, language="python")

            local_env = {"df": df}
            exec(code, {}, local_env)
            result_df = local_env.get("result_df", df)
            st.subheader("Result")
            st.dataframe(result_df)
        except Exception as e:
            st.error(f"Error: {e}")

with doc_tab:
    st.header("Search and Summarize Documents")
    docs = []
    uploaded_docs = st.file_uploader("Upload text files", type=["txt"], accept_multiple_files=True)
    if uploaded_docs:
        for f in uploaded_docs:
            text = f.read().decode("utf-8", errors="ignore")
            emb = openai.Embedding.create(input=text, model="text-embedding-3-small")
            docs.append({"name": f.name, "text": text, "embedding": np.array(emb["data"][0]["embedding"])})
        st.success(f"Loaded {len(docs)} documents.")

    query = st.text_input("Search query")
    if st.button("Search", key="doc_search") and query and docs:
        q_emb = openai.Embedding.create(input=query, model="text-embedding-3-small")
        q_vec = np.array(q_emb["data"][0]["embedding"])
        sims = [np.dot(d["embedding"], q_vec) for d in docs]
        best = docs[int(np.argmax(sims))]
        st.subheader(f"Best match: {best['name']}")
        st.write(best["text"][:500] + ("..." if len(best["text"]) > 500 else ""))
        try:
            summ = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": f"Summarize the following text:\n\n{best['text']}"}]
            )
            st.subheader("Summary")
            st.write(summ.choices[0].message["content"])
        except Exception as e:
            st.error(f"Summary failed: {e}")
