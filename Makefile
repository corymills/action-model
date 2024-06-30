run_executor:
	docker run -p 8085:8085 llmactions

build_executor:
	docker build --rm -f "containers/Dockerfile" -t llmactions:latest .