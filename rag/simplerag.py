from langchain_community.document_loaders import TextLoader

#loading documents from text file
loader = TextLoader("speech.txt")
text_documents = loader.load()
# print(text_documents)

import os
from dotenv import load_dotenv
load_dotenv()

#for loading data from web
from langchain_community.document_loaders import WebBaseLoader
import bs4
loader_web = WebBaseLoader(web_paths =("https://lilianweng.github.io/posts/2023-06-23-agent/",),
                           bs_kwargs=dict(parse_only=bs4.SoupStrainer(
                         class_=("post-title","post-content","post-header")

                     )))
text_documents1 = loader_web.load()
print(text_documents1)

#load data via pdf
from langchain_community.document_loaders import PyPDFLoader
loader2 = PyPDFLoader('attention.pdf')
docs=loader.load()

## split the text
from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap =200)
documents = text_splitter.split_documents(docs)

#embeddings 
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
embeddings = OllamaEmbeddings()

db = Chroma.from_documents(documents[:20],embeddings)

query = "Who are the authors of attention is all you need?"
retireved_results=db.similarity_search(query)
print(retireved_results[0].page_content)






