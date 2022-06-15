import base64
from io import BytesIO

from matplotlib import pyplot as plt


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer)
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_plot(x, titulo, ):
    plt.switch_backend('AGG')
    plt.figure(figsize=(6, 6))
    plt.title(titulo)
    plt.pie(x, autopct='%1.2f%%', labels=x.index.tolist())
    plt.legend(loc="best")
    graph = get_graph()
    return graph
