from langgraph.graph import StateGraph
from src.graph.states import PipelineState
from src.graph.nodes import *

def build_graph():
    graph = StateGraph(PipelineState)

    graph.add_node("preprocess", preprocess_node)
    graph.add_node("vlm", vlm_node)
    graph.add_node("validate", validate_node)
    graph.add_node("retry", retry_node)
    graph.add_node("qc", qc_node)
    graph.add_node("store", store_node)

    graph.set_entry_point("preprocess")

    graph.add_edge("preprocess", "vlm")
    graph.add_edge("vlm", "validate")
    graph.add_conditional_edges("validate",
        lambda s: "store" if s.valid else "retry"
    )
    graph.add_edge("retry", "vlm")
    graph.add_edge("store", "qc")

    return graph.compile()
