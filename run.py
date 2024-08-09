from src.the_langgraph.workflow import Workflow
import chainlit as cl

@cl.on_chat_start
def handle_chat_start():
    print("A new chat session has started!")

@cl.on_message
async def handle_user_message(message: cl.Message):
    """
    This function is called every time a user inputs a message in the UI.
    It processes the input through the Langgraph workflow and sends the response.

    Args:
        message: The user's message.

    Returns:
        None.
    """
    # Create a Workflow instance
    langgraph_workflow = Workflow()

    # Prepare the input for the Langgraph workflow
    workflow_inputs = {"question": message.content}

    # Invoke the Langgraph workflow
    workflow_results = langgraph_workflow.app.invoke(input=workflow_inputs)

    # Extract specific outputs from the Langgraph workflow results
    analysis_output = workflow_results.get('analysis_output')
    research_output = workflow_results.get('research_output')

    # Format the outputs for the final response
    formatted_response = (
        f"Research Movie Results:\n{research_output}\n\n"
        f"Analysis Movie Results:\n{analysis_output}"
    )

    # Send the final response to the user
    response_message = await cl.Message(content=formatted_response).send()
    await response_message.update()

# Run the Chainlit app
if __name__ == "__main__":
    cl.run()
