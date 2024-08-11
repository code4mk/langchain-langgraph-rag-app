def invoke_workflow():
  from src.the_langgraph.workflow import Workflow
  inputs = {"question": "How did the rise of television in the 1950s impact the film industry?"}
  app = Workflow().app

  abc = app.invoke(input=inputs)
  print( f'question: {abc.get("question")}')
  print( f'final asnwer (analysis): {abc.get("analysis_output")}')


def stream_workflow():
  from src.the_langgraph.workflow import Workflow

  inputs = {"question": "How did the rise of television in the 1950s impact the film industry?"}
  app = Workflow().app

  # Assuming the app.stream() method directly supports yielding streaming responses
  for response_chunk in app.stream(input=inputs):
      print(response_chunk)
      
invoke_workflow()
#stream_workflow()

# import asyncio
# from src.the_langgraph.workflow import Workflow

# async def main():
#     inputs = {"question": "How did the rise of television in the 1950s impact the film industry?"}
#     app = Workflow().app

#     # Using async for to iterate over the streaming response
#     # async for response_chunk in app.astream(input=inputs, stream_mode="values"):
#     #     print(response_chunk)
        
#     async for response_chunk in app.astream(input=inputs, stream_mode="updates"):
#       for node, values in response_chunk.items():
#         print(f"Receiving update from node: '{node}'")
#         print(values)
#         print("\n\n")

# # Run the async main function
# asyncio.run(main())



