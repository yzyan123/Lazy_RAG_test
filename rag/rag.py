import lazyllm
from lazyllm import Document, Retriever


def rag():
    documents = Document("lazyllm_yzy/Lazy_RAG_test/rag/dataset")
    seperator = '\n' + '='*200 + '\n'
    retriever = Retriever(doc=documents,
                          group_name="CoarseChunk",
                          similarity="bm25_chinese",
                          topk=1,
                          output_format="content",
                          join=seperator
                          )
    retriever.start()

    prompt = ('You will act as an AI question-answering assistant and complete a dialogue task.'  
            'In this task, you need to provide your answers based on the given context and questions.')
    llm = lazyllm.OnlineChatModule(source='deepseek').prompt(lazyllm.ChatPrompter(instruction=prompt, extra_keys=['context_str']))

    query = "航班延误或取消的相关法律法规\n"
    res = llm({"query": query, "context_str": retriever(query=query)})
    print(f"With RAG Answer:\n{res}")


if __name__ == "__main__":
    rag()
    