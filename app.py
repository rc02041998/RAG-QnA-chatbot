from langchain_docling import DoclingLoader

FILE_PATH = "data/BidIFB#03A3974.pdf"

loader = DoclingLoader(file_path=FILE_PATH)
documents = loader.load()
with open("output.txt", "w", encoding="utf-8") as f:
    for doc in documents:
        f.write(doc.page_content)
        f.write("\n" + "-"*80 + "\n") 
