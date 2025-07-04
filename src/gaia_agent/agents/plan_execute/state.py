from typing import Optional, List, Tuple, Annotated
from langgraph.graph import MessagesState
import operator

# Define the state type with annotations
class AgentState(MessagesState):
    system_message: str
    last_ai_message: str
    question: str
    final_answer: str
    plan: List[str]
    past_steps: Annotated[List[Tuple], operator.add]
    error: Optional[str]

class AgentStateInput(MessagesState):
    system_message: str
    question: str

class AgentStateOutput(MessagesState):
    final_answer: str
    error: Optional[str]