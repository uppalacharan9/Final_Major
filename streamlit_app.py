import os
import streamlit as st
from file_checker import checkFile
def main():
        st.markdown(
            f"""
            <style>
            .reportview-container {{
                background-size: cover;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
st.title("A Strategy for Effective Detection of Malware")
st.markdown("""
Malwares can wreak havoc on a computer and its network. Hackers use it to steal passwords, delete files and render computers inoperable. A malware infection can cause many problems that affect daily operation and the long-term security of your company..""")
st.subheader("Check yourself:-")

file = st.file_uploader("Upload a file to check for malwares:", accept_multiple_files=True)
if len(file):
    with st.spinner("Checking..."):
        for i in file:
            open('malwares/tempFile', 'wb').write(i.getvalue())
            legitimate = checkFile("malwares/tempFile")
            os.remove("malwares/tempFile")
            if legitimate:
                st.write(f"File {i.name} seems *LEGITIMATE*!")
            else:
                st.markdown(f"File {i.name} is probably a **MALWARE**!!!")
if __name__ == "__main__":
    main()
