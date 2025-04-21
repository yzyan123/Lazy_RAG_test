from lazyllm import Document, Retriever

doc = Document("Lazy_RAG_test/rag/dataset")
seperator = '\n' + '='*200 + '\n'
retriever = Retriever(
    doc,
    group_name='CoarseChunk',
    similarity="bm25_chinese",
    topk=6,
    output_format="content",
    join=seperator
)
res = retriever("关于航班取消的法律条文")
print(res)