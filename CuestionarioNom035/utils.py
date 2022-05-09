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

def get_plot(x,titulo,colors,legends):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10, 10))
    plt.title(titulo)
    plt.pie(x, colors=colors,autopct='%1.2f%%')
    plt.legend(legends, loc='best')
    graph = get_graph()
    return graph