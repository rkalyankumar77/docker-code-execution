# Code Execution Engine

The crux or the heart of the remote code execution engine for the online judge is in this project (main.py) file.

## Further thoughts

1. Create REST API (FastAPI) to accept code submissions

2. Create a pool of containers & LRU/LFU cache for the code execution containers

3. Create a code execution scheduler on top of LRU/LFU cache

4. [Good to have] UI Frontend for code submission

5. [Good to have] Store the code submissions per user

6. [Good to have] Handle user authentication/authorization and track code submissions

7. [Good to have] Use test execution framework for matching input & output from the code submitted
