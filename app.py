from src.the_langgraph.workflow import Workflow
inputs = {"question": "How did the rise of television in the 1950s impact the film industry?"}
app = Workflow().app
app.invoke(input=inputs)