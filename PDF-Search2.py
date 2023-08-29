import os
import streamlit as st
import zipfile

def main():
    st.title("PDF Downloader")

    pdf_folder = "D:\Execute Program"
    target_name = "IPF"

    pdf_files = [file for file in os.listdir(pdf_folder) if file.lower().endswith(".pdf") and target_name.lower() in file.lower()]

    if not pdf_files:
        st.write("No PDFs found with the specified name.")
        return

    st.write("Select PDFs to download:")

    # Create a dictionary to store PDF selection status
    pdf_selection = {pdf: False for pdf in pdf_files}

    # Display list of PDFs with checkboxes
    for pdf in pdf_files:
        pdf_selection[pdf] = st.checkbox(f"{pdf}", pdf_selection[pdf])

    # Create a list of selected PDFs
    selected_pdfs = [pdf for pdf, selected in pdf_selection.items() if selected]

    # Download selected PDFs
    if selected_pdfs:
        # Create a combined zip file for the selected PDFs
        if st.button("Download Selected PDFs"):
            zip_filename = "selected_pdfs.zip"
            zip_path = os.path.join(os.path.expanduser("~"), "Downloads", zip_filename)
            with st.spinner("Creating zip file..."):
                with zipfile.ZipFile(zip_path, "w") as zip_file:
                    for pdf in selected_pdfs:
                        pdf_path = os.path.join(pdf_folder, pdf)
                        zip_file.write(pdf_path, os.path.basename(pdf_path))
            st.success(f"[Download Zip File]({zip_path})")

if __name__ == "__main__":
    main()
