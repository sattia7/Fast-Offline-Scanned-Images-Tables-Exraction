from src.agents.image_agent import ImageAgent
from src.agents.vlm_agent import VLMAgent
from src.agents.validator_agent import ValidatorAgent
from src.agents.retry_agent import RetryAgent
from src.agents.qc_agent import QCAgent

image_agent = ImageAgent()
vlm_agent = VLMAgent()
validator = ValidatorAgent()
retry_agent = RetryAgent()
qc_agent = QCAgent()

def preprocess_node(state):
    state.image = image_agent.run(state.image)
    return state

def vlm_node(state):
    result = vlm_agent.run(state.image)
    state.table = result["table"]
    return state

def validate_node(state):
    state.valid = validator.run(state.table)
    return state

def retry_node(state):
    state.image = retry_agent.run(state.image)
    return state

def qc_node(state):
    qc_agent.run(state.table)
    return state

def store_node(state):
    return state
