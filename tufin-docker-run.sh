#!/bin/bash

# Define variables
IMAGE_NAME="tufin-app"
INPUT_DIR="$(pwd)/input"
OUTPUT_DIR="$(pwd)/output"
INPUT_FILE="coalesce_input.csv"
OUTPUT_FILE="coalesce_output.txt"

# Create input and output directories if they don't exist
mkdir -p "$INPUT_DIR"
mkdir -p "$OUTPUT_DIR"

# Check if the input file exists in the input directory
if [ ! -f "$INPUT_DIR/$INPUT_FILE" ]; then
  echo "Input file not found in $INPUT_DIR. Please ensure $INPUT_FILE is present."
  exit 1
fi

# Build the Docker image
echo "Building Docker image..."
docker build -t "$IMAGE_NAME" .

# Run the Docker container
echo "Running Docker container..."
docker run -v "$INPUT_DIR:/usr/src/app/data" -v "$OUTPUT_DIR:/output" "$IMAGE_NAME" > "$OUTPUT_DIR/$OUTPUT_FILE"

# Print the output file content
echo "Processing complete. Output written to $OUTPUT_DIR/$OUTPUT_FILE"
cat "$OUTPUT_DIR/$OUTPUT_FILE"
