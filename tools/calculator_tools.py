#here the calculator tool will be created which will be used by the agent

# from langchain.tools import tool

# class CalculatorTools():
#     @tool("Make a calculation")
#     def calculate(operation):
#         """Useful to perform any mathematical calculations, like sum, minus, multiplication, division etc. The input to this tool should be a mathematical expression, a couple examples are '20*7' or '5000/2*10'
#         """
#         try:
#             return eval(operation)
#         except SyntaxError:
#             return "Error: Invalid syntax in mathematical expression"



        
### under the hood, this is the code functionality which is making the above template work
# from pydantic import BaseModel, Field
# from langchain.tools import tool

# #define a Pydantic model for the tool's input parameters
# class CalculationInput(BaseModel):
#     operation: str = Field(..., description = "The mathematical operation to perform")
#     factor : float = Field(..., description = "A factor by which to multiply the result of the operation" )

# #use the tool decorator with the args_schema parameter pointing to the Pydantic model
# @tool("perform_calculation", args_schema=CalculationInput, return_direct = True)
# def perform_calculation(operation : str, factor : float) -> str:
#     """
#     Performs a specified mathematical operation and multiples the result to the given factor.
#     Parameters:
#     -operation(str): A String representing a mathematical operation(eg., "10+5")
#     -factor(float) : A factor by which to multiply the result to the operation
#     Returns :
#     - A String representation of the calculation result.
#     """
#     # Perform the calculation 
#     result = eval(operation)*factor

#     #return the result as a string 
#     return f"The result of {operation} multiplied by the {factor} is {result}"

