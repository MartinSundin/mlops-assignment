
exec uv run python -m vllm.entrypoints.openai.api_server \
    --model "$MODEL" \
    --host 0.0.0.0 \
    --port 8000 \
    --gpu-memory-utilization 0.95 \
    --max-model-len 150000

- Necessary to not max out the memory of the GPU.

- I added an instructive prompt to turn the question into a valid sql query. A more advanced version would have been to perform RAG to include the relevant columns into the question.